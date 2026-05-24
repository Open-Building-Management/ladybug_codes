"""Manage hvac equipments - secondary methods
around EMS
"""
from typing import Any

from eppy.bunch_subclass import EpBunch

from idfhub.hvac import (
    PLANT, INLET, OUTLET,
    EPValues,
    LoopNodes
)

from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import (
    EnergymanagementsystemSensor, EnergymanagementsystemSensorMeta,
    EnergymanagementsystemGlobalvariable,
    EnergymanagementsystemOutputvariable,
    OutputVariable,
    BoilerHotwater,
    EnergymanagementsystemActuator,
    EnergymanagementsystemProgram,
    EnergymanagementsystemProgramcallingmanager,
    EnergymanagementsystemMeteredoutputvariable,
    OutdoorairNode,
    CurveBiquadratic,
    CurveQuadratic,
    CoilWaterheatingAirtowaterheatpumpPumped,
    ScheduleCompact,
)

from idfhub.idf_autocomplete.v24_1_0.idf_types_short import (
    EnergymanagementsystemSensorType,
    EnergymanagementsystemGlobalvariableType,
    EnergymanagementsystemOutputvariableType,
    OutputVariableType,
    BoilerHotwaterType,
    EnergymanagementsystemActuatorType,
    EnergymanagementsystemProgramType,
    EnergymanagementsystemProgramcallingmanagerType,
    EnergymanagementsystemMeteredoutputvariableType,
    OutdoorairNodeType,
    CurveBiquadraticType,
    CurveQuadraticType,
    CoilWaterheatingAirtowaterheatpumpPumpedType,
    ScheduleCompactType,
)

from idfhub.common import idf, CONF
from .hvac24_1_0 import equipments


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
        self.name = name
        self.ems_instructions = []
        try:
            self.conf = CONF[name]
        except KeyError:
            self.conf = None

    def append(self, instruction):
        """add an instruction to the list"""
        self.ems_instructions.append(instruction)

    def generate(self, calling_point="InsideHVACSystemIterationLoop"):
        """generate the system program & the calling manager"""
        program = EnergymanagementsystemProgram(
            idf,
            **EnergymanagementsystemProgramType(
                Name=f"{self.name}_program"
            )
        )
        for i, instruction in enumerate(self.ems_instructions):
            program[f"Program_Line_{i+1}"] = instruction
        EnergymanagementsystemProgramcallingmanager(
            idf,
            **EnergymanagementsystemProgramcallingmanagerType(
                Name=f"{self.name}_control",
                EnergyPlus_Model_Calling_Point=calling_point,
                Program_Name_1=program.Name
            )
        )

    def discrete(
        self,
        *,
        command,
        sensor_name, value,
        actuator_name, low_value, high_value
    ):
        """discrete control
        command is a string like :
        start_above, stop_above, start_below, stop_below"""
        if "start" not in command and "stop" not in command:
            return
        if "below" in command:
            self.append(f"IF {sensor_name} < {value}")
        if "above" in command:
            self.append(f"IF {sensor_name} >= {value}")
        if "stop" in command:
            self.append(f"SET {actuator_name} = {low_value}")
        if "start" in command:
            self.append(f"SET {actuator_name} = {high_value}")
        self.append("ENDIF")

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
        """return the instructions array
        rubbish if using generate"""
        return self.ems_instructions

    def biquadratic_on_x_y(self, *, key, var_name):
        """add a biquadratic formula on ems variables x and y"""
        if not self.conf:
            return
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


def schedule_control(name: str, sensor_name: str, conf: dict[str, Any]):
    """control through availability schedule
    a sensor called sensor_name must prexist
    """
    actuator_name = f"{name}_availability"
    schedule_name = f"{name}_availability_schedule"
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
    ems_program = EmsProgram(name)
    lower_limit = conf.get("min", 0)
    upper_limit = conf.get("max", 1)
    for key in conf:
        # some keys may not be a program_code
        ems_program.discrete(
            command=key,
            sensor_name=sensor_name,
            value=conf[key],
            actuator_name=actuator_name,
            low_value=lower_limit,
            high_value=upper_limit
        )
    ems_program.generate()
    schedule_name = conf.get("type", "Pump_Flow_Rate_Schedule_Name").replace(" ", "_")
    equipments[name][schedule_name] = schedule.Name


def ems_control(machine_name: str, sensor_name: str, conf: dict[str, Any]):
    """control a machine through On/Off supervisory
    a sensor called sensor_name must prexist"""
    actuator_name = f"{machine_name}_actuator"

    EnergymanagementsystemActuator(
        idf,
        **EnergymanagementsystemActuatorType(
            Name=actuator_name,
            Actuated_Component_Unique_Name=equipments[machine_name].Name,
            Actuated_Component_Type=f"Plant Component {equipments[machine_name].key}",
            Actuated_Component_Control_Type=conf.get("type", "On/Off Supervisory")
        )
    )
    ems_program = EmsProgram(machine_name)
    for key in conf:
        ems_program.discrete(
            command=key,
            sensor_name=sensor_name,
            value=conf[key],
            actuator_name=actuator_name,
            low_value=conf.get("min", 0),
            high_value=conf.get("max", 1)
        )
    ems_program.generate()


def initialise_sensors(
    conf: dict[str, dict[str, str]]
) -> dict[str, EpBunch]:
    """initialise all sensors"""
    sensor_dict: dict[str, EpBunch] = {}
    for sensor_name, sensor_conf in conf.items():
        sensor_type = sensor_conf.get(
            "type",
            "System Node Temperature"
        )
        location_name = sensor_conf.get("location_name")
        if sensor_type == "Site Outdoor Air Drybulb Temperature":
            location_name = "Environment"
        if not location_name:
            location_name = LoopNodes(sensor_conf["loop"]).get(
                side=sensor_conf.get("side", "plant"),
                port=sensor_conf.get("port", "inlet")
            )
        sensor_object = create_sensor(
            sensor_name = sensor_name,
            sensor_type = sensor_type,
            location_name = location_name
        )
        sensor_dict[sensor_name] = sensor_object
        # add sensor to output for simple ctrl
        OutputVariable(
            idf,
            **OutputVariableType(
                Key_Value=location_name,
                Variable_Name=sensor_type,
                Reporting_Frequency="Timestep"
            )
        )
    return sensor_dict


def control(machine_name, sensor_name, conf: dict[str, Any]):
    """equipment control through sensor"""
    control_type = conf.get("type", "Pump_Flow_Rate_Schedule_Name")
    if "Schedule" in control_type:
        schedule_control(machine_name, sensor_name, conf)
        return
    ems_control(machine_name, sensor_name, conf)


def air_to_water_heatpump_ems(name):
    """simulate an air to water heatpump using EMS
    dont use
    """
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
