""""hvac generator"""
import os

from eppy.bunch_subclass import EpBunch

from idfhub.hvac import (
    PLANT, DEMAND, SUPPLY,
    EPApi, EPValues,
    add_plantloop,
    add_baseboard,
    create_pipe
)
# autocompletion use
from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import (
    Timestep, SizingperiodDesignday, Runperiod, Version, Simulationcontrol,
    Building, Globalgeometryrules,
    SizingParameters, SizingZone, SizingPlant, SizingSystem,
    ZonehvacEquipmentconnections,
    OutputEnergymanagementsystem,
    OutputVariabledictionary,
    OutputTableSummaryreports, OutputcontrolTableStyle,
    OutputVariable, OutputSqlite,
    FluidpropertiesGlycolconcentration,FluidpropertiesGlycolconcentrationMeta,
    DesignspecificationOutdoorair,
)
from idfhub.idf_autocomplete.v24_1_0.idf_types_short import (
    TimestepType, SizingperiodDesigndayType, RunperiodType, VersionType, SimulationcontrolType,
    BuildingType, GlobalgeometryrulesType,
    SizingParametersType, SizingZoneType, SizingPlantType, SizingSystemType,
    ZonehvacEquipmentconnectionsType,
    OutputEnergymanagementsystemType,
    OutputVariabledictionaryType,
    OutputTableSummaryreportsType, OutputcontrolTableStyleType,
    OutputVariableType, OutputSqliteType,
    FluidpropertiesGlycolconcentrationType,
    DesignspecificationOutdoorairType,
)

from idfhub.common import (
    idf, get_logger,
    BUILDING_NAME, PROJECT_NAME,
    CONF, ZONES, LOOPS,
    EQUIPMENTS,
    SCHEDULES,
    RUN_PERIOD
)

from idfhub.hvac24_1_0 import (
    loops, equipments, controllers,
    schedule_typelimits,
    resolve_side,
    pump,
    water_law, constant_set_point,
    adjust_nodes_branch, operation_list_scheme,
    schedule_objects, zone_control,
    gas_boiler,
    zone_list
)
from idfhub.hvac24_1_0_airloops import add_airloop, cv_no_reheat, oa_mixer
from idfhub.hvac24_1_0_fan import fan
from idfhub.hvac24_1_0_exchanger import heat_exchanger
from idfhub.hvac24_1_0_geoexchanger import (
    ground_temperature,
    vertical_geoexchanger,
)

from idfhub.hvac24_1_0_heatpump import (
    water_to_water_heatpump,
    air_to_water_heatpump_eir
)
from idfhub.hvac24_1_0_hydronic_cooling import fcu_cooling
from idfhub.hvac24_1_0_photovoltaic import PV_plant
from idfhub.hvac24_1_0_secondary import initialise_sensors, control, compute

AIRLOOPS: list[str] = CONF.get("airloops", [])
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
FCU = "fcu"
FAN = "fan"
CV_NO_REHEAT = "cv_no_reheat"
OA_MIXER = "oa_mixer"

zone_equipments: dict[str, list] = {}
air_nodes: dict[str, dict[str, str]] = {}
air_zone_splitters: dict[str, EpBunch] = {}
air_zone_mixers: dict[str, EpBunch] = {}

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
        Name="winter_design_day",
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

SizingperiodDesignday(
    idf,
    **SizingperiodDesigndayType(
        Name="summer_design_day",
        Month=7,
        Day_of_Month=21,
        Day_Type=EPValues.SUMMER_DESIGN_DAY,
        Maximum_DryBulb_Temperature=38,
        Daily_DryBulb_Temperature_Range=10,
        Wind_Speed=2,
        Wind_Direction=180,
        Wetbulb_or_DewPoint_at_Maximum_DryBulb=18,
        Humidity_Condition_Type="DewPoint",
        Barometric_Pressure=101325
    )
)

Runperiod(
    idf,
    **RunperiodType(
        Name="run period",
        Begin_Month=RUN_PERIOD["Begin_Month"],
        Begin_Day_of_Month=RUN_PERIOD["Begin_Day_of_Month"],
        Begin_Year=RUN_PERIOD["Begin_Year"],
        End_Month=RUN_PERIOD["End_Month"],
        End_Day_of_Month=RUN_PERIOD["End_Day_of_Month"],
        End_Year=RUN_PERIOD["End_Year"],
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
        Name=CONF["building_name"],
        Terrain=CONF.get("Terrain", "Suburbs"),
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

# typelimits
schedule_typelimits(EPValues.TEMPERATURE, unit_type=EPValues.TEMPERATURE)
# honeybee (utilisé dans generate_geometry) crée un schedule constant appelé Always On
# Always On utilise le typelimits Fractional, mais honeybee ne l'initialise pas ??
schedule_typelimits(EPValues.FRACTIONAL, lower_limit=0, upper_limit=1)
# Control types are integers:
# 0 - Uncontrolled (floating, no thermostat),
# 1 = ThermostatSetpoint:SingleHeating,
# 2 = ThermostatSetpoint:SingleCooling,
# 3 = ThermostatSetpoint:SingleHeatingOrCooling,
# 4 = ThermostatSetpoint:DualSetpoint
schedule_typelimits(
    EPValues.CONTROL_TYPES,
    lower_limit=0, upper_limit=4,
    numeric_type=EPValues.DISCRETE
)


#------------------------------------------------------------------------------
# Schedules and zone controls
#------------------------------------------------------------------------------
schedules = schedule_objects(SCHEDULES)
zone_control(
    schedules,
    ZONES
)


#------------------------------------------------------------------------------
# Air Loops
#------------------------------------------------------------------------------
for airloop in AIRLOOPS:
   air_splitter, air_mixer, air_loop = add_airloop(airloop)
   loops[airloop] = air_loop
   air_zone_splitters[airloop] = air_splitter
   air_zone_mixers[airloop] = air_mixer
   SizingSystem(
       idf,
       **SizingSystemType(
           AirLoop_Name=airloop,
           Preheat_Design_Temperature=7,
           Preheat_Design_Humidity_Ratio=0.008,
           Precool_Design_Temperature=12.8,
           Precool_Design_Humidity_Ratio=0.008,
           Central_Cooling_Design_Supply_Air_Temperature=12.8,
           Central_Heating_Design_Supply_Air_Temperature=40,
       )
   )

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
            Design_Loop_Exit_Temperature=conf.get(
                "Design_Loop_Exit_Temperature", 70),
            Loop_Design_Temperature_Difference=conf.get(
                "Loop_Design_Temperature_Difference", 10),
            Sizing_Option="NonCoincident",
            Zone_Timesteps_in_Averaging_Window=1,
        )
    )

def basic_zone_sizing(zone_name: str):
    """basic zone sizing"""
    zone_conf = CONF.get(zone_name, {})
    # other methods : Flow/Person
    design_spec = DesignspecificationOutdoorair(
        idf,
        **DesignspecificationOutdoorairType(
            Name=f"{zone_name}_design_spec_oa",
            Outdoor_Air_Method=zone_conf.get(
                "Outdoor_Air_Method", "Flow/Zone"
            ),
            Outdoor_Air_Flow_per_Person=zone_conf.get(
                "Outdoor_Air_Flow_per_Person", 0.007
            ),
            Outdoor_Air_Flow_per_Zone=zone_conf.get(
                "Outdoor_Air_Flow_per_Zone", 0.1
            )
        )
    )
    # other methods : TemperatureDifference
    return SizingZone(
        idf,
        **SizingZoneType(
            Zone_or_ZoneList_Name=zone_name,
            Zone_Cooling_Design_Supply_Air_Temperature_Input_Method="SupplyAirTemperature",
            Zone_Cooling_Design_Supply_Air_Temperature=14,
            Zone_Cooling_Design_Supply_Air_Humidity_Ratio=0.008,
            Zone_Heating_Design_Supply_Air_Temperature_Input_Method="SupplyAirTemperature",
            Zone_Heating_Design_Supply_Air_Temperature=40,
            Zone_Heating_Design_Supply_Air_Humidity_Ratio=0.008,
            Design_Specification_Outdoor_Air_Object_Name=design_spec.Name,
            Cooling_Design_Air_Flow_Method=zone_conf.get(
                "Cooling_Design_Air_Flow_Method", "DesignDay"
            ),
            Cooling_Design_Air_Flow_Rate=zone_conf.get(
                "Cooling_Design_Air_Flow_Rate", 0.6
            )
        )
    )
for zone in ZONES:
    basic_zone_sizing(zone)
    zone_equipments[zone] = []
    air_nodes[zone] = {
        "air_inlet_node": f"{zone}_inlet_air_node",
        "air_exhaust_node": f"{zone}_exhaust_air_node",
        "air_return_node": f"{zone}_return_air_node",
        "air_node": f"{zone}_air_node"
    }

USE_AIR = {"return": 0, "exhaust": 0}
ground_temperature()

for equipment_name in EQUIPMENTS:
    if OA_MIXER in equipment_name:
        elements = oa_mixer(equipment_name)
        equipments[equipment_name] = elements[0]
        if len(elements) == 2:
            controllers[equipment_name] = elements[1]
        continue
    if FAN in equipment_name:
        equipments[equipment_name] = fan(equipment_name)
        continue
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
    if "PV" in equipment_name:
        PV_plant(equipment_name)
        continue
    # zone equipment
    try:
        zone = equipment_name.split("_")[-1]
    except IndexError:
        zone = None
    if zone in ZONES:
        if "baseboards" in equipment_name:
            zone_equipment = add_baseboard(idf, zone)
            equipments[equipment_name] = zone_equipment
        if CV_NO_REHEAT in equipment_name:
            air_terminal, zone_equipment = cv_no_reheat(
                equipment_name,
                zone_air_inlet_node=air_nodes[zone]["air_inlet_node"]
            )
            USE_AIR["return"] = 1
            equipments[equipment_name] = air_terminal
        if FCU in equipment_name:
            coil_cooling_water, zone_equipment = fcu_cooling(
                equipment_name,
                zone_air_inlet_node=air_nodes[zone]["air_inlet_node"],
                zone_air_exhaust_node=air_nodes[zone]["air_exhaust_node"]
            )
            USE_AIR["exhaust"] = 1
            equipments[equipment_name] = coil_cooling_water
        zone_equipments[zone].append(zone_equipment)

#----------------------------------------------------------------
# ZONE EQUIPMENTS DECLARATION
#----------------------------------------------------------------
for zone, equipment_list in zone_equipments.items():
    zone_equipment_list = zone_list(zone, equipment_list)
    connections = ZonehvacEquipmentconnections(
        idf,
        **ZonehvacEquipmentconnectionsType(
            Zone_Name=zone,
            Zone_Conditioning_Equipment_List_Name=zone_equipment_list.Name,
            Zone_Air_Node_Name=air_nodes[zone]["air_node"]
        )
    )
    if USE_AIR["return"] or USE_AIR["exhaust"]:
        connections["Zone_Air_Inlet_Node_or_NodeList_Name"]=air_nodes[zone]["air_inlet_node"]
    if USE_AIR["return"]:
        connections["Zone_Return_Air_Node_or_NodeList_Name"]=air_nodes[zone]["air_return_node"]
    if USE_AIR["exhaust"]:
        connections["Zone_Air_Exhaust_Node_or_NodeList_Name"]=air_nodes[zone]["air_exhaust_node"]

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

for loop in AIRLOOPS:
    branches_descr = CONF[loop].get("branches", {})
    if SUPPLY in branches_descr:
        adjust_nodes_branch(
            loop,
            loop_side=SUPPLY,
            branches_descr=branches_descr
        )
    terminals = CONF[loop].get("terminals", [])
    for i, name in enumerate(terminals):
        zone = name.split("_")[-1]
        side = resolve_side(name)
        terminal = equipments[name]
        inlet = f"{side}_{EPApi.INLET.node_name()}"
        outlet = f"{side}_{EPApi.OUTLET.node_name()}"
        air_zone_splitters[loop][EPApi.OUTLET.node_name(i+1)] = terminal[inlet]
        air_zone_mixers[loop][EPApi.INLET.node_name(i+1)] = air_nodes[zone]["air_return_node"]

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
            side = resolve_side(obj_name, loop_side=PLANT)
            equipment = equipments[obj_name]
            outlet = equipment[f"{side}_{EPApi.OUTLET.node_name()}"]
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
add_variable("Site Outdoor Air Humidity Ratio")
add_variable("Site Outdoor Air Relative Humidity")
add_variable("Zone Air Temperature")
add_variable("Zone Air Relative Humidity")
add_variable("Zone Air Humidity Ratio")
add_variable("Zone Thermostat Heating Setpoint Temperature")
add_variable("Zone Thermostat Cooling Setpoint Temperature")
add_variable("Zone Mean Air Dewpoint Temperature")

if CONF.get("verbose"):
    add_variable("System Node Setpoint Temperature")
    add_variable("System Node Temperature")

for equipment_name in EQUIPMENTS:
    if BOREHOLE in equipment_name:
        suffix = "Ground Heat Exchanger"
        add_variable(f"{suffix} Heat Transfer Rate")
        add_variable(f"{suffix} Inlet Temperature")
        add_variable(f"{suffix} Outlet Temperature")
        add_variable(f"{suffix} Average Borehole Temperature")
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
        suffix = "Boiler"
        add_variable(f"{suffix} Heating Rate")
        add_variable(f"{suffix} Inlet Temperature")
        add_variable(f"{suffix} Outlet Temperature")
        add_variable(f"{suffix} Part Load Ratio")
    if EXCHANGER in equipment_name:
        suffix = "Fluid Heat Exchanger"
        add_variable(f"{suffix} Heat Transfer Rate")
        add_variable(f"{suffix} Loop Supply Side Mass Flow Rate")
        add_variable(f"{suffix} Loop Supply Side Inlet Temperature")
        add_variable(f"{suffix} Loop Supply Side Outlet Temperature")
        add_variable(f"{suffix} Loop Demand Side Mass Flow Rate")
        add_variable(f"{suffix} Loop Demand Side Inlet Temperature")
        add_variable(f"{suffix} Loop Demand Side Outlet Temperature")
    if FCU in equipment_name:
        #add_variable("Heating Coil Heating Rate")
        add_variable("Cooling Coil Total Cooling Rate")
        add_variable("Cooling Coil Sensible Cooling Rate")
        add_variable("Cooling Coil Wetted Area Fraction")
        add_variable("Fan Electricity Rate")
        add_variable("Fan Coil Fan Electricity Rate")
        add_variable("Fan Coil Heating Rate")
        add_variable("Fan Coil Total Cooling Rate")
        add_variable("Fan Coil Fan Speed Level")
    if FAN in equipment_name:
        add_variable("Fan Electricity Rate")
        add_variable("Fan Air Mass Flow Rate")
    if "baseboard" in equipment_name:
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

BUILDING_LAST_NAME = BUILDING_NAME.split("/")[-1]

if not os.path.exists(EP_SIM_PATH):
    os.mkdir(EP_SIM_PATH)
if not os.path.exists(f"{EP_SIM_PATH}/{BUILDING_LAST_NAME}"):
    os.mkdir(f"{EP_SIM_PATH}/{BUILDING_LAST_NAME}")
if not os.path.exists(f"{EP_SIM_PATH}/{BUILDING_LAST_NAME}/{PROJECT_NAME}"):
    os.mkdir(f"{EP_SIM_PATH}/{BUILDING_LAST_NAME}/{PROJECT_NAME}")

final_name = f"{EP_SIM_PATH}/{BUILDING_LAST_NAME}/{PROJECT_NAME}/{BUILDING_LAST_NAME}.idf"
idf.save(final_name)
