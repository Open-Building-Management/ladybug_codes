"""hvac four pipe fan coil (and two pipe also)

# Capacity_Control_Method
Si le ventilateur tourne toujours à la même vitesse et que seule la vanne d'eau froide module : ConstantFanVariableFlow
Si vanne On/Off et fan Petite/Moyenne/Grande vitesse : MultiSpeedFan
Si moteur EC/vitesse variable continue/vanne modulante : VariableFanVariableFlow


Pour une zone :
Zone Air Node = air mélangé de la pièce, référence, n'est pas un node de connexion
zone_air_inlet_node = là où les équipements soufflent
zone_air_exhaust_node = là où les équipements prélèvent

Pour le Fan, on prend 120 Pa de pressure rise, parce que le système est local (zone HVAC)
- peu de pertes réseau
- seulement une batterie eau glacée, une grille de soufflage et un petit plénum (volume air “tampon”)
pour les vitesses :
- petite vitesse ≈ confort nuit / faible charge
- moyenne ≈ régime normal
- grande ≈ pointe
"""
from typing import Tuple
from eppy.bunch_subclass import EpBunch

from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import (
    ZonehvacFourpipefancoil,
    FanSystemmodel,
    CoilCoolingWater,
    CoilHeatingElectric,
    OutdoorairMixer,
    OutputVariable,
    OutdoorairNode,
)

from idfhub.idf_autocomplete.v24_1_0.idf_types_short import (
    ZonehvacFourpipefancoilType,
    FanSystemmodelType,
    CoilCoolingWaterType,
    CoilHeatingElectricType,
    OutdoorairMixerType,
    OutputVariableType,
    OutdoorairNodeType,
)

from idfhub.common import idf
from idfhub.hvac24_1_0 import (
    EPValues,
    schedule_typelimits, summer,
    constant_schedule, two_season_schedule
)

def fcu_cooling(
    name: str,
    *,
    zone_air_inlet_node: str,
    zone_air_exhaust_node: str
) -> Tuple[EpBunch, EpBunch]:
    """ventilo convecteur
    FCU : Fan Coil Unit
    Le FCU :
    - puise sur le zone_exhaust_air, 
    - le mixe à l'air extérieur, le fait passer dans le fan,
    - le raffraichit avec la CC = coil cooling
    - rejette vers zone_air_inlet"""
    zone_name = name.split("_")[1]
    # le noeud de l'air extérieur
    oa_in_node = f"{name} OA in node"
    zone_oa_mixer_outlet = f"{zone_name} mixer outlet node"
    node_names = [
        oa_in_node,
        zone_air_exhaust_node,
        zone_oa_mixer_outlet,
        zone_air_inlet_node,
    ]
    rdd_variables = [
        "System Node Temperature",
        "System Node Mass Flow Rate"
    ]
    for node_name in node_names:
        for variable in rdd_variables:
            OutputVariable(
                idf,
                **OutputVariableType(
                    Key_Value=node_name,
                    Variable_Name=variable,
                    Reporting_Frequency="Timestep"
                )
            )
    mixer = OutdoorairMixer(
        idf,
        **OutdoorairMixerType(
            Name=f"{name} OA mixer",
            Mixed_Air_Node_Name= zone_oa_mixer_outlet,
            Outdoor_Air_Stream_Node_Name=oa_in_node,
            Relief_Air_Stream_Node_Name=f"{name} Exh node",
            Return_Air_Stream_Node_Name=zone_air_exhaust_node
        )
    )
    OutdoorairNode(
        idf,
        **OutdoorairNodeType(
            Name=oa_in_node
        )
    )
    fan = FanSystemmodel(
        idf,
        **FanSystemmodelType(
            Name=f"{name}_fan",
            Air_Inlet_Node_Name=zone_oa_mixer_outlet,
            Air_Outlet_Node_Name=f"{name}_fan_outlet",
            Design_Maximum_Air_Flow_Rate=EPValues.AUTOSIZE,
            Design_Pressure_Rise=120,
            Motor_Efficiency=0.8,
            Number_of_Speeds=3,
            Speed_1_Flow_Fraction=0.33,
            Speed_2_Flow_Fraction=0.66,
            Speed_3_Flow_Fraction=1,
            Speed_1_Electric_Power_Fraction=0.3,
            Speed_2_Electric_Power_Fraction=0.65,
            Speed_3_Electric_Power_Fraction=1
        )
    )
    # availability schedule
    # typelimits are initialized in generate_hvac
    # so this part is not really needed
    schedule_typelimits(
        EPValues.FRACTIONAL,
        lower_limit=0, upper_limit=1
    )
    summer_start, summer_end = summer()
    if summer_start and summer_end:
        fan_schedule = two_season_schedule(
            name=f"common_summer_fan_schedule",
            period_start=summer_start,
            period_end=summer_end,
            value_on_period=1,
            value_out_period=0,
            typelimits_name=EPValues.FRACTIONAL
        )
        fan["Availability_Schedule_Name"] = fan_schedule.Name
    coil_cooling_water = CoilCoolingWater(
        idf,
        **CoilCoolingWaterType(
            Name=f"{name}_coil_cooling_water",
            Water_Inlet_Node_Name=f"{name}_water_inlet",
            Water_Outlet_Node_Name=f"{name}_water_outlet",
            Air_Inlet_Node_Name=f"{name}_fan_outlet",
            Air_Outlet_Node_Name=f"{name}_CC_water_air_outlet"
        )
    )
    always_off = "Always OFF"
    constant_schedule(
        0, typelimits_name=EPValues.FRACTIONAL,
        name = always_off
    )
    coil_heating_electric = CoilHeatingElectric(
        idf,
        **CoilHeatingElectricType(
            Name=f"{name}_coil_heating_electric",
            Air_Inlet_Node_Name=f"{name}_CC_water_air_outlet",
            Air_Outlet_Node_Name=zone_air_inlet_node,
            Availability_Schedule_Name=always_off
        ) 
    )
    # other control methods
    # ConstantFanVariableFlow < pour les FanConstantVolume
    # CyclingFan < pour les FanOnOff
    fcu = ZonehvacFourpipefancoil(
        idf,
        **ZonehvacFourpipefancoilType(
            Name=name,
            Capacity_Control_Method="MultiSpeedFan",
            Maximum_Supply_Air_Flow_Rate=EPValues.AUTOSIZE,
            Maximum_Outdoor_Air_Flow_Rate=EPValues.AUTOSIZE,
            Outdoor_Air_Mixer_Object_Type=mixer.key,
            Outdoor_Air_Mixer_Name=mixer.Name,
            Air_Inlet_Node_Name=zone_air_exhaust_node,
            Air_Outlet_Node_Name=zone_air_inlet_node,
            Supply_Air_Fan_Name=fan.Name,
            Supply_Air_Fan_Object_Type=fan.key,
            Cooling_Coil_Name=coil_cooling_water.Name,
            Cooling_Coil_Object_Type=coil_cooling_water.key,
            Maximum_Cold_Water_Flow_Rate=EPValues.AUTOSIZE,
            Heating_Coil_Name=coil_heating_electric.Name,
            Heating_Coil_Object_Type=coil_heating_electric.key,
            Maximum_Hot_Water_Flow_Rate=EPValues.AUTOSIZE
        )
    )
    return coil_cooling_water, fcu
