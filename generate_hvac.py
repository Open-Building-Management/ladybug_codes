""""hvac generator"""
import os

from idfhub.hvac import (
    PLANT, DEMAND,
    EPApi, EPValues,
    add_plantloop,
    add_baseboard,
    create_branch,
    Branches,
    plantloop_split_mix
)
# autocompletion use
from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import (
    Timestep, SizingperiodDesignday, Runperiod, Version, Simulationcontrol,
    Building, Globalgeometryrules,
    Scheduletypelimits,
    ThermostatsetpointDualsetpoint, ZonecontrolThermostat,
    SizingParameters, SizingZone, SizingPlant,
    ZonehvacEquipmentlist, ZonehvacEquipmentconnections,
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
    OutputVariabledictionaryType,
    OutputTableSummaryreportsType, OutputcontrolTableStyleType,
    OutputVariableType, OutputSqliteType,
    FluidpropertiesGlycolconcentrationType,
)

from idfhub.helpers.common import get_logger

from idfhub.common import (
    idf,
    BUILDING_NAME, PROJECT_NAME,
    CONF, ZONES, LOOPS,
    EQUIPMENTS, SENSORS
)

from idfhub.hvac24_1_0 import (
    loops, equipments,
    consigne_cool, consigne_heat,
    ground_temperature,
    vertical_geoexchanger,
    pump,
    water_to_water_heatpump,
    water_law, constant_set_point,
    adjust_nodes_branch, generate_operation_list,
    control_manager,
    constant_schedule, basic_compact_schedule
)

FORMAT = (
    '%(asctime)s | %(levelname).1s | '
    '%(name)s:%(lineno)d | '
    '%(message)s'
)

LOGGER = get_logger(format=FORMAT)


MESSAGE = f"idf hvac injection for energyplus {idf.idd_version}"
LOGGER.info(MESSAGE)

EP_SIM_PATH = "ep_simulations"
SOIL_LOOP = "soil_loop"
WATER_HEATING = "water_heating"
WATER_LAW = "water_law"
CONSTANT = "constant"
BOREHOLE = "borehole"
PUMP = "pump"
HPWTW = "hpwtw"


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
)

for zone in ZONES:
    ZonecontrolThermostat(
        idf,
        **ZonecontrolThermostatType(
            Name=f"{zone}_thermostat",
            Zone_or_ZoneList_Name=zone,
            Control_Type_Schedule_Name=control_type_schedule.Name,
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
    if loop == SOIL_LOOP:
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
        plant_loop = add_plantloop(idf, loop, 35, -5)
        plant_loop.Fluid_Type = "UserDefinedFluidType"
        plant_loop.User_Defined_Fluid_Type = glycol_water_30.Name
        loops[loop] = plant_loop
        SizingPlant(
            idf,
            **SizingPlantType(
                Plant_or_Condenser_Loop_Name=loop,
                Loop_Type="Cooling",
                Design_Loop_Exit_Temperature=12,
                Loop_Design_Temperature_Difference=5,
                Sizing_Option="NonCoincident",
                Zone_Timesteps_in_Averaging_Window=1,
            )
        )
    if WATER_HEATING in loop:
        heating_loop = add_plantloop(idf, loop, 100, 0)
        loops[loop] = heating_loop
        SizingPlant(
            idf,
            **SizingPlantType(
                Plant_or_Condenser_Loop_Name=loop,
                Loop_Type="Heating",
                Design_Loop_Exit_Temperature=70,
                Loop_Design_Temperature_Difference=10,
                Sizing_Option="NonCoincident",
                Zone_Timesteps_in_Averaging_Window=1,
            )
        )
        # à supprimer
        heating_loop_branches = Branches(loop)

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
    if BOREHOLE in equipment_name:
        ground_temperature()
        borehole = vertical_geoexchanger(equipment_name)
        equipments[equipment_name] = borehole
        continue
    if HPWTW in equipment_name:
        hpwtw = water_to_water_heatpump(equipment_name)
        equipments[equipment_name] = hpwtw

for sensor, conf in SENSORS.items():
    if conf.get("active", 1):
        control_manager(sensor, conf)

for loop in LOOPS:
    setpoint = CONF[loop].get("setpoint")
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
    generate_operation_list(loop)


#------------------------------------------------------------------------------
# EMISSION SYSTEMS
#------------------------------------------------------------------------------
baseboards = {}
baseboard_branches = {}
for zone in ZONES:
    baseboards[zone] =  add_baseboard(idf, zone)
    baseboard_branches[zone] = create_branch(
        idf,
        name = f"{heating_loop_branches.demand_branch} {zone}",
        objects = [baseboards[zone]],
        sides = [None]
    )

plantloop_split_mix(
    idf=idf,
    plantloop=heating_loop,
    side=EPApi.DEMAND_SIDE,
    branches=list(baseboard_branches.values())
)

#------------------------------------------------------------------------------
# ZONE EQUIPMENTS DECLARATION
#------------------------------------------------------------------------------
equipment_list = {}
for zone in ZONES:
    equipment_list[zone] = ZonehvacEquipmentlist(
        idf,
        **ZonehvacEquipmentlistType(
            Name=f"{zone} equipment list",
            Zone_Equipment_1_Name=baseboards[zone].Name,
            Zone_Equipment_1_Object_Type=baseboards[zone].key,
            Zone_Equipment_1_Cooling_Sequence=1,
            Zone_Equipment_1_Heating_or_NoLoad_Sequence=1
        )
    )
    ZonehvacEquipmentconnections(
        idf,
        **ZonehvacEquipmentconnectionsType(
            Zone_Name=zone,
            Zone_Conditioning_Equipment_List_Name=equipment_list[zone].Name,
            Zone_Air_Node_Name=f"{zone} air node"
        )
    )


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

def add_variable(name):
    """add a variable to the ep output"""
    OutputVariable(
        idf,
        **OutputVariableType(
            Key_Value="*",
            Variable_Name=name,
            Reporting_Frequency="Timestep"
        )
    )
# tout ce tuning des variables de sortie peut être raisonnablement fait avec IDFEditor
add_variable("Site Outdoor Air Drybulb Temperature")
add_variable("Zone Air Temperature")
add_variable("Zone Thermostat Heating Setpoint Temperature")

for equipment_name in EQUIPMENTS:
    if BOREHOLE in equipment_name:
        add_variable("Ground Heat Exchanger Heat Transfer Rate")
        add_variable("Ground Heat Exchanger Inlet Temperature")
        add_variable("Ground Heat Exchanger Outlet Temperature")
    if HPWTW in equipment_name:
        add_variable("Heat Pump Load Side Outlet Temperature")
        add_variable("Heat Pump Load Side Inlet Temperature")
        add_variable("Heat Pump Source Side Outlet Temperature")
        add_variable("Heat Pump Source Side Inlet Temperature")
        add_variable("Heat Pump Source Side Mass Flow Rate")
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
