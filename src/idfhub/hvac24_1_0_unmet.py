"""unmet hours tools
not used - evrything usefull is in the html :-)
"""

from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import(
    EnergymanagementsystemSensorMeta,
    EnergymanagementsystemProgram
)

from idfhub.idf_autocomplete.v24_1_0.idf_types_short import(
    EnergymanagementsystemProgramType
)

from .common import idf
from .hvac24_1_0 import create_sensor

def evaluate_unmet(zone_name, schedule_name):
    """evaluate unmet hours"""
    # same activity for all the zones > a single sensor
    activity_sensor = idf.getobject(
        EnergymanagementsystemSensorMeta.idf_name,
        "activity"
    )
    if not activity_sensor:
        create_sensor(
            sensor_name="activity",
            sensor_type="Schedule Value",
            location_name=schedule_name
        )
    zone_temp = create_sensor(
        sensor_name=f"T_{zone_name}",
        sensor_type="Zone Air Temperature",
        location_name=zone_name
    )
    zone_setpoint = create_sensor(
        sensor_name=f"Tset_{zone_name}",
        sensor_type="Zone Thermostat Heating Setpoint Temperature",
        location_name=zone_name
    )
    EnergymanagementsystemProgram(
        idf,
        **EnergymanagementsystemProgramType(
            Name=f"calcUnmet{zone_name}",
            Program_Line_1=f"IF (activity > 0) && ({zone_temp.Name} < {zone_setpoint.Name})",
            Program_Line_2="SET UnmetFlag = 1",
            Program_Line_3="ELSE",
            Program_Line_4="SET UnmetFlag = 0",
            Program_Line_5="ENDIF"
        )
    )
