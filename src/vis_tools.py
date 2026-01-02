"""visualisation helpers"""
from dataclasses import dataclass
from enum import StrEnum
import math
import os
import sys
from typing import Sequence

from matplotlib import pyplot as plt
import numpy as np


CSV_FOLDER = "csv"
EPLUSOUT = "eplusout.csv"
ZONE = "zone"
OUTDOOR = "outdoor"
RATE = "rate"
SCHEDULES = "schedules"
COP = "cop"

class Pattern(StrEnum):
    """patterns to track"""
    ZONE_TEMP = ":Zone Air Temperature"
    OUTDOOR = ":Site Outdoor Air"
    SCHEDULE = ":Schedule"
    ENERGY = "Energy"
    RATE = "Rate"
    ELECTRICITY_RATE = "Electricity Rate"
    HEATING_RATE = "Heating Rate"
    DX = "DX"
    FAN = "Fan"


class Exclude(StrEnum):
    "excluded patterns"
    THERMOSTAT_SCHEDULE = "THERMOSTAT SCHEDULE"
    ALWAYS = "ALWAYS"


def init_single_column_plt(nb_graphes) :
    """Initialise un graphe a une seule colonne"""
    plt.rcParams.update({'font.size':6})
    return plt.subplots(
        nrows=nb_graphes,
        ncols=1,
        figsize=(15,6),
        sharex=True,
        gridspec_kw={'hspace': 0.5}
    )


def get_values(data, label):
    """extract a column with a given column label"""
    result = []
    try:
        result = [
            float(row[label])
            for row in data
        ]
    except ValueError as e:
        print(e)
    return result


@dataclass(frozen=True)
class CopConfig:
    """labels to use for cop calculation"""
    cop_labels: Sequence[str]
    schedule_label: str
    outdoor_label: str


def get_cop_points(
    data,
    config: CopConfig,
    min_plr=0.15, # PART LOAD RATIO
    p_nominal=43150,
    setpoint=20.0,
):
    """COP horaire avec COP=0 hors chauffage"""
    cops = []
    outdoor = []

    for row in data:
        # température extérieure toujours stockée
        t_out = float(
            row[config.outdoor_label]
        )
        outdoor.append(t_out)

        # hors plage de chauffage
        if float(row[config.schedule_label]) != setpoint:
            cops.append(0.0)
            continue

        # puissance électrique
        elec = sum(
            float(row[col])
            for col in config.cop_labels
            if Pattern.ELECTRICITY_RATE in col
            if row.get(col) not in ("", None)
        )

        # puissance thermique
        heating = sum(
            float(row[col])
            for col in config.cop_labels
            if Pattern.HEATING_RATE in col
            if row.get(col) not in ("", None)
        )

        # filtres physiques
        if elec <= 0:
            cops.append(0.0)
            continue

        if heating < min_plr * p_nominal:
            cops.append(0.0)
            continue

        cops.append(heating / elec)

    mask = np.array(cops) > 0
    return np.array(outdoor)[mask], np.array(cops)[mask], cops


def bin_cop_by_outdoor_temp(
    outdoor,
    cops,
    bin_width=2.0,
    min_points=10,
):
    """COP médian par bin de température extérieure"""
    bins = np.arange(
        math.floor(outdoor.min()),
        math.ceil(outdoor.max()) + bin_width,
        bin_width,
    )

    bin_centers = (bins[:-1] + bins[1:]) / 2

    cop_median = []
    cop_p25 = []
    cop_p75 = []

    for i in range(len(bins) - 1):
        mask = (outdoor >= bins[i]) & (outdoor < bins[i + 1])

        if np.sum(mask) >= min_points:
            cop_median.append(np.median(cops[mask]))
            cop_p25.append(np.percentile(cops[mask], 25))
            cop_p75.append(np.percentile(cops[mask], 75))
        else:
            cop_median.append(np.nan)
            cop_p25.append(np.nan)
            cop_p75.append(np.nan)

    return bin_centers, np.array(cop_median), np.array(cop_p25), np.array(cop_p75)


def plot(labels, ax, data):
    """plot on an axis"""
    for label in labels:
        serie = get_values(data, label)
        if len(serie) > 0:
            ax.plot(
                serie,
                label=label
            )
    ax.legend()


def choose_in_list(liste):
    """choix parmi une liste."""
    for n, d in enumerate(liste, start=1):
        print(f"  {n}. {d}")
    while True:
        try:
            choix = int(input("\nChoisis un numéro : "))
            if 1 <= choix <= len(liste):
                return liste[choix - 1]
            print("Numéro invalide, réessaie.")
        except ValueError:
            print("Il faut entrer un nombre.")


def choose_folder(base_path):
    """choix du dossier de projet."""
    sous_dossiers = [
        d for d in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, d))
    ]
    if not sous_dossiers:
        print(f"Aucun sous-dossier dans '{base_path}'.")
        sys.exit(1)

    print(f"\nSous-dossiers disponibles dans '{base_path}' :")
    return os.path.join(base_path, choose_in_list(sous_dossiers))
