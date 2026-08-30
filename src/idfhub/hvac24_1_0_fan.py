"""fans"""
from eppy.bunch_subclass import EpBunch

from idfhub.common import idf, CONF
from idfhub.hvac import EPValues

from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import (
    FanConstantvolume, FanSystemmodel
)
from idfhub.idf_autocomplete.v24_1_0.idf_types_short import (
    FanConstantvolumeType, FanSystemmodelType
)

def fan(
    name,
    *,
    inlet_node_name: str|None = None,
    outlet_node_name: str|None = None
) -> EpBunch:
    """create a fan
    not implemented yet : exhaust and variable
    """
    conf = CONF.get(name, {})
    if not inlet_node_name:
        inlet_node_name = f"{name}_air_inlet_node"
    if not outlet_node_name:
        outlet_node_name = f"{name}_air_outlet_node"
    if "constant" in name:
        return FanConstantvolume(
            idf,
            **FanConstantvolumeType(
                Name=name,
                Pressure_Rise=conf.get("Presure_Rise", 500),
                Maximum_Flow_Rate=EPValues.AUTOSIZE,
                Motor_Efficiency=conf.get("Motor_Efficiency", 0.9),
                Air_Inlet_Node_Name=inlet_node_name,
                Air_Outlet_Node_Name=outlet_node_name 
            )
        )
    if "system" in name:
        return FanSystemmodel(
            idf,
            **FanSystemmodelType(
                Name=name,
                Air_Inlet_Node_Name=inlet_node_name,
                Air_Outlet_Node_Name=outlet_node_name,
                Design_Maximum_Air_Flow_Rate=EPValues.AUTOSIZE,
                Design_Pressure_Rise=conf.get("Design_Presure_Rise", 120),
                Motor_Efficiency=conf.get("Motor_Efficiency", 0.8),
                Number_of_Speeds=3,
                Speed_1_Flow_Fraction=0.33,
                Speed_2_Flow_Fraction=0.66,
                Speed_3_Flow_Fraction=1,
                Speed_1_Electric_Power_Fraction=0.3,
                Speed_2_Electric_Power_Fraction=0.65,
                Speed_3_Electric_Power_Fraction=1
            )
        )
