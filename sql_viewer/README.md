# EnergyPlus SQL viewer

This directory contains a small command-line tool to inspect and plot EnergyPlus
SQLite result files, export selected report variables, compare simulations, and
integrate power time series into energy totals.

## Requirements

Install the project dependencies from the repository root:

```bash
python -m pip install -e .
```

The `tzdata` dependency is used by Python's `zoneinfo` module, including on
Windows installations where the system timezone database may not be available.

## Configuration

Run the script from this directory, or pass the YAML file explicitly with
`--yml`. The default configuration is `sql.yaml`.

- `path`: directory containing EnergyPlus `.sql` files.
- `colors`: custom colors.
- `environment`: EnergyPlus environment to read, for example `RUN PERIOD`.
- `variables`: variables and expressions used by plots and CSV exports.
- `accumulate`: expressions that calculate an energy value for each reporting
  interval, before the values are accumulated by calendar month or year.

Entries used in `variables` and `accumulate` are defined with the EnergyPlus report `name` and `key` and an optional `label` for legending.

```yaml
outdoor_t:
  name: "Site Outdoor Air Drybulb Temperature"
  key: Environment
  label: "Outdoor Temp °C"
  
indoor_t_r1:
  name: "Zone Air Temperature"
  key: RPLUS1
  label: "RPLUS1 temp °C"

pac_elec:
  name: "Heat Pump Electricity Rate"
  key: HPWTW
  label: "HeatPump W"

pac_load_heat_transfer:
  name: "Heat Pump Load Side Heat Transfer Rate"
  key: HPWTW
  label: "HP Load heat W"

glhe_heat_rate:
  name: "Ground Heat Exchanger Heat Transfer Rate"
  key: "BOREHOLE"

soil_pump_elec:
  name: "Pump Electricity Rate"
  key: "SOIL_PUMP"
  label: "soil pump W"

pac_pump_elec:
  name: "Pump Electricity Rate"
  key: PAC_VARIABLE_PUMP
  label: "pac pump W"

zone_pump_elec:
  name: "Pump Electricity Rate"
  key: ZONE_VARIABLE_PUMP
  label: "zone pump W"

fan_rdc_elec:
  name: "Fan Coil Fan Electricity Rate"
  key: FCU_RDC
  label: "fan RDC W"

fan_rplus1_elec:
  name: "Fan Coil Fan Electricity Rate"
  key: FCU_RPLUS1
  label: "fan RPLUS1 W"
```

### Variables

The following yaml creates a graph with 3 subplots.
- The first subplot will render 2 curves of temperature (indoor and outdoor)
- The second one will calculate the COP
- The third will show cumulative stack of the auxiliary powers, as the pattern `stack`
  is used in the key name

```yaml
variables:
  temperature:
    - outdoor_t
    - indoor_t_r1

  COP: pac_load_heat_transfer / pac_elec

  stack_auxiliary_rates:
    - soil_pump_elec
    - pac_pump_elec
    - zone_pump_elec
    - fan_rdc_elec
    - fan_rplus1_elec
```

### Accumulation formulas

An accumulation formula is an arithmetic expression using the same variable
identifiers as the `variables` section. The SQL reader additionally provides
`interval_minutes`, read from the EnergyPlus `Time.Interval` column. It is the
duration of each reporting interval in minutes.

For example:

```yaml
accumulate:
  borehole_energy_GJ: glhe_heat_rate * interval_minutes * 60 * 1e-9
```

Here, the rate is in watts, the interval is converted to seconds, and the
resulting joules are converted to gigajoules. Using `Time.Interval` rather than
a fixed 3600-second factor supports timestep, hourly, and daily reporting.

The formula is evaluated for every report row. Its signed values are then
grouped by calendar period:
- `positive`: sum of positive interval energies;
- `negative`: absolute sum of negative interval energies;
- `net`: signed sum (positive plus negative).

The accumulator does not assign a physical meaning to either sign. Check the
EnergyPlus variable's sign convention against a known operating period before
interpreting the positive and negative totals as heat injection or extraction.

## Commands

The script prompts for one or more SQL files found in the configured `path`.
Use `--yml` to select another configuration file.

List available report variables:

```bash
python eplus_sql_reader.py --list
```

Explore simulation environments:

```bash
python eplus_sql_reader.py --explore
```

Inspect a SQL table schema:

```bash
python eplus_sql_reader.py --table_info Time
```

Plot configured variables:

```bash
python eplus_sql_reader.py --plot
```

Plot a multi years simulation in an overlay fashion, with consecutive years stacked :

```bash
python eplus_sql_reader.py --plot --overlay=1
```

Export configured source variables to chunked CSV files:

```bash
python eplus_sql_reader.py --csv
```

Calculate accumulated energy by month (default) or year:

```bash
python eplus_sql_reader.py --accumulate
python eplus_sql_reader.py --accumulate --period year
```

For another YAML file:

```bash
python eplus_sql_reader.py --yml path/to/sql.yaml --accumulate --period month
```

## Notes

- The selected `environment` is applied to SQL queries, so design-day
  environments are not mixed with the run period.
- Accumulation uses `Time.Interval`; it does not assume a one-hour interval.
- EnergyPlus timestamps mark the end of each reporting interval; monthly and yearly grouping uses the interval start, so the final interval at a month boundary is assigned to the month it belongs to.
- The current reader loads selected series into memory for plotting and
  accumulation. Very large databases may therefore require substantial memory.
