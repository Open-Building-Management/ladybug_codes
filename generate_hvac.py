""""hvac generator"""
import os
from typing import Any

from eppy.bunch_subclass import BadEPFieldError

from idfhub.hvac import (
    PLANT, SUPPLY, DEMAND, RETURN, INLET, OUTLET,
    EPApi, EPValues,
    add_plant_loop,
    add_baseboard,
    create_branch,
    LoopNodes, Branches,
    set_nodes, split_mix
)
# autocompletion use
from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import (
    Timestep, SizingperiodDesignday, Runperiod, Version, Simulationcontrol,
    Building, Globalgeometryrules,
    SiteGroundtemperatureBuildingsurface,
    SiteGroundtemperatureUndisturbedKusudaachenbach,
    Scheduletypelimits, ScheduleConstant,
    ScheduleCompact,
    ThermostatsetpointDualsetpoint, ZonecontrolThermostat,
    CurveQuadlinear,
    HeatpumpWatertowaterEquationfitHeating,
    GroundheatexchangerVerticalProperties,
    GroundheatexchangerVerticalArray,
    GroundheatexchangerSystem,
    Plantequipmentlist, Plantequipmentoperationschemes,
    PlantequipmentoperationHeatingload, PlantequipmentoperationCoolingload,
    SetpointmanagerOutdoorairreset, SetpointmanagerScheduled,
    SizingParameters, SizingZone, SizingPlant,
    ZonehvacEquipmentlist, ZonehvacEquipmentconnections,
    OutputVariabledictionary,
    OutputTableSummaryreports, OutputcontrolTableStyle,
    OutputVariable, OutputSqlite,
    FluidpropertiesGlycolconcentration,
    PumpConstantspeed
)
from idfhub.idf_autocomplete.v24_1_0.idf_types_short import (
    TimestepType, SizingperiodDesigndayType, RunperiodType, VersionType, SimulationcontrolType,
    BuildingType, GlobalgeometryrulesType,
    SiteGroundtemperatureBuildingsurfaceType,
    SiteGroundtemperatureUndisturbedKusudaachenbachType,
    ScheduletypelimitsType, ScheduleConstantType,
    ScheduleCompactType,
    ThermostatsetpointDualsetpointType, ZonecontrolThermostatType,
    CurveQuadlinearType,
    HeatpumpWatertowaterEquationfitHeatingType,
    GroundheatexchangerVerticalPropertiesType,
    GroundheatexchangerVerticalArrayType,
    GroundheatexchangerSystemType,
    PlantequipmentlistType, PlantequipmentoperationschemesType,
    PlantequipmentoperationHeatingloadType, PlantequipmentoperationCoolingloadType,
    SetpointmanagerOutdoorairresetType, SetpointmanagerScheduledType,
    SizingParametersType, SizingZoneType, SizingPlantType,
    ZonehvacEquipmentlistType, ZonehvacEquipmentconnectionsType,
    OutputVariabledictionaryType,
    OutputTableSummaryreportsType, OutputcontrolTableStyleType,
    OutputVariableType, OutputSqliteType,
    FluidpropertiesGlycolconcentrationType,
    PumpConstantspeedType
)

from idfhub.helpers.common import get_logger

from common import (
    idf,
    BUILDING_NAME, PROJECT_NAME,
    CONF, ZONES, LOOPS, BRANCHES,
    EQUIPMENTS
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
WATER_HEATING_LOOP = "water_heating_loop"
WATER_LAW_SET_POINT = "water_law_set_point"
CONSTANT_SET_POINT = "constant_set_point"
BOREHOLE = "borehole"
PUMP = "pump"
BYPASS = "bypass"
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
# on crée 2 schedules constants, 20°C chauffage et 25°C raffraichissement :
# - const_temp_sched_20deg
# - const_temp_sched_25deg
#------------------------------------------------------------------------------
temperature_typelimits = Scheduletypelimits(
    idf,
    **ScheduletypelimitsType(
        Name="temperature",
        Numeric_Type=EPValues.CONTINUOUS,
        Unit_Type=EPValues.TEMPERATURE
    )
)

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

def create_const_sched(temp: int):
    """create a constant schedule type"""
    return ScheduleConstantType(
        Name=f"const_temp_sched_{temp}deg",
        Schedule_Type_Limits_Name=temperature_typelimits.Name,
        Hourly_Value=temp
    )

consigne_25deg = ScheduleConstant(idf, **create_const_sched(25))
consigne_20deg = ScheduleConstant(idf, **create_const_sched(20))

zone_thermostat = ThermostatsetpointDualsetpoint(
    idf,
    **ThermostatsetpointDualsetpointType(
        Name="zone_thermostat",
        Heating_Setpoint_Temperature_Schedule_Name=consigne_20deg.Name,
        Cooling_Setpoint_Temperature_Schedule_Name=consigne_25deg.Name
    )
)

# Control types are integers:
# 0 - Uncontrolled (floating, no thermostat),
# 1 = ThermostatSetpoint:SingleHeating,
# 2 = ThermostatSetpoint:SingleCooling,
# 3 = ThermostatSetpoint:SingleHeatingOrCooling,
# 4 = ThermostatSetpoint:DualSetpoint
control_types = Scheduletypelimits(
    idf,
    **ScheduletypelimitsType(
        Name="control_types",
        Lower_Limit_Value=0,
        Upper_Limit_Value=4,
        Numeric_Type=EPValues.DISCRETE
    )
)

# on utilise un schedule compact
# Mots-clés utiles dans For:
# Weekdays
# Weekends
# AllDays
# Monday
# Tuesday
# ...
# Holidays
# SummerDesignDay
# WinterDesignDay
# CustomDay1/2
control_type_schedule = ScheduleCompact(
    idf,
    **ScheduleCompactType(
        Name="control_type_schedule",
        Schedule_Type_Limits_Name=control_types.Name,
        Field_1=f"{EPValues.THROUGH}: 12/31",
        Field_2=f"{EPValues.FOR}: {EPValues.WEEKDAYS}",
        Field_3=f"{EPValues.UNTIL}: 07:00",
        Field_4=0,
        Field_5=f"{EPValues.UNTIL}: 17:00",
        Field_6=4,
        Field_7=f"{EPValues.UNTIL}: 24:00",
        Field_8=0,
        Field_9=f"{EPValues.FOR}: {EPValues.WEEKENDS}",
        Field_10=f"{EPValues.UNTIL}: 24:00",
        Field_11=0,
        Field_12=f"{EPValues.FOR}:{EPValues.WINTER_DESIGN_DAY}",
        Field_13=f"{EPValues.UNTIL}: 07:00",
        Field_14=0,
        Field_15=f"{EPValues.UNTIL}: 17:00",
        Field_16=4,
        Field_17=f"{EPValues.UNTIL}: 24:00",
        Field_18=0,
    )
)

thermostats = {}
for zone in ZONES:
    thermostats[zone] = ZonecontrolThermostat(
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
loops = {}
for loop in LOOPS:
    if loop == SOIL_LOOP:
        glycol_water_30 = FluidpropertiesGlycolconcentration(
            idf,
            **FluidpropertiesGlycolconcentrationType(
                Name="eau glycol 30pourcent",
                Glycol_Type="PropyleneGlycol",
                Glycol_Concentration=0.3
            )
        )
        soil_loop = add_plant_loop(idf, loop, 35, -5)
        soil_loop.Fluid_Type = "UserDefinedFluidType"
        soil_loop.User_Defined_Fluid_Type = glycol_water_30.Name
        loops[loop] = soil_loop
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
    if loop == WATER_HEATING_LOOP:
        heating_loop = add_plant_loop(idf, loop, 100, 0)
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

#------------------------------------------------------------------------------
# SETPOINTS
#------------------------------------------------------------------------------
def water_law(loop_name: str, setup: str):
    """add a waterlaw setpoint on a loop plant outlet"""
    loop_nodes = LoopNodes(loop_name)
    message = f"waterlaw @ {loop_nodes.plant_outlet} with {CONF[setup]}"
    LOGGER.debug(message)
    SetpointmanagerOutdoorairreset(
        idf,
        **SetpointmanagerOutdoorairresetType(
            Name=f"{setup} {loop_name}",
            Control_Variable=EPValues.TEMPERATURE,
            Setpoint_at_Outdoor_Low_Temperature=CONF[setup].get(
                "Setpoint_at_Outdoor_Low_Temperature", 70),
            Outdoor_Low_Temperature=CONF[setup].get(
                "Outdoor_Low_Temperature", -5),
            Setpoint_at_Outdoor_High_Temperature=CONF[setup].get(
                "Setpoint_at_Outdoor_High_Temperature", 40),
            Outdoor_High_Temperature=CONF[setup].get(
                "Outdoor_High_Temperature", 15),
            Setpoint_Node_or_NodeList_Name=loop_nodes.plant_outlet
        )
    )

def constant_set_point(loop_name: str, setup: str):
    """add a constant setpoint on a loop plant outlet"""
    loop_nodes = LoopNodes(loop_name)
    message = f"constant setpoint @ {loop_nodes.plant_outlet} with {CONF[setup]}"
    LOGGER.debug(message)
    consigne = ScheduleConstant(
        idf,
        **create_const_sched(
            CONF[setup].get("temp", 12)
        )
    )
    SetpointmanagerScheduled(
        idf,
        **SetpointmanagerScheduledType(
            Name=f"{setup} {loop_name}",
            Control_Variable=EPValues.TEMPERATURE,
            Schedule_Name=consigne.Name,
            Setpoint_Node_or_NodeList_Name=loop_nodes.plant_outlet,
        )
    )

#------------------------------------------------------------------------------
# SOIL, BOREHOLE, PRODUCTION SYSTEMS
#------------------------------------------------------------------------------
def ground_temperature():
    """create a basic ground temperature for the building"""
    SiteGroundtemperatureBuildingsurface(
        idf,
        **SiteGroundtemperatureBuildingsurfaceType(
            January_Ground_Temperature=7.0,
            February_Ground_Temperature=8.0,
            March_Ground_Temperature=9.5,
            April_Ground_Temperature=11.0,
            May_Ground_Temperature=12.5,
            June_Ground_Temperature=13.5,
            July_Ground_Temperature=14.0,
            August_Ground_Temperature=13.8,
            September_Ground_Temperature=12.5,
            October_Ground_Temperature=10.5,
            November_Ground_Temperature=8.5,
            December_Ground_Temperature=7.5,
        )
    )

def vertical_geoexchanger(name: str):
    """add a geoexchanger with vertical boreholes"""
    soil = SiteGroundtemperatureUndisturbedKusudaachenbach(
        idf,
        **SiteGroundtemperatureUndisturbedKusudaachenbachType(
            Name="Sol_KA",
            Soil_Thermal_Conductivity=2.5, # W/(m K)
            Soil_Density=2000, # kg/m3
            Soil_Specific_Heat=900, # J/(kg K)
            Average_Soil_Surface_Temperature=11,
            Average_Amplitude_of_Surface_Temperature=10,
            Phase_Shift_of_Minimum_Surface_Temperature=45 #days
        )
    )
    hole = GroundheatexchangerVerticalProperties(
        idf,
        **GroundheatexchangerVerticalPropertiesType(
            Name="single typical hole",
            Depth_of_Top_of_Borehole=0,
            Borehole_Length=100,
            Borehole_Diameter=0.15,
            Grout_Thermal_Conductivity=1.2, # W / (m K)
            Grout_Thermal_Heat_Capacity=3.0e6, # J / (m3 K)
            Pipe_Thermal_Conductivity=0.4,
            Pipe_Thermal_Heat_Capacity=2.0e6,
            Pipe_Thickness=0.003,
            Pipe_Outer_Diameter=0.032,
            UTube_Distance=0.055,
        )
    )

    boreholes = GroundheatexchangerVerticalArray(
        idf,
        **GroundheatexchangerVerticalArrayType(
            Name="champ de sondes",
            GHEVerticalProperties_Object_Name=hole.Name,
            Number_of_Boreholes_in_XDirection=CONF[name].get(
                "Number_of_Boreholes_in_XDirection", 5),
            Number_of_Boreholes_in_YDirection=CONF[name].get(
                "Number_of_Boreholes_in_YDirection", 2),
            Borehole_Spacing=6
        )
    )

    # 0.0033*3600 m3/h soit 11,88 m3/h pour 10 forages, soit 1.2 m3/h par forage
    return GroundheatexchangerSystem(
        idf,
        **GroundheatexchangerSystemType(
            Name="vertical geoexchanger",
            Inlet_Node_Name="vertical geoexchanger inlet",
            Outlet_Node_Name="vertical geoexchanger outlet",
            Design_Flow_Rate=0.006, # m3/s before 0.0033
            Undisturbed_Ground_Temperature_Model_Name=soil.Name,
            Undisturbed_Ground_Temperature_Model_Type=soil.key,
            Ground_Thermal_Conductivity=2.5, #W / (m K) - 0.69 serait une valeur médiocre
            Ground_Thermal_Heat_Capacity=1.8e6, #Pa/K = J / (m3 K)
            GHEVerticalArray_Object_Name=boreholes.Name
        )
    )

def constant_pump(name):
    """add a constant speed pump"""
    return PumpConstantspeed(
        idf,
        **PumpConstantspeedType(
            Name=name,
            Inlet_Node_Name=f"{name} inlet",
            Outlet_Node_Name=f"{name} outlet",
            Design_Flow_Rate=EPValues.AUTOSIZE,
            Design_Power_Consumption=EPValues.AUTOSIZE,
            Motor_Efficiency=0.9,
            Pump_Control_Type=EPValues.INTERMITTENT
        )
    )

def create_quadlincurve(name, coeff1, coeff2, coeff3, coeff4):
    """create a curve for heatpump configuration"""
    return CurveQuadlinearType(
        Name=name,
        Coefficient1_Constant=coeff1,
        Coefficient2_w=coeff2,
        Coefficient3_x=coeff3,
        Coefficient4_y=coeff4,
        Coefficient5_z=0,
        Minimum_Value_of_w=-5.0,
        Maximum_Value_of_w=20.0,
        Minimum_Value_of_x=30.0,
        Maximum_Value_of_x=55.0,
        Minimum_Value_of_y=-5.0,
        Maximum_Value_of_y=20.0,
        Minimum_Value_of_z=0.0,
        Maximum_Value_of_z=1.0,
        Minimum_Curve_Output=0.5,
        Maximum_Curve_Output=1,
        Input_Unit_Type_for_w=EPValues.TEMPERATURE,
        Input_Unit_Type_for_x=EPValues.TEMPERATURE,
        Input_Unit_Type_for_y=EPValues.TEMPERATURE,
        Input_Unit_Type_for_z="Dimensionless"
    )

def water_to_water_heatpump(name):
    """add a water to water heatpump"""
    capacity_curve = CurveQuadlinear(
        idf,
        **create_quadlincurve(
            f"{name} Heating capacity curve",
            0.8, 0.002, 0.002, 0
        )
    )

    power_curve = CurveQuadlinear(
        idf,
        **create_quadlincurve(
            f"{name} Heating power curve",
            0.4, 0.002, 0.002, 0
        )
    )

    return HeatpumpWatertowaterEquationfitHeating(
        idf,
        **HeatpumpWatertowaterEquationfitHeatingType(
            Name=name,
            Source_Side_Inlet_Node_Name=f"{name} source side inlet",
            Source_Side_Outlet_Node_Name=f"{name} source side outlet",
            Load_Side_Inlet_Node_Name=f"{name} load side inlet",
            Load_Side_Outlet_Node_Name=f"{name} load side outlet",
            Reference_Load_Side_Flow_Rate=EPValues.AUTOSIZE,
            Reference_Source_Side_Flow_Rate=EPValues.AUTOSIZE,
            Reference_Heating_Capacity=EPValues.AUTOSIZE,
            Reference_Heating_Power_Consumption=EPValues.AUTOSIZE,
            Reference_Coefficient_of_Performance=CONF[name].get(
                "Reference_Coefficient_of_Performance", 2.5),
            Sizing_Factor=1,
            Heating_Capacity_Curve_Name=capacity_curve.Name,
            Heating_Compressor_Power_Curve_Name=power_curve.Name
        )
    )

def resolve_side(name, branch_type):
    """resolve equipment side
    for two sided equipments like heat pumps"""
    if name not in CONF:
        return None
    if CONF[name].get("sides", 1) == 2:
        return {
            SUPPLY: EPApi.LOAD_SIDE,
            PLANT: EPApi.LOAD_SIDE,
            DEMAND: EPApi.SOURCE_SIDE,
            RETURN: EPApi.SOURCE_SIDE
        }[branch_type]
    return None

equipments: dict[str, Any] = {}

def adjust_nodes_branch(loop_name: str, branch_type: str):
    """use yaml declaration to organise a branch and relevant nodes on a side loop"""
    object_names = BRANCHES[loop_name][branch_type]
    # we adjust the nodes
    nb_objects = len(object_names)
    for i, obj in enumerate(object_names):
        inlet_node: str|None = None
        outlet_node: str|None = None
        # start and end of the loop side
        if i == 0:
            inlet_node = LoopNodes(loop_name).get(side=branch_type, port=INLET)
        if i == nb_objects - 1:
            outlet_node = LoopNodes(loop_name).get(side=branch_type, port=OUTLET)
        # we only modify inlets using the previous equipement
        if inlet_node is None:
            # previous object exists
            prev_name = object_names[i-1]
            prev_obj = equipments[prev_name]
            try:
                inlet_node = prev_obj[EPApi.OUTLET_NODE_NAME]
            except BadEPFieldError:
                # we have a 2 sided equipment - heatpump
                side = resolve_side(prev_name, branch_type)
                inlet_node = prev_obj[f"{side}_{EPApi.OUTLET_NODE_NAME}"]
        set_nodes(
            equipments[obj],
            inlet=inlet_node,
            outlet=outlet_node,
            side=resolve_side(obj, branch_type)
        )
    # we create the branch using the objects as nodes are now correct
    objects = [equipments[obj] for obj in object_names]
    sides = [resolve_side(obj, branch_type) for obj in object_names]
    create_branch(
        idf,
        name = Branches(loop).get(side=branch_type),
        objects = objects,
        sides = sides
    )

for equipment_name in EQUIPMENTS:
    if equipment_name == BOREHOLE:
        ground_temperature()
        borehole = vertical_geoexchanger(equipment_name)
        equipments[equipment_name] = borehole
    if PUMP in equipment_name:
        equipments[equipment_name] = constant_pump(equipment_name)
    if equipment_name == HPWTW:
        hpwtw = water_to_water_heatpump(equipment_name)
        equipments[equipment_name] = hpwtw

for loop in LOOPS:
    for tune in CONF[loop]:
        if tune == WATER_LAW_SET_POINT:
            water_law(loop, tune)
        if tune == CONSTANT_SET_POINT:
            constant_set_point(loop, tune)

    if loop in BRANCHES:
        if PLANT in BRANCHES[loop]:
            adjust_nodes_branch(loop, PLANT)
        if DEMAND in BRANCHES[loop]:
            adjust_nodes_branch(loop, DEMAND)

#------------------------------------------------------------------------------
# PLANT EQUIPEMENTS
#------------------------------------------------------------------------------
soil_loop_equipement_list = Plantequipmentlist(
    idf,
    **PlantequipmentlistType(
        Name=f"{soil_loop.Name} Equipment List",
        Equipment_1_Object_Type=borehole.key,
        Equipment_1_Name=borehole.Name
    )
)

soil_loop_operation = PlantequipmentoperationCoolingload(
    idf,
    **PlantequipmentoperationCoolingloadType(
        Name=f"{soil_loop.Name} cooling operation",
        Load_Range_1_Lower_Limit=0,
        Load_Range_1_Upper_Limit=1e9,
        Range_1_Equipment_List_Name=soil_loop_equipement_list.Name
    )
)
heating_loop_equipement_list = Plantequipmentlist(
    idf,
    **PlantequipmentlistType(
        Name=f"{heating_loop.Name} Equipment List",
        Equipment_1_Object_Type=hpwtw.key,
        Equipment_1_Name=hpwtw.Name
    )
)
heating_loop_operation = PlantequipmentoperationHeatingload(
    idf,
    **PlantequipmentoperationHeatingloadType(
        Name=f"{heating_loop.Name} heating operation",
        Load_Range_1_Lower_Limit=0,
        Load_Range_1_Upper_Limit=1e9,
        Range_1_Equipment_List_Name=heating_loop_equipement_list.Name
    )
)
Plantequipmentoperationschemes(
    idf,
    **PlantequipmentoperationschemesType(
        Name=SOIL_LOOP,
        Control_Scheme_1_Object_Type=soil_loop_operation.key,
        Control_Scheme_1_Name=soil_loop_operation.Name,
        Control_Scheme_1_Schedule_Name="Always On"
    )
)
Plantequipmentoperationschemes(
    idf,
    **PlantequipmentoperationschemesType(
        Name=WATER_HEATING_LOOP,
        Control_Scheme_1_Object_Type=heating_loop_operation.key,
        Control_Scheme_1_Name=heating_loop_operation.Name,
        Control_Scheme_1_Schedule_Name="Always On"
    )
)

#------------------------------------------------------------------------------
# EMISSION SYSTEMS
#------------------------------------------------------------------------------
baseboards = {}
baseboard_branches = {}
for zone in ZONES:
    baseboards[zone] =  add_baseboard(idf, zone, f"{zone} inlet", f"{zone} outlet")
    baseboard_branches[zone] = create_branch(
        idf,
        name = f"{heating_loop_branches.demand_branch} {zone}",
        objects = [baseboards[zone]],
        sides = [None]
    )

split_mix(
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
add_variable("Site Outdoor Air Drybulb Temperature")
add_variable("Zone Air Temperature")
add_variable("Ground Heat Exchanger Heat Transfer Rate")
add_variable("Ground Heat Exchanger Inlet Temperature")
add_variable("Ground Heat Exchanger Outlet Temperature")
add_variable("Baseboard Total Heating Rate")
add_variable("Baseboard Water Inlet Temperature")
add_variable("Baseboard Water Outlet Temperature")
add_variable("Heat Pump Load Side Outlet Temperature")
add_variable("Heat Pump Load Side Inlet Temperature")
add_variable("Heat Pump Source Side Outlet Temperature")
add_variable("Heat Pump Source Side Inlet Temperature")

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
