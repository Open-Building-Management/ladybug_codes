"""Manage hvac equipments"""
import sys
from typing import Any
from eppy.bunch_subclass import BadEPFieldError, EpBunch

from idfhub.hvac import (
    PLANT, SUPPLY, DEMAND, RETURN, INLET, OUTLET, ALWAYS_ON,
    EPApi, EPValues,
    create_branch,
    LoopNodes, Branches,
    set_nodes, node_name, plantloop_split_mix,
    branchlist_update,
    split_mix, pipe_splitter, pipe_mixer,
    get_branch_inlet_outlet_nodes
)

from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import (
    Scheduletypelimits,ScheduletypelimitsMeta,ScheduleConstant,ScheduleConstantMeta,
    SiteGroundtemperatureBuildingsurface,
    SiteGroundtemperatureUndisturbedKusudaachenbach,
    HeatpumpWatertowaterEquationfitHeating, HeatpumpPlantloopEirHeating,
    GroundheatexchangerVerticalProperties,
    GroundheatexchangerVerticalArray,
    GroundheatexchangerSystem,
    SetpointmanagerOutdoorairreset, SetpointmanagerScheduled,
    PumpConstantspeed, PumpVariablespeed,
    ScheduleCompact,
    Plantequipmentlist, Plantequipmentoperationschemes,
    PlantequipmentoperationHeatingload, PlantequipmentoperationCoolingload,
    OutdoorairNode,
    CurveBiquadratic, CurveQuadratic, CurveQuadlinear,
    BoilerHotwater,
    PlantequipmentoperationOutdoordrybulb,
    OutputVariable,
)

from idfhub.idf_autocomplete.v24_1_0.idf_types_short import (
    ScheduletypelimitsType,ScheduleConstantType,
    SiteGroundtemperatureBuildingsurfaceType,
    SiteGroundtemperatureUndisturbedKusudaachenbachType,
    HeatpumpWatertowaterEquationfitHeatingType, HeatpumpPlantloopEirHeatingType,
    GroundheatexchangerVerticalPropertiesType,
    GroundheatexchangerVerticalArrayType,
    GroundheatexchangerSystemType,
    SetpointmanagerOutdoorairresetType, SetpointmanagerScheduledType,
    PumpConstantspeedType, PumpVariablespeedType,
    ScheduleCompactType,
    PlantequipmentlistType, PlantequipmentoperationschemesType,
    PlantequipmentoperationHeatingloadType, PlantequipmentoperationCoolingloadType,
    OutdoorairNodeType,
    CurveBiquadraticType, CurveQuadraticType,CurveQuadlinearType,
    BoilerHotwaterType,
    PlantequipmentoperationOutdoordrybulbType,
    OutputVariableType,
)

from idfhub.common import get_logger, idf, CONF

LOGGER = get_logger()
BYPASS = "bypass"
loops: dict = {}
equipments: dict[str, Any] = {}

if not idf:
    LOGGER.error("no idf > generate_geometry")
    sys.exit()


temperature_typelimits = idf.getobject(
        ScheduletypelimitsMeta.idf_name,
        "temperature"
    )
if not temperature_typelimits:
    temperature_typelimits = Scheduletypelimits(
        idf,
        **ScheduletypelimitsType(
            Name="temperature",
            Numeric_Type=EPValues.CONTINUOUS,
            Unit_Type=EPValues.TEMPERATURE
        )
    )

# on utilise un schedule compact
# Mots-clés utiles dans For:
# Weekdays
# Weekends
# AllDays
# Monday
# Tuesday
# ...
# Holidays
# SummerDesignDay
# WinterDesignDay
# CustomDay1/2
def basic_compact_schedule(
    value: float,
    *,
    schedule_name: str,
    typelimits: EpBunch = temperature_typelimits
):
    """create a compact schedule"""
    return ScheduleCompact(
        idf,
        **ScheduleCompactType(
            Name=schedule_name,
            Schedule_Type_Limits_Name=typelimits.Name,
            Field_1=f"{EPValues.THROUGH}: 12/31",
            Field_2=f"{EPValues.FOR}: {EPValues.WEEKDAYS}",
            Field_3=f"{EPValues.UNTIL}: 07:00",
            Field_4=0,
            Field_5=f"{EPValues.UNTIL}: 17:00",
            Field_6=value,
            Field_7=f"{EPValues.UNTIL}: 24:00",
            Field_8=0,
            Field_9=f"{EPValues.FOR}: {EPValues.WEEKENDS}",
            Field_10=f"{EPValues.UNTIL}: 24:00",
            Field_11=0,
            Field_12=f"{EPValues.FOR}:{EPValues.WINTER_DESIGN_DAY}",
            Field_13=f"{EPValues.UNTIL}: 07:00",
            Field_14=0,
            Field_15=f"{EPValues.UNTIL}: 17:00",
            Field_16=value,
            Field_17=f"{EPValues.UNTIL}: 24:00",
            Field_18=0,
            Field_19=f"{EPValues.FOR}:{EPValues.SUMMER_DESIGN_DAY}",
            Field_20=f"{EPValues.UNTIL}: 07:00",
            Field_21=0,
            Field_22=f"{EPValues.UNTIL}: 17:00",
            Field_23=value,
            Field_24=f"{EPValues.UNTIL}: 24:00",
            Field_25=0,
        )
    )

def constant_schedule(
    value: int,
    *,
    name: str|None = None,
    typelimits:EpBunch = temperature_typelimits
):
    """create a constant schedule type"""
    if name is None:
        name = f"const_temp_sched_{value}deg"
    return ScheduleConstant(
        idf,
        **ScheduleConstantType(
            Name=name,
            Schedule_Type_Limits_Name=typelimits.Name,
            Hourly_Value=value
        )
    )

#------------------------------------------------------------------------------
# SETPOINTS
#------------------------------------------------------------------------------
def water_law(loop_name: str, setup: str):
    """add a waterlaw setpoint on a loop plant outlet"""
    loop_nodes = LoopNodes(loop_name)
    message = f"waterlaw @ {loop_nodes.plant_outlet} with {CONF[setup]}"
    LOGGER.debug(message)
    SetpointmanagerOutdoorairreset(
        idf,
        **SetpointmanagerOutdoorairresetType(
            Name=f"{setup} {loop_name}",
            Control_Variable=EPValues.TEMPERATURE,
            Setpoint_at_Outdoor_Low_Temperature=CONF[setup].get(
                "Setpoint_at_Outdoor_Low_Temperature", 70),
            Outdoor_Low_Temperature=CONF[setup].get(
                "Outdoor_Low_Temperature", -5),
            Setpoint_at_Outdoor_High_Temperature=CONF[setup].get(
                "Setpoint_at_Outdoor_High_Temperature", 40),
            Outdoor_High_Temperature=CONF[setup].get(
                "Outdoor_High_Temperature", 15),
            Setpoint_Node_or_NodeList_Name=loop_nodes.plant_outlet
        )
    )
    OutputVariable(
        idf,
        **OutputVariableType(
            Key_Value=loop_nodes.plant_outlet,
            Variable_Name="System Node Setpoint Temperature",
            Reporting_Frequency="Timestep"
        )
    )

def constant_set_point(loop_name: str, setup: str):
    """add a constant setpoint on a loop plant outlet"""
    loop_nodes = LoopNodes(loop_name)
    message = f"constant setpoint @ {loop_nodes.plant_outlet} with {CONF[setup]}"
    LOGGER.debug(message)
    temp = CONF[setup].get("temp", 12)
    name = f"const_temp_sched_{temp}deg"
    consigne = idf.getobject(
        ScheduleConstantMeta.idf_name,
        name
    )
    if consigne is None:
        consigne = constant_schedule(temp, name=name)
    SetpointmanagerScheduled(
        idf,
        **SetpointmanagerScheduledType(
            Name=f"{setup} {loop_name}",
            Control_Variable=EPValues.TEMPERATURE,
            Schedule_Name=consigne.Name,
            Setpoint_Node_or_NodeList_Name=loop_nodes.plant_outlet,
        )
    )

#------------------------------------------------------------------------------
# SOIL, BOREHOLE, PRODUCTION SYSTEMS
#------------------------------------------------------------------------------
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
    soil = SiteGroundtemperatureUndisturbedKusudaachenbach(
        idf,
        **SiteGroundtemperatureUndisturbedKusudaachenbachType(
            Name="Sol_KA",
            Soil_Thermal_Conductivity=2.5, # W/(m K)
            Soil_Density=2000, # kg/m3
            Soil_Specific_Heat=900, # J/(kg K)
            Average_Soil_Surface_Temperature=11,
            Average_Amplitude_of_Surface_Temperature=10,
            Phase_Shift_of_Minimum_Surface_Temperature=45 #days
        )
    )
    hole = GroundheatexchangerVerticalProperties(
        idf,
        **GroundheatexchangerVerticalPropertiesType(
            Name=f"single vertical hole for {name}",
            Depth_of_Top_of_Borehole=0,
            Borehole_Length=100,
            Borehole_Diameter=0.15,
            Grout_Thermal_Conductivity=1.2, # W / (m K)
            Grout_Thermal_Heat_Capacity=3.0e6, # J / (m3 K)
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
            Design_Flow_Rate=0.006, # m3/s before 0.0033
            Undisturbed_Ground_Temperature_Model_Name=soil.Name,
            Undisturbed_Ground_Temperature_Model_Type=soil.key,
            Ground_Thermal_Conductivity=2.5, #W / (m K) - 0.69 serait une valeur médiocre
            Ground_Thermal_Heat_Capacity=1.8e6, #Pa/K = J / (m3 K)
            GHEVerticalArray_Object_Name=boreholes.Name
        )
    )

def pump(name, pump_type="constant"):
    """add a pump"""
    conf = CONF.get(name, {})
    if pump_type == "variable":
        return PumpVariablespeed(
            idf,
            **PumpVariablespeedType(
                Name=name,
                Inlet_Node_Name=f"{name}_inlet_node",
                Outlet_Node_Name=f"{name}_outlet_node",
                Design_Maximum_Flow_Rate=conf.get(
                    "Design_Maximum_Flow_Rate", EPValues.AUTOSIZE),
                Design_Power_Consumption=conf.get(
                    "Design_Power_Consumption", EPValues.AUTOSIZE),
                Motor_Efficiency=0.9,
                Design_Minimum_Flow_Rate=conf.get(
                    "Design_Minimum_Flow_Rate", 0),
                Fraction_of_Motor_Inefficiencies_to_Fluid_Stream=0,
                Coefficient_1_of_the_Part_Load_Performance_Curve=0,
                Coefficient_2_of_the_Part_Load_Performance_Curve=1,
                Coefficient_3_of_the_Part_Load_Performance_Curve=0,
                Coefficient_4_of_the_Part_Load_Performance_Curve=0,
                Pump_Control_Type=EPValues.INTERMITTENT,
            )
        )
    return PumpConstantspeed(
        idf,
        **PumpConstantspeedType(
            Name=name,
            Inlet_Node_Name=f"{name}_inlet_node",
            Outlet_Node_Name=f"{name}_outlet_node",
            Design_Flow_Rate=conf.get(
                    "Design_Flow_Rate", EPValues.AUTOSIZE),
            Design_Power_Consumption=conf.get(
                    "Design_Power_Consumption", EPValues.AUTOSIZE),
            Motor_Efficiency=0.9,
            Pump_Control_Type=EPValues.INTERMITTENT,
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


def gas_boiler(name):
    """Add a classic gaz boiler"""
    suffix = "efficiency"
    conf = CONF[name]
    boiler_efficiency = CurveBiquadratic(
        idf,
        **CurveBiquadraticType(
            Name=f"{name}_efficiency_curve",
            Coefficient1_Constant=conf.get(f"{suffix}_c", 1.02),
            Coefficient2_x=conf.get(f"{suffix}_x", -0.02), # x=PLR
            Coefficient3_x2=conf.get(f"{suffix}_x2", -0.05),
            Coefficient4_y=conf.get(f"{suffix}_y", -0.002), # y=Twater
            Coefficient5_y2=conf.get(f"{suffix}_y2", 0),
            Coefficient6_xy=conf.get(f"{suffix}_xy", 0),
            Minimum_Value_of_x=0.1,
            Maximum_Value_of_x=1,
            Minimum_Value_of_y=25,
            Maximum_Value_of_y=80,
            Input_Unit_Type_for_X=EPValues.TEMPERATURE,
            Input_Unit_Type_for_Y=EPValues.TEMPERATURE,
            Output_Unit_Type=EPValues.DIMENSIONLESS
        )
    )
    return BoilerHotwater(
        idf,
        **BoilerHotwaterType(
            Name=name,
            Fuel_Type="NaturalGas",
            Efficiency_Curve_Temperature_Evaluation_Variable="LeavingBoiler",
            Normalized_Boiler_Efficiency_Curve_Name=boiler_efficiency.Name,
            Nominal_Capacity=EPValues.AUTOSIZE,
            Nominal_Thermal_Efficiency=0.8,
            Boiler_Water_Inlet_Node_Name=f"{name}_inlet_node",
            Boiler_Water_Outlet_Node_Name=f"{name}_outlet_node",
            Boiler_Flow_Mode="LeavingSetpointModulated"
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
            Minimum_Value_of_x=-17.77778, # 0 Fahrenheit
            Maximum_Value_of_x=35.0, # 95 Fahrenheit
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


def resolve_side(name, branch_type):
    """resolve equipment side
    for two sided equipments like heat pumps"""
    if name not in CONF:
        return None
    equipment_type = CONF[name].get("type")
    if equipment_type == "heatpump":
        return {
            SUPPLY: EPApi.LOAD_SIDE,
            PLANT: EPApi.LOAD_SIDE,
            DEMAND: EPApi.SOURCE_SIDE,
            RETURN: EPApi.SOURCE_SIDE
        }[branch_type]
    if equipment_type == "exchanger":
        return {
            SUPPLY: EPApi.LOOP_SUPPLY_SIDE,
            PLANT: EPApi.LOOP_SUPPLY_SIDE,
            DEMAND: EPApi.LOOP_DEMAND_SIDE,
            RETURN: EPApi.LOOP_DEMAND_SIDE
        }[branch_type]
    force_side = CONF[name].get("force_side")
    if force_side:
        return force_side
    return None


def process_serie(
    branch_name: str,
    loop_side: str,
    *,
    structure_serie: list[str],
    inlet_node: str|None = None,
    outlet_node: str|None = None
):
    """process a serie and return a branch"""
    if inlet_node is None:
        inlet_node = node_name(branch_name, INLET)
    if outlet_node is None:
        outlet_node = node_name(branch_name, OUTLET)
    current_inlet = inlet_node
    _objects = []
    _sides = []
    for i, obj_name in enumerate(structure_serie):
        is_last = i == len(structure_serie) - 1
        next_outlet = outlet_node if is_last else None

        obj = equipments[obj_name]
        side = resolve_side(obj_name, loop_side)
        set_nodes(
            obj,
            inlet=current_inlet,
            outlet=next_outlet,
            side=side
        )
        _objects.append(obj)
        _sides.append(side)
        try:
            current_inlet = obj[EPApi.OUTLET_NODE_NAME]
        except BadEPFieldError:
            current_inlet = obj[f"{side}_{EPApi.OUTLET_NODE_NAME}"]
    branch = create_branch(
        idf,
        name=branch_name,
        objects=_objects,
        sides=_sides
    )
    return branch


def process_series(
    loop_name,
    loop_side,
    *,
    structure,
    inlet_node=None,
    outlet_node=None,
    branch_name=None,
    from_parallel=False
):
    """process a complex structure"""
    if not branch_name:
        branch_name = f"{loop_name}_{loop_side}_branch"
    if not inlet_node:
        inlet_node = node_name(branch_name, INLET)
    if not outlet_node:
        outlet_node = node_name(branch_name, OUTLET)
    _parallel = False
    for elem in structure:
        if isinstance(elem, dict) and "parallel" in elem:
            _parallel = True
    if not _parallel:
        if from_parallel:
            inlet_node = node_name(branch_name, INLET)
            outlet_node = node_name(branch_name, OUTLET)
        branch = process_serie(
            branch_name,
            loop_side,
            structure_serie=structure,
            inlet_node=inlet_node,
            outlet_node=outlet_node
        )
        branchlist_update(
            idf,
            loop_name=loop_name,
            loop_side=loop_side,
            branches=branch
        )
        return branch
    # on a des structures parallèles
    # on traite d'abord les structures de type liste
    split_branch = None
    mix_branch = None
    for i, elem in enumerate(structure):
        if isinstance(elem, list):
            if not split_branch:
                split_branch = process_serie(
                    f"{branch_name}_{i}_splitter",
                    loop_side,
                    structure_serie=elem,
                    inlet_node=inlet_node
                )
            else:
                mix_branch = process_serie(
                    f"{branch_name}_{i}_mixer",
                    loop_side,
                    structure_serie=elem,
                    outlet_node=outlet_node
                )
    if not split_branch:
        split_branch = pipe_splitter(
            idf,
            inlet_node=inlet_node,
            branch_name=f"{branch_name}_splitter"
        )
    if not mix_branch:
        mix_branch = pipe_mixer(
            idf,
            outlet_node=outlet_node,
            branch_name=f"{branch_name}_mixer"
        )
    for i, elem in enumerate(structure):
        if isinstance(elem, dict) and "parallel" in elem:
            process_parallel(
                loop_name,
                loop_side,
                structure_parallele=elem["parallel"],
                split_branch=split_branch,
                mix_branch=mix_branch,
                branch_name=f"{branch_name}_{i}",
            )
    return [split_branch, mix_branch]


def process_parallel(
    loop_name: str,
    loop_side: str,
    *,
    structure_parallele: list,
    split_branch: EpBunch,
    mix_branch: EpBunch,
    branch_name: str
):
    """organise parallel branches
    given a structure read from the yaml"""
    branchlist_update(
        idf,
        loop_name=loop_name,
        loop_side=loop_side,
        branches=split_branch
    )
    branch_list = []
    # on récupère inlet et outlet depuis les split et mix branch
    _, inlet_node = get_branch_inlet_outlet_nodes(split_branch)
    outlet_node, _ = get_branch_inlet_outlet_nodes(mix_branch)
    for i, struct in enumerate(structure_parallele):
        branch = process_series(
            loop_name,
            loop_side,
            structure=struct,
            inlet_node=inlet_node,
            outlet_node=outlet_node,
            branch_name=f"{branch_name}_{i}",
            from_parallel = True
        )
        if branch:
            branch_list.append(branch)
    side = EPApi.DEMAND_SIDE if loop_side == DEMAND else EPApi.PLANT_SIDE
    split_mix(
        idf=idf,
        plantloop=loops[loop_name],
        side=side,
        inlet_branch=split_branch,
        branches=branch_list,
        outlet_branch=mix_branch
    )
    branchlist_update(
        idf,
        loop_name=loop_name,
        loop_side=loop_side,
        branches=mix_branch
    )


def adjust_nodes_branch(loop_name: str, *, loop_side: str, branches_descr: dict[str, list[str]]):
    """use yaml declaration to organise a branch and relevant nodes on a side loop"""
    object_names = branches_descr[loop_side]
    inlet_node = LoopNodes(loop_name).get(side=loop_side, port=INLET)
    outlet_node = LoopNodes(loop_name).get(side=loop_side, port=OUTLET)
    process_series(
        loop_name,
        loop_side,
        structure=object_names,
        inlet_node=inlet_node,
        outlet_node=outlet_node
    )


def adjust_nodes_branch_old(
    loop_name: str,
    *,
    loop_side: str,
    branches_descr: dict[str, list[str]]
):
    """first attempt"""
    object_names = branches_descr[loop_side]
    bypass = False
    inlet_node = LoopNodes(loop_name).get(side=loop_side, port=INLET)
    outlet_node = LoopNodes(loop_name).get(side=loop_side, port=OUTLET)
    branch_name = Branches(loop_name).get(side=loop_side)
    if BYPASS in branches_descr:
        if loop_side in branches_descr[BYPASS]:
            bypass = True
            inlet_node = None
            outlet_node = None
    branch = process_serie(
        branch_name,
        loop_side,
        structure_serie=object_names,
        inlet_node=inlet_node,
        outlet_node=outlet_node
    )
    branchlist_update(
        idf,
        loop_name=loop_name,
        loop_side=loop_side,
        branches=branch
    )
    if bypass:
        side = EPApi.DEMAND_SIDE if loop_side == DEMAND else EPApi.PLANT_SIDE
        plantloop_split_mix(
            idf=idf,
            plantloop=loops[loop_name],
            side=side,
            branches=[branch],
            bypass=True
        )


def generate_operation(
    *,
    operation_name:str, loop_type: str,
    names: list[str],
    ranges: list[list[float]]
):
    """return operation object"""
    if EPValues.LOAD in loop_type:
        if EPValues.HEATING in loop_type:
            operation = PlantequipmentoperationHeatingload(
                idf,
                **PlantequipmentoperationHeatingloadType(
                    Name=operation_name)
            )
        else:
            operation = PlantequipmentoperationCoolingload(
                idf,
                **PlantequipmentoperationCoolingloadType(
                    Name=operation_name)
            )
        for i, limits in enumerate(ranges):
            operation[f"Range_{i+1}_Equipment_List_Name"] = names[i]
            operation[f"Load_Range_{i+1}_Lower_Limit"] = limits[0]
            operation[f"Load_Range_{i+1}_Upper_Limit"] = limits[1]
        return operation
    # temperature control...
    operation = PlantequipmentoperationOutdoordrybulb(
        idf,
        **PlantequipmentoperationOutdoordrybulbType(
            Name=operation_name)
    )
    for i, limits in enumerate(ranges):
        operation[f"Range_{i+1}_Equipment_List_Name"] = names[i]
        operation[f"DryBulb_Temperature_Range_{i+1}_Lower_Limit"] = limits[0]
        operation[f"DryBulb_Temperature_Range_{i+1}_Upper_Limit"] = limits[1]
    return operation


def operation_list_scheme(loop_name:str):
    """GENERATE LIST OF EQUIPMENTS & OPERATION SCHEMES FOR A PLANTLOOP"""
    conf = CONF.get(loop_name, {})
    loop_type = conf.get("Loop_Type", EPValues.HEATING)
    loop_types = [str(el).capitalize() for el in loop_type.split("_")]
    add_load = False
    if len(loop_types) == 1:
        add_load = True
    if len(loop_types) == 2 and loop_types[1] == "Mix":
        add_load = True
    if add_load:
        loop_types.append(EPValues.LOAD)
    loop_type = "_".join(loop_types)
    mix = "Mix" in loop_type
    def_range = [0, 1e9] if EPValues.LOAD in loop_type else [0, 20]
    names = []
    ranges = []
    loop_machines = CONF[loop_name].get("operation", [])
    if mix:
        # a list for each machine referenced in the operation loop
        for i, obj_name in enumerate(loop_machines):
            list_name = f"{obj_name}_Only"
            Plantequipmentlist(
                idf,
                **PlantequipmentlistType(
                    Name=list_name,
                    Equipment_1_Object_Type = equipments[obj_name].key,
                    Equipment_1_Name = equipments[obj_name].Name
                )
            )
            names.append(list_name)
            op_range = CONF[obj_name].get("operation_range", def_range)
            ranges.append(op_range)
    else:
        # a single list with all the machines
        list_name = f"{loop_name} Equipment List"
        loop_equipment_list = Plantequipmentlist(
            idf,
            **PlantequipmentlistType(
                Name=list_name
            )
        )
        for i, obj_name in enumerate(loop_machines):
            loop_equipment_list[f"Equipment_{i+1}_Object_Type"] = equipments[obj_name].key
            loop_equipment_list[f"Equipment_{i+1}_Name"] = equipments[obj_name].Name
        names.append(list_name)
        ranges.append(def_range)
    # a single operation for the loop
    operation = generate_operation(
        operation_name = f"{loop_name} operation",
        loop_type=loop_type,
        names=names,
        ranges=ranges
    )
    # a single scheme for the loop
    Plantequipmentoperationschemes(
        idf,
        **PlantequipmentoperationschemesType(
            Name=loop_name,
            Control_Scheme_1_Object_Type=operation.key,
            Control_Scheme_1_Name=operation.Name,
            Control_Scheme_1_Schedule_Name=ALWAYS_ON
        )
    )
