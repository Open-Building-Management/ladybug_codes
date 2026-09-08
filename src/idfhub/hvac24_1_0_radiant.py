"""radiant and convective baseboards"""

from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import (
    ZonehvacBaseboardRadiantconvectiveWaterDesign,
    ZonehvacBaseboardRadiantconvectiveWater,
    BuildingsurfaceDetailedMeta
)
from idfhub.idf_autocomplete.v24_1_0.idf_types_short import (
    ZonehvacBaseboardRadiantconvectiveWaterDesignType,
    ZonehvacBaseboardRadiantconvectiveWaterType
)
from idfhub.hvac import EPValues, EPApi
from idfhub.common import idf, CONF

def baseboards(equipment_name: str, zone_name):
    """Add baseboards like (radiant and convective) EU heaters"""
    conf = CONF.get(equipment_name, {})
    frac_rad = conf.get(
        "Fraction_Radiant",
        0.3
    )
    frac_rad_people = conf.get(
        "Fraction_of_Radiant_Energy_Incident_on_People",
        0.3
    )
    design = ZonehvacBaseboardRadiantconvectiveWaterDesign(
        idf,
        **ZonehvacBaseboardRadiantconvectiveWaterDesignType(
            Name = f"{equipment_name}_baseboard_design",
            Heating_Design_Capacity_Per_Floor_Area=0,
            Fraction_of_Autosized_Heating_Design_Capacity=1,
            Convergence_Tolerance=0.001,
            Fraction_Radiant=frac_rad,
            Fraction_of_Radiant_Energy_Incident_on_People=frac_rad_people
        )
    )
    zone_baseboard = ZonehvacBaseboardRadiantconvectiveWater(
        idf,
        **ZonehvacBaseboardRadiantconvectiveWaterType(
            Name=equipment_name,
            Design_Object=design.Name,
            Rated_Average_Water_Temperature=87.78,
            Rated_Water_Mass_Flow_Rate=0.063,
            Heating_Design_Capacity=EPValues.AUTOSIZE,
            Maximum_Water_Flow_Rate=EPValues.AUTOSIZE,
            Inlet_Node_Name=f"{equipment_name}_inlet_node",
            Outlet_Node_Name=f"{equipment_name}_outlet_node"
        )
    )
    surfaces = [
        s for s in idf.idfobjects[BuildingsurfaceDetailedMeta.idf_name]
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
        zone_baseboard[EPApi.SURFACE.field_name(i+1)] = s.Name
        value = (1 -frac_rad_people) * weights[s.Surface_Type] / nbs[s.Surface_Type]
        field = f"Fraction_of_Radiant_Energy_to_Surface_{i+1}"
        zone_baseboard[field] = value
    return zone_baseboard
