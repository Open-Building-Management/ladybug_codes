"""PV generation"""

from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import (
    PhotovoltaicperformanceSimple,
    GeneratorPhotovoltaic,
    ZoneMeta,
    ElectricloadcenterGenerators,
    ElectricloadcenterDistribution,
    OutputVariable,
    OutputMeterCumulative,
    ShadingBuildingDetailed
)

from idfhub.idf_autocomplete.v24_1_0.idf_types_short import (
    PhotovoltaicperformanceSimpleType,
    GeneratorPhotovoltaicType,
    ElectricloadcenterGeneratorsType,
    ElectricloadcenterDistributionType,
    OutputVariableType,
    OutputMeterCumulativeType,
    ShadingBuildingDetailedType
)

from idfhub.helpers.geometry import get_variables, eval_expr
from idfhub.common import idf, CONF

def surface(equipment_name):
    """get surface name for a photovoltaic equipment
    create the surface if needed"""
    conf = CONF.get(equipment_name, {})
    variables = get_variables(conf)
    shading_surface = conf.get("surface")
    surface_name: str | None = None
    if shading_surface:
        surface_name = f"{equipment_name} dedicated surface"
        pv_surf = ShadingBuildingDetailed(
            idf,
            **ShadingBuildingDetailedType(
                Name=surface_name,
                Number_of_Vertices=4,
            )
        )
        for i, point in enumerate(shading_surface):
            for j, axis in enumerate(["X", "Y", "Z"]):
                try:
                    pv_surf[f"Vertex_{i+1}_{axis}coordinate"] = eval_expr(
                        point[j],
                        variables=variables
                    )
                except AttributeError:
                    pv_surf[f"Vertex_{i+1}_{axis}coordinate"] = point[j]
        if len(shading_surface):
            return surface_name
    try:
        zone_name = equipment_name.split("_")[1]
    except IndexError:
        return surface_name
    zone = idf.getobject(
        ZoneMeta.idf_name,
        zone_name
    )
    if zone:
        surfaces = [
            s for s in idf.idfobjects["BUILDINGSURFACE:DETAILED"]
            if s.Zone_Name.lower() == zone_name.lower()
            and s.Surface_Type == "Roof"
        ]
        if surfaces:
            return surfaces[0].Name
    return surface_name


def PV_plant(equipment_name):
    """create a photovoltaic production plant"""    
    surface_name = surface(equipment_name)
    if surface_name:
        conf = CONF.get(equipment_name, {})
        pv_perf = PhotovoltaicperformanceSimple(
            idf,
            **PhotovoltaicperformanceSimpleType(
                Name=f"{equipment_name} performance",
                Fraction_of_Surface_Area_with_Active_Solar_Cells=conf.get(
                    "Fraction_of_Surface_Area_with_Active_Solar_Cells",
                    0.8
                ),
                Conversion_Efficiency_Input_Mode="Fixed",
                Value_for_Cell_Efficiency_if_Fixed=conf.get(
                    "Value_for_Cell_Efficiency_if_Fixed",
                    0.18
                )
            )
        )
        pv_array = GeneratorPhotovoltaic(
            idf,
            **GeneratorPhotovoltaicType(
                Name=f"{equipment_name} PV array",
                Surface_Name = surface_name,
                Photovoltaic_Performance_Object_Type=pv_perf.key,
                Module_Performance_Name=pv_perf.Name
            )
        )
        pv_list = ElectricloadcenterGenerators(
            idf,
            **ElectricloadcenterGeneratorsType(
                Name=f"{equipment_name} list of generators",
                Generator_1_Name=pv_array.Name,
                Generator_1_Object_Type=pv_array.key
            )
        )
        ElectricloadcenterDistribution(
            idf,
            **ElectricloadcenterDistributionType(
                Name=f"{equipment_name} electric distribution",
                Generator_List_Name=pv_list.Name,
                Generator_Operation_Scheme_Type="Baseload"
            )
        )
        OutputMeterCumulative(
            idf,
            **OutputMeterCumulativeType(
                Key_Name="Photovoltaic:ElectricityProduced",
                Reporting_Frequency="Hourly"
            )
        )
        # Generator Produced DC Electricity Rate ou Energy
        OutputVariable(
            idf,
            **OutputVariableType(
                Key_Value=pv_array.Name,
                Variable_Name="Generator Produced DC Electricity Rate",
                Reporting_Frequency="Timestep"
            )
        )
        OutputVariable(
            idf,
            **OutputVariableType(
                Key_Value=pv_array.Name,
                Variable_Name="Generator Produced DC Electricity Energy",
                Reporting_Frequency="Timestep"
            )
        )
