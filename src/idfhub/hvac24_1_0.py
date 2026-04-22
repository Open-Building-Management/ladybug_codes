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
    CoilWaterheatingAirtowaterheatpumpPumped, OutdoorairNode,
    CurveBiquadratic, CurveQuadratic,
    BoilerHotwater,
    EnergymanagementsystemGlobalvariable,EnergymanagementsystemOutputvariable,
    EnergymanagementsystemMeteredoutputvariable,
    OutputVariable,
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
    CoilWaterheatingAirtowaterheatpumpPumpedType, OutdoorairNodeType,
    CurveBiquadraticType, CurveQuadraticType,
    BoilerHotwaterType,
    EnergymanagementsystemGlobalvariableType, EnergymanagementsystemOutputvariableType,
    EnergymanagementsystemMeteredoutputvariableType,
    OutputVariableType
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

class EmsProgram():
    """manage ems instructions"""
    def __init__(self, name):
        """initialization"""
        self.conf = CONF[name]
        self.ems_instructions = []

    def append(self, instruction):
        """add an instruction to the list"""
        self.ems_instructions.append(instruction)

    def upper_limit(self, var_name, upper_limit):
        """upper limit a var"""
        self.ems_instructions.append(f"IF {var_name} > {upper_limit}")
        self.ems_instructions.append(f"SET {var_name} = {upper_limit}")
        self.ems_instructions.append("ENDIF")

    def lower_limit(self, var_name, lower_limit):
        """lower limit a var"""
        self.ems_instructions.append(f"IF {var_name} < {lower_limit}")
        self.ems_instructions.append(f"SET {var_name} = {lower_limit}")
        self.ems_instructions.append("ENDIF")

    def clamp(self, var_name, lower_limit, upper_limit):
        """clamp on a var name"""
        self.lower_limit(var_name, lower_limit)
        self.upper_limit(var_name, upper_limit)

    def get(self):
        """return the instructions array"""
        return self.ems_instructions

    def biquadratic_on_x_y(self, *, key, var_name):
        """add a biquadratic formula on ems variables x and y"""
        c = self.conf.get(f"{key}_c", 1.192)
        x = self.conf.get(f"{key}_x", 0.05)
        x2 = self.conf.get(f"{key}_x2", -0.0007)
        y = self.conf.get(f"{key}_y", -0.035)
        y2 = self.conf.get(f"{key}_y2", 0.00025)
        xy = self.conf.get(f"{key}_xy", -0.0012)
        formula = f"{c}+{x}*x+{x2}*x*x+{y}*y+{y2}*y*y+{xy}*x*y"
        formula = formula.replace("+-","-")
        self.ems_instructions.append(f"SET {var_name} = {formula}")

def add_ems_vars_to_output(ems_var_names: list[str], name_suffix: str):
    """add ems variables to the outputs"""
    global_ems_vars = EnergymanagementsystemGlobalvariable(
        idf,
        **EnergymanagementsystemGlobalvariableType()
    )
    for i, ems_var_name in enumerate(ems_var_names):
        global_ems_vars[f"Erl_Variable_{i+1}_Name"] = ems_var_name
        output_name = f"{name_suffix}_{ems_var_name}"
        EnergymanagementsystemOutputvariable(
            idf,
            **EnergymanagementsystemOutputvariableType(
                Name=output_name,
                EMS_Variable_Name=ems_var_name,
                Type_of_Data_in_Variable="Averaged",
                Update_Frequency="SystemTimestep"
            )
        )
        OutputVariable(
            idf,
            **OutputVariableType(
                Key_Value="*",
                Variable_Name=output_name,
                Reporting_Frequency="Timestep"
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


def air_to_water_heatpump_ems(name):
    """simulate an air to water heatpump using EMS"""
    conf = CONF[name]
    nominal_capacity = conf.get("Nominal_Capacity", 30000)
    loop = conf.get("loop")
    water_node_name = LoopNodes(loop).get(
        side=conf.get("water_node_side", PLANT),
        port=conf.get("water_node_port", INLET)
    )
    setpoint_node_name = LoopNodes(loop).get(side=PLANT, port=OUTLET)
    text_sensor = create_sensor(
        sensor_name="T_ext",
        sensor_type="Site Outdoor Air Drybulb Temperature",
        location_name="Environment"
    )
    mdot_sensor = create_sensor(
        sensor_name=f"{name}_m_dot",
        sensor_type="System Node Mass Flow Rate",
        location_name=water_node_name
    )
    twater_sensor = create_sensor(
        sensor_name=f"{name}_T_water_in",
        sensor_type="System Node Temperature",
        location_name=water_node_name
    )
    setpoint_sensor = create_sensor(
        sensor_name=f"{name}_T_set",
        sensor_type="System Node Setpoint Temperature",
        location_name=setpoint_node_name
    )
    # equipments
    # boiler = injecteur PAC
    hp_virtual_boiler = BoilerHotwater(
        idf,
        **BoilerHotwaterType(
            Name=f"{name}_Virtual_Boiler",
            Fuel_Type="NaturalGas", # no impact
            Nominal_Capacity=nominal_capacity,
            Nominal_Thermal_Efficiency=10000, # pour effacer la consommation de gaz
            Boiler_Water_Inlet_Node_Name=f"{name}_HP_WaterInletNode",
            Boiler_Water_Outlet_Node_Name=f"{name}_HP_WaterOutletNode"
        )
    )
    pwr_sensor = create_sensor(
        sensor_name=f"{name}_Q_boiler",
        sensor_type="Boiler Heating Rate",
        location_name=hp_virtual_boiler.Name,
    )
    # actuator
    actuator_setpoint = EnergymanagementsystemActuator(
        idf,
        **EnergymanagementsystemActuatorType(
            Name=f"{name}_T_set_limited",
            Actuated_Component_Unique_Name=setpoint_node_name,
            Actuated_Component_Type="System Node Setpoint",
            Actuated_Component_Control_Type="Temperature Setpoint"
        )
    )
    ems_program = EmsProgram(name)
    ems_program.append(f"SET Q_nom = {nominal_capacity}")
    ems_program.append(f"SET x = {text_sensor.Name}")
    ems_program.append(f"SET y = {twater_sensor.Name}")
    ems_program.biquadratic_on_x_y(key="capacity", var_name="CapFTemp")
    ems_program.clamp("CapFTemp", 0, 1.2)
    ems_program.append("SET Q_available = Q_nom * CapFTemp")
    ems_program.append("SET Cp = 4180")
    ems_program.append(f"IF {mdot_sensor.Name} > 0")
    ems_program.append(f"SET DeltaT_possible = Q_available / ({mdot_sensor.Name} * Cp)")
    ems_program.append("ELSE, SET DeltaT_possible = 0, ENDIF")
    ems_program.append(f"SET T_possible = {twater_sensor.Name} + DeltaT_possible")
    ems_program.upper_limit("T_possible", 55)
    ems_program.append(f"SET {actuator_setpoint.Name} = {setpoint_sensor.Name}")
    ems_program.upper_limit(actuator_setpoint.Name, "T_possible")
    # COP, PLR & PLF / quality indicators
    ems_program.append(f"SET COP_nom = {conf.get("cop", 3.2)}")
    ems_program.biquadratic_on_x_y(key="cop", var_name="COPFTemp")
    ems_program.clamp("COPFTemp", 0.4, 2.0)
    ems_program.append("SET COP = COP_nom * COPFTemp")
    ems_program.lower_limit("COP", 1.1)
    ems_program.append(f"SET Q_demand = {mdot_sensor.Name} * Cp * ({setpoint_sensor.Name} - y)")
    ems_program.append("IF Q_available > 0")
    ems_program.append("SET PLR = Q_demand / Q_available, ELSE, SET PLR = 0, ENDIF")
    ems_program.clamp("PLR", 0, 1)
    ems_program.append("SET PLF = 0.85 + 0.15 * PLR")
    ems_program.append("SET COP_effective = COP / PLF")
    ems_program.lower_limit("COP_effective", 1)
    ems_program.append("IF COP_effective > 0")
    ems_program.append(f"SET P_elec = {pwr_sensor.Name} / COP_effective, ELSE, SET P_elec = 0")
    ems_program.append("ENDIF")
    ems_program.append("SET E_elec = P_elec * SystemTimeStep * 3600")

    program = EnergymanagementsystemProgram(
        idf,
        **EnergymanagementsystemProgramType(
            Name=f"{name}_HP_Calc"
        )
    )
    for i, instruction in enumerate(ems_program.get()):
        program[f"Program_Line_{i+1}"] = instruction
    EnergymanagementsystemProgramcallingmanager(
        idf,
        **EnergymanagementsystemProgramcallingmanagerType(
            Name=f"{name}_HP_Control_Manager",
            EnergyPlus_Model_Calling_Point="InsideHVACSystemIterationLoop",
            Program_Name_1=program.Name
        )
    )
    output_var_list = [
        "PLR", "PLF",
        "COP", "COP_effective",
        "y", "P_elec", "E_elec",
    ]
    add_ems_vars_to_output(output_var_list, name)
    EnergymanagementsystemMeteredoutputvariable(
        idf,
        **EnergymanagementsystemMeteredoutputvariableType(
            Name=f"{name}_Electricity",
            EMS_Variable_Name="E_elec",
            Update_Frequency="SystemTimestep",
            Resource_Type="Electricity",
            Group_Type="HVAC",
            EndUse_Category="Heating",
            Units="J"
        )
    )
    return hp_virtual_boiler


def air_to_water_heatpump(name):
    """add an air to water heatpump
    cannot be injected as is on a plantloop !"""
    air_node_name = f"{name}_InputOutdoorAirNode"
    input_air_node = OutdoorairNode(
        idf,
        **OutdoorairNodeType(
            Name=air_node_name,
            Height_Above_Ground=10
        )
    )
    # un set de courbes théoriques pour fonctionner avec une loi d'eau de type 35/55
    heating_capacity_curve = CurveBiquadratic(
        idf,
        **CurveBiquadraticType(
            Name=f"{name}_HP_AW_HeatingCapFTemp",
            Coefficient1_Constant=0.88,
            Coefficient2_x=0.02, # x=air
            Coefficient3_x2=-0.0002,
            Coefficient4_y=-0.015, # y=water
            Coefficient5_y2=-0.00015,
            Coefficient6_xy=-0.0004,
            Minimum_Value_of_x=-10,
            Maximum_Value_of_x=20,
            Minimum_Value_of_y=20,
            Maximum_Value_of_y=60,
            Input_Unit_Type_for_X=EPValues.TEMPERATURE,
            Input_Unit_Type_for_Y=EPValues.TEMPERATURE,
            Output_Unit_Type=EPValues.DIMENSIONLESS
        )
    )
    cop_curve = CurveBiquadratic(
        idf,
        **CurveBiquadraticType(
            Name=f"{name}_HP_AW_HeatingCOPFTemp",
            Coefficient1_Constant=1.192,
            Coefficient2_x=0.050, # x=air
            Coefficient3_x2=-0.0007,
            Coefficient4_y=-0.035, #y=water
            Coefficient5_y2=0.00025,
            Coefficient6_xy=-0.0012,
            Minimum_Value_of_x=-10,
            Maximum_Value_of_x=20,
            Minimum_Value_of_y=20,
            Maximum_Value_of_y=60,
            Minimum_Curve_Output=0.4,
            Maximum_Curve_Output=2,
            Input_Unit_Type_for_X=EPValues.TEMPERATURE,
            Input_Unit_Type_for_Y=EPValues.TEMPERATURE,
            Output_Unit_Type=EPValues.DIMENSIONLESS
        )
    )
    plf = CurveQuadratic(
        idf,
        **CurveQuadraticType(
            Name=f"{name}_HP_PLF",
            Coefficient1_Constant=0.85,
            Coefficient2_x=0.15,
            Coefficient3_x2=0.0,
            Minimum_Value_of_x=0.0,
            Maximum_Value_of_x=1.0
        )
    )
    # cf EN14511 (PAC chauffage)
    return CoilWaterheatingAirtowaterheatpumpPumped(
        idf,
        **CoilWaterheatingAirtowaterheatpumpPumpedType(
            Name=f"{name}_AirToWaterHP",
            Rated_Heating_Capacity=30000,
            Rated_Sensible_Heat_Ratio=1,
            Rated_COP=3.2,
            Rated_Evaporator_Air_Flow_Rate=EPValues.AUTOCALCULATE,
            Rated_Condenser_Water_Flow_Rate=EPValues.AUTOCALCULATE,
            Evaporator_Fan_Power_Included_in_Rated_COP=EPValues.YES,
            Fraction_of_Condenser_Pump_Heat_to_Water=1,
            Rated_Evaporator_Inlet_Air_DryBulb_Temperature=7,
            Rated_Evaporator_Inlet_Air_WetBulb_Temperature=6,
            Rated_Condenser_Inlet_Water_Temperature=35,
            Evaporator_Air_Inlet_Node_Name=input_air_node.Name,
            Evaporator_Air_Outlet_Node_Name=f"{name}_OutputOutdoorAirNode",
            Condenser_Water_Inlet_Node_Name=f"{name}_WaterInletNode",
            Condenser_Water_Outlet_Node_Name=f"{name}_WaterOutletNode",
            Heating_Capacity_Function_of_Temperature_Curve_Name=heating_capacity_curve.Name,
            Heating_COP_Function_of_Temperature_Curve_Name=cop_curve.Name,
            Part_Load_Fraction_Correlation_Curve_Name=plf.Name
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
