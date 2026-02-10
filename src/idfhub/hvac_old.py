"""hvac old"""
from dataclasses import dataclass
from eppy.modeleditor import IDF

from eppy.bunch_subclass import EpBunch

from idfhub.hvac import EPApi, set_nodes_on_loop_side, LoopNodes

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


def add_watertowater_heatpump(idf: IDF, name: str):
    """Add a water to water heatpump
    l'objet heatpump est trop complexe, il vaut mieux passer par l'autocompletion
    """
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
