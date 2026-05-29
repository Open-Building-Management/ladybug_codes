"""Manage hvac heat pumps and geothermal systems"""
from idfhub.hvac import EPValues, EPApi

from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import (
    SiteGroundtemperatureBuildingsurface,
    SiteGroundtemperatureUndisturbedKusudaachenbach,
    HeatpumpWatertowaterEquationfitHeating,
    GroundheatexchangerVerticalProperties,
    GroundheatexchangerVerticalArray,
    GroundheatexchangerSystem,
    CurveBiquadratic,
    CurveQuadratic,
    CurveQuadlinear,
    HeatpumpPlantloopEirHeating,
    OutdoorairNode,
)

from idfhub.idf_autocomplete.v24_1_0.idf_types_short import (
    SiteGroundtemperatureBuildingsurfaceType,
    SiteGroundtemperatureUndisturbedKusudaachenbachType,
    HeatpumpWatertowaterEquationfitHeatingType,
    GroundheatexchangerVerticalPropertiesType,
    GroundheatexchangerVerticalArrayType,
    GroundheatexchangerSystemType,
    CurveBiquadraticType,
    CurveQuadraticType,
    CurveQuadlinearType,
    HeatpumpPlantloopEirHeatingType,
    OutdoorairNodeType,
)

from idfhub.common import idf, CONF


def ground_temperature():
    """create a basic ground temperature for the building"""
    SiteGroundtemperatureBuildingsurface(
        idf,
        **SiteGroundtemperatureBuildingSurfaceType(
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
    soil = SiteGroundtemperatureUndisturbedKusudaachenbach(
        idf,
        **SiteGroundtemperatureUndisturbedKusudaachenbachType(
            Name="Sol_KA",
            Soil_Thermal_Conductivity=2.5,  # W/(m K)
            Soil_Density=2000,  # kg/m3
            Soil_Specific_Heat=900,  # J/(kg K)
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
            Borehole_Length=100,
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
            Number_of_Boreholes_in_XDirection=CONF[name].get(
                "Number_of_Boreholes_in_XDirection", 5),
            Number_of_Boreholes_in_YDirection=CONF[name].get(
                "Number_of_Boreholes_in_YDirection", 2),
            Borehole_Spacing=6
        )
    )

    # 0.0033*3600 m3/h soit 11,88 m3/h pour 10 forages, soit 1.2 m3/h par forage
    return GroundheatexchangerSystem(
        idf,
        **GroundheatexchangerSystemType(
            Name=f"{name} vertical geoexchanger",
            Inlet_Node_Name=f"{name}_vertical_geoexchanger_inlet_node",
            Outlet_Node_Name=f"{name}_vertical_geoexchanger_outlet_node",
            Design_Flow_Rate=0.006,  # m3/s before 0.0033
            Undisturbed_Ground_Temperature_Model_Name=soil.Name,
            Undisturbed_Ground_Temperature_Model_Type=soil.key,
            Ground_Thermal_Conductivity=2.5,  # W / (m K) - 0.69 serait une valeur médiocre
            Ground_Thermal_Heat_Capacity=1.8e6,  # Pa/K = J / (m3 K)
            GHEVerticalArray_Object_Name=boreholes.Name
        )
    )


def create_quadlincurve(name, coeff1, coeff2, coeff3, coeff4):
    """create a curve for heatpump configuration"""
    return CurveQuadlinearType(
        Name=name,
        Coefficient1_Constant=coeff1,
        Coefficient2_w=coeff2,
        Coefficient3_x=coeff3,
        Coefficient4_y=coeff4,
        Coefficient5_z=0,
        Minimum_Value_of_w=-5.0,
        Maximum_Value_of_w=20.0,
        Minimum_Value_of_x=30.0,
        Maximum_Value_of_x=55.0,
        Minimum_Value_of_y=-5.0,
        Maximum_Value_of_y=20.0,
        Minimum_Value_of_z=0.0,
        Maximum_Value_of_z=1.0,
        Minimum_Curve_Output=0.1,
        Maximum_Curve_Output=1,
        Input_Unit_Type_for_w=EPValues.TEMPERATURE,
        Input_Unit_Type_for_x=EPValues.TEMPERATURE,
        Input_Unit_Type_for_y=EPValues.TEMPERATURE,
        Input_Unit_Type_for_z=EPValues.DIMENSIONLESS
    )


def water_to_water_heatpump(name):
    """add a water to water heatpump"""
    capacity_curve = CurveQuadlinear(
        idf,
        **create_quadlincurve(
            f"{name} Heating capacity curve",
            0.8, 0.002, 0.002, 0
        )
    )

    power_curve = CurveQuadlinear(
        idf,
        **create_quadlincurve(
            f"{name} Heating power curve",
            0.4, 0.002, 0.002, 0
        )
    )

    return HeatpumpWatertowaterEquationfitHeating(
        idf,
        **HeatpumpWatertowaterEquationfitHeatingType(
            Name=name,
            Source_Side_Inlet_Node_Name=f"{name}_source_side_inlet_node",
            Source_Side_Outlet_Node_Name=f"{name}_source_side_outlet_node",
            Load_Side_Inlet_Node_Name=f"{name}_load_side_inlet_node",
            Load_Side_Outlet_Node_Name=f"{name}_load_side_outlet_node",
            Reference_Load_Side_Flow_Rate=EPValues.AUTOSIZE,
            Reference_Source_Side_Flow_Rate=EPValues.AUTOSIZE,
            Reference_Heating_Capacity=CONF[name].get(
                "Reference_Heating_Capacity", EPValues.AUTOSIZE),
            Reference_Heating_Power_Consumption=EPValues.AUTOSIZE,
            Reference_Coefficient_of_Performance=CONF[name].get(
                "Reference_Coefficient_of_Performance", 2.5),
            Sizing_Factor=1,
            Heating_Capacity_Curve_Name=capacity_curve.Name,
            Heating_Compressor_Power_Curve_Name=power_curve.Name
        )
    )


def air_to_water_heatpump_eir(name):
    """simulate an EIR air to water heatpump"""
    # set de courbes théoriques issues des courbes quadratiques trane
    # x=load side outlet temperature (water)
    # y=source inlet temperature (air)
    conf = CONF[name]
    capacity_curve_f_temp = CurveBiquadratic(
        idf,
        **CurveBiquadraticType(
            Name=f"{name}_HeatingCapFTemp",
            Coefficient1_Constant=conf.get("capacity_c", 0.794900878202383),
            Coefficient2_x=conf.get("capacity_x", 0.00388524034840032),
            Coefficient3_x2=conf.get("capacity_x2", -0.0000575169230965453),
            Coefficient4_y=conf.get("capacity_y", 0.0278109488428528),
            Coefficient5_y2=conf.get("capacity_y2", 0.000318168),
            Coefficient6_xy=conf.get("capacity_xy", -0.000130572089253355),
            Minimum_Value_of_x=15,
            Maximum_Value_of_x=70,
            Minimum_Value_of_y=-17,
            Maximum_Value_of_y=37,
            Maximum_Curve_Output=1.55,
            Input_Unit_Type_for_X=EPValues.TEMPERATURE,
            Input_Unit_Type_for_Y=EPValues.TEMPERATURE,
            Output_Unit_Type=EPValues.DIMENSIONLESS
        )
    )
    eir_curve_f_temp = CurveBiquadratic(
        idf,
        **CurveBiquadraticType(
            Name=f"{name}_HeatEIRCurveFTemp",
            Coefficient1_Constant=conf.get("eir_c", 0.530730392560108),
            Coefficient2_x=conf.get("eir_x", 0.00655164780603528),
            Coefficient3_x2=conf.get("eir_x2", 0.000263599226028026),
            Coefficient4_y=conf.get("eir_y", -0.03620668194737),
            Coefficient5_y2=conf.get("eir_y2", 0.00126617163409192),
            Coefficient6_xy=conf.get("eir_xy", -0.000791224057761721),
            Minimum_Value_of_x=15,
            Maximum_Value_of_x=70,
            Minimum_Value_of_y=-17,
            Maximum_Value_of_y=32,
            Minimum_Curve_Output=0.4,
            Maximum_Curve_Output=1.48,
            Input_Unit_Type_for_X=EPValues.TEMPERATURE,
            Input_Unit_Type_for_Y=EPValues.TEMPERATURE,
            Output_Unit_Type=EPValues.DIMENSIONLESS
        )
    )
    # lois d'eau internes
    min_waterlaw = CurveQuadratic(
        idf,
        **CurveBiquadraticType(
            Name=f"{name}_MinSWTvsOAT",
            Coefficient1_Constant=0.0,
            Coefficient2_x=1.0,
            Coefficient3_x2=0.0,
            Minimum_Value_of_x=-17.77778,  # 0 Fahrenheit
            Maximum_Value_of_x=35.0,  # 95 Fahrenheit
            Minimum_Curve_Output=20.0,
            Maximum_Curve_Output=35.0,
            Input_Unit_Type_for_X=EPValues.TEMPERATURE,
            Output_Unit_Type=EPValues.TEMPERATURE
        )
    )
    max_waterlaw = CurveQuadratic(
        idf,
        **CurveQuadraticType(
            Name=f"{name}_MaxSWTvsOAT",
            Coefficient1_Constant=53.1666666666667,
            Coefficient2_x=0.85,
            Coefficient3_x2=0.0,
            Minimum_Value_of_x=-17.777778,
            Maximum_Value_of_x=35.0,
            Minimum_Curve_Output=20.0,
            Maximum_Curve_Output=60.0,
            Input_Unit_Type_for_X=EPValues.TEMPERATURE,
            Output_Unit_Type=EPValues.TEMPERATURE
        )
    )
    eir_f_plr = CurveQuadratic(
        idf,
        **CurveQuadraticType(
            Name=f"{name}_EIRCurveFPLR",
            Coefficient1_Constant=1.0,
            Coefficient2_x=0.0,
            Coefficient3_x2=0.0,
            Minimum_Value_of_x=0.0,
            Maximum_Value_of_x=1.0
        ))
    time_defrost_nrj = CurveQuadratic(
        idf,
        **CurveQuadraticType(
            Name=f"{name}_TimedDefrostHeatEnergy",
            Coefficient1_Constant=0.03423,
            Coefficient2_x=-0.00072,
            Coefficient3_x2=0.0,
            Minimum_Value_of_x=-30.0,
            Maximum_Value_of_x=10.60675883
        )
    )
    time_defrost_frq = CurveQuadratic(
        idf,
        **CurveQuadraticType(
            Name=f"{name}_TimedDefrostFrequency",
            Coefficient1_Constant=0.71582,
            Coefficient2_x=-0.024822,
            Coefficient3_x2=0.0,
            Minimum_Value_of_x=-30.0,
            Maximum_Value_of_x=10.60675883
        )
    )
    time_defrost_heatload = CurveQuadratic(
        idf,
        **CurveQuadraticType(
            Name=f"{name}_TimedDefrostHeatLoad",
            Coefficient1_Constant=0.08286,
            Coefficient2_x=-0.007812,
            Coefficient3_x2=0.0,
            Minimum_Value_of_x=-30.0,
            Maximum_Value_of_x=10.60675883
        )
    )
    dry_coil_correc = CurveQuadratic(
        idf,
        **CurveQuadraticType(
            Name=f"{name}_HeatDryCoilFOAT",
            Coefficient1_Constant=0.9574744,
            Coefficient2_x=-0.00299322,
            Coefficient3_x2=0.000055728,
            Minimum_Value_of_x=-11.675,
            Maximum_Value_of_x=26.6666667
        )
    )
    air_node_name = f"{name}_source_inlet_outdoor_air_node"
    input_air_node = OutdoorairNode(
        idf,
        **OutdoorairNodeType(
            Name=air_node_name,
            Height_Above_Ground=10
        )
    )
    hpatw = HeatpumpPlantloopEirHeating(
        idf,
        **HeatpumpPlantloopEirHeatingType(
            Name=f"{name}_EIR_heatpump_air2water",
            Load_Side_Inlet_Node_Name=f"{name}_load_inlet_node",
            Load_Side_Outlet_Node_Name=f"{name}_load_outlet_node",
            Condenser_Type="AirSource",
            Source_Side_Inlet_Node_Name=input_air_node.Name,
            Source_Side_Outlet_Node_Name=f"{name}_source_outlet_outdoor_air_node",
            Reference_Coefficient_of_Performance=conf.get(
                "Reference_Coefficient_Of_Performance", 3.2),
            Reference_Capacity=conf.get("Reference_Capacity", EPValues.AUTOSIZE),
            Sizing_Factor=1,
            Capacity_Modifier_Function_of_Temperature_Curve_Name=
                capacity_curve_f_temp.Name,
            Electric_Input_to_Output_Ratio_Modifier_Function_of_Temperature_Curve_Name=
                eir_curve_f_temp.Name,
            Electric_Input_to_Output_Ratio_Modifier_Function_of_Part_Load_Ratio_Curve_Name=
                eir_f_plr.Name,
            Heat_Pump_Sizing_Method="GreaterOfHeatingOrCooling",
            Control_Type=conf.get("Control_Type", "Setpoint"),
            Flow_Mode="VariableSpeedPumping",
            Minimum_Part_Load_Ratio=0.2,
            Minimum_Source_Inlet_Temperature=-25.0,
            Maximum_Source_Inlet_Temperature=35.0,
            Minimum_Supply_Water_Temperature_Curve_Name=
                min_waterlaw.Name,
            Maximum_Supply_Water_Temperature_Curve_Name=
                max_waterlaw.Name,
            Dry_Outdoor_Correction_Factor_Curve_Name=
                dry_coil_correc.Name,
            Maximum_Outdoor_Dry_Bulb_Temperature_For_Defrost_Operation=10.60675883,
            Heat_Pump_Defrost_Control="TimedEmpirical",
            Heat_Pump_Defrost_Time_Period_Fraction=0.1166667,
            Timed_Empirical_Defrost_Frequency_Curve_Name=
                time_defrost_frq.Name,
            Timed_Empirical_Defrost_Heat_Load_Penalty_Curve_Name=
                time_defrost_heatload.Name,
            Timed_Empirical_Defrost_Heat_Input_Energy_Fraction_Curve_Name=
                time_defrost_nrj.Name
        )
    )
    return hpatw
