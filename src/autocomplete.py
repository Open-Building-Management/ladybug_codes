"""example use for autocompletion
run generate_helpers.py first !!!!!!!!!!!!!!
"""
from eppy.modeleditor import IDF
from idf_autocomplete.idf_helpers import Plantloop 
from idf_autocomplete.idf_types import PlantloopType
from helpers.consts import REPO_ROOT

# Charger ton IDF
IDF.setiddname("C:/openstudioapplication-1.8.0/EnergyPlus/Energy+.idd")
idf = IDF(f"{REPO_ROOT}/batiment_600m2_windows_b.idf")

plantloop_type = PlantloopType(
    Name="test",
    Fluid_Type="Water",
    Maximum_Loop_Temperature=100,
    Minimum_Loop_Temperature=0,
    Plant_Loop_Volume="Autocalculate",
    Plant_Side_Inlet_Node_Name="test supply inlet",
    Plant_Side_Outlet_Node_Name="test supply outlet",
    Demand_Side_Inlet_Node_Name="test demand inlet,",
    Demand_Side_Outlet_Node_Name="test demand outlet"
)
# Créer un nouvel objet Zone
new_plantloop = Plantloop(idf, **plantloop_type)

# Maintenant new_zone est un objet IDF dans ton IDF réel
print(new_plantloop)