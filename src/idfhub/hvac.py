"""Manage hvac topology with eppy raw layer"""
from enum import StrEnum
from dataclasses import dataclass

from eppy.modeleditor import IDF
from eppy.bunch_subclass import EpBunch

SUPPLY = "air_supply"
RETURN = "air_return"
PLANT = "plant"
DEMAND = "demand"
INLET = "inlet"
OUTLET = "outlet"
BRANCH = "branch"
LIST = "list"

@dataclass(frozen=True)
class LoopNodes:
    """Produces generic node names for a plant or air loop"""
    name: str

    def get(self, *, side, port):
        """get a node name on a loop side/port"""
        return f"{self.name} {side} {port}"
    @property
    def supply_inlet(self):
        """Supply Inlet"""
        return self.get(side=SUPPLY, port=INLET)
    @property
    def supply_outlet(self):
        "Supply Outlet"
        return self.get(side=SUPPLY, port=OUTLET)
    @property
    def return_inlet(self):
        """Return Inlet"""
        return self.get(side=RETURN, port=INLET)
    @property
    def return_outlet(self):
        "Return Outlet"
        return self.get(side=RETURN, port=OUTLET)
    @property
    def plant_inlet(self):
        """Plant Inlet"""
        return self.get(side=PLANT, port=INLET)
    @property
    def plant_outlet(self):
        "Plant Outlet"
        return self.get(side=PLANT, port=OUTLET)
    @property
    def demand_inlet(self):
        """Demand Inlet"""
        return self.get(side=DEMAND, port=INLET)
    @property
    def demand_outlet(self):
        """Demand Outlet"""
        return self.get(side=DEMAND, port=OUTLET)

@dataclass(frozen=True)
class Branches:
    """Produces generic branch names for a plant or air loop"""
    name: str

    def get(self, *, side, branch_list=False):
        """get a branch or branch list name on a loop side"""
        end = "" if not branch_list else LIST
        return f"{self.name} {side} {BRANCH} {end}".strip()
    @property
    def supply_branch(self):
        """Supply Branch"""
        return self.get(side=SUPPLY)
    @property
    def return_branch(self):
        """Return Branch"""
        return self.get(side=RETURN)
    @property
    def plant_branch(self):
        """Plant Branch"""
        return self.get(side=PLANT)
    @property
    def demand_branch(self):
        """Demand Branch"""
        return self.get(side=DEMAND)
    @property
    def supply_branch_list(self):
        """Supply Branch List"""
        return self.get(side=SUPPLY, branch_list=True)
    @property
    def return_branch_list(self):
        """Return Branch List"""
        return self.get(side=RETURN, branch_list=True)
    @property
    def plant_branch_list(self):
        """Plant Branch List"""
        return self.get(side=PLANT, branch_list=True)
    @property
    def demand_branch_list(self):
        """Demand Branch List"""
        return self.get(side=DEMAND, branch_list=True)

class EPValues(StrEnum):
    """EnergyPlus possible values"""
    AUTOSIZE = "Autosize"
    AUTOCALCULATE = "Autocalculate"
    DISCRETE = "Discrete"
    CONTINUOUS = "Continuous"
    INTERMITTENT = "Intermittent"
    TEMPERATURE = "Temperature"
    DIMENSIONLESS = "Dimensionless"
    WEEKDAYS = "Weekdays"
    WEEKENDS = "Weekends"
    ALLDAYS = "AllDays"
    SUMMER_DESIGN_DAY = "SummerDesignDay"
    WINTER_DESIGN_DAY = "WinterDesignDay"
    CUSTOM_DAY = "CustomDay1/2"
    THROUGH = "Through"
    FOR = "For"
    UNTIL = "Until"
    YES = "Yes"

class EPApi(StrEnum):
    "EnergyPlus consts"
    INLET_NODE_NAME = "Inlet_Node_Name"
    OUTLET_NODE_NAME = "Outlet_Node_Name"
    PLANT_SIDE = "Plant_Side"
    DEMAND_SIDE = "Demand_Side"
    BRANCH_LIST_NAME = "Branch_List_Name"
    CONNECTOR_LIST_NAME = "Connector_List_Name"
    SOURCE_SIDE = "Source_Side"
    LOAD_SIDE = "Load_Side"
    INLET_BRANCH_NAME = "Inlet_Branch_Name"
    OUTLET_BRANCH_NAME = "Outlet_Branch_Name"


def set_nodes(obj, *, inlet: str|None, outlet: str|None, side: str|None = None):
    """Set object nodes - loop or equipment"""
    prefix = f"{side}_" if side else ""
    if inlet is not None:
        obj[f"{prefix}{EPApi.INLET_NODE_NAME}"] = inlet
    if outlet is not None:
        obj[f"{prefix}{EPApi.OUTLET_NODE_NAME}"] = outlet


def set_branch_list(obj, *, side, branch_list):
    """Set branch list on a loop side"""
    obj[f"{side}_{EPApi.BRANCH_LIST_NAME}"] = branch_list


def add_plantloop(
    idf:IDF,
    name:str,
    max_t:int = 100,
    min_t:int = 0
):
    """create a plant loop
    On crée les objets BRANCHLIST
    On met le setpoint sur le plant outlet"""
    nodes = LoopNodes(name)
    branches = Branches(name)

    idf.newidfobject(
        "BRANCHLIST",
        Name=branches.plant_branch_list,
        Branch_1_Name=branches.plant_branch,
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
        Loop_Temperature_Setpoint_Node_Name=nodes.plant_outlet,
        Maximum_Loop_Temperature=max_t,
        Minimum_Loop_Temperature=min_t,
        Maximum_Loop_Flow_Rate=EPValues.AUTOSIZE,
        Minimum_Loop_Flow_Rate=0,
        Plant_Loop_Volume=EPValues.AUTOCALCULATE,
        #Plant_Side_Connector_List_Name
        #Demand_Side_Connector_List_Name
        #Load_Distribution_Scheme
        #Availability_Manager_List_Name
        #Plant_Loop_Demand_Calculation_Scheme
        #Common_Pipe_Simulation
        #Pressure_Simulation_Type
        #Loop_Circulation_Time
    )
    set_nodes(
        plantloop,
        side=EPApi.PLANT_SIDE,
        inlet=nodes.plant_inlet,
        outlet=nodes.plant_outlet,
    )
    set_branch_list(
        plantloop,
        side=EPApi.PLANT_SIDE,
        branch_list=branches.plant_branch_list,
    )

    set_nodes(
        plantloop,
        side=EPApi.DEMAND_SIDE,
        inlet=nodes.demand_inlet,
        outlet=nodes.demand_outlet,

    )
    set_branch_list(
        plantloop,
        side=EPApi.DEMAND_SIDE,
        branch_list=branches.demand_branch_list,
    )

    return plantloop


def _create_splitter(idf: IDF, *, name: str, branches: list):
    """create a splitter"""
    splitter = idf.newidfobject(
        "CONNECTOR:SPLITTER",
        Name=name
    )
    splitter[EPApi.INLET_BRANCH_NAME] = f"{name} inlet branch"
    for i, branch in enumerate(branches):
        splitter[f"Outlet_Branch_{i+1}_Name"] = branch.Name
    return splitter


def _create_mixer(idf: IDF, *, name: str, branches: list):
    """create a mixer"""
    mixer = idf.newidfobject(
        "CONNECTOR:MIXER",
        Name=name
    )
    mixer[EPApi.OUTLET_BRANCH_NAME] = f"{name} outlet branch"
    for i, branch in enumerate(branches):
        mixer[f"Inlet_Branch_{i+1}_Name"] = branch.Name
    return mixer


def _create_connector_list(idf: IDF, *, name:str, connectors: list):
    """create a connector list"""
    connector_list = idf.newidfobject(
        "CONNECTORLIST",
        Name=name
    )
    for i, connector in enumerate(connectors):
        connector_list[f"Connector_{i+1}_Object_Type"] = connector.key
        connector_list[f"Connector_{i+1}_Name"] = connector.Name
    return connector_list


def _create_pipe(
    idf: IDF,
    *,
    name: str,
    inlet_node_name: str,
    outlet_node_name: str
):
    """create an adiabatic pipe"""
    pipe = idf.newidfobject(
        "PIPE:ADIABATIC",
        Name=name
    )
    pipe[EPApi.INLET_NODE_NAME] = inlet_node_name
    pipe[EPApi.OUTLET_NODE_NAME] = outlet_node_name
    return pipe


def add_baseboard(idf: IDF, zone_name, frac_rad=0.3, frac_rad_people=0.3):
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
        Heating_Design_Capacity=EPValues.AUTOSIZE,
        Maximum_Water_Flow_Rate=EPValues.AUTOSIZE,
    )
    zone_baseboard[EPApi.INLET_NODE_NAME] = f"{zone_name} baseboards inlet"
    zone_baseboard[EPApi.OUTLET_NODE_NAME] = f"{zone_name} baseboards outlet"
    surfaces = [
        s for s in idf.idfobjects["BUILDINGSURFACE:DETAILED"]
        if s.Zone_Name == zone_name
    ]
    walls = [s for s in surfaces if s.Surface_Type == "Wall"]
    floors = [s for s in surfaces if s.Surface_Type == "Floor"]
    ceilings = [s for s in surfaces if s.Surface_Type == "Ceiling"]
    roofs = [s for s in surfaces if s.Surface_Type == "Roof"]
    nbs = {
        "Wall": len(walls),
        "Floor": len(floors),
        "Ceiling": len(ceilings),
        "Roof": len(roofs)
    }
    w_ceiling = 0.1
    w_roof = 0.1
    if nbs["Ceiling"] and not nbs["Roof"]:
        w_ceiling = 0.2
        w_roof = 0
    if nbs["Roof"] and not nbs["Ceiling"]:
        w_ceiling = 0
        w_roof = 0.2
    weights = {
        "Wall": 0.6,
        "Floor": 0.2,
        "Ceiling": w_ceiling,
        "Roof": w_roof
    }
    for i, s in enumerate(surfaces):
        zone_baseboard[f"Surface_{i+1}_Name"] = s.Name
        value = (1 -frac_rad_people) * weights[s.Surface_Type] / nbs[s.Surface_Type]
        field = f"Fraction_of_Radiant_Energy_to_Surface_{i+1}"
        zone_baseboard[field] = value
    return zone_baseboard


def create_branch(idf: IDF, *, name: str, objects: list[EpBunch], sides: list):
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
        if sides[i] is None:
            branch[inlet_node] = obj[EPApi.INLET_NODE_NAME]
            branch[outlet_node] = obj[EPApi.OUTLET_NODE_NAME]
        else:
            branch[inlet_node] = obj[f"{sides[i]}_{EPApi.INLET_NODE_NAME}"]
            branch[outlet_node] = obj[f"{sides[i]}_{EPApi.OUTLET_NODE_NAME}"]
    #print(branch)
    return branch


def plantloop_split_mix(
    idf: IDF,
    *,
    plantloop:EpBunch,
    side: str,
    branches: list[EpBunch],
    bypass: bool = False
):
    """split to branches and mix on a side of a plantloop"""
    if bypass:
        # add a bypass branch if needed
        bypass_name = f"{plantloop.Name} {side} bypass pipe"
        bypass_pipe = _create_pipe(
            idf,
            name=bypass_name,
            inlet_node_name=f"{bypass_name} inlet node",
            outlet_node_name=f"{bypass_name} outlet node"
        )
        bypass_branch = create_branch(
            idf,
            name = f"{bypass_name} branch",
            objects = [bypass_pipe],
            sides = [None]
        )
        branches.append(bypass_branch)
    splitter = _create_splitter(
        idf,
        name=f"{plantloop.Name} {side} splitter",
        branches=branches
    )
    mixer = _create_mixer(
        idf,
        name=f"{plantloop.Name} {side} mixer",
        branches=branches
    )
    connector_list_name = f"{plantloop.Name} {side} connector list"
    _create_connector_list(
        idf,
        name=connector_list_name,
        connectors=[splitter, mixer]
    )
    plantloop[f"{side}_{EPApi.CONNECTOR_LIST_NAME}"] = connector_list_name
    # on récupère la branchlist du plantloop pour mise à jour !
    plantloop_branch_list = idf.getobject(
        "BRANCHLIST",
        plantloop[f"{side}_{EPApi.BRANCH_LIST_NAME}"]
    )
    i = 1
    plantloop_branch_list[f"Branch_{i}_Name"] = splitter[EPApi.INLET_BRANCH_NAME]
    for branch in branches:
        i += 1
        plantloop_branch_list[f"Branch_{i}_Name"] = branch.Name
    i += 1
    plantloop_branch_list[f"Branch_{i}_Name"] = mixer[EPApi.OUTLET_BRANCH_NAME]
    plantloop_inlet_node_name = plantloop[f"{side}_{EPApi.INLET_NODE_NAME}"]
    inlet_pipe = _create_pipe(
        idf,
        name=f"{plantloop_inlet_node_name} Pipe",
        inlet_node_name=plantloop_inlet_node_name,
        outlet_node_name=f"{plantloop_inlet_node_name} Pipe outlet"
    )
    create_branch(
        idf,
        name = splitter[EPApi.INLET_BRANCH_NAME],
        objects = [inlet_pipe],
        sides = [None]
    )
    plantloop_outlet_node_name = plantloop[f"{side}_{EPApi.OUTLET_NODE_NAME}"]
    outlet_pipe = _create_pipe(
        idf,
        name=f"{plantloop_outlet_node_name} Pipe",
        inlet_node_name=f"{plantloop_outlet_node_name} Pipe inlet",
        outlet_node_name=plantloop_outlet_node_name
    )
    create_branch(
        idf,
        name = mixer[EPApi.OUTLET_BRANCH_NAME],
        objects = [outlet_pipe],
        sides = [None]
    )
