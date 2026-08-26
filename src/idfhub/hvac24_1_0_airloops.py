"""air loops"""
from typing import Tuple
from eppy.bunch_subclass import EpBunch

from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import (
    Airloophvac,
    Branchlist,
    Nodelist,
    AirloophvacZonesplitter,AirloophvacSupplypath,
    AirloophvacZonemixer,AirloophvacReturnpath,
    FanConstantvolume,
    ZonehvacAirdistributionunit,
    AirterminalSingleductConstantvolumeNoreheat,
)

from idfhub.idf_autocomplete.v24_1_0.idf_types_short import (
    AirloophvacType,
    BranchlistType,
    NodelistType,
    AirloophvacZonesplitterType,AirloophvacSupplypathType,
    AirloophvacZonemixerType,AirloophvacReturnpathType,
    FanConstantvolumeType,
    ZonehvacAirdistributionunitType,
    AirterminalSingleductConstantvolumeNoreheatType,
)

from idfhub.common import idf, CONF
from idfhub.hvac import LoopNodes, Branches, set_nodes, set_branch_list, EPApi, EPValues, ALWAYS_ON

def fan(name) -> EpBunch:
    """create a fan"""
    conf = CONF.get(name, {})
    return FanConstantvolume(
        idf,
        **FanConstantvolumeType(
            Name=name,
            Pressure_Rise=conf.get("Presure_Rise", 500),
            Maximum_Flow_Rate=EPValues.AUTOSIZE,
            Motor_Efficiency=conf.get("Motor_Efficiency", 0.9),
            Air_Inlet_Node_Name=f"{name} air inlet node",
            Air_Outlet_Node_Name=f"{name} air outlet node" 
        )
    )

def cv_no_reheat(
    name,
    * ,
    zone_air_inlet_node: str
) -> Tuple[EpBunch, EpBunch]:
    """create an CV no reheat air terminal and its air distribution unit wrapper"""
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
