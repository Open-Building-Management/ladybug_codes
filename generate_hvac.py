""""hvac generator"""

from eppy.modeleditor import IDF

from idfhub.hvac import (
    EPApi,
    add_plant_loop, add_ground_exchanger,
    add_constant_pump, add_baseboard,
    create_branch, create_splitter, create_mixer,
    create_pipe, create_connector_list,
    LoopNodes, Branches,
    set_nodes
)
# autocompletion use
from idfhub.idf_autocomplete.idf_helpers_short import (
    Timestep, Version, Simulationcontrol,
    SiteGroundtemperatureUndisturbedKusudaachenbach,
    Scheduletypelimits, ScheduleConstant,
    ScheduleCompact,
    ThermostatsetpointDualsetpoint, ZonecontrolThermostat,
    CurveQuadlinear,
    HeatpumpWatertowaterEquationfitHeating,
    SiteGroundtemperatureDeep
)
from idfhub.idf_autocomplete.idf_types_short import (
    TimestepType, VersionType, SimulationcontrolType,
    SiteGroundtemperatureUndisturbedKusudaachenbachType,
    ScheduletypelimitsType, ScheduleConstantType,
    ScheduleCompactType,
    ThermostatsetpointDualsetpointType, ZonecontrolThermostatType,
    CurveQuadlinearType,
    HeatpumpWatertowaterEquationfitHeatingType,
    SiteGroundtemperatureDeepType
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


SOIL_LOOP = "Soil Loop"
HEAT_LOOP = "Heating Loop"

soil = SiteGroundtemperatureUndisturbedKusudaachenbachType(
    Name="Sol_KA",
    Soil_Thermal_Conductivity=2.5, # W/(m K)
    Soil_Density=2000, # kg/m3
    Soil_Specific_Heat=900, # J/(kg K)
    Average_Soil_Surface_Temperature=11,
    Average_Amplitude_of_Surface_Temperature=10,
    Phase_Shift_of_Minimum_Surface_Temperature=45 #days
)
SiteGroundtemperatureUndisturbedKusudaachenbach(idf, **soil)

timestep = TimestepType(
    Number_of_Timesteps_per_Hour=6
)
Timestep(idf, **timestep)
version = VersionType()
Version(idf, **version)
simulationcontrol = SimulationcontrolType(
    Do_Zone_Sizing_Calculation="Yes",
    Do_Plant_Sizing_Calculation="Yes",
    Do_System_Sizing_Calculation="Yes",
    Do_HVAC_Sizing_Simulation_for_Sizing_Periods="Yes",
    Maximum_Number_of_HVAC_Sizing_Simulation_Passes=2
)
Simulationcontrol(idf, **simulationcontrol)

DISCRETE = "Discrete"
CONTINUOUS = "Continuous"
#---------------------------------------------------------------------------------------------------
# Schedules
# on crée 2 schedules constants, à 20°C pour le chauffage et à 25°C pour le raffraichissement :
# - const_temp_sched_20deg
# - const_temp_sched_25deg
#---------------------------------------------------------------------------------------------------
temperature_typelimits = ScheduletypelimitsType(
    Name="temperature",
    Numeric_Type=CONTINUOUS,
    Unit_Type="Temperature"
)
Scheduletypelimits(idf, **temperature_typelimits)
on_off_typelimits = ScheduletypelimitsType(
    Name="on_off",
    Lower_Limit_Value=0,
    Upper_Limit_Value=1,
    Numeric_Type=DISCRETE,
    Unit_Type="Availability"
)
Scheduletypelimits(idf, **on_off_typelimits)
# ajout car generate_geometry produit un schedule constant qui nécessite Fractional ????
fractional_typelimits = ScheduletypelimitsType(
    Name="Fractional",
    Lower_Limit_Value=0,
    Upper_Limit_Value=1,
    Numeric_Type=CONTINUOUS,
)
Scheduletypelimits(idf, **fractional_typelimits)

def create_const_sched(temp: int):
    """create a constant schedule type"""
    return ScheduleConstantType(
        Name=f"const_temp_sched_{temp}deg",
        Schedule_Type_Limits_Name="temperature",
        Hourly_Value=temp
    )

ScheduleConstant(idf, **create_const_sched(25))
ScheduleConstant(idf, **create_const_sched(20))

#---------------------------------------------------------------------------------------------------
# End Of Schedules
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# Thermostats
#---------------------------------------------------------------------------------------------------
zone_thermostat = ThermostatsetpointDualsetpointType(
    Name="zone_thermostat",
    Heating_Setpoint_Temperature_Schedule_Name="const_temp_sched_20deg",
    Cooling_Setpoint_Temperature_Schedule_Name="const_temp_sched_25deg"
)
ThermostatsetpointDualsetpoint(idf, **zone_thermostat)

# Control types are integers: 
# 0 - Uncontrolled (floating, no thermostat),
# 1 = ThermostatSetpoint:SingleHeating,
# 2 = ThermostatSetpoint:SingleCooling,
# 3 = ThermostatSetpoint:SingleHeatingOrCooling,
# 4 = ThermostatSetpoint:DualSetpoint
control_types = ScheduletypelimitsType(
    Name="control_types",
    Lower_Limit_Value=0,
    Upper_Limit_Value=4,
    Numeric_Type=DISCRETE
)
Scheduletypelimits(idf, **control_types)

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
control_type_schedule = ScheduleCompactType(
    Name="control_type_schedule",
    Schedule_Type_Limits_Name="control_types",
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
    Field_11=0
)
ScheduleCompact(idf, **control_type_schedule)

rdc_thermostat = ZonecontrolThermostatType(
    Name="RDC_thermostat",
    Zone_or_ZoneList_Name="RDC",
    Control_Type_Schedule_Name="control_type_schedule",
    Control_1_Object_Type="ThermostatSetpoint:DualSetpoint",
    Control_1_Name="zone_thermostat"
)
ZonecontrolThermostat(idf, **rdc_thermostat)

rplus1_thermostat = ZonecontrolThermostatType(
    Name="RPLUS1_thermostat",
    Zone_or_ZoneList_Name="RPLUS1",
    Control_Type_Schedule_Name="control_type_schedule",
    Control_1_Object_Type="ThermostatSetpoint:DualSetpoint",
    Control_1_Name="zone_thermostat"
)
ZonecontrolThermostat(idf, **rplus1_thermostat)
#---------------------------------------------------------------------------------------------------
# End Of Thermostats
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# Plant Loops
#---------------------------------------------------------------------------------------------------
add_plant_loop(idf, SOIL_LOOP, 15, -5)
soil_loop_nodes = LoopNodes(SOIL_LOOP)
soil_loop_branches = Branches(SOIL_LOOP)

heating_loop = add_plant_loop(idf, HEAT_LOOP, 100, 0)
heating_loop_nodes = LoopNodes(HEAT_LOOP)
heating_loop_branches = Branches(HEAT_LOOP)

#---------------------------------------------------------------------------------------------------
# PRODUCTION SYSTEMS
#---------------------------------------------------------------------------------------------------
borehole = add_ground_exchanger(
    idf,
    "Borehole",
    soil_loop_nodes.supply_inlet,
    "Borehole outlet"
)
soil_pump = add_constant_pump(
    idf,
    f"{SOIL_LOOP} Pump",
    "Borehole outlet",
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
capacity_curve_name = f"{hpwtw_name} Heating capacity curve"
power_curve_name = f"{hpwtw_name} Heating power curve"
CurveQuadlinear(
    idf,
    **create_quadlincurve(
        capacity_curve_name,
        0.8, 0.01, 0.02, 0.03
    )
)

CurveQuadlinear(
    idf,
    **create_quadlincurve(
        power_curve_name,
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
        Heating_Capacity_Curve_Name=capacity_curve_name,
        Heating_Compressor_Power_Curve_Name=power_curve_name
    )
)
set_nodes(
    hpwtw,
    side=EPApi.SOURCE_SIDE,
    inlet=soil_loop_nodes.demand_inlet,
    outlet=soil_loop_nodes.demand_outlet
)
set_nodes(
    hpwtw,
    side=EPApi.LOAD_SIDE,
    inlet=inside_pump[EPApi.OUTLET_NODE_NAME],
    outlet=heating_loop_nodes.supply_outlet
)

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

SiteGroundtemperatureDeep(
    idf,
    **SiteGroundtemperatureDeepType(
        January_Deep_Ground_Temperature=7.0,
        February_Deep_Ground_Temperature=8.0,
        March_Deep_Ground_Temperature=9.5,
        April_Deep_Ground_Temperature=11.0,
        May_Deep_Ground_Temperature=12.5,
        June_Deep_Ground_Temperature=13.5,
        July_Deep_Ground_Temperature=14.0,
        August_Deep_Ground_Temperature=13.8,
        September_Deep_Ground_Temperature=12.5,
        October_Deep_Ground_Temperature=10.5,
        November_Deep_Ground_Temperature=8.5,
        December_Deep_Ground_Temperature=7.5,
    )
)

idf.newidfobject(
    "SETPOINTMANAGER:FOLLOWGROUNDTEMPERATURE",
    Name="SetPoint Follow Ground Temperature",
    Control_Variable="Temperature",
    Reference_Ground_Temperature_Object_Type="Site:GroundTemperature:Deep",
    #Offset_Temperature_Difference=0,
    #Maximum_Setpoint_Temperature=60,
    #Minimum_Setpoint_Temperature=0,
    Setpoint_Node_or_NodeList_Name=soil_loop_nodes.supply_outlet
)

idf.newidfobject(
    "SIZING:PLANT",
    Plant_or_Condenser_Loop_Name=SOIL_LOOP,
    Loop_Type="Condenser",
    Design_Loop_Exit_Temperature=15,
    Loop_Design_Temperature_Difference=5,
    Sizing_Option="NonCoincident",
    Zone_Timesteps_in_Averaging_Window=1,
    #Coincident_Sizing_Factor_Mode
)

idf.newidfobject(
    "PLANTEQUIPMENTOPERATIONSCHEMES",
    Name=SOIL_LOOP,
    Control_Scheme_1_Object_Type="PlantEquipmentOperation:Uncontrolled",
    Control_Scheme_1_Name="Plant Soil Loop Uncontrolled",
    Control_Scheme_1_Schedule_Name="Always On"
)

idf.newidfobject(
    "PLANTEQUIPMENTOPERATION:UNCONTROLLED",
    Name="Plant Soil Loop Uncontrolled",
    Equipment_List_Name="Plant Soil Loop Equipment List"
)

idf.newidfobject(
    "PLANTEQUIPMENTLIST",
    Name="Plant Soil Loop Equipment List",
    Equipment_1_Object_Type="GROUNDHEATEXCHANGER:SYSTEM",
    Equipment_1_Name="Borehole"
)

#---------------------------------------------------------------------------------------------------
# EMISSION SYSTEMS
#---------------------------------------------------------------------------------------------------
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

splitter = create_splitter(
    idf,
    "demand splitter",
    [rdc_baseboard_branch, rplus1_baseboard_branch]
)
mixer = create_mixer(
    idf,
    "demand mixer",
    [rdc_baseboard_branch, rplus1_baseboard_branch]
)
create_connector_list(
    idf,
    "heating demand connector list",
    [splitter, mixer]
)
heating_loop.Demand_Side_Connector_List_Name = "heating demand connector list"

heat_loop_demand_branch = idf.getobject(
    "BRANCHLIST",
    heating_loop_branches.demand_branch_list
)
heat_loop_demand_branch.Branch_1_Name = splitter[EPApi.INLET_BRANCH_NAME]
heat_loop_demand_branch.Branch_2_Name = rdc_baseboard_branch.Name
heat_loop_demand_branch.Branch_3_Name = rplus1_baseboard_branch.Name
heat_loop_demand_branch.Branch_4_Name = mixer[EPApi.OUTLET_BRANCH_NAME]

pipe = create_pipe(
    idf,
    f"{heating_loop_nodes.demand_inlet} Pipe",
    heating_loop_nodes.demand_inlet,
    f"{heating_loop_nodes.demand_inlet} Pipe Node"
)
create_branch(
    idf,
    name = splitter[EPApi.INLET_BRANCH_NAME], 
    objects = [pipe],
    sides = [None]
)
pipe = create_pipe(
    idf,
    f"{heating_loop_nodes.demand_outlet} Pipe",
    f"{heating_loop_nodes.demand_outlet} Pipe Node",
    heating_loop_nodes.demand_outlet
)
create_branch(
    idf,
    name = mixer[EPApi.OUTLET_BRANCH_NAME],
    objects = [pipe],
    sides = [None]
)
input("press")

idf.save(f"{BUILDING_NAME}_W_HVAC.idf")
