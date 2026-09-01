"""Manage hvac topology with eppy raw layer"""
from enum import StrEnum
from dataclasses import dataclass

from eppy.modeleditor import IDF
from eppy.bunch_subclass import EpBunch

from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import (
    ConnectorMixer, ConnectorSplitter, Connectorlist, ConnectorlistMeta,
    Branchlist, BranchlistMeta,
    AirloophvacMeta, AirloophvacOutdoorairsystemMeta,
    AirloophvacOutdoorairsystemEquipmentlistMeta,
    OutdoorairMixerMeta
)

from idfhub.idf_autocomplete.v24_1_0.idf_types_short import (
    ConnectorMixerType, ConnectorSplitterType, ConnectorlistType,
    BranchlistType
)

SUPPLY = "air_supply"
RETURN = "air_return"
PLANT = "plant"
DEMAND = "demand"
INLET = "inlet"
OUTLET = "outlet"
BRANCH = "branch"
LIST = "list"
ALWAYS_ON ="Always On"

@dataclass(frozen=True)
class LoopNodes:
    """Produces generic node names for a plant or air loop"""
    name: str

    def get(self, *, side, port, end="node"):
        """get a node name on a loop side/port"""
        return f"{self.name}_{side}_{port}_{end}"
    @property
    def supply_inlet(self):
        """Supply Inlet"""
        return self.get(side=SUPPLY, port=INLET)
    @property
    def supply_outlet(self):
        "Supply Outlet"
        return self.get(side=SUPPLY, port=OUTLET)
    @property
    def supply_outlets(self):
        "Supply Outlets"
        return self.get(side=SUPPLY, port=OUTLET, end="Node_List")
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
    def demand_inlets(self):
        """Demand Inlets"""
        return self.get(side=DEMAND, port=INLET, end="Node_List")
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
        name = f"{self.name}_{side}_{BRANCH}"
        if branch_list:
            name = f"{name}_{LIST}"
        return name
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
    FRACTIONAL = "Fractional"
    CONTROL_TYPES = "Control_types"
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
    HEATING = "Heating"
    COOLING = "Cooling"
    LOAD = "Load"
    IDEAL = "Ideal"
    UNCONTROLLED_ON = "UncontrolledOn"
    LOOPTOLOOP ="LoopToLoop"

class EPApi(StrEnum):
    "EnergyPlus field names"
    INLET = "Inlet"
    OUTLET = "Outlet"
    BRANCH = "Branch"
    CONNECTOR = "Connector"
    INLET_NODE_NAMES = "Inlet_Node_Names"
    OUTLET_NODE_NAMES = "Outlet_Node_Names"
    PLANT_SIDE = "Plant_Side"
    SUPPLY_SIDE = "Supply_Side"
    DEMAND_SIDE = "Demand_Side"
    SOURCE_SIDE = "Source_Side"
    LOAD_SIDE = "Load_Side"
    INLET_BRANCH = "Inlet_Branch"
    OUTLET_BRANCH = "Outlet_Branch"
    LOOP_DEMAND_SIDE = "Loop_Demand_Side"
    LOOP_SUPPLY_SIDE = "Loop_Supply_Side"
    OUTDOOR_AIR = "Outdoor_Air"
    OUTDOOR_AIR_EQUIPMENT = "Outdoor_Air_Equipment"
    RETURN_AIR = "Return_Air"
    ACTUATOR = "Actuator"
    RELIEF_AIR = "Relief_Air"
    MIXED_AIR = "Mixed_Air"
    CONTROLLER = "Controller"
    COMPONENT = "Component"
    EQUIPMENT = "Equipment"
    CONTROL = "Control"
    DEMAND_CALCULATION = "Demand_Calculation"
    SETPOINT = "Setpoint"
    OPERATION = "Operation"
    RANGE = "Range"
    LOAD_RANGE = "Load_Range"
    DRYBULB_T_RANGE = "DryBulb_Temperature_Range"
    CONTROL_SCHEME = "Control_Scheme"
    ZONE_EQUIPMENT = "Zone_Equipment"

    @property
    def stream_node_name(self) -> str:
        """return a stream_node_name field"""
        return f"{self}_Stream_Node_Name"
    @property
    def list_name(self) -> str:
        """return a list_name field"""
        return f"{self}_List_Name"
    def node_name(self, i: int|None = None) -> str:
        """return a node_name field"""
        if i is None:
            return f"{self}_Node_Name"
        return f"{self}_{i}_Node_Name"
    def field_name(self, i: int|None = None) -> str:
        """return a name field
        EPApi.CONNECTOR.field_name(2) -> Connector_2_Name
        """
        if i is None:
            return f"{self}_Name"
        return f"{self}_{i}_Name"
    def object_type(self, i: int|None = None) -> str:
        """return a object_type field"""
        if i is None:
            return f"{self}_Object_Type"
        return f"{self}_{i}_Object_Type"
    def inlet_node_name(self, i: int|None = None) -> str:
        """return a inlet_node_name field"""
        if i is None:
            return f"{self}_Inlet_Node_Name"
        return f"{self}_{i}_Inlet_Node_Name"
    def oulet_node_name(self, i: int|None = None) -> str:
        """return a outlet_node_name field"""
        if i is None:
            return f"{self}_Outlet_Node_Name"
        return f"{self}_{i}_Outlet_Node_Name"
    def flow_rate(self, i: int) -> str:
        """return a flow_rate field"""
        return f"{self}_{i}_Flow_Rate"
    def type(self, i: int) -> str:
        """return a type field"""
        return f"{self}_{i}_Type"
    def equipment_list_name(self, i: int) -> str:
        """return a equipment_list_name field"""
        return f"{self}_{i}_Equipment_List_Name"
    def lower_limit(self, i:int) -> str:
        """return a lower_limit field"""
        return f"{self}_{i}_Lower_Limit"
    def upper_limit(self, i:int) -> str:
        """return a upper_limit field"""
        return f"{self}_{i}_Upper_Limit"
    def schedule_name(self, i:int) -> str:
        """return a schedule_name field"""
        return f"{self}_{i}_Schedule_Name"
    def heating_sequence(self, i:int) -> str:
        """return a heating_or_noload_sequence field"""
        return f"{self}_{i}_Heating_or_NoLoad_Sequence"
    def cooling_sequence(self, i:int) -> str:
        """return a cooling sequence field"""
        return f"{self}_{i}_Cooling_Sequence"


def set_nodes(
    obj: EpBunch,
    *,
    inlet: str|None,
    outlet: str|None,
    side: str|None = None
):
    """Set object nodes - loop or equipment"""
    prefix = f"{side}_" if side else ""
    inlet_field = f"{prefix}{EPApi.INLET.node_name()}"
    outlet_field = f"{prefix}{EPApi.OUTLET.node_name()}"
    if obj.key == AirloophvacMeta.idf_name:
        if side == EPApi.DEMAND_SIDE:
            inlet_field = f"{prefix}{EPApi.INLET_NODE_NAMES}"
        if side == EPApi.SUPPLY_SIDE:
            outlet_field = f"{prefix}{EPApi.OUTLET_NODE_NAMES}"
    if inlet is not None:
        obj[inlet_field] = inlet
    if outlet is not None:
        obj[outlet_field] = outlet


def node_name(branch_name: str, port: str):
    """set generic node name from a branch name"""
    return f"{object_name(branch_name)}_{port}_node"


def set_branch_list(obj, *, branch_list, side: str|None = None):
    """Set branch list on a loop side"""
    if side is None:
        obj[EPApi.BRANCH.list_name] = branch_list
    else:
        obj[f"{side}_{EPApi.BRANCH.list_name}"] = branch_list

def add_plantloop(
    idf:IDF,
    name:str,
    conf:dict
):
    """create a plant loop
    On crée les objets BRANCHLIST
    On met le setpoint sur le plant outlet"""
    nodes = LoopNodes(name)
    branches = Branches(name)
    max_t = conf.get("Maximum_Loop_Temperature", 100)
    min_t = conf.get("Minimum_Loop_Temperature", 0)

    idf.newidfobject(
        "BRANCHLIST",
        Name=branches.plant_branch_list,
    )
    idf.newidfobject(
        "BRANCHLIST",
        Name=branches.demand_branch_list,
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
        Load_Distribution_Scheme=conf.get(
            "Load_Distribution_Scheme",
            "SequentialLoad"
        )
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


def create_pipe(
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
    pipe[EPApi.INLET.node_name()] = inlet_node_name
    pipe[EPApi.OUTLET.node_name()] = outlet_node_name
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
        Availability_Schedule_Name=ALWAYS_ON,
        Rated_Average_Water_Temperature=87.78,
        Rated_Water_Mass_Flow_Rate=0.063,
        Heating_Design_Capacity=EPValues.AUTOSIZE,
        Maximum_Water_Flow_Rate=EPValues.AUTOSIZE,
    )
    zone_baseboard[EPApi.INLET.node_name()] = f"{zone_name} baseboards inlet"
    zone_baseboard[EPApi.OUTLET.node_name()] = f"{zone_name} baseboards outlet"
    surfaces = [
        s for s in idf.idfobjects["BUILDINGSURFACE:DETAILED"]
        if s.Zone_Name.lower() == zone_name.lower()
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


def get_oa_system_mixer(idf: IDF, list_name: str) -> EpBunch|None:
    """get oa system mixer regards to its equipment list
    in EnergyPlus : only a single OutdoorAir:Mixer per AirLoopHVAC:OutdoorAirSystem
    on a une equipment list qui peut référencer plusieurs mixers
    mais celà n'a pas de sens d'enchainer des mixers en série
    """
    mixer_list = idf.getobject(
        AirloophvacOutdoorairsystemEquipmentlistMeta.idf_name,
        list_name
    )
    if not mixer_list:
        return None
    mixer_name = mixer_list[EPApi.COMPONENT.field_name(1)]
    mixer = idf.getobject(
        OutdoorairMixerMeta.idf_name,
        mixer_name
    )
    return mixer


def create_branch(idf: IDF, *, name: str, objects: list[EpBunch], sides: list):
    """create a branch"""
    branch = idf.newidfobject(
        "BRANCH",
        Name=name
    )
    for i, obj in enumerate(objects):
        branch[EPApi.COMPONENT.object_type(i+1)] = obj.key
        branch[EPApi.COMPONENT.field_name(i+1)] = obj.Name
        inlet_node = EPApi.COMPONENT.inlet_node_name(i+1)
        outlet_node = EPApi.COMPONENT.oulet_node_name(i+1)
        if sides[i] is None:
            if obj.key == AirloophvacOutdoorairsystemMeta.idf_name:
                list_name = obj[EPApi.OUTDOOR_AIR_EQUIPMENT.list_name]
                mixer = get_oa_system_mixer(idf, list_name)
                if mixer:
                    branch[inlet_node] = mixer[EPApi.RETURN_AIR.stream_node_name]
                    branch[outlet_node] = mixer[EPApi.MIXED_AIR.node_name()]
            else:
                branch[inlet_node] = obj[EPApi.INLET.node_name()]
                branch[outlet_node] = obj[EPApi.OUTLET.node_name()]
        else:
            branch[inlet_node] = obj[f"{sides[i]}_{EPApi.INLET.node_name()}"]
            branch[outlet_node] = obj[f"{sides[i]}_{EPApi.OUTLET.node_name()}"]
    #print(branch)
    return branch


def object_name(branch: EpBunch|str):
    """from branch to object name"""
    branch_name = branch if isinstance(branch, str) else branch.Name
    return f"{branch_name}".replace("_branch","").strip()


def split_mix(
    idf: IDF,
    *,
    plantloop: EpBunch,
    side: str,
    inlet_branch: EpBunch,
    branches: list[EpBunch],
    outlet_branch: EpBunch
):
    """create and register split & mix connectors 
    all branches must preexist"""
    splitter = ConnectorSplitter(
        idf,
        **ConnectorSplitterType(
            Name=object_name(inlet_branch),
            Inlet_Branch_Name=inlet_branch.Name
        )
    )
    for i, branch in enumerate(branches):
        splitter[EPApi.OUTLET_BRANCH.field_name(i+1)] = branch.Name
    mixer = ConnectorMixer(
        idf,
        **ConnectorMixerType(
            Name=object_name(outlet_branch),
            Outlet_Branch_Name=outlet_branch.Name
        )
    )
    for i, branch in enumerate(branches):
        mixer[EPApi.INLET_BRANCH.field_name(i+1)] = branch.Name
    # at this stage, we should add connectors to the connector list
    # or create it if it does not exist
    connector_list_name = f"{plantloop.Name} {side} connector list"
    plantloop[f"{side}_{EPApi.CONNECTOR.list_name}"] = connector_list_name
    connector_list = idf.getobject(
        ConnectorlistMeta.idf_name,
        connector_list_name
    )
    start_index = 1
    if connector_list:
        while True:
            name = getattr(connector_list, EPApi.CONNECTOR.field_name(start_index))
            if not name:
                break
            start_index += 1
    else:
        connector_list = Connectorlist(
            idf,
            **ConnectorlistType(
                Name=connector_list_name
            )
        )
    for i, connector in enumerate([splitter, mixer]):
        connector_list[EPApi.CONNECTOR.object_type(start_index + i)] = connector.key
        connector_list[EPApi.CONNECTOR.field_name(start_index + i)] = connector.Name


def branchlist_update(
    idf: IDF,
    *,
    loop_name: str,
    loop_side: str,
    branches: list[EpBunch] | EpBunch
):
    """register a branch to the correct branchlist object"""
    # tous les objets branchlist sont crées à l'initialisation du loop
    # mais pour la robustesse, on crée la branchlist en cas de non existence
    branch_list_name = Branches(loop_name).get(side=loop_side, branch_list=True)
    branch_list = idf.getobject(
        BranchlistMeta.idf_name,
        branch_list_name
    )
    start_index = 1
    if branch_list:
        while True:
            field = EPApi.BRANCH.field_name(start_index)
            if field not in branch_list.fieldnames:
                break
            name = getattr(branch_list, field)
            if not name:
                break
            start_index += 1
    else:
        branch_list = Branchlist(
            idf,
            **BranchlistType(
                Name=branch_list_name
            )
        )
    if isinstance(branches, list):
        for i, branch in enumerate(branches):
            branch_list[EPApi.BRANCH.field_name(start_index + i)] = branch.Name
    else:
        branch_list[EPApi.BRANCH.field_name(start_index)] = branches.Name


def pipe_splitter(idf: IDF, *, inlet_node: str, branch_name: str):
    """create pipe and return a pipe splitter branch"""
    pipe_name = object_name(branch_name)
    inlet_pipe = create_pipe(
        idf,
        name=f"{pipe_name} Pipe",
        inlet_node_name=inlet_node,
        outlet_node_name=f"{pipe_name} Pipe outlet"
    )
    return create_branch(
        idf,
        name = branch_name,
        objects = [inlet_pipe],
        sides = [None]
    )


def pipe_mixer(idf:IDF, *, outlet_node: str, branch_name: str):
    """create pipe and return a pipe mixer branch"""
    pipe_name = object_name(branch_name)
    outlet_pipe = create_pipe(
        idf,
        name=f"{pipe_name} Pipe",
        inlet_node_name=f"{pipe_name} Pipe inlet",
        outlet_node_name=outlet_node
    )
    return create_branch(
        idf,
        name = branch_name,
        objects = [outlet_pipe],
        sides = [None]
    )


def get_branch_inlet_outlet_nodes(branch: EpBunch):
    """branch inlet and outlet nodes"""
    # inlet = premier composant
    inlet = getattr(branch, EPApi.COMPONENT.inlet_node_name(1), None)
    # outlet = dernier composant
    i = 1
    last_outlet = None
    while True:
        outlet = getattr(branch, EPApi.COMPONENT.oulet_node_name(i), None)
        if not outlet:
            break
        last_outlet = outlet
        i += 1
    return inlet, last_outlet
