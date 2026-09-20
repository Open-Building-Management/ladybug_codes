"""read energyplus results databases"""
import argparse
import contextlib
from collections import defaultdict
import sqlite3
from datetime import datetime, timedelta

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import yaml


def list_variables(db):
    """list variables stored in the sql"""
    with sqlite3.connect(db) as con:
        rows = con.execute("""
            SELECT DISTINCT
                KeyValue,
                Name,
                Units
            FROM ReportDataDictionary
            ORDER BY Name, KeyValue
        """)

        for key, name, units in rows:
            print(f"{name:50} | {key:40} | {units:10}")


def explore(db):
    """sql exploration"""
    with sqlite3.connect(db) as con:
        rows = con.execute("""
            SELECT
                EnvironmentPeriodIndex,
                EnvironmentName
            FROM EnvironmentPeriods
        """).fetchall()

    for row in rows:
        print(row)


def fetch(con, name, key, config):
    """fetch datas related to name and key"""
    rows = con.execute("""
        SELECT
            t.Year, t.Month, t.Day, t.Hour, t.Minute,
            r.Value
        FROM ReportData r
        JOIN ReportDataDictionary d
            ON r.ReportDataDictionaryIndex =
               d.ReportDataDictionaryIndex
        JOIN Time t
            ON r.TimeIndex = t.TimeIndex
        JOIN EnvironmentPeriods e
            ON t.EnvironmentPeriodIndex =
               e.EnvironmentPeriodIndex
        WHERE d.Name = ?
          AND d.KeyValue = ?
          AND e.EnvironmentName = ?
        ORDER BY t.TimeIndex
    """, (name, key, config["environment"])).fetchall()
    if not rows:
        print(f"WARNING: no data for {name} / {key}")
        return None, None
    dates = []
    for y, mo, d, h, mi, _ in rows:
        dt = datetime(y, mo, d, h % 24, mi)
        if h == 24:
            dt += timedelta(days=1)
        dates.append(dt)
    values = [value for *_, value in rows]
    return dates, values


def multidb_plot_variables(dbs: dict[str, str], config: dict):
    """Plot variables declared in the yaml for multiple sql databases.
    permits to compare 2 scenarios"""
    nb = len(config["variables"])
    if nb < 1:
        return
    with contextlib.ExitStack() as stack:
        cons = {
            db_name: stack.enter_context(sqlite3.connect(db_path))
            for db_name, db_path in dbs.items()
        }
        fig, ax = plt.subplots(nb, 1, sharex=True, squeeze=False)
        ax = ax[:, 0]
        for i, (thema_name, thema) in enumerate(config["variables"].items()):
            for variable in thema:
                name = variable["name"]
                key = variable["key"]
                label = variable.get("label", f"{name} — {key}")
                for db_name, con in cons.items():
                    db_label = label if db_name == "main" else f"{db_name} {label}"
                    dates, values = fetch(con, name, key, config)
                    ax[i].plot(dates, values, label=db_label)
            ax[i].set_xlabel("date")
            ax[i].set_ylabel(thema_name)
            ax[i].grid(True)
            ax[i].legend()
    fig.tight_layout()
    plt.show()


def plot_variables(db, config, overlay_years=True):
    """Plot variables declared in the yaml.
    For a single database !
    overlay mode to overlap successive years
    TODO : prise en compte des années bisextiles
    """
    nb = len(config["variables"])
    if nb < 1:
        return
    fig, ax = plt.subplots(
        nb,
        1,
        sharex=True,
        squeeze=False,
    )
    ax = ax[:, 0]
    with sqlite3.connect(db) as con:
        for i, (thema_name, thema) in enumerate(
            config["variables"].items()
        ):
            for variable in thema:
                name = variable["name"]
                key = variable["key"]
                label = variable.get(
                    "label",
                    f"{name} — {key}",
                )
                dates, values = fetch(
                    con,
                    name,
                    key,
                    config,
                )
                if not overlay_years:
                    ax[i].plot(
                        dates,
                        values,
                        label=label,
                    )
                    continue
                # Regroupement par année
                yearly_data = defaultdict(
                    lambda: ([], [])
                )
                for date, value in zip(dates, values):
                    year = date.year
                    yearly_data[year][0].append(
                        date.replace(year=2000)
                    )
                    yearly_data[year][1].append(value)
                for year, (year_dates, year_values) in (
                    yearly_data.items()
                ):
                    ax[i].plot(
                        year_dates,
                        year_values,
                        label=f"{label} — {year}",
                    )
            ax[i].set_xlabel("date")
            ax[i].set_ylabel(thema_name)
            ax[i].grid(True)
            ax[i].legend()
    if overlay_years:
        for axis in ax:
            axis.xaxis.set_major_locator(
                mdates.MonthLocator()
            )
            axis.xaxis.set_major_formatter(
                mdates.DateFormatter("%b")
            )
    fig.tight_layout()
    plt.show()


def main():
    """main"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--plot", action="store_true")
    parser.add_argument("--explore", action="store_true")
    parser.add_argument("--yml", default="sql.yaml")
    args = parser.parse_args()
    with open(args.yml, encoding="utf-8") as f:
        sql_config = yaml.safe_load(f)
    databases = {}
    if isinstance(sql_config.get('name'), str):
        database = f"{sql_config.get('path')}/{sql_config.get('name')}"
        databases["main"] = database
    if isinstance(sql_config.get('name'), dict):
        for key, value in sql_config.get('name').items():
            database = f"{sql_config.get('path')}/{value}"
            databases[key] = database

    if args.list:
        for database in databases.values():
            list_variables(database)
        return

    if args.plot:
        if len(databases) == 1:
            plot_variables(
                databases["main"],
                sql_config,
                overlay_years=sql_config.get('overlay', False)
            )
            return
        multidb_plot_variables(databases, sql_config)
        return

    if args.explore:
        for database in databases.values():
            explore(database)


if __name__ == "__main__":
    main()
