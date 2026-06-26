"""Manage hvac equipments"""
import sys
from typing import Any
from eppy.bunch_subclass import BadEPFieldError, EpBunch

from idfhub.hvac import (
    PLANT, SUPPLY, DEMAND, RETURN, INLET, OUTLET, ALWAYS_ON,
    EPApi, EPValues,
    create_branch,
    LoopNodes,
    set_nodes, node_name,
    branchlist_update,
    split_mix, pipe_splitter, pipe_mixer,
    get_branch_inlet_outlet_nodes
)

from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import (
    Scheduletypelimits,ScheduletypelimitsMeta,ScheduleConstant,ScheduleConstantMeta,
    SetpointmanagerOutdoorairreset,SetpointmanagerOutdoorairresetMeta,
    SetpointmanagerScheduled,
    PumpConstantspeed, PumpVariablespeed,
    ScheduleCompact,ScheduleCompactMeta,
    Plantequipmentlist, Plantequipmentoperationschemes,
    PlantequipmentoperationHeatingload, PlantequipmentoperationCoolingload,
    PlantequipmentoperationUncontrolled,
    CurveBiquadratic,
    BoilerHotwater,
    PlantequipmentoperationOutdoordrybulb,
    OutputVariable,
    PlantequipmentoperationComponentsetpoint,
    ZonehvacEquipmentlist, ZonehvacEquipmentlistMeta,
    ThermostatsetpointDualsetpoint,
    ThermostatsetpointSingleheating,
    ThermostatsetpointSinglecooling,
    ZonecontrolThermostat,
)

from idfhub.idf_autocomplete.v24_1_0.idf_types_short import (
    ScheduletypelimitsType,ScheduleConstantType,
    SetpointmanagerOutdoorairresetType, SetpointmanagerScheduledType,
    PumpConstantspeedType, PumpVariablespeedType,
    ScheduleCompactType,
    PlantequipmentlistType, PlantequipmentoperationschemesType,
    PlantequipmentoperationHeatingloadType, PlantequipmentoperationCoolingloadType,
    PlantequipmentoperationUncontrolledType,
    CurveBiquadraticType,
    BoilerHotwaterType,
    PlantequipmentoperationOutdoordrybulbType,
    OutputVariableType,
    PlantequipmentoperationComponentsetpointType,
    ZonehvacEquipmentlistType,
    ThermostatsetpointDualsetpointType,
    ThermostatsetpointSingleheatingType,
    ThermostatsetpointSinglecoolingType,
    ZonecontrolThermostatType,
)

from idfhub.common import get_logger, idf, CONF

LOGGER = get_logger()
BYPASS = "bypass"
loops: dict = {}
equipments: dict[str, Any] = {}

if not idf:
    LOGGER.error("no idf > generate_geometry")
    sys.exit()

def schedule_typelimits(
    name,
    *,
    lower_limit: float|None = None,
    upper_limit: float|None = None,
    numeric_type: str|None = EPValues.CONTINUOUS,
    unit_type: str|None = None
):
    """create a typelimits object"""
    typelimit = idf.getobject(
        ScheduletypelimitsMeta.idf_name,
        name
    )
    if not typelimit:
        typelimit = Scheduletypelimits(
            idf,
            **ScheduletypelimitsType(
                Name=name
            )
        )
        if lower_limit is not None:
            typelimit["Lower_Limit_Value"] = lower_limit
        if upper_limit is not None:
            typelimit["Upper_Limit_Value"] = upper_limit
        if numeric_type:
            typelimit["Numeric_Type"] = numeric_type
        if unit_type:
            typelimit["Unit_Type"] = unit_type
    return typelimit


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
    value_confort: float,
    value_standby: float,
    *,
    schedule_name: str,
    typelimits_name: str
):
    """create a compact schedule"""
    compact_sched = idf.getobject(
        ScheduleCompactMeta.idf_name,
        schedule_name
    )
    if not compact_sched:
        compact_sched = ScheduleCompact(
            idf,
            **ScheduleCompactType(
                Name=schedule_name,
                Schedule_Type_Limits_Name=typelimits_name,
                Field_1=f"{EPValues.THROUGH}: 12/31",
                Field_2=f"{EPValues.FOR}: {EPValues.WEEKDAYS}",
                Field_3=f"{EPValues.UNTIL}: 07:00",
                Field_4=value_standby,
                Field_5=f"{EPValues.UNTIL}: 17:00",
                Field_6=value_confort,
                Field_7=f"{EPValues.UNTIL}: 24:00",
                Field_8=value_standby,
                Field_9=f"{EPValues.FOR}: {EPValues.WEEKENDS}",
                Field_10=f"{EPValues.UNTIL}: 24:00",
                Field_11=value_standby,
                Field_12=f"{EPValues.FOR}:{EPValues.WINTER_DESIGN_DAY}",
                Field_13=f"{EPValues.UNTIL}: 07:00",
                Field_14=value_standby,
                Field_15=f"{EPValues.UNTIL}: 17:00",
                Field_16=value_confort,
                Field_17=f"{EPValues.UNTIL}: 24:00",
                Field_18=value_standby,
                Field_19=f"{EPValues.FOR}:{EPValues.SUMMER_DESIGN_DAY}",
                Field_20=f"{EPValues.UNTIL}: 07:00",
                Field_21=value_standby,
                Field_22=f"{EPValues.UNTIL}: 17:00",
                Field_23=value_confort,
                Field_24=f"{EPValues.UNTIL}: 24:00",
                Field_25=value_standby,
            )
        )
    return compact_sched


def constant_schedule(
    value: int,
    *,
    typelimits_name: str,
    name: str|None = None
):
    """create a constant schedule type"""
    if name is None:
        name = f"const_temp_sched_{value}deg"
    constant_sched = idf.getobject(
        ScheduleConstantMeta.idf_name,
        name
    )
    if not constant_sched:
        constant_sched = ScheduleConstant(
            idf,
            **ScheduleConstantType(
                Name=name,
                Schedule_Type_Limits_Name=typelimits_name,
                Hourly_Value=value
            )
        )
    return constant_sched


def schedule_objects(conf: dict[str, dict]) -> dict[str, EpBunch]:
    """build schedules idf objects from yml conf"""
    schedules: dict[str, EpBunch] = {}
    for sched_name, sched_conf in conf.items():
        confort = sched_conf["confort"]
        standby = sched_conf["standby"]
        if sched_conf["mode"] == "compact":
            schedules[sched_name] = basic_compact_schedule(
                confort,
                standby,
                schedule_name=f"{sched_name}_schedule_{confort}",
                typelimits_name=EPValues.TEMPERATURE
            )
        else:
            schedules[sched_name] = constant_schedule(
                confort,
                typelimits_name=EPValues.TEMPERATURE
            )
    return schedules


def zone_control(schedules: dict[str, EpBunch], zones: list[str], cooling_conf: dict):
    """control zone schedule"""
    required = ("from", "to")
    thermostats: dict[str, EpBunch] = {}
    if all(key in cooling_conf for key in required):
        summer_start = cooling_conf["from"]
        summer_end = cooling_conf["to"]
        # 1 is heating and 2 is cooling in control types
        control_schedule = idf.getobject(
            ScheduleCompactMeta.idf_name,
            "SeasonalSetpoint"
        )
        if not control_schedule:
            control_schedule = ScheduleCompact(
                idf,
                **ScheduleCompactType(
                    Name="SeasonalSetpoint",
                    Schedule_Type_Limits_Name=EPValues.CONTROL_TYPES,
                    Field_1=f"{EPValues.THROUGH}: {summer_start}",
                    Field_2=f"{EPValues.FOR}: {EPValues.ALLDAYS}",
                    Field_3=f"{EPValues.UNTIL}: 24:00,1",
                    Field_4=f"{EPValues.THROUGH}: {summer_end}",
                    Field_5=f"{EPValues.FOR}: {EPValues.ALLDAYS}",
                    Field_6=f"{EPValues.UNTIL}: 24:00,2",
                    Field_7=f"{EPValues.THROUGH}: 12/31",
                    Field_8=f"{EPValues.FOR}: {EPValues.ALLDAYS}",
                    Field_9=f"{EPValues.UNTIL}: 24:00,1",
                )
            )
        thermostats["heating"] = ThermostatsetpointSingleheating(
            idf,
            **ThermostatsetpointSingleheatingType(
                Name="heating thermostat",
                Setpoint_Temperature_Schedule_Name=schedules["heating"].Name
            )
        )
        thermostats["cooling"] = ThermostatsetpointSinglecooling(
            idf,
            **ThermostatsetpointSinglecoolingType(
                Name="cooling thermostat",
                Setpoint_Temperature_Schedule_Name=schedules["cooling"].Name
            )
        )
    else:
        control_schedule = idf.getobject(
            ScheduleCompactMeta.idf_name,
            "AlwaysDualSetpoint"
        )
        if not control_schedule:
            control_schedule = constant_schedule(
                4,
                name= "AlwaysDualSetpoint",
                typelimits_name=EPValues.CONTROL_TYPES
            )
        thermostats["dual"] = ThermostatsetpointDualsetpoint(
            idf,
            **ThermostatsetpointDualsetpointType(
                Name="dual_thermostat",
                Heating_Setpoint_Temperature_Schedule_Name=schedules["heating"].Name,
                Cooling_Setpoint_Temperature_Schedule_Name=schedules["cooling"].Name
            )
        )
    for zone in zones:
        controller = ZonecontrolThermostat(
            idf,
            **ZonecontrolThermostatType(
                Name=f"{zone}_thermostat",
                Zone_or_ZoneList_Name=zone,
                Control_Type_Schedule_Name=control_schedule.Name,
            )
        )
        for i, thermostat in enumerate(thermostats.values()):
            controller[f"Control_{i+1}_Object_Type"] = thermostat.key
            controller[f"Control_{i+1}_Name"] = thermostat.Name


#------------------------------------------------------------------------------
# SETPOINTS
#------------------------------------------------------------------------------
def water_law(loop_name: str, setpoint_name: str, node: str|None = None):
    """add a waterlaw setpoint on a loop plant outlet"""
    if node is None:
        node = LoopNodes(loop_name).plant_outlet
    water_law_name = f"{setpoint_name} {loop_name}"
    water_law_object = idf.getobject(
        SetpointmanagerOutdoorairresetMeta.idf_name,
        water_law_name
    )
    if water_law_object is not None:
        return
    message = f"waterlaw @ {node} with {CONF[setpoint_name]}"
    LOGGER.debug(message)
    SetpointmanagerOutdoorairreset(
        idf,
        **SetpointmanagerOutdoorairresetType(
            Name=f"{setpoint_name} {loop_name}",
            Control_Variable=EPValues.TEMPERATURE,
            Setpoint_at_Outdoor_Low_Temperature=CONF[setpoint_name].get(
                "Setpoint_at_Outdoor_Low_Temperature", 70),
            Outdoor_Low_Temperature=CONF[setpoint_name].get(
                "Outdoor_Low_Temperature", -5),
            Setpoint_at_Outdoor_High_Temperature=CONF[setpoint_name].get(
                "Setpoint_at_Outdoor_High_Temperature", 40),
            Outdoor_High_Temperature=CONF[setpoint_name].get(
                "Outdoor_High_Temperature", 15),
            Setpoint_Node_or_NodeList_Name=node
        )
    )
    OutputVariable(
        idf,
        **OutputVariableType(
            Key_Value=node,
            Variable_Name="System Node Setpoint Temperature",
            Reporting_Frequency="Timestep"
        )
    )

def constant_set_point(loop_name: str, setpoint_name: str):
    """add a constant setpoint on a loop plant outlet"""
    node = LoopNodes(loop_name).plant_outlet
    message = f"constant setpoint @ {node} with {CONF[setpoint_name]}"
    LOGGER.debug(message)
    temp = CONF[setpoint_name].get("temp", 12)
    name = f"const_temp_sched_{temp}deg"
    consigne = idf.getobject(
        ScheduleConstantMeta.idf_name,
        name
    )
    if consigne is None:
        consigne = constant_schedule(
            temp,
            name=name,
            typelimits_name=EPValues.TEMPERATURE
        )
    SetpointmanagerScheduled(
        idf,
        **SetpointmanagerScheduledType(
            Name=f"{setpoint_name} {loop_name}",
            Control_Variable=EPValues.TEMPERATURE,
            Schedule_Name=consigne.Name,
            Setpoint_Node_or_NodeList_Name=node,
        )
    )

#------------------------------------------------------------------------------
# PRODUCTION SYSTEMS
#------------------------------------------------------------------------------

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
            Nominal_Capacity=conf.get(
                "Nominal_Capacity",
                EPValues.AUTOSIZE
            ),
            Nominal_Thermal_Efficiency=conf.get(
                "Nominal_Thermal_Efficiency",
                0.8
            ),
            Boiler_Water_Inlet_Node_Name=f"{name}_inlet_node",
            Boiler_Water_Outlet_Node_Name=f"{name}_outlet_node",
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


def generate_operation(
    *,
    loop_name:str,
    control_mode: str,
    loop_type: str,
    names: list[str],
    operation_type: str|None = None
):
    """return operation object
    names = list of equipment names"""
    operation_name = f"{loop_name} operation"
    if control_mode == "ComponentSetpoint":
        operation = PlantequipmentoperationComponentsetpoint(
            idf,
            **PlantequipmentoperationComponentsetpointType(
                Name=operation_name)
        )
        for i, obj_name in enumerate(names):
            side = resolve_side(obj_name, PLANT)
            equipment = equipments[obj_name]
            inlet = equipment[f"{side}_{EPApi.INLET_NODE_NAME}"]
            outlet = equipment[f"{side}_{EPApi.OUTLET_NODE_NAME}"]
            operation[f"Equipment_{i+1}_Object_Type"] = equipment.key
            operation[f"Equipment_{i+1}_Name"] = obj_name
            operation[f"Demand_Calculation_{i+1}_Node_Name"] = inlet
            operation[f"Setpoint_{i+1}_Node_Name"] = outlet
            operation[f"Component_{i+1}_Flow_Rate"] = EPValues.AUTOSIZE
            operation[f"Operation_{i+1}_Type"] = EPValues.HEATING
        return operation
    list_names = []
    if "mix" in loop_type.lower():
        LOGGER.info("mix mode :-)")
        # a list for each machine referenced in the operation loop
        for i, obj_name in enumerate(names):
            list_name = f"{obj_name}_Only"
            Plantequipmentlist(
                idf,
                **PlantequipmentlistType(
                    Name=list_name,
                    Equipment_1_Object_Type = equipments[obj_name].key,
                    Equipment_1_Name = equipments[obj_name].Name
                )
            )
            list_names.append(list_name)
    else:
        # a single list with all the machines
        list_name = f"{loop_name} Equipment List"
        loop_equipment_list = Plantequipmentlist(
            idf,
            **PlantequipmentlistType(
                Name=list_name
            )
        )
        for i, obj_name in enumerate(names):
            loop_equipment_list[f"Equipment_{i+1}_Object_Type"] = equipments[obj_name].key
            loop_equipment_list[f"Equipment_{i+1}_Name"] = equipments[obj_name].Name
        list_names.append(list_name)

    if control_mode.lower() == EPValues.LOAD.lower():
        operation_types = [
            "heating",
            "cooling",
            "uncontrolled"
        ]
        if operation_type is None:
            for value in operation_types:
                if value in loop_type.lower():
                    operation_type = value
                    break
        if operation_type == "uncontrolled":
            operation = PlantequipmentoperationUncontrolled(
                idf,
                **PlantequipmentoperationUncontrolledType(
                    Name=operation_name,
                    Equipment_List_Name=list_names[0]
                    )
            )
            return operation
        if operation_type == "heating":
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
        for i, list_name in enumerate(list_names):
            try:
                obj_name = names[i]
            except IndexError:
                op_range = [0, 1e9]
            else:
                op_range = CONF[obj_name].get(
                    "operation_range",
                    [0, 1e9]
                )
            operation[f"Range_{i+1}_Equipment_List_Name"] = list_name
            operation[f"Load_Range_{i+1}_Lower_Limit"] = op_range[0]
            operation[f"Load_Range_{i+1}_Upper_Limit"] = op_range[1]
        return operation
    # on est en control_mode == "OutdoorDryBulb":
    operation = PlantequipmentoperationOutdoordrybulb(
        idf,
        **PlantequipmentoperationOutdoordrybulbType(
            Name=operation_name)
    )
    for i, list_name in enumerate(list_names):
        try:
            obj_name = names[i]
        except IndexError:
            op_range = [-20, 20]
        else:
            op_range = CONF[obj_name].get(
                "operation_range",
                [-20, 20]
            )
        operation[f"Range_{i+1}_Equipment_List_Name"] = list_name
        operation[f"DryBulb_Temperature_Range_{i+1}_Lower_Limit"] = op_range[0]
        operation[f"DryBulb_Temperature_Range_{i+1}_Upper_Limit"] = op_range[1]
    return operation


def operation_list_scheme(loop_name:str):
    """GENERATE OPERATION SCHEMES FOR A PLANTLOOP"""
    conf = CONF.get(loop_name, {})
    loop_type = conf.get("Loop_Type", EPValues.HEATING)
    control_mode = conf.get("control_mode", EPValues.LOAD)
    LOGGER.info("%s > %s", loop_type, control_mode)
    loop_machines = conf.get("operation", [])
    operations = []
    if isinstance(loop_machines, dict):
        for operation_type, machines in loop_machines.items():
            operations.append(
                generate_operation(
                    loop_name=loop_name,
                    control_mode=control_mode,
                    loop_type=loop_type,
                    names=machines,
                    operation_type=operation_type
                )
            )
    else:
        # a single operation
        operations.append(
            generate_operation(
                loop_name=loop_name,
                control_mode=control_mode,
                loop_type=loop_type,
                names=loop_machines,
            )
        )
    # a single scheme for the loop with all operations
    scheme = Plantequipmentoperationschemes(
        idf,
        **PlantequipmentoperationschemesType(
            Name=loop_name
        )
    )
    for i, operation in enumerate(operations):
        scheme[f"Control_Scheme_{i+1}_Object_Type"] = operation.key
        scheme[f"Control_Scheme_{i+1}_Name"] = operation.Name
        scheme[f"Control_Scheme_{i+1}_Schedule_Name"] = ALWAYS_ON


def zone_list(
    zone_name: str,
    zone_equipments: EpBunch | list[EpBunch]
) -> EpBunch:
    """manage zone equipements"""
    suffix = "Zone_Equipment"
    equipment_list_name = f"{zone_name} equipment list"
    zone_equipment_list = idf.getobject(
        ZonehvacEquipmentlistMeta.idf_name,
        equipment_list_name
    )
    start_index = 1
    cooling_index = 1
    heating_index = 1
    if zone_equipment_list:
        while True:
            field = f"{suffix}_{start_index}_Name"
            if field not in zone_equipment_list.fieldnames:
                break
            name = getattr(zone_equipment_list, field)
            if not name:
                break
            start_index += 1
    else:
        zone_equipment_list = ZonehvacEquipmentlist(
            idf,
            **ZonehvacEquipmentlistType(
                Name=equipment_list_name
            )
        )
    def heating_field(i):
        """heating field to search"""
        return f"{suffix}_{i}_Heating_or_NoLoad_Sequence"
    def cooling_field(i):
        """cooling field to search"""
        return f"{suffix}_{i}_Cooling_Sequence"
    if start_index > 1:
        cooling_indexes = [
            int(getattr(zone_equipment_list, heating_field(i)))
            for i in range(1, start_index)
        ]
        heating_indexes = [
            int(getattr(zone_equipment_list, cooling_field(i)))
            for i in range(1, start_index)
        ]
        cooling_index = max(cooling_indexes) + 1
        heating_index = max(heating_indexes) + 1
    if not isinstance(zone_equipments, list):
        zone_equipments = [zone_equipments]
    for i, equipment in enumerate(zone_equipments):
        conf = CONF.get(equipment.Name, {})
        process = conf.get("process", "heating")
        if process == "heating":
            cooling = 0
            heating = heating_index
            heating_index += 1
        else:
            heating = 0
            cooling = cooling_index
            cooling_index += 1
        zone_equipment_list[f"{suffix}_{start_index + i}_Name"] = equipment.Name
        zone_equipment_list[f"{suffix}_{start_index + i}_Object_Type"] = equipment.key
        zone_equipment_list[cooling_field(start_index + i)] = cooling
        zone_equipment_list[heating_field(start_index + i)] = heating
    return zone_equipment_list
