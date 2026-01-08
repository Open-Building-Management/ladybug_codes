"""Manage hvac with eppy raw layer"""
from enum import StrEnum
from dataclasses import dataclass

from eppy.modeleditor import IDF
from eppy.bunch_subclass import EpBunch


OS_EP_PATH = "C:/openstudioapplication-1.8.0/EnergyPlus"
IDF.setiddname(f"{OS_EP_PATH}/Energy+.idd")
idf = IDF("batiment_600m2_windows_b.idf")
print(idf.idd_version)

all_classes = idf.idfobjects
for c in sorted(all_classes):
    if "CURVE" in c:
        print(c)

CLASS_NAME = "HEATPUMP:WATERTOWATER:EQUATIONFIT:HEATING"
dummy = idf.newidfobject(CLASS_NAME)

#Liste tous les attributs existants
for attr in dummy.fieldnames:
    print(attr)

input("discovery achieved : press a key")

SOIL_LOOP = "Soil Loop"
HEAT_LOOP = "Heating Loop"
NAME = "Name"


@dataclass(frozen=True)
class LoopNodes:
    """Loop nodes management"""
    name: str

    @property
    def supply_inlet(self):
        """Supply Inlet"""
        return f"{self.name} Supply Inlet"
    @property
    def supply_outlet(self):
        "Supply Outlet"
        return f"{self.name} Supply Outlet"
    @property
    def demand_inlet(self):
        """Demand Inlet"""
        return f"{self.name} Demand Inlet"
    @property
    def demand_outlet(self):
        """Demand Outlet"""
        return f"{self.name} Demand Outlet"

@dataclass(frozen=True)
class Branches:
    """Branches Management"""
    name: str

    @property
    def supply_branch(self):
        """Supply Branch"""
        return f"{self.name} Supply Branch"
    @property
    def demand_branch(self):
        """Demand Branch"""
        return f"{self.name} Demand Branch"

    @property
    def supply_branch_list(self):
        """Supply Branch List"""
        return f"{self.supply_branch} List"
    @property
    def demand_branch_list(self):
        """Demand Branch List"""
        return f"{self.demand_branch} List"


class EPApi(StrEnum):
    "EnergyPlus consts"
    AUTOSIZE = "Autosize"
    INLET_NODE_NAME = "Inlet_Node_Name"
    OUTLET_NODE_NAME = "Outlet_Node_Name"
    PLANT_SIDE = "Plant_Side"
    DEMAND_SIDE = "Demand_Side"
    BRANCH_LIST_NAME = "Branch_List_Name"
    CONNECTOR_LIST_NAME = "Connector_List_Name"
    SOURCE_SIDE = "Source_Side"
    LOAD_SIDE = "Load_Side"

@dataclass
class NodeSetter:
    """Node setter"""
    obj: EpBunch

    def set_inlet(self, side, node):
        """set an inlet"""
        self.obj[f"{side}_{EPApi.INLET_NODE_NAME}"] = node
    def set_outlet(self, side, node):
        """set an outlet"""
        self.obj[f"{side}_{EPApi.OUTLET_NODE_NAME}"] = node


def set_nodes_on_loop_side(obj, side, *, inlet, outlet):
    """Set nodes on a loop side"""
    obj[f"{side}_{EPApi.INLET_NODE_NAME}"] = inlet
    obj[f"{side}_{EPApi.OUTLET_NODE_NAME}"] = outlet
    

def set_branch_list_on_loop_side(obj, side, *, branch_list):
    """Set branch list on a loop side"""
    obj[f"{side}_{EPApi.BRANCH_LIST_NAME}"] = branch_list


def add_plant_loop(
    name:str,
    max_t:int = 100,
    min_t:int = 0
):
    """create a plant loop
    pour la robustesse, on ne crée aucune branche
    mais on crée les objets BRANCHLIST"""
    nodes = LoopNodes(name)
    branches = Branches(name)

    idf.newidfobject(
        "BRANCHLIST",
        Name=branches.supply_branch_list,
        Branch_1_Name=branches.supply_branch,
    )
    idf.newidfobject(
        "BRANCHLIST",
        Name=branches.demand_branch_list,
        Branch_1_Name=branches.demand_branch,
    )
    plantloop = idf.newidfobject(
        "PLANTLOOP",
        Name=name,
        Fluid_Type="Water",
        #User_Defined_Fluid_Type
        Plant_Equipment_Operation_Scheme_Name=name,
        Loop_Temperature_Setpoint_Node_Name=nodes.supply_outlet,
        Maximum_Loop_Temperature=max_t,
        Minimum_Loop_Temperature=min_t,
        Maximum_Loop_Flow_Rate=EPApi.AUTOSIZE,
        Minimum_Loop_Flow_Rate=0,
        Plant_Loop_Volume="Autocalculate",
        #Plant_Side_Connector_List_Name
        #Demand_Side_Connector_List_Name
        #Load_Distribution_Scheme
        #Availability_Manager_List_Name
        #Plant_Loop_Demand_Calculation_Scheme
        #Common_Pipe_Simulation
        #Pressure_Simulation_Type
        #Loop_Circulation_Time
    )
    set_nodes_on_loop_side(
        plantloop,
        EPApi.PLANT_SIDE,
        inlet=nodes.supply_inlet,
        outlet=nodes.supply_outlet,
    )
    set_branch_list_on_loop_side(
        plantloop,
        EPApi.PLANT_SIDE,
        branch_list=branches.supply_branch_list,
    )

    set_nodes_on_loop_side(
        plantloop,
        EPApi.DEMAND_SIDE,
        inlet=nodes.demand_inlet,
        outlet=nodes.demand_outlet,
        
    )
    set_branch_list_on_loop_side(
        plantloop,
        EPApi.DEMAND_SIDE,
        branch_list=branches.demand_branch_list,
    )

    return plantloop


def create_splitter(name: str, branches: list):
    """create a splitter"""
    splitter = idf.newidfobject(
        "CONNECTOR:SPLITTER",
        Name=name,
        Inlet_Branch_Name=f"{name} inlet branch"
    )
    for i, branch in enumerate(branches):
        splitter[f"Outlet_Branch_{i+1}_Name"] = branch.Name
    return splitter


def create_mixer(name: str, branches: list):
    """create a mixer"""
    mixer = idf.newidfobject(
        "CONNECTOR:MIXER",
        Name=name,
        Outlet_Branch_Name=f"{name} outlet branch"
    )
    for i, branch in enumerate(branches):
        mixer[f"Inlet_Branch_{i+1}_Name"] = branch.Name
    return mixer


def create_connector_list(name:str, connectors: list):
    """create a connector list"""
    connector_list = idf.newidfobject(
        "CONNECTORLIST",
        Name=name
    )
    for i, connector in enumerate(connectors):
        connector_list[f"Connector_{i+1}_Object_Type"] = connector.key
        connector_list[f"Connector_{i+1}_Name"] = connector.Name
    return connector_list


def create_pipe(name: str, inlet: str, outlet: str):
    """create an adiabatic pipe"""
    pipe = idf.newidfobject(
        "PIPE:ADIABATIC",
        Name=name
    )
    pipe[EPApi.INLET_NODE_NAME] = inlet
    pipe[EPApi.OUTLET_NODE_NAME] = outlet
    return pipe


def add_constant_pump(name: str, inlet: str, outlet: str):
    """add a constant speed pump"""
    pump = idf.newidfobject(
        "PUMP:CONSTANTSPEED",
        Name=name,
        Design_Flow_Rate=EPApi.AUTOSIZE,
        Design_Pump_Head=179352,
        Design_Power_Consumption=EPApi.AUTOSIZE,
        Motor_Efficiency=0.9,
        #Fraction_of_Motor_Inefficiencies_to_Fluid_Stream
        Pump_Control_Type="Intermittent",
        #Pump_Flow_Rate_Schedule_Name
        #Pump_Curve_Name
        #Impeller_Diameter
        #Rotational_Speed
        #Zone_Name
        #Skin_Loss_Radiative_Fraction
        #Design_Power_Sizing_Method
        #Design_Electric_Power_per_Unit_Flow_Rate
        #Design_Shaft_Power_per_Unit_Flow_Rate_per_Unit_Head
        #EndUse_Subcategory
    )
    pump[EPApi.INLET_NODE_NAME] = inlet
    pump[EPApi.OUTLET_NODE_NAME] = outlet
    return pump

def add_ground_exchanger(name, inlet, outlet):
    """add a borehole ?"""
    borehole = idf.newidfobject(
        "GROUNDHEATEXCHANGER:SYSTEM",
        Name=name,
        Design_Flow_Rate=0.0033,
        Undisturbed_Ground_Temperature_Model_Type="SITE:GROUNDTEMPERATURE:UNDISTURBED:KUSUDAACHENBACH",
        Undisturbed_Ground_Temperature_Model_Name="Sol_KA",
        Ground_Thermal_Conductivity=0.692626, #W/(m K)
        Ground_Thermal_Heat_Capacity=2347000, #Pa/k = J/(m3 K)
        #GHEVerticalResponseFactors_Object_Name
        #gFunction_Calculation_Method
        #GHEVerticalArray_Object_Name
        #GHEVerticalSingle_Object_Name_1
        #GHEVerticalSingle_Object_Name_2
        #GHEVerticalSingle_Object_Name_3
        #GHEVerticalSingle_Object_Name_4
        #GHEVerticalSingle_Object_Name_5
        #GHEVerticalSingle_Object_Name_6
        #GHEVerticalSingle_Object_Name_7
        #GHEVerticalSingle_Object_Name_8
        #GHEVerticalSingle_Object_Name_9
        #GHEVerticalSingle_Object_Name_10
        #GHEVerticalSingle_Object_Name_11
        #GHEVerticalSingle_Object_Name_12
        #GHEVerticalSingle_Object_Name_13
        #GHEVerticalSingle_Object_Name_14
        #GHEVerticalSingle_Object_Name_15
        #GHEVerticalSingle_Object_Name_100
    )
    borehole[EPApi.INLET_NODE_NAME] = inlet
    borehole[EPApi.OUTLET_NODE_NAME] = outlet
    return borehole


def add_baseboard(zone_name, inlet, outlet, frac_rad=0.3, frac_rad_people=0.3):
    """Add baseboards like (radiant and convective) EU heaters"""
    idf.newidfobject(
        "ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:WATER:DESIGN",
        Name=f"{zone_name} Baseboard Design",
        #Heating_Design_Capacity_Method="HeatingDesignCapacity",
        Heating_Design_Capacity_Per_Floor_Area=0,
        Fraction_of_Autosized_Heating_Design_Capacity=1,
        Convergence_Tolerance= 0.001,
        Fraction_Radiant=frac_rad,
        Fraction_of_Radiant_Energy_Incident_on_People=frac_rad_people
    )
    zone_baseboard = idf.newidfobject(
        "ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:WATER",
        Name=f"{zone_name} Baseboard",
        Design_Object=f"{zone_name} Baseboard Design",
        Availability_Schedule_Name="Always On",
        Rated_Average_Water_Temperature=87.78,
        Rated_Water_Mass_Flow_Rate=0.063,
        Heating_Design_Capacity=EPApi.AUTOSIZE,
        Maximum_Water_Flow_Rate=EPApi.AUTOSIZE,
    )
    zone_baseboard[EPApi.INLET_NODE_NAME] = inlet
    zone_baseboard[EPApi.OUTLET_NODE_NAME] = outlet
    surfaces = [
        s for s in idf.idfobjects["BUILDINGSURFACE:DETAILED"]
        if s.Zone_Name == zone_name
    ]
    walls = [s for s in surfaces if s.Surface_Type == "Wall"]
    floors = [s for s in surfaces if s.Surface_Type == "Floor"]
    ceilings = [s for s in surfaces if s.Surface_Type == "Ceiling"]
    roofs = [s for s in surfaces if s.Surface_Type == "Roof"]
    weights = {
        "Wall": 0.7,
        "Floor": 0.2,
        "Ceiling": 0.1,
        "Roof": 0.1
    }
    nbs = {
        "Wall": len(walls),
        "Floor": len(floors),
        "Ceiling": len(ceilings),
        "Roof": len(roofs)
    }
    for i, s in enumerate(surfaces):
        zone_baseboard[f"Surface_{i+1}_Name"] = s.Name
        value = (1 -frac_rad_people) * weights[s.Surface_Type] / nbs[s.Surface_Type]
        field = f"Fraction_of_Radiant_Energy_to_Surface_{i+1}"
        zone_baseboard[field] = value
    return zone_baseboard


def add_watertowater_heatpump(name: str):
    """Add a water to water heatpump"""
    nodes = LoopNodes(name)
    heatpump = idf.newidfobject(
        "HEATPUMP:WATERTOWATER:EQUATIONFIT:HEATING",
        Name=name,
        Reference_Load_Side_Flow_Rate=EPApi.AUTOSIZE,
        Reference_Source_Side_Flow_Rate=EPApi.AUTOSIZE,
        Reference_Heating_Capacity=EPApi.AUTOSIZE,
        Reference_Heating_Power_Consumption=EPApi.AUTOSIZE,
        Heating_Capacity_Curve_Name=f"{name} - heating HeatCapCurve",
        Heating_Compressor_Power_Curve_Name=f"{name} - heating HeatCompPowerCurve",
        Reference_Coefficient_of_Performance=5,
        Sizing_Factor=1,
        #Companion_Cooling_Heat_Pump_Name
    )
    set_nodes_on_loop_side(
        heatpump,
        EPApi.SOURCE_SIDE,
        inlet=nodes.demand_inlet,
        outlet=nodes.demand_outlet
    )
    set_nodes_on_loop_side(
        heatpump,
        EPApi.LOAD_SIDE,
        inlet=nodes.supply_inlet,
        outlet=nodes.supply_outlet
    )
    return heatpump



def create_branch(name: str, objects: list[EpBunch], levels: list):
    """create a branch"""
    branch = idf.newidfobject(
        "BRANCH",
        Name=name
    )
    for i, object in enumerate(objects):
        suffix = f"Component_{i+1}"
        branch[f"{suffix}_Object_Type"] = object.key
        branch[f"{suffix}_Name"] = object.Name
        inlet_node = f"{suffix}_{EPApi.INLET_NODE_NAME}"
        outlet_node = f"{suffix}_{EPApi.OUTLET_NODE_NAME}"
        if levels[i] == None:
            branch[inlet_node] = object[EPApi.INLET_NODE_NAME]
            branch[outlet_node] = object[EPApi.OUTLET_NODE_NAME]
        else:
            branch[inlet_node] = object[f"{levels[i]}_{EPApi.INLET_NODE_NAME}"]
            branch[outlet_node] = object[f"{levels[i]}_{EPApi.OUTLET_NODE_NAME}"]
    #print(branch)
    return branch


idf.newidfobject(
    "SITE:GROUNDTEMPERATURE:UNDISTURBED:KUSUDAACHENBACH",
    Name="Sol_KA",
    Soil_Thermal_Conductivity=2.5, # W/(m K)
    Soil_Density=2000, # kg/m3
    Soil_Specific_Heat=900, # J/(kg K)
    Average_Soil_Surface_Temperature=11.0,
    Average_Amplitude_of_Surface_Temperature=10.0,
    Phase_Shift_of_Minimum_Surface_Temperature=45.0,#days
)

idf.newidfobject(
    "ZONECONTROL:THERMOSTAT:STAGEDDUALSETPOINT",
    Name="RDC dualsetpoint",
    Zone_or_ZoneList_Name="RDC",
    Number_of_Heating_Stages=1,
    Heating_Temperature_Setpoint_Schedule_Name="heating schedule",
    #Heating_Throttling_Temperature_Range
    Stage_1_Heating_Temperature_Offset=0,
    #Stage_2_Heating_Temperature_Offset
    #Stage_3_Heating_Temperature_Offset
    #Stage_4_Heating_Temperature_Offset
    Number_of_Cooling_Stages=1,
    Cooling_Temperature_Setpoint_Base_Schedule_Name="cooling schedule",
    #Cooling_Throttling_Temperature_Range
    Stage_1_Cooling_Temperature_Offset=0,
    #Stage_2_Cooling_Temperature_Offset
    #Stage_3_Cooling_Temperature_Offset
    #Stage_4_Cooling_Temperature_Offset
)

add_plant_loop(SOIL_LOOP, 15, -5)
soil_loop_nodes = LoopNodes(SOIL_LOOP)
soil_loop_branches = Branches(SOIL_LOOP)

borehole = add_ground_exchanger(
    "Borehole",
    soil_loop_nodes.supply_inlet,
    "Borehole outlet"
)
soil_pump = add_constant_pump(
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


hpwtw = add_watertowater_heatpump("HPWTW")

hpwtw.Heating_Capacity_Curve_Name = "HPWTW Heating Capacity Curve"
hpwtw.Heating_Compressor_Power_Curve_Name = "HPWTW Heating Power Curve"

create_branch(soil_loop_branches.supply_branch, [borehole, soil_pump], [None, None])
create_branch(soil_loop_branches.demand_branch, [hpwtw], ["Source_Side"])

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


heating_loop = add_plant_loop(HEAT_LOOP, 100, 0)
heating_loop_nodes = LoopNodes(HEAT_LOOP)
heating_loop_branches = Branches(HEAT_LOOP)

inside_pump = add_constant_pump(
    f"{HEAT_LOOP} Pump",
    heating_loop_nodes.supply_inlet,
    "inside pump outlet"
)

hpns = NodeSetter(hpwtw)
hpns.set_inlet(EPApi.LOAD_SIDE, "inside pump outlet")

create_branch(
    heating_loop_branches.supply_branch,
    [inside_pump, hpwtw],
    [None, "Load_Side"]
)

rplus1_baseboard = add_baseboard("RPLUS1", "rplus1 inlet", "rplus1 outlet")
rdc_baseboard = add_baseboard("RDC", "rdc inlet", "rdc outlet")

rplus1_baseboard_branch = create_branch(
    f"{heating_loop_branches.demand_branch} rplus1",
    [rplus1_baseboard],
    [None]
)
rdc_baseboard_branch = create_branch(
    f"{heating_loop_branches.demand_branch} rdc",
    [rdc_baseboard],
    [None]
)

splitter = create_splitter("demand splitter", [rdc_baseboard_branch, rplus1_baseboard_branch])
mixer = create_mixer("demand mixer", [rdc_baseboard_branch, rplus1_baseboard_branch])
create_connector_list("heating demand connector list", [splitter, mixer])
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
    f"{heating_loop_nodes.demand_inlet} Pipe",
    heating_loop_nodes.demand_inlet,
    f"{heating_loop_nodes.demand_inlet} Pipe Node"
)
create_branch("demand splitter inlet branch", [pipe], [None])
pipe = create_pipe(
    f"{heating_loop_nodes.demand_outlet} Pipe",
    f"{heating_loop_nodes.demand_outlet} Pipe Node",
    heating_loop_nodes.demand_outlet
)
create_branch("demand mixer outlet branch", [pipe], [None])
input("press")

idf.save("model_with_soil.idf")
