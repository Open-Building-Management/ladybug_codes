""""hvac generator"""
import os

from idfhub.hvac import (
    EPApi,
    add_plant_loop,
    add_constant_pump, add_baseboard,
    create_branch,
    LoopNodes, Branches,
    set_nodes, split_mix
)
# autocompletion use
from idfhub.idf_autocomplete.idf_helpers_short import (
    Timestep, SizingperiodDesignday, Runperiod, Version, Simulationcontrol,
    Building, Globalgeometryrules,
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
    FluidpropertiesGlycolconcentration
)
from idfhub.idf_autocomplete.idf_types_short import (
    TimestepType, SizingperiodDesigndayType, RunperiodType, VersionType, SimulationcontrolType,
    BuildingType, GlobalgeometryrulesType,
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
    FluidpropertiesGlycolconcentrationType
)

from idfhub.helpers.common import get_logger

from common import idf, BUILDING_NAME

FORMAT = (
    '%(asctime)s | %(levelname).1s | '
    '%(name)s:%(lineno)d | '
    '%(message)s'
)

LOGGER = get_logger(format=FORMAT)


message = f"idf hvac injection for energyplus {idf.idd_version}"
LOGGER.info(message)

EP_SIM_PATH = "ep_simulations"
SOIL_LOOP = "Soil Loop"
HEAT_LOOP = "Heating Loop"
PROJECT_NAME = f"{BUILDING_NAME}_no_bypass"

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
        Day_Type="WinterDesignDay",
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
SizingParameters(idf, **SizingParametersType(Heating_Sizing_Factor=1.25, Cooling_Sizing_Factor=1.15))
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


DISCRETE = "Discrete"
CONTINUOUS = "Continuous"
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
        Numeric_Type=CONTINUOUS,
        Unit_Type="Temperature"
    )
)

# ajout car generate_geometry nécessite un schedule constant appelé Always On qui utilise Fractional ????
fractional_typelimits = Scheduletypelimits(
    idf,
    **ScheduletypelimitsType(
        Name="Fractional",
        Lower_Limit_Value=0,
        Upper_Limit_Value=1,
        Numeric_Type=CONTINUOUS,
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
consigne_12deg = ScheduleConstant(idf, **create_const_sched(12))

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
        Numeric_Type=DISCRETE
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
        Field_1="Through: 12/31",
        Field_2="For: Weekdays",
        Field_3="Until: 07:00",
        Field_4=0,
        Field_5="Until: 17:00",
        Field_6=4,
        Field_7="Until: 24:00",
        Field_8=0,
        Field_9="For: Weekends",
        Field_10="Until: 24:00",
        Field_11=0,
        Field_12="For:WinterDesignDay",
        Field_13="Until: 07:00",
        Field_14=0,
        Field_15="Until: 17:00",
        Field_16=4,
        Field_17="Until: 24:00",
        Field_18=0,
    )
)

rdc_thermostat = ZonecontrolThermostat(
    idf,
    **ZonecontrolThermostatType(
        Name="RDC_thermostat",
        Zone_or_ZoneList_Name="RDC",
        Control_Type_Schedule_Name=control_type_schedule.Name,
        Control_1_Object_Type=zone_thermostat.key,
        Control_1_Name=zone_thermostat.Name
    )
)

rplus1_thermostat = ZonecontrolThermostat(
    idf,
    **ZonecontrolThermostatType(
        Name="RPLUS1_thermostat",
        Zone_or_ZoneList_Name="RPLUS1",
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
glycol_water_30 = FluidpropertiesGlycolconcentration(
    idf,
    **FluidpropertiesGlycolconcentrationType(
        Name="eau glycol 30pourcent",
        Glycol_Type="PropyleneGlycol",
        Glycol_Concentration=0.3
    )
)

soil_loop = add_plant_loop(idf, SOIL_LOOP, 35, -5)
soil_loop.Fluid_Type = "UserDefinedFluidType"
soil_loop.User_Defined_Fluid_Type = glycol_water_30.Name
soil_loop_nodes = LoopNodes(SOIL_LOOP)
soil_loop_branches = Branches(SOIL_LOOP)

heating_loop = add_plant_loop(idf, HEAT_LOOP, 100, 0)
heating_loop_nodes = LoopNodes(HEAT_LOOP)
heating_loop_branches = Branches(HEAT_LOOP)

SizingPlant(
    idf,
    **SizingPlantType(
        Plant_or_Condenser_Loop_Name=SOIL_LOOP,
        Loop_Type="Cooling",
        Design_Loop_Exit_Temperature=12,
        Loop_Design_Temperature_Difference=5,
        Sizing_Option="NonCoincident",
        Zone_Timesteps_in_Averaging_Window=1,
    )
)
SizingPlant(
    idf,
    **SizingPlantType(
        Plant_or_Condenser_Loop_Name=HEAT_LOOP,
        Loop_Type="Heating",
        Design_Loop_Exit_Temperature=70,
        Loop_Design_Temperature_Difference=10,
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
basic_zone_sizing("RDC")
basic_zone_sizing("RPLUS1")

#------------------------------------------------------------------------------
# SETPOINTS
# > LOI D'EAU sur le heating loop
#------------------------------------------------------------------------------
SetpointmanagerOutdoorairreset(
    idf,
    **SetpointmanagerOutdoorairresetType(
        Name="loi d'eau heating loop",
        Control_Variable="Temperature",
        Setpoint_at_Outdoor_Low_Temperature=70,
        Outdoor_Low_Temperature=-5,
        Setpoint_at_Outdoor_High_Temperature=40,
        Outdoor_High_Temperature=15,
        Setpoint_Node_or_NodeList_Name=heating_loop_nodes.supply_outlet
    )
)
SetpointmanagerScheduled(
    idf,
    **SetpointmanagerScheduledType(
        Name="set point soil loop",
        Control_Variable="temperature",
        Schedule_Name=consigne_12deg.Name,
        Setpoint_Node_or_NodeList_Name=soil_loop_nodes.supply_outlet,
    )
)
#------------------------------------------------------------------------------
# SOIL, BOREHOLE, PRODUCTION SYSTEMS
#------------------------------------------------------------------------------

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
        Depth_of_Top_of_Borehole=1,
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

champ_de_sondes = GroundheatexchangerVerticalArray(
    idf,
    **GroundheatexchangerVerticalArrayType(
        Name="champ de sondes",
        GHEVerticalProperties_Object_Name=hole.Name,
        Number_of_Boreholes_in_XDirection=5,
        Number_of_Boreholes_in_YDirection=2,
        Borehole_Spacing=6
    )
)

# 0.0033*3600 m3/h soit 11,88 m3/h pour 10 forages, soit 1.2 m3/h par forage
borehole = GroundheatexchangerSystem(
    idf, 
    **GroundheatexchangerSystemType(
        Name="Borehole",
        Inlet_Node_Name=soil_loop_nodes.supply_inlet,
        Outlet_Node_Name="Borehole outlet",
        Design_Flow_Rate=0.0033, # m3/s
        Undisturbed_Ground_Temperature_Model_Name=soil.Name,
        Undisturbed_Ground_Temperature_Model_Type=soil.key,
        Ground_Thermal_Conductivity=2.5, #W / (m K) - 0.69 serait une valeur médiocre
        Ground_Thermal_Heat_Capacity=1.8e6, #Pa/K = J / (m3 K)
        GHEVerticalArray_Object_Name=champ_de_sondes.Name
    )
)

soil_pump = add_constant_pump(
    idf,
    f"{SOIL_LOOP} Pump",
    borehole[EPApi.OUTLET_NODE_NAME],
    soil_loop_nodes.supply_outlet
)
inside_pump = add_constant_pump(
    idf,
    f"{HEAT_LOOP} Pump",
    heating_loop_nodes.supply_inlet,
    "inside pump outlet"
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
        Maximum_Curve_Output=1.5,
        Input_Unit_Type_for_w="Temperature",
        Input_Unit_Type_for_x="Temperature",
        Input_Unit_Type_for_y="Temperature",
        Input_Unit_Type_for_z="Dimensionless"
    )

hpwtw_name = "HPWTW"
capacity_curve = CurveQuadlinear(
    idf,
    **create_quadlincurve(
        f"{hpwtw_name} Heating capacity curve",
        0.8, 0.01, 0.02, 0.03
    )
)

power_curve = CurveQuadlinear(
    idf,
    **create_quadlincurve(
        f"{hpwtw_name} Heating power curve",
        0.5, 0.005, 0.015, 0.02
    )
)

hpwtw = HeatpumpWatertowaterEquationfitHeating(
    idf, 
    **HeatpumpWatertowaterEquationfitHeatingType(
        Name=hpwtw_name,
        Reference_Load_Side_Flow_Rate=EPApi.AUTOSIZE,
        Reference_Source_Side_Flow_Rate=EPApi.AUTOSIZE,
        Reference_Heating_Capacity=EPApi.AUTOSIZE,
        Reference_Heating_Power_Consumption=EPApi.AUTOSIZE,
        Reference_Coefficient_of_Performance=5,
        Sizing_Factor=1,
        Heating_Capacity_Curve_Name=capacity_curve.Name,
        Heating_Compressor_Power_Curve_Name=power_curve.Name
    )
)
set_nodes(
    hpwtw,
    side=EPApi.SOURCE_SIDE,
    inlet=soil_loop_nodes.demand_inlet,
    outlet=soil_loop_nodes.demand_outlet,
)
set_nodes(
    hpwtw,
    side=EPApi.LOAD_SIDE,
    inlet=inside_pump[EPApi.OUTLET_NODE_NAME],
    outlet=heating_loop_nodes.supply_outlet
)

# BRANCHES
# on donne aux branches des noms standards qui ont déjà été attribués à une branchlist
# lors de la création du loop correspondant
create_branch(
    idf,
    name = soil_loop_branches.supply_branch,
    objects = [borehole, soil_pump],
    sides = [None, None]
)
create_branch(
    idf,
    name = soil_loop_branches.demand_branch,
    objects = [hpwtw],
    sides = [EPApi.SOURCE_SIDE]
)
create_branch(
    idf,
    name = heating_loop_branches.supply_branch,
    objects = [inside_pump, hpwtw],
    sides = [None, EPApi.LOAD_SIDE]
)


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
        Name=HEAT_LOOP,
        Control_Scheme_1_Object_Type=heating_loop_operation.key,
        Control_Scheme_1_Name=heating_loop_operation.Name,
        Control_Scheme_1_Schedule_Name="Always On"
    )
)

#------------------------------------------------------------------------------
# EMISSION SYSTEMS
#------------------------------------------------------------------------------
rplus1_baseboard = add_baseboard(idf, "RPLUS1", "rplus1 inlet", "rplus1 outlet")
rdc_baseboard = add_baseboard(idf, "RDC", "rdc inlet", "rdc outlet")

rplus1_baseboard_branch = create_branch(
    idf,
    name = f"{heating_loop_branches.demand_branch} rplus1",
    objects = [rplus1_baseboard],
    sides = [None]
)
rdc_baseboard_branch = create_branch(
    idf,
    name = f"{heating_loop_branches.demand_branch} rdc",
    objects = [rdc_baseboard],
    sides = [None]
)
split_mix(
    idf=idf,
    plantloop=heating_loop,
    side=EPApi.DEMAND_SIDE,
    branches=[rdc_baseboard_branch, rplus1_baseboard_branch]
)

#------------------------------------------------------------------------------
# ZONE EQUIPMENTS DECLARATION
#------------------------------------------------------------------------------
rdc_equipment_list = ZonehvacEquipmentlist(
    idf,
    **ZonehvacEquipmentlistType(
        Name="rdc equipment list",
        Zone_Equipment_1_Name=rdc_baseboard.Name,
        Zone_Equipment_1_Object_Type=rdc_baseboard.key,
        Zone_Equipment_1_Cooling_Sequence=1,
        Zone_Equipment_1_Heating_or_NoLoad_Sequence=1
    )
)
rplus1_equipment_list = ZonehvacEquipmentlist(
    idf,
    **ZonehvacEquipmentlistType(
        Name="rplus1 equipment list",
        Zone_Equipment_1_Name=rplus1_baseboard.Name,
        Zone_Equipment_1_Object_Type=rplus1_baseboard.key,
        Zone_Equipment_1_Cooling_Sequence=1,
        Zone_Equipment_1_Heating_or_NoLoad_Sequence=1
    )
)
ZonehvacEquipmentconnections(
    idf,
    **ZonehvacEquipmentconnectionsType(
        Zone_Name="RDC",
        Zone_Conditioning_Equipment_List_Name=rdc_equipment_list.Name,
        Zone_Air_Node_Name="rdc air node"
    )
)
ZonehvacEquipmentconnections(
    idf,
    **ZonehvacEquipmentconnectionsType(
        Zone_Name="RPLUS1",
        Zone_Conditioning_Equipment_List_Name=rplus1_equipment_list.Name,
        Zone_Air_Node_Name="rplus1 air node"
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

OutputSqlite(
    idf,
    **OutputSqliteType(
        Option_Type="SimpleAndTabular"
    )
)
input("press")

if not os.path.exists(EP_SIM_PATH):
    os.mkdir(EP_SIM_PATH)
if not os.path.exists(f"{EP_SIM_PATH}/{PROJECT_NAME}"):
    os.mkdir(f"{EP_SIM_PATH}/{PROJECT_NAME}")

idf.save(f"ep_simulations/{PROJECT_NAME}/{PROJECT_NAME}_W_HVAC.idf")
