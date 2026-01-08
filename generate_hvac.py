""""hvac generator"""

from eppy.modeleditor import IDF

from idfhub.hvac import (
    EPApi,
    add_plant_loop, add_ground_exchanger, 
    add_constant_pump, add_watertowater_heatpump, add_baseboard,
    create_branch, create_splitter, create_mixer,
    create_pipe, create_connector_list,
    LoopNodes, Branches, NodeSetter,
)
# autocompletion use
from idfhub.helpers.consts import REPO_ROOT
from idfhub.idf_autocomplete.idf_helpers import (
    Timestep, Version, Simulationcontrol,
    SiteGroundtemperatureUndisturbedKusudaachenbach
)
from idfhub.idf_autocomplete.idf_types import (
    TimestepType, VersionType, SimulationcontrolType,
    SiteGroundtemperatureUndisturbedKusudaachenbachType
)

OS_EP_PATH = "C:/openstudioapplication-1.8.0/EnergyPlus"
IDF.setiddname(f"{OS_EP_PATH}/Energy+.idd")
idf = IDF(f"{REPO_ROOT}/batiment_600m2_windows_b.idf")
print(idf.idd_version)

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

add_plant_loop(idf, SOIL_LOOP, 15, -5)
soil_loop_nodes = LoopNodes(SOIL_LOOP)
soil_loop_branches = Branches(SOIL_LOOP)

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


idf.newidfobject(
    "CURVE:QUADLINEAR",
    Name="HPWTW Heating Capacity Curve",
    Coefficient1_Constant=0.8,
    Coefficient2_w=0.01,
    Coefficient3_x=0.02,
    Coefficient4_y=0.03,
    Coefficient5_z=0.0,
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

idf.newidfobject(
    "CURVE:QUADLINEAR",
    Name="HPWTW Heating Power Curve",
    Coefficient1_Constant=0.5,
    Coefficient2_w=0.005,
    Coefficient3_x=0.015,
    Coefficient4_y=0.02,
    Coefficient5_z=0.0,
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


hpwtw = add_watertowater_heatpump(idf, "HPWTW")

hpwtw.Heating_Capacity_Curve_Name = "HPWTW Heating Capacity Curve"
hpwtw.Heating_Compressor_Power_Curve_Name = "HPWTW Heating Power Curve"

create_branch(idf, soil_loop_branches.supply_branch, [borehole, soil_pump], [None, None])
create_branch(idf, soil_loop_branches.demand_branch, [hpwtw], ["Source_Side"])

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
    Plant_or_Condenser_Loop_Name="Soil Loop",
    Loop_Type="Condenser",
    Design_Loop_Exit_Temperature=15,
    Loop_Design_Temperature_Difference=5,
    Sizing_Option="NonCoincident",
    Zone_Timesteps_in_Averaging_Window=1,
    #Coincident_Sizing_Factor_Mode
)

idf.newidfobject(
    "PLANTEQUIPMENTOPERATIONSCHEMES",
    Name="Soil Loop",
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


heating_loop = add_plant_loop(idf, HEAT_LOOP, 100, 0)
heating_loop_nodes = LoopNodes(HEAT_LOOP)
heating_loop_branches = Branches(HEAT_LOOP)

inside_pump = add_constant_pump(
    idf,
    f"{HEAT_LOOP} Pump",
    heating_loop_nodes.supply_inlet,
    "inside pump outlet"
)

hpns = NodeSetter(hpwtw)
hpns.set_inlet(EPApi.LOAD_SIDE, "inside pump outlet")

create_branch(
    idf,
    heating_loop_branches.supply_branch,
    [inside_pump, hpwtw],
    [None, "Load_Side"]
)

rplus1_baseboard = add_baseboard(idf, "RPLUS1", "rplus1 inlet", "rplus1 outlet")
rdc_baseboard = add_baseboard(idf, "RDC", "rdc inlet", "rdc outlet")

rplus1_baseboard_branch = create_branch(
    idf,
    f"{heating_loop_branches.demand_branch} rplus1",
    [rplus1_baseboard],
    [None]
)
rdc_baseboard_branch = create_branch(
    idf,
    f"{heating_loop_branches.demand_branch} rdc",
    [rdc_baseboard],
    [None]
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
heat_loop_demand_branch.Branch_1_Name = "demand splitter inlet branch"
heat_loop_demand_branch.Branch_2_Name = rdc_baseboard_branch.Name
heat_loop_demand_branch.Branch_3_Name = rplus1_baseboard_branch.Name
heat_loop_demand_branch.Branch_4_Name = "demand mixer outlet branch"

pipe = create_pipe(
    idf,
    f"{heating_loop_nodes.demand_inlet} Pipe",
    heating_loop_nodes.demand_inlet,
    f"{heating_loop_nodes.demand_inlet} Pipe Node"
)
create_branch(idf, "demand splitter inlet branch", [pipe], [None])
pipe = create_pipe(
    idf,
    f"{heating_loop_nodes.demand_outlet} Pipe",
    f"{heating_loop_nodes.demand_outlet} Pipe Node",
    heating_loop_nodes.demand_outlet
)
create_branch(idf, "demand mixer outlet branch", [pipe], [None])
input("press")

idf.save("model_with_soil.idf")

