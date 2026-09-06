"""setpoints management"""

from idfhub.common import idf, CONF, get_logger
from idfhub.hvac import EPApi, EPValues, LoopNodes
from idfhub.hvac24_1_0 import constant_schedule
from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import (
    SetpointmanagerMultizoneCoolingAverage, SetpointmanagerMultizoneCoolingAverageMeta,
    SetpointmanagerOutdoorairreset,SetpointmanagerOutdoorairresetMeta,
    SetpointmanagerScheduled, ScheduleConstantMeta,
    OutputVariable,
)
from idfhub.idf_autocomplete.v24_1_0.idf_types_short import (
    SetpointmanagerMultizoneCoolingAverageType,
    SetpointmanagerOutdoorairresetType, SetpointmanagerScheduledType,
    OutputVariableType,
)

LOGGER = get_logger()

def airloop_setpoint(loop_name: str, setpoint_name: str, node: str):
    """add a specific airloop setpoint"""
    name = f"{setpoint_name}@{node}"
    if "multi_zone_cooling" in setpoint_name:
        setpoint = idf.getobject(
            SetpointmanagerMultizoneCoolingAverageMeta.idf_name,
            name
        )
        if not setpoint:
            setpoint = SetpointmanagerMultizoneCoolingAverage(
                idf,
                **SetpointmanagerMultizoneCoolingAverageType(
                    Name=name,
                    HVAC_Air_Loop_Name=loop_name,
                    Minimum_Setpoint_Temperature=12,
                    Maximum_Setpoint_Temperature=28,
                    Setpoint_Node_or_NodeList_Name=node
                )
            )
            message = f"multi zone cooling average setpoint @ {node}"
            LOGGER.debug(message)


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
            Name=f"{setpoint_name}@{node}",
            Control_Variable=EPValues.TEMPERATURE,
            Schedule_Name=consigne.Name,
            Setpoint_Node_or_NodeList_Name=node,
        )
    )


def oa_reset(loop_name: str, setpoint_name: str, node: str|None = None):
    """add an outdoorair reset on a loop plant outlet"""
    if node is None:
        node = LoopNodes(loop_name).plant_outlet
    name = f"{setpoint_name}@{node}"
    oa_reset_object = idf.getobject(
        SetpointmanagerOutdoorairresetMeta.idf_name,
        name
    )
    if oa_reset_object is not None:
        return
    message = f"outdoor air reset @ {node} with {CONF[setpoint_name]}"
    LOGGER.debug(message)
    SetpointmanagerOutdoorairreset(
        idf,
        **SetpointmanagerOutdoorairresetType(
            Name=name,
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

