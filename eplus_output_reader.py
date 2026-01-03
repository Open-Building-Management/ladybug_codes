"""synthetize an eplus simulation output"""
import csv
from dataclasses import dataclass

from matplotlib import pyplot as plt

from src.vis_tools import (
    Pattern, Exclude,
    CSV_FOLDER, EPLUSOUT,
    ZONE, OUTDOOR, RATE, SCHEDULES, COP,
    choose_folder, choose_in_list,
    init_single_column_plt, plot, get_diff,
    CopConfig, get_cop_points, bin_cop_by_outdoor_temp
)

DT = "deltaT"

@dataclass(frozen=True)
class Rule:
    """rules"""
    includes: tuple[tuple[str, ...], ...]
    excludes: tuple[str, ...] = ()

RULES: dict[str, Rule] = {
    ZONE: Rule(
        includes=(
            (Pattern.ZONE_TEMP,),
        ),
    ),
    OUTDOOR: Rule(
        includes=(
            (Pattern.OUTDOOR,),
        ),
    ),
    RATE: Rule(
        includes=(
            (Pattern.RATE,),
        ),
    ),
    SCHEDULES: Rule(
        includes=(
            (Pattern.SCHEDULE,),
        ),
        excludes=(
            Exclude.THERMOSTAT_SCHEDULE,
            Exclude.ALWAYS,
        ),
    ),
    COP: Rule(
        includes=(
            (Pattern.HEATING_RATE, Pattern.ELECTRICITY_RATE),
            (Pattern.DX,),
        )
    ),
    "setPoint": Rule(
        includes=(
            ("NODE 6",),
        )
    ),
    DT: Rule(
        includes=(
            (Pattern.INLET, Pattern.OUTLET,),
        )
    )
}


folder = choose_folder(CSV_FOLDER)

with open(f"{folder}/{EPLUSOUT}", "r", encoding="utf-8") as eplus_result:
    eplus_data = list(csv.DictReader(eplus_result, delimiter=','))

eplus_labels: dict[str, list[str]] = {name: [] for name in RULES}

for key in eplus_data[0].keys():
    for name, rule in RULES.items():
        # AND entre groupes
        if not all(
            any(p in key for p in group)
            for group in rule.includes
        ):
            continue
        # exclusions
        if any(e in key for e in rule.excludes):
            continue
        eplus_labels[name].append(key)

nbg = sum(1 for group in eplus_labels.values() if len(group) > 0)

if eplus_labels[COP]:
    schedule_label = choose_in_list(eplus_labels[SCHEDULES])
    outdoor_label = choose_in_list(eplus_labels[OUTDOOR])
    cop_config = CopConfig(
        cop_labels=eplus_labels[COP],
        schedule_label=schedule_label,
        outdoor_label=outdoor_label
    )
    outdoor_filtered, cops_filtered, all_cops = get_cop_points(
        eplus_data,
        cop_config,
        min_plr=0.15,
        p_nominal=43150,
        setpoint=20
    )
    nbg += 1

fig, axes = init_single_column_plt(nbg)

i = 0
for key, group in eplus_labels.items():
    if len(group):
        if key == DT:
            diff = get_diff(eplus_data, group[-1], group[0])
            axes[i].plot(diff, label=DT)
            axes[i].legend()
        else:
            plot(group, axes[i], eplus_data)
        i += 1

if eplus_labels[COP]:
    axes[-1].plot(all_cops, label=COP)
    axes[-1].legend()

print(eplus_labels)

plt.show()

if eplus_labels[COP]:
    bins, cop_med, cop_p25, cop_p75 = bin_cop_by_outdoor_temp(
        outdoor_filtered,
        cops_filtered,
        bin_width=1.0,
    )
    plt.figure(figsize=(8, 5))
    plt.scatter(outdoor_filtered, cops_filtered, s=5, alpha=0.15, label="Instant COP")
    plt.plot(bins, cop_med, "-o", color="black", label="Median COP")
    plt.fill_between(bins, cop_p25, cop_p75, alpha=0.3, label="IQR")
    plt.xlabel("Température extérieure [°C]")
    plt.ylabel("COP chauffage DX")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
