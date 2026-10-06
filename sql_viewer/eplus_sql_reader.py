"""read energyplus results databases"""
import argparse
import contextlib
import csv
import io
import os
import re
import sqlite3

from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import inquirer
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import yaml

from idfhub.ast_utils import get_dependencies, eval_expr


class CheckForFiles:
    """Recherche fichiers suivant extension"""
    def __init__(self, folder_path) -> None:
        """Initialize."""
        self.names: list[str] = []
        self.folder_path: str = os.path.abspath(folder_path)

    def get_names(self) -> list[str]:
        """Return list of files paths."""
        return self.names

    def path(self, name):
        """Return the path"""
        return os.path.join(self.folder_path, name)

    def filter_extension(self, ext="lite") -> None:
        """Filter files with extension ext."""
        folder_path = self.folder_path
        for name in [name for name in os.listdir(folder_path) if name not in [".",".."]]:
            full_path = self.path(name)
            if os.path.isfile(full_path) and name.split(".")[-1] == ext:
                self.names.append(name)


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


def get_dictionary_indexes(con, config):
    """Return dictionary indexes for requested variables."""
    if "variables" not in config:
        return {}
    variables = []
    for thema in config["variables"].values():
        if isinstance(thema, list):
            for variable in thema:
                variables.append(variable)
        if isinstance(thema, str):
            # we have a formula so we must get the dependencies
            variables.extend(get_dependencies(thema))
    conditions = []
    params = []
    for variable in variables:
        conditions.append(
            "(Name = ? AND KeyValue = ?)"
        )
        params.extend([
            config[variable]["name"],
            config[variable]["key"],
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
    indexes = get_dictionary_indexes(con, config)
    if not indexes:
        return {}
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
        variable: {
            "dates": [],
            "values": []
        }
        for variable in indexes
    }
    for _, y, mo, d, h, mi, dict_index, value in rows:
        dt = energyplus_date(y, mo, d, h, mi, tz_name=tz_name, mode=mode)
        variable = index_to_variable[dict_index]
        data[variable]["dates"].append(dt)
        data[variable]["values"].append(value)
    return data


def multidb_plot_variables(dbs: dict[str, str], config: dict):
    """Plot variables declared in the yaml for multiple sql databases.
    permits to compare 2 scenarios"""
    nb = len(config["variables"])
    if nb < 1:
        return
    colors = config.get("colors", {})
    with contextlib.ExitStack() as stack:
        cons = {
            db_name: stack.enter_context(sqlite3.connect(db_path))
            for db_name, db_path in dbs.items()
        }
        datas: dict[str, dict] = {db_name : {} for db_name in cons}
        for db_name, con in cons.items():
            datas[db_name] = fetch_many(con, config)
        fig, ax = plt.subplots(nb, 1, sharex=True, squeeze=False)
        if "title" in config:
            fig.suptitle(config["title"])
        ax = ax[:, 0]
        for i, (thema_name, thema) in enumerate(config["variables"].items()):
            y_label = config.get(thema_name, {}).get("label", thema_name)
            if isinstance(thema, str):
                dependencies = get_dependencies(thema)
                values_by_name: dict[str, dict] = {db_name: {} for db_name in cons}
                dates: list = []
                for dependency in dependencies:
                    name = config[dependency]["name"]
                    key = config[dependency]["key"]
                    identifier = (name, key)
                    for db_name in cons:
                        if not dates:
                            dates = datas[db_name][identifier]["dates"]
                        values_by_name[db_name][dependency] = np.array(
                            datas[db_name][identifier]["values"]
                        )
                for db_name in cons:
                    values = eval_expr(thema, values_by_name[db_name])
                    color = colors.get(db_name)
                    ax[i].plot(dates, values, label=db_name, color=color)
            if isinstance(thema, list):
                for variable in thema:
                    name = config[variable]["name"]
                    key = config[variable]["key"]
                    identifier = (name, key)
                    for db_name in cons:
                        dates = datas[db_name][identifier]["dates"]
                        values = datas[db_name][identifier]["values"]
                        ax[i].plot(dates, values, label=db_name)
            ax[i].set_xlabel("date")
            ax[i].set_ylabel(y_label)
            ax[i].grid(True)
            ax[i].legend()
    fig.tight_layout()
    plt.show()


def plot_variable(ax, dates, values, label, overlay_years=False):
    """plot a single serie on an matplotlib axe"""
    if not overlay_years:
        ax.plot(
            dates,
            values,
            label=label,
        )
        return
    # overlay mode
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
        ax.plot(
            year_dates,
            year_values,
            label=year
        )


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
    if "title" in config:
        fig.suptitle(config["title"])
    ax = ax[:, 0]
    with sqlite3.connect(db) as con:
        data = fetch_many(con, config)
        for i, (thema_name, thema) in enumerate(
            config["variables"].items()
        ):
            if isinstance(thema, str):
                dependencies = get_dependencies(thema)
                values_by_name = {}
                dates = []
                for dependency in dependencies:
                    name = config[dependency]["name"]
                    key = config[dependency]["key"]
                    identifier = (name, key)
                    if not dates:
                        dates = data[identifier]["dates"]
                    values_by_name[dependency] = np.array(
                        data[identifier]["values"]
                    )
                values = eval_expr(thema, values_by_name)
                label = config.get(thema_name, {}).get("label", thema_name)
                plot_variable(ax[i], dates, values, label=None, overlay_years=overlay_years)
                ax[i].set_ylabel(label)
            if isinstance(thema, list):
                for variable in thema:
                    name = config[variable]["name"]
                    key = config[variable]["key"]
                    label = config[variable].get(
                        "label",
                        f"{name} — {key}",
                    )
                    identifier = (name, key)
                    dates = data[identifier]["dates"]
                    values = data[identifier]["values"]
                    plot_variable(ax[i], dates, values, label, overlay_years=overlay_years)
                ax[i].set_ylabel(thema_name)
            ax[i].grid(True)
    if overlay_years:
        for axis in ax:
            axis.xaxis.set_major_locator(
                mdates.MonthLocator()
            )
            axis.xaxis.set_major_formatter(
                mdates.DateFormatter("%b")
            )
        handles, labels = ax[0].get_legend_handles_labels()
        fig.legend(
            handles,
            labels,
            loc="upper center",
            bbox_to_anchor=(0.5, 0.96),
            ncol=5,
        )
        fig.tight_layout(rect=[0, 0, 1, 0.92])
    else:
        for axis in ax:
            axis.legend()
        fig.tight_layout()
    plt.show()


def safe_filename(name):
    """Return a filesystem-safe filename."""
    return re.sub(r'[<>:"/\\|?*]', "_", name)


def open_chunk(output_dir, base_name, chunk_number):
    """open chunk"""
    filename = (
        f"{base_name}.csv"
        if chunk_number == 1
        else f"{base_name}_{chunk_number:03d}.csv"
    )
    filepath = output_dir / filename
    csvfile = filepath.open(
        "w",
        newline="",
        encoding="utf-8",
    )
    writer = csv.writer(csvfile)
    writer.writerow(["timestamp", "value"])
    print(f"Exporting: {filepath}")
    return csvfile, writer


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
        for _, thema in config["variables"].items():
            # on n'applique pas les formules, on peut faire du postprocessing dans emoncms
            dependencies = thema
            if isinstance(thema, str):
                dependencies = get_dependencies(thema)
            for variable in dependencies:
                name = config[variable]["name"]
                key = config[variable]["key"]
                identifier = (name, key)
                dates = data[identifier]["dates"]
                values = data[identifier]["values"]
                # Export in chunks.
                chunk_index = 1
                current_size = 0
                try:
                    csvfile, writer = open_chunk(
                        output_dir,
                        safe_filename(name),
                        chunk_index,
                    )
                    current_size = 0
                    for date, value in zip(dates, values):
                        buffer = io.StringIO(newline="")
                        row_writer = csv.writer(buffer)
                        row_writer.writerow([date, value])
                        row = buffer.getvalue()
                        row_size = len(row.encode("utf-8"))
                        if (
                            current_size + row_size > max_size
                            and current_size > 0
                        ):
                            csvfile.close()
                            chunk_index += 1
                            csvfile, writer = open_chunk(
                                output_dir,
                                safe_filename(name),
                                chunk_index,
                            )
                            current_size = 0
                        writer.writerow([date, value])
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
    parser.add_argument("--overlay", default=0)

    args = parser.parse_args()
    with open(args.yml, encoding="utf-8") as f:
        sql_config = yaml.safe_load(f)
    databases = {}
    sql_db_paths = CheckForFiles(
        folder_path=sql_config.get('path')
    )
    sql_db_paths.filter_extension(
        ext="sql"
    )
    remaining = sql_db_paths.get_names().copy()
    while remaining:
        answers = inquirer.prompt([
            inquirer.List(
                "file",
                message="Choose a file",
                choices=remaining,
            ),
            inquirer.Text(
                "name",
                message="Short label for legend",
            ),
        ])
        filename = answers["file"]
        databases[answers["name"]] = sql_db_paths.path(filename)
        remaining.remove(filename)

        if not remaining:
            break

        if not inquirer.confirm(
            "Add another file ?",
            default=False,
        ):
            break
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
            print(databases.values())
            plot_variables(
                next(iter(databases.values())),
                sql_config,
                overlay_years=args.overlay
            )
            return
        multidb_plot_variables(databases, sql_config)
        return

    if args.explore:
        for database in databases.values():
            explore(database)


if __name__ == "__main__":
    main()
