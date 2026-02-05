"""Manage hvac with eppy raw layer"""
from enum import StrEnum
from dataclasses import dataclass

from eppy.modeleditor import IDF
from eppy.bunch_subclass import EpBunch

KUSUDAACHENBACH = "SITE:GROUNDTEMPERATURE:UNDISTURBED:KUSUDAACHENBACH"

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
    idf:IDF,
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


def create_splitter(idf: IDF, name: str, branches: list):
    """create a splitter"""
    splitter = idf.newidfobject(
        "CONNECTOR:SPLITTER",
        Name=name,
        Inlet_Branch_Name=f"{name} inlet branch"
    )
    for i, branch in enumerate(branches):
        splitter[f"Outlet_Branch_{i+1}_Name"] = branch.Name
    return splitter


def create_mixer(idf: IDF, name: str, branches: list):
    """create a mixer"""
    mixer = idf.newidfobject(
        "CONNECTOR:MIXER",
        Name=name,
        Outlet_Branch_Name=f"{name} outlet branch"
    )
    for i, branch in enumerate(branches):
        mixer[f"Inlet_Branch_{i+1}_Name"] = branch.Name
    return mixer


def create_connector_list(idf: IDF, name:str, connectors: list):
    """create a connector list"""
    connector_list = idf.newidfobject(
        "CONNECTORLIST",
        Name=name
    )
    for i, connector in enumerate(connectors):
        connector_list[f"Connector_{i+1}_Object_Type"] = connector.key
        connector_list[f"Connector_{i+1}_Name"] = connector.Name
    return connector_list


def create_pipe(idf: IDF, name: str, inlet: str, outlet: str):
    """create an adiabatic pipe"""
    pipe = idf.newidfobject(
        "PIPE:ADIABATIC",
        Name=name
    )
    pipe[EPApi.INLET_NODE_NAME] = inlet
    pipe[EPApi.OUTLET_NODE_NAME] = outlet
    return pipe


def add_constant_pump(idf: IDF, name: str, inlet: str, outlet: str):
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

def add_ground_exchanger(idf: IDF, name, inlet, outlet):
    """add a borehole ?"""
    borehole = idf.newidfobject(
        "GROUNDHEATEXCHANGER:SYSTEM",
        Name=name,
        Design_Flow_Rate=0.0033,
        Undisturbed_Ground_Temperature_Model_Type=KUSUDAACHENBACH,
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


def add_baseboard(idf: IDF, zone_name, inlet, outlet, frac_rad=0.3, frac_rad_people=0.3):
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


def add_watertowater_heatpump(idf: IDF, name: str):
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



def create_branch(idf: IDF, name: str, objects: list[EpBunch], levels: list):
    """create a branch"""
    branch = idf.newidfobject(
        "BRANCH",
        Name=name
    )
    for i, obj in enumerate(objects):
        suffix = f"Component_{i+1}"
        branch[f"{suffix}_Object_Type"] = obj.key
        branch[f"{suffix}_Name"] = obj.Name
        inlet_node = f"{suffix}_{EPApi.INLET_NODE_NAME}"
        outlet_node = f"{suffix}_{EPApi.OUTLET_NODE_NAME}"
        if levels[i] is None:
            branch[inlet_node] = obj[EPApi.INLET_NODE_NAME]
            branch[outlet_node] = obj[EPApi.OUTLET_NODE_NAME]
        else:
            branch[inlet_node] = obj[f"{levels[i]}_{EPApi.INLET_NODE_NAME}"]
            branch[outlet_node] = obj[f"{levels[i]}_{EPApi.OUTLET_NODE_NAME}"]
    #print(branch)
    return branch
