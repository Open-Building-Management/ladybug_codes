"""synthetize an eplus simulation output"""
import csv
from dataclasses import dataclass
from enum import StrEnum
import os
import sys
from matplotlib import pyplot as plt

CSV_FOLDER = "osm"
EPLUSOUT = "eplusout.csv"

class Pattern(StrEnum):
    """patterns to track"""
    ZONE_TEMP = ":Zone Air Temperature"
    OUTDOOR = ":Site Outdoor Air"
    SCHEDULE = ":Schedule"
    ENERGY = "Energy"
    RATE = "Rate"

class Exclude(StrEnum):
    "excluded patterns"
    THERMOSTAT_SCHEDULE = "THERMOSTAT SCHEDULE"
    ALWAYS = "ALWAYS"

@dataclass(frozen=True)
class Rule:
    """rules"""
    includes: tuple[str, ...]
    excludes: tuple[str, ...] = ()

RULES: dict[str, Rule] = {
    "zone": Rule(
        includes=(Pattern.ZONE_TEMP,),
    ),
    "outdoor": Rule(
        includes=(Pattern.OUTDOOR,),
    ),
    "rate": Rule(
        includes=(Pattern.RATE,),
    ),
    "schedules": Rule(
        includes=(Pattern.SCHEDULE,),
        excludes=(
            Exclude.THERMOSTAT_SCHEDULE,
            Exclude.ALWAYS,
        ),
    ),
}


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

def choose_folder(base_path):
    """choix du dossier de projet"""
    sous_dossiers = [
        d for d in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, d))
    ]
    if not sous_dossiers:
        print(f"Aucun sous-dossier dans '{base_path}'.")
        sys.exit(1)

    print(f"\nSous-dossiers disponibles dans '{base_path}' :")
    for n, d in enumerate(sous_dossiers, start=1):
        print(f"  {n}. {d}")

    while True:
        try:
            choix = int(input("\nChoisis un numéro : "))
            if 1 <= choix <= len(sous_dossiers):
                return os.path.join(base_path, sous_dossiers[choix - 1])
            print("Numéro invalide, réessaie.")
        except ValueError:
            print("Il faut entrer un nombre.")

folder = choose_folder(CSV_FOLDER)

with open(f"{folder}/{EPLUSOUT}", "r", encoding="utf-8") as eplus_result:
    eplus_data = list(csv.DictReader(eplus_result, delimiter=','))

eplus_labels: dict[str, list[str]] = {name: [] for name in RULES}

for key in eplus_data[0].keys():
    for name, rule in RULES.items():
        if any(p in key for p in rule.includes):
            if any(e in key for e in rule.excludes):
                continue
            eplus_labels[name].append(key)

print(eplus_labels)

fig, axes = init_single_column_plt(len(RULES))

for i, eplus_label in enumerate(eplus_labels.values()):
    plot(eplus_label, axes[i], eplus_data)

plt.show()
