"""Manage geothermal systems and ground heat exchangers"""

from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import (
    SiteGroundtemperatureBuildingsurface,
    SiteGroundtemperatureDeep,
    SiteGroundtemperatureUndisturbedKusudaachenbach,
    GroundheatexchangerVerticalProperties,
    GroundheatexchangerVerticalArray,
    GroundheatexchangerSystem,
)

from idfhub.idf_autocomplete.v24_1_0.idf_types_short import (
    SiteGroundtemperatureBuildingsurfaceType,
    SiteGroundtemperatureDeepType,
    SiteGroundtemperatureUndisturbedKusudaachenbachType,
    GroundheatexchangerVerticalPropertiesType,
    GroundheatexchangerVerticalArrayType,
    GroundheatexchangerSystemType,
)

from idfhub.common import idf, CONF


def deep_ground_temperature():
    """deep ground -> values from energyplus examples ?"""
    SiteGroundtemperatureDeep(
        idf,
        **SiteGroundtemperatureDeepType(
            January_Deep_Ground_Temperature=13.03,
            February_Deep_Ground_Temperature=13.03,
            March_Deep_Ground_Temperature=12.13,
            April_Deep_Ground_Temperature=13.3,
            May_Deep_Ground_Temperature=13.43,
            June_Deep_Ground_Temperature=13.52,
            July_Deep_Ground_Temperature=13.62,
            August_Deep_Ground_Temperature=13.77,
            September_Deep_Ground_Temperature=13.78,
            October_Deep_Ground_Temperature=13.55,
            November_Deep_Ground_Temperature=13.44,
            December_Deep_Ground_Temperature=13.2
        )
    )


def ground_temperature():
    """create a basic ground temperature for the building"""
    SiteGroundtemperatureBuildingsurface(
        idf,
        **SiteGroundtemperatureBuildingsurfaceType(
            January_Ground_Temperature=7.0,
            February_Ground_Temperature=8.0,
            March_Ground_Temperature=9.5,
            April_Ground_Temperature=11.0,
            May_Ground_Temperature=12.5,
            June_Ground_Temperature=13.5,
            July_Ground_Temperature=14.0,
            August_Ground_Temperature=13.8,
            September_Ground_Temperature=12.5,
            October_Ground_Temperature=10.5,
            November_Ground_Temperature=8.5,
            December_Ground_Temperature=7.5,
        )
    )


def vertical_geoexchanger(name: str):
    """add a geoexchanger with vertical boreholes"""
    conf = CONF.get(name, {})
    # conductivité en W/(m K) - 0.69 serait une valeur médiocre
    conductivity = conf.get("Soil_Thermal_Conductivity", 2.5)
    soil_density = conf.get("Soil_Density", 2000) # kg/m3
    specific_heat = conf.get("Soil_Specific_Heat", 900)  # J/(kg K)
    soil = SiteGroundtemperatureUndisturbedKusudaachenbach(
        idf,
        **SiteGroundtemperatureUndisturbedKusudaachenbachType(
            Name="Sol_KA",
            Soil_Thermal_Conductivity=conductivity,
            Soil_Density=soil_density,
            Soil_Specific_Heat=specific_heat,
            Average_Soil_Surface_Temperature=11,
            Average_Amplitude_of_Surface_Temperature=10,
            Phase_Shift_of_Minimum_Surface_Temperature=45  # days
        )
    )
    hole = GroundheatexchangerVerticalProperties(
        idf,
        **GroundheatexchangerVerticalPropertiesType(
            Name=f"single vertical hole for {name}",
            Depth_of_Top_of_Borehole=0,
            Borehole_Length=conf.get("Borehole_Length", 100),
            Borehole_Diameter=0.15,
            Grout_Thermal_Conductivity=1.2,  # W / (m K)
            Grout_Thermal_Heat_Capacity=3.0e6,  # J / (m3 K)
            Pipe_Thermal_Conductivity=0.4,
            Pipe_Thermal_Heat_Capacity=2.0e6,
            Pipe_Thickness=0.003,
            Pipe_Outer_Diameter=0.032,
            UTube_Distance=0.055,
        )
    )

    boreholes = GroundheatexchangerVerticalArray(
        idf,
        **GroundheatexchangerVerticalArrayType(
            Name=f"{name} field array",
            GHEVerticalProperties_Object_Name=hole.Name,
            Number_of_Boreholes_in_XDirection=conf.get(
                "Number_of_Boreholes_in_XDirection", 5),
            Number_of_Boreholes_in_YDirection=conf.get(
                "Number_of_Boreholes_in_YDirection", 2),
            Borehole_Spacing=conf.get(
                "Borehole_Spacing",6)
        )
    )

    # 0.0033*3600 m3/h soit 11,88 m3/h pour 10 forages, soit 1.2 m3/h par forage
    return GroundheatexchangerSystem(
        idf,
        **GroundheatexchangerSystemType(
            Name=name,
            Inlet_Node_Name=f"{name}_inlet_node",
            Outlet_Node_Name=f"{name}_outlet_node",
            Design_Flow_Rate=0.006,  # m3/s before 0.0033
            Undisturbed_Ground_Temperature_Model_Name=soil.Name,
            Undisturbed_Ground_Temperature_Model_Type=soil.key,
            Ground_Thermal_Conductivity=conductivity,
            Ground_Thermal_Heat_Capacity=soil_density*specific_heat,  # Pa/K = J / (m3 K)
            GHEVerticalArray_Object_Name=boreholes.Name
        )
    )
