"""
Analyse les conditions estivales d'un fichier EPW pour préparer
des objets EnergyPlus SizingPeriod:DesignDay.

Événements analysés :
1. Heure de température sèche maximale (Hot Design Day).
2. Heure de point de rosée maximal (Humid Design Day).

Pour chaque événement, le script extrait :
- date et heure ;
- dry-bulb et dewpoint concomitants ;
- minimum journalier de dry-bulb ;
- amplitude journalière de dry-bulb ;
- humidité relative ;
- ratio d'humidité.

Usage :
    python analyze_epw.py fichier.epw
"""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
import pandas as pd

OUTPUT_FILE = Path("design_days.txt")

# Colonnes du format EPW, indexées à partir de zéro.
COL_YEAR = 0
COL_MONTH = 1
COL_DAY = 2
COL_HOUR = 3
COL_MINUTE = 4
COL_DRY_BULB = 6
COL_DEW_POINT = 7
COL_RELATIVE_HUMIDITY = 8
COL_PRESSURE = 9

# Pression atmosphérique standard, en Pa, utilisée uniquement
# lorsque la pression du fichier EPW n'est pas exploitable.
STANDARD_PRESSURE = 101325.0


def saturation_vapor_pressure(temp_c: float | pd.Series) -> float | pd.Series:
    """Pression de vapeur saturante sur eau, en Pa."""
    return 610.94 * np.exp(17.625 * temp_c / (temp_c + 243.04))


def saturation_vapor_pressure_ashrae(
    temp_c: npt.ArrayLike,
) -> npt.NDArray[np.float64]:
    """Pression de vapeur saturante selon l'ASHRAE, en Pa.
    Args:
        temp_c: Température en °C, scalaire ou tableau.
    Returns:
        Pression de vapeur saturante en Pa, sous forme de tableau NumPy.
    """
    t = np.asarray(temp_c, dtype=np.float64) + 273.15  # Kelvin
    ln_p = np.empty_like(t)

    # Glace : T <= 0.01 °C
    ice = t <= 273.16
    ti = t[ice]
    ln_p[ice] = (
        -5.6745359e3 / ti
        + 6.3925247
        - 9.677843e-3 * ti
        + 6.2215701e-7 * ti**2
        + 2.0747825e-9 * ti**3
        - 9.484024e-13 * ti**4
        + 4.1635019 * np.log(ti)
    )

    # Eau liquide : T > 0.01 °C
    water = ~ice
    tw = t[water]
    ln_p[water] = (
        -5.8002206e3 / tw
        + 1.3914993
        - 4.8640239e-2 * tw
        + 4.1764768e-5 * tw**2
        - 1.4452093e-8 * tw**3
        + 6.5459673 * np.log(tw)
    )

    return np.exp(ln_p)


def humidity_ratio(pressure: float, dew_point: float) -> float:
    """humidity ratio en kg vapeur/kg air sec"""
    p_v = saturation_vapor_pressure_ashrae(dew_point)
    denominator = pressure - p_v
    return (
        0.621945 * p_v / denominator
        if denominator > 0
        else float("nan")
    )


def read_epw(path: Path) -> pd.DataFrame:
    """Lit les données météorologiques horaires d'un fichier EPW."""
    # Les 8 premières lignes constituent l'en-tête EPW.
    df = pd.read_csv(
        path,
        skiprows=8,
        header=None,
        usecols=[
            COL_YEAR,
            COL_MONTH,
            COL_DAY,
            COL_HOUR,
            COL_MINUTE,
            COL_DRY_BULB,
            COL_DEW_POINT,
            COL_RELATIVE_HUMIDITY,
            COL_PRESSURE,
        ],
    )

    df.columns = [
        "year",
        "month",
        "day",
        "hour",
        "minute",
        "dry_bulb",
        "dew_point",
        "relative_humidity",
        "pressure",
    ]

    # Dans le format EPW, l'heure 1 correspond à 00:00–01:00,
    # l'heure 24 à 23:00–24:00.
    # On associe les données à la fin de leur intervalle.
    df["timestamp"] = pd.to_datetime(
        {
            "year": df["year"],
            "month": df["month"],
            "day": df["day"],
        },
        errors="coerce",
    ) + pd.to_timedelta(df["hour"], unit="h")

    # Les valeurs manquantes EPW sont notamment codées par 99.9 °C.
    df.loc[df["dry_bulb"] >= 99.0, "dry_bulb"] = np.nan
    df.loc[df["dew_point"] >= 99.0, "dew_point"] = np.nan

    # Pression EPW en Pa ; certaines données peuvent être manquantes.
    df.loc[
        (df["pressure"] <= 0) | (df["pressure"] > 120000),
        "pressure",
    ] = np.nan

    df["pressure"] = df["pressure"].fillna(STANDARD_PRESSURE)

    df["date"] = df["timestamp"].dt.date

    if df["dry_bulb"].notna().sum() == 0:
        raise ValueError("Aucune température sèche exploitable dans cet EPW.")

    if df["dew_point"].notna().sum() == 0:
        raise ValueError("Aucun point de rosée exploitable dans cet EPW.")

    return df


def analyze_event(
    df: pd.DataFrame,
    variable: str,
    event_name: str,
) -> dict[str, object]:
    """Analyse la journée contenant le maximum de la variable choisie."""
    valid = df.dropna(subset=[variable])

    event_idx = valid[variable].idxmax()
    event = df.loc[event_idx]
    event_date = event["date"]

    day = df.loc[df["date"] == event_date]
    day_valid = day.dropna(subset=["dry_bulb"])

    db_min = float(day_valid["dry_bulb"].min())
    db_max = float(day_valid["dry_bulb"].max())
    db_range = db_max - db_min

    dry_bulb = float(event["dry_bulb"])
    dew_point = float(event["dew_point"])
    pressure = float(event["pressure"])
    rh = float(event["relative_humidity"])

    hr = humidity_ratio(pressure, dew_point)

    # Heure EPW d'origine : 1 à 24.
    epw_hour = int(event["hour"])

    return {
        "event": event_name,
        "date": event_date,
        "hour_epw": epw_hour,
        "timestamp": event["timestamp"],
        "dry_bulb": dry_bulb,
        "dew_point": dew_point,
        "daily_db_min": db_min,
        "daily_db_max": db_max,
        "daily_db_range": db_range,
        "relative_humidity": rh,
        "humidity_ratio_g_per_kg": hr * 1000.0,
        "pressure": pressure,
        "hours_in_day": len(day),
        "valid_db_hours": int(day["dry_bulb"].notna().sum()),
    }


def print_event(result: dict[str, object]) -> None:
    """Affiche les résultats d'un événement."""

    output = f"""
    {'=' * 68}
    {result['event']}
    {'=' * 68}
    Date                  : {result['date']}
    Heure EPW             : {result['hour_epw']}
    Horodatage            : {result['timestamp']}
    Dry-bulb concomitante : {result['dry_bulb']:.2f} °C
    Dewpoint concomitant  : {result['dew_point']:.2f} °C
    Minimum journalier DB : {result['daily_db_min']:.2f} °C
    Maximum journalier DB : {result['daily_db_max']:.2f} °C
    Amplitude journalière : {result['daily_db_range']:.2f} K
    Humidité relative     : {result['relative_humidity']:.1f} %
    Rapport d'humidité    : {result['humidity_ratio_g_per_kg']:.2f} g/kg d'air sec
    Pression atmosphérique: {result['pressure']:.0f} Pa
    """
    with OUTPUT_FILE.open("a", encoding="utf-8") as f:
        f.write(output)
    print(output)

    if result["dew_point"] > result["dry_bulb"]:
        print(
            "ATTENTION : le point de rosée dépasse la température sèche. "
            "Vérifier les données."
        )


def plot_relative_humidity(df: pd.DataFrame) -> None:
    """Compare l'humidité relative de l'EPW à celle recalculée."""
    valid = df.dropna(
        subset=["dry_bulb", "dew_point", "relative_humidity", "pressure"]
    ).copy()

    p_ws_db = saturation_vapor_pressure_ashrae(valid["dry_bulb"])
    p_ws_dp = saturation_vapor_pressure_ashrae(valid["dew_point"])

    valid["rh_calculated"] = 100.0 * p_ws_dp / p_ws_db

    # Écarter les lignes présentant des valeurs psychrométriques impossibles.
    valid.loc[
        (valid["dew_point"] > valid["dry_bulb"])
        | (valid["rh_calculated"] > 100.0),
        "rh_calculated",
    ] = np.nan

    fig, ax = plt.subplots(figsize=(14, 5))
    ax.plot(
        valid["relative_humidity"] - valid["rh_calculated"],
        label="écart valeur EPW vs valeur calculée"
    )
    ax.plot(
        p_ws_db - saturation_vapor_pressure(valid["dry_bulb"]),
        label="écart ashrae/magnus p_ws_db"
    )
    ax.plot(
        p_ws_dp - saturation_vapor_pressure(valid["dew_point"]),
        label= "écart ashrae/magnus p_ws_dp"
    )
    ax.plot(
        valid["rh_calculated"],
        label="Humidité relative calculée"
    )
    ax.plot(
        valid["relative_humidity"],
        label="Humidité relative EPW"
    )
    ax.set(
        title="Contrôle qualité",
        ylabel="Humidité relative (%)",
    )
    ax.set_ylim(0, 105)
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    plt.show()



def main() -> None:
    """main"""
    parser = argparse.ArgumentParser(
        description="Analyse les conditions de dimensionnement estival d'un EPW."
    )
    parser.add_argument("epw", type=Path, help="Chemin du fichier EPW")
    parser.add_argument(
        "--csv",
        type=Path,
        help="Chemin facultatif pour exporter les deux résultats en CSV",
    )
    args = parser.parse_args()

    df = read_epw(args.epw)

    hot = analyze_event(
        df,
        variable="dry_bulb",
        event_name="HOT DESIGN DAY — maximum annuel de dry-bulb",
    )

    humid = analyze_event(
        df,
        variable="dew_point",
        event_name="HUMID DESIGN DAY — maximum annuel de dewpoint",
    )

    header = f"""
    Fichier : {args.epw}
    Nombre d'heures : {len(df)}
    Période : {df['timestamp'].min()} à {df['timestamp'].max()}
    """
    with OUTPUT_FILE.open("a", encoding="utf-8") as f:
        f.write(header)
    print(header)
    print_event(hot)
    print_event(humid)
    plot_relative_humidity(df)

    if args.csv:
        pd.DataFrame([hot, humid]).to_csv(
            args.csv,
            index=False,
            encoding="utf-8",
        )
        print(f"\nRésultats exportés vers : {args.csv}")


if __name__ == "__main__":
    main()
