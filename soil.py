"""complètement idiot - revient à dire on force l’eau à la température du sol
on pourrait néanmoins garder ground_temperature pour l'enveloppe du bâtiment
utile si :
- géothermie
- bâtiment semi-enterré
- sous-sol chauffé
- étude fine pertes plancher 
"""

from idfhub.idf_autocomplete.idf_helpers_short import SiteGroundtemperatureDeep
from idfhub.idf_autocomplete.idf_types_short import SiteGroundtemperatureDeepType
from idfhub.hvac import LoopNodes

from common import idf
SOIL_LOOP = "Soil Loop"
soil_loop_nodes = LoopNodes(SOIL_LOOP)

ground_temperature = SiteGroundtemperatureDeep(
    idf,
    **SiteGroundtemperatureDeepType(
        January_Deep_Ground_Temperature=7.0,
        February_Deep_Ground_Temperature=8.0,
        March_Deep_Ground_Temperature=9.5,
        April_Deep_Ground_Temperature=11.0,
        May_Deep_Ground_Temperature=12.5,
        June_Deep_Ground_Temperature=13.5,
        July_Deep_Ground_Temperature=14.0,
        August_Deep_Ground_Temperature=13.8,
        September_Deep_Ground_Temperature=12.5,
        October_Deep_Ground_Temperature=10.5,
        November_Deep_Ground_Temperature=8.5,
        December_Deep_Ground_Temperature=7.5,
    )
)

idf.newidfobject(
    "SETPOINTMANAGER:FOLLOWGROUNDTEMPERATURE",
    Name="SetPoint Follow Ground Temperature",
    Control_Variable="Temperature",
    Reference_Ground_Temperature_Object_Type=ground_temperature.key,
    #Offset_Temperature_Difference=0,
    #Maximum_Setpoint_Temperature=60,
    #Minimum_Setpoint_Temperature=0,
    Setpoint_Node_or_NodeList_Name=soil_loop_nodes.supply_outlet
)