"""read energyplus results databases"""
import argparse
import contextlib
import csv
import io
import re
import sqlite3

from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

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
    """sql exploration
    to identify the periods : main run, design day(s)"""
    with sqlite3.connect(db) as con:
        rows = con.execute("""
            SELECT
                EnvironmentPeriodIndex,
                EnvironmentName
            FROM EnvironmentPeriods
        """).fetchall()
    for row in rows:
        print(row)


def table_info(db, table_name):
    """fetch table info"""
    with sqlite3.connect(db) as con:
        return con.execute(
            f"PRAGMA table_info({table_name})"
        ).fetchall()


def energyplus_date(y, mo, d, h, mi,
    tz_name="Europe/Paris",
    mode="human"
):
    """Manage EnergyPlus date/time."""
    tz = ZoneInfo(tz_name)
    # EnergyPlus peut utiliser 24:00 pour la fin de journée.
    dt = datetime(y, mo, d, h % 24, mi, tzinfo=tz)
    if h == 24:
        dt += timedelta(days=1)
    return dt if mode=="human" else int(dt.timestamp())


def fetch(con, name, key, config):
    """fetch datas related to name and key"""
    date_field = "t.Year, t.Month, t.Day, t.Hour, t.Minute"
    rows = con.execute(f"""
        SELECT
            {date_field},
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
        dt = energyplus_date(y, mo, d, h, mi)
        dates.append(dt)
    values = [value for *_, value in rows]
    return dates, values


def get_dictionary_indexes(con, variables):
    """Return dictionary indexes for requested variables."""
    if not variables:
        return {}
    conditions = []
    params = []
    for variable in variables:
        conditions.append(
            "(Name = ? AND KeyValue = ?)"
        )
        params.extend([
            variable["name"],
            variable["key"],
        ])
    query = f"""
        SELECT
            ReportDataDictionaryIndex,
            Name,
            KeyValue
        FROM ReportDataDictionary
        WHERE {" OR ".join(conditions)}
    """
    rows = con.execute(query, params).fetchall()
    return {
        (name, key): index
        for index, name, key in rows
    }


def fetch_many(con, config,
    tz_name="Europe/Paris",
    mode="human"
):
    """Fetch several EnergyPlus variables sharing the same dates."""
    variables = [
        variable
        for thema in config["variables"].values()
        for variable in thema
    ]
    indexes = get_dictionary_indexes(con, variables)
    if not indexes:
        return { "dates": [] }
    index_to_variable = {
        index: variable
        for variable, index in indexes.items()
    }
    placeholders = ", ".join(
        "?" for _ in index_to_variable
    )
    query = f"""
        SELECT
            r.TimeIndex,
            t.Year,
            t.Month,
            t.Day,
            t.Hour,
            t.Minute,
            r.ReportDataDictionaryIndex,
            r.Value
        FROM ReportData r
        JOIN Time t
            ON r.TimeIndex = t.TimeIndex
        JOIN EnvironmentPeriods e
            ON t.EnvironmentPeriodIndex =
               e.EnvironmentPeriodIndex
        WHERE r.ReportDataDictionaryIndex IN ({placeholders})
          AND e.EnvironmentName = ?
        ORDER BY r.TimeIndex
    """
    params = list(index_to_variable)
    params.append(config["environment"])
    rows = con.execute(query, params).fetchall()
    data = {
        variable: []
        for variable in indexes
    }
    data["dates"] = []
    last_time_index = None
    for time_index, y, mo, d, h, mi, dict_index, value in rows:
        # A single date per TimeIndex
        if time_index != last_time_index:
            dt = energyplus_date(y, mo, d, h, mi, tz_name=tz_name, mode=mode)
            data["dates"].append(dt)
            last_time_index = time_index
        variable = index_to_variable[dict_index]
        data[variable].append(value)
    return data


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
        datas = {db_name : {} for db_name in cons}
        for db_name, con in cons.items():
            datas[db_name] = fetch_many(con, config)
        fig, ax = plt.subplots(nb, 1, sharex=True, squeeze=False)
        ax = ax[:, 0]
        for i, (thema_name, thema) in enumerate(config["variables"].items()):
            for variable in thema:
                name = variable["name"]
                key = variable["key"]
                identifier = (name, key)
                label = variable.get("label", f"{name} — {key}")
                for db_name, con in cons.items():
                    db_label = label if db_name == "main" else f"{db_name} {label}"
                    dates = datas[db_name]["dates"]
                    values = datas[db_name][identifier]
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
        data = fetch_many(con, config)
        dates = data["dates"]
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
                identifier = (name, key)
                values = data[identifier]
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


def safe_filename(name):
    """Return a filesystem-safe filename."""
    return re.sub(r'[<>:"/\\|?*]', "_", name)


def export_variables_csv_chunk(db, config,
    output_dir="exports",
    tz_name="Europe/Paris",
    max_size_mb=1.5,
):
    """Export variables declared in the yaml to CSV files.
    One CSV file per variable, split into chunks if needed.
    First column: Unix timestamp (seconds).
    Second column: value.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    max_size = int(max_size_mb * 1_000_000)
    with sqlite3.connect(db) as con:
        data = fetch_many(
            con,
            config,
            tz_name=tz_name,
            mode="timestamp",
        )
        dates = data["dates"]
        for _, thema in config["variables"].items():
            for variable in thema:
                name = variable["name"]
                key = variable["key"]
                identifier = (name, key)
                values = data[identifier]
                filename = safe_filename(name)
                # Export in chunks.
                chunk_index = 1
                current_size = 0
                csvfile = None
                writer = None
                def open_chunk(index):
                    """open chunk"""
                    nonlocal csvfile, writer, current_size
                    if csvfile is not None:
                        csvfile.close()
                    if index == 1:
                        filepath = output_dir / f"{filename}.csv"
                    else:
                        filepath = output_dir / (
                            f"{filename}_{index:03d}.csv"
                        )
                    csvfile = filepath.open(
                        "w",
                        newline="",
                        encoding="utf-8",
                    )
                    writer = csv.writer(csvfile)
                    writer.writerow(["timestamp", "value"])
                    csvfile.flush()
                    current_size = csvfile.tell()
                    print(f"Exporting: {filepath}")
                try:
                    open_chunk(chunk_index)
                    for date, value in zip(dates, values):
                        # Generate the CSV row in memory
                        # to determine its encoded size.
                        buffer = io.StringIO(newline="")
                        row_writer = csv.writer(buffer)
                        row_writer.writerow([date, value])
                        row = buffer.getvalue()
                        row_size = len(
                            row.encode("utf-8")
                        )
                        # Start a new chunk before writing
                        # if the size limit would be exceeded.
                        if (
                            current_size + row_size > max_size
                            and current_size > 0
                        ):
                            chunk_index += 1
                            open_chunk(chunk_index)
                        writer.writerow([date, value])
                        csvfile.flush()
                        current_size += row_size
                finally:
                    if csvfile is not None:
                        csvfile.close()


def main():
    """main"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--plot", action="store_true")
    parser.add_argument("--explore", action="store_true")
    parser.add_argument("--csv", action="store_true")
    parser.add_argument("--yml", default="sql.yaml")
    parser.add_argument("--tz", default="Europe/Paris")
    parser.add_argument("--mb", default=2)
    parser.add_argument("--table_info")

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

    if args.table_info:
        print(args.table_info)
        for database in databases.values():
            for line in table_info(database, args.table_info):
                print(line)
        return

    if args.csv:
        for database in databases.values():
            export_variables_csv_chunk(
                database,
                sql_config,
                tz_name=args.tz,
                max_size_mb=args.mb
            )
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
