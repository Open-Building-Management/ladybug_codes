"""air loops

the most basic airloop has not oamixer, oa for outdoor air,
just a terminal and its distribution wrapper on the demand side
and optionally a fan on the supply
this basic airloop is of no interest in practise
it just helps to understand the hierarchy of the main objects

next step to get something more interesting is to add a oasystem
an oasystem is a controller and an equipment
the equipment is an oamixer and the controller is an oacontroller
"""
from typing import Tuple
from eppy.bunch_subclass import BadEPFieldError, EpBunch

from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import (
    Airloophvac,
    Branchlist,
    Nodelist,
    AirloophvacZonesplitter,AirloophvacSupplypath,
    AirloophvacZonemixer,AirloophvacReturnpath,
    ZonehvacAirdistributionunit,
    AirterminalSingleductConstantvolumeNoreheat,
    HeatexchangerAirtoairSensibleandlatent,
    OutdoorairMixer,
    OutdoorairNode,
    ControllerOutdoorair,
    AirloophvacControllerlist,
    AirloophvacOutdoorairsystemEquipmentlist,
    AirloophvacOutdoorairsystem,
)

from idfhub.idf_autocomplete.v24_1_0.idf_types_short import (
    AirloophvacType,
    BranchlistType,
    NodelistType,
    AirloophvacZonesplitterType,AirloophvacSupplypathType,
    AirloophvacZonemixerType,AirloophvacReturnpathType,
    ZonehvacAirdistributionunitType,
    AirterminalSingleductConstantvolumeNoreheatType,
    HeatexchangerAirtoairSensibleandlatentType,
    OutdoorairMixerType,OutdoorairNodeType,
    ControllerOutdoorairType, AirloophvacControllerlistType,
    AirloophvacOutdoorairsystemEquipmentlistType,
    AirloophvacOutdoorairsystemType
)

from idfhub.common import idf, CONF
from idfhub.hvac import LoopNodes, Branches, set_nodes, set_branch_list, EPApi, EPValues

def cv_no_reheat(
    name,
    * ,
    zone_air_inlet_node: str
) -> Tuple[EpBunch, EpBunch]:
    """create an Constant volume (CV) no reheat air terminal and its air distribution unit wrapper"""
    terminal_name = f"{name} terminal unit"
    air_terminal = AirterminalSingleductConstantvolumeNoreheat(
        idf,
        **AirterminalSingleductConstantvolumeNoreheatType(
            Name=terminal_name,
            Air_Inlet_Node_Name=f"{terminal_name} inlet node",
            Air_Outlet_Node_Name=zone_air_inlet_node,
            Maximum_Air_Flow_Rate=EPValues.AUTOSIZE
        )
    )
    air_distribution_unit = ZonehvacAirdistributionunit(
        idf,
        **ZonehvacAirdistributionunitType(
            Name=name,
            Air_Distribution_Unit_Outlet_Node_Name=zone_air_inlet_node,
            Air_Terminal_Object_Type=air_terminal.key,
            Air_Terminal_Name=air_terminal.Name
        )
    )
    return air_terminal, air_distribution_unit


def oa_mixer(
    name,
    *,
    mixed_node: str|None = None,
    oa_in_node: str|None = None,
    relief_node: str|None = None,
    return_node: str|None = None,
) -> list[EpBunch]:
    """create oa mixer and node
    create controller if required in conf
    """
    if not mixed_node:
        mixed_node = f"{name}_mixed_node"
    if not oa_in_node:
        oa_in_node = f"{name}_OA_in_node"
    if not relief_node:
        relief_node = f"{name}_relief_node"
    if not return_node:
        return_node = f"{name}_return_node"
    conf = CONF.get(name, {})
    ctrl_name = conf.get("controller")
    mixer = OutdoorairMixer(
        idf,
        **OutdoorairMixerType(
            Name=name,
            Mixed_Air_Node_Name=mixed_node,
            Outdoor_Air_Stream_Node_Name=oa_in_node,
            Relief_Air_Stream_Node_Name=relief_node,
            Return_Air_Stream_Node_Name=return_node
        )
    )
    OutdoorairNode(
        idf,
        **OutdoorairNodeType(
            Name=oa_in_node
        )
    )
    if ctrl_name:
        ctrl = ControllerOutdoorair(
            idf,
            **ControllerOutdoorairType(
                Name=ctrl_name,
                Mixed_Air_Node_Name=mixed_node,
                Actuator_Node_Name=oa_in_node,
                Relief_Air_Outlet_Node_Name=relief_node,
                Return_Air_Node_Name=return_node,
                Minimum_Outdoor_Air_Flow_Rate=0,
                Maximum_Outdoor_Air_Flow_Rate=EPValues.AUTOSIZE
            )
        )
        return [mixer, ctrl]
    return [mixer]


def oa_system(
    name,
    *,
    mixer_list: list[EpBunch],
    ctrl_list: list[EpBunch]
) -> EpBunch:
    """create an oa system"""
    oas_eq_list = AirloophvacOutdoorairsystemEquipmentlist(
        idf,
        **AirloophvacOutdoorairsystemEquipmentlistType(
            Name=f"{name}_equipment_list"
        )
    )
    oas_ctrl_list = AirloophvacControllerlist(
        idf,
        **AirloophvacControllerlistType(
            Name=f"{name}_ctrl_list"
        )
    )
    for i, mixer in enumerate(mixer_list):
        oas_eq_list[EPApi.COMPONENT.field_name(i+1)] = mixer.Name
        oas_eq_list[EPApi.COMPONENT.object_type(i+1)] = mixer.key
    for i, ctrl in enumerate(ctrl_list):
        oas_ctrl_list[EPApi.CONTROLLER.field_name(i+1)] = ctrl.Name
        oas_ctrl_list[EPApi.CONTROLLER.object_type(i+1)] = ctrl.key
    return AirloophvacOutdoorairsystem(
        idf,
        **AirloophvacOutdoorairsystemType(
            Name=name,
            Controller_List_Name=oas_ctrl_list.Name,
            Outdoor_Air_Equipment_List_Name=oas_eq_list.Name
        )
    )


def add_airloop(name) -> Tuple[EpBunch, EpBunch, EpBunch]:
    """create an air loop"""
    nodes = LoopNodes(name)
    branches = Branches(name)
    airloop = Airloophvac(
        idf,
        **AirloophvacType(
            Name=name,
            Design_Supply_Air_Flow_Rate=EPValues.AUTOSIZE
        )
    )
    Branchlist(
        idf,
        **BranchlistType(
            Name=branches.supply_branch_list
        )
    )
    set_branch_list(
        airloop,
        branch_list=branches.supply_branch_list,
    )
    set_nodes(
        airloop,
        side=EPApi.SUPPLY_SIDE,
        inlet=nodes.supply_inlet,
        outlet=nodes.supply_outlets
    )
    set_nodes(
        airloop,
        side=EPApi.DEMAND_SIDE,
        inlet=nodes.demand_inlets,
        outlet=nodes.demand_outlet
    )
    Nodelist(
        idf,
        **NodelistType(
            Name=nodes.supply_outlets,
            Node_1_Name=nodes.supply_outlet
        )
    )
    Nodelist(
        idf,
        **NodelistType(
            Name=nodes.demand_inlets,
            Node_1_Name=nodes.demand_inlet
        )
    )
    # creating the zone splitter - outlet nodes to be filled 
    air_zone_splitter = AirloophvacZonesplitter(
        idf,
        **AirloophvacZonesplitterType(
            Name=f"{name} airzone splitter",
            Inlet_Node_Name=nodes.demand_inlet
        )
    )
    AirloophvacSupplypath(
        idf,
        **AirloophvacSupplypathType(
            Name=f"{name} supply path",
            Supply_Air_Path_Inlet_Node_Name=nodes.demand_inlet,
            Component_1_Object_Type=air_zone_splitter.key,
            Component_1_Name=air_zone_splitter.Name
        )
    )
    # creating the zone mixer - inlet nodes to be filled
    air_zone_mixer = AirloophvacZonemixer(
        idf,
        **AirloophvacZonemixerType(
            Name=f"{name} airzone mixer",
            Outlet_Node_Name=nodes.demand_outlet,
        )
    )
    AirloophvacReturnpath(
        idf,
        **AirloophvacReturnpathType(
            Name=f"{name} return path",
            Return_Air_Path_Outlet_Node_Name=nodes.demand_outlet,
            Component_1_Object_Type=air_zone_mixer.key,
            Component_1_Name=air_zone_mixer.Name
        )
    )
    return air_zone_splitter, air_zone_mixer, airloop
