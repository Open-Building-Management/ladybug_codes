"""coils"""
from eppy.bunch_subclass import EpBunch

from idfhub.common import idf, CONF
from idfhub.hvac import EPValues, EPApi
from idfhub.hvac24_1_0 import resolve_side
from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import (
    CoilCoolingDxSinglespeed, CoilsystemCoolingDx,
    CurveBiquadratic, CurveQuadratic
)
from idfhub.idf_autocomplete.v24_1_0.idf_types_short import (
    CoilCoolingDxSinglespeedType, CoilsystemCoolingDxType,
    CurveBiquadraticType, CurveQuadraticType
)


def coil_system_cooling_dx(name) -> list[EpBunch]|None:
    """coil cooling system direct expansion"""
    conf = CONF.get(name, {})
    coil_name = conf.get("coil")
    if not coil_name:
        return None
    side = resolve_side(coil_name)
    if not side:
         return None
    coil = None
    if "cooling_dx_single_speed" in coil_name:
            coil = coil_cooling_dx_single_speed(coil_name)
    if not coil:
        return None
    inlet = f"{side}_{EPApi.INLET.node_name()}"
    outlet = f"{side}_{EPApi.OUTLET.node_name()}"
    system = CoilsystemCoolingDx(
        idf,
        **CoilsystemCoolingDxType(
            Name=name,
            DX_Cooling_Coil_System_Inlet_Node_Name=coil[inlet],
            DX_Cooling_Coil_System_Outlet_Node_Name=coil[outlet],
            DX_Cooling_Coil_System_Sensor_Node_Name=coil[outlet],
            Cooling_Coil_Object_Type=coil.key,
            Cooling_Coil_Name=coil.Name
        )
    )
    return [coil, system]

def coil_cooling_dx_single_speed(name: str) -> EpBunch:
    """coil cooling direct expansion"""
    conf = CONF.get(name, {})
    # the default values come from the energy plus examples,
    # they are caracterisation values for a window air conditionner 
    # x = inside air temperature, which enters the evaporator
    # y = outside air temperature, which enters the condenser
    # nota : there is a DXcoolingcoil.idf file in the datasets folder of the energyplus installation 
    capacity_f_iat_oat = CurveBiquadratic(
        idf,
        **CurveBiquadraticType(
            Name=f"{name}_Capacity_f_iat_oat",
            Coefficient1_Constant=0.942587793,
            Coefficient2_x=0.009543347,
            Coefficient3_x2=0.00068377,
            Coefficient4_y=-0.011042676,
            Coefficient5_y2=5.249e-06,
            Coefficient6_xy=-9.72e-06,
            Minimum_Value_of_x=17,
            Maximum_Value_of_x=26,
            Minimum_Value_of_y=13,
            Maximum_Value_of_y=46
        )
    )
    capacity_f_flowfrac = CurveQuadratic(
        idf,
        **CurveQuadraticType(
            Name=f"{name}_Capacity_f_flowfrac",
            Coefficient1_Constant=0.8,
            Coefficient2_x=0.2,
            Coefficient3_x2=0,
            Minimum_Value_of_x=0.5,
            Maximum_Value_of_x=1.5
        )
    )
    eir_f_iat_oat = CurveBiquadratic(
        idf,
        **CurveBiquadraticType(
            Name=f"{name}_EIR_f_iat_oat",
            Coefficient1_Constant=0.342414409,
            Coefficient2_x=0.034885008,
            Coefficient3_x2=-0.0006237,
            Coefficient4_y=0.004977216,
            Coefficient5_y2=0.000437951,
            Coefficient6_xy=-0.000728028,
            Minimum_Value_of_x=17,
            Maximum_Value_of_x=26,
            Minimum_Value_of_y=13,
            Maximum_Value_of_y=46
        )
    )
    eir_f_flowfrac = CurveQuadratic(
        idf,
        **CurveQuadraticType(
            Name=f"{name}_EIR_f_flowfrac",
            Coefficient1_Constant=1.1552,
            Coefficient2_x=-0.1808,
            Coefficient3_x2=0.0256,
            Minimum_Value_of_x=0.5,
            Maximum_Value_of_x=1.5
        )
    )
    plf = CurveQuadratic(
        idf,
        **CurveQuadraticType(
            Name=f"{name}_PLF",
            Coefficient1_Constant=0.85,
            Coefficient2_x=0.15,
            Coefficient3_x2=0.0,
            Minimum_Value_of_x=0.0,
            Maximum_Value_of_x=1.0
        )
    )
    coil = CoilCoolingDxSinglespeed(
        idf,
        **CoilCoolingDxSinglespeedType(
            Name=name,
            Gross_Rated_Total_Cooling_Capacity=EPValues.AUTOSIZE,
            Gross_Rated_Sensible_Heat_Ratio=EPValues.AUTOSIZE,
            Gross_Rated_Cooling_COP=conf.get("cop", 3),
            Rated_Air_Flow_Rate=EPValues.AUTOSIZE,
            Air_Inlet_Node_Name=f"{name}_air_inlet_node",
            Air_Outlet_Node_Name=f"{name}_air_outlet_node",
            Total_Cooling_Capacity_Function_of_Temperature_Curve_Name=capacity_f_iat_oat.Name,
            Total_Cooling_Capacity_Function_of_Flow_Fraction_Curve_Name=capacity_f_flowfrac.Name,
            Energy_Input_Ratio_Function_of_Temperature_Curve_Name=eir_f_iat_oat.Name,
            Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name=eir_f_flowfrac.Name,
            Part_Load_Fraction_Correlation_Curve_Name=plf.Name
        )
    )
    return coil
