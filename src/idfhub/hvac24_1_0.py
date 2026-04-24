"""Manage hvac equipments"""
import sys
from typing import Any
from eppy.bunch_subclass import BadEPFieldError, EpBunch

from idfhub.hvac import (
    PLANT, SUPPLY, DEMAND, RETURN, INLET, OUTLET,
    ALWAYS_ON,
    EPApi, EPValues,
    create_branch,
    LoopNodes, Branches,
    set_nodes, plantloop_split_mix
)

from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import (
    Scheduletypelimits,ScheduleConstant,ScheduleConstantMeta,
    SiteGroundtemperatureBuildingsurface,
    SiteGroundtemperatureUndisturbedKusudaachenbach,
    CurveQuadlinear,
    HeatpumpWatertowaterEquationfitHeating,
    GroundheatexchangerVerticalProperties,
    GroundheatexchangerVerticalArray,
    GroundheatexchangerSystem,
    SetpointmanagerOutdoorairreset, SetpointmanagerScheduled,
    PumpConstantspeed, PumpVariablespeed,
    ScheduleCompact,
    Plantequipmentlist, Plantequipmentoperationschemes,
    PlantequipmentoperationHeatingload, PlantequipmentoperationCoolingload,
    EnergymanagementsystemSensor, EnergymanagementsystemSensorMeta, EnergymanagementsystemActuator,
    EnergymanagementsystemProgram, EnergymanagementsystemProgramcallingmanager,
    CurveBiquadratic, CurveQuadratic,
    BoilerHotwater,
)

from idfhub.idf_autocomplete.v24_1_0.idf_types_short import (
    ScheduletypelimitsType,ScheduleConstantType,
    SiteGroundtemperatureBuildingsurfaceType,
    SiteGroundtemperatureUndisturbedKusudaachenbachType,
    CurveQuadlinearType,
    HeatpumpWatertowaterEquationfitHeatingType,
    GroundheatexchangerVerticalPropertiesType,
    GroundheatexchangerVerticalArrayType,
    GroundheatexchangerSystemType,
    SetpointmanagerOutdoorairresetType, SetpointmanagerScheduledType,
    PumpConstantspeedType, PumpVariablespeedType,
    ScheduleCompactType,
    PlantequipmentlistType, PlantequipmentoperationschemesType,
    PlantequipmentoperationHeatingloadType, PlantequipmentoperationCoolingloadType,
    EnergymanagementsystemSensorType, EnergymanagementsystemActuatorType,
    EnergymanagementsystemProgramType, EnergymanagementsystemProgramcallingmanagerType,
    CurveBiquadraticType, CurveQuadraticType,
    BoilerHotwaterType,
)

from idfhub.common import get_logger, idf, CONF

LOGGER = get_logger()
BYPASS = "bypass"
loops: dict = {}
equipments: dict[str, Any] = {}

if not idf:
    LOGGER.error("no idf > generate_geometry")
    sys.exit()


def create_sensor(*, sensor_name, sensor_type, location_name):
    """create a sensor"""
    sensor = idf.getobject(
        EnergymanagementsystemSensorMeta.idf_name,
        sensor_name
    )
    if sensor is None:
        return EnergymanagementsystemSensor(
            idf,
            **EnergymanagementsystemSensorType(
                Name=sensor_name,
                OutputVariable_or_OutputMeter_Index_Key_Name=location_name,
                OutputVariable_or_OutputMeter_Name=sensor_type
            )
        )
    return sensor

    )
        )
        )

def control_manager(sensor_name, conf: dict[str, Any]):
    """manage equipment availability using a sensor"""
    node_name = LoopNodes(conf["loop"]).get(
         side=conf["side"],
         port=conf["port"]
    )
    create_sensor(
        sensor_name = sensor_name,
        sensor_type = conf["type"],
        location_name = node_name,
    )
    for equipment_name in conf.get("controls", []):
        if "pump" not in equipment_name:
            continue
        actuator_name = f"{equipment_name}_availability"
        program_name = f"{equipment_name}_program"
        schedule_name = f"{equipment_name}_availability_schedule"
        schedule = ScheduleCompact(
            idf,
            **ScheduleCompactType(
                Name=schedule_name,
                Schedule_Type_Limits_Name="Fractional",
                Field_1=f"{EPValues.THROUGH}: 12/31",
                Field_2=f"{EPValues.FOR}: {EPValues.ALLDAYS}",
                Field_3=f"{EPValues.UNTIL}: 24:00",
                Field_4=1
            )
        )
        EnergymanagementsystemActuator(
            idf,
            **EnergymanagementsystemActuatorType(
                Name=actuator_name,
                Actuated_Component_Unique_Name=schedule.Name,
                Actuated_Component_Type=schedule.key,
                Actuated_Component_Control_Type="Schedule Value"
            )
        )
        ems_instructions = []
        value = conf.get("stop_below", -5)
        ems_instructions.append(f"IF {sensor_name} < {value}")
        value = conf.get("min_flow", 0.1)
        ems_instructions.append(f"SET {actuator_name} = {value}")
        ems_instructions.append("ENDIF")
        value = conf.get("start_above", -5)
        ems_instructions.append(f"IF {sensor_name} >= {value}")
        value = conf.get("normal_flow")
        ems_instructions.append(f"SET {actuator_name} = {value}")
        ems_instructions.append("ENDIF")

        program = EnergymanagementsystemProgram(
            idf,
            **EnergymanagementsystemProgramType(
                Name=program_name)
        )
        for i, instruction in enumerate(ems_instructions):
            program[f"Program_Line_{i+1}"] = instruction
        EnergymanagementsystemProgramcallingmanager(
            idf,
            **EnergymanagementsystemProgramcallingmanagerType(
                Name=f"{equipment_name}_control",
                EnergyPlus_Model_Calling_Point="InsideHVACSystemIterationLoop",
                Program_Name_1=program_name
            )
        )
        equipments[equipment_name]["Pump_Flow_Rate_Schedule_Name"] = schedule.Name


#------------------------------------------------------------------------------
# on crée 2 schedules constants, 20°C chauffage et 25°C raffraichissement :
# - const_temp_sched_20deg
# - const_temp_sched_25deg
#------------------------------------------------------------------------------

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

consigne_cool = constant_schedule(25)
consigne_heat = constant_schedule(20)

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
            Inlet_Node_Name=f"{name} vertical geoexchanger inlet",
            Outlet_Node_Name=f"{name} vertical geoexchanger outlet",
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
    if pump_type == "variable":
        return PumpVariablespeed(
            idf,
            **PumpVariablespeedType(
                Name=name,
                Inlet_Node_Name=f"{name} inlet",
                Outlet_Node_Name=f"{name} outlet",
                Design_Maximum_Flow_Rate=EPValues.AUTOSIZE,
                Design_Power_Consumption=EPValues.AUTOSIZE,
                Motor_Efficiency=0.9,
                Design_Minimum_Flow_Rate=0,
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
            Inlet_Node_Name=f"{name} inlet",
            Outlet_Node_Name=f"{name} outlet",
            Design_Flow_Rate=EPValues.AUTOSIZE,
            Design_Power_Consumption=EPValues.AUTOSIZE,
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
        Minimum_Curve_Output=0.5,
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
            Source_Side_Inlet_Node_Name=f"{name} source side inlet",
            Source_Side_Outlet_Node_Name=f"{name} source side outlet",
            Load_Side_Inlet_Node_Name=f"{name} load side inlet",
            Load_Side_Outlet_Node_Name=f"{name} load side outlet",
            Reference_Load_Side_Flow_Rate=EPValues.AUTOSIZE,
            Reference_Source_Side_Flow_Rate=EPValues.AUTOSIZE,
            Reference_Heating_Capacity=EPValues.AUTOSIZE,
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
            Boiler_Water_Inlet_Node_Name=f"{name}_InletNode",
            Boiler_Water_Outlet_Node_Name=f"{name}_OutletNode",
            Boiler_Flow_Mode="LeavingSetpointModulated"
        )
    )


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
    force_side = CONF[name].get("force_side")
    if force_side:
        return force_side
    return None


def adjust_nodes_branch(loop_name: str, *, loop_side: str, branches_descr: dict[str, list[str]]):
    """use yaml declaration to organise a branch and relevant nodes on a side loop"""
    object_names = branches_descr[loop_side]
    bypass = False
    if BYPASS in branches_descr:
        if loop_side in branches_descr[BYPASS]:
            bypass = True
    # we adjust the nodes
    nb_objects = len(object_names)
    for i, obj in enumerate(object_names):
        inlet_node: str|None = None
        outlet_node: str|None = None
        # start and end of the loop side
        if i == 0:
            inlet_node = LoopNodes(loop_name).get(side=loop_side, port=INLET)
        if i == nb_objects - 1:
            outlet_node = LoopNodes(loop_name).get(side=loop_side, port=OUTLET)
        # we only modify inlets using the previous equipement
        if inlet_node is None:
            # previous object exists
            prev_name = object_names[i-1]
            prev_obj = equipments[prev_name]
            try:
                inlet_node = prev_obj[EPApi.OUTLET_NODE_NAME]
            except BadEPFieldError:
                # we have a 2 sided equipment - heatpump
                side = resolve_side(prev_name, loop_side)
                inlet_node = prev_obj[f"{side}_{EPApi.OUTLET_NODE_NAME}"]
        # if bypass, we dont modify inlet node of first equipment
        if i == 0 and bypass:
            inlet_node = None
        # if bypass, we dont modify outlet node of last equipment
        if i == nb_objects - 1 and bypass:
            outlet_node = None
        set_nodes(
            equipments[obj],
            inlet=inlet_node,
            outlet=outlet_node,
            side=resolve_side(obj, loop_side)
        )
    # we create the branch using the objects as nodes are now correct
    objects = [equipments[obj] for obj in object_names]
    sides = [resolve_side(obj, loop_side) for obj in object_names]
    adjusted_branch = create_branch(
        idf,
        name = Branches(loop_name).get(side=loop_side),
        objects = objects,
        sides = sides
    )
    if bypass:
        side = EPApi.DEMAND_SIDE if loop_side == DEMAND else EPApi.PLANT_SIDE
        plantloop_split_mix(
            idf=idf,
            plantloop=loops[loop_name],
            side=side,
            branches=[adjusted_branch],
            bypass=True
        )


def generate_operation_list(loop_name:str):
    """GENERATE LIST OF EQUIPMENTS & OPERATION SCHEMES FOR A PLANTLOOP"""
    conf = CONF.get(loop_name, {})
    loop_equipment_list = Plantequipmentlist(
        idf,
        **PlantequipmentlistType(
            Name=f"{loop_name} Equipment List",
        )
    )
    for i, obj_name in enumerate(CONF[loop_name].get("operation", [])):
        loop_equipment_list[f"Equipment_{i+1}_Object_Type"] = equipments[obj_name].key
        loop_equipment_list[f"Equipment_{i+1}_Name"] = equipments[obj_name].Name
    loop_type = conf.get("Loop_Type", "heating")
    operation_name = f"{loop_name} {loop_type} operation"
    if loop_type == "cooling":
        loop_operation = PlantequipmentoperationCoolingload(
            idf,
            **PlantequipmentoperationCoolingloadType(
                Name=operation_name,
                Load_Range_1_Lower_Limit=0,
                Load_Range_1_Upper_Limit=1e9,
                Range_1_Equipment_List_Name=loop_equipment_list.Name
            )
        )
    else:
        loop_operation = PlantequipmentoperationHeatingload(
            idf,
            **PlantequipmentoperationHeatingloadType(
                Name=operation_name,
                Load_Range_1_Lower_Limit=0,
                Load_Range_1_Upper_Limit=1e9,
                Range_1_Equipment_List_Name=loop_equipment_list.Name
            )
        )
    Plantequipmentoperationschemes(
        idf,
        **PlantequipmentoperationschemesType(
            Name=loop_name,
            Control_Scheme_1_Object_Type=loop_operation.key,
            Control_Scheme_1_Name=loop_operation.Name,
            Control_Scheme_1_Schedule_Name=ALWAYS_ON
        )
    )
