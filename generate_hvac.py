""""hvac generator"""
import os

from idfhub.hvac import (
    PLANT, DEMAND,
    EPApi, EPValues,
    add_plantloop,
    add_baseboard,
    create_pipe
)
# autocompletion use
from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import (
    Timestep, SizingperiodDesignday, Runperiod, Version, Simulationcontrol,
    Building, Globalgeometryrules,
    Scheduletypelimits,
    ThermostatsetpointDualsetpoint, ZonecontrolThermostat,
    SizingParameters, SizingZone, SizingPlant,
    ZonehvacEquipmentlist, ZonehvacEquipmentconnections,
    OutputEnergymanagementsystem,
    OutputVariabledictionary,
    OutputTableSummaryreports, OutputcontrolTableStyle,
    OutputVariable, OutputSqlite,
    FluidpropertiesGlycolconcentration,FluidpropertiesGlycolconcentrationMeta
)
from idfhub.idf_autocomplete.v24_1_0.idf_types_short import (
    TimestepType, SizingperiodDesigndayType, RunperiodType, VersionType, SimulationcontrolType,
    BuildingType, GlobalgeometryrulesType,
    ScheduletypelimitsType,
    ThermostatsetpointDualsetpointType, ZonecontrolThermostatType,
    SizingParametersType, SizingZoneType, SizingPlantType,
    ZonehvacEquipmentlistType, ZonehvacEquipmentconnectionsType,
    OutputEnergymanagementsystemType,
    OutputVariabledictionaryType,
    OutputTableSummaryreportsType, OutputcontrolTableStyleType,
    OutputVariableType, OutputSqliteType,
    FluidpropertiesGlycolconcentrationType,
)

from idfhub.common import (
    idf, get_logger,
    BUILDING_NAME, PROJECT_NAME,
    CONF, ZONES, LOOPS,
    EQUIPMENTS,
)

from idfhub.hvac24_1_0 import (
    loops, equipments, resolve_side,
    pump,
    water_law, constant_set_point,
    adjust_nodes_branch, operation_list_scheme,
    constant_schedule, basic_compact_schedule,
    gas_boiler,
)

from idfhub.hvac24_1_0_geoexchanger import (
    ground_temperature,
    vertical_geoexchanger,
)

from idfhub.hvac24_1_0_heatpump import (
    water_to_water_heatpump,
    air_to_water_heatpump_eir
)

from idfhub.hvac24_1_0_secondary import initialise_sensors, control, compute
from idfhub.hvac24_1_0_exchanger import heat_exchanger


FORMAT = (
    '%(asctime)s | %(levelname).1s | '
    '%(name)s:%(lineno)d | '
    '%(message)s'
)

LOGGER = get_logger(log_format=FORMAT)


MESSAGE = f"idf hvac injection for energyplus {idf.idd_version}"
LOGGER.info(MESSAGE)

EP_SIM_PATH = "ep_simulations"
SOIL = "soil"
WATER_HEATING = "water_heating"
WATER_LAW = "water_law"
CONSTANT = "constant"
BOREHOLE = "borehole"
PUMP = "pump"
PIPE = "pipe"
HP = "hp"
HPWTW = "hpwtw"
HPATW = "hpatw"
BOILER = "boiler"
EXCHANGER = "HX"

def add_variable(name, key="*"):
    """add a variable to the ep output"""
    OutputVariable(
        idf,
        **OutputVariableType(
            Key_Value=key,
            Variable_Name=name,
            Reporting_Frequency="Timestep"
        )
    )

Timestep(
    idf,
    **TimestepType(
        Number_of_Timesteps_per_Hour=6
    )
)
Version(idf, **VersionType())

Simulationcontrol(
    idf,
    **SimulationcontrolType(
        Do_Zone_Sizing_Calculation="Yes",
        Do_Plant_Sizing_Calculation="Yes",
        Do_System_Sizing_Calculation="Yes",
        Do_HVAC_Sizing_Simulation_for_Sizing_Periods="Yes",
        Maximum_Number_of_HVAC_Sizing_Simulation_Passes=2
    )
)

SizingperiodDesignday(
    idf,
    **SizingperiodDesigndayType(
        Name="design_day",
        Month=1,
        Day_of_Month=1,
        Day_Type=EPValues.WINTER_DESIGN_DAY,
        Maximum_DryBulb_Temperature=-5,
        Wind_Speed=0,
        Wind_Direction=0,
        Wetbulb_or_DewPoint_at_Maximum_DryBulb=-10,
        Humidity_Condition_Type="DewPoint"
    )
)

Runperiod(
    idf,
    **RunperiodType(
        Name="run period",
        Begin_Month=1,
        Begin_Day_of_Month=1,
        End_Month=12,
        End_Day_of_Month=31,
        Use_Weather_File_Holidays_and_Special_Days="No",
        Use_Weather_File_Daylight_Saving_Period="No"
    )
)
SizingParameters(
    idf,
    **SizingParametersType(
        Heating_Sizing_Factor=1.25,
        Cooling_Sizing_Factor=1.15
    )
)
Building(
    idf,
    **BuildingType(
        Name="CeremaCF",
        North_Axis=CONF.get("North_Axis", 0),
        Loads_Convergence_Tolerance_Value=0.04,
        Temperature_Convergence_Tolerance_Value=0.4
    )
)
Globalgeometryrules(
    idf,
    **GlobalgeometryrulesType(
        Starting_Vertex_Position="UpperLeftCorner",
        Vertex_Entry_Direction="Counterclockwise",
        Coordinate_System="Relative"
    )
)

#------------------------------------------------------------------------------
# Schedules and Thermostats
# 20°C chauffage et 25°C raffraichissement
#------------------------------------------------------------------------------

# generate_geometry nécessite un schedule constant appelé Always On utilisant Fractional ????
fractional_typelimits = Scheduletypelimits(
    idf,
    **ScheduletypelimitsType(
        Name="Fractional",
        Lower_Limit_Value=0,
        Upper_Limit_Value=1,
        Numeric_Type=EPValues.CONTINUOUS,
    )
)

#consigne_heat = constant_schedule(20)
consigne_heat = basic_compact_schedule(20, schedule_name="heating_schedule")
consigne_cool = constant_schedule(25)
#consigne_cool = basic_compact_schedule(25, schedule_name="cooling_schedule")

zone_thermostat = ThermostatsetpointDualsetpoint(
    idf,
    **ThermostatsetpointDualsetpointType(
        Name="zone_thermostat",
        Heating_Setpoint_Temperature_Schedule_Name=consigne_heat.Name,
        Cooling_Setpoint_Temperature_Schedule_Name=consigne_cool.Name
    )
)

# Control types are integers:
# 0 - Uncontrolled (floating, no thermostat),
# 1 = ThermostatSetpoint:SingleHeating,
# 2 = ThermostatSetpoint:SingleCooling,
# 3 = ThermostatSetpoint:SingleHeatingOrCooling,
# 4 = ThermostatSetpoint:DualSetpoint
control_typelimits = Scheduletypelimits(
    idf,
    **ScheduletypelimitsType(
        Name="control_types",
        Lower_Limit_Value=0,
        Upper_Limit_Value=4,
        Numeric_Type=EPValues.DISCRETE
    )
)

control_type_schedule = basic_compact_schedule(
    4,
    schedule_name="control_type_schedule",
    typelimits=control_typelimits
)

control_type_constant_schedule = constant_schedule(
    4,
    name= "AlwaysDualSetpoint",
    typelimits=control_typelimits
)

for zone in ZONES:
    ZonecontrolThermostat(
        idf,
        **ZonecontrolThermostatType(
            Name=f"{zone}_thermostat",
            Zone_or_ZoneList_Name=zone,
            Control_Type_Schedule_Name=control_type_constant_schedule.Name,
            Control_1_Object_Type=zone_thermostat.key,
            Control_1_Name=zone_thermostat.Name
        )
    )

#------------------------------------------------------------------------------
# End Of Schedules and Thermostats
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# Plant Loops
#------------------------------------------------------------------------------
for loop in LOOPS:
    conf = CONF.get(loop, {})
    if SOIL in loop:
        liquid_name = "eau glycol 30pourcent"
        glycol_water_30 = idf.getobject(
            FluidpropertiesGlycolconcentrationMeta.idf_name,
            liquid_name
        )
        if glycol_water_30 is None:
            glycol_water_30 = FluidpropertiesGlycolconcentration(
                idf,
                **FluidpropertiesGlycolconcentrationType(
                    Name=liquid_name,
                    Glycol_Type="PropyleneGlycol",
                    Glycol_Concentration=0.3
                )
            )
        plant_loop = add_plantloop(idf, loop, conf)
        plant_loop.Fluid_Type = "UserDefinedFluidType"
        plant_loop.User_Defined_Fluid_Type = glycol_water_30.Name
        loops[loop] = plant_loop
        add_variable("Plant Supply Side Cooling Demand Rate", key=loop)
    if WATER_HEATING in loop:
        heating_loop = add_plantloop(idf, loop, conf)
        loops[loop] = heating_loop
    add_variable("Plant Supply Side heating Demand Rate", key=loop)

    SizingPlant(
        idf,
        **SizingPlantType(
            Plant_or_Condenser_Loop_Name=loop,
            Loop_Type=conf.get("Loop_Type", EPValues.HEATING).split("_")[0],
            Design_Loop_Exit_Temperature=conf.get("Design_Loop_Exit_Temperature", 70),
            Loop_Design_Temperature_Difference=conf.get("Loop_Design_Temperature_Difference", 10),
            Sizing_Option="NonCoincident",
            Zone_Timesteps_in_Averaging_Window=1,
        )
    )

def basic_zone_sizing(zone_name: str):
    """basic zone sizing"""
    return SizingZone(
        idf,
        **SizingZoneType(
            Zone_or_ZoneList_Name=zone_name,
            Zone_Cooling_Design_Supply_Air_Humidity_Ratio=0.008,
            Zone_Heating_Design_Supply_Air_Humidity_Ratio=0.008,
            Zone_Heating_Design_Supply_Air_Temperature=40,
        )
    )
for zone in ZONES:
    basic_zone_sizing(zone)

for equipment_name in EQUIPMENTS:
    if PUMP in equipment_name:
        pump_type = "constant"
        if "variable" in equipment_name:
            pump_type = "variable"
        equipments[equipment_name] = pump(equipment_name, pump_type=pump_type)
        continue
    if PIPE in equipment_name:
        pipe = create_pipe(
            idf,
            name=equipment_name,
            inlet_node_name=f"{equipment_name}_inlet_node",
            outlet_node_name=f"{equipment_name}_outlet_node"
        )
        equipments[equipment_name] = pipe
        continue
    if BOREHOLE in equipment_name:
        ground_temperature()
        borehole = vertical_geoexchanger(equipment_name)
        equipments[equipment_name] = borehole
        continue
    if HPWTW in equipment_name:
        hpwtw = water_to_water_heatpump(equipment_name)
        equipments[equipment_name] = hpwtw
        continue
    if HPATW in equipment_name:
        hpatw = air_to_water_heatpump_eir(equipment_name)
        equipments[equipment_name] = hpatw
        continue
    if BOILER in equipment_name:
        boiler = gas_boiler(equipment_name)
        equipments[equipment_name] = boiler
        continue
    if EXCHANGER in equipment_name:
        exchanger = heat_exchanger(equipment_name)
        equipments[equipment_name] = exchanger
        continue
    if "baseboards" in equipment_name:
        try:
            zone = equipment_name.split("_")[1]
        except IndexError:
            zone = None
        if zone in ZONES:
            baseboards = add_baseboard(idf, zone)
            equipments[equipment_name] = baseboards
            #----------------------------------------------------------------
            # ZONE EQUIPMENTS DECLARATION
            #----------------------------------------------------------------
            zone_equipment_list = ZonehvacEquipmentlist(
                idf,
                **ZonehvacEquipmentlistType(
                    Name=f"{zone} equipment list",
                    Zone_Equipment_1_Name=baseboards.Name,
                    Zone_Equipment_1_Object_Type=baseboards.key,
                    Zone_Equipment_1_Cooling_Sequence=1,
                    Zone_Equipment_1_Heating_or_NoLoad_Sequence=1
                )
            )
            ZonehvacEquipmentconnections(
                idf,
                **ZonehvacEquipmentconnectionsType(
                    Zone_Name=zone,
                    Zone_Conditioning_Equipment_List_Name=zone_equipment_list.Name,
                    Zone_Air_Node_Name=f"{zone}_air_node"
                )
            )

sensors = initialise_sensors(CONF.get("sensors", {}))
process = CONF.get("process", {})
compute(process)

controls = CONF.get("controls", {})
for control_conf in controls.values():
    sensor_name = control_conf.get("sensor")
    if not sensor_name:
        LOGGER.error("mention a sensor !")
        continue
    if sensor_name not in sensors and sensor_name not in process:
        LOGGER.error("unknown sensor")
        continue
    machines = control_conf.get("pilot", [])
    if isinstance(machines, str):
        machines = [machines]
    for machine in machines:
        if machine in equipments:
            LOGGER.debug(
                "Adding control on %s through sensor %s",
                machine, sensor_name
            )
            control(machine, sensor_name, control_conf)


for loop in LOOPS:
    setpoint = CONF[loop].get("setpoint", {})
    branches_descr: dict[str, list[str]]
    branches_descr = CONF[loop].get("branches", {})
    if WATER_LAW in setpoint:
        water_law(loop, setpoint)
    if CONSTANT in setpoint:
        constant_set_point(loop, setpoint)
    for loop_side in [PLANT, DEMAND]:
        if loop_side in branches_descr:
            adjust_nodes_branch(
                loop,
                loop_side=loop_side,
                branches_descr=branches_descr
            )
    operation_list_scheme(loop)

# machine level setpoints management
# this can only to be done after all nodes and branches adjustments
for loop in loops:
    setpoints = CONF[loop].get("setpoints", [])
    machines = CONF[loop].get("operation", [])
    for i, obj_name in enumerate(machines):
        try:
            setpoint = setpoints[i]
        except IndexError:
            setpoint = None
        if setpoint is not None:
            side = resolve_side(obj_name, PLANT)
            equipment = equipments[obj_name]
            outlet = equipment[f"{side}_{EPApi.OUTLET_NODE_NAME}"]
            water_law(loop, setpoint, outlet)

#------------------------------------------------------------------------------
# OUTPUT CONFIGURATION
#------------------------------------------------------------------------------
OutputVariabledictionary(
    idf,
    **OutputVariabledictionaryType(
        Key_Field="IDF",
        Sort_Option="Unsorted"
    )
)
OutputTableSummaryreports(idf, **OutputTableSummaryreportsType(Report_1_Name="AllSummary"))
OutputcontrolTableStyle(idf, **OutputcontrolTableStyleType(Column_Separator="HTML"))
OutputEnergymanagementsystem(idf, **OutputEnergymanagementsystemType(
    Actuator_Availability_Dictionary_Reporting="Verbose",
    Internal_Variable_Availability_Dictionary_Reporting="Verbose",
    EMS_Runtime_Language_Debug_Output_Level="None"
))


# tout ce tuning des variables de sortie peut être raisonnablement fait avec IDFEditor
add_variable("Site Outdoor Air Drybulb Temperature")
add_variable("Zone Air Temperature")
add_variable("Zone Thermostat Heating Setpoint Temperature")
if CONF.get("verbose"):
    add_variable("System Node Setpoint Temperature")
    add_variable("System Node Temperature")

for equipment_name in EQUIPMENTS:
    if BOREHOLE in equipment_name:
        add_variable("Ground Heat Exchanger Heat Transfer Rate")
        add_variable("Ground Heat Exchanger Inlet Temperature")
        add_variable("Ground Heat Exchanger Outlet Temperature")
        add_variable("Ground Heat Exchanger Average Borehole Temperature")
    if HP in equipment_name:
        suffix = "Heat Pump"
        add_variable(f"{suffix} Load Side Outlet Temperature")
        add_variable(f"{suffix} Load Side Inlet Temperature")
        add_variable(f"{suffix} Source Side Outlet Temperature")
        add_variable(f"{suffix} Source Side Inlet Temperature")
        add_variable(f"{suffix} Source Side Mass Flow Rate")
        add_variable(f"{suffix} Electricity Rate")
        add_variable(f"{suffix} Load Side Heat Transfer Rate")
        add_variable(f"{suffix} Source Side Heat Transfer Rate")
    if BOILER in equipment_name:
        add_variable("Boiler Heating Rate")
        add_variable("Boiler Inlet Temperature")
        add_variable("Boiler Outlet Temperature")
        add_variable("Boiler Part Load Ratio")
    if EXCHANGER in equipment_name:
        add_variable("Fluid Heat Exchanger Heat Transfer Rate")
        add_variable("Fluid Heat Exchanger Loop Supply Side Mass Flow Rate")
        add_variable("Fluid Heat Exchanger Loop Supply Side Inlet Temperature")
        add_variable("Fluid Heat Exchanger Loop Supply Side Outlet Temperature")
        add_variable("Fluid Heat Exchanger Loop Demand Side Mass Flow Rate")
        add_variable("Fluid Heat Exchanger Loop Demand Side Inlet Temperature")
        add_variable("Fluid Heat Exchanger Loop Demand Side Outlet Temperature")

add_variable("Baseboard Total Heating Rate")
add_variable("Baseboard Water Inlet Temperature")
add_variable("Baseboard Water Outlet Temperature")

add_variable("Pump Mass Flow Rate")

OutputSqlite(
    idf,
    **OutputSqliteType(
        Option_Type="SimpleAndTabular"
    )
)
input("press")

if not os.path.exists(EP_SIM_PATH):
    os.mkdir(EP_SIM_PATH)
if not os.path.exists(f"{EP_SIM_PATH}/{BUILDING_NAME}"):
    os.mkdir(f"{EP_SIM_PATH}/{BUILDING_NAME}")
if not os.path.exists(f"{EP_SIM_PATH}/{BUILDING_NAME}/{PROJECT_NAME}"):
    os.mkdir(f"{EP_SIM_PATH}/{BUILDING_NAME}/{PROJECT_NAME}")

final_name = f"{EP_SIM_PATH}/{BUILDING_NAME}/{PROJECT_NAME}/{PROJECT_NAME}.idf"
idf.save(final_name)
