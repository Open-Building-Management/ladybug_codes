"""exchangers"""
from .idf_autocomplete.idf_helpers_short import (
    HeatexchangerFluidtofluid
)

from .idf_autocomplete.idf_types_short import (
    HeatexchangerFluidtofluidType
)

from idfhub.hvac import EPValues
from idfhub.common import idf, CONF

def heat_exchanger(name: str):
    """fluid/fluid heat exchanger
    loop_demand > nodes on the demand side of a loop
    loop_supply > nodes on the plant side if a loop
    """
    conf = CONF.get(name, {})
    return HeatexchangerFluidtofluid(
        idf,
        **HeatexchangerFluidtofluidType(
            Name=name,
            Loop_Demand_Side_Inlet_Node_Name=f"{name} demand inlet",
            Loop_Demand_Side_Outlet_Node_Name=f"{name} demand outlet",
            Loop_Supply_Side_Inlet_Node_Name=f"{name} supply inlet",
            Loop_Supply_Side_Outlet_Node_Name=f"{name} supply outlet",
            Loop_Demand_Side_Design_Flow_Rate=EPValues.AUTOSIZE,
            Loop_Supply_Side_Design_Flow_Rate=EPValues.AUTOSIZE,
            Heat_Exchanger_UFactor_Times_Area_Value=conf.get(
                "Heat_Exchanger_UFactor_Times_Area_Value", EPValues.AUTOSIZE),
            Heat_Exchange_Model_Type=conf.get(
                "Heat_Exchanger_Model_Type", EPValues.IDEAL),
            Control_Type=conf.get(
                "Control_Type", EPValues.UNCONTROLLED_ON
            ),
            Minimum_Temperature_Difference_to_Activate_Heat_Exchanger=conf.get(
                "Minimum_Temperature_Difference_to_Activate_Heat_Exchanger", 1
            ),
            Heat_Transfer_Metering_End_Use_Type=conf.get(
                "Heat_Transfer_Metering_End_Use_Type", EPValues.LOOPTOLOOP
            ),
            Sizing_Factor=conf.get("Siaing_Factor", 1)
        )
    )
