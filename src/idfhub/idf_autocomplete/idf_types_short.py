from __future__ import annotations
from typing import TypedDict, Literal

class AirconditionerVariablerefrigerantflowType(TypedDict, total=False):
    """"dict for AirconditionerVariablerefrigerantflow"""
    Heat_Pump_Name: str
    Availability_Schedule_Name: str
    Gross_Rated_Total_Cooling_Capacity: str
    Gross_Rated_Cooling_COP: str
    Minimum_Condenser_Inlet_Node_Temperature_in_Cooling_Mode: str
    Maximum_Condenser_Inlet_Node_Temperature_in_Cooling_Mode: str
    Cooling_Capacity_Ratio_Modifier_Function_of_Low_Temperature_Curve_Name: str
    Cooling_Capacity_Ratio_Boundary_Curve_Name: str
    Cooling_Capacity_Ratio_Modifier_Function_of_High_Temperature_Curve_Name: str
    Cooling_Energy_Input_Ratio_Modifier_Function_of_Low_Temperature_Curve_Name: str
    Cooling_Energy_Input_Ratio_Boundary_Curve_Name: str
    Cooling_Energy_Input_Ratio_Modifier_Function_of_High_Temperature_Curve_Name: str
    Cooling_Energy_Input_Ratio_Modifier_Function_of_Low_PartLoad_Ratio_Curve_Name: str
    Cooling_Energy_Input_Ratio_Modifier_Function_of_High_PartLoad_Ratio_Curve_Name: str
    Cooling_Combination_Ratio_Correction_Factor_Curve_Name: str
    Cooling_PartLoad_Fraction_Correlation_Curve_Name: str
    Gross_Rated_Heating_Capacity: str
    Rated_Heating_Capacity_Sizing_Ratio: str
    Gross_Rated_Heating_COP: str
    Minimum_Condenser_Inlet_Node_Temperature_in_Heating_Mode: str
    Maximum_Condenser_Inlet_Node_Temperature_in_Heating_Mode: str
    Heating_Capacity_Ratio_Modifier_Function_of_Low_Temperature_Curve_Name: str
    Heating_Capacity_Ratio_Boundary_Curve_Name: str
    Heating_Capacity_Ratio_Modifier_Function_of_High_Temperature_Curve_Name: str
    Heating_Energy_Input_Ratio_Modifier_Function_of_Low_Temperature_Curve_Name: str
    Heating_Energy_Input_Ratio_Boundary_Curve_Name: str
    Heating_Energy_Input_Ratio_Modifier_Function_of_High_Temperature_Curve_Name: str
    Heating_Performance_Curve_Outdoor_Temperature_Type: str
    Heating_Energy_Input_Ratio_Modifier_Function_of_Low_PartLoad_Ratio_Curve_Name: str
    Heating_Energy_Input_Ratio_Modifier_Function_of_High_PartLoad_Ratio_Curve_Name: str
    Heating_Combination_Ratio_Correction_Factor_Curve_Name: str
    Heating_PartLoad_Fraction_Correlation_Curve_Name: str
    Minimum_Heat_Pump_PartLoad_Ratio: str
    Zone_Name_for_Master_Thermostat_Location: str
    Master_Thermostat_Priority_Control_Type: str
    Thermostat_Priority_Schedule_Name: str
    Zone_Terminal_Unit_List_Name: str
    Heat_Pump_Waste_Heat_Recovery: str
    Equivalent_Piping_Length_used_for_Piping_Correction_Factor_in_Cooling_Mode: str
    Vertical_Height_used_for_Piping_Correction_Factor: str
    Piping_Correction_Factor_for_Length_in_Cooling_Mode_Curve_Name: str
    Piping_Correction_Factor_for_Height_in_Cooling_Mode_Coefficient: str
    Equivalent_Piping_Length_used_for_Piping_Correction_Factor_in_Heating_Mode: str
    Piping_Correction_Factor_for_Length_in_Heating_Mode_Curve_Name: str
    Piping_Correction_Factor_for_Height_in_Heating_Mode_Coefficient: str
    Crankcase_Heater_Power_per_Compressor: str
    Number_of_Compressors: str
    Ratio_of_Compressor_Size_to_Total_Compressor_Capacity: str
    Maximum_Outdoor_DryBulb_Temperature_for_Crankcase_Heater: str
    Defrost_Strategy: str
    Defrost_Control: str
    Defrost_Energy_Input_Ratio_Modifier_Function_of_Temperature_Curve_Name: str
    Defrost_Time_Period_Fraction: str
    Resistive_Defrost_Heater_Capacity: str
    Maximum_Outdoor_Drybulb_Temperature_for_Defrost_Operation: str
    Condenser_Type: str
    Condenser_Inlet_Node_Name: str
    Condenser_Outlet_Node_Name: str
    Water_Condenser_Volume_Flow_Rate: str
    Evaporative_Condenser_Effectiveness: str
    Evaporative_Condenser_Air_Flow_Rate: str
    Evaporative_Condenser_Pump_Rated_Power_Consumption: str
    Supply_Water_Storage_Tank_Name: str
    Basin_Heater_Capacity: str
    Basin_Heater_Setpoint_Temperature: str
    Basin_Heater_Operating_Schedule_Name: str
    Fuel_Type: str
    Minimum_Condenser_Inlet_Node_Temperature_in_Heat_Recovery_Mode: str
    Maximum_Condenser_Inlet_Node_Temperature_in_Heat_Recovery_Mode: str
    Heat_Recovery_Cooling_Capacity_Modifier_Curve_Name: str
    Initial_Heat_Recovery_Cooling_Capacity_Fraction: str
    Heat_Recovery_Cooling_Capacity_Time_Constant: str
    Heat_Recovery_Cooling_Energy_Modifier_Curve_Name: str
    Initial_Heat_Recovery_Cooling_Energy_Fraction: str
    Heat_Recovery_Cooling_Energy_Time_Constant: str
    Heat_Recovery_Heating_Capacity_Modifier_Curve_Name: str
    Initial_Heat_Recovery_Heating_Capacity_Fraction: str
    Heat_Recovery_Heating_Capacity_Time_Constant: str
    Heat_Recovery_Heating_Energy_Modifier_Curve_Name: str
    Initial_Heat_Recovery_Heating_Energy_Fraction: str
    Heat_Recovery_Heating_Energy_Time_Constant: str

class AirconditionerVariablerefrigerantflowFluidtemperaturecontrolType(TypedDict, total=False):
    """"dict for AirconditionerVariablerefrigerantflowFluidtemperaturecontrol"""
    Heat_Pump_Name: str
    Availability_Schedule_Name: str
    Zone_Terminal_Unit_List_Name: str
    Refrigerant_Type: str
    Rated_Evaporative_Capacity: str
    Rated_Compressor_Power_Per_Unit_of_Rated_Evaporative_Capacity: str
    Minimum_Outdoor_Air_Temperature_in_Cooling_Mode: str
    Maximum_Outdoor_Air_Temperature_in_Cooling_Mode: str
    Minimum_Outdoor_Air_Temperature_in_Heating_Mode: str
    Maximum_Outdoor_Air_Temperature_in_Heating_Mode: str
    Reference_Outdoor_Unit_Superheating: str
    Reference_Outdoor_Unit_Subcooling: str
    Refrigerant_Temperature_Control_Algorithm_for_Indoor_Unit: str
    Reference_Evaporating_Temperature_for_Indoor_Unit: str
    Reference_Condensing_Temperature_for_Indoor_Unit: str
    Variable_Evaporating_Temperature_Minimum_for_Indoor_Unit: str
    Variable_Evaporating_Temperature_Maximum_for_Indoor_Unit: str
    Variable_Condensing_Temperature_Minimum_for_Indoor_Unit: str
    Variable_Condensing_Temperature_Maximum_for_Indoor_Unit: str
    Outdoor_Unit_Fan_Power_Per_Unit_of_Rated_Evaporative_Capacity: str
    Outdoor_Unit_Fan_Flow_Rate_Per_Unit_of_Rated_Evaporative_Capacity: str
    Outdoor_Unit_Evaporating_Temperature_Function_of_Superheating_Curve_Name: str
    Outdoor_Unit_Condensing_Temperature_Function_of_Subcooling_Curve_Name: str
    Diameter_of_Main_Pipe_Connecting_Outdoor_Unit_to_the_First_Branch_Joint: str
    Length_of_Main_Pipe_Connecting_Outdoor_Unit_to_the_First_Branch_Joint: str
    Equivalent_Length_of_Main_Pipe_Connecting_Outdoor_Unit_to_the_First_Branch_Joint: str
    Height_Difference_Between_Outdoor_Unit_and_Indoor_Units: str
    Main_Pipe_Insulation_Thickness: str
    Main_Pipe_Insulation_Thermal_Conductivity: str
    Crankcase_Heater_Power_per_Compressor: str
    Number_of_Compressors: str
    Ratio_of_Compressor_Size_to_Total_Compressor_Capacity: str
    Maximum_Outdoor_DryBulb_Temperature_for_Crankcase_Heater: str
    Defrost_Strategy: str
    Defrost_Control: str
    Defrost_Energy_Input_Ratio_Modifier_Function_of_Temperature_Curve_Name: str
    Defrost_Time_Period_Fraction: str
    Resistive_Defrost_Heater_Capacity: str
    Maximum_Outdoor_Drybulb_Temperature_for_Defrost_Operation: str
    Compressor_maximum_delta_Pressure: str
    Number_of_Compressor_Loading_Index_Entries: str
    Compressor_Speed_at_Loading_Index_1: str
    Loading_Index_1_Evaporative_Capacity_Multiplier_Function_of_Temperature_Curve_Name: str
    Loading_Index_1_Compressor_Power_Multiplier_Function_of_Temperature_Curve_Name: str
    Compressor_Speed_at_Loading_Index_2: str
    Loading_Index_2_Evaporative_Capacity_Multiplier_Function_of_Temperature_Curve_Name: str
    Loading_Index_2_Compressor_Power_Multiplier_Function_of_Temperature_Curve_Name: str
    Compressor_Speed_at_Loading_Index_3: str
    Loading_Index_3_Evaporative_Capacity_Multiplier_Function_of_Temperature_Curve_Name: str
    Loading_Index_3_Compressor_Power_Multiplier_Function_of_Temperature_Curve_Name: str
    Compressor_Speed_at_Loading_Index_4: str
    Loading_Index_4_Evaporative_Capacity_Multiplier_Function_of_Temperature_Curve_Name: str
    Loading_Index_4_Compressor_Power_Multiplier_Function_of_Temperature_Curve_Name: str
    Compressor_Speed_at_Loading_Index_5: str
    Loading_Index_5_Evaporative_Capacity_Multiplier_Function_of_Temperature_Curve_Name: str
    Loading_Index_5_Compressor_Power_Multiplier_Function_of_Temperature_Curve_Name: str
    Compressor_Speed_at_Loading_Index_6: str
    Loading_Index_6_Evaporative_Capacity_Multiplier_Function_of_Temperature_Curve_Name: str
    Loading_Index_6_Compressor_Power_Multiplier_Function_of_Temperature_Curve_Name: str
    Compressor_Speed_at_Loading_Index_7: str
    Loading_Index_7_Evaporative_Capacity_Multiplier_Function_of_Temperature_Curve_Name: str
    Loading_Index_7_list: str
    Compressor_Speed_at_Loading_Index_8: str
    Loading_Index_8_Evaporative_Capacity_Multiplier_Function_of_Temperature_Curve_Name: str
    Loading_Index_8_Compressor_Power_Multiplier_Function_of_Temperature_Curve_Name: str
    Compressor_Speed_at_Loading_Index_9: str
    Loading_Index_9_Evaporative_Capacity_Multiplier_Function_of_Temperature_Curve_Name: str
    Loading_Index_9_Compressor_Power_Multiplier_Function_of_Temperature_Curve_Name: str

class AirconditionerVariablerefrigerantflowFluidtemperaturecontrolHrType(TypedDict, total=False):
    """"dict for AirconditionerVariablerefrigerantflowFluidtemperaturecontrolHr"""
    Name: str
    Availability_Schedule_Name: str
    Zone_Terminal_Unit_List_Name: str
    Refrigerant_Type: str
    Rated_Evaporative_Capacity: str
    Rated_Compressor_Power_Per_Unit_of_Rated_Evaporative_Capacity: str
    Minimum_Outdoor_Air_Temperature_in_Cooling_Only_Mode: str
    Maximum_Outdoor_Air_Temperature_in_Cooling_Only_Mode: str
    Minimum_Outdoor_Air_Temperature_in_Heating_Only_Mode: str
    Maximum_Outdoor_Air_Temperature_in_Heating_Only_Mode: str
    Minimum_Outdoor_Temperature_in_Heat_Recovery_Mode: str
    Maximum_Outdoor_Temperature_in_Heat_Recovery_Mode: str
    Refrigerant_Temperature_Control_Algorithm_for_Indoor_Unit: str
    Reference_Evaporating_Temperature_for_Indoor_Unit: str
    Reference_Condensing_Temperature_for_Indoor_Unit: str
    Variable_Evaporating_Temperature_Minimum_for_Indoor_Unit: str
    Variable_Evaporating_Temperature_Maximum_for_Indoor_Unit: str
    Variable_Condensing_Temperature_Minimum_for_Indoor_Unit: str
    Variable_Condensing_Temperature_Maximum_for_Indoor_Unit: str
    Outdoor_Unit_Evaporator_Reference_Superheating: str
    Outdoor_Unit_Condenser_Reference_Subcooling: str
    Outdoor_Unit_Evaporator_Rated_Bypass_Factor: str
    Outdoor_Unit_Condenser_Rated_Bypass_Factor: str
    Difference_between_Outdoor_Unit_Evaporating_Temperature_and_Outdoor_Air_Temperature_in_Heat_Recovery_Mode: str
    Outdoor_Unit_Heat_Exchanger_Capacity_Ratio: str
    Outdoor_Unit_Fan_Power_Per_Unit_of_Rated_Evaporative_Capacity: str
    Outdoor_Unit_Fan_Flow_Rate_Per_Unit_of_Rated_Evaporative_Capacity: str
    Outdoor_Unit_Evaporating_Temperature_Function_of_Superheating_Curve_Name: str
    Outdoor_Unit_Condensing_Temperature_Function_of_Subcooling_Curve_Name: str
    Diameter_of_Main_Pipe_for_Suction_Gas: str
    Diameter_of_Main_Pipe_for_Discharge_Gas: str
    Length_of_Main_Pipe_Connecting_Outdoor_Unit_to_the_First_Branch_Joint: str
    Equivalent_Length_of_Main_Pipe_Connecting_Outdoor_Unit_to_the_First_Branch_Joint: str
    Height_Difference_Between_Outdoor_Unit_and_Indoor_Units: str
    Main_Pipe_Insulation_Thickness: str
    Main_Pipe_Insulation_Thermal_Conductivity: str
    Crankcase_Heater_Power_per_Compressor: str
    Number_of_Compressors: str
    Ratio_of_Compressor_Size_to_Total_Compressor_Capacity: str
    Maximum_Outdoor_DryBulb_Temperature_for_Crankcase_Heater: str
    Defrost_Strategy: str
    Defrost_Control: str
    Defrost_Energy_Input_Ratio_Modifier_Function_of_Temperature_Curve_Name: str
    Defrost_Time_Period_Fraction: str
    Resistive_Defrost_Heater_Capacity: str
    Maximum_Outdoor_Drybulb_Temperature_for_Defrost_Operation: str
    Initial_Heat_Recovery_Cooling_Capacity_Fraction: str
    Heat_Recovery_Cooling_Capacity_Time_Constant: str
    Initial_Heat_Recovery_Cooling_Energy_Fraction: str
    Heat_Recovery_Cooling_Energy_Time_Constant: str
    Initial_Heat_Recovery_Heating_Capacity_Fraction: str
    Heat_Recovery_Heating_Capacity_Time_Constant: str
    Initial_Heat_Recovery_Heating_Energy_Fraction: str
    Heat_Recovery_Heating_Energy_Time_Constant: str
    Compressor_maximum_delta_Pressure: str
    Compressor_Inverter_Efficiency: str
    Compressor_Evaporative_Capacity_Correction_Factor: str
    Number_of_Compressor_Loading_Index_Entries: str
    Compressor_Speed_at_Loading_Index_1: str
    Loading_Index_1_Evaporative_Capacity_Multiplier_Function_of_Temperature_Curve_Name: str
    Loading_Index_1_Compressor_Power_Multiplier_Function_of_Temperature_Curve_Name: str
    Compressor_Speed_at_Loading_Index_2: str
    Loading_Index_2_Evaporative_Capacity_Multiplier_Function_of_Temperature_Curve_Name: str
    Loading_Index_2_Compressor_Power_Multiplier_Function_of_Temperature_Curve_Name: str
    Compressor_Speed_at_Loading_Index_3: str
    Loading_Index_3_Evaporative_Capacity_Multiplier_Function_of_Temperature_Curve_Name: str
    Loading_Index_3_Compressor_Power_Multiplier_Function_of_Temperature_Curve_Name: str
    Compressor_Speed_at_Loading_Index_4: str
    Loading_Index_4_Evaporative_Capacity_Multiplier_Function_of_Temperature_Curve_Name: str
    Loading_Index_4_Compressor_Power_Multiplier_Function_of_Temperature_Curve_Name: str
    Compressor_Speed_at_Loading_Index_5: str
    Loading_Index_5_Evaporative_Capacity_Multiplier_Function_of_Temperature_Curve_Name: str
    Loading_Index_5_Compressor_Power_Multiplier_Function_of_Temperature_Curve_Name: str
    Compressor_Speed_at_Loading_Index_6: str
    Loading_Index_6_Evaporative_Capacity_Multiplier_Function_of_Temperature_Curve_Name: str
    Loading_Index_6_Compressor_Power_Multiplier_Function_of_Temperature_Curve_Name: str
    Compressor_Speed_at_Loading_Index_7: str
    Loading_Index_7_Evaporative_Capacity_Multiplier_Function_of_Temperature_Curve_Name: str
    Loading_Index_7_list: str
    Compressor_Speed_at_Loading_Index_8: str
    Loading_Index_8_Evaporative_Capacity_Multiplier_Function_of_Temperature_Curve_Name: str
    Loading_Index_8_Compressor_Power_Multiplier_Function_of_Temperature_Curve_Name: str
    Compressor_Speed_at_Loading_Index_9: str
    Loading_Index_9_Evaporative_Capacity_Multiplier_Function_of_Temperature_Curve_Name: str
    Loading_Index_9_Compressor_Power_Multiplier_Function_of_Temperature_Curve_Name: str
    Compressor_Speed_at_Loading_Index_10: str
    Loading_Index_10_Evaporative_Capacity_Multiplier_Function_of_Temperature_Curve_Name: str
    Loading_Index_10_Compressor_Power_Multiplier_Function_of_Temperature_Curve_Name: str
    Compressor_Speed_at_Loading_Index_11: str
    Loading_Index_11_Evaporative_Capacity_Multiplier_Function_of_Temperature_Curve_Name: str
    Loading_Index_11_Compressor_Power_Multiplier_Function_of_Temperature_Curve_Name: str

class AirflownetworkDistributionComponentCoilType(TypedDict, total=False):
    """"dict for AirflownetworkDistributionComponentCoil"""
    Coil_Name: str
    Coil_Object_Type: str
    Air_Path_Length: str
    Air_Path_Hydraulic_Diameter: str

class AirflownetworkDistributionComponentConstantpressuredropType(TypedDict, total=False):
    """"dict for AirflownetworkDistributionComponentConstantpressuredrop"""
    Name: str
    Pressure_Difference_Across_the_Component: str

class AirflownetworkDistributionComponentDuctType(TypedDict, total=False):
    """"dict for AirflownetworkDistributionComponentDuct"""
    Name: str
    Duct_Length: str
    Hydraulic_Diameter: str
    Cross_Section_Area: str
    Surface_Roughness: str
    Coefficient_for_Local_Dynamic_Loss_Due_to_Fitting: str
    Heat_Transmittance_Coefficient_UFactor_for_Duct_Wall_Construction: str
    Overall_Moisture_Transmittance_Coefficient_from_Air_to_Air: str
    Outside_Convection_Coefficient: str
    Inside_Convection_Coefficient: str

class AirflownetworkDistributionComponentFanType(TypedDict, total=False):
    """"dict for AirflownetworkDistributionComponentFan"""
    Fan_Name: str
    Supply_Fan_Object_Type: str

class AirflownetworkDistributionComponentHeatexchangerType(TypedDict, total=False):
    """"dict for AirflownetworkDistributionComponentHeatexchanger"""
    HeatExchanger_Name: str
    HeatExchanger_Object_Type: str
    Air_Path_Length: str
    Air_Path_Hydraulic_Diameter: str

class AirflownetworkDistributionComponentLeakType(TypedDict, total=False):
    """"dict for AirflownetworkDistributionComponentLeak"""
    Name: str
    Air_Mass_Flow_Coefficient: str
    Air_Mass_Flow_Exponent: str

class AirflownetworkDistributionComponentLeakageratioType(TypedDict, total=False):
    """"dict for AirflownetworkDistributionComponentLeakageratio"""
    Name: str
    Effective_Leakage_Ratio: str
    Maximum_Flow_Rate: str
    Reference_Pressure_Difference: str
    Air_Mass_Flow_Exponent: str

class AirflownetworkDistributionComponentOutdoorairflowType(TypedDict, total=False):
    """"dict for AirflownetworkDistributionComponentOutdoorairflow"""
    Name: str
    Outdoor_Air_Mixer_Name: str
    Air_Mass_Flow_Coefficient_When_No_Outdoor_Air_Flow_at_Reference_Conditions: str
    Air_Mass_Flow_Exponent_When_No_Outdoor_Air_Flow: str
    Reference_Crack_Conditions: str

class AirflownetworkDistributionComponentReliefairflowType(TypedDict, total=False):
    """"dict for AirflownetworkDistributionComponentReliefairflow"""
    Name: str
    Outdoor_Air_Mixer_Name: str
    Air_Mass_Flow_Coefficient_When_No_Outdoor_Air_Flow_at_Reference_Conditions: str
    Air_Mass_Flow_Exponent_When_No_Outdoor_Air_Flow: str
    Reference_Crack_Conditions: str

class AirflownetworkDistributionComponentTerminalunitType(TypedDict, total=False):
    """"dict for AirflownetworkDistributionComponentTerminalunit"""
    Terminal_Unit_Name: str
    Terminal_Unit_Object_Type: str
    Air_Path_Length: str
    Air_Path_Hydraulic_Diameter: str

class AirflownetworkDistributionDuctsizingType(TypedDict, total=False):
    """"dict for AirflownetworkDistributionDuctsizing"""
    Name: str
    Duct_Sizing_Method: str
    Duct_Sizing_Factor: str
    Maximum_Airflow_Velocity: str
    Total_Pressure_Loss_Across_Supply_Trunk: str
    Total_Pressure_Loss_Across_Supply_Branch: str
    Total_Pressure_Loss_Across_Return_Trunk: str
    Total_Pressure_Loss_Across_Return_Branch: str

class AirflownetworkDistributionDuctviewfactorsType(TypedDict, total=False):
    """"dict for AirflownetworkDistributionDuctviewfactors"""
    Linkage_Name: str
    Duct_Surface_Exposure_Fraction: str
    Duct_Surface_Emittance: str
    Surface_1_Name: str
    Surface_1_View_Factor: str
    Surface_2_Name: str
    Surface_2_View_Factor: str
    Surface_3_Name: str
    Surface_3_View_Factor: str
    Surface_4_Name: str
    Surface_4_View_Factor: str
    Surface_5_Name: str
    Surface_5_View_Factor: str
    Surface_6_Name: str
    Surface_6_View_Factor: str
    Surface_7_Name: str
    Surface_7_View_Factor: str
    Surface_8_Name: str
    Surface_8_View_Factor: str
    Surface_9_Name: str
    Surface_9_View_Factor: str
    Surface_10_Name: str
    Surface_10_View_Factor: str
    Surface_11_Name: str
    Surface_11_View_Factor: str
    Surface_12_Name: str
    Surface_12_View_Factor: str
    Surface_13_Name: str
    Surface_13_View_Factor: str
    Surface_14_Name: str
    Surface_14_View_Factor: str
    Surface_15_Name: str
    Surface_15_View_Factor: str
    Surface_16_Name: str
    Surface_16_View_Factor: str
    Surface_17_Name: str
    Surface_17_View_Factor: str
    Surface_18_Name: str
    Surface_18_View_Factor: str
    Surface_19_Name: str
    Surface_19_View_Factor: str
    Surface_20_Name: str
    Surface_20_View_Factor: str

class AirflownetworkDistributionLinkageType(TypedDict, total=False):
    """"dict for AirflownetworkDistributionLinkage"""
    Name: str
    Node_1_Name: str
    Node_2_Name: str
    Component_Name: str
    Thermal_Zone_Name: str

class AirflownetworkDistributionNodeType(TypedDict, total=False):
    """"dict for AirflownetworkDistributionNode"""
    Name: str
    Component_Name_or_Node_Name: str
    Component_Object_Type_or_Node_Type: str
    Node_Height: str

class AirflownetworkIntrazoneLinkageType(TypedDict, total=False):
    """"dict for AirflownetworkIntrazoneLinkage"""
    Name: str
    Node_1_Name: str
    Node_2_Name: str
    Component_Name: str
    AirflowNetworkMultiZoneSurface_Name: str

class AirflownetworkIntrazoneNodeType(TypedDict, total=False):
    """"dict for AirflownetworkIntrazoneNode"""
    Name: str
    RoomAirNodeAirflowNetwork_Name: str
    Zone_Name: str
    Node_Height: str

class AirflownetworkMultizoneComponentDetailedopeningType(TypedDict, total=False):
    """"dict for AirflownetworkMultizoneComponentDetailedopening"""
    Name: str
    Air_Mass_Flow_Coefficient_When_Opening_is_Closed: str
    Air_Mass_Flow_Exponent_When_Opening_is_Closed: str
    Type_of_Rectangular_Large_Vertical_Opening_LVO: str
    Extra_Crack_Length_or_Height_of_Pivoting_Axis: str
    Number_of_Sets_of_Opening_Factor_Data: str
    Opening_Factor_1: str
    Discharge_Coefficient_for_Opening_Factor_1: str
    Width_Factor_for_Opening_Factor_1: str
    Height_Factor_for_Opening_Factor_1: str
    Start_Height_Factor_for_Opening_Factor_1: str
    Opening_Factor_2: str
    Discharge_Coefficient_for_Opening_Factor_2: str
    Width_Factor_for_Opening_Factor_2: str
    Height_Factor_for_Opening_Factor_2: str
    Start_Height_Factor_for_Opening_Factor_2: str
    Opening_Factor_3: str
    Discharge_Coefficient_for_Opening_Factor_3: str
    Width_Factor_for_Opening_Factor_3: str
    Height_Factor_for_Opening_Factor_3: str
    Start_Height_Factor_for_Opening_Factor_3: str
    Opening_Factor_4: str
    Discharge_Coefficient_for_Opening_Factor_4: str
    Width_Factor_for_Opening_Factor_4: str
    Height_Factor_for_Opening_Factor_4: str
    Start_Height_Factor_for_Opening_Factor_4: str

class AirflownetworkMultizoneComponentHorizontalopeningType(TypedDict, total=False):
    """"dict for AirflownetworkMultizoneComponentHorizontalopening"""
    Name: str
    Air_Mass_Flow_Coefficient_When_Opening_is_Closed: str
    Air_Mass_Flow_Exponent_When_Opening_is_Closed: str
    Sloping_Plane_Angle: str
    Discharge_Coefficient: str

class AirflownetworkMultizoneComponentSimpleopeningType(TypedDict, total=False):
    """"dict for AirflownetworkMultizoneComponentSimpleopening"""
    Name: str
    Air_Mass_Flow_Coefficient_When_Opening_is_Closed: str
    Air_Mass_Flow_Exponent_When_Opening_is_Closed: str
    Minimum_Density_Difference_for_TwoWay_Flow: str
    Discharge_Coefficient: str

class AirflownetworkMultizoneComponentZoneexhaustfanType(TypedDict, total=False):
    """"dict for AirflownetworkMultizoneComponentZoneexhaustfan"""
    Name: str
    Air_Mass_Flow_Coefficient_When_the_Zone_Exhaust_Fan_is_Off_at_Reference_Conditions: str
    Air_Mass_Flow_Exponent_When_the_Zone_Exhaust_Fan_is_Off: str
    Reference_Crack_Conditions: str

class AirflownetworkMultizoneExternalnodeType(TypedDict, total=False):
    """"dict for AirflownetworkMultizoneExternalnode"""
    Name: str
    External_Node_Height: str
    Wind_Pressure_Coefficient_Curve_Name: str
    Symmetric_Wind_Pressure_Coefficient_Curve: str
    Wind_Angle_Type: str

class AirflownetworkMultizoneReferencecrackconditionsType(TypedDict, total=False):
    """"dict for AirflownetworkMultizoneReferencecrackconditions"""
    Name: str
    Reference_Temperature: str
    Reference_Barometric_Pressure: str
    Reference_Humidity_Ratio: str

class AirflownetworkMultizoneSpecifiedflowrateType(TypedDict, total=False):
    """"dict for AirflownetworkMultizoneSpecifiedflowrate"""
    Name: str
    Air_Flow_Value: str
    Air_Flow_Units: str

class AirflownetworkMultizoneSurfaceType(TypedDict, total=False):
    """"dict for AirflownetworkMultizoneSurface"""
    Surface_Name: str
    Leakage_Component_Name: str
    External_Node_Name: str
    WindowDoor_Opening_Factor_or_Crack_Factor: str
    Ventilation_Control_Mode: str
    Ventilation_Control_Zone_Temperature_Setpoint_Schedule_Name: str
    Minimum_Venting_Open_Factor: str
    Indoor_and_Outdoor_Temperature_Difference_Lower_Limit_For_Maximum_Venting_Open_Factor: str
    Indoor_and_Outdoor_Temperature_Difference_Upper_Limit_for_Minimum_Venting_Open_Factor: str
    Indoor_and_Outdoor_Enthalpy_Difference_Lower_Limit_For_Maximum_Venting_Open_Factor: str
    Indoor_and_Outdoor_Enthalpy_Difference_Upper_Limit_for_Minimum_Venting_Open_Factor: str
    Venting_Availability_Schedule_Name: str
    Occupant_Ventilation_Control_Name: str
    Equivalent_Rectangle_Method: str
    Equivalent_Rectangle_Aspect_Ratio: str

class AirflownetworkMultizoneSurfaceCrackType(TypedDict, total=False):
    """"dict for AirflownetworkMultizoneSurfaceCrack"""
    Name: str
    Air_Mass_Flow_Coefficient_at_Reference_Conditions: str
    Air_Mass_Flow_Exponent: str
    Reference_Crack_Conditions: str

class AirflownetworkMultizoneSurfaceEffectiveleakageareaType(TypedDict, total=False):
    """"dict for AirflownetworkMultizoneSurfaceEffectiveleakagearea"""
    Name: str
    Effective_Leakage_Area: str
    Discharge_Coefficient: str
    Reference_Pressure_Difference: str
    Air_Mass_Flow_Exponent: str

class AirflownetworkMultizoneWindpressurecoefficientarrayType(TypedDict, total=False):
    """"dict for AirflownetworkMultizoneWindpressurecoefficientarray"""
    Name: str
    Wind_Direction_1: str
    Wind_Direction_2: str
    Wind_Direction_3: str
    Wind_Direction_4: str
    Wind_Direction_5: str
    Wind_Direction_6: str
    Wind_Direction_7: str
    Wind_Direction_8: str
    Wind_Direction_9: str
    Wind_Direction_10: str
    Wind_Direction_11: str
    Wind_Direction_12: str
    Wind_Direction_13: str
    Wind_Direction_14: str
    Wind_Direction_15: str
    Wind_Direction_16: str
    Wind_Direction_17: str
    Wind_Direction_18: str
    Wind_Direction_19: str
    Wind_Direction_20: str
    Wind_Direction_21: str
    Wind_Direction_22: str
    Wind_Direction_23: str
    Wind_Direction_24: str
    Wind_Direction_25: str
    Wind_Direction_26: str
    Wind_Direction_27: str
    Wind_Direction_28: str
    Wind_Direction_29: str
    Wind_Direction_30: str
    Wind_Direction_31: str
    Wind_Direction_32: str
    Wind_Direction_33: str
    Wind_Direction_34: str
    Wind_Direction_35: str
    Wind_Direction_36: str

class AirflownetworkMultizoneWindpressurecoefficientvaluesType(TypedDict, total=False):
    """"dict for AirflownetworkMultizoneWindpressurecoefficientvalues"""
    Name: str
    AirflowNetworkMultiZoneWindPressureCoefficientArray_Name: str
    Wind_Pressure_Coefficient_Value_1: str
    Wind_Pressure_Coefficient_Value_2: str
    Wind_Pressure_Coefficient_Value_3: str
    Wind_Pressure_Coefficient_Value_4: str
    Wind_Pressure_Coefficient_Value_5: str
    Wind_Pressure_Coefficient_Value_6: str
    Wind_Pressure_Coefficient_Value_7: str
    Wind_Pressure_Coefficient_Value_8: str
    Wind_Pressure_Coefficient_Value_9: str
    Wind_Pressure_Coefficient_Value_10: str
    Wind_Pressure_Coefficient_Value_11: str
    Wind_Pressure_Coefficient_Value_12: str
    Wind_Pressure_Coefficient_Value_13: str
    Wind_Pressure_Coefficient_Value_14: str
    Wind_Pressure_Coefficient_Value_15: str
    Wind_Pressure_Coefficient_Value_16: str
    Wind_Pressure_Coefficient_Value_17: str
    Wind_Pressure_Coefficient_Value_18: str
    Wind_Pressure_Coefficient_Value_19: str
    Wind_Pressure_Coefficient_Value_20: str
    Wind_Pressure_Coefficient_Value_21: str
    Wind_Pressure_Coefficient_Value_22: str
    Wind_Pressure_Coefficient_Value_23: str
    Wind_Pressure_Coefficient_Value_24: str
    Wind_Pressure_Coefficient_Value_25: str
    Wind_Pressure_Coefficient_Value_26: str
    Wind_Pressure_Coefficient_Value_27: str
    Wind_Pressure_Coefficient_Value_28: str
    Wind_Pressure_Coefficient_Value_29: str
    Wind_Pressure_Coefficient_Value_30: str
    Wind_Pressure_Coefficient_Value_31: str
    Wind_Pressure_Coefficient_Value_32: str
    Wind_Pressure_Coefficient_Value_33: str
    Wind_Pressure_Coefficient_Value_34: str
    Wind_Pressure_Coefficient_Value_35: str
    Wind_Pressure_Coefficient_Value_36: str

class AirflownetworkMultizoneZoneType(TypedDict, total=False):
    """"dict for AirflownetworkMultizoneZone"""
    Zone_Name: str
    Ventilation_Control_Mode: str
    Ventilation_Control_Zone_Temperature_Setpoint_Schedule_Name: str
    Minimum_Venting_Open_Factor: str
    Indoor_and_Outdoor_Temperature_Difference_Lower_Limit_For_Maximum_Venting_Open_Factor: str
    Indoor_and_Outdoor_Temperature_Difference_Upper_Limit_for_Minimum_Venting_Open_Factor: str
    Indoor_and_Outdoor_Enthalpy_Difference_Lower_Limit_For_Maximum_Venting_Open_Factor: str
    Indoor_and_Outdoor_Enthalpy_Difference_Upper_Limit_for_Minimum_Venting_Open_Factor: str
    Venting_Availability_Schedule_Name: str
    Single_Sided_Wind_Pressure_Coefficient_Algorithm: str
    Facade_Width: str
    Occupant_Ventilation_Control_Name: str

class AirflownetworkOccupantventilationcontrolType(TypedDict, total=False):
    """"dict for AirflownetworkOccupantventilationcontrol"""
    Name: str
    Minimum_Opening_Time: str
    Minimum_Closing_Time: str
    Thermal_Comfort_Low_Temperature_Curve_Name: str
    Thermal_Comfort_Temperature_Boundary_Point: str
    Thermal_Comfort_High_Temperature_Curve_Name: str
    Maximum_Threshold_for_Persons_Dissatisfied_PPD: str
    Occupancy_Check: str
    Opening_Probability_Schedule_Name: str
    Closing_Probability_Schedule_Name: str

class AirflownetworkSimulationcontrolType(TypedDict, total=False):
    """"dict for AirflownetworkSimulationcontrol"""
    Name: str
    AirflowNetwork_Control: str
    Wind_Pressure_Coefficient_Type: str
    Height_Selection_for_Local_Wind_Pressure_Calculation: str
    Building_Type: str
    Maximum_Number_of_Iterations: str
    Initialization_Type: str
    Relative_Airflow_Convergence_Tolerance: str
    Absolute_Airflow_Convergence_Tolerance: str
    Convergence_Acceleration_Limit: str
    Azimuth_Angle_of_Long_Axis_of_Building: str
    Ratio_of_Building_Width_Along_Short_Axis_to_Width_Along_Long_Axis: str
    Height_Dependence_of_External_Node_Temperature: str
    Solver: str
    Allow_Unsupported_Zone_Equipment: str
    Do_Distribution_Duct_Sizing_Calculation: str

class AirflownetworkZonecontrolPressurecontrollerType(TypedDict, total=False):
    """"dict for AirflownetworkZonecontrolPressurecontroller"""
    Name: str
    Control_Zone_Name: str
    Control_Object_Type: str
    Control_Object_Name: str
    Pressure_Control_Availability_Schedule_Name: str
    Pressure_Setpoint_Schedule_Name: str

class AirloophvacType(TypedDict, total=False):
    """"dict for Airloophvac"""
    Name: str
    Controller_List_Name: str
    Availability_Manager_List_Name: str
    Design_Supply_Air_Flow_Rate: str
    Branch_List_Name: str
    Connector_List_Name: str
    Supply_Side_Inlet_Node_Name: str
    Demand_Side_Outlet_Node_Name: str
    Demand_Side_Inlet_Node_Names: str
    Supply_Side_Outlet_Node_Names: str
    Design_Return_Air_Flow_Fraction_of_Supply_Air_Flow: str

class AirloophvacControllerlistType(TypedDict, total=False):
    """"dict for AirloophvacControllerlist"""
    Name: str
    Controller_1_Object_Type: str
    Controller_1_Name: str
    Controller_2_Object_Type: str
    Controller_2_Name: str
    Controller_3_Object_Type: str
    Controller_3_Name: str
    Controller_4_Object_Type: str
    Controller_4_Name: str
    Controller_5_Object_Type: str
    Controller_5_Name: str
    Controller_6_Object_Type: str
    Controller_6_Name: str
    Controller_7_Object_Type: str
    Controller_7_Name: str
    Controller_8_Object_Type: str
    Controller_8_Name: str

class AirloophvacDedicatedoutdoorairsystemType(TypedDict, total=False):
    """"dict for AirloophvacDedicatedoutdoorairsystem"""
    Name: str
    AirLoopHVACOutdoorAirSystem_Name: str
    Availability_Schedule_Name: str
    AirLoopHVACMixer_Name: str
    AirLoopHVACSplitter_Name: str
    Preheat_Design_Temperature: str
    Preheat_Design_Humidity_Ratio: str
    Precool_Design_Temperature: str
    Precool_Design_Humidity_Ratio: str
    Number_of_AirLoopHVAC: str
    AirLoopHVAC_1_Name: str
    AirLoopHVAC_2_Name: str
    AirLoopHVAC_3_Name: str
    AirLoopHVAC_4_Name: str
    AirLoopHVAC_5_Name: str
    AirLoopHVAC_6_Name: str
    AirLoopHVAC_7_Name: str
    AirLoopHVAC_8_Name: str
    AirLoopHVAC_9_Name: str
    AirLoopHVAC_10_Name: str
    AirLoopHVAC_11_Name: str
    AirLoopHVAC_12_Name: str
    AirLoopHVAC_13_Name: str
    AirLoopHVAC_14_Name: str
    AirLoopHVAC_15_Name: str
    AirLoopHVAC_16_Name: str
    AirLoopHVAC_17_Name: str
    AirLoopHVAC_18_Name: str
    AirLoopHVAC_19_Name: str
    AirLoopHVAC_20_Name: str

class AirloophvacExhaustsystemType(TypedDict, total=False):
    """"dict for AirloophvacExhaustsystem"""
    Name: str
    Zone_Mixer_Name: str
    Fan_Object_Type: str
    Fan_Name: str

class AirloophvacMixerType(TypedDict, total=False):
    """"dict for AirloophvacMixer"""
    Name: str
    Outlet_Node_Name: str
    Inlet_1_Node_Name: str
    Inlet_2_Node_Name: str
    Inlet_3_Node_Name: str
    Inlet_4_Node_Name: str
    Inlet_5_Node_Name: str
    Inlet_6_Node_Name: str
    Inlet_7_Node_Name: str
    Inlet_8_Node_Name: str
    Inlet_9_Node_Name: str
    Inlet_10_Node_Name: str
    Inlet_11_Node_Name: str
    Inlet_12_Node_Name: str
    Inlet_13_Node_Name: str
    Inlet_14_Node_Name: str
    Inlet_15_Node_Name: str
    Inlet_16_Node_Name: str
    Inlet_17_Node_Name: str
    Inlet_18_Node_Name: str
    Inlet_19_Node_Name: str
    Inlet_20_Node_Name: str
    Inlet_21_Node_Name: str
    Inlet_22_Node_Name: str
    Inlet_23_Node_Name: str
    Inlet_24_Node_Name: str
    Inlet_25_Node_Name: str
    Inlet_26_Node_Name: str
    Inlet_27_Node_Name: str
    Inlet_28_Node_Name: str
    Inlet_29_Node_Name: str
    Inlet_30_Node_Name: str
    Inlet_31_Node_Name: str
    Inlet_32_Node_Name: str
    Inlet_33_Node_Name: str
    Inlet_34_Node_Name: str
    Inlet_35_Node_Name: str
    Inlet_36_Node_Name: str
    Inlet_37_Node_Name: str
    Inlet_38_Node_Name: str
    Inlet_39_Node_Name: str
    Inlet_40_Node_Name: str
    Inlet_41_Node_Name: str
    Inlet_42_Node_Name: str
    Inlet_43_Node_Name: str
    Inlet_44_Node_Name: str
    Inlet_45_Node_Name: str
    Inlet_46_Node_Name: str
    Inlet_47_Node_Name: str
    Inlet_48_Node_Name: str
    Inlet_49_Node_Name: str

class AirloophvacOutdoorairsystemType(TypedDict, total=False):
    """"dict for AirloophvacOutdoorairsystem"""
    Name: str
    Controller_List_Name: str
    Outdoor_Air_Equipment_List_Name: str

class AirloophvacOutdoorairsystemEquipmentlistType(TypedDict, total=False):
    """"dict for AirloophvacOutdoorairsystemEquipmentlist"""
    Name: str
    Component_1_Object_Type: str
    Component_1_Name: str
    Component_2_Object_Type: str
    Component_2_Name: str
    Component_3_Object_Type: str
    Component_3_Name: str
    Component_4_Object_Type: str
    Component_4_Name: str
    Component_5_Object_Type: str
    Component_5_Name: str
    Component_6_Object_Type: str
    Component_6_Name: str
    Component_7_Object_Type: str
    Component_7_Name: str
    Component_8_Object_Type: str
    Component_8_Name: str
    Component_9_Object_Type: str
    Component_9_Name: str

class AirloophvacReturnpathType(TypedDict, total=False):
    """"dict for AirloophvacReturnpath"""
    Name: str
    Return_Air_Path_Outlet_Node_Name: str
    Component_1_Object_Type: str
    Component_1_Name: str
    Component_2_Object_Type: str
    Component_2_Name: str
    Component_3_Object_Type: str
    Component_3_Name: str
    Component_4_Object_Type: str
    Component_4_Name: str
    Component_5_Object_Type: str
    Component_5_Name: str
    Component_6_Object_Type: str
    Component_6_Name: str
    Component_7_Object_Type: str
    Component_7_Name: str
    Component_8_Object_Type: str
    Component_8_Name: str
    Component_9_Object_Type: str
    Component_9_Name: str
    Component_10_Object_Type: str
    Component_10_Name: str
    Component_11_Object_Type: str
    Component_11_Name: str
    Component_12_Object_Type: str
    Component_12_Name: str
    Component_13_Object_Type: str
    Component_13_Name: str
    Component_14_Object_Type: str
    Component_14_Name: str
    Component_15_Object_Type: str
    Component_15_Name: str
    Component_16_Object_Type: str
    Component_16_Name: str
    Component_17_Object_Type: str
    Component_17_Name: str
    Component_18_Object_Type: str
    Component_18_Name: str
    Component_19_Object_Type: str
    Component_19_Name: str
    Component_20_Object_Type: str
    Component_20_Name: str
    Component_21_Object_Type: str
    Component_21_Name: str
    Component_22_Object_Type: str
    Component_22_Name: str
    Component_23_Object_Type: str
    Component_23_Name: str
    Component_24_Object_Type: str
    Component_24_Name: str
    Component_25_Object_Type: str
    Component_25_Name: str

class AirloophvacReturnplenumType(TypedDict, total=False):
    """"dict for AirloophvacReturnplenum"""
    Name: str
    Zone_Name: str
    Zone_Node_Name: str
    Outlet_Node_Name: str
    Induced_Air_Outlet_Node_or_NodeList_Name: str
    Inlet_1_Node_Name: str
    Inlet_2_Node_Name: str
    Inlet_3_Node_Name: str
    Inlet_4_Node_Name: str
    Inlet_5_Node_Name: str
    Inlet_6_Node_Name: str
    Inlet_7_Node_Name: str
    Inlet_8_Node_Name: str
    Inlet_9_Node_Name: str
    Inlet_10_Node_Name: str
    Inlet_11_Node_Name: str
    Inlet_12_Node_Name: str
    Inlet_13_Node_Name: str
    Inlet_14_Node_Name: str
    Inlet_15_Node_Name: str
    Inlet_16_Node_Name: str
    Inlet_17_Node_Name: str
    Inlet_18_Node_Name: str
    Inlet_19_Node_Name: str
    Inlet_20_Node_Name: str
    Inlet_21_Node_Name: str
    Inlet_22_Node_Name: str
    Inlet_23_Node_Name: str
    Inlet_24_Node_Name: str
    Inlet_25_Node_Name: str
    Inlet_26_Node_Name: str
    Inlet_27_Node_Name: str
    Inlet_28_Node_Name: str
    Inlet_29_Node_Name: str
    Inlet_30_Node_Name: str
    Inlet_31_Node_Name: str
    Inlet_32_Node_Name: str
    Inlet_33_Node_Name: str
    Inlet_34_Node_Name: str
    Inlet_35_Node_Name: str
    Inlet_36_Node_Name: str
    Inlet_37_Node_Name: str
    Inlet_38_Node_Name: str
    Inlet_39_Node_Name: str
    Inlet_40_Node_Name: str
    Inlet_41_Node_Name: str
    Inlet_42_Node_Name: str
    Inlet_43_Node_Name: str
    Inlet_44_Node_Name: str
    Inlet_45_Node_Name: str
    Inlet_46_Node_Name: str
    Inlet_47_Node_Name: str
    Inlet_48_Node_Name: str
    Inlet_49_Node_Name: str

class AirloophvacSplitterType(TypedDict, total=False):
    """"dict for AirloophvacSplitter"""
    Name: str
    Inlet_Node_Name: str
    Outlet_1_Node_Name: str
    Outlet_2_Node_Name: str
    Outlet_3_Node_Name: str
    Outlet_4_Node_Name: str
    Outlet_5_Node_Name: str
    Outlet_6_Node_Name: str
    Outlet_7_Node_Name: str
    Outlet_8_Node_Name: str
    Outlet_9_Node_Name: str
    Outlet_10_Node_Name: str
    Outlet_11_Node_Name: str
    Outlet_12_Node_Name: str
    Outlet_13_Node_Name: str
    Outlet_14_Node_Name: str
    Outlet_15_Node_Name: str
    Outlet_16_Node_Name: str
    Outlet_17_Node_Name: str
    Outlet_18_Node_Name: str
    Outlet_19_Node_Name: str
    Outlet_20_Node_Name: str
    Outlet_21_Node_Name: str
    Outlet_22_Node_Name: str
    Outlet_23_Node_Name: str
    Outlet_24_Node_Name: str
    Outlet_25_Node_Name: str
    Outlet_26_Node_Name: str
    Outlet_27_Node_Name: str
    Outlet_28_Node_Name: str
    Outlet_29_Node_Name: str
    Outlet_30_Node_Name: str
    Outlet_31_Node_Name: str
    Outlet_32_Node_Name: str
    Outlet_33_Node_Name: str
    Outlet_34_Node_Name: str
    Outlet_35_Node_Name: str
    Outlet_36_Node_Name: str
    Outlet_37_Node_Name: str
    Outlet_38_Node_Name: str
    Outlet_39_Node_Name: str
    Outlet_40_Node_Name: str
    Outlet_41_Node_Name: str
    Outlet_42_Node_Name: str
    Outlet_43_Node_Name: str
    Outlet_44_Node_Name: str
    Outlet_45_Node_Name: str
    Outlet_46_Node_Name: str
    Outlet_47_Node_Name: str
    Outlet_48_Node_Name: str
    Outlet_49_Node_Name: str

class AirloophvacSupplypathType(TypedDict, total=False):
    """"dict for AirloophvacSupplypath"""
    Name: str
    Supply_Air_Path_Inlet_Node_Name: str
    Component_1_Object_Type: str
    Component_1_Name: str
    Component_2_Object_Type: str
    Component_2_Name: str
    Component_3_Object_Type: str
    Component_3_Name: str
    Component_4_Object_Type: str
    Component_4_Name: str
    Component_5_Object_Type: str
    Component_5_Name: str
    Component_6_Object_Type: str
    Component_6_Name: str
    Component_7_Object_Type: str
    Component_7_Name: str
    Component_8_Object_Type: str
    Component_8_Name: str
    Component_9_Object_Type: str
    Component_9_Name: str
    Component_10_Object_Type: str
    Component_10_Name: str
    Component_11_Object_Type: str
    Component_11_Name: str
    Component_12_Object_Type: str
    Component_12_Name: str
    Component_13_Object_Type: str
    Component_13_Name: str
    Component_14_Object_Type: str
    Component_14_Name: str
    Component_15_Object_Type: str
    Component_15_Name: str
    Component_16_Object_Type: str
    Component_16_Name: str
    Component_17_Object_Type: str
    Component_17_Name: str
    Component_18_Object_Type: str
    Component_18_Name: str
    Component_19_Object_Type: str
    Component_19_Name: str
    Component_20_Object_Type: str
    Component_20_Name: str
    Component_21_Object_Type: str
    Component_21_Name: str
    Component_22_Object_Type: str
    Component_22_Name: str
    Component_23_Object_Type: str
    Component_23_Name: str
    Component_24_Object_Type: str
    Component_24_Name: str
    Component_25_Object_Type: str
    Component_25_Name: str

class AirloophvacSupplyplenumType(TypedDict, total=False):
    """"dict for AirloophvacSupplyplenum"""
    Name: str
    Zone_Name: str
    Zone_Node_Name: str
    Inlet_Node_Name: str
    Outlet_1_Node_Name: str
    Outlet_2_Node_Name: str
    Outlet_3_Node_Name: str
    Outlet_4_Node_Name: str
    Outlet_5_Node_Name: str
    Outlet_6_Node_Name: str
    Outlet_7_Node_Name: str
    Outlet_8_Node_Name: str
    Outlet_9_Node_Name: str
    Outlet_10_Node_Name: str
    Outlet_11_Node_Name: str
    Outlet_12_Node_Name: str
    Outlet_13_Node_Name: str
    Outlet_14_Node_Name: str
    Outlet_15_Node_Name: str
    Outlet_16_Node_Name: str
    Outlet_17_Node_Name: str
    Outlet_18_Node_Name: str
    Outlet_19_Node_Name: str
    Outlet_20_Node_Name: str
    Outlet_21_Node_Name: str
    Outlet_22_Node_Name: str
    Outlet_23_Node_Name: str
    Outlet_24_Node_Name: str
    Outlet_25_Node_Name: str
    Outlet_26_Node_Name: str
    Outlet_27_Node_Name: str
    Outlet_28_Node_Name: str
    Outlet_29_Node_Name: str
    Outlet_30_Node_Name: str
    Outlet_31_Node_Name: str
    Outlet_32_Node_Name: str
    Outlet_33_Node_Name: str
    Outlet_34_Node_Name: str
    Outlet_35_Node_Name: str
    Outlet_36_Node_Name: str
    Outlet_37_Node_Name: str
    Outlet_38_Node_Name: str
    Outlet_39_Node_Name: str
    Outlet_40_Node_Name: str
    Outlet_41_Node_Name: str
    Outlet_42_Node_Name: str
    Outlet_43_Node_Name: str
    Outlet_44_Node_Name: str
    Outlet_45_Node_Name: str
    Outlet_46_Node_Name: str
    Outlet_47_Node_Name: str
    Outlet_48_Node_Name: str
    Outlet_49_Node_Name: str

class AirloophvacUnitaryFurnaceHeatcoolType(TypedDict, total=False):
    """"dict for AirloophvacUnitaryFurnaceHeatcool"""
    Name: str
    Availability_Schedule_Name: str
    Furnace_Air_Inlet_Node_Name: str
    Furnace_Air_Outlet_Node_Name: str
    Supply_Air_Fan_Operating_Mode_Schedule_Name: str
    Maximum_Supply_Air_Temperature: str
    Cooling_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate: str
    No_Load_Supply_Air_Flow_Rate: str
    Controlling_Zone_or_Thermostat_Location: str
    Supply_Fan_Object_Type: str
    Supply_Fan_Name: str
    Fan_Placement: str
    Heating_Coil_Object_Type: str
    Heating_Coil_Name: str
    Cooling_Coil_Object_Type: str
    Cooling_Coil_Name: str
    Dehumidification_Control_Type: str
    Reheat_Coil_Object_Type: str
    Reheat_Coil_Name: str

class AirloophvacUnitaryFurnaceHeatonlyType(TypedDict, total=False):
    """"dict for AirloophvacUnitaryFurnaceHeatonly"""
    Name: str
    Availability_Schedule_Name: str
    Furnace_Air_Inlet_Node_Name: str
    Furnace_Air_Outlet_Node_Name: str
    Supply_Air_Fan_Operating_Mode_Schedule_Name: str
    Maximum_Supply_Air_Temperature: str
    Heating_Supply_Air_Flow_Rate: str
    Controlling_Zone_or_Thermostat_Location: str
    Supply_Fan_Object_Type: str
    Supply_Fan_Name: str
    Fan_Placement: str
    Heating_Coil_Object_Type: str
    Heating_Coil_Name: str

class AirloophvacUnitaryheatcoolType(TypedDict, total=False):
    """"dict for AirloophvacUnitaryheatcool"""
    Name: str
    Availability_Schedule_Name: str
    Unitary_System_Air_Inlet_Node_Name: str
    Unitary_System_Air_Outlet_Node_Name: str
    Supply_Air_Fan_Operating_Mode_Schedule_Name: str
    Maximum_Supply_Air_Temperature: str
    Cooling_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate: str
    No_Load_Supply_Air_Flow_Rate: str
    Controlling_Zone_or_Thermostat_Location: str
    Supply_Fan_Object_Type: str
    Supply_Fan_Name: str
    Fan_Placement: str
    Heating_Coil_Object_Type: str
    Heating_Coil_Name: str
    Cooling_Coil_Object_Type: str
    Cooling_Coil_Name: str
    Dehumidification_Control_Type: str
    Reheat_Coil_Object_Type: str
    Reheat_Coil_Name: str

class AirloophvacUnitaryheatcoolVavchangeoverbypassType(TypedDict, total=False):
    """"dict for AirloophvacUnitaryheatcoolVavchangeoverbypass"""
    Name: str
    Availability_Schedule_Name: str
    Cooling_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate: str
    No_Load_Supply_Air_Flow_Rate: str
    Cooling_Outdoor_Air_Flow_Rate: str
    Heating_Outdoor_Air_Flow_Rate: str
    No_Load_Outdoor_Air_Flow_Rate: str
    Outdoor_Air_Flow_Rate_Multiplier_Schedule_Name: str
    Air_Inlet_Node_Name: str
    Bypass_Duct_Mixer_Node_Name: str
    Bypass_Duct_Splitter_Node_Name: str
    Air_Outlet_Node_Name: str
    Outdoor_Air_Mixer_Object_Type: str
    Outdoor_Air_Mixer_Name: str
    Supply_Air_Fan_Object_Type: str
    Supply_Air_Fan_Name: str
    Supply_Air_Fan_Placement: str
    Supply_Air_Fan_Operating_Mode_Schedule_Name: str
    Cooling_Coil_Object_Type: str
    Cooling_Coil_Name: str
    Heating_Coil_Object_Type: str
    Heating_Coil_Name: str
    Priority_Control_Mode: str
    Minimum_Outlet_Air_Temperature_During_Cooling_Operation: str
    Maximum_Outlet_Air_Temperature_During_Heating_Operation: str
    Dehumidification_Control_Type: str
    Plenum_or_Mixer_Inlet_Node_Name: str
    Minimum_Runtime_Before_Operating_Mode_Change: str

class AirloophvacUnitaryheatonlyType(TypedDict, total=False):
    """"dict for AirloophvacUnitaryheatonly"""
    Name: str
    Availability_Schedule_Name: str
    Unitary_System_Air_Inlet_Node_Name: str
    Unitary_System_Air_Outlet_Node_Name: str
    Supply_Air_Fan_Operating_Mode_Schedule_Name: str
    Maximum_Supply_Air_Temperature: str
    Heating_Supply_Air_Flow_Rate: str
    Controlling_Zone_or_Thermostat_Location: str
    Supply_Fan_Object_Type: str
    Supply_Fan_Name: str
    Fan_Placement: str
    Heating_Coil_Object_Type: str
    Heating_Coil_Name: str

class AirloophvacUnitaryheatpumpAirtoairType(TypedDict, total=False):
    """"dict for AirloophvacUnitaryheatpumpAirtoair"""
    Name: str
    Availability_Schedule_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Cooling_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate: str
    No_Load_Supply_Air_Flow_Rate: str
    Controlling_Zone_or_Thermostat_Location: str
    Supply_Air_Fan_Object_Type: str
    Supply_Air_Fan_Name: str
    Heating_Coil_Object_Type: str
    Heating_Coil_Name: str
    Cooling_Coil_Object_Type: str
    Cooling_Coil_Name: str
    Supplemental_Heating_Coil_Object_Type: str
    Supplemental_Heating_Coil_Name: str
    Maximum_Supply_Air_Temperature_from_Supplemental_Heater: str
    Maximum_Outdoor_DryBulb_Temperature_for_Supplemental_Heater_Operation: str
    Fan_Placement: str
    Supply_Air_Fan_Operating_Mode_Schedule_Name: str
    Dehumidification_Control_Type: str

class AirloophvacUnitaryheatpumpAirtoairMultispeedType(TypedDict, total=False):
    """"dict for AirloophvacUnitaryheatpumpAirtoairMultispeed"""
    Name: str
    Availability_Schedule_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Controlling_Zone_or_Thermostat_Location: str
    Supply_Air_Fan_Object_Type: str
    Supply_Air_Fan_Name: str
    Supply_Air_Fan_Placement: str
    Supply_Air_Fan_Operating_Mode_Schedule_Name: str
    Heating_Coil_Object_Type: str
    Heating_Coil_Name: str
    Minimum_Outdoor_DryBulb_Temperature_for_Compressor_Operation: str
    Cooling_Coil_Object_Type: str
    Cooling_Coil_Name: str
    Supplemental_Heating_Coil_Object_Type: str
    Supplemental_Heating_Coil_Name: str
    Maximum_Supply_Air_Temperature_from_Supplemental_Heater: str
    Maximum_Outdoor_DryBulb_Temperature_for_Supplemental_Heater_Operation: str
    Auxiliary_OnCycle_Electric_Power: str
    Auxiliary_OffCycle_Electric_Power: str
    Design_Heat_Recovery_Water_Flow_Rate: str
    Maximum_Temperature_for_Heat_Recovery: str
    Heat_Recovery_Water_Inlet_Node_Name: str
    Heat_Recovery_Water_Outlet_Node_Name: str
    No_Load_Supply_Air_Flow_Rate: str
    Number_of_Speeds_for_Heating: str
    Number_of_Speeds_for_Cooling: str
    Heating_Speed_1_Supply_Air_Flow_Rate: str
    Heating_Speed_2_Supply_Air_Flow_Rate: str
    Heating_Speed_3_Supply_Air_Flow_Rate: str
    Heating_Speed_4_Supply_Air_Flow_Rate: str
    Cooling_Speed_1_Supply_Air_Flow_Rate: str
    Cooling_Speed_2_Supply_Air_Flow_Rate: str
    Cooling_Speed_3_Supply_Air_Flow_Rate: str
    Cooling_Speed_4_Supply_Air_Flow_Rate: str

class AirloophvacUnitaryheatpumpWatertoairType(TypedDict, total=False):
    """"dict for AirloophvacUnitaryheatpumpWatertoair"""
    Name: str
    Availability_Schedule_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Supply_Air_Flow_Rate: str
    Controlling_Zone_or_Thermostat_Location: str
    Supply_Air_Fan_Object_Type: str
    Supply_Air_Fan_Name: str
    Heating_Coil_Object_Type: str
    Heating_Coil_Name: str
    Heating_Convergence: str
    Cooling_Coil_Object_Type: str
    Cooling_Coil_Name: str
    Cooling_Convergence: str
    Supplemental_Heating_Coil_Object_Type: str
    Supplemental_Heating_Coil_Name: str
    Maximum_Supply_Air_Temperature_from_Supplemental_Heater: str
    Maximum_Outdoor_DryBulb_Temperature_for_Supplemental_Heater_Operation: str
    Outdoor_DryBulb_Temperature_Sensor_Node_Name: str
    Fan_Placement: str
    Supply_Air_Fan_Operating_Mode_Schedule_Name: str
    Dehumidification_Control_Type: str
    Heat_Pump_Coil_Water_Flow_Mode: str

class AirloophvacUnitarysystemType(TypedDict, total=False):
    """"dict for AirloophvacUnitarysystem"""
    Name: str
    Control_Type: str
    Controlling_Zone_or_Thermostat_Location: str
    Dehumidification_Control_Type: str
    Availability_Schedule_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Supply_Fan_Object_Type: str
    Supply_Fan_Name: str
    Fan_Placement: str
    Supply_Air_Fan_Operating_Mode_Schedule_Name: str
    Heating_Coil_Object_Type: str
    Heating_Coil_Name: str
    DX_Heating_Coil_Sizing_Ratio: str
    Cooling_Coil_Object_Type: str
    Cooling_Coil_Name: str
    Use_DOAS_DX_Cooling_Coil: str
    Minimum_Supply_Air_Temperature: str
    Latent_Load_Control: str
    Supplemental_Heating_Coil_Object_Type: str
    Supplemental_Heating_Coil_Name: str
    Cooling_Supply_Air_Flow_Rate_Method: str
    Cooling_Supply_Air_Flow_Rate: str
    Cooling_Supply_Air_Flow_Rate_Per_Floor_Area: str
    Cooling_Fraction_of_Autosized_Cooling_Supply_Air_Flow_Rate: str
    Cooling_Supply_Air_Flow_Rate_Per_Unit_of_Capacity: str
    Heating_Supply_Air_Flow_Rate_Method: str
    Heating_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate_Per_Floor_Area: str
    Heating_Fraction_of_Autosized_Heating_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate_Per_Unit_of_Capacity: str
    No_Load_Supply_Air_Flow_Rate_Method: str
    No_Load_Supply_Air_Flow_Rate: str
    No_Load_Supply_Air_Flow_Rate_Per_Floor_Area: str
    No_Load_Fraction_of_Autosized_Cooling_Supply_Air_Flow_Rate: str
    No_Load_Fraction_of_Autosized_Heating_Supply_Air_Flow_Rate: str
    No_Load_Supply_Air_Flow_Rate_Per_Unit_of_Capacity_During_Cooling_Operation: str
    No_Load_Supply_Air_Flow_Rate_Per_Unit_of_Capacity_During_Heating_Operation: str
    No_Load_Supply_Air_Flow_Rate_Control_Set_To_Low_Speed: str
    Maximum_Supply_Air_Temperature: str
    Maximum_Outdoor_DryBulb_Temperature_for_Supplemental_Heater_Operation: str
    Outdoor_DryBulb_Temperature_Sensor_Node_Name: str
    Ancillary_OnCycle_Electric_Power: str
    Ancillary_OffCycle_Electric_Power: str
    Design_Heat_Recovery_Water_Flow_Rate: str
    Maximum_Temperature_for_Heat_Recovery: str
    Heat_Recovery_Water_Inlet_Node_Name: str
    Heat_Recovery_Water_Outlet_Node_Name: str
    Design_Specification_Multispeed_Object_Type: str
    Design_Specification_Multispeed_Object_Name: str

class AirloophvacZonemixerType(TypedDict, total=False):
    """"dict for AirloophvacZonemixer"""
    Name: str
    Outlet_Node_Name: str
    Inlet_1_Node_Name: str
    Inlet_2_Node_Name: str
    Inlet_3_Node_Name: str
    Inlet_4_Node_Name: str
    Inlet_5_Node_Name: str
    Inlet_6_Node_Name: str
    Inlet_7_Node_Name: str
    Inlet_8_Node_Name: str
    Inlet_9_Node_Name: str
    Inlet_10_Node_Name: str
    Inlet_11_Node_Name: str
    Inlet_12_Node_Name: str
    Inlet_13_Node_Name: str
    Inlet_14_Node_Name: str
    Inlet_15_Node_Name: str
    Inlet_16_Node_Name: str
    Inlet_17_Node_Name: str
    Inlet_18_Node_Name: str
    Inlet_19_Node_Name: str
    Inlet_20_Node_Name: str
    Inlet_21_Node_Name: str
    Inlet_22_Node_Name: str
    Inlet_23_Node_Name: str
    Inlet_24_Node_Name: str
    Inlet_25_Node_Name: str
    Inlet_26_Node_Name: str
    Inlet_27_Node_Name: str
    Inlet_28_Node_Name: str
    Inlet_29_Node_Name: str
    Inlet_30_Node_Name: str
    Inlet_31_Node_Name: str
    Inlet_32_Node_Name: str
    Inlet_33_Node_Name: str
    Inlet_34_Node_Name: str
    Inlet_35_Node_Name: str
    Inlet_36_Node_Name: str
    Inlet_37_Node_Name: str
    Inlet_38_Node_Name: str
    Inlet_39_Node_Name: str
    Inlet_40_Node_Name: str
    Inlet_41_Node_Name: str
    Inlet_42_Node_Name: str
    Inlet_43_Node_Name: str
    Inlet_44_Node_Name: str
    Inlet_45_Node_Name: str
    Inlet_46_Node_Name: str
    Inlet_47_Node_Name: str
    Inlet_48_Node_Name: str
    Inlet_49_Node_Name: str

class AirloophvacZonesplitterType(TypedDict, total=False):
    """"dict for AirloophvacZonesplitter"""
    Name: str
    Inlet_Node_Name: str
    Outlet_1_Node_Name: str
    Outlet_2_Node_Name: str
    Outlet_3_Node_Name: str
    Outlet_4_Node_Name: str
    Outlet_5_Node_Name: str
    Outlet_6_Node_Name: str
    Outlet_7_Node_Name: str
    Outlet_8_Node_Name: str
    Outlet_9_Node_Name: str
    Outlet_10_Node_Name: str
    Outlet_11_Node_Name: str
    Outlet_12_Node_Name: str
    Outlet_13_Node_Name: str
    Outlet_14_Node_Name: str
    Outlet_15_Node_Name: str
    Outlet_16_Node_Name: str
    Outlet_17_Node_Name: str
    Outlet_18_Node_Name: str
    Outlet_19_Node_Name: str
    Outlet_20_Node_Name: str
    Outlet_21_Node_Name: str
    Outlet_22_Node_Name: str
    Outlet_23_Node_Name: str
    Outlet_24_Node_Name: str
    Outlet_25_Node_Name: str
    Outlet_26_Node_Name: str
    Outlet_27_Node_Name: str
    Outlet_28_Node_Name: str
    Outlet_29_Node_Name: str
    Outlet_30_Node_Name: str
    Outlet_31_Node_Name: str
    Outlet_32_Node_Name: str
    Outlet_33_Node_Name: str
    Outlet_34_Node_Name: str
    Outlet_35_Node_Name: str
    Outlet_36_Node_Name: str
    Outlet_37_Node_Name: str
    Outlet_38_Node_Name: str
    Outlet_39_Node_Name: str
    Outlet_40_Node_Name: str
    Outlet_41_Node_Name: str
    Outlet_42_Node_Name: str
    Outlet_43_Node_Name: str
    Outlet_44_Node_Name: str
    Outlet_45_Node_Name: str
    Outlet_46_Node_Name: str
    Outlet_47_Node_Name: str
    Outlet_48_Node_Name: str
    Outlet_49_Node_Name: str

class AirterminalDualductConstantvolumeType(TypedDict, total=False):
    """"dict for AirterminalDualductConstantvolume"""
    Name: str
    Availability_Schedule_Name: str
    Air_Outlet_Node_Name: str
    Hot_Air_Inlet_Node_Name: str
    Cold_Air_Inlet_Node_Name: str
    Maximum_Air_Flow_Rate: str

class AirterminalDualductVavType(TypedDict, total=False):
    """"dict for AirterminalDualductVav"""
    Name: str
    Availability_Schedule_Name: str
    Air_Outlet_Node_Name: str
    Hot_Air_Inlet_Node_Name: str
    Cold_Air_Inlet_Node_Name: str
    Maximum_Damper_Air_Flow_Rate: str
    Zone_Minimum_Air_Flow_Fraction: str
    Design_Specification_Outdoor_Air_Object_Name: str
    Minimum_Air_Flow_Turndown_Schedule_Name: str

class AirterminalDualductVavOutdoorairType(TypedDict, total=False):
    """"dict for AirterminalDualductVavOutdoorair"""
    Name: str
    Availability_Schedule_Name: str
    Air_Outlet_Node_Name: str
    Outdoor_Air_Inlet_Node_Name: str
    Recirculated_Air_Inlet_Node_Name: str
    Maximum_Terminal_Air_Flow_Rate: str
    Design_Specification_Outdoor_Air_Object_Name: str
    Per_Person_Ventilation_Rate_Mode: str

class AirterminalSingleductConstantvolumeCooledbeamType(TypedDict, total=False):
    """"dict for AirterminalSingleductConstantvolumeCooledbeam"""
    Name: str
    Availability_Schedule_Name: str
    Cooled_Beam_Type: str
    Supply_Air_Inlet_Node_Name: str
    Supply_Air_Outlet_Node_Name: str
    Chilled_Water_Inlet_Node_Name: str
    Chilled_Water_Outlet_Node_Name: str
    Supply_Air_Volumetric_Flow_Rate: str
    Maximum_Total_Chilled_Water_Volumetric_Flow_Rate: str
    Number_of_Beams: str
    Beam_Length: str
    Design_Inlet_Water_Temperature: str
    Design_Outlet_Water_Temperature: str
    Coil_Surface_Area_per_Coil_Length: str
    Model_Parameter_a: str
    Model_Parameter_n1: str
    Model_Parameter_n2: str
    Model_Parameter_n3: str
    Model_Parameter_a0: str
    Model_Parameter_K1: str
    Model_Parameter_n: str
    Coefficient_of_Induction_Kin: str
    Leaving_Pipe_Inside_Diameter: str

class AirterminalSingleductConstantvolumeFourpipebeamType(TypedDict, total=False):
    """"dict for AirterminalSingleductConstantvolumeFourpipebeam"""
    Name: str
    Primary_Air_Availability_Schedule_Name: str
    Cooling_Availability_Schedule_Name: str
    Heating_Availability_Schedule_Name: str
    Primary_Air_Inlet_Node_Name: str
    Primary_Air_Outlet_Node_Name: str
    Chilled_Water_Inlet_Node_Name: str
    Chilled_Water_Outlet_Node_Name: str
    Hot_Water_Inlet_Node_Name: str
    Hot_Water_Outlet_Node_Name: str
    Design_Primary_Air_Volume_Flow_Rate: str
    Design_Chilled_Water_Volume_Flow_Rate: str
    Design_Hot_Water_Volume_Flow_Rate: str
    Zone_Total_Beam_Length: str
    Rated_Primary_Air_Flow_Rate_per_Beam_Length: str
    Beam_Rated_Cooling_Capacity_per_Beam_Length: str
    Beam_Rated_Cooling_Room_Air_Chilled_Water_Temperature_Difference: str
    Beam_Rated_Chilled_Water_Volume_Flow_Rate_per_Beam_Length: str
    Beam_Cooling_Capacity_Temperature_Difference_Modification_Factor_Curve_Name: str
    Beam_Cooling_Capacity_Air_Flow_Modification_Factor_Curve_Name: str
    Beam_Cooling_Capacity_Chilled_Water_Flow_Modification_Factor_Curve_Name: str
    Beam_Rated_Heating_Capacity_per_Beam_Length: str
    Beam_Rated_Heating_Room_Air_Hot_Water_Temperature_Difference: str
    Beam_Rated_Hot_Water_Volume_Flow_Rate_per_Beam_Length: str
    Beam_Heating_Capacity_Temperature_Difference_Modification_Factor_Curve_Name: str
    Beam_Heating_Capacity_Air_Flow_Modification_Factor_Curve_Name: str
    Beam_Heating_Capacity_Hot_Water_Flow_Modification_Factor_Curve_Name: str

class AirterminalSingleductConstantvolumeFourpipeinductionType(TypedDict, total=False):
    """"dict for AirterminalSingleductConstantvolumeFourpipeinduction"""
    Name: str
    Availability_Schedule_Name: str
    Maximum_Total_Air_Flow_Rate: str
    Induction_Ratio: str
    Supply_Air_Inlet_Node_Name: str
    Induced_Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Heating_Coil_Object_Type: str
    Heating_Coil_Name: str
    Maximum_Hot_Water_Flow_Rate: str
    Minimum_Hot_Water_Flow_Rate: str
    Heating_Convergence_Tolerance: str
    Cooling_Coil_Object_Type: str
    Cooling_Coil_Name: str
    Maximum_Cold_Water_Flow_Rate: str
    Minimum_Cold_Water_Flow_Rate: str
    Cooling_Convergence_Tolerance: str
    Zone_Mixer_Name: str

class AirterminalSingleductConstantvolumeNoreheatType(TypedDict, total=False):
    """"dict for AirterminalSingleductConstantvolumeNoreheat"""
    Name: str
    Availability_Schedule_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Maximum_Air_Flow_Rate: str
    Design_Specification_Outdoor_Air_Object_Name: str
    Per_Person_Ventilation_Rate_Mode: str

class AirterminalSingleductConstantvolumeReheatType(TypedDict, total=False):
    """"dict for AirterminalSingleductConstantvolumeReheat"""
    Name: str
    Availability_Schedule_Name: str
    Air_Outlet_Node_Name: str
    Air_Inlet_Node_Name: str
    Maximum_Air_Flow_Rate: str
    Reheat_Coil_Object_Type: str
    Reheat_Coil_Name: str
    Maximum_Hot_Water_or_Steam_Flow_Rate: str
    Minimum_Hot_Water_or_Steam_Flow_Rate: str
    Convergence_Tolerance: str
    Maximum_Reheat_Air_Temperature: str

class AirterminalSingleductMixerType(TypedDict, total=False):
    """"dict for AirterminalSingleductMixer"""
    Name: str
    ZoneHVAC_Unit_Object_Type: str
    ZoneHVAC_Unit_Object_Name: str
    Mixer_Outlet_Node_Name: str
    Mixer_Primary_Air_Inlet_Node_Name: str
    Mixer_Secondary_Air_Inlet_Node_Name: str
    Mixer_Connection_Type: str
    Design_Specification_Outdoor_Air_Object_Name: str
    Per_Person_Ventilation_Rate_Mode: str

class AirterminalSingleductParallelpiuReheatType(TypedDict, total=False):
    """"dict for AirterminalSingleductParallelpiuReheat"""
    Name: str
    Availability_Schedule_Name: str
    Maximum_Primary_Air_Flow_Rate: str
    Maximum_Secondary_Air_Flow_Rate: str
    Minimum_Primary_Air_Flow_Fraction: str
    Fan_On_Flow_Fraction: str
    Supply_Air_Inlet_Node_Name: str
    Secondary_Air_Inlet_Node_Name: str
    Outlet_Node_Name: str
    Reheat_Coil_Air_Inlet_Node_Name: str
    Zone_Mixer_Name: str
    Fan_Name: str
    Reheat_Coil_Object_Type: str
    Reheat_Coil_Name: str
    Maximum_Hot_Water_or_Steam_Flow_Rate: str
    Minimum_Hot_Water_or_Steam_Flow_Rate: str
    Convergence_Tolerance: str

class AirterminalSingleductSeriespiuReheatType(TypedDict, total=False):
    """"dict for AirterminalSingleductSeriespiuReheat"""
    Name: str
    Availability_Schedule_Name: str
    Maximum_Air_Flow_Rate: str
    Maximum_Primary_Air_Flow_Rate: str
    Minimum_Primary_Air_Flow_Fraction: str
    Supply_Air_Inlet_Node_Name: str
    Secondary_Air_Inlet_Node_Name: str
    Outlet_Node_Name: str
    Reheat_Coil_Air_Inlet_Node_Name: str
    Zone_Mixer_Name: str
    Fan_Name: str
    Reheat_Coil_Object_Type: str
    Reheat_Coil_Name: str
    Maximum_Hot_Water_or_Steam_Flow_Rate: str
    Minimum_Hot_Water_or_Steam_Flow_Rate: str
    Convergence_Tolerance: str

class AirterminalSingleductUserdefinedType(TypedDict, total=False):
    """"dict for AirterminalSingleductUserdefined"""
    Name: str
    Overall_Model_Simulation_Program_Calling_Manager_Name: str
    Model_Setup_and_Sizing_Program_Calling_Manager_Name: str
    Primary_Air_Inlet_Node_Name: str
    Primary_Air_Outlet_Node_Name: str
    Secondary_Air_Inlet_Node_Name: str
    Secondary_Air_Outlet_Node_Name: str
    Number_of_Plant_Loop_Connections: str
    Plant_Connection_1_Inlet_Node_Name: str
    Plant_Connection_1_Outlet_Node_Name: str
    Plant_Connection_2_Inlet_Node_Name: str
    Plant_Connection_2_Outlet_Node_Name: str
    Supply_Inlet_Water_Storage_Tank_Name: str
    Collection_Outlet_Water_Storage_Tank_Name: str
    Ambient_Zone_Name: str

class AirterminalSingleductVavHeatandcoolNoreheatType(TypedDict, total=False):
    """"dict for AirterminalSingleductVavHeatandcoolNoreheat"""
    Name: str
    Availability_Schedule_Name: str
    Air_Outlet_Node_Name: str
    Air_Inlet_Node_Name: str
    Maximum_Air_Flow_Rate: str
    Zone_Minimum_Air_Flow_Fraction: str
    Minimum_Air_Flow_Turndown_Schedule_Name: str

class AirterminalSingleductVavHeatandcoolReheatType(TypedDict, total=False):
    """"dict for AirterminalSingleductVavHeatandcoolReheat"""
    Name: str
    Availability_Schedule_Name: str
    Damper_Air_Outlet_Node_Name: str
    Air_Inlet_Node_Name: str
    Maximum_Air_Flow_Rate: str
    Zone_Minimum_Air_Flow_Fraction: str
    Reheat_Coil_Object_Type: str
    Reheat_Coil_Name: str
    Maximum_Hot_Water_or_Steam_Flow_Rate: str
    Minimum_Hot_Water_or_Steam_Flow_Rate: str
    Air_Outlet_Node_Name: str
    Convergence_Tolerance: str
    Maximum_Reheat_Air_Temperature: str
    Minimum_Air_Flow_Turndown_Schedule_Name: str

class AirterminalSingleductVavNoreheatType(TypedDict, total=False):
    """"dict for AirterminalSingleductVavNoreheat"""
    Name: str
    Availability_Schedule_Name: str
    Air_Outlet_Node_Name: str
    Air_Inlet_Node_Name: str
    Maximum_Air_Flow_Rate: str
    Zone_Minimum_Air_Flow_Input_Method: str
    Constant_Minimum_Air_Flow_Fraction: str
    Fixed_Minimum_Air_Flow_Rate: str
    Minimum_Air_Flow_Fraction_Schedule_Name: str
    Design_Specification_Outdoor_Air_Object_Name: str
    Minimum_Air_Flow_Turndown_Schedule_Name: str

class AirterminalSingleductVavReheatType(TypedDict, total=False):
    """"dict for AirterminalSingleductVavReheat"""
    Name: str
    Availability_Schedule_Name: str
    Damper_Air_Outlet_Node_Name: str
    Air_Inlet_Node_Name: str
    Maximum_Air_Flow_Rate: str
    Zone_Minimum_Air_Flow_Input_Method: str
    Constant_Minimum_Air_Flow_Fraction: str
    Fixed_Minimum_Air_Flow_Rate: str
    Minimum_Air_Flow_Fraction_Schedule_Name: str
    Reheat_Coil_Object_Type: str
    Reheat_Coil_Name: str
    Maximum_Hot_Water_or_Steam_Flow_Rate: str
    Minimum_Hot_Water_or_Steam_Flow_Rate: str
    Air_Outlet_Node_Name: str
    Convergence_Tolerance: str
    Damper_Heating_Action: str
    Maximum_Flow_per_Zone_Floor_Area_During_Reheat: str
    Maximum_Flow_Fraction_During_Reheat: str
    Maximum_Reheat_Air_Temperature: str
    Design_Specification_Outdoor_Air_Object_Name: str
    Minimum_Air_Flow_Turndown_Schedule_Name: str

class AirterminalSingleductVavReheatVariablespeedfanType(TypedDict, total=False):
    """"dict for AirterminalSingleductVavReheatVariablespeedfan"""
    Name: str
    Availability_Schedule_Name: str
    Maximum_Cooling_Air_Flow_Rate: str
    Maximum_Heating_Air_Flow_Rate: str
    Zone_Minimum_Air_Flow_Fraction: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Fan_Object_Type: str
    Fan_Name: str
    Heating_Coil_Object_Type: str
    Heating_Coil_Name: str
    Maximum_Hot_Water_or_Steam_Flow_Rate: str
    Minimum_Hot_Water_or_Steam_Flow_Rate: str
    Heating_Convergence_Tolerance: str
    Minimum_Air_Flow_Turndown_Schedule_Name: str

class AvailabilitymanagerDifferentialthermostatType(TypedDict, total=False):
    """"dict for AvailabilitymanagerDifferentialthermostat"""
    Name: str
    Hot_Node_Name: str
    Cold_Node_Name: str
    Temperature_Difference_On_Limit: str
    Temperature_Difference_Off_Limit: str

class AvailabilitymanagerHightemperatureturnoffType(TypedDict, total=False):
    """"dict for AvailabilitymanagerHightemperatureturnoff"""
    Name: str
    Sensor_Node_Name: str
    Temperature: str

class AvailabilitymanagerHightemperatureturnonType(TypedDict, total=False):
    """"dict for AvailabilitymanagerHightemperatureturnon"""
    Name: str
    Sensor_Node_Name: str
    Temperature: str

class AvailabilitymanagerHybridventilationType(TypedDict, total=False):
    """"dict for AvailabilitymanagerHybridventilation"""
    Name: str
    HVAC_Air_Loop_Name: str
    Control_Zone_Name: str
    Ventilation_Control_Mode_Schedule_Name: str
    Use_Weather_File_Rain_Indicators: str
    Maximum_Wind_Speed: str
    Minimum_Outdoor_Temperature: str
    Maximum_Outdoor_Temperature: str
    Minimum_Outdoor_Enthalpy: str
    Maximum_Outdoor_Enthalpy: str
    Minimum_Outdoor_Dewpoint: str
    Maximum_Outdoor_Dewpoint: str
    Minimum_Outdoor_Ventilation_Air_Schedule_Name: str
    Opening_Factor_Function_of_Wind_Speed_Curve_Name: str
    AirflowNetwork_Control_Type_Schedule_Name: str
    Simple_Airflow_Control_Type_Schedule_Name: str
    ZoneVentilation_Object_Name: str
    Minimum_HVAC_Operation_Time: str
    Minimum_Ventilation_Time: str

class AvailabilitymanagerLowtemperatureturnoffType(TypedDict, total=False):
    """"dict for AvailabilitymanagerLowtemperatureturnoff"""
    Name: str
    Sensor_Node_Name: str
    Temperature: str
    Applicability_Schedule_Name: str

class AvailabilitymanagerLowtemperatureturnonType(TypedDict, total=False):
    """"dict for AvailabilitymanagerLowtemperatureturnon"""
    Name: str
    Sensor_Node_Name: str
    Temperature: str

class AvailabilitymanagerNightcycleType(TypedDict, total=False):
    """"dict for AvailabilitymanagerNightcycle"""
    Name: str
    Applicability_Schedule_Name: str
    Fan_Schedule_Name: str
    Control_Type: str
    Thermostat_Tolerance: str
    Cycling_Run_Time_Control_Type: str
    Cycling_Run_Time: str
    Control_Zone_or_Zone_List_Name: str
    Cooling_Control_Zone_or_Zone_List_Name: str
    Heating_Control_Zone_or_Zone_List_Name: str
    Heating_Zone_Fans_Only_Zone_or_Zone_List_Name: str

class AvailabilitymanagerNightventilationType(TypedDict, total=False):
    """"dict for AvailabilitymanagerNightventilation"""
    Name: str
    Applicability_Schedule_Name: str
    Fan_Schedule_Name: str
    Ventilation_Temperature_Schedule_Name: str
    Ventilation_Temperature_Difference: str
    Ventilation_Temperature_Low_Limit: str
    Night_Venting_Flow_Fraction: str
    Control_Zone_Name: str

class AvailabilitymanagerOptimumstartType(TypedDict, total=False):
    """"dict for AvailabilitymanagerOptimumstart"""
    Name: str
    Applicability_Schedule_Name: str
    Fan_Schedule_Name: str
    Control_Type: str
    Control_Zone_Name: str
    Zone_List_Name: str
    Maximum_Value_for_Optimum_Start_Time: str
    Control_Algorithm: str
    Constant_Temperature_Gradient_during_Cooling: str
    Constant_Temperature_Gradient_during_Heating: str
    Initial_Temperature_Gradient_during_Cooling: str
    Initial_Temperature_Gradient_during_Heating: str
    Constant_Start_Time: str
    Number_of_Previous_Days: str

class AvailabilitymanagerScheduledType(TypedDict, total=False):
    """"dict for AvailabilitymanagerScheduled"""
    Name: str
    Schedule_Name: str

class AvailabilitymanagerScheduledoffType(TypedDict, total=False):
    """"dict for AvailabilitymanagerScheduledoff"""
    Name: str
    Schedule_Name: str

class AvailabilitymanagerScheduledonType(TypedDict, total=False):
    """"dict for AvailabilitymanagerScheduledon"""
    Name: str
    Schedule_Name: str

class AvailabilitymanagerassignmentlistType(TypedDict, total=False):
    """"dict for Availabilitymanagerassignmentlist"""
    Name: str
    Availability_Manager_1_Object_Type: str
    Availability_Manager_1_Name: str
    Availability_Manager_2_Object_Type: str
    Availability_Manager_2_Name: str
    Availability_Manager_3_Object_Type: str
    Availability_Manager_3_Name: str
    Availability_Manager_4_Object_Type: str
    Availability_Manager_4_Name: str
    Availability_Manager_5_Object_Type: str
    Availability_Manager_5_Name: str
    Availability_Manager_6_Object_Type: str
    Availability_Manager_6_Name: str

class BoilerHotwaterType(TypedDict, total=False):
    """"dict for BoilerHotwater"""
    Name: str
    Fuel_Type: str
    Nominal_Capacity: str
    Nominal_Thermal_Efficiency: str
    Efficiency_Curve_Temperature_Evaluation_Variable: str
    Normalized_Boiler_Efficiency_Curve_Name: str
    Design_Water_Flow_Rate: str
    Minimum_Part_Load_Ratio: str
    Maximum_Part_Load_Ratio: str
    Optimum_Part_Load_Ratio: str
    Boiler_Water_Inlet_Node_Name: str
    Boiler_Water_Outlet_Node_Name: str
    Water_Outlet_Upper_Temperature_Limit: str
    Boiler_Flow_Mode: str
    On_Cycle_Parasitic_Electric_Load: str
    Sizing_Factor: str
    EndUse_Subcategory: str
    Off_Cycle_Parasitic_Fuel_Load: str

class BoilerSteamType(TypedDict, total=False):
    """"dict for BoilerSteam"""
    Name: str
    Fuel_Type: str
    Maximum_Operating_Pressure: str
    Theoretical_Efficiency: str
    Design_Outlet_Steam_Temperature: str
    Nominal_Capacity: str
    Minimum_Part_Load_Ratio: str
    Maximum_Part_Load_Ratio: str
    Optimum_Part_Load_Ratio: str
    Coefficient_1_of_Fuel_Use_Function_of_Part_Load_Ratio_Curve: str
    Coefficient_2_of_Fuel_Use_Function_of_Part_Load_Ratio_Curve: str
    Coefficient_3_of_Fuel_Use_Function_of_Part_Load_Ratio_Curve: str
    Water_Inlet_Node_Name: str
    Steam_Outlet_Node_Name: str
    Sizing_Factor: str
    EndUse_Subcategory: str

class BranchType(TypedDict, total=False):
    """"dict for Branch"""
    Name: str
    Pressure_Drop_Curve_Name: str
    Component_1_Object_Type: str
    Component_1_Name: str
    Component_1_Inlet_Node_Name: str
    Component_1_Outlet_Node_Name: str
    Component_2_Object_Type: str
    Component_2_Name: str
    Component_2_Inlet_Node_Name: str
    Component_2_Outlet_Node_Name: str
    Component_3_Object_Type: str
    Component_3_Name: str
    Component_3_Inlet_Node_Name: str
    Component_3_Outlet_Node_Name: str
    Component_4_Object_Type: str
    Component_4_Name: str
    Component_4_Inlet_Node_Name: str
    Component_4_Outlet_Node_Name: str
    Component_5_Object_Type: str
    Component_5_Name: str
    Component_5_Inlet_Node_Name: str
    Component_5_Outlet_Node_Name: str
    Component_6_Object_Type: str
    Component_6_Name: str
    Component_6_Inlet_Node_Name: str
    Component_6_Outlet_Node_Name: str
    Component_7_Object_Type: str
    Component_7_Name: str
    Component_7_Inlet_Node_Name: str
    Component_7_Outlet_Node_Name: str
    Component_8_Object_Type: str
    Component_8_Name: str
    Component_8_Inlet_Node_Name: str
    Component_8_Outlet_Node_Name: str
    Component_9_Object_Type: str
    Component_9_Name: str
    Component_9_Inlet_Node_Name: str
    Component_9_Outlet_Node_Name: str
    Component_10_Object_Type: str
    Component_10_Name: str
    Component_10_Inlet_Node_Name: str
    Component_10_Outlet_Node_Name: str
    Component_11_Object_Type: str
    Component_11_Name: str
    Component_11_Inlet_Node_Name: str
    Component_11_Outlet_Node_Name: str

class BranchlistType(TypedDict, total=False):
    """"dict for Branchlist"""
    Name: str
    Branch_1_Name: str
    Branch_2_Name: str
    Branch_3_Name: str
    Branch_4_Name: str
    Branch_5_Name: str
    Branch_6_Name: str
    Branch_7_Name: str
    Branch_8_Name: str
    Branch_9_Name: str
    Branch_10_Name: str
    Branch_11_Name: str
    Branch_12_Name: str
    Branch_13_Name: str
    Branch_14_Name: str
    Branch_15_Name: str
    Branch_16_Name: str
    Branch_17_Name: str
    Branch_18_Name: str
    Branch_19_Name: str
    Branch_20_Name: str
    Branch_21_Name: str
    Branch_22_Name: str
    Branch_23_Name: str
    Branch_24_Name: str
    Branch_25_Name: str
    Branch_26_Name: str
    Branch_27_Name: str
    Branch_28_Name: str
    Branch_29_Name: str
    Branch_30_Name: str
    Branch_31_Name: str
    Branch_32_Name: str
    Branch_33_Name: str
    Branch_34_Name: str
    Branch_35_Name: str
    Branch_36_Name: str
    Branch_37_Name: str
    Branch_38_Name: str
    Branch_39_Name: str
    Branch_40_Name: str
    Branch_41_Name: str
    Branch_42_Name: str
    Branch_43_Name: str
    Branch_44_Name: str
    Branch_45_Name: str
    Branch_46_Name: str
    Branch_47_Name: str
    Branch_48_Name: str
    Branch_49_Name: str

class BuildingType(TypedDict, total=False):
    """"dict for Building"""
    Name: str
    North_Axis: str
    Terrain: str
    Loads_Convergence_Tolerance_Value: str
    Temperature_Convergence_Tolerance_Value: str
    Solar_Distribution: str
    Maximum_Number_of_Warmup_Days: str
    Minimum_Number_of_Warmup_Days: str

class BuildingsurfaceDetailedType(TypedDict, total=False):
    """"dict for BuildingsurfaceDetailed"""
    Name: str
    Surface_Type: str
    Construction_Name: str
    Zone_Name: str
    Space_Name: str
    Outside_Boundary_Condition: str
    Outside_Boundary_Condition_Object: str
    Sun_Exposure: str
    Wind_Exposure: str
    View_Factor_to_Ground: str
    Number_of_Vertices: str
    Vertex_1_Xcoordinate: str
    Vertex_1_Ycoordinate: str
    Vertex_1_Zcoordinate: str
    Vertex_2_Xcoordinate: str
    Vertex_2_Ycoordinate: str
    Vertex_2_Zcoordinate: str
    Vertex_3_Xcoordinate: str
    Vertex_3_Ycoordinate: str
    Vertex_3_Zcoordinate: str
    Vertex_4_Xcoordinate: str
    Vertex_4_Ycoordinate: str
    Vertex_4_Zcoordinate: str
    Vertex_5_Xcoordinate: str
    Vertex_5_Ycoordinate: str
    Vertex_5_Zcoordinate: str
    Vertex_6_Xcoordinate: str
    Vertex_6_Ycoordinate: str
    Vertex_6_Zcoordinate: str
    Vertex_7_Xcoordinate: str
    Vertex_7_Ycoordinate: str
    Vertex_7_Zcoordinate: str
    Vertex_8_Xcoordinate: str
    Vertex_8_Ycoordinate: str
    Vertex_8_Zcoordinate: str
    Vertex_9_Xcoordinate: str
    Vertex_9_Ycoordinate: str
    Vertex_9_Zcoordinate: str
    Vertex_10_Xcoordinate: str
    Vertex_10_Ycoordinate: str
    Vertex_10_Zcoordinate: str
    Vertex_11_Xcoordinate: str
    Vertex_11_Ycoordinate: str
    Vertex_11_Zcoordinate: str
    Vertex_12_Xcoordinate: str
    Vertex_12_Ycoordinate: str
    Vertex_12_Zcoordinate: str
    Vertex_13_Xcoordinate: str
    Vertex_13_Ycoordinate: str
    Vertex_13_Zcoordinate: str
    Vertex_14_Xcoordinate: str
    Vertex_14_Ycoordinate: str
    Vertex_14_Zcoordinate: str
    Vertex_15_Xcoordinate: str
    Vertex_15_Ycoordinate: str
    Vertex_15_Zcoordinate: str
    Vertex_16_Xcoordinate: str
    Vertex_16_Ycoordinate: str
    Vertex_16_Zcoordinate: str
    Vertex_17_Xcoordinate: str
    Vertex_17_Ycoordinate: str
    Vertex_17_Zcoordinate: str
    Vertex_18_Xcoordinate: str
    Vertex_18_Ycoordinate: str
    Vertex_18_Zcoordinate: str
    Vertex_19_Xcoordinate: str
    Vertex_19_Ycoordinate: str
    Vertex_19_Zcoordinate: str
    Vertex_20_Xcoordinate: str
    Vertex_20_Ycoordinate: str
    Vertex_20_Zcoordinate: str
    Vertex_21_Xcoordinate: str
    Vertex_21_Ycoordinate: str
    Vertex_21_Zcoordinate: str
    Vertex_22_Xcoordinate: str
    Vertex_22_Ycoordinate: str
    Vertex_22_Zcoordinate: str
    Vertex_23_Xcoordinate: str
    Vertex_23_Ycoordinate: str
    Vertex_23_Zcoordinate: str
    Vertex_24_Xcoordinate: str
    Vertex_24_Ycoordinate: str
    Vertex_24_Zcoordinate: str
    Vertex_25_Xcoordinate: str
    Vertex_25_Ycoordinate: str
    Vertex_25_Zcoordinate: str
    Vertex_26_Xcoordinate: str
    Vertex_26_Ycoordinate: str
    Vertex_26_Zcoordinate: str
    Vertex_27_Xcoordinate: str
    Vertex_27_Ycoordinate: str
    Vertex_27_Zcoordinate: str
    Vertex_28_Xcoordinate: str
    Vertex_28_Ycoordinate: str
    Vertex_28_Zcoordinate: str
    Vertex_29_Xcoordinate: str
    Vertex_29_Ycoordinate: str
    Vertex_29_Zcoordinate: str
    Vertex_30_Xcoordinate: str
    Vertex_30_Ycoordinate: str
    Vertex_30_Zcoordinate: str
    Vertex_31_Xcoordinate: str
    Vertex_31_Ycoordinate: str
    Vertex_31_Zcoordinate: str
    Vertex_32_Xcoordinate: str
    Vertex_32_Ycoordinate: str
    Vertex_32_Zcoordinate: str
    Vertex_33_Xcoordinate: str
    Vertex_33_Ycoordinate: str
    Vertex_33_Zcoordinate: str
    Vertex_34_Xcoordinate: str
    Vertex_34_Ycoordinate: str
    Vertex_34_Zcoordinate: str
    Vertex_35_Xcoordinate: str
    Vertex_35_Ycoordinate: str
    Vertex_35_Zcoordinate: str
    Vertex_36_Xcoordinate: str
    Vertex_36_Ycoordinate: str
    Vertex_36_Zcoordinate: str
    Vertex_37_Xcoordinate: str
    Vertex_37_Ycoordinate: str
    Vertex_37_Zcoordinate: str
    Vertex_38_Xcoordinate: str
    Vertex_38_Ycoordinate: str
    Vertex_38_Zcoordinate: str
    Vertex_39_Xcoordinate: str
    Vertex_39_Ycoordinate: str
    Vertex_39_Zcoordinate: str
    Vertex_40_Xcoordinate: str
    Vertex_40_Ycoordinate: str
    Vertex_40_Zcoordinate: str
    Vertex_41_Xcoordinate: str
    Vertex_41_Ycoordinate: str
    Vertex_41_Zcoordinate: str
    Vertex_42_Xcoordinate: str
    Vertex_42_Ycoordinate: str
    Vertex_42_Zcoordinate: str
    Vertex_43_Xcoordinate: str
    Vertex_43_Ycoordinate: str
    Vertex_43_Zcoordinate: str
    Vertex_44_Xcoordinate: str
    Vertex_44_Ycoordinate: str
    Vertex_44_Zcoordinate: str
    Vertex_45_Xcoordinate: str
    Vertex_45_Ycoordinate: str
    Vertex_45_Zcoordinate: str
    Vertex_46_Xcoordinate: str
    Vertex_46_Ycoordinate: str
    Vertex_46_Zcoordinate: str
    Vertex_47_Xcoordinate: str
    Vertex_47_Ycoordinate: str
    Vertex_47_Zcoordinate: str
    Vertex_48_Xcoordinate: str
    Vertex_48_Ycoordinate: str
    Vertex_48_Zcoordinate: str
    Vertex_49_Xcoordinate: str
    Vertex_49_Ycoordinate: str
    Vertex_49_Zcoordinate: str

class CeilingAdiabaticType(TypedDict, total=False):
    """"dict for CeilingAdiabatic"""
    Name: str
    Construction_Name: str
    Zone_Name: str
    Space_Name: str
    Azimuth_Angle: str
    Tilt_Angle: str
    Starting_X_Coordinate: str
    Starting_Y_Coordinate: str
    Starting_Z_Coordinate: str
    Length: str
    Width: str

class CeilingInterzoneType(TypedDict, total=False):
    """"dict for CeilingInterzone"""
    Name: str
    Construction_Name: str
    Zone_Name: str
    Space_Name: str
    Outside_Boundary_Condition_Object: str
    Azimuth_Angle: str
    Tilt_Angle: str
    Starting_X_Coordinate: str
    Starting_Y_Coordinate: str
    Starting_Z_Coordinate: str
    Length: str
    Width: str

class CentralheatpumpsystemType(TypedDict, total=False):
    """"dict for Centralheatpumpsystem"""
    Name: str
    Control_Method: str
    Cooling_Loop_Inlet_Node_Name: str
    Cooling_Loop_Outlet_Node_Name: str
    Source_Loop_Inlet_Node_Name: str
    Source_Loop_Outlet_Node_Name: str
    Heating_Loop_Inlet_Node_Name: str
    Heating_Loop_Outlet_Node_Name: str
    Ancillary_Power: str
    Ancillary_Operation_Schedule_Name: str
    Chiller_Heater_Modules_Performance_Component_Object_Type_1: str
    Chiller_Heater_Modules_Performance_Component_Name_1: str
    Chiller_Heater_Modules_Control_Schedule_Name_1: str
    Number_of_Chiller_Heater_Modules_1: str
    Chiller_Heater_Modules_Performance_Component_Object_Type_2: str
    Chiller_Heater_Modules_Performance_Component_Name_2: str
    Chiller_Heater_Modules_Control_Schedule_Name_2: str
    Number_of_Chiller_Heater_Modules_2: str
    Chiller_Heater_Performance_Component_Object_Type_3: str
    Chiller_Heater_Performance_Component_Name_3: str
    Chiller_Heater_Modules_Control_Schedule_Name_3: str
    Number_of_Chiller_Heater_Modules_3: str
    Chiller_Heater_Modules_Performance_Component_Object_Type_4: str
    Chiller_Heater_Modules_Performance_Component_Name_4: str
    Chiller_Heater_Modules_Control_Schedule_Name_4: str
    Number_of_Chiller_Heater_Modules_4: str
    Chiller_Heater_Modules_Performance_Component_Object_Type_5: str
    Chiller_Heater_Models_Performance_Component_Name_5: str
    Chiller_Heater_Modules_Control_Schedule_Name_5: str
    Number_of_Chiller_Heater_Modules_5: str
    Chiller_Heater_Modules_Performance_Component_Object_Type_6: str
    Chiller_Heater_Modules_Performance_Component_Name_6: str
    Chiller_Heater_Modules_Control_Schedule_Name_6: str
    Number_of_Chiller_Heater_Modules_6: str
    Chiller_Heater_Modules_Performance_Component_Object_Type_7: str
    Chiller_Heater_Modules_Performance_Component_Name_7: str
    Chiller_Heater_Modules_Control_Schedule_Name_7: str
    Number_of_Chiller_Heater_Modules_7: str
    Chiller_Heater_Modules_Performance_Component_Object_Type_8: str
    Chiller_Heater_Modules_Performance_Component_Name_8: str
    Chiller_Heater_Modules_Control_Schedule_Name_8: str
    Number_of_Chiller_Heater_Modules_8: str
    Chiller_Heater_Modules_Performance_Component_Object_Type_9: str
    Chiller_Heater_Modules_Performance_Component_Name_9: str
    Chiller_Heater_Modules_Control_Schedule_Name_9: str
    Number_of_Chiller_Heater_Modules_9: str
    Chiller_Heater_Modules_Performance_Component_Object_Type_10: str
    Chiller_Heater_Modules_Performance_Component_Name_10: str
    Chiller_Heater_Modules_Control_Schedule_Name_10: str
    Number_of_Chiller_Heater_Modules_10: str
    Chiller_Heater_Modules_Performance_Component_Object_Type_11: str
    Chiller_Heater_Modules_Performance_Component_Name_11: str
    Chiller_Heater_Module_Control_Schedule_Name_11: str
    Number_of_Chiller_Heater_Modules_11: str
    Chiller_Heater_Modules_Performance_Component_Object_Type_12: str
    Chiller_Heater_Modules_Performance_Component_Name_12: str
    Chiller_Heater_Modules_Control_Schedule_Name_12: str
    Number_of_Chiller_Heater_Modules_12: str
    Chiller_Heater_Modules_Performance_Component_Object_Type_13: str
    Chiller_Heater_Modules_Performance_Component_Name_13: str
    Chiller_Heater_Modules_Control_Schedule_Name_13: str
    Number_of_Chiller_Heater_Modules_13: str
    Chiller_Heater_Modules_Performance_Component_Object_Type_14: str
    Chiller_Heater_Modules_Performance_Component_Name_14: str
    Chiller_Heater_Modules_Control_Schedule_Name_14: str
    Number_of_Chiller_Heater_Modules_14: str
    Chiller_Heater_Modules_Performance_Component_Object_Type_15: str
    Chiller_Heater_Modules_Performance_Component_Name_15: str
    Chiller_Heater_Modules_Control_Schedule_Name_15: str
    Number_of_Chiller_Heater_Modules_15: str
    Chiller_Heater_Modules_Performance_Component_Object_Type_16: str
    Chiller_Heater_Modules_Performance_Component_Name_16: str
    Chiller_Heater_Modules_Control_Schedule_Name_16: str
    Number_of_Chiller_Heater_Modules_16: str
    Chiller_Heater_Modules_Performance_Component_Object_Type_17: str
    Chiller_Heater_Modules_Performance_Component_Name_17: str
    Chiller_Heater_Modules_Control_Schedule_Name_17: str
    Number_of_Chiller_Heater_Modules_17: str
    Chiller_Heater_Modules_Performance_Component_Object_Type_18: str
    Chiller_Heater_Modules_Performance_Component_Name_18: str
    Chiller_Heater_Modules_Control_Control_Schedule_Name_18: str
    Number_of_Chiller_Heater_Modules_18: str
    Chiller_Heater_Modules_Performance_Component_Object_Type_19: str
    Chiller_Heater_Modules_Performance_Component_Name_19: str
    Chiller_Heater_Modules_Control_Schedule_Name_19: str
    Number_of_Chiller_Heater_Modules_19: str
    Chiller_Heater_Modules_Performance_Component_Object_Type_20: str
    Chiller_Heater_Modules_Performance_Component_Name_20: str
    Chiller_Heater_Modules_Control_Schedule_Name_20: str
    Number_of_Chiller_Heater_Modules_20: str

class ChillerAbsorptionType(TypedDict, total=False):
    """"dict for ChillerAbsorption"""
    Name: str
    Nominal_Capacity: str
    Nominal_Pumping_Power: str
    Chilled_Water_Inlet_Node_Name: str
    Chilled_Water_Outlet_Node_Name: str
    Condenser_Inlet_Node_Name: str
    Condenser_Outlet_Node_Name: str
    Minimum_Part_Load_Ratio: str
    Maximum_Part_Load_Ratio: str
    Optimum_Part_Load_Ratio: str
    Design_Condenser_Inlet_Temperature: str
    Design_Chilled_Water_Flow_Rate: str
    Design_Condenser_Water_Flow_Rate: str
    Coefficient_1_of_the_Hot_Water_or_Steam_Use_Part_Load_Ratio_Curve: str
    Coefficient_2_of_the_Hot_Water_or_Steam_Use_Part_Load_Ratio_Curve: str
    Coefficient_3_of_the_Hot_Water_or_Steam_Use_Part_Load_Ratio_Curve: str
    Coefficient_1_of_the_Pump_Electric_Use_Part_Load_Ratio_Curve: str
    Coefficient_2_of_the_Pump_Electric_Use_Part_Load_Ratio_Curve: str
    Coefficient_3_of_the_Pump_Electric_Use_Part_Load_Ratio_Curve: str
    Chilled_Water_Outlet_Temperature_Lower_Limit: str
    Generator_Inlet_Node_Name: str
    Generator_Outlet_Node_Name: str
    Chiller_Flow_Mode: str
    Generator_Heat_Source_Type: str
    Design_Generator_Fluid_Flow_Rate: str
    Degree_of_Subcooling_in_Steam_Generator: str
    Sizing_Factor: str

class ChillerAbsorptionIndirectType(TypedDict, total=False):
    """"dict for ChillerAbsorptionIndirect"""
    Name: str
    Nominal_Capacity: str
    Nominal_Pumping_Power: str
    Chilled_Water_Inlet_Node_Name: str
    Chilled_Water_Outlet_Node_Name: str
    Condenser_Inlet_Node_Name: str
    Condenser_Outlet_Node_Name: str
    Minimum_Part_Load_Ratio: str
    Maximum_Part_Load_Ratio: str
    Optimum_Part_Load_Ratio: str
    Design_Condenser_Inlet_Temperature: str
    Condenser_Inlet_Temperature_Lower_Limit: str
    Chilled_Water_Outlet_Temperature_Lower_Limit: str
    Design_Chilled_Water_Flow_Rate: str
    Design_Condenser_Water_Flow_Rate: str
    Chiller_Flow_Mode: str
    Generator_Heat_Input_Function_of_Part_Load_Ratio_Curve_Name: str
    Pump_Electric_Input_Function_of_Part_Load_Ratio_Curve_Name: str
    Generator_Inlet_Node_Name: str
    Generator_Outlet_Node_Name: str
    Capacity_Correction_Function_of_Condenser_Temperature_Curve_Name: str
    Capacity_Correction_Function_of_Chilled_Water_Temperature_Curve_Name: str
    Capacity_Correction_Function_of_Generator_Temperature_Curve_Name: str
    Generator_Heat_Input_Correction_Function_of_Condenser_Temperature_Curve_Name: str
    Generator_Heat_Input_Correction_Function_of_Chilled_Water_Temperature_Curve_Name: str
    Generator_Heat_Source_Type: str
    Design_Generator_Fluid_Flow_Rate: str
    Temperature_Lower_Limit_Generator_Inlet: str
    Degree_of_Subcooling_in_Steam_Generator: str
    Degree_of_Subcooling_in_Steam_Condensate_Loop: str
    Sizing_Factor: str

class ChillerCombustionturbineType(TypedDict, total=False):
    """"dict for ChillerCombustionturbine"""
    Name: str
    Condenser_Type: str
    Nominal_Capacity: str
    Nominal_COP: str
    Chilled_Water_Inlet_Node_Name: str
    Chilled_Water_Outlet_Node_Name: str
    Condenser_Inlet_Node_Name: str
    Condenser_Outlet_Node_Name: str
    Minimum_Part_Load_Ratio: str
    Maximum_Part_Load_Ratio: str
    Optimum_Part_Load_Ratio: str
    Design_Condenser_Inlet_Temperature: str
    Temperature_Rise_Coefficient: str
    Design_Chilled_Water_Outlet_Temperature: str
    Design_Chilled_Water_Flow_Rate: str
    Design_Condenser_Water_Flow_Rate: str
    Coefficient_1_of_Capacity_Ratio_Curve: str
    Coefficient_2_of_Capacity_Ratio_Curve: str
    Coefficient_3_of_Capacity_Ratio_Curve: str
    Coefficient_1_of_Power_Ratio_Curve: str
    Coefficient_2_of_Power_Ratio_Curve: str
    Coefficient_3_of_Power_Ratio_Curve: str
    Coefficient_1_of_Full_Load_Ratio_Curve: str
    Coefficient_2_of_Full_Load_Ratio_Curve: str
    Coefficient_3_of_Full_Load_Ratio_Curve: str
    Chilled_Water_Outlet_Temperature_Lower_Limit: str
    Coefficient_1_of_Fuel_Input_Curve: str
    Coefficient_2_of_Fuel_Input_Curve: str
    Coefficient_3_of_Fuel_Input_Curve: str
    Coefficient_1_of_Temperature_Based_Fuel_Input_Curve: str
    Coefficient_2_of_Temperature_Based_Fuel_Input_Curve: str
    Coefficient_3_of_Temperature_Based_Fuel_Input_Curve: str
    Coefficient_1_of_Exhaust_Flow_Curve: str
    Coefficient_2_of_Exhaust_Flow_Curve: str
    Coefficient_3_of_Exhaust_Flow_Curve: str
    Coefficient_1_of_Exhaust_Gas_Temperature_Curve: str
    Coefficient_2_of_Exhaust_Gas_Temperature_Curve: str
    Coefficient_3_of_Exhaust_Gas_Temperature_Curve: str
    Coefficient_1_of_Temperature_Based_Exhaust_Gas_Temperature_Curve: str
    Coefficient_2_of_Temperature_Based_Exhaust_Gas_Temperature_Curve: str
    Coefficient_3_of_Temperature_Based_Exhaust_Gas_Temperature_Curve: str
    Coefficient_1_of_Recovery_Lube_Heat_Curve: str
    Coefficient_2_of_Recovery_Lube_Heat_Curve: str
    Coefficient_3_of_Recovery_Lube_Heat_Curve: str
    Coefficient_1_of_UFactor_Times_Area_Curve: str
    Coefficient_2_of_UFactor_Times_Area_Curve: str
    Gas_Turbine_Engine_Capacity: str
    Maximum_Exhaust_Flow_per_Unit_of_Power_Output: str
    Design_Steam_Saturation_Temperature: str
    Fuel_Higher_Heating_Value: str
    Design_Heat_Recovery_Water_Flow_Rate: str
    Heat_Recovery_Inlet_Node_Name: str
    Heat_Recovery_Outlet_Node_Name: str
    Chiller_Flow_Mode: str
    Fuel_Type: str
    Heat_Recovery_Maximum_Temperature: str
    Sizing_Factor: str
    Basin_Heater_Capacity: str
    Basin_Heater_Setpoint_Temperature: str
    Basin_Heater_Operating_Schedule_Name: str
    Condenser_Heat_Recovery_Relative_Capacity_Fraction: str
    Turbine_Engine_Efficiency: str

class ChillerConstantcopType(TypedDict, total=False):
    """"dict for ChillerConstantcop"""
    Name: str
    Nominal_Capacity: str
    Nominal_COP: str
    Design_Chilled_Water_Flow_Rate: str
    Design_Condenser_Water_Flow_Rate: str
    Chilled_Water_Inlet_Node_Name: str
    Chilled_Water_Outlet_Node_Name: str
    Condenser_Inlet_Node_Name: str
    Condenser_Outlet_Node_Name: str
    Condenser_Type: str
    Chiller_Flow_Mode: str
    Sizing_Factor: str
    Basin_Heater_Capacity: str
    Basin_Heater_Setpoint_Temperature: str
    Basin_Heater_Operating_Schedule_Name: str

class ChillerElectricType(TypedDict, total=False):
    """"dict for ChillerElectric"""
    Name: str
    Condenser_Type: str
    Nominal_Capacity: str
    Nominal_COP: str
    Chilled_Water_Inlet_Node_Name: str
    Chilled_Water_Outlet_Node_Name: str
    Condenser_Inlet_Node_Name: str
    Condenser_Outlet_Node_Name: str
    Minimum_Part_Load_Ratio: str
    Maximum_Part_Load_Ratio: str
    Optimum_Part_Load_Ratio: str
    Design_Condenser_Inlet_Temperature: str
    Temperature_Rise_Coefficient: str
    Design_Chilled_Water_Outlet_Temperature: str
    Design_Chilled_Water_Flow_Rate: str
    Design_Condenser_Fluid_Flow_Rate: str
    Coefficient_1_of_Capacity_Ratio_Curve: str
    Coefficient_2_of_Capacity_Ratio_Curve: str
    Coefficient_3_of_Capacity_Ratio_Curve: str
    Coefficient_1_of_Power_Ratio_Curve: str
    Coefficient_2_of_Power_Ratio_Curve: str
    Coefficient_3_of_Power_Ratio_Curve: str
    Coefficient_1_of_Full_Load_Ratio_Curve: str
    Coefficient_2_of_Full_Load_Ratio_Curve: str
    Coefficient_3_of_Full_Load_Ratio_Curve: str
    Chilled_Water_Outlet_Temperature_Lower_Limit: str
    Chiller_Flow_Mode: str
    Design_Heat_Recovery_Water_Flow_Rate: str
    Heat_Recovery_Inlet_Node_Name: str
    Heat_Recovery_Outlet_Node_Name: str
    Sizing_Factor: str
    Basin_Heater_Capacity: str
    Basin_Heater_Setpoint_Temperature: str
    Basin_Heater_Operating_Schedule_Name: str
    Condenser_Heat_Recovery_Relative_Capacity_Fraction: str
    Heat_Recovery_Inlet_High_Temperature_Limit_Schedule_Name: str
    Heat_Recovery_Leaving_Temperature_Setpoint_Node_Name: str
    EndUse_Subcategory: str

class ChillerElectricAshrae205Type(TypedDict, total=False):
    """"dict for ChillerElectricAshrae205"""
    Name: str
    Representation_File_Name: str
    Performance_Interpolation_Method: str
    Rated_Capacity: str
    Sizing_Factor: str
    Ambient_Temperature_Indicator: str
    Ambient_Temperature_Schedule_Name: str
    Ambient_Temperature_Zone_Name: str
    Ambient_Temperature_Outdoor_Air_Node_Name: str
    Chilled_Water_Inlet_Node_Name: str
    Chilled_Water_Outlet_Node_Name: str
    Chilled_Water_Maximum_Requested_Flow_Rate: str
    Condenser_Inlet_Node_Name: str
    Condenser_Outlet_Node_Name: str
    Condenser_Maximum_Requested_Flow_Rate: str
    Chiller_Flow_Mode: str
    Oil_Cooler_Inlet_Node_Name: str
    Oil_Cooler_Outlet_Node_Name: str
    Oil_Cooler_Design_Flow_Rate: str
    Auxiliary_Inlet_Node_Name: str
    Auxiliary_Outlet_Node_Name: str
    Auxiliary_Cooling_Design_Flow_Rate: str
    Heat_Recovery_Inlet_Node_Name: str
    Heat_Recovery_Outlet_Node_Name: str
    EndUse_Subcategory: str

class ChillerElectricEirType(TypedDict, total=False):
    """"dict for ChillerElectricEir"""
    Name: str
    Reference_Capacity: str
    Reference_COP: str
    Reference_Leaving_Chilled_Water_Temperature: str
    Reference_Entering_Condenser_Fluid_Temperature: str
    Reference_Chilled_Water_Flow_Rate: str
    Reference_Condenser_Fluid_Flow_Rate: str
    Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Electric_Input_to_Cooling_Output_Ratio_Function_of_Temperature_Curve_Name: str
    Electric_Input_to_Cooling_Output_Ratio_Function_of_Part_Load_Ratio_Curve_Name: str
    Minimum_Part_Load_Ratio: str
    Maximum_Part_Load_Ratio: str
    Optimum_Part_Load_Ratio: str
    Minimum_Unloading_Ratio: str
    Chilled_Water_Inlet_Node_Name: str
    Chilled_Water_Outlet_Node_Name: str
    Condenser_Inlet_Node_Name: str
    Condenser_Outlet_Node_Name: str
    Condenser_Type: str
    Condenser_Fan_Power_Ratio: str
    Fraction_of_Compressor_Electric_Consumption_Rejected_by_Condenser: str
    Leaving_Chilled_Water_Lower_Temperature_Limit: str
    Chiller_Flow_Mode: str
    Design_Heat_Recovery_Water_Flow_Rate: str
    Heat_Recovery_Inlet_Node_Name: str
    Heat_Recovery_Outlet_Node_Name: str
    Sizing_Factor: str
    Basin_Heater_Capacity: str
    Basin_Heater_Setpoint_Temperature: str
    Basin_Heater_Operating_Schedule_Name: str
    Condenser_Heat_Recovery_Relative_Capacity_Fraction: str
    Heat_Recovery_Inlet_High_Temperature_Limit_Schedule_Name: str
    Heat_Recovery_Leaving_Temperature_Setpoint_Node_Name: str
    EndUse_Subcategory: str

class ChillerElectricReformulatedeirType(TypedDict, total=False):
    """"dict for ChillerElectricReformulatedeir"""
    Name: str
    Reference_Capacity: str
    Reference_COP: str
    Reference_Leaving_Chilled_Water_Temperature: str
    Reference_Leaving_Condenser_Water_Temperature: str
    Reference_Chilled_Water_Flow_Rate: str
    Reference_Condenser_Water_Flow_Rate: str
    Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Electric_Input_to_Cooling_Output_Ratio_Function_of_Temperature_Curve_Name: str
    Electric_Input_to_Cooling_Output_Ratio_Function_of_Part_Load_Ratio_Curve_Type: str
    Electric_Input_to_Cooling_Output_Ratio_Function_of_Part_Load_Ratio_Curve_Name: str
    Minimum_Part_Load_Ratio: str
    Maximum_Part_Load_Ratio: str
    Optimum_Part_Load_Ratio: str
    Minimum_Unloading_Ratio: str
    Chilled_Water_Inlet_Node_Name: str
    Chilled_Water_Outlet_Node_Name: str
    Condenser_Inlet_Node_Name: str
    Condenser_Outlet_Node_Name: str
    Fraction_of_Compressor_Electric_Consumption_Rejected_by_Condenser: str
    Leaving_Chilled_Water_Lower_Temperature_Limit: str
    Chiller_Flow_Mode_Type: str
    Design_Heat_Recovery_Water_Flow_Rate: str
    Heat_Recovery_Inlet_Node_Name: str
    Heat_Recovery_Outlet_Node_Name: str
    Sizing_Factor: str
    Condenser_Heat_Recovery_Relative_Capacity_Fraction: str
    Heat_Recovery_Inlet_High_Temperature_Limit_Schedule_Name: str
    Heat_Recovery_Leaving_Temperature_Setpoint_Node_Name: str
    EndUse_Subcategory: str

class ChillerEnginedrivenType(TypedDict, total=False):
    """"dict for ChillerEnginedriven"""
    Name: str
    Condenser_Type: str
    Nominal_Capacity: str
    Nominal_COP: str
    Chilled_Water_Inlet_Node_Name: str
    Chilled_Water_Outlet_Node_Name: str
    Condenser_Inlet_Node_Name: str
    Condenser_Outlet_Node_Name: str
    Minimum_Part_Load_Ratio: str
    Maximum_Part_Load_Ratio: str
    Optimum_Part_Load_Ratio: str
    Design_Condenser_Inlet_Temperature: str
    Temperature_Rise_Coefficient: str
    Design_Chilled_Water_Outlet_Temperature: str
    Design_Chilled_Water_Flow_Rate: str
    Design_Condenser_Water_Flow_Rate: str
    Coefficient_1_of_Capacity_Ratio_Curve: str
    Coefficient_2_of_Capacity_Ratio_Curve: str
    Coefficient_3_of_Capacity_Ratio_Curve: str
    Coefficient_1_of_Power_Ratio_Curve: str
    Coefficient_2_of_Power_Ratio_Curve: str
    Coefficient_3_of_Power_Ratio_Curve: str
    Coefficient_1_of_Full_Load_Ratio_Curve: str
    Coefficient_2_of_Full_Load_Ratio_Curve: str
    Coefficient_3_of_Full_Load_Ratio_Curve: str
    Chilled_Water_Outlet_Temperature_Lower_Limit: str
    Fuel_Use_Curve_Name: str
    Jacket_Heat_Recovery_Curve_Name: str
    Lube_Heat_Recovery_Curve_Name: str
    Total_Exhaust_Energy_Curve_Name: str
    Exhaust_Temperature_Curve_Name: str
    Coefficient_1_of_UFactor_Times_Area_Curve: str
    Coefficient_2_of_UFactor_Times_Area_Curve: str
    Maximum_Exhaust_Flow_per_Unit_of_Power_Output: str
    Design_Minimum_Exhaust_Temperature: str
    Fuel_Type: str
    Fuel_Higher_Heating_Value: str
    Design_Heat_Recovery_Water_Flow_Rate: str
    Heat_Recovery_Inlet_Node_Name: str
    Heat_Recovery_Outlet_Node_Name: str
    Chiller_Flow_Mode: str
    Maximum_Temperature_for_Heat_Recovery_at_Heat_Recovery_Outlet_Node: str
    Sizing_Factor: str
    Basin_Heater_Capacity: str
    Basin_Heater_Setpoint_Temperature: str
    Basin_Heater_Operating_Schedule_Name: str
    Condenser_Heat_Recovery_Relative_Capacity_Fraction: str

class ChillerheaterAbsorptionDirectfiredType(TypedDict, total=False):
    """"dict for ChillerheaterAbsorptionDirectfired"""
    Name: str
    Nominal_Cooling_Capacity: str
    Heating_to_Cooling_Capacity_Ratio: str
    Fuel_Input_to_Cooling_Output_Ratio: str
    Fuel_Input_to_Heating_Output_Ratio: str
    Electric_Input_to_Cooling_Output_Ratio: str
    Electric_Input_to_Heating_Output_Ratio: str
    Chilled_Water_Inlet_Node_Name: str
    Chilled_Water_Outlet_Node_Name: str
    Condenser_Inlet_Node_Name: str
    Condenser_Outlet_Node_Name: str
    Hot_Water_Inlet_Node_Name: str
    Hot_Water_Outlet_Node_Name: str
    Minimum_Part_Load_Ratio: str
    Maximum_Part_Load_Ratio: str
    Optimum_Part_Load_Ratio: str
    Design_Entering_Condenser_Water_Temperature: str
    Design_Leaving_Chilled_Water_Temperature: str
    Design_Chilled_Water_Flow_Rate: str
    Design_Condenser_Water_Flow_Rate: str
    Design_Hot_Water_Flow_Rate: str
    Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Fuel_Input_to_Cooling_Output_Ratio_Function_of_Temperature_Curve_Name: str
    Fuel_Input_to_Cooling_Output_Ratio_Function_of_Part_Load_Ratio_Curve_Name: str
    Electric_Input_to_Cooling_Output_Ratio_Function_of_Temperature_Curve_Name: str
    Electric_Input_to_Cooling_Output_Ratio_Function_of_Part_Load_Ratio_Curve_Name: str
    Heating_Capacity_Function_of_Cooling_Capacity_Curve_Name: str
    Fuel_Input_to_Heat_Output_Ratio_During_Heating_Only_Operation_Curve_Name: str
    Temperature_Curve_Input_Variable: str
    Condenser_Type: str
    Chilled_Water_Temperature_Lower_Limit: str
    Fuel_Higher_Heating_Value: str
    Fuel_Type: str
    Sizing_Factor: str

class ChillerheaterAbsorptionDoubleeffectType(TypedDict, total=False):
    """"dict for ChillerheaterAbsorptionDoubleeffect"""
    Name: str
    Nominal_Cooling_Capacity: str
    Heating_to_Cooling_Capacity_Ratio: str
    Thermal_Energy_Input_to_Cooling_Output_Ratio: str
    Thermal_Energy_Input_to_Heating_Output_Ratio: str
    Electric_Input_to_Cooling_Output_Ratio: str
    Electric_Input_to_Heating_Output_Ratio: str
    Chilled_Water_Inlet_Node_Name: str
    Chilled_Water_Outlet_Node_Name: str
    Condenser_Inlet_Node_Name: str
    Condenser_Outlet_Node_Name: str
    Hot_Water_Inlet_Node_Name: str
    Hot_Water_Outlet_Node_Name: str
    Minimum_Part_Load_Ratio: str
    Maximum_Part_Load_Ratio: str
    Optimum_Part_Load_Ratio: str
    Design_Entering_Condenser_Water_Temperature: str
    Design_Leaving_Chilled_Water_Temperature: str
    Design_Chilled_Water_Flow_Rate: str
    Design_Condenser_Water_Flow_Rate: str
    Design_Hot_Water_Flow_Rate: str
    Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Fuel_Input_to_Cooling_Output_Ratio_Function_of_Temperature_Curve_Name: str
    Fuel_Input_to_Cooling_Output_Ratio_Function_of_Part_Load_Ratio_Curve_Name: str
    Electric_Input_to_Cooling_Output_Ratio_Function_of_Temperature_Curve_Name: str
    Electric_Input_to_Cooling_Output_Ratio_Function_of_Part_Load_Ratio_Curve_Name: str
    Heating_Capacity_Function_of_Cooling_Capacity_Curve_Name: str
    Fuel_Input_to_Heat_Output_Ratio_During_Heating_Only_Operation_Curve_Name: str
    Temperature_Curve_Input_Variable: str
    Condenser_Type: str
    Chilled_Water_Temperature_Lower_Limit: str
    Exhaust_Source_Object_Type: str
    Exhaust_Source_Object_Name: str
    Sizing_Factor: str

class ChillerheaterperformanceElectricEirType(TypedDict, total=False):
    """"dict for ChillerheaterperformanceElectricEir"""
    Name: str
    Reference_Cooling_Mode_Evaporator_Capacity: str
    Reference_Cooling_Mode_COP: str
    Reference_Cooling_Mode_Leaving_Chilled_Water_Temperature: str
    Reference_Cooling_Mode_Entering_Condenser_Fluid_Temperature: str
    Reference_Cooling_Mode_Leaving_Condenser_Water_Temperature: str
    Reference_Heating_Mode_Cooling_Capacity_Ratio: str
    Reference_Heating_Mode_Cooling_Power_Input_Ratio: str
    Reference_Heating_Mode_Leaving_Chilled_Water_Temperature: str
    Reference_Heating_Mode_Leaving_Condenser_Water_Temperature: str
    Reference_Heating_Mode_Entering_Condenser_Fluid_Temperature: str
    Heating_Mode_Entering_Chilled_Water_Temperature_Low_Limit: str
    Chilled_Water_Flow_Mode_Type: str
    Design_Chilled_Water_Flow_Rate: str
    Design_Condenser_Water_Flow_Rate: str
    Design_Hot_Water_Flow_Rate: str
    Compressor_Motor_Efficiency: str
    Condenser_Type: str
    Cooling_Mode_Temperature_Curve_Condenser_Water_Independent_Variable: str
    Cooling_Mode_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Cooling_Mode_Electric_Input_to_Cooling_Output_Ratio_Function_of_Temperature_Curve_Name: str
    Cooling_Mode_Electric_Input_to_Cooling_Output_Ratio_Function_of_Part_Load_Ratio_Curve_Name: str
    Cooling_Mode_Cooling_Capacity_Optimum_Part_Load_Ratio: str
    Heating_Mode_Temperature_Curve_Condenser_Water_Independent_Variable: str
    Heating_Mode_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Heating_Mode_Electric_Input_to_Cooling_Output_Ratio_Function_of_Temperature_Curve_Name: str
    Heating_Mode_Electric_Input_to_Cooling_Output_Ratio_Function_of_Part_Load_Ratio_Curve_Name: str
    Heating_Mode_Cooling_Capacity_Optimum_Part_Load_Ratio: str
    Sizing_Factor: str

class CoilCoolingDxType(TypedDict, total=False):
    """"dict for CoilCoolingDx"""
    Name: str
    Evaporator_Inlet_Node_Name: str
    Evaporator_Outlet_Node_Name: str
    Availability_Schedule_Name: str
    Condenser_Zone_Name: str
    Condenser_Inlet_Node_Name: str
    Condenser_Outlet_Node_Name: str
    Performance_Object_Name: str
    Condensate_Collection_Water_Storage_Tank_Name: str
    Evaporative_Condenser_Supply_Water_Storage_Tank_Name: str

class CoilCoolingDxCurvefitOperatingmodeType(TypedDict, total=False):
    """"dict for CoilCoolingDxCurvefitOperatingmode"""
    Name: str
    Rated_Gross_Total_Cooling_Capacity: str
    Rated_Evaporator_Air_Flow_Rate: str
    Rated_Condenser_Air_Flow_Rate: str
    Maximum_Cycling_Rate: str
    Ratio_of_Initial_Moisture_Evaporation_Rate_and_Steady_State_Latent_Capacity: str
    Latent_Capacity_Time_Constant: str
    Nominal_Time_for_Condensate_Removal_to_Begin: str
    Apply_Latent_Degradation_to_Speeds_Greater_than_1: str
    Condenser_Type: str
    Nominal_Evaporative_Condenser_Pump_Power: str
    Nominal_Speed_Number: str
    Speed_1_Name: str
    Speed_2_Name: str
    Speed_3_Name: str
    Speed_4_Name: str
    Speed_5_Name: str
    Speed_6_Name: str
    Speed_7_Name: str
    Speed_8_Name: str
    Speed_9_Name: str
    Speed_10_Name: str

class CoilCoolingDxCurvefitPerformanceType(TypedDict, total=False):
    """"dict for CoilCoolingDxCurvefitPerformance"""
    Name: str
    Crankcase_Heater_Capacity: str
    Crankcase_Heater_Capacity_Function_of_Temperature_Curve_Name: str
    Minimum_Outdoor_DryBulb_Temperature_for_Compressor_Operation: str
    Maximum_Outdoor_DryBulb_Temperature_for_Crankcase_Heater_Operation: str
    Unit_Internal_Static_Air_Pressure: str
    Capacity_Control_Method: str
    Evaporative_Condenser_Basin_Heater_Capacity: str
    Evaporative_Condenser_Basin_Heater_Setpoint_Temperature: str
    Evaporative_Condenser_Basin_Heater_Operating_Schedule_Name: str
    Compressor_Fuel_Type: str
    Base_Operating_Mode: str
    Alternative_Operating_Mode_1: str
    Alternative_Operating_Mode_2: str

class CoilCoolingDxCurvefitSpeedType(TypedDict, total=False):
    """"dict for CoilCoolingDxCurvefitSpeed"""
    Name: str
    Gross_Total_Cooling_Capacity_Fraction: str
    Evaporator_Air_Flow_Rate_Fraction: str
    Condenser_Air_Flow_Rate_Fraction: str
    Gross_Sensible_Heat_Ratio: str
    Gross_Cooling_COP: str
    Active_Fraction_of_Coil_Face_Area: str
    _2017_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    Evaporative_Condenser_Pump_Power_Fraction: str
    Evaporative_Condenser_Effectiveness: str
    Total_Cooling_Capacity_Modifier_Function_of_Temperature_Curve_Name: str
    Total_Cooling_Capacity_Modifier_Function_of_Air_Flow_Fraction_Curve_Name: str
    Energy_Input_Ratio_Modifier_Function_of_Temperature_Curve_Name: str
    Energy_Input_Ratio_Modifier_Function_of_Air_Flow_Fraction_Curve_Name: str
    Part_Load_Fraction_Correlation_Curve_Name: str
    Rated_Waste_Heat_Fraction_of_Power_Input: str
    Waste_Heat_Modifier_Function_of_Temperature_Curve_Name: str
    Sensible_Heat_Ratio_Modifier_Function_of_Temperature_Curve_Name: str
    Sensible_Heat_Ratio_Modifier_Function_of_Flow_Fraction_Curve_Name: str

class CoilCoolingDxMultispeedType(TypedDict, total=False):
    """"dict for CoilCoolingDxMultispeed"""
    Name: str
    Availability_Schedule_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Condenser_Air_Inlet_Node_Name: str
    Condenser_Type: str
    Minimum_Outdoor_DryBulb_Temperature_for_Compressor_Operation: str
    Supply_Water_Storage_Tank_Name: str
    Condensate_Collection_Water_Storage_Tank_Name: str
    Apply_Part_Load_Fraction_to_Speeds_Greater_than_1: str
    Apply_Latent_Degradation_to_Speeds_Greater_than_1: str
    Crankcase_Heater_Capacity: str
    Crankcase_Heater_Capacity_Function_of_Temperature_Curve_Name: str
    Maximum_Outdoor_DryBulb_Temperature_for_Crankcase_Heater_Operation: str
    Basin_Heater_Capacity: str
    Basin_Heater_Setpoint_Temperature: str
    Basin_Heater_Operating_Schedule_Name: str
    Fuel_Type: str
    Number_of_Speeds: str
    Speed_1_Gross_Rated_Total_Cooling_Capacity: str
    Speed_1_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_1_Gross_Rated_Cooling_COP: str
    Speed_1_Rated_Air_Flow_Rate: str
    _2017_Speed_1_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_1_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_1_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_1_Total_Cooling_Capacity_Function_of_Flow_Fraction_Curve_Name: str
    Speed_1_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_1_Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Speed_1_Part_Load_Fraction_Correlation_Curve_Name: str
    Speed_1_Nominal_Time_for_Condensate_Removal_to_Begin: str
    Speed_1_Ratio_of_Initial_Moisture_Evaporation_Rate_and_Steady_State_Latent_Capacity: str
    Speed_1_Maximum_Cycling_Rate: str
    Speed_1_Latent_Capacity_Time_Constant: str
    Speed_1_Rated_Waste_Heat_Fraction_of_Power_Input: str
    Speed_1_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_1_Evaporative_Condenser_Effectiveness: str
    Speed_1_Evaporative_Condenser_Air_Flow_Rate: str
    Speed_1_Rated_Evaporative_Condenser_Pump_Power_Consumption: str
    Speed_2_Gross_Rated_Total_Cooling_Capacity: str
    Speed_2_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_2_Gross_Rated_Cooling_COP: str
    Speed_2_Rated_Air_Flow_Rate: str
    _2017_Speed_2_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_2_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_2_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_2_Total_Cooling_Capacity_Function_of_Flow_Fraction_Curve_Name: str
    Speed_2_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_2_Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Speed_2_Part_Load_Fraction_Correlation_Curve_Name: str
    Speed_2_Nominal_Time_for_Condensate_Removal_to_Begin: str
    Speed_2_Ratio_of_Initial_Moisture_Evaporation_Rate_and_steady_state_Latent_Capacity: str
    Speed_2_Maximum_Cycling_Rate: str
    Speed_2_Latent_Capacity_Time_Constant: str
    Speed_2_Rated_Waste_Heat_Fraction_of_Power_Input: str
    Speed_2_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_2_Evaporative_Condenser_Effectiveness: str
    Speed_2_Evaporative_Condenser_Air_Flow_Rate: str
    Speed_2_Rated_Evaporative_Condenser_Pump_Power_Consumption: str
    Speed_3_Gross_Rated_Total_Cooling_Capacity: str
    Speed_3_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_3_Gross_Rated_Cooling_COP: str
    Speed_3_Rated_Air_Flow_Rate: str
    _2017_Speed_3_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_3_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_3_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_3_Total_Cooling_Capacity_Function_of_Flow_Fraction_Curve_Name: str
    Speed_3_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_3_Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Speed_3_Part_Load_Fraction_Correlation_Curve_Name: str
    Speed_3_Nominal_Time_for_Condensate_Removal_to_Begin: str
    Speed_3_Ratio_of_Initial_Moisture_Evaporation_Rate_and_steady_state_Latent_Capacity: str
    Speed_3_Maximum_Cycling_Rate: str
    Speed_3_Latent_Capacity_Time_Constant: str
    Speed_3_Rated_Waste_Heat_Fraction_of_Power_Input: str
    Speed_3_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_3_Evaporative_Condenser_Effectiveness: str
    Speed_3_Evaporative_Condenser_Air_Flow_Rate: str
    Speed_3_Rated_Evaporative_Condenser_Pump_Power_Consumption: str
    Speed_4_Gross_Rated_Total_Cooling_Capacity: str
    Speed_4_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_4_Gross_Rated_Cooling_COP: str
    Speed_4_Rated_Air_Flow_Rate: str
    _2017_Speed_4_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_4_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_4_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_4_Total_Cooling_Capacity_Function_of_Flow_Fraction_Curve_Name: str
    Speed_4_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_4_Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Speed_4_Part_Load_Fraction_Correlation_Curve_Name: str
    Speed_4_Nominal_Time_for_Condensate_Removal_to_Begin: str
    Speed_4_Ratio_of_Initial_Moisture_Evaporation_Rate_and_steady_state_Latent_Capacity: str
    Speed_4_Maximum_Cycling_Rate: str
    Speed_4_Latent_Capacity_Time_Constant: str
    Speed_4_Rated_Waste_Heat_Fraction_of_Power_Input: str
    Speed_4_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_4_Evaporative_Condenser_Effectiveness: str
    Speed_4_Evaporative_Condenser_Air_Flow_Rate: str
    Speed_4_Rated_Evaporative_Condenser_Pump_Power_Consumption: str
    Zone_Name_for_Condenser_Placement: str

class CoilCoolingDxSinglespeedType(TypedDict, total=False):
    """"dict for CoilCoolingDxSinglespeed"""
    Name: str
    Availability_Schedule_Name: str
    Gross_Rated_Total_Cooling_Capacity: str
    Gross_Rated_Sensible_Heat_Ratio: str
    Gross_Rated_Cooling_COP: str
    Rated_Air_Flow_Rate: str
    _2017_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Total_Cooling_Capacity_Function_of_Flow_Fraction_Curve_Name: str
    Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Part_Load_Fraction_Correlation_Curve_Name: str
    Minimum_Outdoor_DryBulb_Temperature_for_Compressor_Operation: str
    Nominal_Time_for_Condensate_Removal_to_Begin: str
    Ratio_of_Initial_Moisture_Evaporation_Rate_and_Steady_State_Latent_Capacity: str
    Maximum_Cycling_Rate: str
    Latent_Capacity_Time_Constant: str
    Condenser_Air_Inlet_Node_Name: str
    Condenser_Type: str
    Evaporative_Condenser_Effectiveness: str
    Evaporative_Condenser_Air_Flow_Rate: str
    Evaporative_Condenser_Pump_Rated_Power_Consumption: str
    Crankcase_Heater_Capacity: str
    Crankcase_Heater_Capacity_Function_of_Temperature_Curve_Name: str
    Maximum_Outdoor_DryBulb_Temperature_for_Crankcase_Heater_Operation: str
    Supply_Water_Storage_Tank_Name: str
    Condensate_Collection_Water_Storage_Tank_Name: str
    Basin_Heater_Capacity: str
    Basin_Heater_Setpoint_Temperature: str
    Basin_Heater_Operating_Schedule_Name: str
    Sensible_Heat_Ratio_Function_of_Temperature_Curve_Name: str
    Sensible_Heat_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Report_ASHRAE_Standard_127_Performance_Ratings: str
    Zone_Name_for_Condenser_Placement: str

class CoilCoolingDxSinglespeedThermalstorageType(TypedDict, total=False):
    """"dict for CoilCoolingDxSinglespeedThermalstorage"""
    Name: str
    Availability_Schedule_Name: str
    Operating_Mode_Control_Method: str
    Operation_Mode_Control_Schedule_Name: str
    Storage_Type: str
    User_Defined_Fluid_Type: str
    Fluid_Storage_Volume: str
    Ice_Storage_Capacity: str
    Storage_Capacity_Sizing_Factor: str
    Storage_Tank_Ambient_Temperature_Node_Name: str
    Storage_Tank_to_Ambient_Uvalue_Times_Area_Heat_Transfer_Coefficient: str
    Fluid_Storage_Tank_Rating_Temperature: str
    Rated_Evaporator_Air_Flow_Rate: str
    Evaporator_Air_Inlet_Node_Name: str
    Evaporator_Air_Outlet_Node_Name: str
    Cooling_Only_Mode_Available: str
    Cooling_Only_Mode_Rated_Total_Evaporator_Cooling_Capacity: str
    Cooling_Only_Mode_Rated_Sensible_Heat_Ratio: str
    Cooling_Only_Mode_Rated_COP: str
    Cooling_Only_Mode_Total_Evaporator_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Cooling_Only_Mode_Total_Evaporator_Cooling_Capacity_Function_of_Flow_Fraction_Curve_Name: str
    Cooling_Only_Mode_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Cooling_Only_Mode_Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Cooling_Only_Mode_Part_Load_Fraction_Correlation_Curve_Name: str
    Cooling_Only_Mode_Sensible_Heat_Ratio_Function_of_Temperature_Curve_Name: str
    Cooling_Only_Mode_Sensible_Heat_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Cooling_And_Charge_Mode_Available: str
    Cooling_And_Charge_Mode_Rated_Total_Evaporator_Cooling_Capacity: str
    Cooling_And_Charge_Mode_Capacity_Sizing_Factor: str
    Cooling_And_Charge_Mode_Rated_Storage_Charging_Capacity: str
    Cooling_And_Charge_Mode_Storage_Capacity_Sizing_Factor: str
    Cooling_And_Charge_Mode_Rated_Sensible_Heat_Ratio: str
    Cooling_And_Charge_Mode_Cooling_Rated_COP: str
    Cooling_And_Charge_Mode_Charging_Rated_COP: str
    Cooling_And_Charge_Mode_Total_Evaporator_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Cooling_And_Charge_Mode_Total_Evaporator_Cooling_Capacity_Function_of_Flow_Fraction_Curve_Name: str
    Cooling_And_Charge_Mode_Evaporator_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Cooling_And_Charge_Mode_Evaporator_Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Cooling_And_Charge_Mode_Evaporator_Part_Load_Fraction_Correlation_Curve_Name: str
    Cooling_And_Charge_Mode_Storage_Charge_Capacity_Function_of_Temperature_Curve_Name: str
    Cooling_And_Charge_Mode_Storage_Charge_Capacity_Function_of_Total_Evaporator_PLR_Curve_Name: str
    Cooling_And_Charge_Mode_Storage_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Cooling_And_Charge_Mode_Storage_Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Cooling_And_Charge_Mode_Storage_Energy_Part_Load_Fraction_Correlation_Curve_Name: str
    Cooling_And_Charge_Mode_Sensible_Heat_Ratio_Function_of_Temperature_Curve_Name: str
    Cooling_And_Charge_Mode_Sensible_Heat_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Cooling_And_Discharge_Mode_Available: str
    Cooling_And_Discharge_Mode_Rated_Total_Evaporator_Cooling_Capacity: str
    Cooling_And_Discharge_Mode_Evaporator_Capacity_Sizing_Factor: str
    Cooling_And_Discharge_Mode_Rated_Storage_Discharging_Capacity: str
    Cooling_And_Discharge_Mode_Storage_Discharge_Capacity_Sizing_Factor: str
    Cooling_And_Discharge_Mode_Rated_Sensible_Heat_Ratio: str
    Cooling_And_Discharge_Mode_Cooling_Rated_COP: str
    Cooling_And_Discharge_Mode_Discharging_Rated_COP: str
    Cooling_And_Discharge_Mode_Total_Evaporator_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Cooling_And_Discharge_Mode_Total_Evaporator_Cooling_Capacity_Function_of_Flow_Fraction_Curve_Name: str
    Cooling_And_Discharge_Mode_Evaporator_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Cooling_And_Discharge_Mode_Evaporator_Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Cooling_And_Discharge_Mode_Evaporator_Part_Load_Fraction_Correlation_Curve_Name: str
    Cooling_And_Discharge_Mode_Storage_Discharge_Capacity_Function_of_Temperature_Curve_Name: str
    Cooling_And_Discharge_Mode_Storage_Discharge_Capacity_Function_of_Flow_Fraction_Curve_Name: str
    Cooling_And_Discharge_Mode_Storage_Discharge_Capacity_Function_of_Total_Evaporator_PLR_Curve_Name: str
    Cooling_And_Discharge_Mode_Storage_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Cooling_And_Discharge_Mode_Storage_Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Cooling_And_Discharge_Mode_Storage_Energy_Part_Load_Fraction_Correlation_Curve_Name: str
    Cooling_And_Discharge_Mode_Sensible_Heat_Ratio_Function_of_Temperature_Curve_Name: str
    Cooling_And_Discharge_Mode_Sensible_Heat_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Charge_Only_Mode_Available: str
    Charge_Only_Mode_Rated_Storage_Charging_Capacity: str
    Charge_Only_Mode_Capacity_Sizing_Factor: str
    Charge_Only_Mode_Charging_Rated_COP: str
    Charge_Only_Mode_Storage_Charge_Capacity_Function_of_Temperature_Curve_Name: str
    Charge_Only_Mode_Storage_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Discharge_Only_Mode_Available: str
    Discharge_Only_Mode_Rated_Storage_Discharging_Capacity: str
    Discharge_Only_Mode_Capacity_Sizing_Factor: str
    Discharge_Only_Mode_Rated_Sensible_Heat_Ratio: str
    Discharge_Only_Mode_Rated_COP: str
    Discharge_Only_Mode_Storage_Discharge_Capacity_Function_of_Temperature_Curve_Name: str
    Discharge_Only_Mode_Storage_Discharge_Capacity_Function_of_Flow_Fraction_Curve_Name: str
    Discharge_Only_Mode_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Discharge_Only_Mode_Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Discharge_Only_Mode_Part_Load_Fraction_Correlation_Curve_Name: str
    Discharge_Only_Mode_Sensible_Heat_Ratio_Function_of_Temperature_Curve_Name: str
    Discharge_Only_Mode_Sensible_Heat_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Ancillary_Electric_Power: str
    Cold_Weather_Operation_Minimum_Outdoor_Air_Temperature: str
    Cold_Weather_Operation_Ancillary_Power: str
    Condenser_Air_Inlet_Node_Name: str
    Condenser_Air_Outlet_Node_Name: str
    Condenser_Design_Air_Flow_Rate: str
    Condenser_Air_Flow_Sizing_Factor: str
    Condenser_Type: str
    Evaporative_Condenser_Effectiveness: str
    Evaporative_Condenser_Pump_Rated_Power_Consumption: str
    Basin_Heater_Capacity: str
    Basin_Heater_Setpoint_Temperature: str
    Basin_Heater_Availability_Schedule_Name: str
    Supply_Water_Storage_Tank_Name: str
    Condensate_Collection_Water_Storage_Tank_Name: str
    Storage_Tank_Plant_Connection_Inlet_Node_Name: str
    Storage_Tank_Plant_Connection_Outlet_Node_Name: str
    Storage_Tank_Plant_Connection_Design_Flow_Rate: str
    Storage_Tank_Plant_Connection_Heat_Transfer_Effectiveness: str
    Storage_Tank_Minimum_Operating_Limit_Fluid_Temperature: str
    Storage_Tank_Maximum_Operating_Limit_Fluid_Temperature: str

class CoilCoolingDxTwospeedType(TypedDict, total=False):
    """"dict for CoilCoolingDxTwospeed"""
    Name: str
    Availability_Schedule_Name: str
    High_Speed_Gross_Rated_Total_Cooling_Capacity: str
    High_Speed_Rated_Sensible_Heat_Ratio: str
    High_Speed_Gross_Rated_Cooling_COP: str
    High_Speed_Rated_Air_Flow_Rate: str
    High_Speed_2017_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    High_Speed_2023_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    Unit_Internal_Static_Air_Pressure: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Total_Cooling_Capacity_Function_of_Flow_Fraction_Curve_Name: str
    Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Part_Load_Fraction_Correlation_Curve_Name: str
    Low_Speed_Gross_Rated_Total_Cooling_Capacity: str
    Low_Speed_Gross_Rated_Sensible_Heat_Ratio: str
    Low_Speed_Gross_Rated_Cooling_COP: str
    Low_Speed_Rated_Air_Flow_Rate: str
    Low_Speed_2017_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    Low_Speed_2023_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    Low_Speed_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Low_Speed_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Condenser_Air_Inlet_Node_Name: str
    Condenser_Type: str
    Minimum_Outdoor_DryBulb_Temperature_for_Compressor_Operation: str
    High_Speed_Evaporative_Condenser_Effectiveness: str
    High_Speed_Evaporative_Condenser_Air_Flow_Rate: str
    High_Speed_Evaporative_Condenser_Pump_Rated_Power_Consumption: str
    Low_Speed_Evaporative_Condenser_Effectiveness: str
    Low_Speed_Evaporative_Condenser_Air_Flow_Rate: str
    Low_Speed_Evaporative_Condenser_Pump_Rated_Power_Consumption: str
    Supply_Water_Storage_Tank_Name: str
    Condensate_Collection_Water_Storage_Tank_Name: str
    Basin_Heater_Capacity: str
    Basin_Heater_Setpoint_Temperature: str
    Basin_Heater_Operating_Schedule_Name: str
    Sensible_Heat_Ratio_Function_of_Temperature_Curve_Name: str
    Sensible_Heat_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Low_Speed_Sensible_Heat_Ratio_Function_of_Temperature_Curve_Name: str
    Low_Speed_Sensible_Heat_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Zone_Name_for_Condenser_Placement: str

class CoilCoolingDxTwostagewithhumiditycontrolmodeType(TypedDict, total=False):
    """"dict for CoilCoolingDxTwostagewithhumiditycontrolmode"""
    Name: str
    Availability_Schedule_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Crankcase_Heater_Capacity: str
    Crankcase_Heater_Capacity_Function_of_Temperature_Curve_Name: str
    Maximum_Outdoor_DryBulb_Temperature_for_Crankcase_Heater_Operation: str
    Number_of_Capacity_Stages: str
    Number_of_Enhanced_Dehumidification_Modes: str
    Normal_Mode_Stage_1_Coil_Performance_Object_Type: str
    Normal_Mode_Stage_1_Coil_Performance_Name: str
    Normal_Mode_Stage_12_Coil_Performance_Object_Type: str
    Normal_Mode_Stage_12_Coil_Performance_Name: str
    Dehumidification_Mode_1_Stage_1_Coil_Performance_Object_Type: str
    Dehumidification_Mode_1_Stage_1_Coil_Performance_Name: str
    Dehumidification_Mode_1_Stage_12_Coil_Performance_Object_Type: str
    Dehumidification_Mode_1_Stage_12_Coil_Performance_Name: str
    Supply_Water_Storage_Tank_Name: str
    Condensate_Collection_Water_Storage_Tank_Name: str
    Minimum_Outdoor_DryBulb_Temperature_for_Compressor_Operation: str
    Basin_Heater_Capacity: str
    Basin_Heater_Setpoint_Temperature: str
    Basin_Heater_Operating_Schedule_Name: str

class CoilCoolingDxVariablerefrigerantflowType(TypedDict, total=False):
    """"dict for CoilCoolingDxVariablerefrigerantflow"""
    Name: str
    Availability_Schedule_Name: str
    Gross_Rated_Total_Cooling_Capacity: str
    Gross_Rated_Sensible_Heat_Ratio: str
    Rated_Air_Flow_Rate: str
    Cooling_Capacity_Ratio_Modifier_Function_of_Temperature_Curve_Name: str
    Cooling_Capacity_Modifier_Curve_Function_of_Flow_Fraction_Name: str
    Coil_Air_Inlet_Node: str
    Coil_Air_Outlet_Node: str
    Name_of_Water_Storage_Tank_for_Condensate_Collection: str

class CoilCoolingDxVariablerefrigerantflowFluidtemperaturecontrolType(TypedDict, total=False):
    """"dict for CoilCoolingDxVariablerefrigerantflowFluidtemperaturecontrol"""
    Name: str
    Availability_Schedule_Name: str
    Coil_Air_Inlet_Node: str
    Coil_Air_Outlet_Node: str
    Rated_Total_Cooling_Capacity: str
    Rated_Sensible_Heat_Ratio: str
    Indoor_Unit_Reference_Superheating: str
    Indoor_Unit_Evaporating_Temperature_Function_of_Superheating_Curve_Name: str
    Name_of_Water_Storage_Tank_for_Condensate_Collection: str

class CoilCoolingDxVariablespeedType(TypedDict, total=False):
    """"dict for CoilCoolingDxVariablespeed"""
    Name: str
    Indoor_Air_Inlet_Node_Name: str
    Indoor_Air_Outlet_Node_Name: str
    Number_of_Speeds: str
    Nominal_Speed_Level: str
    Gross_Rated_Total_Cooling_Capacity_At_Selected_Nominal_Speed_Level: str
    Rated_Air_Flow_Rate_At_Selected_Nominal_Speed_Level: str
    Nominal_Time_for_Condensate_to_Begin_Leaving_the_Coil: str
    Initial_Moisture_Evaporation_Rate_Divided_by_SteadyState_AC_Latent_Capacity: str
    Maximum_Cycling_Rate: str
    Latent_Capacity_Time_Constant: str
    Fan_Delay_Time: str
    Energy_Part_Load_Fraction_Curve_Name: str
    Condenser_Air_Inlet_Node_Name: str
    Condenser_Type: str
    Evaporative_Condenser_Pump_Rated_Power_Consumption: str
    Crankcase_Heater_Capacity: str
    Crankcase_Heater_Capacity_Function_of_Temperature_Curve_Name: str
    Maximum_Outdoor_DryBulb_Temperature_for_Crankcase_Heater_Operation: str
    Minimum_Outdoor_DryBulb_Temperature_for_Compressor_Operation: str
    Supply_Water_Storage_Tank_Name: str
    Condensate_Collection_Water_Storage_Tank_Name: str
    Basin_Heater_Capacity: str
    Basin_Heater_Setpoint_Temperature: str
    Basin_Heater_Operating_Schedule_Name: str
    Speed_1_Reference_Unit_Gross_Rated_Total_Cooling_Capacity: str
    Speed_1_Reference_Unit_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_1_Reference_Unit_Gross_Rated_Cooling_COP: str
    Speed_1_Reference_Unit_Rated_Air_Flow_Rate: str
    _2017_Speed_1_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_1_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_1_Reference_Unit_Rated_Condenser_Air_Flow_Rate: str
    Speed_1_Reference_Unit_Rated_Pad_Effectiveness_of_Evap_Precooling: str
    Speed_1_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_1_Total_Cooling_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_1_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_1_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_2_Reference_Unit_Gross_Rated_Total_Cooling_Capacity: str
    Speed_2_Reference_Unit_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_2_Reference_Unit_Gross_Rated_Cooling_COP: str
    Speed_2_Reference_Unit_Rated_Air_Flow_Rate: str
    _2017_Speed_2_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_2_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_2_Reference_Unit_Rated_Condenser_Air_Flow_Rate: str
    Speed_2_Reference_Unit_Rated_Pad_Effectiveness_of_Evap_Precooling: str
    Speed_2_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_2_Total_Cooling_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_2_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_2_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_3_Reference_Unit_Gross_Rated_Total_Cooling_Capacity: str
    Speed_3_Reference_Unit_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_3_Reference_Unit_Gross_Rated_Cooling_COP: str
    Speed_3_Reference_Unit_Rated_Air_Flow_Rate: str
    _2017_Speed_3_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_3_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_3_Reference_Unit_Rated_Condenser_Air_Flow_Rate: str
    Speed_3_Reference_Unit_Rated_Pad_Effectiveness_of_Evap_Precooling: str
    Speed_3_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_3_Total_Cooling_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_3_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_3_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_4_Reference_Unit_Gross_Rated_Total_Cooling_Capacity: str
    Speed_4_Reference_Unit_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_4_Reference_Unit_Gross_Rated_Cooling_COP: str
    Speed_4_Reference_Unit_Rated_Air_Flow_Rate: str
    _2017_Speed_4_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_4_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_4_Reference_Unit_Rated_Condenser_Air_Flow_Rate: str
    Speed_4_Reference_Unit_Rated_Pad_Effectiveness_of_Evap_Precooling: str
    Speed_4_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_4_Total_Cooling_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_4_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_4_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_5_Reference_Unit_Gross_Rated_Total_Cooling_Capacity: str
    Speed_5_Reference_Unit_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_5_Reference_Unit_Gross_Rated_Cooling_COP: str
    Speed_5_Reference_Unit_Rated_Air_Flow_Rate: str
    _2017_Speed_5_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_5_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_5_Reference_Unit_Rated_Condenser_Air_Flow_Rate: str
    Speed_5_Reference_Unit_Rated_Pad_Effectiveness_of_Evap_Precooling: str
    Speed_5_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_5_Total_Cooling_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_5_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_5_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_6_Reference_Unit_Gross_Rated_Total_Cooling_Capacity: str
    Speed_6_Reference_Unit_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_6_Reference_Unit_Gross_Rated_Cooling_COP: str
    Speed_6_Reference_Unit_Rated_Air_Flow_Rate: str
    _2017_Speed_6_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_6_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_6_Reference_Unit_Condenser_Air_Flow_Rate: str
    Speed_6_Reference_Unit_Rated_Pad_Effectiveness_of_Evap_Precooling: str
    Speed_6_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_6_Total_Cooling_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_6_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_6_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_7_Reference_Unit_Gross_Rated_Total_Cooling_Capacity: str
    Speed_7_Reference_Unit_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_7_Reference_Unit_Gross_Rated_Cooling_COP: str
    Speed_7_Reference_Unit_Rated_Air_Flow_Rate: str
    _2017_Speed_7_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_7_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_7_Reference_Unit_Condenser_Flow_Rate: str
    Speed_7_Reference_Unit_Rated_Pad_Effectiveness_of_Evap_Precooling: str
    Speed_7_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_7_Total_Cooling_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_7_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_7_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_8_Reference_Unit_Gross_Rated_Total_Cooling_Capacity: str
    Speed_8_Reference_Unit_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_8_Reference_Unit_Gross_Rated_Cooling_COP: str
    Speed_8_Reference_Unit_Rated_Air_Flow_Rate: str
    _2017_Speed_8_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_8_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_8_Reference_Unit_Condenser_Air_Flow_Rate: str
    Speed_8_Reference_Unit_Rated_Pad_Effectiveness_of_Evap_Precooling: str
    Speed_8_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_8_Total_Cooling_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_8_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_8_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_9_Reference_Unit_Gross_Rated_Total_Cooling_Capacity: str
    Speed_9_Reference_Unit_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_9_Reference_Unit_Gross_Rated_Cooling_COP: str
    Speed_9_Reference_Unit_Rated_Air_Flow_Rate: str
    _2017_Speed_9_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_9_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_9_Reference_Unit_Condenser_Air_Flow_Rate: str
    Speed_9_Reference_Unit_Rated_Pad_Effectiveness_of_Evap_Precooling: str
    Speed_9_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_9_Total_Cooling_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_9_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_9_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_10_Reference_Unit_Gross_Rated_Total_Cooling_Capacity: str
    Speed_10_Reference_Unit_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_10_Reference_Unit_Gross_Rated_Cooling_COP: str
    Speed_10_Reference_Unit_Rated_Air_Flow_Rate: str
    _2017_Speed_10_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_10_Rated_Evaporator_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_10_Reference_Unit_Condenser_Air_Flow_Rate: str
    Speed_10_Reference_Unit_Rated_Pad_Effectiveness_of_Evap_Precooling: str
    Speed_10_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_10_Total_Cooling_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_10_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_10_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str

class CoilCoolingWaterType(TypedDict, total=False):
    """"dict for CoilCoolingWater"""
    Name: str
    Availability_Schedule_Name: str
    Design_Water_Flow_Rate: str
    Design_Air_Flow_Rate: str
    Design_Inlet_Water_Temperature: str
    Design_Inlet_Air_Temperature: str
    Design_Outlet_Air_Temperature: str
    Design_Inlet_Air_Humidity_Ratio: str
    Design_Outlet_Air_Humidity_Ratio: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Type_of_Analysis: str
    Heat_Exchanger_Configuration: str
    Condensate_Collection_Water_Storage_Tank_Name: str
    Design_Water_Temperature_Difference: str

class CoilCoolingWaterDetailedgeometryType(TypedDict, total=False):
    """"dict for CoilCoolingWaterDetailedgeometry"""
    Name: str
    Availability_Schedule_Name: str
    Maximum_Water_Flow_Rate: str
    Tube_Outside_Surface_Area: str
    Total_Tube_Inside_Area: str
    Fin_Surface_Area: str
    Minimum_Airflow_Area: str
    Coil_Depth: str
    Fin_Diameter: str
    Fin_Thickness: str
    Tube_Inside_Diameter: str
    Tube_Outside_Diameter: str
    Tube_Thermal_Conductivity: str
    Fin_Thermal_Conductivity: str
    Fin_Spacing: str
    Tube_Depth_Spacing: str
    Number_of_Tube_Rows: str
    Number_of_Tubes_per_Row: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Condensate_Collection_Water_Storage_Tank_Name: str
    Design_Water_Temperature_Difference: str
    Design_Inlet_Water_Temperature: str

class CoilCoolingWatertoairheatpumpEquationfitType(TypedDict, total=False):
    """"dict for CoilCoolingWatertoairheatpumpEquationfit"""
    Name: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Rated_Air_Flow_Rate: str
    Rated_Water_Flow_Rate: str
    Gross_Rated_Total_Cooling_Capacity: str
    Gross_Rated_Sensible_Cooling_Capacity: str
    Gross_Rated_Cooling_COP: str
    Rated_Entering_Water_Temperature: str
    Rated_Entering_Air_DryBulb_Temperature: str
    Rated_Entering_Air_WetBulb_Temperature: str
    Total_Cooling_Capacity_Curve_Name: str
    Sensible_Cooling_Capacity_Curve_Name: str
    Cooling_Power_Consumption_Curve_Name: str
    Part_Load_Fraction_Correlation_Curve_Name: str
    Nominal_Time_for_Condensate_Removal_to_Begin: str
    Ratio_of_Initial_Moisture_Evaporation_Rate_and_Steady_State_Latent_Capacity: str
    Maximum_Cycling_Rate: str
    Latent_Capacity_Time_Constant: str
    Fan_Delay_Time: str

class CoilCoolingWatertoairheatpumpParameterestimationType(TypedDict, total=False):
    """"dict for CoilCoolingWatertoairheatpumpParameterestimation"""
    Name: str
    Compressor_Type: str
    Refrigerant_Type: str
    Design_Source_Side_Flow_Rate: str
    Nominal_Cooling_Coil_Capacity: str
    Nominal_Time_for_Condensate_Removal_to_Begin: str
    Ratio_of_Initial_Moisture_Evaporation_Rate_and_Steady_State_Latent_Capacity: str
    High_Pressure_Cutoff: str
    Low_Pressure_Cutoff: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Load_Side_Total_Heat_Transfer_Coefficient: str
    Load_Side_Outside_Surface_Heat_Transfer_Coefficient: str
    Superheat_Temperature_at_the_Evaporator_Outlet: str
    Compressor_Power_Losses: str
    Compressor_Efficiency: str
    Compressor_Piston_Displacement: str
    Compressor_SuctionDischarge_Pressure_Drop: str
    Compressor_Clearance_Factor: str
    Refrigerant_Volume_Flow_Rate: str
    Volume_Ratio: str
    Leak_Rate_Coefficient: str
    Source_Side_Heat_Transfer_Coefficient: str
    Source_Side_Heat_Transfer_Resistance1: str
    Source_Side_Heat_Transfer_Resistance2: str
    Part_Load_Fraction_Correlation_Curve_Name: str
    Maximum_Cycling_Rate: str
    Latent_Capacity_Time_Constant: str
    Fan_Delay_Time: str

class CoilCoolingWatertoairheatpumpVariablespeedequationfitType(TypedDict, total=False):
    """"dict for CoilCoolingWatertoairheatpumpVariablespeedequationfit"""
    Name: str
    WatertoRefrigerant_HX_Water_Inlet_Node_Name: str
    WatertoRefrigerant_HX_Water_Outlet_Node_Name: str
    Indoor_Air_Inlet_Node_Name: str
    Indoor_Air_Outlet_Node_Name: str
    Number_of_Speeds: str
    Nominal_Speed_Level: str
    Gross_Rated_Total_Cooling_Capacity_At_Selected_Nominal_Speed_Level: str
    Rated_Air_Flow_Rate_At_Selected_Nominal_Speed_Level: str
    Rated_Water_Flow_Rate_At_Selected_Nominal_Speed_Level: str
    Nominal_Time_for_Condensate_to_Begin_Leaving_the_Coil: str
    Initial_Moisture_Evaporation_Rate_Divided_by_SteadyState_AC_Latent_Capacity: str
    Maximum_Cycling_Rate: str
    Latent_Capacity_Time_Constant: str
    Fan_Delay_Time: str
    Flag_for_Using_Hot_Gas_Reheat_0_or_1: str
    Energy_Part_Load_Fraction_Curve_Name: str
    Speed_1_Reference_Unit_Gross_Rated_Total_Cooling_Capacity: str
    Speed_1_Reference_Unit_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_1_Reference_Unit_Gross_Rated_Cooling_COP: str
    Speed_1_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_1_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_1_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_1_Total_Cooling_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_1_Total_Cooling_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_1_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_1_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_1_Energy_Input_Ratio_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_1_Reference_Unit_Waste_Heat_Fraction_of_Input_Power_At_Rated_Conditions: str
    Speed_1_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_2_Reference_Unit_Gross_Rated_Total_Cooling_Capacity: str
    Speed_2_Reference_Unit_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_2_Reference_Unit_Gross_Rated_Cooling_COP: str
    Speed_2_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_2_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_2_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_2_Total_Cooling_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_2_Total_Cooling_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_2_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_2_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_2_Energy_Input_Ratio_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_2_Reference_Unit_Waste_Heat_Fraction_of_Input_Power_At_Rated_Conditions: str
    Speed_2_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_3_Reference_Unit_Gross_Rated_Total_Cooling_Capacity: str
    Speed_3_Reference_Unit_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_3_Reference_Unit_Gross_Rated_Cooling_COP: str
    Speed_3_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_3_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_3_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_3_Total_Cooling_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_3_Total_Cooling_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_3_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_3_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_3_Energy_Input_Ratio_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_3_Reference_Unit_Waste_Heat_Fraction_of_Input_Power_At_Rated_Conditions: str
    Speed_3_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_4_Reference_Unit_Gross_Rated_Total_Cooling_Capacity: str
    Speed_4_Reference_Unit_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_4_Reference_Unit_Gross_Rated_Cooling_COP: str
    Speed_4_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_4_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_4_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_4_Total_Cooling_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_4_Total_Cooling_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_4_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_4_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_4_Energy_Input_Ratio_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_4_Reference_Unit_Waste_Heat_Fraction_of_Input_Power_At_Rated_Conditions: str
    Speed_4_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_5_Reference_Unit_Gross_Rated_Total_Cooling_Capacity: str
    Speed_5_Reference_Unit_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_5_Reference_Unit_Gross_Rated_Cooling_COP: str
    Speed_5_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_5_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_5_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_5_Total_Cooling_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_5_Total_Cooling_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_5_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_5_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_5_Energy_Input_Ratio_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_5_Reference_Unit_Waste_Heat_Fraction_of_Input_Power_At_Rated_Conditions: str
    Speed_5_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_6_Reference_Unit_Gross_Rated_Total_Cooling_Capacity: str
    Speed_6_Reference_Unit_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_6_Reference_Unit_Gross_Rated_Cooling_COP: str
    Speed_6_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_6_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_6_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_6_Total_Cooling_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_6_Total_Cooling_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_6_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_6_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_6_Energy_Input_Ratio_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_6_Reference_Unit_Waste_Heat_Fraction_of_Input_Power_At_Rated_Conditions: str
    Speed_6_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_7_Reference_Unit_Gross_Rated_Total_Cooling_Capacity: str
    Speed_7_Reference_Unit_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_7_Reference_Unit_Gross_Rated_Cooling_COP: str
    Speed_7_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_7_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_7_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_7_Total_Cooling_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_7_Total_Cooling_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_7_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_7_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_7_Energy_Input_Ratio_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_7_Reference_Unit_Waste_Heat_Fraction_of_Input_Power_At_Rated_Conditions: str
    Speed_7_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_8_Reference_Unit_Gross_Rated_Total_Cooling_Capacity: str
    Speed_8_Reference_Unit_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_8_Reference_Unit_Gross_Rated_Cooling_COP: str
    Speed_8_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_8_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_8_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_8_Total_Cooling_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_8_Total_Cooling_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_8_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_8_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_8_Energy_Input_Ratio_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_8_Reference_Unit_Waste_Heat_Fraction_of_Input_Power_At_Rated_Conditions: str
    Speed_8_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_9_Reference_Unit_Gross_Rated_Total_Cooling_Capacity: str
    Speed_9_Reference_Unit_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_9_Reference_Unit_Gross_Rated_Cooling_COP: str
    Speed_9_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_9_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_9_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_9_Total_Cooling_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_9_Total_Cooling_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_9_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_9_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_9_Energy_Input_Ratio_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_9_Reference_Unit_Waste_Heat_Fraction_of_Input_Power_At_Rated_Conditions: str
    Speed_9_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_10_Reference_Unit_Gross_Rated_Total_Cooling_Capacity: str
    Speed_10_Reference_Unit_Gross_Rated_Sensible_Heat_Ratio: str
    Speed_10_Reference_Unit_Gross_Rated_Cooling_COP: str
    Speed_10_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_10_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_10_Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_10_Total_Cooling_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_10_Total_Cooling_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_10_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_10_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_10_Energy_Input_Ratio_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_10_Reference_Unit_Waste_Heat_Fraction_of_Input_Power_At_Rated_Conditions: str
    Speed_10_Waste_Heat_Function_of_Temperature_Curve_Name: str

class CoilHeatingDesuperheaterType(TypedDict, total=False):
    """"dict for CoilHeatingDesuperheater"""
    Name: str
    Availability_Schedule_Name: str
    Heat_Reclaim_Recovery_Efficiency: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Heating_Source_Object_Type: str
    Heating_Source_Name: str
    Temperature_Setpoint_Node_Name: str
    On_Cycle_Parasitic_Electric_Load: str

class CoilHeatingDxMultispeedType(TypedDict, total=False):
    """"dict for CoilHeatingDxMultispeed"""
    Name: str
    Availability_Schedule_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Minimum_Outdoor_DryBulb_Temperature_for_Compressor_Operation: str
    Outdoor_DryBulb_Temperature_to_Turn_On_Compressor: str
    Crankcase_Heater_Capacity: str
    Crankcase_Heater_Capacity_Function_of_Temperature_Curve_Name: str
    Maximum_Outdoor_DryBulb_Temperature_for_Crankcase_Heater_Operation: str
    Defrost_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Maximum_Outdoor_DryBulb_Temperature_for_Defrost_Operation: str
    Defrost_Strategy: str
    Defrost_Control: str
    Defrost_Time_Period_Fraction: str
    Resistive_Defrost_Heater_Capacity: str
    Apply_Part_Load_Fraction_to_Speeds_Greater_than_1: str
    Fuel_Type: str
    Region_number_for_Calculating_HSPF: str
    Number_of_Speeds: str
    Speed_1_Gross_Rated_Heating_Capacity: str
    Speed_1_Gross_Rated_Heating_COP: str
    Speed_1_Rated_Air_Flow_Rate: str
    _2017_Speed_1_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_1_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_1_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_1_Heating_Capacity_Function_of_Flow_Fraction_Curve_Name: str
    Speed_1_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_1_Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Speed_1_Part_Load_Fraction_Correlation_Curve_Name: str
    Speed_1_Rated_Waste_Heat_Fraction_of_Power_Input: str
    Speed_1_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_2_Gross_Rated_Heating_Capacity: str
    Speed_2_Gross_Rated_Heating_COP: str
    Speed_2_Rated_Air_Flow_Rate: str
    _2017_Speed_2_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_2_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_2_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_2_Heating_Capacity_Function_of_Flow_Fraction_Curve_Name: str
    Speed_2_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_2_Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Speed_2_Part_Load_Fraction_Correlation_Curve_Name: str
    Speed_2_Rated_Waste_Heat_Fraction_of_Power_Input: str
    Speed_2_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_3_Gross_Rated_Heating_Capacity: str
    Speed_3_Gross_Rated_Heating_COP: str
    Speed_3_Rated_Air_Flow_Rate: str
    _2017_Speed_3_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_3_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_3_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_3_Heating_Capacity_Function_of_Flow_Fraction_Curve_Name: str
    Speed_3_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_3_Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Speed_3_Part_Load_Fraction_Correlation_Curve_Name: str
    Speed_3_Rated_Waste_Heat_Fraction_of_Power_Input: str
    Speed_3_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_4_Gross_Rated_Heating_Capacity: str
    Speed_4_Gross_Rated_Heating_COP: str
    Speed_4_Rated_Air_Flow_Rate: str
    _2017_Speed_4_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_4_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_4_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_4_Heating_Capacity_Function_of_Flow_Fraction_Curve_Name: str
    Speed_4_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_4_Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Speed_4_Part_Load_Fraction_Correlation_Curve_Name: str
    Speed_4_Rated_Waste_Heat_Fraction_of_Power_Input: str
    Speed_4_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Zone_Name_for_Evaporator_Placement: str
    Speed_1_Secondary_Coil_Air_Flow_Rate: str
    Speed_1_Secondary_Coil_Fan_Flow_Scaling_Factor: str
    Speed_1_Nominal_Sensible_Heat_Ratio_of_Secondary_Coil: str
    Speed_1_Sensible_Heat_Ratio_Modifier_Function_of_Temperature_Curve_Name: str
    Speed_1_Sensible_Heat_Ratio_Modifier_Function_of_Flow_Fraction_Curve_Name: str
    Speed_2_Secondary_Coil_Air_Flow_Rate: str
    Speed_2_Secondary_Coil_Fan_Flow_Scaling_Factor: str
    Speed_2_Nominal_Sensible_Heat_Ratio_of_Secondary_Coil: str
    Speed_2_Sensible_Heat_Ratio_Modifier_Function_of_Temperature_Curve_Name: str
    Speed_2_Sensible_Heat_Ratio_Modifier_Function_of_Flow_Fraction_Curve_Name: str
    Speed_3_Secondary_Coil_Air_Flow_Rate: str
    Speed_3_Secondary_Coil_Fan_Flow_Scaling_Factor: str
    Speed_3_Nominal_Sensible_Heat_Ratio_of_Secondary_Coil: str
    Speed_3_Sensible_Heat_Ratio_Modifier_Function_of_Temperature_Curve_Name: str
    Speed_3_Sensible_Heat_Ratio_Modifier_Function_of_Flow_Fraction_Curve_Name: str
    Speed_4_Secondary_Coil_Air_Flow_Rate: str
    Speed_4_Secondary_Coil_Fan_Flow_Scaling_Factor: str
    Speed_4_Nominal_Sensible_Heat_Ratio_of_Secondary_Coil: str
    Speed_4_Sensible_Heat_Ratio_Modifier_Function_of_Temperature_Curve_Name: str
    Speed_4_Sensible_Heat_Ratio_Modifier_Function_of_Flow_Fraction_Curve_Name: str

class CoilHeatingDxSinglespeedType(TypedDict, total=False):
    """"dict for CoilHeatingDxSinglespeed"""
    Name: str
    Availability_Schedule_Name: str
    Gross_Rated_Heating_Capacity: str
    Gross_Rated_Heating_COP: str
    Rated_Air_Flow_Rate: str
    _2017_Rated_Supply_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Rated_Supply_Fan_Power_Per_Volume_Flow_Rate: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Heating_Capacity_Function_of_Flow_Fraction_Curve_Name: str
    Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Part_Load_Fraction_Correlation_Curve_Name: str
    Defrost_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Minimum_Outdoor_DryBulb_Temperature_for_Compressor_Operation: str
    Outdoor_DryBulb_Temperature_to_Turn_On_Compressor: str
    Maximum_Outdoor_DryBulb_Temperature_for_Defrost_Operation: str
    Crankcase_Heater_Capacity: str
    Crankcase_Heater_Capacity_Function_of_Temperature_Curve_Name: str
    Maximum_Outdoor_DryBulb_Temperature_for_Crankcase_Heater_Operation: str
    Defrost_Strategy: str
    Defrost_Control: str
    Defrost_Time_Period_Fraction: str
    Resistive_Defrost_Heater_Capacity: str
    Region_number_for_calculating_HSPF: str
    Evaporator_Air_Inlet_Node_Name: str
    Zone_Name_for_Evaporator_Placement: str
    Secondary_Coil_Air_Flow_Rate: str
    Secondary_Coil_Fan_Flow_Scaling_Factor: str
    Nominal_Sensible_Heat_Ratio_of_Secondary_Coil: str
    Sensible_Heat_Ratio_Modifier_Function_of_Temperature_Curve_Name: str
    Sensible_Heat_Ratio_Modifier_Function_of_Flow_Fraction_Curve_Name: str

class CoilHeatingDxVariablerefrigerantflowType(TypedDict, total=False):
    """"dict for CoilHeatingDxVariablerefrigerantflow"""
    Name: str
    Availability_Schedule: str
    Gross_Rated_Heating_Capacity: str
    Rated_Air_Flow_Rate: str
    Coil_Air_Inlet_Node: str
    Coil_Air_Outlet_Node: str
    Heating_Capacity_Ratio_Modifier_Function_of_Temperature_Curve_Name: str
    Heating_Capacity_Modifier_Function_of_Flow_Fraction_Curve_Name: str

class CoilHeatingDxVariablerefrigerantflowFluidtemperaturecontrolType(TypedDict, total=False):
    """"dict for CoilHeatingDxVariablerefrigerantflowFluidtemperaturecontrol"""
    Name: str
    Availability_Schedule: str
    Coil_Air_Inlet_Node: str
    Coil_Air_Outlet_Node: str
    Rated_Total_Heating_Capacity: str
    Indoor_Unit_Reference_Subcooling: str
    Indoor_Unit_Condensing_Temperature_Function_of_Subcooling_Curve_Name: str

class CoilHeatingDxVariablespeedType(TypedDict, total=False):
    """"dict for CoilHeatingDxVariablespeed"""
    Name: str
    Indoor_Air_Inlet_Node_Name: str
    Indoor_Air_Outlet_Node_Name: str
    Number_of_Speeds: str
    Nominal_Speed_Level: str
    Rated_Heating_Capacity_At_Selected_Nominal_Speed_Level: str
    Rated_Air_Flow_Rate_At_Selected_Nominal_Speed_Level: str
    Energy_Part_Load_Fraction_Curve_Name: str
    Defrost_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Minimum_Outdoor_DryBulb_Temperature_for_Compressor_Operation: str
    Outdoor_DryBulb_Temperature_to_Turn_On_Compressor: str
    Maximum_Outdoor_DryBulb_Temperature_for_Defrost_Operation: str
    Crankcase_Heater_Capacity: str
    Crankcase_Heater_Capacity_Function_of_Temperature_Curve_Name: str
    Maximum_Outdoor_DryBulb_Temperature_for_Crankcase_Heater_Operation: str
    Defrost_Strategy: str
    Defrost_Control: str
    Defrost_Time_Period_Fraction: str
    Resistive_Defrost_Heater_Capacity: str
    Speed_1_Reference_Unit_Gross_Rated_Heating_Capacity: str
    Speed_1_Reference_Unit_Gross_Rated_Heating_COP: str
    Speed_1_Reference_Unit_Rated_Air_Flow_Rate: str
    _2017_Speed_1_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_1_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_1_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_1_Total_Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_1_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_1_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_2_Reference_Unit_Gross_Rated_Heating_Capacity: str
    Speed_2_Reference_Unit_Gross_Rated_Heating_COP: str
    Speed_2_Reference_Unit_Rated_Air_Flow_Rate: str
    _2017_Speed_2_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_2_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_2_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_2_Total_Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_2_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_2_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_3_Reference_Unit_Gross_Rated_Heating_Capacity: str
    Speed_3_Reference_Unit_Gross_Rated_Heating_COP: str
    Speed_3_Reference_Unit_Rated_Air_Flow_Rate: str
    _2017_Speed_3_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_3_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_3_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_3_Total_Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_3_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_3_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_4_Reference_Unit_Gross_Rated_Heating_Capacity: str
    Speed_4_Reference_Unit_Gross_Rated_Heating_COP: str
    Speed_4_Reference_Unit_Rated_Air_Flow_Rate: str
    _2017_Speed_4_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_4_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_4_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_4_Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_4_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_4_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_5_Reference_Unit_Gross_Rated_Heating_Capacity: str
    Speed_5_Reference_Unit_Gross_Rated_Heating_COP: str
    Speed_5_Reference_Unit_Rated_Air_Flow_Rate: str
    _2017_Speed_5_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_5_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_5_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_5_Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_5_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_5_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_6_Reference_Unit_Gross_Rated_Heating_Capacity: str
    Speed_6_Reference_Unit_Gross_Rated_Heating_COP: str
    Speed_6_Reference_Unit_Rated_Air_Flow_Rate: str
    _2017_Speed_6_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_6_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_6_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_6_Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_6_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_6_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_7_Reference_Unit_Gross_Rated_Heating_Capacity: str
    Speed_7_Reference_Unit_Gross_Rated_Heating_COP: str
    Speed_7_Reference_Unit_Rated_Air_Flow_Rate: str
    _2017_Speed_7_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_7_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_7_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_7_Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_7_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_7_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_8_Reference_Unit_Gross_Rated_Heating_Capacity: str
    Speed_8_Reference_Unit_Gross_Rated_Heating_COP: str
    Speed_8_Reference_Unit_Rated_Air_Flow_Rate: str
    _2017_Speed_8_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_8_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_8_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_8_Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_8_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_8_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_9_Reference_Unit_Gross_Rated_Heating_Capacity: str
    Speed_9_Reference_Unit_Gross_Rated_Heating_COP: str
    Speed_9_Reference_Unit_Rated_Air_Flow_Rate: str
    _2017_Speed_9_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_9_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_9_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_9_Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_9_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_9_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_10_Reference_Unit_Gross_Rated_Heating_Capacity: str
    Speed_10_Reference_Unit_Gross_Rated_Heating_COP: str
    Speed_10_Reference_Unit_Rated_Air_Flow_Rate: str
    _2017_Speed_10_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    _2023_Speed_10_Rated_Supply_Air_Fan_Power_Per_Volume_Flow_Rate: str
    Speed_10_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_10_Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_10_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_10_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str

class CoilHeatingElectricType(TypedDict, total=False):
    """"dict for CoilHeatingElectric"""
    Name: str
    Availability_Schedule_Name: str
    Efficiency: str
    Nominal_Capacity: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Temperature_Setpoint_Node_Name: str

class CoilHeatingElectricMultistageType(TypedDict, total=False):
    """"dict for CoilHeatingElectricMultistage"""
    Name: str
    Availability_Schedule_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Temperature_Setpoint_Node_Name: str
    Number_of_Stages: str
    Stage_1_Efficiency: str
    Stage_1_Nominal_Capacity: str
    Stage_2_Efficiency: str
    Stage_2_Nominal_Capacity: str
    Stage_3_Efficiency: str
    Stage_3_Nominal_Capacity: str
    Stage_4_Efficiency: str
    Stage_4_Nominal_Capacity: str

class CoilHeatingFuelType(TypedDict, total=False):
    """"dict for CoilHeatingFuel"""
    Name: str
    Availability_Schedule_Name: str
    Fuel_Type: str
    Burner_Efficiency: str
    Nominal_Capacity: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Temperature_Setpoint_Node_Name: str
    On_Cycle_Parasitic_Electric_Load: str
    Part_Load_Fraction_Correlation_Curve_Name: str
    Off_Cycle_Parasitic_Fuel_Load: str

class CoilHeatingGasMultistageType(TypedDict, total=False):
    """"dict for CoilHeatingGasMultistage"""
    Name: str
    Availability_Schedule_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Temperature_Setpoint_Node_Name: str
    Part_Load_Fraction_Correlation_Curve_Name: str
    Off_Cycle_Parasitic_Gas_Load: str
    Number_of_Stages: str
    Stage_1_Gas_Burner_Efficiency: str
    Stage_1_Nominal_Capacity: str
    Stage_1_On_Cycle_Parasitic_Electric_Load: str
    Stage_2_Gas_Burner_Efficiency: str
    Stage_2_Nominal_Capacity: str
    Stage_2_On_Cycle_Parasitic_Electric_Load: str
    Stage_3_Gas_Burner_Efficiency: str
    Stage_3_Nominal_Capacity: str
    Stage_3_On_Cycle_Parasitic_Electric_Load: str
    Stage_4_Gas_Burner_Efficiency: str
    Stage_4_Nominal_Capacity: str
    Stage_4_On_Cycle_Parasitic_Electric_Load: str

class CoilHeatingSteamType(TypedDict, total=False):
    """"dict for CoilHeatingSteam"""
    Name: str
    Availability_Schedule_Name: str
    Maximum_Steam_Flow_Rate: str
    Degree_of_SubCooling: str
    Degree_of_Loop_SubCooling: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Coil_Control_Type: str
    Temperature_Setpoint_Node_Name: str

class CoilHeatingWaterType(TypedDict, total=False):
    """"dict for CoilHeatingWater"""
    Name: str
    Availability_Schedule_Name: str
    UFactor_Times_Area_Value: str
    Maximum_Water_Flow_Rate: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Performance_Input_Method: str
    Rated_Capacity: str
    Rated_Inlet_Water_Temperature: str
    Rated_Inlet_Air_Temperature: str
    Rated_Outlet_Water_Temperature: str
    Rated_Outlet_Air_Temperature: str
    Rated_Ratio_for_Air_and_Water_Convection: str
    Design_Water_Temperature_Difference: str

class CoilHeatingWatertoairheatpumpEquationfitType(TypedDict, total=False):
    """"dict for CoilHeatingWatertoairheatpumpEquationfit"""
    Name: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Rated_Air_Flow_Rate: str
    Rated_Water_Flow_Rate: str
    Gross_Rated_Heating_Capacity: str
    Gross_Rated_Heating_COP: str
    Rated_Entering_Water_Temperature: str
    Rated_Entering_Air_DryBulb_Temperature: str
    Ratio_of_Rated_Heating_Capacity_to_Rated_Cooling_Capacity: str
    Heating_Capacity_Curve_Name: str
    Heating_Power_Consumption_Curve_Name: str
    Part_Load_Fraction_Correlation_Curve_Name: str

class CoilHeatingWatertoairheatpumpParameterestimationType(TypedDict, total=False):
    """"dict for CoilHeatingWatertoairheatpumpParameterestimation"""
    Name: str
    Compressor_Type: str
    Refrigerant_Type: str
    Design_Source_Side_Flow_Rate: str
    Gross_Rated_Heating_Capacity: str
    High_Pressure_Cutoff: str
    Low_Pressure_Cutoff: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Load_Side_Total_Heat_Transfer_Coefficient: str
    Superheat_Temperature_at_the_Evaporator_Outlet: str
    Compressor_Power_Losses: str
    Compressor_Efficiency: str
    Compressor_Piston_Displacement: str
    Compressor_SuctionDischarge_Pressure_Drop: str
    Compressor_Clearance_Factor: str
    Refrigerant_Volume_Flow_Rate: str
    Volume_Ratio: str
    Leak_Rate_Coefficient: str
    Source_Side_Heat_Transfer_Coefficient: str
    Source_Side_Heat_Transfer_Resistance1: str
    Source_Side_Heat_Transfer_Resistance2: str
    Part_Load_Fraction_Correlation_Curve_Name: str

class CoilHeatingWatertoairheatpumpVariablespeedequationfitType(TypedDict, total=False):
    """"dict for CoilHeatingWatertoairheatpumpVariablespeedequationfit"""
    Name: str
    WatertoRefrigerant_HX_Water_Inlet_Node_Name: str
    WatertoRefrigerant_HX_Water_Outlet_Node_Name: str
    Indoor_Air_Inlet_Node_Name: str
    Indoor_Air_Outlet_Node_Name: str
    Number_of_Speeds: str
    Nominal_Speed_Level: str
    Rated_Heating_Capacity_At_Selected_Nominal_Speed_Level: str
    Rated_Air_Flow_Rate_At_Selected_Nominal_Speed_Level: str
    Rated_Water_Flow_Rate_At_Selected_Nominal_Speed_Level: str
    Energy_Part_Load_Fraction_Curve_Name: str
    Speed_1_Reference_Unit_Gross_Rated_Heating_Capacity: str
    Speed_1_Reference_Unit_Gross_Rated_Heating_COP: str
    Speed_1_Reference_Unit_Rated_Air_Flow: str
    Speed_1_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_1_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_1_Total_Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_1_Heating_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_1_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_1_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_1_Energy_Input_Ratio_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_1_Reference_Unit_Waste_Heat_Fraction_of_Input_Power_At_Rated_Conditions: str
    Speed_1_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_2_Reference_Unit_Gross_Rated_Heating_Capacity: str
    Speed_2_Reference_Unit_Gross_Rated_Heating_COP: str
    Speed_2_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_2_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_2_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_2_Total_Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_2_Heating_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_2_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_2_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_2_Energy_Input_Ratio_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_2_Reference_Unit_Waste_Heat_Fraction_of_Input_Power_At_Rated_Conditions: str
    Speed_2_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_3_Reference_Unit_Gross_Rated_Heating_Capacity: str
    Speed_3_Reference_Unit_Gross_Rated_Heating_COP: str
    Speed_3_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_3_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_3_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_3_Total_Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_3_Heating_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_3_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_3_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_3_Energy_Input_Ratio_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_3_Reference_Unit_Waste_Heat_Fraction_of_Input_Power_At_Rated_Conditions: str
    Speed_3_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_4_Reference_Unit_Gross_Rated_Heating_Capacity: str
    Speed_4_Reference_Unit_Gross_Rated_Heating_COP: str
    Speed_4_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_4_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_4_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_4_Total_Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_4_Heating_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_4_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_4_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_4_Energy_Input_Ratio_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_4_Reference_Unit_Waste_Heat_Fraction_of_Input_Power_At_Rated_Conditions: str
    Speed_4_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_5_Reference_Unit_Gross_Rated_Heating_Capacity: str
    Speed_5_Reference_Unit_Gross_Rated_Heating_COP: str
    Speed_5_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_5_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_5_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_5_Total_Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_5_Heating_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_5_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_5_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_5_Energy_Input_Ratio_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_5_Reference_Unit_Waste_Heat_Fraction_of_Input_Power_At_Rated_Conditions: str
    Speed_5_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_6_Reference_Unit_Gross_Rated_Heating_Capacity: str
    Speed_6_Reference_Unit_Gross_Rated_Heating_COP: str
    Speed_6_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_6_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_6_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_6_Total_Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_6_Heating_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_6_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_6_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_6_Energy_Input_Ratio_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_6_Reference_Unit_Waste_Heat_Fraction_of_Input_Power_At_Rated_Conditions: str
    Speed_6_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_7_Reference_Unit_Gross_Rated_Heating_Capacity: str
    Speed_7_Reference_Unit_Gross_Rated_Heating_COP: str
    Speed_7_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_7_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_7_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_7_Total_Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_7_Heating_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_7_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_7_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_7_Energy_Input_Ratio_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_7_Reference_Unit_Waste_Heat_Fraction_of_Input_Power_At_Rated_Conditions: str
    Speed_7_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_8_Reference_Unit_Gross_Rated_Heating_Capacity: str
    Speed_8_Reference_Unit_Gross_Rated_Heating_COP: str
    Speed_8_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_8_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_8_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_8_Total_Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_8_Heating_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_8_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_8_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_8_Energy_Input_Ratio_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_8_Reference_Unit_Waste_Heat_Fraction_of_Input_Power_At_Rated_Conditions: str
    Speed_8_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_9_Reference_Unit_Gross_Rated_Heating_Capacity: str
    Speed_9_Reference_Unit_Gross_Rated_Heating_COP: str
    Speed_9_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_9_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_9_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_9_Total_Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_9_Heating_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_9_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_9_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_9_Energy_Input_Ratio_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_9_Reference_Unit_Waste_Heat_Fraction_of_Input_Power_At_Rated_Conditions: str
    Speed_9_Waste_Heat_Function_of_Temperature_Curve_Name: str
    Speed_10_Reference_Unit_Gross_Rated_Heating_Capacity: str
    Speed_10_Reference_Unit_Gross_Rated_Heating_COP: str
    Speed_10_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_10_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_10_Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_10_Total_Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_10_Heating_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_10_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Speed_10_Energy_Input_Ratio_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_10_Energy_Input_Ratio_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_10_Reference_Unit_Waste_Heat_Fraction_of_Input_Power_At_Rated_Conditions: str
    Speed_10_Waste_Heat_Function_of_Temperature_Curve_Name: str

class CoilUserdefinedType(TypedDict, total=False):
    """"dict for CoilUserdefined"""
    Name: str
    Overall_Model_Simulation_Program_Calling_Manager_Name: str
    Model_Setup_and_Sizing_Program_Calling_Manager_Name: str
    Number_of_Air_Connections: str
    Air_Connection_1_Inlet_Node_Name: str
    Air_Connection_1_Outlet_Node_Name: str
    Air_Connection_2_Inlet_Node_Name: str
    Air_Connection_2_Outlet_Node_Name: str
    Plant_Connection_is_Used: str
    Plant_Connection_Inlet_Node_Name: str
    Plant_Connection_Outlet_Node_Name: str
    Supply_Inlet_Water_Storage_Tank_Name: str
    Collection_Outlet_Water_Storage_Tank_Name: str
    Ambient_Zone_Name: str

class CoilWaterheatingAirtowaterheatpumpPumpedType(TypedDict, total=False):
    """"dict for CoilWaterheatingAirtowaterheatpumpPumped"""
    Name: str
    Rated_Heating_Capacity: str
    Rated_COP: str
    Rated_Sensible_Heat_Ratio: str
    Rated_Evaporator_Inlet_Air_DryBulb_Temperature: str
    Rated_Evaporator_Inlet_Air_WetBulb_Temperature: str
    Rated_Condenser_Inlet_Water_Temperature: str
    Rated_Evaporator_Air_Flow_Rate: str
    Rated_Condenser_Water_Flow_Rate: str
    Evaporator_Fan_Power_Included_in_Rated_COP: str
    Condenser_Pump_Power_Included_in_Rated_COP: str
    Condenser_Pump_Heat_Included_in_Rated_Heating_Capacity_and_Rated_COP: str
    Condenser_Water_Pump_Power: str
    Fraction_of_Condenser_Pump_Heat_to_Water: str
    Evaporator_Air_Inlet_Node_Name: str
    Evaporator_Air_Outlet_Node_Name: str
    Condenser_Water_Inlet_Node_Name: str
    Condenser_Water_Outlet_Node_Name: str
    Crankcase_Heater_Capacity: str
    Crankcase_Heater_Capacity_Function_of_Temperature_Curve_Name: str
    Maximum_Ambient_Temperature_for_Crankcase_Heater_Operation: str
    Evaporator_Air_Temperature_Type_for_Curve_Objects: str
    Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Heating_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Heating_COP_Function_of_Temperature_Curve_Name: str
    Heating_COP_Function_of_Air_Flow_Fraction_Curve_Name: str
    Heating_COP_Function_of_Water_Flow_Fraction_Curve_Name: str
    Part_Load_Fraction_Correlation_Curve_Name: str

class CoilWaterheatingAirtowaterheatpumpVariablespeedType(TypedDict, total=False):
    """"dict for CoilWaterheatingAirtowaterheatpumpVariablespeed"""
    Name: str
    Number_of_Speeds: str
    Nominal_Speed_Level: str
    Rated_Water_Heating_Capacity: str
    Rated_Evaporator_Inlet_Air_DryBulb_Temperature: str
    Rated_Evaporator_Inlet_Air_WetBulb_Temperature: str
    Rated_Condenser_Inlet_Water_Temperature: str
    Rated_Evaporator_Air_Flow_Rate: str
    Rated_Condenser_Water_Flow_Rate: str
    Evaporator_Fan_Power_Included_in_Rated_COP: str
    Condenser_Pump_Power_Included_in_Rated_COP: str
    Condenser_Pump_Heat_Included_in_Rated_Heating_Capacity_and_Rated_COP: str
    Fraction_of_Condenser_Pump_Heat_to_Water: str
    Evaporator_Air_Inlet_Node_Name: str
    Evaporator_Air_Outlet_Node_Name: str
    Condenser_Water_Inlet_Node_Name: str
    Condenser_Water_Outlet_Node_Name: str
    Crankcase_Heater_Capacity: str
    Crankcase_Heater_Capacity_Function_of_Temperature_Curve_Name: str
    Maximum_Ambient_Temperature_for_Crankcase_Heater_Operation: str
    Evaporator_Air_Temperature_Type_for_Curve_Objects: str
    Part_Load_Fraction_Correlation_Curve_Name: str
    Rated_Water_Heating_Capacity_at_Speed_1: str
    Rated_Water_Heating_COP_at_Speed_1: str
    Rated_Sensible_Heat_Ratio_at_Speed_1: str
    Speed_1_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_1_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_1_Reference_Unit_Water_Pump_Input_Power_At_Rated_Conditions: str
    Speed_1_Total_WH_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_1_Total_WH_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_1_Total_WH_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_1_COP_Function_of_Temperature_Curve_Name: str
    Speed_1_COP_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_1_COP_Function_of_Water_Flow_Fraction_Curve_Name: str
    Rated_Water_Heating_Capacity_at_Speed_2: str
    Rated_Water_Heating_COP_at_Speed_2: str
    Rated_Sensible_Heat_Ratio_at_Speed_2: str
    Speed_2_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_2_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_2_Reference_Unit_Water_Pump_Input_Power_At_Rated_Conditions: str
    Speed_2_Total_WH_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_2_Total_WH_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_2_Total_WH_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_2_COP_Function_of_Temperature_Curve_Name: str
    Speed_2_COP_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_2_COP_Function_of_Water_Flow_Fraction_Curve_Name: str
    Rated_Water_Heating_Capacity_at_speed_3: str
    Rated_Water_Heating_COP_at_Speed_3: str
    Rated_Sensible_Heat_Ratio_at_Speed_3: str
    Speed_3_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_3_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_3_Reference_Unit_Water_Pump_Input_Power_At_Rated_Conditions: str
    Speed_3_Total_WH_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_3_Total_WH_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_3_Total_WH_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_3_COP_Function_of_Temperature_Curve_Name: str
    Speed_3_COP_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_3_COP_Function_of_Water_Flow_Fraction_Curve_Name: str
    Rated_Water_Heating_Capacity_at_Speed_4: str
    Rated_Water_Heating_COP_at_Speed_4: str
    Rated_Sensible_Heat_Ratio_at_Speed_4: str
    Speed_4_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_4_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_4_Reference_Unit_Water_Pump_Input_Power_At_Rated_Conditions: str
    Speed_4_Total_WH_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_4_Total_WH_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_4_Total_WH_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_4_COP_Function_of_Temperature_Curve_Name: str
    Speed_4_COP_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_4_COP_Function_of_Water_Flow_Fraction_Curve_Name: str
    Rated_Water_Heating_Capacity_at_Speed_5: str
    Rated_Water_Heating_COP_at_Speed_5: str
    Rated_Sensible_Heat_Ratio_at_Speed_5: str
    Speed_5_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_5_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_5_Reference_Unit_Water_Pump_Input_Power_At_Rated_Conditions: str
    Speed_5_Total_WH_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_5_Total_WH_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_5_Total_WH_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_5_COP_Function_of_Temperature_Curve_Name: str
    Speed_5_COP_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_5_COP_Function_of_Water_Flow_Fraction_Curve_Name: str
    Rated_Water_Heating_Capacity_at_Speed_6: str
    Rated_Water_Heating_COP_at_Speed_6: str
    Rated_Sensible_Heat_Ratio_at_Speed_6: str
    Speed_6_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_6_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_6_Reference_Unit_Water_Pump_Input_Power_At_Rated_Conditions: str
    Speed_6_Total_WH_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_6_Total_WH_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_6_Total_WH_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_6_COP_Function_of_Temperature_Curve_Name: str
    Speed_6_COP_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_6_COP_Function_of_Water_Flow_Fraction_Curve_Name: str
    Rated_Water_Heating_Capacity_at_Speed_7: str
    Rated_Water_Heating_COP_at_Speed_7: str
    Rated_Sensible_Heat_Ratio_at_Speed_7: str
    Speed_7_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_7_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_7_Reference_Unit_Water_Pump_Input_Power_At_Rated_Conditions: str
    Speed_7_Total_WH_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_7_Total_WH_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_7_Total_WH_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_7_COP_Function_of_Temperature_Curve_Name: str
    Speed_7_COP_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_7_COP_Function_of_Water_Flow_Fraction_Curve_Name: str
    Rated_Water_Heating_Capacity_at_Speed_8: str
    Rated_Water_Heating_COP_at_Speed_8: str
    Rated_Sensible_Heat_Ratio_at_Speed_8: str
    Speed_8_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_8_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_8_Reference_Unit_Water_Pump_Input_Power_At_Rated_Conditions: str
    Speed_8_Total_WH_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_8_Total_WH_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_8_Total_WH_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_8_COP_Function_of_Temperature_Curve_Name: str
    Speed_8_COP_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_8_COP_Function_of_Water_Flow_Fraction_Curve_Name: str
    Rated_Water_Heating_Capacity_at_Speed_9: str
    Rated_Water_Heating_COP_at_Speed_9: str
    Rated_Sensible_Heat_Ratio_at_Speed_9: str
    Speed_9_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_9_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_9_Reference_Unit_Water_Pump_Input_Power_At_Rated_Conditions: str
    Speed_9_Total_WH_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_9_Total_WH_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_9_Total_WH_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_9_COP_Function_of_Temperature_Curve_Name: str
    Speed_9_COP_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_9_COP_Function_of_Water_Flow_Fraction_Curve_Name: str
    Rated_Water_Heating_Capacity_at_Speed_10: str
    Rated_Water_Heating_COP_at_Speed_10: str
    Rated_Sensible_Heat_Ratio_at_Speed_10: str
    Speed_10_Reference_Unit_Rated_Air_Flow_Rate: str
    Speed_10_Reference_Unit_Rated_Water_Flow_Rate: str
    Speed_10_Reference_Unit_Water_Pump_Input_Power_At_Rated_Conditions: str
    Speed_10_Total_WH_Capacity_Function_of_Temperature_Curve_Name: str
    Speed_10_Total_WH_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_10_Total_WH_Capacity_Function_of_Water_Flow_Fraction_Curve_Name: str
    Speed_10_COP_Function_of_Temperature_Curve_Name: str
    Speed_10_COP_Function_of_Air_Flow_Fraction_Curve_Name: str
    Speed_10_COP_Function_of_Water_Flow_Fraction_Curve_Name: str

class CoilWaterheatingAirtowaterheatpumpWrappedType(TypedDict, total=False):
    """"dict for CoilWaterheatingAirtowaterheatpumpWrapped"""
    Name: str
    Rated_Heating_Capacity: str
    Rated_COP: str
    Rated_Sensible_Heat_Ratio: str
    Rated_Evaporator_Inlet_Air_DryBulb_Temperature: str
    Rated_Evaporator_Inlet_Air_WetBulb_Temperature: str
    Rated_Condenser_Water_Temperature: str
    Rated_Evaporator_Air_Flow_Rate: str
    Evaporator_Fan_Power_Included_in_Rated_COP: str
    Evaporator_Air_Inlet_Node_Name: str
    Evaporator_Air_Outlet_Node_Name: str
    Crankcase_Heater_Capacity: str
    Crankcase_Heater_Capacity_Function_of_Temperature_Curve_Name: str
    Maximum_Ambient_Temperature_for_Crankcase_Heater_Operation: str
    Evaporator_Air_Temperature_Type_for_Curve_Objects: str
    Heating_Capacity_Function_of_Temperature_Curve_Name: str
    Heating_Capacity_Function_of_Air_Flow_Fraction_Curve_Name: str
    Heating_COP_Function_of_Temperature_Curve_Name: str
    Heating_COP_Function_of_Air_Flow_Fraction_Curve_Name: str
    Part_Load_Fraction_Correlation_Curve_Name: str

class CoilWaterheatingDesuperheaterType(TypedDict, total=False):
    """"dict for CoilWaterheatingDesuperheater"""
    Name: str
    Availability_Schedule_Name: str
    Setpoint_Temperature_Schedule_Name: str
    Dead_Band_Temperature_Difference: str
    Rated_Heat_Reclaim_Recovery_Efficiency: str
    Rated_Inlet_Water_Temperature: str
    Rated_Outdoor_Air_Temperature: str
    Maximum_Inlet_Water_Temperature_for_Heat_Reclaim: str
    Heat_Reclaim_Efficiency_Function_of_Temperature_Curve_Name: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    Tank_Object_Type: str
    Tank_Name: str
    Heating_Source_Object_Type: str
    Heating_Source_Name: str
    Water_Flow_Rate: str
    Water_Pump_Power: str
    Fraction_of_Pump_Heat_to_Water: str
    OnCycle_Parasitic_Electric_Load: str
    OffCycle_Parasitic_Electric_Load: str

class CoilperformanceDxCoolingType(TypedDict, total=False):
    """"dict for CoilperformanceDxCooling"""
    Name: str
    Gross_Rated_Total_Cooling_Capacity: str
    Gross_Rated_Sensible_Heat_Ratio: str
    Gross_Rated_Cooling_COP: str
    Rated_Air_Flow_Rate: str
    Fraction_of_Air_Flow_Bypassed_Around_Coil: str
    Total_Cooling_Capacity_Function_of_Temperature_Curve_Name: str
    Total_Cooling_Capacity_Function_of_Flow_Fraction_Curve_Name: str
    Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Energy_Input_Ratio_Function_of_Flow_Fraction_Curve_Name: str
    Part_Load_Fraction_Correlation_Curve_Name: str
    Nominal_Time_for_Condensate_Removal_to_Begin: str
    Ratio_of_Initial_Moisture_Evaporation_Rate_and_Steady_State_Latent_Capacity: str
    Maximum_Cycling_Rate: str
    Latent_Capacity_Time_Constant: str
    Condenser_Air_Inlet_Node_Name: str
    Condenser_Type: str
    Evaporative_Condenser_Effectiveness: str
    Evaporative_Condenser_Air_Flow_Rate: str
    Evaporative_Condenser_Pump_Rated_Power_Consumption: str
    Sensible_Heat_Ratio_Function_of_Temperature_Curve_Name: str
    Sensible_Heat_Ratio_Function_of_Flow_Fraction_Curve_Name: str

class CoilsystemCoolingDxType(TypedDict, total=False):
    """"dict for CoilsystemCoolingDx"""
    Name: str
    Availability_Schedule_Name: str
    DX_Cooling_Coil_System_Inlet_Node_Name: str
    DX_Cooling_Coil_System_Outlet_Node_Name: str
    DX_Cooling_Coil_System_Sensor_Node_Name: str
    Cooling_Coil_Object_Type: str
    Cooling_Coil_Name: str
    Dehumidification_Control_Type: str
    Run_on_Sensible_Load: str
    Run_on_Latent_Load: str
    Use_Outdoor_Air_DX_Cooling_Coil: str
    Outdoor_Air_DX_Cooling_Coil_Leaving_Minimum_Air_Temperature: str

class CoilsystemCoolingDxHeatexchangerassistedType(TypedDict, total=False):
    """"dict for CoilsystemCoolingDxHeatexchangerassisted"""
    Name: str
    Heat_Exchanger_Object_Type: str
    Heat_Exchanger_Name: str
    Cooling_Coil_Object_Type: str
    Cooling_Coil_Name: str

class CoilsystemCoolingWaterType(TypedDict, total=False):
    """"dict for CoilsystemCoolingWater"""
    Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Availability_Schedule_Name: str
    Cooling_Coil_Object_Type: str
    Cooling_Coil_Name: str
    Dehumidification_Control_Type: str
    Run_on_Sensible_Load: str
    Run_on_Latent_Load: str
    Minimum_Air_To_Water_Temperature_Offset: str
    Economizer_Lockout: str
    Minimum_Water_Loop_Temperature_For_Heat_Recovery: str
    Companion_Coil_Used_For_Heat_Recovery: str

class CoilsystemCoolingWaterHeatexchangerassistedType(TypedDict, total=False):
    """"dict for CoilsystemCoolingWaterHeatexchangerassisted"""
    Name: str
    Heat_Exchanger_Object_Type: str
    Heat_Exchanger_Name: str
    Cooling_Coil_Object_Type: str
    Cooling_Coil_Name: str

class CoilsystemHeatingDxType(TypedDict, total=False):
    """"dict for CoilsystemHeatingDx"""
    Name: str
    Availability_Schedule_Name: str
    Heating_Coil_Object_Type: str
    Heating_Coil_Name: str

class CoilsystemIntegratedheatpumpAirsourceType(TypedDict, total=False):
    """"dict for CoilsystemIntegratedheatpumpAirsource"""
    Name: str
    Supply_Hot_Water_Flow_Sensor_Node_Name: str
    Space_Cooling_Coil_Name: str
    Space_Heating_Coil_Name: str
    Dedicated_Water_Heating_Coil_Name: str
    SCWH_Coil_Name: str
    SCDWH_Cooling_Coil_Name: str
    SCDWH_Water_Heating_Coil_Name: str
    SHDWH_Heating_Coil_Name: str
    SHDWH_Water_Heating_Coil_Name: str
    Indoor_Temperature_Limit_for_SCWH_Mode: str
    Ambient_Temperature_Limit_for_SCWH_Mode: str
    Indoor_Temperature_above_Which_WH_has_Higher_Priority: str
    Ambient_Temperature_above_Which_WH_has_Higher_Priority: str
    Flag_to_Indicate_Load_Control_in_SCWH_Mode: str
    Minimum_Speed_Level_for_SCWH_Mode: str
    Maximum_Water_Flow_Volume_before_Switching_from_SCDWH_to_SCWH_Mode: str
    Minimum_Speed_Level_for_SCDWH_Mode: str
    Maximum_Running_Time_before_Allowing_Electric_Resistance_Heat_Use_during_SHDWH_Mode: str
    Minimum_Speed_Level_for_SHDWH_Mode: str

class ComfortviewfactoranglesType(TypedDict, total=False):
    """"dict for Comfortviewfactorangles"""
    Name: str
    Surface_1_Name: str
    Angle_Factor_1: str
    Surface_2_Name: str
    Angle_Factor_2: str
    Surface_3_Name: str
    Angle_Factor_3: str
    Surface_4_Name: str
    Angle_Factor_4: str
    Surface_5_Name: str
    Angle_Factor_5: str
    Surface_6_Name: str
    Angle_Factor_6: str
    Surface_7_Name: str
    Angle_Factor_7: str
    Surface_8_Name: str
    Angle_Factor_8: str
    Surface_9_Name: str
    Angle_Factor_9: str
    Surface_10_Name: str
    Angle_Factor_10: str
    Surface_11_Name: str
    Angle_Factor_11: str
    Surface_12_Name: str
    Angle_Factor_12: str
    Surface_13_Name: str
    Angle_Factor_13: str
    Surface_14_Name: str
    Angle_Factor_14: str
    Surface_15_Name: str
    Angle_Factor_15: str
    Surface_16_Name: str
    Angle_Factor_16: str
    Surface_17_Name: str
    Angle_Factor_17: str
    Surface_18_Name: str
    Angle_Factor_18: str
    Surface_19_Name: str
    Angle_Factor_19: str
    Surface_20_Name: str
    Angle_Factor_20: str
    Surface_21_Name: str
    Angle_Factor_21: str
    Surface_22_Name: str
    Angle_Factor_22: str
    Surface_23_Name: str
    Angle_Factor_23: str
    Surface_24_Name: str
    Angle_Factor_24: str
    Surface_25_Name: str
    Angle_Factor_25: str
    Surface_26_Name: str
    Angle_Factor_26: str
    Surface_27_Name: str
    Angle_Factor_27: str
    Surface_28_Name: str
    Angle_Factor_28: str
    Surface_29_Name: str
    Angle_Factor_29: str
    Surface_30_Name: str
    Angle_Factor_30: str
    Surface_31_Name: str
    Angle_Factor_31: str
    Surface_32_Name: str
    Angle_Factor_32: str
    Surface_33_Name: str
    Angle_Factor_33: str
    Surface_34_Name: str
    Angle_Factor_34: str
    Surface_35_Name: str
    Angle_Factor_35: str
    Surface_36_Name: str
    Angle_Factor_36: str
    Surface_37_Name: str
    Angle_Factor_37: str
    Surface_38_Name: str
    Angle_Factor_38: str
    Surface_39_Name: str
    Angle_Factor_39: str
    Surface_40_Name: str
    Angle_Factor_40: str
    Surface_41_Name: str
    Angle_Factor_41: str
    Surface_42_Name: str
    Angle_Factor_42: str
    Surface_43_Name: str
    Angle_Factor_43: str
    Surface_44_Name: str
    Angle_Factor_44: str
    Surface_45_Name: str
    Angle_Factor_45: str
    Surface_46_Name: str
    Angle_Factor_46: str
    Surface_47_Name: str
    Angle_Factor_47: str
    Surface_48_Name: str
    Angle_Factor_48: str
    Surface_49_Name: str
    Angle_Factor_49: str

class ComplexfenestrationpropertySolarabsorbedlayersType(TypedDict, total=False):
    """"dict for ComplexfenestrationpropertySolarabsorbedlayers"""
    Name: str
    Fenestration_Surface: str
    Construction_Name: str
    Layer_1_Solar_Radiation_Absorbed_Schedule_Name: str
    Layer_2_Solar_Radiation_Absorbed_Schedule_Name: str
    Layer_3_Solar_Radiation_Absorbed_Schedule_Name: str
    Layer_4_Solar_Radiation_Absorbed_Schedule_Name: str
    Layer_5_Solar_Radiation_Absorbed_Schedule_Name: str

class ComplianceBuildingType(TypedDict, total=False):
    """"dict for ComplianceBuilding"""
    Building_Rotation_for_Appendix_G: str

class ComponentcostAdjustmentsType(TypedDict, total=False):
    """"dict for ComponentcostAdjustments"""
    Miscellaneous_Cost_per_Conditioned_Area: str
    Design_and_Engineering_Fees: str
    Contractor_Fee: str
    Contingency: str
    Permits_Bonding_and_Insurance: str
    Commissioning_Fee: str
    Regional_Adjustment_Factor: str

class ComponentcostLineitemType(TypedDict, total=False):
    """"dict for ComponentcostLineitem"""
    Name: str
    Type: str
    Line_Item_Type: str
    Item_Name: str
    Object_EndUse_Key: str
    Cost_per_Each: str
    Cost_per_Area: str
    Cost_per_Unit_of_Output_Capacity: str
    Cost_per_Unit_of_Output_Capacity_per_COP: str
    Cost_per_Volume: str
    Cost_per_Volume_Rate: str
    Cost_per_Energy_per_Temperature_Difference: str
    Quantity: str

class ComponentcostReferenceType(TypedDict, total=False):
    """"dict for ComponentcostReference"""
    Reference_Building_Line_Item_Costs: str
    Reference_Building_Miscellaneous_Cost_per_Conditioned_Area: str
    Reference_Building_Design_and_Engineering_Fees: str
    Reference_Building_Contractor_Fee: str
    Reference_Building_Contingency: str
    Reference_Building_Permits_Bonding_and_Insurance: str
    Reference_Building_Commissioning_Fee: str
    Reference_Building_Regional_Adjustment_Factor: str

class CondenserequipmentlistType(TypedDict, total=False):
    """"dict for Condenserequipmentlist"""
    Name: str
    Equipment_1_Object_Type: str
    Equipment_1_Name: str
    Equipment_2_Object_Type: str
    Equipment_2_Name: str
    Equipment_3_Object_Type: str
    Equipment_3_Name: str
    Equipment_4_Object_Type: str
    Equipment_4_Name: str
    Equipment_5_Object_Type: str
    Equipment_5_Name: str
    Equipment_6_Object_Type: str
    Equipment_6_Name: str
    Equipment_7_Object_Type: str
    Equipment_7_Name: str
    Equipment_8_Object_Type: str
    Equipment_8_Name: str
    Equipment_9_Object_Type: str
    Equipment_9_Name: str
    Equipment_10_Object_Type: str
    Equipment_10_Name: str

class CondenserequipmentoperationschemesType(TypedDict, total=False):
    """"dict for Condenserequipmentoperationschemes"""
    Name: str
    Control_Scheme_1_Object_Type: str
    Control_Scheme_1_Name: str
    Control_Scheme_1_Schedule_Name: str
    Control_Scheme_2_Object_Type: str
    Control_Scheme_2_Name: str
    Control_Scheme_2_Schedule_Name: str
    Control_Scheme_3_Object_Type: str
    Control_Scheme_3_Name: str
    Control_Scheme_3_Schedule_Name: str
    Control_Scheme_4_Object_Type: str
    Control_Scheme_4_Name: str
    Control_Scheme_4_Schedule_Name: str
    Control_Scheme_5_Object_Type: str
    Control_Scheme_5_Name: str
    Control_Scheme_5_Schedule_Name: str
    Control_Scheme_6_Object_Type: str
    Control_Scheme_6_Name: str
    Control_Scheme_6_Schedule_Name: str
    Control_Scheme_7_Object_Type: str
    Control_Scheme_7_Name: str
    Control_Scheme_7_Schedule_Name: str
    Control_Scheme_8_Object_Type: str
    Control_Scheme_8_Name: str
    Control_Scheme_8_Schedule_Name: str

class CondenserloopType(TypedDict, total=False):
    """"dict for Condenserloop"""
    Name: str
    Fluid_Type: str
    User_Defined_Fluid_Type: str
    Condenser_Equipment_Operation_Scheme_Name: str
    Condenser_Loop_Temperature_Setpoint_Node_Name: str
    Maximum_Loop_Temperature: str
    Minimum_Loop_Temperature: str
    Maximum_Loop_Flow_Rate: str
    Minimum_Loop_Flow_Rate: str
    Condenser_Loop_Volume: str
    Condenser_Side_Inlet_Node_Name: str
    Condenser_Side_Outlet_Node_Name: str
    Condenser_Side_Branch_List_Name: str
    Condenser_Side_Connector_List_Name: str
    Demand_Side_Inlet_Node_Name: str
    Demand_Side_Outlet_Node_Name: str
    Condenser_Demand_Side_Branch_List_Name: str
    Condenser_Demand_Side_Connector_List_Name: str
    Load_Distribution_Scheme: str
    Pressure_Simulation_Type: str
    Loop_Circulation_Time: str

class ConnectorMixerType(TypedDict, total=False):
    """"dict for ConnectorMixer"""
    Name: str
    Outlet_Branch_Name: str
    Inlet_Branch_1_Name: str
    Inlet_Branch_2_Name: str
    Inlet_Branch_3_Name: str
    Inlet_Branch_4_Name: str
    Inlet_Branch_5_Name: str
    Inlet_Branch_6_Name: str
    Inlet_Branch_7_Name: str
    Inlet_Branch_8_Name: str
    Inlet_Branch_9_Name: str
    Inlet_Branch_10_Name: str
    Inlet_Branch_11_Name: str
    Inlet_Branch_12_Name: str
    Inlet_Branch_13_Name: str
    Inlet_Branch_14_Name: str
    Inlet_Branch_15_Name: str
    Inlet_Branch_16_Name: str
    Inlet_Branch_17_Name: str
    Inlet_Branch_18_Name: str
    Inlet_Branch_19_Name: str
    Inlet_Branch_20_Name: str
    Inlet_Branch_21_Name: str
    Inlet_Branch_22_Name: str
    Inlet_Branch_23_Name: str
    Inlet_Branch_24_Name: str
    Inlet_Branch_25_Name: str
    Inlet_Branch_26_Name: str
    Inlet_Branch_27_Name: str
    Inlet_Branch_28_Name: str
    Inlet_Branch_29_Name: str
    Inlet_Branch_30_Name: str
    Inlet_Branch_31_Name: str
    Inlet_Branch_32_Name: str
    Inlet_Branch_33_Name: str
    Inlet_Branch_34_Name: str
    Inlet_Branch_35_Name: str
    Inlet_Branch_36_Name: str
    Inlet_Branch_37_Name: str
    Inlet_Branch_38_Name: str
    Inlet_Branch_39_Name: str
    Inlet_Branch_40_Name: str
    Inlet_Branch_41_Name: str
    Inlet_Branch_42_Name: str
    Inlet_Branch_43_Name: str
    Inlet_Branch_44_Name: str
    Inlet_Branch_45_Name: str
    Inlet_Branch_46_Name: str
    Inlet_Branch_47_Name: str
    Inlet_Branch_48_Name: str
    Inlet_Branch_49_Name: str

class ConnectorSplitterType(TypedDict, total=False):
    """"dict for ConnectorSplitter"""
    Name: str
    Inlet_Branch_Name: str
    Outlet_Branch_1_Name: str
    Outlet_Branch_2_Name: str
    Outlet_Branch_3_Name: str
    Outlet_Branch_4_Name: str
    Outlet_Branch_5_Name: str
    Outlet_Branch_6_Name: str
    Outlet_Branch_7_Name: str
    Outlet_Branch_8_Name: str
    Outlet_Branch_9_Name: str
    Outlet_Branch_10_Name: str
    Outlet_Branch_11_Name: str
    Outlet_Branch_12_Name: str
    Outlet_Branch_13_Name: str
    Outlet_Branch_14_Name: str
    Outlet_Branch_15_Name: str
    Outlet_Branch_16_Name: str
    Outlet_Branch_17_Name: str
    Outlet_Branch_18_Name: str
    Outlet_Branch_19_Name: str
    Outlet_Branch_20_Name: str
    Outlet_Branch_21_Name: str
    Outlet_Branch_22_Name: str
    Outlet_Branch_23_Name: str
    Outlet_Branch_24_Name: str
    Outlet_Branch_25_Name: str
    Outlet_Branch_26_Name: str
    Outlet_Branch_27_Name: str
    Outlet_Branch_28_Name: str
    Outlet_Branch_29_Name: str
    Outlet_Branch_30_Name: str
    Outlet_Branch_31_Name: str
    Outlet_Branch_32_Name: str
    Outlet_Branch_33_Name: str
    Outlet_Branch_34_Name: str
    Outlet_Branch_35_Name: str
    Outlet_Branch_36_Name: str
    Outlet_Branch_37_Name: str
    Outlet_Branch_38_Name: str
    Outlet_Branch_39_Name: str
    Outlet_Branch_40_Name: str
    Outlet_Branch_41_Name: str
    Outlet_Branch_42_Name: str
    Outlet_Branch_43_Name: str
    Outlet_Branch_44_Name: str
    Outlet_Branch_45_Name: str
    Outlet_Branch_46_Name: str
    Outlet_Branch_47_Name: str
    Outlet_Branch_48_Name: str
    Outlet_Branch_49_Name: str

class ConnectorlistType(TypedDict, total=False):
    """"dict for Connectorlist"""
    Name: str
    Connector_1_Object_Type: str
    Connector_1_Name: str
    Connector_2_Object_Type: str
    Connector_2_Name: str

class ConstructionType(TypedDict, total=False):
    """"dict for Construction"""
    Name: str
    Outside_Layer: str
    Layer_2: str
    Layer_3: str
    Layer_4: str
    Layer_5: str
    Layer_6: str
    Layer_7: str
    Layer_8: str
    Layer_9: str
    Layer_10: str

class ConstructionAirboundaryType(TypedDict, total=False):
    """"dict for ConstructionAirboundary"""
    Name: str
    Air_Exchange_Method: str
    Simple_Mixing_Air_Changes_per_Hour: str
    Simple_Mixing_Schedule_Name: str

class ConstructionCfactorundergroundwallType(TypedDict, total=False):
    """"dict for ConstructionCfactorundergroundwall"""
    Name: str
    CFactor: str
    Height: str

class ConstructionComplexfenestrationstateType(TypedDict, total=False):
    """"dict for ConstructionComplexfenestrationstate"""
    Name: str
    Basis_Type: str
    Basis_Symmetry_Type: str
    Window_Thermal_Model: str
    Basis_Matrix_Name: str
    Solar_Optical_Complex_Front_Transmittance_Matrix_Name: str
    Solar_Optical_Complex_Back_Reflectance_Matrix_Name: str
    Visible_Optical_Complex_Front_Transmittance_Matrix_Name: str
    Visible_Optical_Complex_Back_Transmittance_Matrix_Name: str
    Outside_Layer_Name: str
    Outside_Layer_Directional_Front_Absorptance_Matrix_Name: str
    Outside_Layer_Directional_Back_Absorptance_Matrix_Name: str
    Gap_1_Name: str
    CFS_Gap_1_Directional_Front_Absorptance_Matrix_Name: str
    CFS_Gap_1_Directional_Back_Absorptance_Matrix_Name: str
    Layer_2_Name: str
    Layer_2_Directional_Front_Absorptance_Matrix_Name: str
    Layer_2_Directional_Back_Absorptance_Matrix_Name: str
    Gap_2_Name: str
    Gap_2_Directional_Front_Absorptance_Matrix_Name: str
    Gap_2_Directional_Back_Absorptance_Matrix_Name: str
    Layer_3_Name: str
    Layer_3_Directional_Front_Absorptance_Matrix_Name: str
    Layer_3_Directional_Back_Absorptance_Matrix_Name: str
    Gap_3_Name: str
    Gap_3_Directional_Front_Absorptance_Matrix_Name: str
    Gap_3_Directional_Back_Absorptance_Matrix_Name: str
    Layer_4_Name: str
    Layer_4_Directional_Front_Absorptance_Matrix_Name: str
    Layer_4_Directional_Back_Absorptance_Matrix_Name: str
    Gap_4_Name: str
    Gap_4_Directional_Front_Absorptance_Matrix_Name: str
    Gap_4_Directional_Back_Absorptance_Matrix_Name: str
    Layer_5_Name: str
    Layer_5_Directional_Front_Absorptance_Matrix_Name: str
    Layer_5_Directional_Back_Absorptance_Matrix_Name: str

class ConstructionFfactorgroundfloorType(TypedDict, total=False):
    """"dict for ConstructionFfactorgroundfloor"""
    Name: str
    FFactor: str
    Area: str
    PerimeterExposed: str

class ConstructionWindowdatafileType(TypedDict, total=False):
    """"dict for ConstructionWindowdatafile"""
    Name: str
    File_Name: str

class ConstructionWindowequivalentlayerType(TypedDict, total=False):
    """"dict for ConstructionWindowequivalentlayer"""
    Name: str
    Outside_Layer: str
    Layer_2: str
    Layer_3: str
    Layer_4: str
    Layer_5: str
    Layer_6: str
    Layer_7: str
    Layer_8: str
    Layer_9: str
    Layer_10: str
    Layer_11: str

class ConstructionpropertyInternalheatsourceType(TypedDict, total=False):
    """"dict for ConstructionpropertyInternalheatsource"""
    Name: str
    Construction_Name: str
    Thermal_Source_Present_After_Layer_Number: str
    Temperature_Calculation_Requested_After_Layer_Number: str
    Dimensions_for_the_CTF_Calculation: str
    Tube_Spacing: str
    TwoDimensional_Temperature_Calculation_Position: str

class ControllerMechanicalventilationType(TypedDict, total=False):
    """"dict for ControllerMechanicalventilation"""
    Name: str
    Availability_Schedule_Name: str
    Demand_Controlled_Ventilation: str
    System_Outdoor_Air_Method: str
    Zone_Maximum_Outdoor_Air_Fraction: str
    Zone_or_ZoneList_1_Name: str
    Design_Specification_Outdoor_Air_Object_Name_1: str
    Design_Specification_Zone_Air_Distribution_Object_Name_1: str
    Zone_or_ZoneList_2_Name: str
    Design_Specification_Outdoor_Air_Object_Name_2: str
    Design_Specification_Zone_Air_Distribution_Object_Name_2: str
    Zone_or_ZoneList_3_Name: str
    Design_Specification_Outdoor_Air_Object_Name_3: str
    Design_Specification_Zone_Air_Distribution_Object_Name_3: str
    Zone_or_ZoneList_4_Name: str
    Design_Specification_Outdoor_Air_Object_Name_4: str
    Design_Specification_Zone_Air_Distribution_Object_Name_4: str
    Zone_or_ZoneList_5_Name: str
    Design_Specification_Outdoor_Air_Object_Name_5: str
    Design_Specification_Zone_Air_Distribution_Object_Name_5: str
    Zone_or_ZoneList_6_Name: str
    Design_Specification_Outdoor_Air_Object_Name_6: str
    Design_Specification_Zone_Air_Distribution_Object_Name_6: str
    Zone_or_ZoneList_7_Name: str
    Design_Specification_Outdoor_Air_Object_Name_7: str
    Design_Specification_Zone_Air_Distribution_Object_Name_7: str
    Zone_or_ZoneList_8_Name: str
    Design_Specification_Outdoor_Air_Object_Name_8: str
    Design_Specification_Zone_Air_Distribution_Object_Name_8: str
    Zone_or_ZoneList_9_Name: str
    Design_Specification_Outdoor_Air_Object_Name_9: str
    Design_Specification_Zone_Air_Distribution_Object_Name_9: str
    Zone_or_ZoneList_10_Name: str
    Design_Specification_Outdoor_Air_Object_Name_10: str
    Design_Specification_Zone_Air_Distribution_Object_Name_10: str
    Zone_or_ZoneList_11_Name: str
    Design_Specification_Outdoor_Air_Object_Name_11: str
    Design_Specification_Zone_Air_Distribution_Object_Name_11: str
    Zone_or_ZoneList_12_Name: str
    Design_Specification_Outdoor_Air_Object_Name_12: str
    Design_Specification_Zone_Air_Distribution_Object_Name_12: str
    Zone_or_ZoneList_13_Name: str
    Design_Specification_Outdoor_Air_Object_Name_13: str
    Design_Specification_Zone_Air_Distribution_Object_Name_13: str
    Zone_or_ZoneList_14_Name: str
    Design_Specification_Outdoor_Air_Object_Name_14: str
    Design_Specification_Zone_Air_Distribution_Object_Name_14: str
    Zone_or_ZoneList_15_Name: str
    Design_Specification_Outdoor_Air_Object_Name_15: str
    Design_Specification_Zone_Air_Distribution_Object_Name_15: str
    Zone_or_ZoneList_16_Name: str
    Design_Specification_Outdoor_Air_Object_Name_16: str
    Design_Specification_Zone_Air_Distribution_Object_Name_16: str
    Zone_or_ZoneList_17_Name: str
    Design_Specification_Outdoor_Air_Object_Name_17: str
    Design_Specification_Zone_Air_Distribution_Object_Name_17: str
    Zone_or_ZoneList_18_Name: str
    Design_Specification_Outdoor_Air_Object_Name_18: str
    Design_Specification_Zone_Air_Distribution_Object_Name_18: str
    Zone_or_ZoneList_19_Name: str
    Design_Specification_Outdoor_Air_Object_Name_19: str
    Design_Specification_Zone_Air_Distribution_Object_Name_19: str
    Zone_or_ZoneList_20_Name: str
    Design_Specification_Outdoor_Air_Object_Name_20: str
    Design_Specification_Zone_Air_Distribution_Object_Name_20: str
    Zone_or_ZoneList_21_Name: str
    Design_Specification_Outdoor_Air_Object_Name_21: str
    Design_Specification_Zone_Air_Distribution_Object_Name_21: str
    Zone_or_ZoneList_22_Name: str
    Design_Specification_Outdoor_Air_Object_Name_22: str
    Design_Specification_Zone_Air_Distribution_Object_Name_22: str
    Zone_or_ZoneList_23_Name: str
    Design_Specification_Outdoor_Air_Object_Name_23: str
    Design_Specification_Zone_Air_Distribution_Object_Name_23: str
    Zone_or_ZoneList_24_Name: str
    Design_Specification_Outdoor_Air_Object_Name_24: str
    Design_Specification_Zone_Air_Distribution_Object_Name_24: str
    Zone_or_ZoneList_25_Name: str
    Design_Specification_Outdoor_Air_Object_Name_25: str
    Design_Specification_Zone_Air_Distribution_Object_Name_25: str
    Zone_or_ZoneList_26_Name: str
    Design_Specification_Outdoor_Air_Object_Name_26: str
    Design_Specification_Zone_Air_Distribution_Object_Name_26: str
    Zone_or_ZoneList_27_Name: str
    Design_Specification_Outdoor_Air_Object_Name_27: str
    Design_Specification_Zone_Air_Distribution_Object_Name_27: str
    Zone_or_ZoneList_28_Name: str
    Design_Specification_Outdoor_Air_Object_Name_28: str
    Design_Specification_Zone_Air_Distribution_Object_Name_28: str
    Zone_or_ZoneList_29_Name: str
    Design_Specification_Outdoor_Air_Object_Name_29: str
    Design_Specification_Zone_Air_Distribution_Object_Name_29: str
    Zone_or_ZoneList_30_Name: str
    Design_Specification_Outdoor_Air_Object_Name_30: str
    Design_Specification_Zone_Air_Distribution_Object_Name_30: str
    Zone_or_ZoneList_31_Name: str
    Design_Specification_Outdoor_Air_Object_Name_31: str
    Design_Specification_Zone_Air_Distribution_Object_Name_31: str
    Zone_or_ZoneList_32_Name: str
    Design_Specification_Outdoor_Air_Object_Name_32: str
    Design_Specification_Zone_Air_Distribution_Object_Name_32: str
    Zone_or_ZoneList_33_Name: str
    Design_Specification_Outdoor_Air_Object_Name_33: str
    Design_Specification_Zone_Air_Distribution_Object_Name_33: str
    Zone_or_ZoneList_34_Name: str
    Design_Specification_Outdoor_Air_Object_Name_34: str
    Design_Specification_Zone_Air_Distribution_Object_Name_34: str
    Zone_or_ZoneList_35_Name: str
    Design_Specification_Outdoor_Air_Object_Name_35: str
    Design_Specification_Zone_Air_Distribution_Object_Name_35: str
    Zone_or_ZoneList_36_Name: str
    Design_Specification_Outdoor_Air_Object_Name_36: str
    Design_Specification_Zone_Air_Distribution_Object_Name_36: str
    Zone_or_ZoneList_37_Name: str
    Design_Specification_Outdoor_Air_Object_Name_37: str
    Design_Specification_Zone_Air_Distribution_Object_Name_37: str
    Zone_or_ZoneList_38_Name: str
    Design_Specification_Outdoor_Air_Object_Name_38: str
    Design_Specification_Zone_Air_Distribution_Object_Name_38: str
    Zone_or_ZoneList_39_Name: str
    Design_Specification_Outdoor_Air_Object_Name_39: str
    Design_Specification_Zone_Air_Distribution_Object_Name_39: str
    Zone_or_ZoneList_40_Name: str
    Design_Specification_Outdoor_Air_Object_Name_40: str
    Design_Specification_Zone_Air_Distribution_Object_Name_40: str
    Zone_or_ZoneList_41_Name: str
    Design_Specification_Outdoor_Air_Object_Name_41: str
    Design_Specification_Zone_Air_Distribution_Object_Name_41: str
    Zone_or_ZoneList_42_Name: str
    Design_Specification_Outdoor_Air_Object_Name_42: str
    Design_Specification_Zone_Air_Distribution_Object_Name_42: str
    Zone_or_ZoneList_43_Name: str
    Design_Specification_Outdoor_Air_Object_Name_43: str
    Design_Specification_Zone_Air_Distribution_Object_Name_43: str
    Zone_or_ZoneList_44_Name: str
    Design_Specification_Outdoor_Air_Object_Name_44: str
    Design_Specification_Zone_Air_Distribution_Object_Name_44: str
    Zone_or_ZoneList_45_Name: str
    Design_Specification_Outdoor_Air_Object_Name_45: str
    Design_Specification_Zone_Air_Distribution_Object_Name_45: str
    Zone_or_ZoneList_46_Name: str
    Design_Specification_Outdoor_Air_Object_Name_46: str
    Design_Specification_Zone_Air_Distribution_Object_Name_46: str
    Zone_or_ZoneList_47_Name: str
    Design_Specification_Outdoor_Air_Object_Name_47: str
    Design_Specification_Zone_Air_Distribution_Object_Name_47: str
    Zone_or_ZoneList_48_Name: str
    Design_Specification_Outdoor_Air_Object_Name_48: str
    Design_Specification_Zone_Air_Distribution_Object_Name_48: str
    Zone_or_ZoneList_49_Name: str
    Design_Specification_Outdoor_Air_Object_Name_49: str
    Design_Specification_Zone_Air_Distribution_Object_Name_49: str

class ControllerOutdoorairType(TypedDict, total=False):
    """"dict for ControllerOutdoorair"""
    Name: str
    Relief_Air_Outlet_Node_Name: str
    Return_Air_Node_Name: str
    Mixed_Air_Node_Name: str
    Actuator_Node_Name: str
    Minimum_Outdoor_Air_Flow_Rate: str
    Maximum_Outdoor_Air_Flow_Rate: str
    Economizer_Control_Type: str
    Economizer_Control_Action_Type: str
    Economizer_Maximum_Limit_DryBulb_Temperature: str
    Economizer_Maximum_Limit_Enthalpy: str
    Economizer_Maximum_Limit_Dewpoint_Temperature: str
    Electronic_Enthalpy_Limit_Curve_Name: str
    Economizer_Minimum_Limit_DryBulb_Temperature: str
    Lockout_Type: str
    Minimum_Limit_Type: str
    Minimum_Outdoor_Air_Schedule_Name: str
    Minimum_Fraction_of_Outdoor_Air_Schedule_Name: str
    Maximum_Fraction_of_Outdoor_Air_Schedule_Name: str
    Mechanical_Ventilation_Controller_Name: str
    Time_of_Day_Economizer_Control_Schedule_Name: str
    High_Humidity_Control: str
    Humidistat_Control_Zone_Name: str
    High_Humidity_Outdoor_Air_Flow_Ratio: str
    Control_High_Indoor_Humidity_Based_on_Outdoor_Humidity_Ratio: str
    Heat_Recovery_Bypass_Control_Type: str
    Economizer_Operation_Staging: str

class ControllerWatercoilType(TypedDict, total=False):
    """"dict for ControllerWatercoil"""
    Name: str
    Control_Variable: str
    Action: str
    Actuator_Variable: str
    Sensor_Node_Name: str
    Actuator_Node_Name: str
    Controller_Convergence_Tolerance: str
    Maximum_Actuated_Flow: str
    Minimum_Actuated_Flow: str

class ConvergencelimitsType(TypedDict, total=False):
    """"dict for Convergencelimits"""
    Minimum_System_Timestep: str
    Maximum_HVAC_Iterations: str
    Minimum_Plant_Iterations: str
    Maximum_Plant_Iterations: str

class CoolingtowerSinglespeedType(TypedDict, total=False):
    """"dict for CoolingtowerSinglespeed"""
    Name: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    Design_Water_Flow_Rate: str
    Design_Air_Flow_Rate: str
    Design_Fan_Power: str
    Design_UFactor_Times_Area_Value: str
    Free_Convection_Regime_Air_Flow_Rate: str
    Free_Convection_Regime_Air_Flow_Rate_Sizing_Factor: str
    Free_Convection_Regime_UFactor_Times_Area_Value: str
    Free_Convection_UFactor_Times_Area_Value_Sizing_Factor: str
    Performance_Input_Method: str
    Heat_Rejection_Capacity_and_Nominal_Capacity_Sizing_Ratio: str
    Nominal_Capacity: str
    Free_Convection_Capacity: str
    Free_Convection_Nominal_Capacity_Sizing_Factor: str
    Design_Inlet_Air_DryBulb_Temperature: str
    Design_Inlet_Air_WetBulb_Temperature: str
    Design_Approach_Temperature: str
    Design_Range_Temperature: str
    Basin_Heater_Capacity: str
    Basin_Heater_Setpoint_Temperature: str
    Basin_Heater_Operating_Schedule_Name: str
    Evaporation_Loss_Mode: str
    Evaporation_Loss_Factor: str
    Drift_Loss_Percent: str
    Blowdown_Calculation_Mode: str
    Blowdown_Concentration_Ratio: str
    Blowdown_Makeup_Water_Usage_Schedule_Name: str
    Supply_Water_Storage_Tank_Name: str
    Outdoor_Air_Inlet_Node_Name: str
    Capacity_Control: str
    Number_of_Cells: str
    Cell_Control: str
    Cell_Minimum_Water_Flow_Rate_Fraction: str
    Cell_Maximum_Water_Flow_Rate_Fraction: str
    Sizing_Factor: str
    EndUse_Subcategory: str

class CoolingtowerTwospeedType(TypedDict, total=False):
    """"dict for CoolingtowerTwospeed"""
    Name: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    Design_Water_Flow_Rate: str
    High_Fan_Speed_Air_Flow_Rate: str
    High_Fan_Speed_Fan_Power: str
    High_Fan_Speed_UFactor_Times_Area_Value: str
    Low_Fan_Speed_Air_Flow_Rate: str
    Low_Fan_Speed_Air_Flow_Rate_Sizing_Factor: str
    Low_Fan_Speed_Fan_Power: str
    Low_Fan_Speed_Fan_Power_Sizing_Factor: str
    Low_Fan_Speed_UFactor_Times_Area_Value: str
    Low_Fan_Speed_UFactor_Times_Area_Sizing_Factor: str
    Free_Convection_Regime_Air_Flow_Rate: str
    Free_Convection_Regime_Air_Flow_Rate_Sizing_Factor: str
    Free_Convection_Regime_UFactor_Times_Area_Value: str
    Free_Convection_UFactor_Times_Area_Value_Sizing_Factor: str
    Performance_Input_Method: str
    Heat_Rejection_Capacity_and_Nominal_Capacity_Sizing_Ratio: str
    High_Speed_Nominal_Capacity: str
    Low_Speed_Nominal_Capacity: str
    Low_Speed_Nominal_Capacity_Sizing_Factor: str
    Free_Convection_Nominal_Capacity: str
    Free_Convection_Nominal_Capacity_Sizing_Factor: str
    Design_Inlet_Air_DryBulb_Temperature: str
    Design_Inlet_Air_WetBulb_Temperature: str
    Design_Approach_Temperature: str
    Design_Range_Temperature: str
    Basin_Heater_Capacity: str
    Basin_Heater_Setpoint_Temperature: str
    Basin_Heater_Operating_Schedule_Name: str
    Evaporation_Loss_Mode: str
    Evaporation_Loss_Factor: str
    Drift_Loss_Percent: str
    Blowdown_Calculation_Mode: str
    Blowdown_Concentration_Ratio: str
    Blowdown_Makeup_Water_Usage_Schedule_Name: str
    Supply_Water_Storage_Tank_Name: str
    Outdoor_Air_Inlet_Node_Name: str
    Number_of_Cells: str
    Cell_Control: str
    Cell_Minimum_Water_Flow_Rate_Fraction: str
    Cell_Maximum_Water_Flow_Rate_Fraction: str
    Sizing_Factor: str
    EndUse_Subcategory: str

class CoolingtowerVariablespeedType(TypedDict, total=False):
    """"dict for CoolingtowerVariablespeed"""
    Name: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    Model_Type: str
    Model_Coefficient_Name: str
    Design_Inlet_Air_WetBulb_Temperature: str
    Design_Approach_Temperature: str
    Design_Range_Temperature: str
    Design_Water_Flow_Rate: str
    Design_Air_Flow_Rate: str
    Design_Fan_Power: str
    Fan_Power_Ratio_Function_of_Air_Flow_Rate_Ratio_Curve_Name: str
    Minimum_Air_Flow_Rate_Ratio: str
    Fraction_of_Tower_Capacity_in_Free_Convection_Regime: str
    Basin_Heater_Capacity: str
    Basin_Heater_Setpoint_Temperature: str
    Basin_Heater_Operating_Schedule_Name: str
    Evaporation_Loss_Mode: str
    Evaporation_Loss_Factor: str
    Drift_Loss_Percent: str
    Blowdown_Calculation_Mode: str
    Blowdown_Concentration_Ratio: str
    Blowdown_Makeup_Water_Usage_Schedule_Name: str
    Supply_Water_Storage_Tank_Name: str
    Outdoor_Air_Inlet_Node_Name: str
    Number_of_Cells: str
    Cell_Control: str
    Cell_Minimum_Water_Flow_Rate_Fraction: str
    Cell_Maximum_Water_Flow_Rate_Fraction: str
    Sizing_Factor: str
    EndUse_Subcategory: str

class CoolingtowerVariablespeedMerkelType(TypedDict, total=False):
    """"dict for CoolingtowerVariablespeedMerkel"""
    Name: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    Performance_Input_Method: str
    Heat_Rejection_Capacity_and_Nominal_Capacity_Sizing_Ratio: str
    Nominal_Capacity: str
    Free_Convection_Nominal_Capacity: str
    Free_Convection_Nominal_Capacity_Sizing_Factor: str
    Design_Water_Flow_Rate: str
    Design_Water_Flow_Rate_per_Unit_of_Nominal_Capacity: str
    Design_Air_Flow_Rate: str
    Design_Air_Flow_Rate_Per_Unit_of_Nominal_Capacity: str
    Minimum_Air_Flow_Rate_Ratio: str
    Design_Fan_Power: str
    Design_Fan_Power_Per_Unit_of_Nominal_Capacity: str
    Fan_Power_Modifier_Function_of_Air_Flow_Rate_Ratio_Curve_Name: str
    Free_Convection_Regime_Air_Flow_Rate: str
    Free_Convection_Regime_Air_Flow_Rate_Sizing_Factor: str
    Design_Air_Flow_Rate_UFactor_Times_Area_Value: str
    Free_Convection_Regime_UFactor_Times_Area_Value: str
    Free_Convection_UFactor_Times_Area_Value_Sizing_Factor: str
    UFactor_Times_Area_Modifier_Function_of_Air_Flow_Ratio_Curve_Name: str
    UFactor_Times_Area_Modifier_Function_of_Wetbulb_Temperature_Difference_Curve_Name: str
    UFactor_Times_Area_Modifier_Function_of_Water_Flow_Ratio_Curve_Name: str
    Design_Inlet_Air_DryBulb_Temperature: str
    Design_Inlet_Air_WetBulb_Temperature: str
    Design_Approach_Temperature: str
    Design_Range_Temperature: str
    Basin_Heater_Capacity: str
    Basin_Heater_Setpoint_Temperature: str
    Basin_Heater_Operating_Schedule_Name: str
    Evaporation_Loss_Mode: str
    Evaporation_Loss_Factor: str
    Drift_Loss_Percent: str
    Blowdown_Calculation_Mode: str
    Blowdown_Concentration_Ratio: str
    Blowdown_Makeup_Water_Usage_Schedule_Name: str
    Supply_Water_Storage_Tank_Name: str
    Outdoor_Air_Inlet_Node_Name: str
    Number_of_Cells: str
    Cell_Control: str
    Cell_Minimum_Water_Flow_Rate_Fraction: str
    Cell_Maximum_Water_Flow_Rate_Fraction: str
    Sizing_Factor: str
    EndUse_Subcategory: str

class CoolingtowerperformanceCooltoolsType(TypedDict, total=False):
    """"dict for CoolingtowerperformanceCooltools"""
    Name: str
    Minimum_Inlet_Air_WetBulb_Temperature: str
    Maximum_Inlet_Air_WetBulb_Temperature: str
    Minimum_Range_Temperature: str
    Maximum_Range_Temperature: str
    Minimum_Approach_Temperature: str
    Maximum_Approach_Temperature: str
    Minimum_Water_Flow_Rate_Ratio: str
    Maximum_Water_Flow_Rate_Ratio: str
    Coefficient_1: str
    Coefficient_2: str
    Coefficient_3: str
    Coefficient_4: str
    Coefficient_5: str
    Coefficient_6: str
    Coefficient_7: str
    Coefficient_8: str
    Coefficient_9: str
    Coefficient_10: str
    Coefficient_11: str
    Coefficient_12: str
    Coefficient_13: str
    Coefficient_14: str
    Coefficient_15: str
    Coefficient_16: str
    Coefficient_17: str
    Coefficient_18: str
    Coefficient_19: str
    Coefficient_20: str
    Coefficient_21: str
    Coefficient_22: str
    Coefficient_23: str
    Coefficient_24: str
    Coefficient_25: str
    Coefficient_26: str
    Coefficient_27: str
    Coefficient_28: str
    Coefficient_29: str
    Coefficient_30: str
    Coefficient_31: str
    Coefficient_32: str
    Coefficient_33: str
    Coefficient_34: str
    Coefficient_35: str

class CoolingtowerperformanceYorkcalcType(TypedDict, total=False):
    """"dict for CoolingtowerperformanceYorkcalc"""
    Name: str
    Minimum_Inlet_Air_WetBulb_Temperature: str
    Maximum_Inlet_Air_WetBulb_Temperature: str
    Minimum_Range_Temperature: str
    Maximum_Range_Temperature: str
    Minimum_Approach_Temperature: str
    Maximum_Approach_Temperature: str
    Minimum_Water_Flow_Rate_Ratio: str
    Maximum_Water_Flow_Rate_Ratio: str
    Maximum_Liquid_to_Gas_Ratio: str
    Coefficient_1: str
    Coefficient_2: str
    Coefficient_3: str
    Coefficient_4: str
    Coefficient_5: str
    Coefficient_6: str
    Coefficient_7: str
    Coefficient_8: str
    Coefficient_9: str
    Coefficient_10: str
    Coefficient_11: str
    Coefficient_12: str
    Coefficient_13: str
    Coefficient_14: str
    Coefficient_15: str
    Coefficient_16: str
    Coefficient_17: str
    Coefficient_18: str
    Coefficient_19: str
    Coefficient_20: str
    Coefficient_21: str
    Coefficient_22: str
    Coefficient_23: str
    Coefficient_24: str
    Coefficient_25: str
    Coefficient_26: str
    Coefficient_27: str

class CurrencytypeType(TypedDict, total=False):
    """"dict for Currencytype"""
    Monetary_Unit: str

class CurveBicubicType(TypedDict, total=False):
    """"dict for CurveBicubic"""
    Name: str
    Coefficient1_Constant: str
    Coefficient2_x: str
    Coefficient3_x2: str
    Coefficient4_y: str
    Coefficient5_y2: str
    Coefficient6_xy: str
    Coefficient7_x3: str
    Coefficient8_y3: str
    Coefficient9_x2y: str
    Coefficient10_xy2: str
    Minimum_Value_of_x: str
    Maximum_Value_of_x: str
    Minimum_Value_of_y: str
    Maximum_Value_of_y: str
    Minimum_Curve_Output: str
    Maximum_Curve_Output: str
    Input_Unit_Type_for_X: str
    Input_Unit_Type_for_Y: str
    Output_Unit_Type: str

class CurveBiquadraticType(TypedDict, total=False):
    """"dict for CurveBiquadratic"""
    Name: str
    Coefficient1_Constant: str
    Coefficient2_x: str
    Coefficient3_x2: str
    Coefficient4_y: str
    Coefficient5_y2: str
    Coefficient6_xy: str
    Minimum_Value_of_x: str
    Maximum_Value_of_x: str
    Minimum_Value_of_y: str
    Maximum_Value_of_y: str
    Minimum_Curve_Output: str
    Maximum_Curve_Output: str
    Input_Unit_Type_for_X: str
    Input_Unit_Type_for_Y: str
    Output_Unit_Type: str

class CurveChillerpartloadwithliftType(TypedDict, total=False):
    """"dict for CurveChillerpartloadwithlift"""
    Name: str
    Coefficient1_C1: str
    Coefficient2_C2: str
    Coefficient3_C3: str
    Coefficient4_C4: str
    Coefficient5_C5: str
    Coefficient6_C6: str
    Coefficient7_C7: str
    Coefficient8_C8: str
    Coefficient9_C9: str
    Coefficient10_C10: str
    Coefficient11_C11: str
    Coefficient12_C12: str
    Minimum_Value_of_x: str
    Maximum_Value_of_x: str
    Minimum_Value_of_y: str
    Maximum_Value_of_y: str
    Minimum_Value_of_z: str
    Maximum_Value_of_z: str
    Minimum_Curve_Output: str
    Maximum_Curve_Output: str
    Input_Unit_Type_for_x: str
    Input_Unit_Type_for_y: str
    Input_Unit_Type_for_z: str
    Output_Unit_Type: str

class CurveCubicType(TypedDict, total=False):
    """"dict for CurveCubic"""
    Name: str
    Coefficient1_Constant: str
    Coefficient2_x: str
    Coefficient3_x2: str
    Coefficient4_x3: str
    Minimum_Value_of_x: str
    Maximum_Value_of_x: str
    Minimum_Curve_Output: str
    Maximum_Curve_Output: str
    Input_Unit_Type_for_X: str
    Output_Unit_Type: str

class CurveCubiclinearType(TypedDict, total=False):
    """"dict for CurveCubiclinear"""
    Name: str
    Coefficient1_Constant: str
    Coefficient2_x: str
    Coefficient3_x2: str
    Coefficient4_x3: str
    Coefficient5_y: str
    Coefficient6_xy: str
    Minimum_Value_of_x: str
    Maximum_Value_of_x: str
    Minimum_Value_of_y: str
    Maximum_Value_of_y: str
    Minimum_Curve_Output: str
    Maximum_Curve_Output: str
    Input_Unit_Type_for_X: str
    Input_Unit_Type_for_Y: str
    Output_Unit_Type: str

class CurveDoubleexponentialdecayType(TypedDict, total=False):
    """"dict for CurveDoubleexponentialdecay"""
    Name: str
    Coefficient1_C1: str
    Coefficient2_C2: str
    Coefficient3_C3: str
    Coefficient4_C4: str
    Coefficient5_C5: str
    Minimum_Value_of_x: str
    Maximum_Value_of_x: str
    Minimum_Curve_Output: str
    Maximum_Curve_Output: str
    Input_Unit_Type_for_x: str
    Output_Unit_Type: str

class CurveExponentType(TypedDict, total=False):
    """"dict for CurveExponent"""
    Name: str
    Coefficient1_Constant: str
    Coefficient2_Constant: str
    Coefficient3_Constant: str
    Minimum_Value_of_x: str
    Maximum_Value_of_x: str
    Minimum_Curve_Output: str
    Maximum_Curve_Output: str
    Input_Unit_Type_for_X: str
    Output_Unit_Type: str

class CurveExponentialdecayType(TypedDict, total=False):
    """"dict for CurveExponentialdecay"""
    Name: str
    Coefficient1_C1: str
    Coefficient2_C2: str
    Coefficient3_C3: str
    Minimum_Value_of_x: str
    Maximum_Value_of_x: str
    Minimum_Curve_Output: str
    Maximum_Curve_Output: str
    Input_Unit_Type_for_x: str
    Output_Unit_Type: str

class CurveExponentialskewnormalType(TypedDict, total=False):
    """"dict for CurveExponentialskewnormal"""
    Name: str
    Coefficient1_C1: str
    Coefficient2_C2: str
    Coefficient3_C3: str
    Coefficient4_C4: str
    Minimum_Value_of_x: str
    Maximum_Value_of_x: str
    Minimum_Curve_Output: str
    Maximum_Curve_Output: str
    Input_Unit_Type_for_x: str
    Output_Unit_Type: str

class CurveFanpressureriseType(TypedDict, total=False):
    """"dict for CurveFanpressurerise"""
    Name: str
    Coefficient1_C1: str
    Coefficient2_C2: str
    Coefficient3_C3: str
    Coefficient4_C4: str
    Minimum_Value_of_Qfan: str
    Maximum_Value_of_Qfan: str
    Minimum_Value_of_Psm: str
    Maximum_Value_of_Psm: str
    Minimum_Curve_Output: str
    Maximum_Curve_Output: str

class CurveFunctionalPressuredropType(TypedDict, total=False):
    """"dict for CurveFunctionalPressuredrop"""
    Name: str
    Diameter: str
    Minor_Loss_Coefficient: str
    Length: str
    Roughness: str
    Fixed_Friction_Factor: str

class CurveLinearType(TypedDict, total=False):
    """"dict for CurveLinear"""
    Name: str
    Coefficient1_Constant: str
    Coefficient2_x: str
    Minimum_Value_of_x: str
    Maximum_Value_of_x: str
    Minimum_Curve_Output: str
    Maximum_Curve_Output: str
    Input_Unit_Type_for_X: str
    Output_Unit_Type: str

class CurveQuadlinearType(TypedDict, total=False):
    """"dict for CurveQuadlinear"""
    Name: str
    Coefficient1_Constant: str
    Coefficient2_w: str
    Coefficient3_x: str
    Coefficient4_y: str
    Coefficient5_z: str
    Minimum_Value_of_w: str
    Maximum_Value_of_w: str
    Minimum_Value_of_x: str
    Maximum_Value_of_x: str
    Minimum_Value_of_y: str
    Maximum_Value_of_y: str
    Minimum_Value_of_z: str
    Maximum_Value_of_z: str
    Minimum_Curve_Output: str
    Maximum_Curve_Output: str
    Input_Unit_Type_for_w: str
    Input_Unit_Type_for_x: str
    Input_Unit_Type_for_y: str
    Input_Unit_Type_for_z: str

class CurveQuadraticType(TypedDict, total=False):
    """"dict for CurveQuadratic"""
    Name: str
    Coefficient1_Constant: str
    Coefficient2_x: str
    Coefficient3_x2: str
    Minimum_Value_of_x: str
    Maximum_Value_of_x: str
    Minimum_Curve_Output: str
    Maximum_Curve_Output: str
    Input_Unit_Type_for_X: str
    Output_Unit_Type: str

class CurveQuadraticlinearType(TypedDict, total=False):
    """"dict for CurveQuadraticlinear"""
    Name: str
    Coefficient1_Constant: str
    Coefficient2_x: str
    Coefficient3_x2: str
    Coefficient4_y: str
    Coefficient5_xy: str
    Coefficient6_x2y: str
    Minimum_Value_of_x: str
    Maximum_Value_of_x: str
    Minimum_Value_of_y: str
    Maximum_Value_of_y: str
    Minimum_Curve_Output: str
    Maximum_Curve_Output: str
    Input_Unit_Type_for_X: str
    Input_Unit_Type_for_Y: str
    Output_Unit_Type: str

class CurveQuarticType(TypedDict, total=False):
    """"dict for CurveQuartic"""
    Name: str
    Coefficient1_Constant: str
    Coefficient2_x: str
    Coefficient3_x2: str
    Coefficient4_x3: str
    Coefficient5_x4: str
    Minimum_Value_of_x: str
    Maximum_Value_of_x: str
    Minimum_Curve_Output: str
    Maximum_Curve_Output: str
    Input_Unit_Type_for_X: str
    Output_Unit_Type: str

class CurveQuintlinearType(TypedDict, total=False):
    """"dict for CurveQuintlinear"""
    Name: str
    Coefficient1_Constant: str
    Coefficient2_v: str
    Coefficient3_w: str
    Coefficient4_x: str
    Coefficient5_y: str
    Coefficient6_z: str
    Minimum_Value_of_v: str
    Maximum_Value_of_v: str
    Minimum_Value_of_w: str
    Maximum_Value_of_w: str
    Minimum_Value_of_x: str
    Maximum_Value_of_x: str
    Minimum_Value_of_y: str
    Maximum_Value_of_y: str
    Minimum_Value_of_z: str
    Maximum_Value_of_z: str
    Minimum_Curve_Output: str
    Maximum_Curve_Output: str
    Input_Unit_Type_for_v: str
    Input_Unit_Type_for_w: str
    Input_Unit_Type_for_x: str
    Input_Unit_Type_for_y: str
    Input_Unit_Type_for_z: str

class CurveRectangularhyperbola1Type(TypedDict, total=False):
    """"dict for CurveRectangularhyperbola1"""
    Name: str
    Coefficient1_C1: str
    Coefficient2_C2: str
    Coefficient3_C3: str
    Minimum_Value_of_x: str
    Maximum_Value_of_x: str
    Minimum_Curve_Output: str
    Maximum_Curve_Output: str
    Input_Unit_Type_for_x: str
    Output_Unit_Type: str

class CurveRectangularhyperbola2Type(TypedDict, total=False):
    """"dict for CurveRectangularhyperbola2"""
    Name: str
    Coefficient1_C1: str
    Coefficient2_C2: str
    Coefficient3_C3: str
    Minimum_Value_of_x: str
    Maximum_Value_of_x: str
    Minimum_Curve_Output: str
    Maximum_Curve_Output: str
    Input_Unit_Type_for_x: str
    Output_Unit_Type: str

class CurveSigmoidType(TypedDict, total=False):
    """"dict for CurveSigmoid"""
    Name: str
    Coefficient1_C1: str
    Coefficient2_C2: str
    Coefficient3_C3: str
    Coefficient4_C4: str
    Coefficient5_C5: str
    Minimum_Value_of_x: str
    Maximum_Value_of_x: str
    Minimum_Curve_Output: str
    Maximum_Curve_Output: str
    Input_Unit_Type_for_x: str
    Output_Unit_Type: str

class CurveTriquadraticType(TypedDict, total=False):
    """"dict for CurveTriquadratic"""
    Name: str
    Coefficient1_Constant: str
    Coefficient2_x2: str
    Coefficient3_x: str
    Coefficient4_y2: str
    Coefficient5_y: str
    Coefficient6_z2: str
    Coefficient7_z: str
    Coefficient8_x2y2: str
    Coefficient9_xy: str
    Coefficient10_xy2: str
    Coefficient11_x2y: str
    Coefficient12_x2z2: str
    Coefficient13_xz: str
    Coefficient14_xz2: str
    Coefficient15_x2z: str
    Coefficient16_y2z2: str
    Coefficient17_yz: str
    Coefficient18_yz2: str
    Coefficient19_y2z: str
    Coefficient20_x2y2z2: str
    Coefficient21_x2y2z: str
    Coefficient22_x2yz2: str
    Coefficient23_xy2z2: str
    Coefficient24_x2yz: str
    Coefficient25_xy2z: str
    Coefficient26_xyz2: str
    Coefficient27_xyz: str
    Minimum_Value_of_x: str
    Maximum_Value_of_x: str
    Minimum_Value_of_y: str
    Maximum_Value_of_y: str
    Minimum_Value_of_z: str
    Maximum_Value_of_z: str
    Minimum_Curve_Output: str
    Maximum_Curve_Output: str
    Input_Unit_Type_for_X: str
    Input_Unit_Type_for_Y: str
    Input_Unit_Type_for_Z: str
    Output_Unit_Type: str

class DaylightingControlsType(TypedDict, total=False):
    """"dict for DaylightingControls"""
    Name: str
    Zone_or_Space_Name: str
    Daylighting_Method: str
    Availability_Schedule_Name: str
    Lighting_Control_Type: str
    Minimum_Input_Power_Fraction_for_Continuous_or_ContinuousOff_Dimming_Control: str
    Minimum_Light_Output_Fraction_for_Continuous_or_ContinuousOff_Dimming_Control: str
    Number_of_Stepped_Control_Steps: str
    Probability_Lighting_will_be_Reset_When_Needed_in_Manual_Stepped_Control: str
    Glare_Calculation_Daylighting_Reference_Point_Name: str
    Glare_Calculation_Azimuth_Angle_of_View_Direction_Clockwise_from_Zone_yAxis: str
    Maximum_Allowable_Discomfort_Glare_Index: str
    DElight_Gridding_Resolution: str
    Daylighting_Reference_Point_1_Name: str
    Fraction_of_Lights_Controlled_by_Reference_Point_1: str
    Illuminance_Setpoint_at_Reference_Point_1: str
    Daylighting_Reference_Point_2_Name: str
    Fraction_of_Lights_Controlled_by_Reference_Point_2: str
    Illuminance_Setpoint_at_Reference_Point_2: str
    Daylighting_Reference_Point_3_Name: str
    Fraction_of_Lights_Controlled_by_Reference_Point_3: str
    Illuminance_Setpoint_at_Reference_Point_3: str
    Daylighting_Reference_Point_4_Name: str
    Fraction_of_Lights_Controlled_by_Reference_Point_4: str
    Illuminance_Setpoint_at_Reference_Point_4: str
    Daylighting_Reference_Point_5_Name: str
    Fraction_of_Lights_Controlled_by_Reference_Point_5: str
    Illuminance_Setpoint_at_Reference_Point_5: str
    Daylighting_Reference_Point_6_Name: str
    Fraction_of_Lights_Controlled_by_Reference_Point_6: str
    Illuminance_Setpoint_at_Reference_Point_6: str
    Daylighting_Reference_Point_7_Name: str
    Fraction_of_Lights_Controlled_by_Reference_Point_7: str
    Illuminance_Setpoint_at_Reference_Point_7: str
    Daylighting_Reference_Point_8_Name: str
    Fraction_of_Lights_Controlled_by_Reference_Point_8: str
    Illuminance_Setpoint_at_Reference_Point_8: str
    Daylighting_Reference_Point_9_Name: str
    Fraction_of_Lights_Controlled_by_Reference_Point_9: str
    Illuminance_Setpoint_at_Reference_Point_9: str
    Daylighting_Reference_Point_10_Name: str
    Fraction_of_Lights_Controlled_by_Reference_Point_10: str
    Illuminance_Setpoint_at_Reference_Point_10: str

class DaylightingDelightComplexfenestrationType(TypedDict, total=False):
    """"dict for DaylightingDelightComplexfenestration"""
    Name: str
    Complex_Fenestration_Type: str
    Building_Surface_Name: str
    Window_Name: str
    Fenestration_Rotation: str

class DaylightingReferencepointType(TypedDict, total=False):
    """"dict for DaylightingReferencepoint"""
    Name: str
    Zone_or_Space_Name: str
    XCoordinate_of_Reference_Point: str
    YCoordinate_of_Reference_Point: str
    ZCoordinate_of_Reference_Point: str

class DaylightingdeviceLightwellType(TypedDict, total=False):
    """"dict for DaylightingdeviceLightwell"""
    Exterior_Window_Name: str
    Height_of_Well: str
    Perimeter_of_Bottom_of_Well: str
    Area_of_Bottom_of_Well: str
    Visible_Reflectance_of_Well_Walls: str

class DaylightingdeviceShelfType(TypedDict, total=False):
    """"dict for DaylightingdeviceShelf"""
    Name: str
    Window_Name: str
    Inside_Shelf_Name: str
    Outside_Shelf_Name: str
    Outside_Shelf_Construction_Name: str
    View_Factor_to_Outside_Shelf: str

class DaylightingdeviceTubularType(TypedDict, total=False):
    """"dict for DaylightingdeviceTubular"""
    Name: str
    Dome_Name: str
    Diffuser_Name: str
    Construction_Name: str
    Diameter: str
    Total_Length: str
    Effective_Thermal_Resistance: str
    Transition_Zone_1_Name: str
    Transition_Zone_1_Length: str
    Transition_Zone_2_Name: str
    Transition_Zone_2_Length: str
    Transition_Zone_3_Name: str
    Transition_Zone_3_Length: str
    Transition_Zone_4_Name: str
    Transition_Zone_4_Length: str

class DehumidifierDesiccantNofansType(TypedDict, total=False):
    """"dict for DehumidifierDesiccantNofans"""
    Name: str
    Availability_Schedule_Name: str
    Process_Air_Inlet_Node_Name: str
    Process_Air_Outlet_Node_Name: str
    Regeneration_Air_Inlet_Node_Name: str
    Regeneration_Fan_Inlet_Node_Name: str
    Control_Type: str
    Leaving_Maximum_Humidity_Ratio_Setpoint: str
    Nominal_Process_Air_Flow_Rate: str
    Nominal_Process_Air_Velocity: str
    Rotor_Power: str
    Regeneration_Coil_Object_Type: str
    Regeneration_Coil_Name: str
    Regeneration_Fan_Object_Type: str
    Regeneration_Fan_Name: str
    Performance_Model_Type: str
    Leaving_DryBulb_Function_of_Entering_DryBulb_and_Humidity_Ratio_Curve_Name: str
    Leaving_DryBulb_Function_of_Air_Velocity_Curve_Name: str
    Leaving_Humidity_Ratio_Function_of_Entering_DryBulb_and_Humidity_Ratio_Curve_Name: str
    Leaving_Humidity_Ratio_Function_of_Air_Velocity_Curve_Name: str
    Regeneration_Energy_Function_of_Entering_DryBulb_and_Humidity_Ratio_Curve_Name: str
    Regeneration_Energy_Function_of_Air_Velocity_Curve_Name: str
    Regeneration_Velocity_Function_of_Entering_DryBulb_and_Humidity_Ratio_Curve_Name: str
    Regeneration_Velocity_Function_of_Air_Velocity_Curve_Name: str
    Nominal_Regeneration_Temperature: str

class DehumidifierDesiccantSystemType(TypedDict, total=False):
    """"dict for DehumidifierDesiccantSystem"""
    Name: str
    Availability_Schedule_Name: str
    Desiccant_Heat_Exchanger_Object_Type: str
    Desiccant_Heat_Exchanger_Name: str
    Sensor_Node_Name: str
    Regeneration_Air_Fan_Object_Type: str
    Regeneration_Air_Fan_Name: str
    Regeneration_Air_Fan_Placement: str
    Regeneration_Air_Heater_Object_Type: str
    Regeneration_Air_Heater_Name: str
    Regeneration_Inlet_Air_Setpoint_Temperature: str
    Companion_Cooling_Coil_Object_Type: str
    Companion_Cooling_Coil_Name: str
    Companion_Cooling_Coil_Upstream_of_Dehumidifier_Process_Inlet: str
    Companion_Coil_Regeneration_Air_Heating: str
    Exhaust_Fan_Maximum_Flow_Rate: str
    Exhaust_Fan_Maximum_Power: str
    Exhaust_Fan_Power_Curve_Name: str

class DemandmanagerElectricequipmentType(TypedDict, total=False):
    """"dict for DemandmanagerElectricequipment"""
    Name: str
    Availability_Schedule_Name: str
    Limit_Control: str
    Minimum_Limit_Duration: str
    Maximum_Limit_Fraction: str
    Limit_Step_Change: str
    Selection_Control: str
    Rotation_Duration: str
    Electric_Equipment_1_Name: str
    Electric_Equipment_2_Name: str
    Electric_Equipment_3_Name: str
    Electric_Equipment_4_Name: str
    Electric_Equipment_5_Name: str
    Electric_Equipment_6_Name: str
    Electric_Equipment_7_Name: str
    Electric_Equipment_8_Name: str
    Electric_Equipment_9_Name: str
    Electric_Equipment_10_Name: str

class DemandmanagerExteriorlightsType(TypedDict, total=False):
    """"dict for DemandmanagerExteriorlights"""
    Name: str
    Availability_Schedule_Name: str
    Limit_Control: str
    Minimum_Limit_Duration: str
    Maximum_Limit_Fraction: str
    Limit_Step_Change: str
    Selection_Control: str
    Rotation_Duration: str
    Exterior_Lights_1_Name: str
    Exterior_Lights_2_Name: str
    Exterior_Lights_3_Name: str
    Exterior_Lights_4_Name: str
    Exterior_Lights_5_Name: str
    Exterior_Lights_6_Name: str
    Exterior_Lights_7_Name: str
    Exterior_Lights_8_Name: str
    Exterior_Lights_9_Name: str
    Exterior_Lights_10_Name: str

class DemandmanagerLightsType(TypedDict, total=False):
    """"dict for DemandmanagerLights"""
    Name: str
    Availability_Schedule_Name: str
    Limit_Control: str
    Minimum_Limit_Duration: str
    Maximum_Limit_Fraction: str
    Limit_Step_Change: str
    Selection_Control: str
    Rotation_Duration: str
    Lights_1_Name: str
    Lights_2_Name: str
    Lights_3_Name: str
    Lights_4_Name: str
    Lights_5_Name: str
    Lights_6_Name: str
    Lights_7_Name: str
    Lights_8_Name: str
    Lights_9_Name: str
    Lights_10_Name: str

class DemandmanagerThermostatsType(TypedDict, total=False):
    """"dict for DemandmanagerThermostats"""
    Name: str
    Availability_Schedule_Name: str
    Reset_Control: str
    Minimum_Reset_Duration: str
    Maximum_Heating_Setpoint_Reset: str
    Maximum_Cooling_Setpoint_Reset: str
    Reset_Step_Change: str
    Selection_Control: str
    Rotation_Duration: str
    Thermostat_1_Name: str
    Thermostat_2_Name: str
    Thermostat_3_Name: str
    Thermostat_4_Name: str
    Thermostat_5_Name: str
    Thermostat_6_Name: str
    Thermostat_7_Name: str
    Thermostat_8_Name: str
    Thermostat_9_Name: str
    Thermostat_10_Name: str

class DemandmanagerVentilationType(TypedDict, total=False):
    """"dict for DemandmanagerVentilation"""
    Name: str
    Availability_Schedule_Name: str
    Limit_Control: str
    Minimum_Limit_Duration: str
    Fixed_Rate: str
    Reduction_Ratio: str
    Limit_Step_Change: str
    Selection_Control: str
    Rotation_Duration: str
    Controller_Outdoor_Air_1_Name: str
    Controller_Outdoor_Air_2_Name: str
    Controller_Outdoor_Air_3_Name: str
    Controller_Outdoor_Air_4_Name: str
    Controller_Outdoor_Air_5_Name: str
    Controller_Outdoor_Air_6_Name: str
    Controller_Outdoor_Air_7_Name: str
    Controller_Outdoor_Air_8_Name: str
    Controller_Outdoor_Air_9_Name: str
    Controller_Outdoor_Air_10_Name: str

class DemandmanagerassignmentlistType(TypedDict, total=False):
    """"dict for Demandmanagerassignmentlist"""
    Name: str
    Meter_Name: str
    Demand_Limit_Schedule_Name: str
    Demand_Limit_Safety_Fraction: str
    Billing_Period_Schedule_Name: str
    Peak_Period_Schedule_Name: str
    Demand_Window_Length: str
    Demand_Manager_Priority: str
    DemandManager_1_Object_Type: str
    DemandManager_1_Name: str
    DemandManager_2_Object_Type: str
    DemandManager_2_Name: str
    DemandManager_3_Object_Type: str
    DemandManager_3_Name: str
    DemandManager_4_Object_Type: str
    DemandManager_4_Name: str
    DemandManager_5_Object_Type: str
    DemandManager_5_Name: str
    DemandManager_6_Object_Type: str
    DemandManager_6_Name: str
    DemandManager_7_Object_Type: str
    DemandManager_7_Name: str
    DemandManager_8_Object_Type: str
    DemandManager_8_Name: str
    DemandManager_9_Object_Type: str
    DemandManager_9_Name: str
    DemandManager_10_Object_Type: str
    DemandManager_10_Name: str

class DesignspecificationAirterminalSizingType(TypedDict, total=False):
    """"dict for DesignspecificationAirterminalSizing"""
    Name: str
    Fraction_of_Design_Cooling_Load: str
    Cooling_Design_Supply_Air_Temperature_Difference_Ratio: str
    Fraction_of_Design_Heating_Load: str
    Heating_Design_Supply_Air_Temperature_Difference_Ratio: str
    Fraction_of_Minimum_Outdoor_Air_Flow: str

class DesignspecificationOutdoorairType(TypedDict, total=False):
    """"dict for DesignspecificationOutdoorair"""
    Name: str
    Outdoor_Air_Method: str
    Outdoor_Air_Flow_per_Person: str
    Outdoor_Air_Flow_per_Zone_Floor_Area: str
    Outdoor_Air_Flow_per_Zone: str
    Outdoor_Air_Flow_Air_Changes_per_Hour: str
    Outdoor_Air_Schedule_Name: str
    Proportional_Control_Minimum_Outdoor_Air_Flow_Rate_Schedule_Name: str

class DesignspecificationOutdoorairSpacelistType(TypedDict, total=False):
    """"dict for DesignspecificationOutdoorairSpacelist"""
    Name: str
    Space_1_Name: str
    Space_1_Design_Specification_Outdoor_Air_Object_Name: str
    Space_2_Name: str
    Space_2_Design_Specification_Outdoor_Air_Object_Name: str
    Space_3_Name: str
    Space_3_Design_Specification_Outdoor_Air_Object_Name: str
    Space_4_Name: str
    Space_4_Design_Specification_Outdoor_Air_Object_Name: str
    Space_5_Name: str
    Space_5_Design_Specification_Outdoor_Air_Object_Name: str
    Space_6_Name: str
    Space_6_Design_Specification_Outdoor_Air_Object_Name: str
    Space_7_Name: str
    Space_7_Design_Specification_Outdoor_Air_Object_Name: str
    Space_8_Name: str
    Space_8_Design_Specification_Outdoor_Air_Object_Name: str
    Space_9_Name: str
    Space_9_Design_Specification_Outdoor_Air_Object_Name: str
    Space_10_Name: str
    Space_10_Design_Specification_Outdoor_Air_Object_Name: str
    Space_11_Name: str
    Space_11_Design_Specification_Outdoor_Air_Object_Name: str
    Space_12_Name: str
    Space_12_Design_Specification_Outdoor_Air_Object_Name: str
    Space_13_Name: str
    Space_13_Design_Specification_Outdoor_Air_Object_Name: str
    Space_14_Name: str
    Space_14_Design_Specification_Outdoor_Air_Object_Name: str
    Space_15_Name: str
    Space_15_Design_Specification_Outdoor_Air_Object_Name: str
    Space_16_Name: str
    Space_16_Design_Specification_Outdoor_Air_Object_Name: str
    Space_17_Name: str
    Space_17_Design_Specification_Outdoor_Air_Object_Name: str
    Space_18_Name: str
    Space_18_Design_Specification_Outdoor_Air_Object_Name: str
    Space_19_Name: str
    Space_19_Design_Specification_Outdoor_Air_Object_Name: str
    Space_20_Name: str
    Space_20_Design_Specification_Outdoor_Air_Object_Name: str
    Space_21_Name: str
    Space_21_Design_Specification_Outdoor_Air_Object_Name: str
    Space_22_Name: str
    Space_22_Design_Specification_Outdoor_Air_Object_Name: str
    Space_23_Name: str
    Space_23_Design_Specification_Outdoor_Air_Object_Name: str
    Space_24_Name: str
    Space_24_Design_Specification_Outdoor_Air_Object_Name: str
    Space_25_Name: str
    Space_25_Design_Specification_Outdoor_Air_Object_Name: str

class DesignspecificationZoneairdistributionType(TypedDict, total=False):
    """"dict for DesignspecificationZoneairdistribution"""
    Name: str
    Zone_Air_Distribution_Effectiveness_in_Cooling_Mode: str
    Zone_Air_Distribution_Effectiveness_in_Heating_Mode: str
    Zone_Air_Distribution_Effectiveness_Schedule_Name: str
    Zone_Secondary_Recirculation_Fraction: str
    Minimum_Zone_Ventilation_Efficiency: str

class DesignspecificationZonehvacSizingType(TypedDict, total=False):
    """"dict for DesignspecificationZonehvacSizing"""
    Name: str
    Cooling_Supply_Air_Flow_Rate_Method: str
    Cooling_Supply_Air_Flow_Rate: str
    Cooling_Supply_Air_Flow_Rate_Per_Floor_Area: str
    Cooling_Fraction_of_Autosized_Cooling_Supply_Air_Flow_Rate: str
    Cooling_Supply_Air_Flow_Rate_Per_Unit_Cooling_Capacity: str
    No_Load_Supply_Air_Flow_Rate_Method: str
    No_Load_Supply_Air_Flow_Rate: str
    No_Load_Supply_Air_Flow_Rate_Per_Floor_Area: str
    No_Load_Fraction_of_Cooling_Supply_Air_Flow_Rate: str
    No_Load_Fraction_of_Heating_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate_Method: str
    Heating_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate_Per_Floor_Area: str
    Heating_Fraction_of_Heating_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate_Per_Unit_Heating_Capacity: str
    Cooling_Design_Capacity_Method: str
    Cooling_Design_Capacity: str
    Cooling_Design_Capacity_Per_Floor_Area: str
    Fraction_of_Autosized_Cooling_Design_Capacity: str
    Heating_Design_Capacity_Method: str
    Heating_Design_Capacity: str
    Heating_Design_Capacity_Per_Floor_Area: str
    Fraction_of_Autosized_Heating_Design_Capacity: str

class DistrictcoolingType(TypedDict, total=False):
    """"dict for Districtcooling"""
    Name: str
    Chilled_Water_Inlet_Node_Name: str
    Chilled_Water_Outlet_Node_Name: str
    Nominal_Capacity: str
    Capacity_Fraction_Schedule_Name: str

class DistrictheatingSteamType(TypedDict, total=False):
    """"dict for DistrictheatingSteam"""
    Name: str
    Steam_Inlet_Node_Name: str
    Steam_Outlet_Node_Name: str
    Nominal_Capacity: str
    Capacity_Fraction_Schedule_Name: str

class DistrictheatingWaterType(TypedDict, total=False):
    """"dict for DistrictheatingWater"""
    Name: str
    Hot_Water_Inlet_Node_Name: str
    Hot_Water_Outlet_Node_Name: str
    Nominal_Capacity: str
    Capacity_Fraction_Schedule_Name: str

class DoorType(TypedDict, total=False):
    """"dict for Door"""
    Name: str
    Construction_Name: str
    Building_Surface_Name: str
    Multiplier: str
    Starting_X_Coordinate: str
    Starting_Z_Coordinate: str
    Length: str
    Height: str

class DoorInterzoneType(TypedDict, total=False):
    """"dict for DoorInterzone"""
    Name: str
    Construction_Name: str
    Building_Surface_Name: str
    Outside_Boundary_Condition_Object: str
    Multiplier: str
    Starting_X_Coordinate: str
    Starting_Z_Coordinate: str
    Length: str
    Height: str

class DuctType(TypedDict, total=False):
    """"dict for Duct"""
    Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str

class ElectricequipmentType(TypedDict, total=False):
    """"dict for Electricequipment"""
    Name: str
    Zone_or_ZoneList_or_Space_or_SpaceList_Name: str
    Schedule_Name: str
    Design_Level_Calculation_Method: str
    Design_Level: str
    Watts_per_Floor_Area: str
    Watts_per_Person: str
    Fraction_Latent: str
    Fraction_Radiant: str
    Fraction_Lost: str
    EndUse_Subcategory: str

class ElectricequipmentIteAircooledType(TypedDict, total=False):
    """"dict for ElectricequipmentIteAircooled"""
    Name: str
    Zone_or_Space_Name: str
    Air_Flow_Calculation_Method: str
    Design_Power_Input_Calculation_Method: str
    Watts_per_Unit: str
    Number_of_Units: str
    Watts_per_Floor_Area: str
    Design_Power_Input_Schedule_Name: str
    CPU_Loading_Schedule_Name: str
    CPU_Power_Input_Function_of_Loading_and_Air_Temperature_Curve_Name: str
    Design_Fan_Power_Input_Fraction: str
    Design_Fan_Air_Flow_Rate_per_Power_Input: str
    Air_Flow_Function_of_Loading_and_Air_Temperature_Curve_Name: str
    Fan_Power_Input_Function_of_Flow_Curve_Name: str
    Design_Entering_Air_Temperature: str
    Environmental_Class: str
    Air_Inlet_Connection_Type: str
    Air_Inlet_Room_Air_Model_Node_Name: str
    Air_Outlet_Room_Air_Model_Node_Name: str
    Supply_Air_Node_Name: str
    Design_Recirculation_Fraction: str
    Recirculation_Function_of_Loading_and_Supply_Temperature_Curve_Name: str
    Design_Electric_Power_Supply_Efficiency: str
    Electric_Power_Supply_Efficiency_Function_of_Part_Load_Ratio_Curve_Name: str
    Fraction_of_Electric_Power_Supply_Losses_to_Zone: str
    CPU_EndUse_Subcategory: str
    Fan_EndUse_Subcategory: str
    Electric_Power_Supply_EndUse_Subcategory: str
    Supply_Temperature_Difference: str
    Supply_Temperature_Difference_Schedule: str
    Return_Temperature_Difference: str
    Return_Temperature_Difference_Schedule: str

class ElectricloadcenterDistributionType(TypedDict, total=False):
    """"dict for ElectricloadcenterDistribution"""
    Name: str
    Generator_List_Name: str
    Generator_Operation_Scheme_Type: str
    Generator_Demand_Limit_Scheme_Purchased_Electric_Demand_Limit: str
    Generator_Track_Schedule_Name_Scheme_Schedule_Name: str
    Generator_Track_Meter_Scheme_Meter_Name: str
    Electrical_Buss_Type: str
    Inverter_Name: str
    Electrical_Storage_Object_Name: str
    Transformer_Object_Name: str
    Storage_Operation_Scheme: str
    Storage_Control_Track_Meter_Name: str
    Storage_Converter_Object_Name: str
    Maximum_Storage_State_of_Charge_Fraction: str
    Minimum_Storage_State_of_Charge_Fraction: str
    Design_Storage_Control_Charge_Power: str
    Storage_Charge_Power_Fraction_Schedule_Name: str
    Design_Storage_Control_Discharge_Power: str
    Storage_Discharge_Power_Fraction_Schedule_Name: str
    Storage_Control_Utility_Demand_Target: str
    Storage_Control_Utility_Demand_Target_Fraction_Schedule_Name: str

class ElectricloadcenterGeneratorsType(TypedDict, total=False):
    """"dict for ElectricloadcenterGenerators"""
    Name: str
    Generator_1_Name: str
    Generator_1_Object_Type: str
    Generator_1_Rated_Electric_Power_Output: str
    Generator_1_Availability_Schedule_Name: str
    Generator_1_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_2_Name: str
    Generator_2_Object_Type: str
    Generator_2_Rated_Electric_Power_Output: str
    Generator_2_Availability_Schedule_Name: str
    Generator_2_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_3_Name: str
    Generator_3_Object_Type: str
    Generator_3_Rated_Electric_Power_Output: str
    Generator_3_Availability_Schedule_Name: str
    Generator_3_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_4_Name: str
    Generator_4_Object_Type: str
    Generator_4_Rated_Electric_Power_Output: str
    Generator_4_Availability_Schedule_Name: str
    Generator_4_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_5_Name: str
    Generator_5_Object_Type: str
    Generator_5_Rated_Electric_Power_Output: str
    Generator_5_Availability_Schedule_Name: str
    Generator_5_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_6_Name: str
    Generator_6_Object_Type: str
    Generator_6_Rated_Electric_Power_Output: str
    Generator_6_Availability_Schedule_Name: str
    Generator_6_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_7_Name: str
    Generator_7_Object_Type: str
    Generator_7_Rated_Electric_Power_Output: str
    Generator_7_Availability_Schedule_Name: str
    Generator_7_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_8_Name: str
    Generator_8_Object_Type: str
    Generator_8_Rated_Electric_Power_Output: str
    Generator_8_Availability_Schedule_Name: str
    Generator_8_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_9_Name: str
    Generator_9_Object_Type: str
    Generator_9_Rated_Electric_Power_Output: str
    Generator_9_Availability_Schedule_Name: str
    Generator_9_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_10_Name: str
    Generator_10_Object_Type: str
    Generator_10_Rated_Electric_Power_Output: str
    Generator_10_Availability_Schedule_Name: str
    Generator_10_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_11_Name: str
    Generator_11_Object_Type: str
    Generator_11_Rated_Electric_Power_Output: str
    Generator_11_Availability_Schedule_Name: str
    Generator_11_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_12_Name: str
    Generator_12_Object_Type: str
    Generator_12_Rated_Electric_Power_Output: str
    Generator_12_Availability_Schedule_Name: str
    Generator_12_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_13_Name: str
    Generator_13_Object_Type: str
    Generator_13_Rated_Electric_Power_Output: str
    Generator_13_Availability_Schedule_Name: str
    Generator_13_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_14_Name: str
    Generator_14_Object_Type: str
    Generator_14_Rated_Electric_Power_Output: str
    Generator_14_Availability_Schedule_Name: str
    Generator_14_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_15_Name: str
    Generator_15_Object_Type: str
    Generator_15_Rated_Electric_Power_Output: str
    Generator_15_Availability_Schedule_Name: str
    Generator_15_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_16_Name: str
    Generator_16_Object_Type: str
    Generator_16_Rated_Electric_Power_Output: str
    Generator_16_Availability_Schedule_Name: str
    Generator_16_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_17_Name: str
    Generator_17_Object_Type: str
    Generator_17_Rated_Electric_Power_Output: str
    Generator_17_Availability_Schedule_Name: str
    Generator_17_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_18_Name: str
    Generator_18_Object_Type: str
    Generator_18_Rated_Electric_Power_Output: str
    Generator_18_Availability_Schedule_Name: str
    Generator_18_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_19_Name: str
    Generator_19_Object_Type: str
    Generator_19_Rated_Electric_Power_Output: str
    Generator_19_Availability_Schedule_Name: str
    Generator_19_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_20_Name: str
    Generator_20_Object_Type: str
    Generator_20_Rated_Electric_Power_Output: str
    Generator_20_Availability_Schedule_Name: str
    Generator_20_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_21_Name: str
    Generator_21_Object_Type: str
    Generator_21_Rated_Electric_Power_Output: str
    Generator_21_Availability_Schedule_Name: str
    Generator_21_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_22_Name: str
    Generator_22_Object_Type: str
    Generator_22_Rated_Electric_Power_Output: str
    Generator_22_Availability_Schedule_Name: str
    Generator_22_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_23_Name: str
    Generator_23_Object_Type: str
    Generator_23_Rated_Electric_Power_Output: str
    Generator_23_Availability_Schedule_Name: str
    Generator_23_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_24_Name: str
    Generator_24_Object_Type: str
    Generator_24_Rated_Electric_Power_Output: str
    Generator_24_Availability_Schedule_Name: str
    Generator_24_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_25_Name: str
    Generator_25_Object_Type: str
    Generator_25_Rated_Electric_Power_Output: str
    Generator_25_Availability_Schedule_Name: str
    Generator_25_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_26_Name: str
    Generator_26_Object_Type: str
    Generator_26_Rated_Electric_Power_Output: str
    Generator_26_Availability_Schedule_Name: str
    Generator_26_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_27_Name: str
    Generator_27_Object_Type: str
    Generator_27_Rated_Electric_Power_Output: str
    Generator_27_Availability_Schedule_Name: str
    Generator_27_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_28_Name: str
    Generator_28_Object_Type: str
    Generator_28_Rated_Electric_Power_Output: str
    Generator_28_Availability_Schedule_Name: str
    Generator_28_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_29_Name: str
    Generator_29_Object_Type: str
    Generator_29_Rated_Electric_Power_Output: str
    Generator_29_Availability_Schedule_Name: str
    Generator_29_Rated_Thermal_to_Electrical_Power_Ratio: str
    Generator_30_Name: str
    Generator_30_Object_Type: str
    Generator_30_Rated_Electric_Power_Output: str
    Generator_30_Availability_Schedule_Name: str
    Generator_30_Rated_Thermal_to_Electrical_Power_Ratio: str

class ElectricloadcenterInverterFunctionofpowerType(TypedDict, total=False):
    """"dict for ElectricloadcenterInverterFunctionofpower"""
    Name: str
    Availability_Schedule_Name: str
    Zone_Name: str
    Radiative_Fraction: str
    Efficiency_Function_of_Power_Curve_Name: str
    Rated_Maximum_Continuous_Input_Power: str
    Minimum_Efficiency: str
    Maximum_Efficiency: str
    Minimum_Power_Output: str
    Maximum_Power_Output: str
    Ancillary_Power_Consumed_In_Standby: str

class ElectricloadcenterInverterLookuptableType(TypedDict, total=False):
    """"dict for ElectricloadcenterInverterLookuptable"""
    Name: str
    Availability_Schedule_Name: str
    Zone_Name: str
    Radiative_Fraction: str
    Rated_Maximum_Continuous_Output_Power: str
    Night_Tare_Loss_Power: str
    Nominal_Voltage_Input: str
    Efficiency_at_10_Power_and_Nominal_Voltage: str
    Efficiency_at_20_Power_and_Nominal_Voltage: str
    Efficiency_at_30_Power_and_Nominal_Voltage: str

class ElectricloadcenterInverterPvwattsType(TypedDict, total=False):
    """"dict for ElectricloadcenterInverterPvwatts"""
    Name: str
    DC_to_AC_Size_Ratio: str
    Inverter_Efficiency: str

class ElectricloadcenterInverterSimpleType(TypedDict, total=False):
    """"dict for ElectricloadcenterInverterSimple"""
    Name: str
    Availability_Schedule_Name: str
    Zone_Name: str
    Radiative_Fraction: str
    Inverter_Efficiency: str

class ElectricloadcenterStorageBatteryType(TypedDict, total=False):
    """"dict for ElectricloadcenterStorageBattery"""
    Name: str
    Availability_Schedule_Name: str
    Zone_Name: str
    Radiative_Fraction: str
    Number_of_Battery_Modules_in_Parallel: str
    Number_of_Battery_Modules_in_Series: str
    Maximum_Module_Capacity: str
    Initial_Fractional_State_of_Charge: str
    Fraction_of_Available_Charge_Capacity: str
    Change_Rate_from_Bound_Charge_to_Available_Charge: str
    Fully_Charged_Module_Open_Circuit_Voltage: str
    Fully_Discharged_Module_Open_Circuit_Voltage: str
    Voltage_Change_Curve_Name_for_Charging: str
    Voltage_Change_Curve_Name_for_Discharging: str
    Module_Internal_Electrical_Resistance: str
    Maximum_Module_Discharging_Current: str
    Module_Cutoff_Voltage: str
    Module_Charge_Rate_Limit: str
    Battery_Life_Calculation: str
    Number_of_Cycle_Bins: str
    Battery_Life_Curve_Name: str

class ElectricloadcenterStorageConverterType(TypedDict, total=False):
    """"dict for ElectricloadcenterStorageConverter"""
    Name: str
    Availability_Schedule_Name: str
    Power_Conversion_Efficiency_Method: str
    Simple_Fixed_Efficiency: str
    Design_Maximum_Continuous_Input_Power: str
    Efficiency_Function_of_Power_Curve_Name: str
    Ancillary_Power_Consumed_In_Standby: str
    Zone_Name: str
    Radiative_Fraction: str

class ElectricloadcenterStorageLiionnmcbatteryType(TypedDict, total=False):
    """"dict for ElectricloadcenterStorageLiionnmcbattery"""
    Name: str
    Availability_Schedule_Name: str
    Zone_Name: str
    Radiative_Fraction: str
    Lifetime_Model: str
    Number_of_Cells_in_Series: str
    Number_of_Strings_in_Parallel: str
    Initial_Fractional_State_of_Charge: str
    DC_to_DC_Charging_Efficiency: str
    Battery_Mass: str
    Battery_Surface_Area: str
    Battery_Specific_Heat_Capacity: str
    Heat_Transfer_Coefficient_Between_Battery_and_Ambient: str
    Fully_Charged_Cell_Voltage: str
    Cell_Voltage_at_End_of_Exponential_Zone: str
    Cell_Voltage_at_End_of_Nominal_Zone: str
    Default_Nominal_Cell_Voltage: str
    Fully_Charged_Cell_Capacity: str
    Fraction_of_Cell_Capacity_Removed_at_the_End_of_Exponential_Zone: str
    Fraction_of_Cell_Capacity_Removed_at_the_End_of_Nominal_Zone: str
    Charge_Rate_at_Which_Voltage_vs_Capacity_Curve_Was_Generated: str
    Battery_Cell_Internal_Electrical_Resistance: str

class ElectricloadcenterStorageSimpleType(TypedDict, total=False):
    """"dict for ElectricloadcenterStorageSimple"""
    Name: str
    Availability_Schedule_Name: str
    Zone_Name: str
    Radiative_Fraction_for_Zone_Heat_Gains: str
    Nominal_Energetic_Efficiency_for_Charging: str
    Nominal_Discharging_Energetic_Efficiency: str
    Maximum_Storage_Capacity: str
    Maximum_Power_for_Discharging: str
    Maximum_Power_for_Charging: str
    Initial_State_of_Charge: str

class ElectricloadcenterTransformerType(TypedDict, total=False):
    """"dict for ElectricloadcenterTransformer"""
    Name: str
    Availability_Schedule_Name: str
    Transformer_Usage: str
    Zone_Name: str
    Radiative_Fraction: str
    Rated_Capacity: str
    Phase: str
    Conductor_Material: str
    Full_Load_Temperature_Rise: str
    Fraction_of_Eddy_Current_Losses: str
    Performance_Input_Method: str
    Rated_No_Load_Loss: str
    Rated_Load_Loss: str
    Nameplate_Efficiency: str
    Per_Unit_Load_for_Nameplate_Efficiency: str
    Reference_Temperature_for_Nameplate_Efficiency: str
    Per_Unit_Load_for_Maximum_Efficiency: str
    Consider_Transformer_Loss_for_Utility_Cost: str
    Meter_1_Name: str
    Meter_2_Name: str
    Meter_3_Name: str
    Meter_4_Name: str
    Meter_5_Name: str
    Meter_6_Name: str
    Meter_7_Name: str
    Meter_8_Name: str
    Meter_9_Name: str
    Meter_10_Name: str

class EnergymanagementsystemActuatorType(TypedDict, total=False):
    """"dict for EnergymanagementsystemActuator"""
    Name: str
    Actuated_Component_Unique_Name: str
    Actuated_Component_Type: str
    Actuated_Component_Control_Type: str

class EnergymanagementsystemConstructionindexvariableType(TypedDict, total=False):
    """"dict for EnergymanagementsystemConstructionindexvariable"""
    Name: str
    Construction_Object_Name: str

class EnergymanagementsystemCurveortableindexvariableType(TypedDict, total=False):
    """"dict for EnergymanagementsystemCurveortableindexvariable"""
    Name: str
    Curve_or_Table_Object_Name: str

class EnergymanagementsystemGlobalvariableType(TypedDict, total=False):
    """"dict for EnergymanagementsystemGlobalvariable"""
    Erl_Variable_1_Name: str
    Erl_Variable_2_Name: str
    Erl_Variable_3_Name: str
    Erl_Variable_4_Name: str
    Erl_Variable_5_Name: str
    Erl_Variable_6_Name: str
    Erl_Variable_7_Name: str
    Erl_Variable_8_Name: str
    Erl_Variable_9_Name: str
    Erl_Variable_10_Name: str
    Erl_Variable_11_Name: str
    Erl_Variable_12_Name: str
    Erl_Variable_13_Name: str
    Erl_Variable_14_Name: str
    Erl_Variable_15_Name: str
    Erl_Variable_16_Name: str
    Erl_Variable_17_Name: str
    Erl_Variable_18_Name: str
    Erl_Variable_19_Name: str
    Erl_Variable_20_Name: str
    Erl_Variable_21_Name: str
    Erl_Variable_22_Name: str
    Erl_Variable_23_Name: str
    Erl_Variable_24_Name: str
    Erl_Variable_25_Name: str
    Erl_Variable_26_Name: str
    Erl_Variable_27_Name: str
    Erl_Variable_28_Name: str
    Erl_Variable_29_Name: str
    Erl_Variable_30_Name: str
    Erl_Variable_31_Name: str
    Erl_Variable_32_Name: str
    Erl_Variable_33_Name: str
    Erl_Variable_34_Name: str
    Erl_Variable_35_Name: str
    Erl_Variable_36_Name: str
    Erl_Variable_37_Name: str
    Erl_Variable_38_Name: str
    Erl_Variable_39_Name: str
    Erl_Variable_40_Name: str
    Erl_Variable_41_Name: str
    Erl_Variable_42_Name: str
    Erl_Variable_43_Name: str
    Erl_Variable_44_Name: str
    Erl_Variable_45_Name: str
    Erl_Variable_46_Name: str
    Erl_Variable_47_Name: str
    Erl_Variable_48_Name: str
    Erl_Variable_49_Name: str

class EnergymanagementsystemInternalvariableType(TypedDict, total=False):
    """"dict for EnergymanagementsystemInternalvariable"""
    Name: str
    Internal_Data_Index_Key_Name: str
    Internal_Data_Type: str

class EnergymanagementsystemMeteredoutputvariableType(TypedDict, total=False):
    """"dict for EnergymanagementsystemMeteredoutputvariable"""
    Name: str
    EMS_Variable_Name: str
    Update_Frequency: str
    EMS_Program_or_Subroutine_Name: str
    Resource_Type: str
    Group_Type: str
    EndUse_Category: str
    EndUse_Subcategory: str
    Units: str

class EnergymanagementsystemOutputvariableType(TypedDict, total=False):
    """"dict for EnergymanagementsystemOutputvariable"""
    Name: str
    EMS_Variable_Name: str
    Type_of_Data_in_Variable: str
    Update_Frequency: str
    EMS_Program_or_Subroutine_Name: str
    Units: str

class EnergymanagementsystemProgramType(TypedDict, total=False):
    """"dict for EnergymanagementsystemProgram"""
    Name: str
    Program_Line_1: str
    Program_Line_2: str
    Program_Line_3: str
    Program_Line_4: str
    Program_Line_5: str
    Program_Line_6: str
    Program_Line_7: str
    Program_Line_8: str
    Program_Line_9: str
    Program_Line_10: str
    Program_Line_11: str
    Program_Line_12: str
    Program_Line_13: str
    Program_Line_14: str
    Program_Line_15: str
    Program_Line_16: str
    Program_Line_17: str
    Program_Line_18: str
    Program_Line_19: str
    Program_Line_20: str
    Program_Line_21: str
    Program_Line_22: str
    Program_Line_23: str
    Program_Line_24: str
    Program_Line_25: str
    Program_Line_26: str
    Program_Line_27: str
    Program_Line_28: str
    Program_Line_29: str
    Program_Line_30: str
    Program_Line_31: str
    Program_Line_32: str
    Program_Line_33: str
    Program_Line_34: str
    Program_Line_35: str
    Program_Line_36: str
    Program_Line_37: str
    Program_Line_38: str
    Program_Line_39: str
    Program_Line_40: str
    Program_Line_41: str
    Program_Line_42: str
    Program_Line_43: str
    Program_Line_44: str
    Program_Line_45: str
    Program_Line_46: str
    Program_Line_47: str
    Program_Line_48: str
    Program_Line_49: str

class EnergymanagementsystemProgramcallingmanagerType(TypedDict, total=False):
    """"dict for EnergymanagementsystemProgramcallingmanager"""
    Name: str
    EnergyPlus_Model_Calling_Point: str
    Program_Name_1: str
    Program_Name_2: str
    Program_Name_3: str
    Program_Name_4: str
    Program_Name_5: str
    Program_Name_6: str
    Program_Name_7: str
    Program_Name_8: str
    Program_Name_9: str
    Program_Name_10: str
    Program_Name_11: str
    Program_Name_12: str
    Program_Name_13: str
    Program_Name_14: str
    Program_Name_15: str
    Program_Name_16: str
    Program_Name_17: str
    Program_Name_18: str
    Program_Name_19: str
    Program_Name_20: str
    Program_Name_21: str
    Program_Name_22: str
    Program_Name_23: str
    Program_Name_24: str
    Program_Name_25: str

class EnergymanagementsystemSensorType(TypedDict, total=False):
    """"dict for EnergymanagementsystemSensor"""
    Name: str
    OutputVariable_or_OutputMeter_Index_Key_Name: str
    OutputVariable_or_OutputMeter_Name: str

class EnergymanagementsystemSubroutineType(TypedDict, total=False):
    """"dict for EnergymanagementsystemSubroutine"""
    Name: str
    Program_Line_1: str
    Program_Line_2: str
    Program_Line_3: str
    Program_Line_4: str
    Program_Line_5: str
    Program_Line_6: str
    Program_Line_7: str
    Program_Line_8: str
    Program_Line_9: str
    Program_Line_10: str
    Program_Line_11: str
    Program_Line_12: str
    Program_Line_13: str
    Program_Line_14: str
    Program_Line_15: str
    Program_Line_16: str
    Program_Line_17: str
    Program_Line_18: str
    Program_Line_19: str
    Program_Line_20: str
    Program_Line_21: str
    Program_Line_22: str
    Program_Line_23: str
    Program_Line_24: str
    Program_Line_25: str
    Program_Line_26: str
    Program_Line_27: str
    Program_Line_28: str
    Program_Line_29: str
    Program_Line_30: str
    Program_Line_31: str
    Program_Line_32: str
    Program_Line_33: str
    Program_Line_34: str
    Program_Line_35: str
    Program_Line_36: str
    Program_Line_37: str
    Program_Line_38: str
    Program_Line_39: str
    Program_Line_40: str
    Program_Line_41: str
    Program_Line_42: str
    Program_Line_43: str
    Program_Line_44: str
    Program_Line_45: str
    Program_Line_46: str
    Program_Line_47: str
    Program_Line_48: str
    Program_Line_49: str

class EnergymanagementsystemTrendvariableType(TypedDict, total=False):
    """"dict for EnergymanagementsystemTrendvariable"""
    Name: str
    EMS_Variable_Name: str
    Number_of_Timesteps_to_be_Logged: str

class EnvironmentalimpactfactorsType(TypedDict, total=False):
    """"dict for Environmentalimpactfactors"""
    District_Heating_Water_Efficiency: str
    District_Cooling_COP: str
    District_Heating_Steam_Conversion_Efficiency: str
    Total_Carbon_Equivalent_Emission_Factor_From_N2O: str
    Total_Carbon_Equivalent_Emission_Factor_From_CH4: str
    Total_Carbon_Equivalent_Emission_Factor_From_CO2: str

class EvaporativecoolerDirectCeldekpadType(TypedDict, total=False):
    """"dict for EvaporativecoolerDirectCeldekpad"""
    Name: str
    Availability_Schedule_Name: str
    Direct_Pad_Area: str
    Direct_Pad_Depth: str
    Recirculating_Water_Pump_Power_Consumption: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Control_Type: str
    Water_Supply_Storage_Tank_Name: str

class EvaporativecoolerDirectResearchspecialType(TypedDict, total=False):
    """"dict for EvaporativecoolerDirectResearchspecial"""
    Name: str
    Availability_Schedule_Name: str
    Cooler_Design_Effectiveness: str
    Effectiveness_Flow_Ratio_Modifier_Curve_Name: str
    Primary_Air_Design_Flow_Rate: str
    Recirculating_Water_Pump_Design_Power: str
    Water_Pump_Power_Sizing_Factor: str
    Water_Pump_Power_Modifier_Curve_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Sensor_Node_Name: str
    Water_Supply_Storage_Tank_Name: str
    Drift_Loss_Fraction: str
    Blowdown_Concentration_Ratio: str
    Evaporative_Operation_Minimum_Drybulb_Temperature: str
    Evaporative_Operation_Maximum_Limit_Wetbulb_Temperature: str
    Evaporative_Operation_Maximum_Limit_Drybulb_Temperature: str

class EvaporativecoolerIndirectCeldekpadType(TypedDict, total=False):
    """"dict for EvaporativecoolerIndirectCeldekpad"""
    Name: str
    Availability_Schedule_Name: str
    Direct_Pad_Area: str
    Direct_Pad_Depth: str
    Recirculating_Water_Pump_Power_Consumption: str
    Secondary_Air_Fan_Flow_Rate: str
    Secondary_Air_Fan_Total_Efficiency: str
    Secondary_Air_Fan_Delta_Pressure: str
    Indirect_Heat_Exchanger_Effectiveness: str
    Primary_Air_Inlet_Node_Name: str
    Primary_Air_Outlet_Node_Name: str
    Control_Type: str
    Water_Supply_Storage_Tank_Name: str
    Secondary_Air_Inlet_Node_Name: str

class EvaporativecoolerIndirectResearchspecialType(TypedDict, total=False):
    """"dict for EvaporativecoolerIndirectResearchspecial"""
    Name: str
    Availability_Schedule_Name: str
    Cooler_Wetbulb_Design_Effectiveness: str
    Wetbulb_Effectiveness_Flow_Ratio_Modifier_Curve_Name: str
    Cooler_Drybulb_Design_Effectiveness: str
    Drybulb_Effectiveness_Flow_Ratio_Modifier_Curve_Name: str
    Recirculating_Water_Pump_Design_Power: str
    Water_Pump_Power_Sizing_Factor: str
    Water_Pump_Power_Modifier_Curve_Name: str
    Secondary_Air_Design_Flow_Rate: str
    Secondary_Air_Flow_Scaling_Factor: str
    Secondary_Air_Fan_Design_Power: str
    Secondary_Air_Fan_Sizing_Specific_Power: str
    Secondary_Air_Fan_Power_Modifier_Curve_Name: str
    Primary_Air_Inlet_Node_Name: str
    Primary_Air_Outlet_Node_Name: str
    Primary_Air_Design_Flow_Rate: str
    Dewpoint_Effectiveness_Factor: str
    Secondary_Air_Inlet_Node_Name: str
    Secondary_Air_Outlet_Node_Name: str
    Sensor_Node_Name: str
    Relief_Air_Inlet_Node_Name: str
    Water_Supply_Storage_Tank_Name: str
    Drift_Loss_Fraction: str
    Blowdown_Concentration_Ratio: str
    Evaporative_Operation_Minimum_Limit_Secondary_Air_Drybulb_Temperature: str
    Evaporative_Operation_Maximum_Limit_Outdoor_Wetbulb_Temperature: str
    Dry_Operation_Maximum_Limit_Outdoor_Drybulb_Temperature: str

class EvaporativecoolerIndirectWetcoilType(TypedDict, total=False):
    """"dict for EvaporativecoolerIndirectWetcoil"""
    Name: str
    Availability_Schedule_Name: str
    Coil_Maximum_Efficiency: str
    Coil_Flow_Ratio: str
    Recirculating_Water_Pump_Power_Consumption: str
    Secondary_Air_Fan_Flow_Rate: str
    Secondary_Air_Fan_Total_Efficiency: str
    Secondary_Air_Fan_Delta_Pressure: str
    Primary_Air_Inlet_Node_Name: str
    Primary_Air_Outlet_Node_Name: str
    Control_Type: str
    Water_Supply_Storage_Tank_Name: str
    Secondary_Air_Inlet_Node_Name: str

class EvaporativefluidcoolerSinglespeedType(TypedDict, total=False):
    """"dict for EvaporativefluidcoolerSinglespeed"""
    Name: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    Design_Air_Flow_Rate: str
    Design_Air_Flow_Rate_Fan_Power: str
    Design_Spray_Water_Flow_Rate: str
    Performance_Input_Method: str
    Outdoor_Air_Inlet_Node_Name: str
    Heat_Rejection_Capacity_and_Nominal_Capacity_Sizing_Ratio: str
    Standard_Design_Capacity: str
    Design_Air_Flow_Rate_Ufactor_Times_Area_Value: str
    Design_Water_Flow_Rate: str
    User_Specified_Design_Capacity: str
    Design_Entering_Water_Temperature: str
    Design_Entering_Air_Temperature: str
    Design_Entering_Air_Wetbulb_Temperature: str
    Capacity_Control: str
    Sizing_Factor: str
    Evaporation_Loss_Mode: str
    Evaporation_Loss_Factor: str
    Drift_Loss_Percent: str
    Blowdown_Calculation_Mode: str
    Blowdown_Concentration_Ratio: str
    Blowdown_Makeup_Water_Usage_Schedule_Name: str
    Supply_Water_Storage_Tank_Name: str

class EvaporativefluidcoolerTwospeedType(TypedDict, total=False):
    """"dict for EvaporativefluidcoolerTwospeed"""
    Name: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    High_Fan_Speed_Air_Flow_Rate: str
    High_Fan_Speed_Fan_Power: str
    Low_Fan_Speed_Air_Flow_Rate: str
    Low_Fan_Speed_Air_Flow_Rate_Sizing_Factor: str
    Low_Fan_Speed_Fan_Power: str
    Low_Fan_Speed_Fan_Power_Sizing_Factor: str
    Design_Spray_Water_Flow_Rate: str
    Performance_Input_Method: str
    Outdoor_Air_Inlet_Node_Name: str
    Heat_Rejection_Capacity_and_Nominal_Capacity_Sizing_Ratio: str
    High_Speed_Standard_Design_Capacity: str
    Low_Speed_Standard_Design_Capacity: str
    Low_Speed_Standard_Capacity_Sizing_Factor: str
    High_Fan_Speed_Ufactor_Times_Area_Value: str
    Low_Fan_Speed_Ufactor_Times_Area_Value: str
    Low_Fan_Speed_UFactor_Times_Area_Sizing_Factor: str
    Design_Water_Flow_Rate: str
    High_Speed_User_Specified_Design_Capacity: str
    Low_Speed_User_Specified_Design_Capacity: str
    Low_Speed_User_Specified_Design_Capacity_Sizing_Factor: str
    Design_Entering_Water_Temperature: str
    Design_Entering_Air_Temperature: str
    Design_Entering_Air_Wetbulb_Temperature: str
    High_Speed_Sizing_Factor: str
    Evaporation_Loss_Mode: str
    Evaporation_Loss_Factor: str
    Drift_Loss_Percent: str
    Blowdown_Calculation_Mode: str
    Blowdown_Concentration_Ratio: str
    Blowdown_Makeup_Water_Usage_Schedule_Name: str
    Supply_Water_Storage_Tank_Name: str

class ExteriorFuelequipmentType(TypedDict, total=False):
    """"dict for ExteriorFuelequipment"""
    Name: str
    Fuel_Use_Type: str
    Schedule_Name: str
    Design_Level: str
    EndUse_Subcategory: str

class ExteriorLightsType(TypedDict, total=False):
    """"dict for ExteriorLights"""
    Name: str
    Schedule_Name: str
    Design_Level: str
    Control_Option: str
    EndUse_Subcategory: str

class ExteriorWaterequipmentType(TypedDict, total=False):
    """"dict for ExteriorWaterequipment"""
    Name: str
    Fuel_Use_Type: str
    Schedule_Name: str
    Design_Level: str
    EndUse_Subcategory: str

class ExternalinterfaceType(TypedDict, total=False):
    """"dict for Externalinterface"""
    Name_of_External_Interface: str

class ExternalinterfaceActuatorType(TypedDict, total=False):
    """"dict for ExternalinterfaceActuator"""
    Name: str
    Actuated_Component_Unique_Name: str
    Actuated_Component_Type: str
    Actuated_Component_Control_Type: str
    Optional_Initial_Value: str

class ExternalinterfaceFunctionalmockupunitexportFromVariableType(TypedDict, total=False):
    """"dict for ExternalinterfaceFunctionalmockupunitexportFromVariable"""
    OutputVariable_Index_Key_Name: str
    OutputVariable_Name: str
    FMU_Variable_Name: str

class ExternalinterfaceFunctionalmockupunitexportToActuatorType(TypedDict, total=False):
    """"dict for ExternalinterfaceFunctionalmockupunitexportToActuator"""
    Name: str
    Actuated_Component_Unique_Name: str
    Actuated_Component_Type: str
    Actuated_Component_Control_Type: str
    FMU_Variable_Name: str
    Initial_Value: str

class ExternalinterfaceFunctionalmockupunitexportToScheduleType(TypedDict, total=False):
    """"dict for ExternalinterfaceFunctionalmockupunitexportToSchedule"""
    Schedule_Name: str
    Schedule_Type_Limits_Names: str
    FMU_Variable_Name: str
    Initial_Value: str

class ExternalinterfaceFunctionalmockupunitexportToVariableType(TypedDict, total=False):
    """"dict for ExternalinterfaceFunctionalmockupunitexportToVariable"""
    Name: str
    FMU_Variable_Name: str
    Initial_Value: str

class ExternalinterfaceFunctionalmockupunitimportType(TypedDict, total=False):
    """"dict for ExternalinterfaceFunctionalmockupunitimport"""
    FMU_File_Name: str
    FMU_Timeout: str
    FMU_LoggingOn: str

class ExternalinterfaceFunctionalmockupunitimportFromVariableType(TypedDict, total=False):
    """"dict for ExternalinterfaceFunctionalmockupunitimportFromVariable"""
    OutputVariable_Index_Key_Name: str
    OutputVariable_Name: str
    FMU_File_Name: str
    FMU_Instance_Name: str
    FMU_Variable_Name: str

class ExternalinterfaceFunctionalmockupunitimportToActuatorType(TypedDict, total=False):
    """"dict for ExternalinterfaceFunctionalmockupunitimportToActuator"""
    Name: str
    Actuated_Component_Unique_Name: str
    Actuated_Component_Type: str
    Actuated_Component_Control_Type: str
    FMU_File_Name: str
    FMU_Instance_Name: str
    FMU_Variable_Name: str
    Initial_Value: str

class ExternalinterfaceFunctionalmockupunitimportToScheduleType(TypedDict, total=False):
    """"dict for ExternalinterfaceFunctionalmockupunitimportToSchedule"""
    Name: str
    Schedule_Type_Limits_Names: str
    FMU_File_Name: str
    FMU_Instance_Name: str
    FMU_Variable_Name: str
    Initial_Value: str

class ExternalinterfaceFunctionalmockupunitimportToVariableType(TypedDict, total=False):
    """"dict for ExternalinterfaceFunctionalmockupunitimportToVariable"""
    Name: str
    FMU_File_Name: str
    FMU_Instance_Name: str
    FMU_Variable_Name: str
    Initial_Value: str

class ExternalinterfaceScheduleType(TypedDict, total=False):
    """"dict for ExternalinterfaceSchedule"""
    Name: str
    Schedule_Type_Limits_Name: str
    Initial_Value: str

class ExternalinterfaceVariableType(TypedDict, total=False):
    """"dict for ExternalinterfaceVariable"""
    Name: str
    Initial_Value: str

class FanComponentmodelType(TypedDict, total=False):
    """"dict for FanComponentmodel"""
    Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Availability_Schedule_Name: str
    Maximum_Flow_Rate: str
    Minimum_Flow_Rate: str
    Fan_Sizing_Factor: str
    Fan_Wheel_Diameter: str
    Fan_Outlet_Area: str
    Maximum_Fan_Static_Efficiency: str
    Euler_Number_at_Maximum_Fan_Static_Efficiency: str
    Maximum_Dimensionless_Fan_Airflow: str
    Motor_Fan_Pulley_Ratio: str
    Belt_Maximum_Torque: str
    Belt_Sizing_Factor: str
    Belt_Fractional_Torque_Transition: str
    Motor_Maximum_Speed: str
    Maximum_Motor_Output_Power: str
    Motor_Sizing_Factor: str
    Motor_In_Airstream_Fraction: str
    VFD_Efficiency_Type: str
    Maximum_VFD_Output_Power: str
    VFD_Sizing_Factor: str
    Fan_Pressure_Rise_Curve_Name: str
    Duct_Static_Pressure_Reset_Curve_Name: str
    Normalized_Fan_Static_Efficiency_Curve_NameNonStall_Region: str
    Normalized_Fan_Static_Efficiency_Curve_NameStall_Region: str
    Normalized_Dimensionless_Airflow_Curve_NameNonStall_Region: str
    Normalized_Dimensionless_Airflow_Curve_NameStall_Region: str
    Maximum_Belt_Efficiency_Curve_Name: str
    Normalized_Belt_Efficiency_Curve_Name__Region_1: str
    Normalized_Belt_Efficiency_Curve_Name__Region_2: str
    Normalized_Belt_Efficiency_Curve_Name__Region_3: str
    Maximum_Motor_Efficiency_Curve_Name: str
    Normalized_Motor_Efficiency_Curve_Name: str
    VFD_Efficiency_Curve_Name: str
    EndUse_Subcategory: str

class FanConstantvolumeType(TypedDict, total=False):
    """"dict for FanConstantvolume"""
    Name: str
    Availability_Schedule_Name: str
    Fan_Total_Efficiency: str
    Pressure_Rise: str
    Maximum_Flow_Rate: str
    Motor_Efficiency: str
    Motor_In_Airstream_Fraction: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    EndUse_Subcategory: str

class FanOnoffType(TypedDict, total=False):
    """"dict for FanOnoff"""
    Name: str
    Availability_Schedule_Name: str
    Fan_Total_Efficiency: str
    Pressure_Rise: str
    Maximum_Flow_Rate: str
    Motor_Efficiency: str
    Motor_In_Airstream_Fraction: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Fan_Power_Ratio_Function_of_Speed_Ratio_Curve_Name: str
    Fan_Efficiency_Ratio_Function_of_Speed_Ratio_Curve_Name: str
    EndUse_Subcategory: str

class FanSystemmodelType(TypedDict, total=False):
    """"dict for FanSystemmodel"""
    Name: str
    Availability_Schedule_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Design_Maximum_Air_Flow_Rate: str
    Speed_Control_Method: str
    Electric_Power_Minimum_Flow_Rate_Fraction: str
    Design_Pressure_Rise: str
    Motor_Efficiency: str
    Motor_In_Air_Stream_Fraction: str
    Design_Electric_Power_Consumption: str
    Design_Power_Sizing_Method: str
    Electric_Power_Per_Unit_Flow_Rate: str
    Electric_Power_Per_Unit_Flow_Rate_Per_Unit_Pressure: str
    Fan_Total_Efficiency: str
    Electric_Power_Function_of_Flow_Fraction_Curve_Name: str
    Night_Ventilation_Mode_Pressure_Rise: str
    Night_Ventilation_Mode_Flow_Fraction: str
    Motor_Loss_Zone_Name: str
    Motor_Loss_Radiative_Fraction: str
    EndUse_Subcategory: str
    Number_of_Speeds: str
    Speed_1_Flow_Fraction: str
    Speed_1_Electric_Power_Fraction: str
    Speed_2_Flow_Fraction: str
    Speed_2_Electric_Power_Fraction: str
    Speed_3_Flow_Fraction: str
    Speed_3_Electric_Power_Fraction: str
    Speed_n_Flow_Fraction: str
    Speed_n_Electric_Power_Fraction: str

class FanVariablevolumeType(TypedDict, total=False):
    """"dict for FanVariablevolume"""
    Name: str
    Availability_Schedule_Name: str
    Fan_Total_Efficiency: str
    Pressure_Rise: str
    Maximum_Flow_Rate: str
    Fan_Power_Minimum_Flow_Rate_Input_Method: str
    Fan_Power_Minimum_Flow_Fraction: str
    Fan_Power_Minimum_Air_Flow_Rate: str
    Motor_Efficiency: str
    Motor_In_Airstream_Fraction: str
    Fan_Power_Coefficient_1: str
    Fan_Power_Coefficient_2: str
    Fan_Power_Coefficient_3: str
    Fan_Power_Coefficient_4: str
    Fan_Power_Coefficient_5: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    EndUse_Subcategory: str

class FanZoneexhaustType(TypedDict, total=False):
    """"dict for FanZoneexhaust"""
    Name: str
    Availability_Schedule_Name: str
    Fan_Total_Efficiency: str
    Pressure_Rise: str
    Maximum_Flow_Rate: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    EndUse_Subcategory: str
    Flow_Fraction_Schedule_Name: str
    System_Availability_Manager_Coupling_Mode: str
    Minimum_Zone_Temperature_Limit_Schedule_Name: str
    Balanced_Exhaust_Fraction_Schedule_Name: str

class FanperformanceNightventilationType(TypedDict, total=False):
    """"dict for FanperformanceNightventilation"""
    Fan_Name: str
    Fan_Total_Efficiency: str
    Pressure_Rise: str
    Maximum_Flow_Rate: str
    Motor_Efficiency: str
    Motor_in_Airstream_Fraction: str

class FaultmodelEnthalpysensoroffsetOutdoorairType(TypedDict, total=False):
    """"dict for FaultmodelEnthalpysensoroffsetOutdoorair"""
    Name: str
    Availability_Schedule_Name: str
    Severity_Schedule_Name: str
    Controller_Object_Type: str
    Controller_Object_Name: str
    Enthalpy_Sensor_Offset: str

class FaultmodelEnthalpysensoroffsetReturnairType(TypedDict, total=False):
    """"dict for FaultmodelEnthalpysensoroffsetReturnair"""
    Name: str
    Availability_Schedule_Name: str
    Severity_Schedule_Name: str
    Controller_Object_Type: str
    Controller_Object_Name: str
    Enthalpy_Sensor_Offset: str

class FaultmodelFoulingAirfilterType(TypedDict, total=False):
    """"dict for FaultmodelFoulingAirfilter"""
    Name: str
    Fan_Object_Type: str
    Fan_Name: str
    Availability_Schedule_Name: str
    Pressure_Fraction_Schedule_Name: str
    Fan_Curve_Name: str

class FaultmodelFoulingBoilerType(TypedDict, total=False):
    """"dict for FaultmodelFoulingBoiler"""
    Name: str
    Availability_Schedule_Name: str
    Severity_Schedule_Name: str
    Boiler_Object_Type: str
    Boiler_Object_Name: str
    Fouling_Factor: str

class FaultmodelFoulingChillerType(TypedDict, total=False):
    """"dict for FaultmodelFoulingChiller"""
    Name: str
    Availability_Schedule_Name: str
    Severity_Schedule_Name: str
    Chiller_Object_Type: str
    Chiller_Object_Name: str
    Fouling_Factor: str

class FaultmodelFoulingCoilType(TypedDict, total=False):
    """"dict for FaultmodelFoulingCoil"""
    Name: str
    Coil_Name: str
    Availability_Schedule_Name: str
    Severity_Schedule_Name: str
    Fouling_Input_Method: str
    UAFouled: str
    Water_Side_Fouling_Factor: str
    Air_Side_Fouling_Factor: str
    Outside_Coil_Surface_Area: str
    Inside_to_Outside_Coil_Surface_Area_Ratio: str

class FaultmodelFoulingCoolingtowerType(TypedDict, total=False):
    """"dict for FaultmodelFoulingCoolingtower"""
    Name: str
    Availability_Schedule_Name: str
    Severity_Schedule_Name: str
    Cooling_Tower_Object_Type: str
    Cooling_Tower_Object_Name: str
    Reference_UA_Reduction_Factor: str

class FaultmodelFoulingEvaporativecoolerType(TypedDict, total=False):
    """"dict for FaultmodelFoulingEvaporativecooler"""
    Name: str
    Availability_Schedule_Name: str
    Severity_Schedule_Name: str
    Evaporative_Cooler_Object_Type: str
    Evaporative_Cooler_Object_Name: str
    Fouling_Factor: str

class FaultmodelHumidistatoffsetType(TypedDict, total=False):
    """"dict for FaultmodelHumidistatoffset"""
    Name: str
    Humidistat_Name: str
    Humidistat_Offset_Type: str
    Availability_Schedule_Name: str
    Severity_Schedule_Name: str
    Reference_Humidistat_Offset: str
    Related_Thermostat_Offset_Fault_Name: str

class FaultmodelHumiditysensoroffsetOutdoorairType(TypedDict, total=False):
    """"dict for FaultmodelHumiditysensoroffsetOutdoorair"""
    Name: str
    Availability_Schedule_Name: str
    Severity_Schedule_Name: str
    Controller_Object_Type: str
    Controller_Object_Name: str
    Humidity_Sensor_Offset: str

class FaultmodelTemperaturesensoroffsetChillersupplywaterType(TypedDict, total=False):
    """"dict for FaultmodelTemperaturesensoroffsetChillersupplywater"""
    Name: str
    Availability_Schedule_Name: str
    Severity_Schedule_Name: str
    Chiller_Object_Type: str
    Chiller_Object_Name: str
    Reference_Sensor_Offset: str

class FaultmodelTemperaturesensoroffsetCoilsupplyairType(TypedDict, total=False):
    """"dict for FaultmodelTemperaturesensoroffsetCoilsupplyair"""
    Name: str
    Availability_Schedule_Name: str
    Severity_Schedule_Name: str
    Coil_Object_Type: str
    Coil_Object_Name: str
    Water_Coil_Controller_Name: str
    Reference_Sensor_Offset: str

class FaultmodelTemperaturesensoroffsetCondensersupplywaterType(TypedDict, total=False):
    """"dict for FaultmodelTemperaturesensoroffsetCondensersupplywater"""
    Name: str
    Availability_Schedule_Name: str
    Severity_Schedule_Name: str
    Cooling_Tower_Object_Type: str
    Cooling_Tower_Object_Name: str
    Reference_Sensor_Offset: str

class FaultmodelTemperaturesensoroffsetOutdoorairType(TypedDict, total=False):
    """"dict for FaultmodelTemperaturesensoroffsetOutdoorair"""
    Name: str
    Availability_Schedule_Name: str
    Severity_Schedule_Name: str
    Controller_Object_Type: str
    Controller_Object_Name: str
    Temperature_Sensor_Offset: str

class FaultmodelTemperaturesensoroffsetReturnairType(TypedDict, total=False):
    """"dict for FaultmodelTemperaturesensoroffsetReturnair"""
    Name: str
    Availability_Schedule_Name: str
    Severity_Schedule_Name: str
    Controller_Object_Type: str
    Controller_Object_Name: str
    Temperature_Sensor_Offset: str

class FaultmodelThermostatoffsetType(TypedDict, total=False):
    """"dict for FaultmodelThermostatoffset"""
    Name: str
    Thermostat_Name: str
    Availability_Schedule_Name: str
    Severity_Schedule_Name: str
    Reference_Thermostat_Offset: str

class FenestrationsurfaceDetailedType(TypedDict, total=False):
    """"dict for FenestrationsurfaceDetailed"""
    Name: str
    Surface_Type: str
    Construction_Name: str
    Building_Surface_Name: str
    Outside_Boundary_Condition_Object: str
    View_Factor_to_Ground: str
    Frame_and_Divider_Name: str
    Multiplier: str
    Number_of_Vertices: str
    Vertex_1_Xcoordinate: str
    Vertex_1_Ycoordinate: str
    Vertex_1_Zcoordinate: str
    Vertex_2_Xcoordinate: str
    Vertex_2_Ycoordinate: str
    Vertex_2_Zcoordinate: str
    Vertex_3_Xcoordinate: str
    Vertex_3_Ycoordinate: str
    Vertex_3_Zcoordinate: str
    Vertex_4_Xcoordinate: str
    Vertex_4_Ycoordinate: str
    Vertex_4_Zcoordinate: str

class FloorAdiabaticType(TypedDict, total=False):
    """"dict for FloorAdiabatic"""
    Name: str
    Construction_Name: str
    Zone_Name: str
    Space_Name: str
    Azimuth_Angle: str
    Tilt_Angle: str
    Starting_X_Coordinate: str
    Starting_Y_Coordinate: str
    Starting_Z_Coordinate: str
    Length: str
    Width: str

class FloorDetailedType(TypedDict, total=False):
    """"dict for FloorDetailed"""
    Name: str
    Construction_Name: str
    Zone_Name: str
    Space_Name: str
    Outside_Boundary_Condition: str
    Outside_Boundary_Condition_Object: str
    Sun_Exposure: str
    Wind_Exposure: str
    View_Factor_to_Ground: str
    Number_of_Vertices: str
    Vertex_1_Xcoordinate: str
    Vertex_1_Ycoordinate: str
    Vertex_1_Zcoordinate: str
    Vertex_2_Xcoordinate: str
    Vertex_2_Ycoordinate: str
    Vertex_2_Zcoordinate: str
    Vertex_3_Xcoordinate: str
    Vertex_3_Ycoordinate: str
    Vertex_3_Zcoordinate: str
    Vertex_4_Xcoordinate: str
    Vertex_4_Ycoordinate: str
    Vertex_4_Zcoordinate: str
    Vertex_5_Xcoordinate: str
    Vertex_5_Ycoordinate: str
    Vertex_5_Zcoordinate: str
    Vertex_6_Xcoordinate: str
    Vertex_6_Ycoordinate: str
    Vertex_6_Zcoordinate: str
    Vertex_7_Xcoordinate: str
    Vertex_7_Ycoordinate: str
    Vertex_7_Zcoordinate: str
    Vertex_8_Xcoordinate: str
    Vertex_8_Ycoordinate: str
    Vertex_8_Zcoordinate: str
    Vertex_9_Xcoordinate: str
    Vertex_9_Ycoordinate: str
    Vertex_9_Zcoordinate: str
    Vertex_10_Xcoordinate: str
    Vertex_10_Ycoordinate: str
    Vertex_10_Zcoordinate: str

class FloorGroundcontactType(TypedDict, total=False):
    """"dict for FloorGroundcontact"""
    Name: str
    Construction_Name: str
    Zone_Name: str
    Space_Name: str
    Azimuth_Angle: str
    Tilt_Angle: str
    Starting_X_Coordinate: str
    Starting_Y_Coordinate: str
    Starting_Z_Coordinate: str
    Length: str
    Width: str

class FloorInterzoneType(TypedDict, total=False):
    """"dict for FloorInterzone"""
    Name: str
    Construction_Name: str
    Zone_Name: str
    Space_Name: str
    Outside_Boundary_Condition_Object: str
    Azimuth_Angle: str
    Tilt_Angle: str
    Starting_X_Coordinate: str
    Starting_Y_Coordinate: str
    Starting_Z_Coordinate: str
    Length: str
    Width: str

class FluidcoolerSinglespeedType(TypedDict, total=False):
    """"dict for FluidcoolerSinglespeed"""
    Name: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    Performance_Input_Method: str
    Design_Air_Flow_Rate_Ufactor_Times_Area_Value: str
    Nominal_Capacity: str
    Design_Entering_Water_Temperature: str
    Design_Entering_Air_Temperature: str
    Design_Entering_Air_Wetbulb_Temperature: str
    Design_Water_Flow_Rate: str
    Design_Air_Flow_Rate: str
    Design_Air_Flow_Rate_Fan_Power: str
    Outdoor_Air_Inlet_Node_Name: str

class FluidcoolerTwospeedType(TypedDict, total=False):
    """"dict for FluidcoolerTwospeed"""
    Name: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    Performance_Input_Method: str
    High_Fan_Speed_Ufactor_Times_Area_Value: str
    Low_Fan_Speed_Ufactor_Times_Area_Value: str
    Low_Fan_Speed_UFactor_Times_Area_Sizing_Factor: str
    High_Speed_Nominal_Capacity: str
    Low_Speed_Nominal_Capacity: str
    Low_Speed_Nominal_Capacity_Sizing_Factor: str
    Design_Entering_Water_Temperature: str
    Design_Entering_Air_Temperature: str
    Design_Entering_Air_Wetbulb_Temperature: str
    Design_Water_Flow_Rate: str
    High_Fan_Speed_Air_Flow_Rate: str
    High_Fan_Speed_Fan_Power: str
    Low_Fan_Speed_Air_Flow_Rate: str
    Low_Fan_Speed_Air_Flow_Rate_Sizing_Factor: str
    Low_Fan_Speed_Fan_Power: str
    Low_Fan_Speed_Fan_Power_Sizing_Factor: str
    Outdoor_Air_Inlet_Node_Name: str

class FluidpropertiesConcentrationType(TypedDict, total=False):
    """"dict for FluidpropertiesConcentration"""
    Fluid_Name: str
    Fluid_Property_Type: str
    Temperature_Values_Name: str
    Concentration: str
    Property_Value_1: str
    Property_Value_2: str
    Property_Value_3: str
    Property_Value_4: str
    Property_Value_5: str
    Property_Value_6: str
    Property_Value_7: str
    Property_Value_8: str
    Property_Value_9: str
    Property_Value_10: str
    Property_Value_11: str
    Property_Value_12: str
    Property_Value_13: str
    Property_Value_14: str
    Property_Value_15: str
    Property_Value_16: str
    Property_Value_17: str
    Property_Value_18: str
    Property_Value_19: str
    Property_Value_20: str
    Property_Value_21: str
    Property_Value_22: str
    Property_Value_23: str
    Property_Value_24: str
    Property_Value_25: str
    Property_Value_26: str
    Property_Value_27: str
    Property_Value_28: str
    Property_Value_29: str
    Property_Value_30: str
    Property_Value_31: str
    Property_Value_32: str
    Property_Value_33: str
    Property_Value_34: str
    Property_Value_35: str
    Property_Value_36: str
    Property_Value_37: str
    Property_Value_38: str
    Property_Value_39: str
    Property_Value_40: str
    Property_Value_41: str
    Property_Value_42: str
    Property_Value_43: str
    Property_Value_44: str
    Property_Value_45: str
    Property_Value_46: str
    Property_Value_47: str
    Property_Value_48: str
    Property_Value_49: str

class FluidpropertiesGlycolconcentrationType(TypedDict, total=False):
    """"dict for FluidpropertiesGlycolconcentration"""
    Name: str
    Glycol_Type: str
    User_Defined_Glycol_Name: str
    Glycol_Concentration: str

class FluidpropertiesNameType(TypedDict, total=False):
    """"dict for FluidpropertiesName"""
    Fluid_Name: str
    Fluid_Type: str

class FluidpropertiesSaturatedType(TypedDict, total=False):
    """"dict for FluidpropertiesSaturated"""
    Fluid_Name: str
    Fluid_Property_Type: str
    Fluid_Phase: str
    Temperature_Values_Name: str
    Property_Value_1: str
    Property_Value_2: str
    Property_Value_3: str
    Property_Value_4: str
    Property_Value_5: str
    Property_Value_6: str
    Property_Value_7: str
    Property_Value_8: str
    Property_Value_9: str
    Property_Value_10: str
    Property_Value_11: str
    Property_Value_12: str
    Property_Value_13: str
    Property_Value_14: str
    Property_Value_15: str
    Property_Value_16: str
    Property_Value_17: str
    Property_Value_18: str
    Property_Value_19: str
    Property_Value_20: str
    Property_Value_21: str
    Property_Value_22: str
    Property_Value_23: str
    Property_Value_24: str
    Property_Value_25: str
    Property_Value_26: str
    Property_Value_27: str
    Property_Value_28: str
    Property_Value_29: str
    Property_Value_30: str
    Property_Value_31: str
    Property_Value_32: str
    Property_Value_33: str
    Property_Value_34: str
    Property_Value_35: str
    Property_Value_36: str
    Property_Value_37: str
    Property_Value_38: str
    Property_Value_39: str
    Property_Value_40: str
    Property_Value_41: str
    Property_Value_42: str
    Property_Value_43: str
    Property_Value_44: str
    Property_Value_45: str
    Property_Value_46: str
    Property_Value_47: str
    Property_Value_48: str
    Property_Value_49: str

class FluidpropertiesSuperheatedType(TypedDict, total=False):
    """"dict for FluidpropertiesSuperheated"""
    Fluid_Name: str
    Fluid_Property_Type: str
    Temperature_Values_Name: str
    Pressure: str
    Property_Value_1: str
    Property_Value_2: str
    Property_Value_3: str
    Property_Value_4: str
    Property_Value_5: str
    Property_Value_6: str
    Property_Value_7: str
    Property_Value_8: str
    Property_Value_9: str
    Property_Value_10: str
    Property_Value_11: str
    Property_Value_12: str
    Property_Value_13: str
    Property_Value_14: str
    Property_Value_15: str
    Property_Value_16: str
    Property_Value_17: str
    Property_Value_18: str
    Property_Value_19: str
    Property_Value_20: str
    Property_Value_21: str
    Property_Value_22: str
    Property_Value_23: str
    Property_Value_24: str
    Property_Value_25: str
    Property_Value_26: str
    Property_Value_27: str
    Property_Value_28: str
    Property_Value_29: str
    Property_Value_30: str
    Property_Value_31: str
    Property_Value_32: str
    Property_Value_33: str
    Property_Value_34: str
    Property_Value_35: str
    Property_Value_36: str
    Property_Value_37: str
    Property_Value_38: str
    Property_Value_39: str
    Property_Value_40: str
    Property_Value_41: str
    Property_Value_42: str
    Property_Value_43: str
    Property_Value_44: str
    Property_Value_45: str
    Property_Value_46: str
    Property_Value_47: str
    Property_Value_48: str
    Property_Value_49: str

class FluidpropertiesTemperaturesType(TypedDict, total=False):
    """"dict for FluidpropertiesTemperatures"""
    Name: str
    Temperature_1: str
    Temperature_2: str
    Temperature_3: str
    Temperature_4: str
    Temperature_5: str
    Temperature_6: str
    Temperature_7: str
    Temperature_8: str
    Temperature_9: str
    Temperature_10: str
    Temperature_11: str
    Temperature_12: str
    Temperature_13: str
    Temperature_14: str
    Temperature_15: str
    Temperature_16: str
    Temperature_17: str
    Temperature_18: str
    Temperature_19: str
    Temperature_20: str
    Temperature_21: str
    Temperature_22: str
    Temperature_23: str
    Temperature_24: str
    Temperature_25: str
    Temperature_26: str
    Temperature_27: str
    Temperature_28: str
    Temperature_29: str
    Temperature_30: str
    Temperature_31: str
    Temperature_32: str
    Temperature_33: str
    Temperature_34: str
    Temperature_35: str
    Temperature_36: str
    Temperature_37: str
    Temperature_38: str
    Temperature_39: str
    Temperature_40: str
    Temperature_41: str
    Temperature_42: str
    Temperature_43: str
    Temperature_44: str
    Temperature_45: str
    Temperature_46: str
    Temperature_47: str
    Temperature_48: str
    Temperature_49: str

class FoundationKivaType(TypedDict, total=False):
    """"dict for FoundationKiva"""
    Name: str
    Initial_Indoor_Air_Temperature: str
    Interior_Horizontal_Insulation_Material_Name: str
    Interior_Horizontal_Insulation_Depth: str
    Interior_Horizontal_Insulation_Width: str
    Interior_Vertical_Insulation_Material_Name: str
    Interior_Vertical_Insulation_Depth: str
    Exterior_Horizontal_Insulation_Material_Name: str
    Exterior_Horizontal_Insulation_Depth: str
    Exterior_Horizontal_Insulation_Width: str
    Exterior_Vertical_Insulation_Material_Name: str
    Exterior_Vertical_Insulation_Depth: str
    Wall_Height_Above_Grade: str
    Wall_Depth_Below_Slab: str
    Footing_Wall_Construction_Name: str
    Footing_Material_Name: str
    Footing_Depth: str
    Custom_Block_1_Material_Name: str
    Custom_Block_1_Depth: str
    Custom_Block_1_X_Position: str
    Custom_Block_1_Z_Position: str
    Custom_Block_2_Material_Name: str
    Custom_Block_2_Depth: str
    Custom_Block_2_X_Position: str
    Custom_Block_2_Z_Position: str
    Custom_Block_3_Material_Name: str
    Custom_Block_3_Depth: str
    Custom_Block_3_X_Position: str
    Custom_Block_3_Z_Position: str
    Custom_Block_4_Material_Name: str
    Custom_Block_4_Depth: str
    Custom_Block_4_X_Position: str
    Custom_Block_4_Z_Position: str
    Custom_Block_5_Material_Name: str
    Custom_Block_5_Depth: str
    Custom_Block_5_X_Position: str
    Custom_Block_5_Z_Position: str
    Custom_Block_6_Material_Name: str
    Custom_Block_6_Depth: str
    Custom_Block_6_X_Position: str
    Custom_Block_6_Z_Position: str
    Custom_Block_7_Material_Name: str
    Custom_Block_7_Depth: str
    Custom_Block_7_X_Position: str
    Custom_Block_7_Z_Position: str
    Custom_Block_8_Material_Name: str
    Custom_Block_8_Depth: str
    Custom_Block_8_X_Position: str
    Custom_Block_8_Z_Position: str
    Custom_Block_9_Material_Name: str
    Custom_Block_9_Depth: str
    Custom_Block_9_X_Position: str
    Custom_Block_9_Z_Position: str
    Custom_Block_10_Material_Name: str
    Custom_Block_10_Depth: str
    Custom_Block_10_X_Position: str
    Custom_Block_10_Z_Position: str

class FoundationKivaSettingsType(TypedDict, total=False):
    """"dict for FoundationKivaSettings"""
    Soil_Conductivity: str
    Soil_Density: str
    Soil_Specific_Heat: str
    Ground_Solar_Absorptivity: str
    Ground_Thermal_Absorptivity: str
    Ground_Surface_Roughness: str
    FarField_Width: str
    DeepGround_Boundary_Condition: str
    DeepGround_Depth: str
    Minimum_Cell_Dimension: str
    Maximum_Cell_Growth_Coefficient: str
    Simulation_Timestep: str

class FuelfactorsType(TypedDict, total=False):
    """"dict for Fuelfactors"""
    Existing_Fuel_Resource_Name: str
    Source_Energy_Factor: str
    Source_Energy_Schedule_Name: str
    CO2_Emission_Factor: str
    CO2_Emission_Factor_Schedule_Name: str
    CO_Emission_Factor: str
    CO_Emission_Factor_Schedule_Name: str
    CH4_Emission_Factor: str
    CH4_Emission_Factor_Schedule_Name: str
    NOx_Emission_Factor: str
    NOx_Emission_Factor_Schedule_Name: str
    N2O_Emission_Factor: str
    N2O_Emission_Factor_Schedule_Name: str
    SO2_Emission_Factor: str
    SO2_Emission_Factor_Schedule_Name: str
    PM_Emission_Factor: str
    PM_Emission_Factor_Schedule_Name: str
    PM10_Emission_Factor: str
    PM10_Emission_Factor_Schedule_Name: str
    PM25_Emission_Factor: str
    PM25_Emission_Factor_Schedule_Name: str
    NH3_Emission_Factor: str
    NH3_Emission_Factor_Schedule_Name: str
    NMVOC_Emission_Factor: str
    NMVOC_Emission_Factor_Schedule_Name: str
    Hg_Emission_Factor: str
    Hg_Emission_Factor_Schedule_Name: str
    Pb_Emission_Factor: str
    Pb_Emission_Factor_Schedule_Name: str
    Water_Emission_Factor: str
    Water_Emission_Factor_Schedule_Name: str
    Nuclear_High_Level_Emission_Factor: str
    Nuclear_High_Level_Emission_Factor_Schedule_Name: str
    Nuclear_Low_Level_Emission_Factor: str
    Nuclear_Low_Level_Emission_Factor_Schedule_Name: str

class GasequipmentType(TypedDict, total=False):
    """"dict for Gasequipment"""
    Name: str
    Zone_or_ZoneList_or_Space_or_SpaceList_Name: str
    Schedule_Name: str
    Design_Level_Calculation_Method: str
    Design_Level: str
    Power_per_Floor_Area: str
    Power_per_Person: str
    Fraction_Latent: str
    Fraction_Radiant: str
    Fraction_Lost: str
    Carbon_Dioxide_Generation_Rate: str
    EndUse_Subcategory: str

class GeneratorCombustionturbineType(TypedDict, total=False):
    """"dict for GeneratorCombustionturbine"""
    Name: str
    Rated_Power_Output: str
    Electric_Circuit_Node_Name: str
    Minimum_Part_Load_Ratio: str
    Maximum_Part_Load_Ratio: str
    Optimum_Part_Load_Ratio: str
    Part_Load_Based_Fuel_Input_Curve_Name: str
    Temperature_Based_Fuel_Input_Curve_Name: str
    Exhaust_Flow_Curve_Name: str
    Part_Load_Based_Exhaust_Temperature_Curve_Name: str
    Temperature_Based_Exhaust_Temperature_Curve_Name: str
    Heat_Recovery_Lube_Energy_Curve_Name: str
    Coefficient_1_of_UFactor_Times_Area_Curve: str
    Coefficient_2_of_UFactor_Times_Area_Curve: str
    Maximum_Exhaust_Flow_per_Unit_of_Power_Output: str
    Design_Minimum_Exhaust_Temperature: str
    Design_Air_Inlet_Temperature: str
    Fuel_Higher_Heating_Value: str
    Design_Heat_Recovery_Water_Flow_Rate: str
    Heat_Recovery_Inlet_Node_Name: str
    Heat_Recovery_Outlet_Node_Name: str
    Fuel_Type: str
    Heat_Recovery_Maximum_Temperature: str
    Outdoor_Air_Inlet_Node_Name: str

class GeneratorFuelcellType(TypedDict, total=False):
    """"dict for GeneratorFuelcell"""
    Name: str
    Power_Module_Name: str
    Air_Supply_Name: str
    Fuel_Supply_Name: str
    Water_Supply_Name: str
    Auxiliary_Heater_Name: str
    Heat_Exchanger_Name: str
    Electrical_Storage_Name: str
    Inverter_Name: str
    Stack_Cooler_Name: str

class GeneratorFuelcellAirsupplyType(TypedDict, total=False):
    """"dict for GeneratorFuelcellAirsupply"""
    Name: str
    Air_Inlet_Node_Name: str
    Blower_Power_Curve_Name: str
    Blower_Heat_Loss_Factor: str
    Air_Supply_Rate_Calculation_Mode: str
    Stoichiometric_Ratio: str
    Air_Rate_Function_of_Electric_Power_Curve_Name: str
    Air_Rate_Air_Temperature_Coefficient: str
    Air_Rate_Function_of_Fuel_Rate_Curve_Name: str
    Air_Intake_Heat_Recovery_Mode: str
    Air_Supply_Constituent_Mode: str
    Number_of_UserDefined_Constituents: str
    Constituent_1_Name: str
    Molar_Fraction_1: str
    Constituent_2_Name: str
    Molar_Fraction_2: str
    Constituent_3_Name: str
    Molar_Fraction_3: str
    Constituent_4_Name: str
    Molar_Fraction_4: str
    Constituent_5_Name: str
    Molar_Fraction_5: str

class GeneratorFuelcellAuxiliaryheaterType(TypedDict, total=False):
    """"dict for GeneratorFuelcellAuxiliaryheater"""
    Name: str
    Excess_Air_Ratio: str
    Ancillary_Power_Constant_Term: str
    Ancillary_Power_Linear_Term: str
    Skin_Loss_UFactor_Times_Area_Value: str
    Skin_Loss_Destination: str
    Zone_Name_to_Receive_Skin_Losses: str
    Heating_Capacity_Units: str
    Maximum_Heating_Capacity_in_Watts: str
    Minimum_Heating_Capacity_in_Watts: str
    Maximum_Heating_Capacity_in_Kmol_per_Second: str
    Minimum_Heating_Capacity_in_Kmol_per_Second: str

class GeneratorFuelcellElectricalstorageType(TypedDict, total=False):
    """"dict for GeneratorFuelcellElectricalstorage"""
    Name: str
    Choice_of_Model: str
    Nominal_Charging_Energetic_Efficiency: str
    Nominal_Discharging_Energetic_Efficiency: str
    Simple_Maximum_Capacity: str
    Simple_Maximum_Power_Draw: str
    Simple_Maximum_Power_Store: str
    Initial_Charge_State: str

class GeneratorFuelcellExhaustgastowaterheatexchangerType(TypedDict, total=False):
    """"dict for GeneratorFuelcellExhaustgastowaterheatexchanger"""
    Name: str
    Heat_Recovery_Water_Inlet_Node_Name: str
    Heat_Recovery_Water_Outlet_Node_Name: str
    Heat_Recovery_Water_Maximum_Flow_Rate: str
    Exhaust_Outlet_Air_Node_Name: str
    Heat_Exchanger_Calculation_Method: str
    Method_1_Heat_Exchanger_Effectiveness: str
    Method_2_Parameter_hxs0: str
    Method_2_Parameter_hxs1: str
    Method_2_Parameter_hxs2: str
    Method_2_Parameter_hxs3: str
    Method_2_Parameter_hxs4: str
    Method_3_h0Gas_Coefficient: str
    Method_3_NdotGasRef_Coefficient: str
    Method_3_n_Coefficient: str
    Method_3_Gas_Area: str
    Method_3_h0_Water_Coefficient: str
    Method_3_N_dot_Water_ref_Coefficient: str
    Method_3_m_Coefficient: str
    Method_3_Water_Area: str
    Method_3_F_Adjustment_Factor: str
    Method_4_hxl1_Coefficient: str
    Method_4_hxl2_Coefficient: str
    Method_4_Condensation_Threshold: str

class GeneratorFuelcellInverterType(TypedDict, total=False):
    """"dict for GeneratorFuelcellInverter"""
    Name: str
    Inverter_Efficiency_Calculation_Mode: str
    Inverter_Efficiency: str
    Efficiency_Function_of_DC_Power_Curve_Name: str

class GeneratorFuelcellPowermoduleType(TypedDict, total=False):
    """"dict for GeneratorFuelcellPowermodule"""
    Name: str
    Efficiency_Curve_Mode: str
    Efficiency_Curve_Name: str
    Nominal_Efficiency: str
    Nominal_Electrical_Power: str
    Number_of_Stops_at_Start_of_Simulation: str
    Cycling_Performance_Degradation_Coefficient: str
    Number_of_Run_Hours_at_Beginning_of_Simulation: str
    Accumulated_Run_Time_Degradation_Coefficient: str
    Run_Time_Degradation_Initiation_Time_Threshold: str
    Power_Up_Transient_Limit: str
    Power_Down_Transient_Limit: str
    Start_Up_Time: str
    Start_Up_Fuel: str
    Start_Up_Electricity_Consumption: str
    Start_Up_Electricity_Produced: str
    Shut_Down_Time: str
    Shut_Down_Fuel: str
    Shut_Down_Electricity_Consumption: str
    Ancillary_Electricity_Constant_Term: str
    Ancillary_Electricity_Linear_Term: str
    Skin_Loss_Calculation_Mode: str
    Zone_Name: str
    Skin_Loss_Radiative_Fraction: str
    Constant_Skin_Loss_Rate: str
    Skin_Loss_UFactor_Times_Area_Term: str
    Skin_Loss_Quadratic_Curve_Name: str
    Dilution_Air_Flow_Rate: str
    Stack_Heat_loss_to_Dilution_Air: str
    Dilution_Inlet_Air_Node_Name: str
    Dilution_Outlet_Air_Node_Name: str
    Minimum_Operating_Point: str
    Maximum_Operating_Point: str

class GeneratorFuelcellStackcoolerType(TypedDict, total=False):
    """"dict for GeneratorFuelcellStackcooler"""
    Name: str
    Heat_Recovery_Water_Inlet_Node_Name: str
    Heat_Recovery_Water_Outlet_Node_Name: str
    Nominal_Stack_Temperature: str
    Actual_Stack_Temperature: str
    Coefficient_r0: str
    Coefficient_r1: str
    Coefficient_r2: str
    Coefficient_r3: str
    Stack_Coolant_Flow_Rate: str
    Stack_Cooler_UFactor_Times_Area_Value: str
    Fscogen_Adjustment_Factor: str
    Stack_Cogeneration_Exchanger_Area: str
    Stack_Cogeneration_Exchanger_Nominal_Flow_Rate: str
    Stack_Cogeneration_Exchanger_Nominal_Heat_Transfer_Coefficient: str
    Stack_Cogeneration_Exchanger_Nominal_Heat_Transfer_Coefficient_Exponent: str
    Stack_Cooler_Pump_Power: str
    Stack_Cooler_Pump_Heat_Loss_Fraction: str
    Stack_Air_Cooler_Fan_Coefficient_f0: str
    Stack_Air_Cooler_Fan_Coefficient_f1: str
    Stack_Air_Cooler_Fan_Coefficient_f2: str

class GeneratorFuelcellWatersupplyType(TypedDict, total=False):
    """"dict for GeneratorFuelcellWatersupply"""
    Name: str
    Reformer_Water_Flow_Rate_Function_of_Fuel_Rate_Curve_Name: str
    Reformer_Water_Pump_Power_Function_of_Fuel_Rate_Curve_Name: str
    Pump_Heat_Loss_Factor: str
    Water_Temperature_Modeling_Mode: str
    Water_Temperature_Reference_Node_Name: str
    Water_Temperature_Schedule_Name: str

class GeneratorFuelsupplyType(TypedDict, total=False):
    """"dict for GeneratorFuelsupply"""
    Name: str
    Fuel_Temperature_Modeling_Mode: str
    Fuel_Temperature_Reference_Node_Name: str
    Fuel_Temperature_Schedule_Name: str
    Compressor_Power_Multiplier_Function_of_Fuel_Rate_Curve_Name: str
    Compressor_Heat_Loss_Factor: str
    Fuel_Type: str
    Liquid_Generic_Fuel_Lower_Heating_Value: str
    Liquid_Generic_Fuel_Higher_Heating_Value: str
    Liquid_Generic_Fuel_Molecular_Weight: str
    Liquid_Generic_Fuel_CO2_Emission_Factor: str
    Number_of_Constituents_in_Gaseous_Constituent_Fuel_Supply: str
    Constituent_1_Name: str
    Constituent_1_Molar_Fraction: str
    Constituent_2_Name: str
    Constituent_2_Molar_Fraction: str
    Constituent_3_Name: str
    Constituent_3_Molar_Fraction: str
    Constituent_4_Name: str
    Constituent_4_Molar_Fraction: str
    Constituent_5_Name: str
    Constituent_5_Molar_Fraction: str
    Constituent_6_Name: str
    Constituent_6_Molar_Fraction: str
    Constituent_7_Name: str
    Constituent_7_Molar_Fraction: str
    Constituent_8_Name: str
    Constituent_8_Molar_Fraction: str
    Constituent_9_Name: str
    Constituent_9_Molar_Fraction: str
    Constituent_10_Name: str
    Constituent_10_Molar_Fraction: str
    Constituent_11_Name: str
    Constituent_11_Molar_Fraction: str
    Constituent_12_Name: str
    Constituent_12_Molar_Fraction: str

class GeneratorInternalcombustionengineType(TypedDict, total=False):
    """"dict for GeneratorInternalcombustionengine"""
    Name: str
    Rated_Power_Output: str
    Electric_Circuit_Node_Name: str
    Minimum_Part_Load_Ratio: str
    Maximum_Part_Load_Ratio: str
    Optimum_Part_Load_Ratio: str
    Shaft_Power_Curve_Name: str
    Jacket_Heat_Recovery_Curve_Name: str
    Lube_Heat_Recovery_Curve_Name: str
    Total_Exhaust_Energy_Curve_Name: str
    Exhaust_Temperature_Curve_Name: str
    Coefficient_1_of_UFactor_Times_Area_Curve: str
    Coefficient_2_of_UFactor_Times_Area_Curve: str
    Maximum_Exhaust_Flow_per_Unit_of_Power_Output: str
    Design_Minimum_Exhaust_Temperature: str
    Fuel_Higher_Heating_Value: str
    Design_Heat_Recovery_Water_Flow_Rate: str
    Heat_Recovery_Inlet_Node_Name: str
    Heat_Recovery_Outlet_Node_Name: str
    Fuel_Type: str
    Heat_Recovery_Maximum_Temperature: str

class GeneratorMicrochpType(TypedDict, total=False):
    """"dict for GeneratorMicrochp"""
    Name: str
    Performance_Parameters_Name: str
    Zone_Name: str
    Cooling_Water_Inlet_Node_Name: str
    Cooling_Water_Outlet_Node_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Generator_Fuel_Supply_Name: str
    Availability_Schedule_Name: str

class GeneratorMicrochpNonnormalizedparametersType(TypedDict, total=False):
    """"dict for GeneratorMicrochpNonnormalizedparameters"""
    Name: str
    Maximum_Electric_Power: str
    Minimum_Electric_Power: str
    Minimum_Cooling_Water_Flow_Rate: str
    Maximum_Cooling_Water_Temperature: str
    Electrical_Efficiency_Curve_Name: str
    Thermal_Efficiency_Curve_Name: str
    Cooling_Water_Flow_Rate_Mode: str
    Cooling_Water_Flow_Rate_Curve_Name: str
    Air_Flow_Rate_Curve_Name: str
    Maximum_Net_Electrical_Power_Rate_of_Change: str
    Maximum_Fuel_Flow_Rate_of_Change: str
    Heat_Exchanger_UFactor_Times_Area_Value: str
    Skin_Loss_UFactor_Times_Area_Value: str
    Skin_Loss_Radiative_Fraction: str
    Aggregated_Thermal_Mass_of_Energy_Conversion_Portion_of_Generator: str
    Aggregated_Thermal_Mass_of_Heat_Recovery_Portion_of_Generator: str
    Standby_Power: str
    Warm_Up_Mode: str
    Warm_Up_Fuel_Flow_Rate_Coefficient: str
    Nominal_Engine_Operating_Temperature: str
    Warm_Up_Power_Coefficient: str
    Warm_Up_Fuel_Flow_Rate_Limit_Ratio: str
    Warm_Up_Delay_Time: str
    Cool_Down_Power: str
    Cool_Down_Delay_Time: str
    Restart_Mode: str

class GeneratorMicroturbineType(TypedDict, total=False):
    """"dict for GeneratorMicroturbine"""
    Name: str
    Reference_Electrical_Power_Output: str
    Minimum_Full_Load_Electrical_Power_Output: str
    Maximum_Full_Load_Electrical_Power_Output: str
    Reference_Electrical_Efficiency_Using_Lower_Heating_Value: str
    Reference_Combustion_Air_Inlet_Temperature: str
    Reference_Combustion_Air_Inlet_Humidity_Ratio: str
    Reference_Elevation: str
    Electrical_Power_Function_of_Temperature_and_Elevation_Curve_Name: str
    Electrical_Efficiency_Function_of_Temperature_Curve_Name: str
    Electrical_Efficiency_Function_of_Part_Load_Ratio_Curve_Name: str
    Fuel_Type: str
    Fuel_Higher_Heating_Value: str
    Fuel_Lower_Heating_Value: str
    Standby_Power: str
    Ancillary_Power: str
    Ancillary_Power_Function_of_Fuel_Input_Curve_Name: str
    Heat_Recovery_Water_Inlet_Node_Name: str
    Heat_Recovery_Water_Outlet_Node_Name: str
    Reference_Thermal_Efficiency_Using_Lower_Heat_Value: str
    Reference_Inlet_Water_Temperature: str
    Heat_Recovery_Water_Flow_Operating_Mode: str
    Reference_Heat_Recovery_Water_Flow_Rate: str
    Heat_Recovery_Water_Flow_Rate_Function_of_Temperature_and_Power_Curve_Name: str
    Thermal_Efficiency_Function_of_Temperature_and_Elevation_Curve_Name: str
    Heat_Recovery_Rate_Function_of_Part_Load_Ratio_Curve_Name: str
    Heat_Recovery_Rate_Function_of_Inlet_Water_Temperature_Curve_Name: str
    Heat_Recovery_Rate_Function_of_Water_Flow_Rate_Curve_Name: str
    Minimum_Heat_Recovery_Water_Flow_Rate: str
    Maximum_Heat_Recovery_Water_Flow_Rate: str
    Maximum_Heat_Recovery_Water_Temperature: str
    Combustion_Air_Inlet_Node_Name: str
    Combustion_Air_Outlet_Node_Name: str
    Reference_Exhaust_Air_Mass_Flow_Rate: str
    Exhaust_Air_Flow_Rate_Function_of_Temperature_Curve_Name: str
    Exhaust_Air_Flow_Rate_Function_of_Part_Load_Ratio_Curve_Name: str
    Nominal_Exhaust_Air_Outlet_Temperature: str
    Exhaust_Air_Temperature_Function_of_Temperature_Curve_Name: str
    Exhaust_Air_Temperature_Function_of_Part_Load_Ratio_Curve_Name: str

class GeneratorPhotovoltaicType(TypedDict, total=False):
    """"dict for GeneratorPhotovoltaic"""
    Name: str
    Surface_Name: str
    Photovoltaic_Performance_Object_Type: str
    Module_Performance_Name: str
    Heat_Transfer_Integration_Mode: str
    Number_of_Series_Strings_in_Parallel: str
    Number_of_Modules_in_Series: str

class GeneratorPvwattsType(TypedDict, total=False):
    """"dict for GeneratorPvwatts"""
    Name: str
    PVWatts_Version: str
    DC_System_Capacity: str
    Module_Type: str
    Array_Type: str
    System_Losses: str
    Array_Geometry_Type: str
    Tilt_Angle: str
    Azimuth_Angle: str
    Surface_Name: str
    Ground_Coverage_Ratio: str

class GeneratorWindturbineType(TypedDict, total=False):
    """"dict for GeneratorWindturbine"""
    Name: str
    Availability_Schedule_Name: str
    Rotor_Type: str
    Power_Control: str
    Rated_Rotor_Speed: str
    Rotor_Diameter: str
    Overall_Height: str
    Number_of_Blades: str
    Rated_Power: str
    Rated_Wind_Speed: str
    Cut_In_Wind_Speed: str
    Cut_Out_Wind_Speed: str
    Fraction_system_Efficiency: str
    Maximum_Tip_Speed_Ratio: str
    Maximum_Power_Coefficient: str
    Annual_Local_Average_Wind_Speed: str
    Height_for_Local_Average_Wind_Speed: str
    Blade_Chord_Area: str
    Blade_Drag_Coefficient: str
    Blade_Lift_Coefficient: str
    Power_Coefficient_C1: str
    Power_Coefficient_C2: str
    Power_Coefficient_C3: str
    Power_Coefficient_C4: str
    Power_Coefficient_C5: str
    Power_Coefficient_C6: str

class GeometrytransformType(TypedDict, total=False):
    """"dict for Geometrytransform"""
    Plane_of_Transform: str
    Current_Aspect_Ratio: str
    New_Aspect_Ratio: str

class GlazeddoorType(TypedDict, total=False):
    """"dict for Glazeddoor"""
    Name: str
    Construction_Name: str
    Building_Surface_Name: str
    Frame_and_Divider_Name: str
    Multiplier: str
    Starting_X_Coordinate: str
    Starting_Z_Coordinate: str
    Length: str
    Height: str

class GlazeddoorInterzoneType(TypedDict, total=False):
    """"dict for GlazeddoorInterzone"""
    Name: str
    Construction_Name: str
    Building_Surface_Name: str
    Outside_Boundary_Condition_Object: str
    Multiplier: str
    Starting_X_Coordinate: str
    Starting_Z_Coordinate: str
    Length: str
    Height: str

class GlobalgeometryrulesType(TypedDict, total=False):
    """"dict for Globalgeometryrules"""
    Starting_Vertex_Position: str
    Vertex_Entry_Direction: str
    Coordinate_System: str
    Daylighting_Reference_Point_Coordinate_System: str
    Rectangular_Surface_Coordinate_System: str

class GroundheatexchangerHorizontaltrenchType(TypedDict, total=False):
    """"dict for GroundheatexchangerHorizontaltrench"""
    Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str
    Design_Flow_Rate: str
    Trench_Length_in_Pipe_Axial_Direction: str
    Number_of_Trenches: str
    Horizontal_Spacing_Between_Pipes: str
    Pipe_Inner_Diameter: str
    Pipe_Outer_Diameter: str
    Burial_Depth: str
    Soil_Thermal_Conductivity: str
    Soil_Density: str
    Soil_Specific_Heat: str
    Pipe_Thermal_Conductivity: str
    Pipe_Density: str
    Pipe_Specific_Heat: str
    Soil_Moisture_Content_Percent: str
    Soil_Moisture_Content_Percent_at_Saturation: str
    Undisturbed_Ground_Temperature_Model_Type: str
    Undisturbed_Ground_Temperature_Model_Name: str
    Evapotranspiration_Ground_Cover_Parameter: str

class GroundheatexchangerPondType(TypedDict, total=False):
    """"dict for GroundheatexchangerPond"""
    Name: str
    Fluid_Inlet_Node_Name: str
    Fluid_Outlet_Node_Name: str
    Pond_Depth: str
    Pond_Area: str
    Hydronic_Tubing_Inside_Diameter: str
    Hydronic_Tubing_Outside_Diameter: str
    Hydronic_Tubing_Thermal_Conductivity: str
    Ground_Thermal_Conductivity: str
    Number_of_Tubing_Circuits: str
    Length_of_Each_Tubing_Circuit: str

class GroundheatexchangerResponsefactorsType(TypedDict, total=False):
    """"dict for GroundheatexchangerResponsefactors"""
    Name: str
    GHEVerticalProperties_Object_Name: str
    Number_of_Boreholes: str
    GFunction_Reference_Ratio: str
    gFunction_LnTTs_Value_1: str
    gFunction_g_Value_1: str
    gFunction_LnTTs_Value_2: str
    gFunction_g_Value_2: str
    gFunction_LnTTs_Value_3: str
    gFunction_g_Value_3: str
    gFunction_LnTTs_Value_4: str
    gFunction_g_Value_4: str
    gFunction_LnTTs_Value_5: str
    gFunction_g_Value_5: str
    gFunction_LnTTs_Value_6: str
    gFunction_g_Value_6: str
    gFunction_LnTTs_Value_7: str
    gFunction_g_Value_7: str
    gFunction_LnTTs_Value_8: str
    gFunction_g_Value_8: str
    gFunction_LnTTs_Value_9: str
    gFunction_g_Value_9: str
    gFunction_LnTTs_Value_10: str
    gFunction_g_Value_10: str
    gFunction_LnTTs_Value_11: str
    gFunction_g_Value_11: str
    gFunction_LnTTs_Value_12: str
    gFunction_g_Value_12: str
    gFunction_LnTTs_Value_13: str
    gFunction_g_Value_13: str
    gFunction_LnTTs_Value_14: str
    gFunction_g_Value_14: str
    gFunction_LnTTs_Value_15: str
    gFunction_g_Value_15: str
    gFunction_LnTTs_Value_16: str
    gFunction_g_Value_16: str
    gFunction_LnTTs_Value_17: str
    gFunction_g_Value_17: str
    gFunction_LnTTs_Value_18: str
    gFunction_g_Value_18: str
    gFunction_LnTTs_Value_19: str
    gFunction_g_Value_19: str
    gFunction_LnTTs_Value_20: str
    gFunction_g_Value_20: str
    gFunction_LnTTs_Value_21: str
    gFunction_g_Value_21: str
    gFunction_LnTTs_Value_22: str
    gFunction_g_Value_22: str
    gFunction_LnTTs_Value_23: str
    gFunction_g_Value_23: str
    gFunction_LnTTs_Value_24: str
    gFunction_g_Value_24: str
    gFunction_LnTTs_Value_25: str
    gFunction_g_Value_25: str
    gFunction_LnTTs_Value_26: str
    gFunction_g_Value_26: str
    gFunction_LnTTs_Value_27: str
    gFunction_g_Value_27: str
    gFunction_LnTTs_Value_28: str
    gFunction_g_Value_28: str
    gFunction_LnTTs_Value_29: str
    gFunction_g_Value_29: str
    gFunction_LnTTs_Value_30: str
    gFunction_g_Value_30: str
    gFunction_LnTTs_Value_31: str
    gFunction_g_Value_31: str
    gFunction_LnTTs_Value_32: str
    gFunction_g_Value_32: str
    gFunction_LnTTs_Value_33: str
    gFunction_g_Value_33: str
    gFunction_LnTTs_Value_34: str
    gFunction_g_Value_34: str
    gFunction_LnTTs_Value_35: str
    gFunction_g_Value_35: str
    gFunction_LnTTs_Value_36: str
    gFunction_g_Value_36: str
    gFunction_LnTTs_Value_37: str
    gFunction_g_Value_37: str
    gFunction_LnTTs_Value_38: str
    gFunction_g_Value_38: str
    gFunction_LnTTs_Value_39: str
    gFunction_g_Value_39: str
    gFunction_LnTTs_Value_40: str
    gFunction_g_Value_40: str
    gFunction_LnTTs_Value_41: str
    gFunction_g_Value_41: str
    gFunction_LnTTs_Value_42: str
    gFunction_g_Value_42: str
    gFunction_LnTTs_Value_43: str
    gFunction_g_Value_43: str
    gFunction_LnTTs_Value_44: str
    gFunction_g_Value_44: str
    gFunction_LnTTs_Value_45: str
    gFunction_g_Value_45: str
    gFunction_LnTTs_Value_46: str
    gFunction_g_Value_46: str
    gFunction_LnTTs_Value_47: str
    gFunction_g_Value_47: str
    gFunction_LnTTs_Value_48: str
    gFunction_g_Value_48: str
    gFunction_LnTTs_Value_49: str
    gFunction_g_Value_49: str

class GroundheatexchangerSlinkyType(TypedDict, total=False):
    """"dict for GroundheatexchangerSlinky"""
    Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str
    Design_Flow_Rate: str
    Soil_Thermal_Conductivity: str
    Soil_Density: str
    Soil_Specific_Heat: str
    Pipe_Thermal_Conductivity: str
    Pipe_Density: str
    Pipe_Specific_Heat: str
    Pipe_Outer_Diameter: str
    Pipe_Thickness: str
    Heat_Exchanger_Configuration: str
    Coil_Diameter: str
    Coil_Pitch: str
    Trench_Depth: str
    Trench_Length: str
    Number_of_Trenches: str
    Horizontal_Spacing_Between_Pipes: str
    Undisturbed_Ground_Temperature_Model_Type: str
    Undisturbed_Ground_Temperature_Model_Name: str
    Maximum_Length_of_Simulation: str

class GroundheatexchangerSurfaceType(TypedDict, total=False):
    """"dict for GroundheatexchangerSurface"""
    Name: str
    Construction_Name: str
    Fluid_Inlet_Node_Name: str
    Fluid_Outlet_Node_Name: str
    Hydronic_Tubing_Inside_Diameter: str
    Number_of_Tubing_Circuits: str
    Hydronic_Tube_Spacing: str
    Surface_Length: str
    Surface_Width: str
    Lower_Surface_Environment: str

class GroundheatexchangerSystemType(TypedDict, total=False):
    """"dict for GroundheatexchangerSystem"""
    Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str
    Design_Flow_Rate: str
    Undisturbed_Ground_Temperature_Model_Type: str
    Undisturbed_Ground_Temperature_Model_Name: str
    Ground_Thermal_Conductivity: str
    Ground_Thermal_Heat_Capacity: str
    GHEVerticalResponseFactors_Object_Name: str
    gFunction_Calculation_Method: str
    GHEVerticalArray_Object_Name: str
    GHEVerticalSingle_Object_Name_1: str
    GHEVerticalSingle_Object_Name_2: str
    GHEVerticalSingle_Object_Name_3: str
    GHEVerticalSingle_Object_Name_4: str
    GHEVerticalSingle_Object_Name_5: str
    GHEVerticalSingle_Object_Name_6: str
    GHEVerticalSingle_Object_Name_7: str
    GHEVerticalSingle_Object_Name_8: str
    GHEVerticalSingle_Object_Name_9: str
    GHEVerticalSingle_Object_Name_10: str
    GHEVerticalSingle_Object_Name_11: str
    GHEVerticalSingle_Object_Name_12: str
    GHEVerticalSingle_Object_Name_13: str
    GHEVerticalSingle_Object_Name_14: str
    GHEVerticalSingle_Object_Name_15: str
    GHEVerticalSingle_Object_Name_16: str
    GHEVerticalSingle_Object_Name_17: str
    GHEVerticalSingle_Object_Name_18: str
    GHEVerticalSingle_Object_Name_19: str
    GHEVerticalSingle_Object_Name_20: str
    GHEVerticalSingle_Object_Name_21: str
    GHEVerticalSingle_Object_Name_22: str
    GHEVerticalSingle_Object_Name_23: str
    GHEVerticalSingle_Object_Name_24: str
    GHEVerticalSingle_Object_Name_25: str
    GHEVerticalSingle_Object_Name_26: str
    GHEVerticalSingle_Object_Name_27: str
    GHEVerticalSingle_Object_Name_28: str
    GHEVerticalSingle_Object_Name_29: str
    GHEVerticalSingle_Object_Name_30: str
    GHEVerticalSingle_Object_Name_31: str
    GHEVerticalSingle_Object_Name_32: str
    GHEVerticalSingle_Object_Name_33: str
    GHEVerticalSingle_Object_Name_34: str
    GHEVerticalSingle_Object_Name_35: str
    GHEVerticalSingle_Object_Name_36: str
    GHEVerticalSingle_Object_Name_37: str
    GHEVerticalSingle_Object_Name_38: str
    GHEVerticalSingle_Object_Name_39: str
    GHEVerticalSingle_Object_Name_40: str
    GHEVerticalSingle_Object_Name_41: str
    GHEVerticalSingle_Object_Name_42: str
    GHEVerticalSingle_Object_Name_43: str
    GHEVerticalSingle_Object_Name_44: str
    GHEVerticalSingle_Object_Name_45: str
    GHEVerticalSingle_Object_Name_46: str
    GHEVerticalSingle_Object_Name_47: str
    GHEVerticalSingle_Object_Name_48: str
    GHEVerticalSingle_Object_Name_49: str

class GroundheatexchangerVerticalArrayType(TypedDict, total=False):
    """"dict for GroundheatexchangerVerticalArray"""
    Name: str
    GHEVerticalProperties_Object_Name: str
    Number_of_Boreholes_in_XDirection: str
    Number_of_Boreholes_in_YDirection: str
    Borehole_Spacing: str

class GroundheatexchangerVerticalPropertiesType(TypedDict, total=False):
    """"dict for GroundheatexchangerVerticalProperties"""
    Name: str
    Depth_of_Top_of_Borehole: str
    Borehole_Length: str
    Borehole_Diameter: str
    Grout_Thermal_Conductivity: str
    Grout_Thermal_Heat_Capacity: str
    Pipe_Thermal_Conductivity: str
    Pipe_Thermal_Heat_Capacity: str
    Pipe_Outer_Diameter: str
    Pipe_Thickness: str
    UTube_Distance: str

class GroundheatexchangerVerticalSingleType(TypedDict, total=False):
    """"dict for GroundheatexchangerVerticalSingle"""
    Name: str
    GHEVerticalProperties_Object_Name: str
    XLocation: str
    YLocation: str

class GroundheattransferBasementAutogridType(TypedDict, total=False):
    """"dict for GroundheattransferBasementAutogrid"""
    CLEARANCE_Distance_from_outside_of_wall_to_edge: str
    SLABX_X_dimension_of_the_building_slab: str
    SLABY_Y_dimension_of_the_building_slab: str
    ConcAGHeight_Height_of_the_foundation_wall_above_grade: str
    SlabDepth_Thickness_of_the_floor_slab: str
    BaseDepth_Depth_of_the_basement_wall_below_grade: str

class GroundheattransferBasementBldgdataType(TypedDict, total=False):
    """"dict for GroundheattransferBasementBldgdata"""
    DWALL_Wall_thickness: str
    DSLAB_Floor_slab_thickness: str
    DGRAVXY_Width_of_gravel_pit_beside_basement_wall: str
    DGRAVZN_Gravel_depth_extending_above_the_floor_slab: str
    DGRAVZP_Gravel_depth_below_the_floor_slab: str

class GroundheattransferBasementCombldgType(TypedDict, total=False):
    """"dict for GroundheattransferBasementCombldg"""
    January_average_temperature: str
    February_average_temperature: str
    March_average_temperature: str
    April_average_temperature: str
    May_average_temperature: str
    June_average_temperature: str
    July_average_temperature: str
    August_average_temperature: str
    September_average_temperature: str
    October_average_temperature: str
    November_average_temperature: str
    December_average_temperature: str
    Daily_variation_sine_wave_amplitude: str

class GroundheattransferBasementEquivautogridType(TypedDict, total=False):
    """"dict for GroundheattransferBasementEquivautogrid"""
    CLEARANCE_Distance_from_outside_of_wall_to_edge_of_3D_ground_domain: str
    SlabDepth_Thickness_of_the_floor_slab: str
    BaseDepth_Depth_of_the_basement_wall_below_grade: str

class GroundheattransferBasementEquivslabType(TypedDict, total=False):
    """"dict for GroundheattransferBasementEquivslab"""
    APRatio_The_area_to_perimeter_ratio_for_this_slab: str
    EquivSizing_Flag: str

class GroundheattransferBasementInsulationType(TypedDict, total=False):
    """"dict for GroundheattransferBasementInsulation"""
    REXT_R_Value_of_any_exterior_insulation: str
    INSFULL_Flag_Is_the_wall_fully_insulated: str

class GroundheattransferBasementInteriorType(TypedDict, total=False):
    """"dict for GroundheattransferBasementInterior"""
    COND_Flag_Is_the_basement_conditioned: str
    HIN_Downward_convection_only_heat_transfer_coefficient: str
    HIN_Upward_convection_only_heat_transfer_coefficient: str
    HIN_Horizontal_convection_only_heat_transfer_coefficient: str
    HIN_Downward_combined_convection_and_radiation_heat_transfer_coefficient: str
    HIN_Upward_combined_convection_and_radiation_heat_transfer_coefficient: str
    HIN_Horizontal_combined_convection_and_radiation_heat_transfer_coefficient: str

class GroundheattransferBasementManualgridType(TypedDict, total=False):
    """"dict for GroundheattransferBasementManualgrid"""
    NX_Number_of_cells_in_the_X_direction_20: str
    NY_Number_of_cells_in_the_Y_direction_20: str
    NZAG_Number_of_cells_in_the_Z_direction_above_grade_4_Always: str
    NZBG_Number_of_cells_in_Z_direction_below_grade_1035: str
    IBASE_X_direction_cell_indicator_of_slab_edge_520: str
    JBASE_Y_direction_cell_indicator_of_slab_edge_520: str
    KBASE_Z_direction_cell_indicator_of_the_top_of_the_floor_slab_520: str

class GroundheattransferBasementMatlpropsType(TypedDict, total=False):
    """"dict for GroundheattransferBasementMatlprops"""
    NMAT_Number_of_materials_in_this_domain: str
    Density_for_Foundation_Wall: str
    density_for_Floor_Slab: str
    density_for_Ceiling: str
    density_for_Soil: str
    density_for_Gravel: str
    density_for_Wood: str
    Specific_heat_for_foundation_wall: str
    Specific_heat_for_floor_slab: str
    Specific_heat_for_ceiling: str
    Specific_heat_for_soil: str
    Specific_heat_for_gravel: str
    Specific_heat_for_wood: str
    Thermal_conductivity_for_foundation_wall: str
    Thermal_conductivity_for_floor_slab: str
    Thermal_conductivity_for_ceiling: str
    thermal_conductivity_for_soil: str
    thermal_conductivity_for_gravel: str
    thermal_conductivity_for_wood: str

class GroundheattransferBasementSimparametersType(TypedDict, total=False):
    """"dict for GroundheattransferBasementSimparameters"""
    F_Multiplier_for_the_ADI_solution: str
    IYRS_Maximum_number_of_yearly_iterations: str

class GroundheattransferBasementSurfacepropsType(TypedDict, total=False):
    """"dict for GroundheattransferBasementSurfaceprops"""
    ALBEDO_Surface_albedo_for_No_snow_conditions: str
    ALBEDO_Surface_albedo_for_snow_conditions: str
    EPSLN_Surface_emissivity_No_Snow: str
    EPSLN_Surface_emissivity_with_Snow: str
    VEGHT_Surface_roughness_No_snow_conditions: str
    VEGHT_Surface_roughness_Snow_conditions: str
    PET_Flag_Potential_evapotranspiration_on: str

class GroundheattransferBasementXfaceType(TypedDict, total=False):
    """"dict for GroundheattransferBasementXface"""
    N1: str
    N2: str
    N3: str
    N4: str
    N5: str
    N6: str
    N7: str
    N8: str
    N9: str
    N10: str
    N11: str
    N12: str
    N13: str
    N14: str
    N15: str
    N16: str
    N17: str
    N18: str
    N19: str
    N20: str
    N21: str
    N22: str
    N23: str
    N24: str
    N25: str
    N26: str
    N27: str
    N28: str
    N29: str
    N30: str
    N31: str
    N32: str
    N33: str
    N34: str
    N35: str
    N36: str
    N37: str
    N38: str
    N39: str
    N40: str
    N41: str
    N42: str
    N43: str
    N44: str

class GroundheattransferBasementYfaceType(TypedDict, total=False):
    """"dict for GroundheattransferBasementYface"""
    N1: str
    N2: str
    N3: str
    N4: str
    N5: str
    N6: str
    N7: str
    N8: str
    N9: str
    N10: str
    N11: str
    N12: str
    N13: str
    N14: str
    N15: str
    N16: str
    N17: str
    N18: str
    N19: str
    N20: str
    N21: str
    N22: str
    N23: str
    N24: str
    N25: str
    N26: str
    N27: str
    N28: str
    N29: str
    N30: str
    N31: str
    N32: str
    N33: str
    N34: str
    N35: str
    N36: str
    N37: str
    N38: str
    N39: str
    N40: str
    N41: str
    N42: str
    N43: str
    N44: str

class GroundheattransferBasementZfaceType(TypedDict, total=False):
    """"dict for GroundheattransferBasementZface"""
    N1: str
    N2: str
    N3: str
    N4: str
    N5: str
    N6: str
    N7: str
    N8: str
    N9: str
    N10: str
    N11: str
    N12: str
    N13: str
    N14: str
    N15: str
    N16: str
    N17: str
    N18: str
    N19: str
    N20: str
    N21: str
    N22: str
    N23: str
    N24: str
    N25: str
    N26: str
    N27: str
    N28: str
    N29: str
    N30: str
    N31: str
    N32: str
    N33: str
    N34: str
    N35: str
    N36: str
    N37: str
    N38: str
    N39: str
    N40: str

class GroundheattransferControlType(TypedDict, total=False):
    """"dict for GroundheattransferControl"""
    Name: str
    Run_Basement_Preprocessor: str
    Run_Slab_Preprocessor: str

class GroundheattransferSlabAutogridType(TypedDict, total=False):
    """"dict for GroundheattransferSlabAutogrid"""
    SLABX_X_dimension_of_the_building_slab: str
    SLABY_Y_dimension_of_the_building_slab: str
    SLABDEPTH_Thickness_of_slab_on_grade: str
    CLEARANCE_Distance_from_edge_of_slab_to_domain_edge: str
    ZCLEARANCE_Distance_from_bottom_of_slab_to_domain_bottom: str

class GroundheattransferSlabBldgpropsType(TypedDict, total=False):
    """"dict for GroundheattransferSlabBldgprops"""
    IYRS_Number_of_years_to_iterate: str
    Shape_Slab_shape: str
    HBLDG_Building_height: str
    TIN1_January_Indoor_Average_Temperature_Setpoint: str
    TIN2_February_Indoor_Average_Temperature_Setpoint: str
    TIN3_March_Indoor_Average_Temperature_Setpoint: str
    TIN4_April_Indoor_Average_Temperature_Setpoint: str
    TIN5_May_Indoor_Average_Temperature_Setpoint: str
    TIN6_June_Indoor_Average_Temperature_Setpoint: str
    TIN7_July_Indoor_Average_Temperature_Setpoint: str
    TIN8_August_Indoor_Average_Temperature_Setpoint: str
    TIN9_September_Indoor_Average_Temperature_Setpoint: str
    TIN10_October_Indoor_Average_Temperature_Setpoint: str
    TIN11_November_Indoor_Average_Temperature_Setpoint: str
    TIN12_December_Indoor_Average_Temperature_Setpoint: str
    TINAmp_Daily_Indoor_sine_wave_variation_amplitude: str
    ConvTol_Convergence_Tolerance: str

class GroundheattransferSlabBoundcondsType(TypedDict, total=False):
    """"dict for GroundheattransferSlabBoundconds"""
    EVTR_Is_surface_evapotranspiration_modeled: str
    FIXBC_is_the_lower_boundary_at_a_fixed_temperature: str
    TDEEPin: str
    USRHflag_Is_the_ground_surface_h_specified_by_the_user: str
    USERH_User_specified_ground_surface_heat_transfer_coefficient: str

class GroundheattransferSlabEquivalentslabType(TypedDict, total=False):
    """"dict for GroundheattransferSlabEquivalentslab"""
    APRatio_The_area_to_perimeter_ratio_for_this_slab: str
    SLABDEPTH_Thickness_of_slab_on_grade: str
    CLEARANCE_Distance_from_edge_of_slab_to_domain_edge: str
    ZCLEARANCE_Distance_from_bottom_of_slab_to_domain_bottom: str

class GroundheattransferSlabInsulationType(TypedDict, total=False):
    """"dict for GroundheattransferSlabInsulation"""
    RINS_R_value_of_under_slab_insulation: str
    DINS_Width_of_strip_of_under_slab_insulation: str
    RVINS_R_value_of_vertical_insulation: str
    ZVINS_Depth_of_vertical_insulation: str
    IVINS_Flag_Is_there_vertical_insulation: str

class GroundheattransferSlabManualgridType(TypedDict, total=False):
    """"dict for GroundheattransferSlabManualgrid"""
    NX_Number_of_cells_in_the_X_direction: str
    NY_Number_of_cells_in_the_Y_direction: str
    NZ_Number_of_cells_in_the_Z_direction: str
    IBOX_X_direction_cell_indicator_of_slab_edge: str
    JBOX_Y_direction_cell_indicator_of_slab_edge: str

class GroundheattransferSlabMaterialsType(TypedDict, total=False):
    """"dict for GroundheattransferSlabMaterials"""
    NMAT_Number_of_materials: str
    ALBEDO_Surface_Albedo_No_Snow: str
    ALBEDO_Surface_Albedo_Snow: str
    EPSLW_Surface_Emissivity_No_Snow: str
    EPSLW_Surface_Emissivity_Snow: str
    Z0_Surface_Roughness_No_Snow: str
    Z0_Surface_Roughness_Snow: str
    HIN_Indoor_HConv_Downward_Flow: str
    HIN_Indoor_HConv_Upward: str

class GroundheattransferSlabMatlpropsType(TypedDict, total=False):
    """"dict for GroundheattransferSlabMatlprops"""
    RHO_Slab_Material_density: str
    RHO_Soil_Density: str
    CP_Slab_CP: str
    CP_Soil_CP: str
    TCON_Slab_k: str
    TCON_Soil_k: str

class GroundheattransferSlabXfaceType(TypedDict, total=False):
    """"dict for GroundheattransferSlabXface"""
    N1: str
    N2: str
    N3: str
    N4: str
    N5: str
    N6: str
    N7: str
    N8: str
    N9: str
    N10: str
    N11: str
    N12: str
    N13: str
    N14: str
    N15: str
    N16: str
    N17: str
    N18: str
    N19: str
    N20: str
    N21: str
    N22: str
    N23: str
    N24: str
    N25: str
    N26: str
    N27: str
    N28: str
    N29: str
    N30: str
    N31: str
    N32: str
    N33: str
    N34: str
    N35: str
    N36: str
    N37: str
    N38: str
    N39: str
    N40: str

class GroundheattransferSlabYfaceType(TypedDict, total=False):
    """"dict for GroundheattransferSlabYface"""
    N1: str
    N2: str
    N3: str
    N4: str
    N5: str
    N6: str
    N7: str
    N8: str
    N9: str
    N10: str
    N11: str
    N12: str
    N13: str
    N14: str
    N15: str
    N16: str
    N17: str
    N18: str
    N19: str
    N20: str
    N21: str
    N22: str
    N23: str
    N24: str
    N25: str
    N26: str
    N27: str
    N28: str
    N29: str
    N30: str
    N31: str
    N32: str
    N33: str
    N34: str
    N35: str
    N36: str
    N37: str
    N38: str
    N39: str
    N40: str

class GroundheattransferSlabZfaceType(TypedDict, total=False):
    """"dict for GroundheattransferSlabZface"""
    N1: str
    N2: str
    N3: str
    N4: str
    N5: str
    N6: str
    N7: str
    N8: str
    N9: str
    N10: str
    N11: str
    N12: str
    N13: str
    N14: str
    N15: str
    N16: str
    N17: str
    N18: str
    N19: str
    N20: str
    N21: str
    N22: str
    N23: str
    N24: str
    N25: str

class HeaderedpumpsConstantspeedType(TypedDict, total=False):
    """"dict for HeaderedpumpsConstantspeed"""
    Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str
    Total_Design_Flow_Rate: str
    Number_of_Pumps_in_Bank: str
    Flow_Sequencing_Control_Scheme: str
    Design_Pump_Head: str
    Design_Power_Consumption: str
    Motor_Efficiency: str
    Fraction_of_Motor_Inefficiencies_to_Fluid_Stream: str
    Pump_Control_Type: str
    Pump_Flow_Rate_Schedule_Name: str
    Zone_Name: str
    Skin_Loss_Radiative_Fraction: str
    Design_Power_Sizing_Method: str
    Design_Electric_Power_per_Unit_Flow_Rate: str
    Design_Shaft_Power_per_Unit_Flow_Rate_per_Unit_Head: str
    EndUse_Subcategory: str

class HeaderedpumpsVariablespeedType(TypedDict, total=False):
    """"dict for HeaderedpumpsVariablespeed"""
    Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str
    Total_Design_Flow_Rate: str
    Number_of_Pumps_in_Bank: str
    Flow_Sequencing_Control_Scheme: str
    Design_Pump_Head: str
    Design_Power_Consumption: str
    Motor_Efficiency: str
    Fraction_of_Motor_Inefficiencies_to_Fluid_Stream: str
    Coefficient_1_of_the_Part_Load_Performance_Curve: str
    Coefficient_2_of_the_Part_Load_Performance_Curve: str
    Coefficient_3_of_the_Part_Load_Performance_Curve: str
    Coefficient_4_of_the_Part_Load_Performance_Curve: str
    Minimum_Flow_Rate_Fraction: str
    Pump_Control_Type: str
    Pump_Flow_Rate_Schedule_Name: str
    Zone_Name: str
    Skin_Loss_Radiative_Fraction: str
    Design_Power_Sizing_Method: str
    Design_Electric_Power_per_Unit_Flow_Rate: str
    Design_Shaft_Power_per_Unit_Flow_Rate_per_Unit_Head: str
    EndUse_Subcategory: str

class HeatbalancealgorithmType(TypedDict, total=False):
    """"dict for Heatbalancealgorithm"""
    Algorithm: str
    Surface_Temperature_Upper_Limit: str
    Minimum_Surface_Convection_Heat_Transfer_Coefficient_Value: str
    Maximum_Surface_Convection_Heat_Transfer_Coefficient_Value: str

class HeatbalancesettingsConductionfinitedifferenceType(TypedDict, total=False):
    """"dict for HeatbalancesettingsConductionfinitedifference"""
    Difference_Scheme: str
    Space_Discretization_Constant: str
    Relaxation_Factor: str
    Inside_Face_Surface_Temperature_Convergence_Criteria: str

class HeatexchangerAirtoairFlatplateType(TypedDict, total=False):
    """"dict for HeatexchangerAirtoairFlatplate"""
    Name: str
    Availability_Schedule_Name: str
    Flow_Arrangement_Type: str
    Economizer_Lockout: str
    Ratio_of_Supply_to_Secondary_hA_Values: str
    Nominal_Supply_Air_Flow_Rate: str
    Nominal_Supply_Air_Inlet_Temperature: str
    Nominal_Supply_Air_Outlet_Temperature: str
    Nominal_Secondary_Air_Flow_Rate: str
    Nominal_Secondary_Air_Inlet_Temperature: str
    Nominal_Electric_Power: str
    Supply_Air_Inlet_Node_Name: str
    Supply_Air_Outlet_Node_Name: str
    Secondary_Air_Inlet_Node_Name: str
    Secondary_Air_Outlet_Node_Name: str

class HeatexchangerAirtoairSensibleandlatentType(TypedDict, total=False):
    """"dict for HeatexchangerAirtoairSensibleandlatent"""
    Name: str
    Availability_Schedule_Name: str
    Nominal_Supply_Air_Flow_Rate: str
    Sensible_Effectiveness_at_100_Heating_Air_Flow: str
    Latent_Effectiveness_at_100_Heating_Air_Flow: str
    Sensible_Effectiveness_at_100_Cooling_Air_Flow: str
    Latent_Effectiveness_at_100_Cooling_Air_Flow: str
    Supply_Air_Inlet_Node_Name: str
    Supply_Air_Outlet_Node_Name: str
    Exhaust_Air_Inlet_Node_Name: str
    Exhaust_Air_Outlet_Node_Name: str
    Nominal_Electric_Power: str
    Supply_Air_Outlet_Temperature_Control: str
    Heat_Exchanger_Type: str
    Frost_Control_Type: str
    Threshold_Temperature: str
    Initial_Defrost_Time_Fraction: str
    Rate_of_Defrost_Time_Fraction_Increase: str
    Economizer_Lockout: str
    Sensible_Effectiveness_of_Heating_Air_Flow_Curve_Name: str
    Latent_Effectiveness_of_Heating_Air_Flow_Curve_Name: str
    Sensible_Effectiveness_of_Cooling_Air_Flow_Curve_Name: str
    Latent_Effectiveness_of_Cooling_Air_Flow_Curve_Name: str

class HeatexchangerDesiccantBalancedflowType(TypedDict, total=False):
    """"dict for HeatexchangerDesiccantBalancedflow"""
    Name: str
    Availability_Schedule_Name: str
    Regeneration_Air_Inlet_Node_Name: str
    Regeneration_Air_Outlet_Node_Name: str
    Process_Air_Inlet_Node_Name: str
    Process_Air_Outlet_Node_Name: str
    Heat_Exchanger_Performance_Object_Type: str
    Heat_Exchanger_Performance_Name: str
    Economizer_Lockout: str

class HeatexchangerDesiccantBalancedflowPerformancedatatype1Type(TypedDict, total=False):
    """"dict for HeatexchangerDesiccantBalancedflowPerformancedatatype1"""
    Name: str
    Nominal_Air_Flow_Rate: str
    Nominal_Air_Face_Velocity: str
    Nominal_Electric_Power: str
    Temperature_Equation_Coefficient_1: str
    Temperature_Equation_Coefficient_2: str
    Temperature_Equation_Coefficient_3: str
    Temperature_Equation_Coefficient_4: str
    Temperature_Equation_Coefficient_5: str
    Temperature_Equation_Coefficient_6: str
    Temperature_Equation_Coefficient_7: str
    Temperature_Equation_Coefficient_8: str
    Minimum_Regeneration_Inlet_Air_Humidity_Ratio_for_Temperature_Equation: str
    Maximum_Regeneration_Inlet_Air_Humidity_Ratio_for_Temperature_Equation: str
    Minimum_Regeneration_Inlet_Air_Temperature_for_Temperature_Equation: str
    Maximum_Regeneration_Inlet_Air_Temperature_for_Temperature_Equation: str
    Minimum_Process_Inlet_Air_Humidity_Ratio_for_Temperature_Equation: str
    Maximum_Process_Inlet_Air_Humidity_Ratio_for_Temperature_Equation: str
    Minimum_Process_Inlet_Air_Temperature_for_Temperature_Equation: str
    Maximum_Process_Inlet_Air_Temperature_for_Temperature_Equation: str
    Minimum_Regeneration_Air_Velocity_for_Temperature_Equation: str
    Maximum_Regeneration_Air_Velocity_for_Temperature_Equation: str
    Minimum_Regeneration_Outlet_Air_Temperature_for_Temperature_Equation: str
    Maximum_Regeneration_Outlet_Air_Temperature_for_Temperature_Equation: str
    Minimum_Regeneration_Inlet_Air_Relative_Humidity_for_Temperature_Equation: str
    Maximum_Regeneration_Inlet_Air_Relative_Humidity_for_Temperature_Equation: str
    Minimum_Process_Inlet_Air_Relative_Humidity_for_Temperature_Equation: str
    Maximum_Process_Inlet_Air_Relative_Humidity_for_Temperature_Equation: str
    Humidity_Ratio_Equation_Coefficient_1: str
    Humidity_Ratio_Equation_Coefficient_2: str
    Humidity_Ratio_Equation_Coefficient_3: str
    Humidity_Ratio_Equation_Coefficient_4: str
    Humidity_Ratio_Equation_Coefficient_5: str
    Humidity_Ratio_Equation_Coefficient_6: str
    Humidity_Ratio_Equation_Coefficient_7: str
    Humidity_Ratio_Equation_Coefficient_8: str
    Minimum_Regeneration_Inlet_Air_Humidity_Ratio_for_Humidity_Ratio_Equation: str
    Maximum_Regeneration_Inlet_Air_Humidity_Ratio_for_Humidity_Ratio_Equation: str
    Minimum_Regeneration_Inlet_Air_Temperature_for_Humidity_Ratio_Equation: str
    Maximum_Regeneration_Inlet_Air_Temperature_for_Humidity_Ratio_Equation: str
    Minimum_Process_Inlet_Air_Humidity_Ratio_for_Humidity_Ratio_Equation: str
    Maximum_Process_Inlet_Air_Humidity_Ratio_for_Humidity_Ratio_Equation: str
    Minimum_Process_Inlet_Air_Temperature_for_Humidity_Ratio_Equation: str
    Maximum_Process_Inlet_Air_Temperature_for_Humidity_Ratio_Equation: str
    Minimum_Regeneration_Air_Velocity_for_Humidity_Ratio_Equation: str
    Maximum_Regeneration_Air_Velocity_for_Humidity_Ratio_Equation: str
    Minimum_Regeneration_Outlet_Air_Humidity_Ratio_for_Humidity_Ratio_Equation: str
    Maximum_Regeneration_Outlet_Air_Humidity_Ratio_for_Humidity_Ratio_Equation: str
    Minimum_Regeneration_Inlet_Air_Relative_Humidity_for_Humidity_Ratio_Equation: str
    Maximum_Regeneration_Inlet_Air_Relative_Humidity_for_Humidity_Ratio_Equation: str
    Minimum_Process_Inlet_Air_Relative_Humidity_for_Humidity_Ratio_Equation: str
    Maximum_Process_Inlet_Air_Relative_Humidity_for_Humidity_Ratio_Equation: str

class HeatexchangerFluidtofluidType(TypedDict, total=False):
    """"dict for HeatexchangerFluidtofluid"""
    Name: str
    Availability_Schedule_Name: str
    Loop_Demand_Side_Inlet_Node_Name: str
    Loop_Demand_Side_Outlet_Node_Name: str
    Loop_Demand_Side_Design_Flow_Rate: str
    Loop_Supply_Side_Inlet_Node_Name: str
    Loop_Supply_Side_Outlet_Node_Name: str
    Loop_Supply_Side_Design_Flow_Rate: str
    Heat_Exchange_Model_Type: str
    Heat_Exchanger_UFactor_Times_Area_Value: str
    Control_Type: str
    Heat_Exchanger_Setpoint_Node_Name: str
    Minimum_Temperature_Difference_to_Activate_Heat_Exchanger: str
    Heat_Transfer_Metering_End_Use_Type: str
    Component_Override_Loop_Supply_Side_Inlet_Node_Name: str
    Component_Override_Loop_Demand_Side_Inlet_Node_Name: str
    Component_Override_Cooling_Control_Temperature_Mode: str
    Sizing_Factor: str
    Operation_Minimum_Temperature_Limit: str
    Operation_Maximum_Temperature_Limit: str

class HeatpumpAirtowaterFuelfiredCoolingType(TypedDict, total=False):
    """"dict for HeatpumpAirtowaterFuelfiredCooling"""
    Name: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    Air_Source_Node_Name: str
    Companion_Heating_Heat_Pump_Name: str
    Fuel_Type: str
    EndUse_Subcategory: str
    Nominal_Cooling_Capacity: str
    Nominal_COP: str
    Design_Flow_Rate: str
    Design_Supply_Temperature: str
    Design_Temperature_Lift: str
    Sizing_Factor: str
    Flow_Mode: str
    Outdoor_Air_Temperature_Curve_Input_Variable: str
    Water_Temperature_Curve_Input_Variable: str
    Normalized_Capacity_Function_of_Temperature_Curve_Name: str
    Fuel_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Fuel_Energy_Input_Ratio_Function_of_PLR_Curve_Name: str
    Minimum_Part_Load_Ratio: str
    Maximum_Part_Load_Ratio: str
    Cycling_Ratio_Factor_Curve_Name: str
    Nominal_Auxiliary_Electric_Power: str
    Auxiliary_Electric_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Auxiliary_Electric_Energy_Input_Ratio_Function_of_PLR_Curve_Name: str
    Standby_Electric_Power: str

class HeatpumpAirtowaterFuelfiredHeatingType(TypedDict, total=False):
    """"dict for HeatpumpAirtowaterFuelfiredHeating"""
    Name: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    Air_Source_Node_Name: str
    Companion_Cooling_Heat_Pump_Name: str
    Fuel_Type: str
    EndUse_Subcategory: str
    Nominal_Heating_Capacity: str
    Nominal_COP: str
    Design_Flow_Rate: str
    Design_Supply_Temperature: str
    Design_Temperature_Lift: str
    Sizing_Factor: str
    Flow_Mode: str
    Outdoor_Air_Temperature_Curve_Input_Variable: str
    Water_Temperature_Curve_Input_Variable: str
    Normalized_Capacity_Function_of_Temperature_Curve_Name: str
    Fuel_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Fuel_Energy_Input_Ratio_Function_of_PLR_Curve_Name: str
    Minimum_Part_Load_Ratio: str
    Maximum_Part_Load_Ratio: str
    Defrost_Control_Type: str
    Defrost_Operation_Time_Fraction: str
    Fuel_Energy_Input_Ratio_Defrost_Adjustment_Curve_Name: str
    Resistive_Defrost_Heater_Capacity: str
    Maximum_Outdoor_Drybulb_Temperature_for_Defrost_Operation: str
    Cycling_Ratio_Factor_Curve_Name: str
    Nominal_Auxiliary_Electric_Power: str
    Auxiliary_Electric_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Auxiliary_Electric_Energy_Input_Ratio_Function_of_PLR_Curve_Name: str
    Standby_Electric_Power: str

class HeatpumpPlantloopEirCoolingType(TypedDict, total=False):
    """"dict for HeatpumpPlantloopEirCooling"""
    Name: str
    Load_Side_Inlet_Node_Name: str
    Load_Side_Outlet_Node_Name: str
    Condenser_Type: str
    Source_Side_Inlet_Node_Name: str
    Source_Side_Outlet_Node_Name: str
    Companion_Heat_Pump_Name: str
    Load_Side_Reference_Flow_Rate: str
    Source_Side_Reference_Flow_Rate: str
    Reference_Capacity: str
    Reference_Coefficient_of_Performance: str
    Sizing_Factor: str
    Capacity_Modifier_Function_of_Temperature_Curve_Name: str
    Electric_Input_to_Output_Ratio_Modifier_Function_of_Temperature_Curve_Name: str
    Electric_Input_to_Output_Ratio_Modifier_Function_of_Part_Load_Ratio_Curve_Name: str
    Control_Type: str
    Flow_Mode: str
    Minimum_Part_Load_Ratio: str
    Minimum_Source_Inlet_Temperature: str
    Maximum_Source_Inlet_Temperature: str
    Minimum_Supply_Water_Temperature_Curve_Name: str
    Maximum_Supply_Water_Temperature_Curve_Name: str

class HeatpumpPlantloopEirHeatingType(TypedDict, total=False):
    """"dict for HeatpumpPlantloopEirHeating"""
    Name: str
    Load_Side_Inlet_Node_Name: str
    Load_Side_Outlet_Node_Name: str
    Condenser_Type: str
    Source_Side_Inlet_Node_Name: str
    Source_Side_Outlet_Node_Name: str
    Companion_Heat_Pump_Name: str
    Load_Side_Reference_Flow_Rate: str
    Source_Side_Reference_Flow_Rate: str
    Reference_Capacity: str
    Reference_Coefficient_of_Performance: str
    Sizing_Factor: str
    Capacity_Modifier_Function_of_Temperature_Curve_Name: str
    Electric_Input_to_Output_Ratio_Modifier_Function_of_Temperature_Curve_Name: str
    Electric_Input_to_Output_Ratio_Modifier_Function_of_Part_Load_Ratio_Curve_Name: str
    Heating_To_Cooling_Capacity_Sizing_Ratio: str
    Heat_Pump_Sizing_Method: str
    Control_Type: str
    Flow_Mode: str
    Minimum_Part_Load_Ratio: str
    Minimum_Source_Inlet_Temperature: str
    Maximum_Source_Inlet_Temperature: str
    Minimum_Supply_Water_Temperature_Curve_Name: str
    Maximum_Supply_Water_Temperature_Curve_Name: str
    Dry_Outdoor_Correction_Factor_Curve_Name: str
    Maximum_Outdoor_Dry_Bulb_Temperature_For_Defrost_Operation: str
    Heat_Pump_Defrost_Control: str
    Heat_Pump_Defrost_Time_Period_Fraction: str
    Defrost_Energy_Input_Ratio_Function_of_Temperature_Curve_Name: str
    Timed_Empirical_Defrost_Frequency_Curve_Name: str
    Timed_Empirical_Defrost_Heat_Load_Penalty_Curve_Name: str
    Timed_Empirical_Defrost_Heat_Input_Energy_Fraction_Curve_Name: str

class HeatpumpWatertowaterEquationfitCoolingType(TypedDict, total=False):
    """"dict for HeatpumpWatertowaterEquationfitCooling"""
    Name: str
    Source_Side_Inlet_Node_Name: str
    Source_Side_Outlet_Node_Name: str
    Load_Side_Inlet_Node_Name: str
    Load_Side_Outlet_Node_Name: str
    Reference_Load_Side_Flow_Rate: str
    Reference_Source_Side_Flow_Rate: str
    Reference_Cooling_Capacity: str
    Reference_Cooling_Power_Consumption: str
    Cooling_Capacity_Curve_Name: str
    Cooling_Compressor_Power_Curve_Name: str
    Reference_Coefficient_of_Performance: str
    Sizing_Factor: str
    Companion_Heating_Heat_Pump_Name: str

class HeatpumpWatertowaterEquationfitHeatingType(TypedDict, total=False):
    """"dict for HeatpumpWatertowaterEquationfitHeating"""
    Name: str
    Source_Side_Inlet_Node_Name: str
    Source_Side_Outlet_Node_Name: str
    Load_Side_Inlet_Node_Name: str
    Load_Side_Outlet_Node_Name: str
    Reference_Load_Side_Flow_Rate: str
    Reference_Source_Side_Flow_Rate: str
    Reference_Heating_Capacity: str
    Reference_Heating_Power_Consumption: str
    Heating_Capacity_Curve_Name: str
    Heating_Compressor_Power_Curve_Name: str
    Reference_Coefficient_of_Performance: str
    Sizing_Factor: str
    Companion_Cooling_Heat_Pump_Name: str

class HeatpumpWatertowaterParameterestimationCoolingType(TypedDict, total=False):
    """"dict for HeatpumpWatertowaterParameterestimationCooling"""
    Name: str
    Source_Side_Inlet_Node_Name: str
    Source_Side_Outlet_Node_Name: str
    Load_Side_Inlet_Node_Name: str
    Load_Side_Outlet_Node_Name: str
    Nominal_COP: str
    Nominal_Capacity: str
    Minimum_Part_Load_Ratio: str
    Maximum_Part_Load_Ratio: str
    Optimum_Part_Load_Ratio: str
    Load_Side_Flow_Rate: str
    Source_Side_Flow_Rate: str
    Load_Side_Heat_Transfer_Coefficient: str
    Source_Side_Heat_Transfer_Coefficient: str
    Piston_Displacement: str
    Compressor_Clearance_Factor: str
    Compressor_Suction_and_Discharge_Pressure_Drop: str
    Superheating: str
    Constant_Part_of_Electromechanical_Power_Losses: str
    Loss_Factor: str
    High_Pressure_Cut_Off: str
    Low_Pressure_Cut_Off: str

class HeatpumpWatertowaterParameterestimationHeatingType(TypedDict, total=False):
    """"dict for HeatpumpWatertowaterParameterestimationHeating"""
    Name: str
    Source_Side_Inlet_Node_Name: str
    Source_Side_Outlet_Node_Name: str
    Load_Side_Inlet_Node_Name: str
    Load_Side_Outlet_Node_Name: str
    Nominal_COP: str
    Nominal_Capacity: str
    Minimum_Part_Load_Ratio: str
    Maximum_Part_Load_Ratio: str
    Optimum_Part_Load_Ratio: str
    Load_Side_Flow_Rate: str
    Source_Side_Flow_Rate: str
    Load_Side_Heat_Transfer_Coefficient: str
    Source_Side_Heat_Transfer_Coefficient: str
    Piston_Displacement: str
    Compressor_Clearance_Factor: str
    Compressor_Suction_and_Discharge_Pressure_Drop: str
    Superheating: str
    Constant_Part_of_Electromechanical_Power_Losses: str
    Loss_Factor: str
    High_Pressure_Cut_Off: str
    Low_Pressure_Cut_Off: str

class HotwaterequipmentType(TypedDict, total=False):
    """"dict for Hotwaterequipment"""
    Name: str
    Zone_or_ZoneList_or_Space_or_SpaceList_Name: str
    Schedule_Name: str
    Design_Level_Calculation_Method: str
    Design_Level: str
    Power_per_Floor_Area: str
    Power_per_Person: str
    Fraction_Latent: str
    Fraction_Radiant: str
    Fraction_Lost: str
    EndUse_Subcategory: str

class HumidifierSteamElectricType(TypedDict, total=False):
    """"dict for HumidifierSteamElectric"""
    Name: str
    Availability_Schedule_Name: str
    Rated_Capacity: str
    Rated_Power: str
    Rated_Fan_Power: str
    Standby_Power: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Water_Storage_Tank_Name: str

class HumidifierSteamGasType(TypedDict, total=False):
    """"dict for HumidifierSteamGas"""
    Name: str
    Availability_Schedule_Name: str
    Rated_Capacity: str
    Rated_Gas_Use_Rate: str
    Thermal_Efficiency: str
    Thermal_Efficiency_Modifier_Curve_Name: str
    Rated_Fan_Power: str
    Auxiliary_Electric_Power: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Water_Storage_Tank_Name: str
    Inlet_Water_Temperature_Option: str

class HvacsystemrootfindingalgorithmType(TypedDict, total=False):
    """"dict for Hvacsystemrootfindingalgorithm"""
    Algorithm: str
    Number_of_Iterations_Before_Algorithm_Switch: str

class HvactemplatePlantBoilerType(TypedDict, total=False):
    """"dict for HvactemplatePlantBoiler"""
    Name: str
    Boiler_Type: str
    Capacity: str
    Efficiency: str
    Fuel_Type: str
    Priority: str
    Sizing_Factor: str
    Minimum_Part_Load_Ratio: str
    Maximum_Part_Load_Ratio: str
    Optimum_Part_Load_Ratio: str
    Water_Outlet_Upper_Temperature_Limit: str
    Template_Plant_Loop_Type: str

class HvactemplatePlantBoilerObjectreferenceType(TypedDict, total=False):
    """"dict for HvactemplatePlantBoilerObjectreference"""
    Name: str
    Boiler_Object_Type: str
    Boiler_Name: str
    Priority: str
    Template_Plant_Loop_Type: str

class HvactemplatePlantChilledwaterloopType(TypedDict, total=False):
    """"dict for HvactemplatePlantChilledwaterloop"""
    Name: str
    Pump_Schedule_Name: str
    Pump_Control_Type: str
    Chiller_Plant_Operation_Scheme_Type: str
    Chiller_Plant_Equipment_Operation_Schemes_Name: str
    Chilled_Water_Setpoint_Schedule_Name: str
    Chilled_Water_Design_Setpoint: str
    Chilled_Water_Pump_Configuration: str
    Primary_Chilled_Water_Pump_Rated_Head: str
    Secondary_Chilled_Water_Pump_Rated_Head: str
    Condenser_Plant_Operation_Scheme_Type: str
    Condenser_Equipment_Operation_Schemes_Name: str
    Condenser_Water_Temperature_Control_Type: str
    Condenser_Water_Setpoint_Schedule_Name: str
    Condenser_Water_Design_Setpoint: str
    Condenser_Water_Pump_Rated_Head: str
    Chilled_Water_Setpoint_Reset_Type: str
    Chilled_Water_Setpoint_at_Outdoor_DryBulb_Low: str
    Chilled_Water_Reset_Outdoor_DryBulb_Low: str
    Chilled_Water_Setpoint_at_Outdoor_DryBulb_High: str
    Chilled_Water_Reset_Outdoor_DryBulb_High: str
    Chilled_Water_Primary_Pump_Type: str
    Chilled_Water_Secondary_Pump_Type: str
    Condenser_Water_Pump_Type: str
    Chilled_Water_Supply_Side_Bypass_Pipe: str
    Chilled_Water_Demand_Side_Bypass_Pipe: str
    Condenser_Water_Supply_Side_Bypass_Pipe: str
    Condenser_Water_Demand_Side_Bypass_Pipe: str
    Fluid_Type: str
    Loop_Design_Delta_Temperature: str
    Minimum_Outdoor_Dry_Bulb_Temperature: str
    Chilled_Water_Load_Distribution_Scheme: str
    Condenser_Water_Load_Distribution_Scheme: str

class HvactemplatePlantChillerType(TypedDict, total=False):
    """"dict for HvactemplatePlantChiller"""
    Name: str
    Chiller_Type: str
    Capacity: str
    Nominal_COP: str
    Condenser_Type: str
    Priority: str
    Sizing_Factor: str
    Minimum_Part_Load_Ratio: str
    Maximum_Part_Load_Ratio: str
    Optimum_Part_Load_Ratio: str
    Minimum_Unloading_Ratio: str
    Leaving_Chilled_Water_Lower_Temperature_Limit: str

class HvactemplatePlantChillerObjectreferenceType(TypedDict, total=False):
    """"dict for HvactemplatePlantChillerObjectreference"""
    Name: str
    Chiller_Object_Type: str
    Chiller_Name: str
    Priority: str

class HvactemplatePlantHotwaterloopType(TypedDict, total=False):
    """"dict for HvactemplatePlantHotwaterloop"""
    Name: str
    Pump_Schedule_Name: str
    Pump_Control_Type: str
    Hot_Water_Plant_Operation_Scheme_Type: str
    Hot_Water_Plant_Equipment_Operation_Schemes_Name: str
    Hot_Water_Setpoint_Schedule_Name: str
    Hot_Water_Design_Setpoint: str
    Hot_Water_Pump_Configuration: str
    Hot_Water_Pump_Rated_Head: str
    Hot_Water_Setpoint_Reset_Type: str
    Hot_Water_Setpoint_at_Outdoor_DryBulb_Low: str
    Hot_Water_Reset_Outdoor_DryBulb_Low: str
    Hot_Water_Setpoint_at_Outdoor_DryBulb_High: str
    Hot_Water_Reset_Outdoor_DryBulb_High: str
    Hot_Water_Pump_Type: str
    Supply_Side_Bypass_Pipe: str
    Demand_Side_Bypass_Pipe: str
    Fluid_Type: str
    Loop_Design_Delta_Temperature: str
    Maximum_Outdoor_Dry_Bulb_Temperature: str
    Load_Distribution_Scheme: str

class HvactemplatePlantMixedwaterloopType(TypedDict, total=False):
    """"dict for HvactemplatePlantMixedwaterloop"""
    Name: str
    Pump_Schedule_Name: str
    Pump_Control_Type: str
    Operation_Scheme_Type: str
    Equipment_Operation_Schemes_Name: str
    High_Temperature_Setpoint_Schedule_Name: str
    High_Temperature_Design_Setpoint: str
    Low_Temperature_Setpoint_Schedule_Name: str
    Low_Temperature_Design_Setpoint: str
    Water_Pump_Configuration: str
    Water_Pump_Rated_Head: str
    Water_Pump_Type: str
    Supply_Side_Bypass_Pipe: str
    Demand_Side_Bypass_Pipe: str
    Fluid_Type: str
    Loop_Design_Delta_Temperature: str
    Load_Distribution_Scheme: str

class HvactemplatePlantTowerType(TypedDict, total=False):
    """"dict for HvactemplatePlantTower"""
    Name: str
    Tower_Type: str
    High_Speed_Nominal_Capacity: str
    High_Speed_Fan_Power: str
    Low_Speed_Nominal_Capacity: str
    Low_Speed_Fan_Power: str
    Free_Convection_Capacity: str
    Priority: str
    Sizing_Factor: str
    Template_Plant_Loop_Type: str

class HvactemplatePlantTowerObjectreferenceType(TypedDict, total=False):
    """"dict for HvactemplatePlantTowerObjectreference"""
    Name: str
    Cooling_Tower_Object_Type: str
    Cooling_Tower_Name: str
    Priority: str
    Template_Plant_Loop_Type: str

class HvactemplateSystemConstantvolumeType(TypedDict, total=False):
    """"dict for HvactemplateSystemConstantvolume"""
    Name: str
    System_Availability_Schedule_Name: str
    Supply_Fan_Maximum_Flow_Rate: str
    Supply_Fan_Total_Efficiency: str
    Supply_Fan_Delta_Pressure: str
    Supply_Fan_Motor_Efficiency: str
    Supply_Fan_Motor_in_Air_Stream_Fraction: str
    Supply_Fan_Placement: str
    Cooling_Coil_Type: str
    Cooling_Coil_Availability_Schedule_Name: str
    Cooling_Coil_Setpoint_Control_Type: str
    Cooling_Coil_Control_Zone_name: str
    Cooling_Coil_Design_Setpoint_Temperature: str
    Cooling_Coil_Setpoint_Schedule_Name: str
    Cooling_Coil_Setpoint_at_Outdoor_DryBulb_Low: str
    Cooling_Coil_Reset_Outdoor_DryBulb_Low: str
    Cooling_Coil_Setpoint_at_Outdoor_DryBulb_High: str
    Cooling_Coil_Reset_Outdoor_DryBulb_High: str
    Heating_Coil_Type: str
    Heating_Coil_Availability_Schedule_Name: str
    Heating_Coil_Setpoint_Control_Type: str
    Heating_Coil_Control_Zone_name: str
    Heating_Coil_Design_Setpoint: str
    Heating_Coil_Setpoint_Schedule_Name: str
    Heating_Coil_Setpoint_at_Outdoor_DryBulb_Low: str
    Heating_Coil_Reset_Outdoor_DryBulb_Low: str
    Heating_Coil_Setpoint_at_Outdoor_DryBulb_High: str
    Heating_Coil_Reset_Outdoor_DryBulb_High: str
    Heating_Coil_Capacity: str
    Gas_Heating_Coil_Efficiency: str
    Gas_Heating_Coil_Parasitic_Electric_Load: str
    Preheat_Coil_Type: str
    Preheat_Coil_Availability_Schedule_Name: str
    Preheat_Coil_Design_Setpoint: str
    Preheat_Coil_Setpoint_Schedule_Name: str
    Gas_Preheat_Coil_Efficiency: str
    Gas_Preheat_Coil_Parasitic_Electric_Load: str
    Maximum_Outdoor_Air_Flow_Rate: str
    Minimum_Outdoor_Air_Flow_Rate: str
    Minimum_Outdoor_Air_Schedule_Name: str
    Economizer_Type: str
    Economizer_Upper_Temperature_Limit: str
    Economizer_Lower_Temperature_Limit: str
    Economizer_Upper_Enthalpy_Limit: str
    Economizer_Maximum_Limit_Dewpoint_Temperature: str
    Supply_Plenum_Name: str
    Return_Plenum_Name: str
    Night_Cycle_Control: str
    Night_Cycle_Control_Zone_Name: str
    Heat_Recovery_Type: str
    Sensible_Heat_Recovery_Effectiveness: str
    Latent_Heat_Recovery_Effectiveness: str
    Heat_Recovery_Heat_Exchanger_Type: str
    Heat_Recovery_Frost_Control_Type: str
    Dehumidification_Control_Type: str
    Dehumidification_Control_Zone_Name: str
    Dehumidification_Relative_Humidity_Setpoint: str
    Dehumidification_Relative_Humidity_Setpoint_Schedule_Name: str
    Humidifier_Type: str
    Humidifier_Availability_Schedule_Name: str
    Humidifier_Rated_Capacity: str
    Humidifier_Rated_Electric_Power: str
    Humidifier_Control_Zone_Name: str
    Humidifier_Relative_Humidity_Setpoint: str
    Humidifier_Relative_Humidity_Setpoint_Schedule_Name: str
    Return_Fan: str
    Return_Fan_Total_Efficiency: str
    Return_Fan_Delta_Pressure: str
    Return_Fan_Motor_Efficiency: str
    Return_Fan_Motor_in_Air_Stream_Fraction: str

class HvactemplateSystemDedicatedoutdoorairType(TypedDict, total=False):
    """"dict for HvactemplateSystemDedicatedoutdoorair"""
    Name: str
    System_Availability_Schedule_Name: str
    Air_Outlet_Type: str
    Supply_Fan_Flow_Rate: str
    Supply_Fan_Total_Efficiency: str
    Supply_Fan_Delta_Pressure: str
    Supply_Fan_Motor_Efficiency: str
    Supply_Fan_Motor_in_Air_Stream_Fraction: str
    Supply_Fan_Placement: str
    Cooling_Coil_Type: str
    Cooling_Coil_Availability_Schedule_Name: str
    Cooling_Coil_Setpoint_Control_Type: str
    Cooling_Coil_Design_Setpoint: str
    Cooling_Coil_Setpoint_Schedule_Name: str
    Cooling_Coil_Setpoint_at_Outdoor_DryBulb_Low: str
    Cooling_Coil_Reset_Outdoor_DryBulb_Low: str
    Cooling_Coil_Setpoint_at_Outdoor_DryBulb_High: str
    Cooling_Coil_Reset_Outdoor_DryBulb_High: str
    DX_Cooling_Coil_Gross_Rated_Total_Capacity: str
    DX_Cooling_Coil_Gross_Rated_Sensible_Heat_Ratio: str
    DX_Cooling_Coil_Gross_Rated_COP: str
    Heating_Coil_Type: str
    Heating_Coil_Availability_Schedule_Name: str
    Heating_Coil_Setpoint_Control_Type: str
    Heating_Coil_Design_Setpoint: str
    Heating_Coil_Setpoint_Schedule_Name: str
    Heating_Coil_Setpoint_at_Outdoor_DryBulb_Low: str
    Heating_Coil_Reset_Outdoor_DryBulb_Low: str
    Heating_Coil_Setpoint_at_Outdoor_DryBulb_High: str
    Heating_Coil_Reset_Outdoor_DryBulb_High: str
    Gas_Heating_Coil_Efficiency: str
    Gas_Heating_Coil_Parasitic_Electric_Load: str
    Heat_Recovery_Type: str
    Heat_Recovery_Sensible_Effectiveness: str
    Heat_Recovery_Latent_Effectiveness: str
    Heat_Recovery_Heat_Exchanger_Type: str
    Heat_Recovery_Frost_Control_Type: str
    Dehumidification_Control_Type: str
    Dehumidification_Setpoint: str
    Humidifier_Type: str
    Humidifier_Availability_Schedule_Name: str
    Humidifier_Rated_Capacity: str
    Humidifier_Rated_Electric_Power: str
    Humidifier_Constant_Setpoint: str
    Dehumidification_Setpoint_Schedule_Name: str
    Humidifier_Setpoint_Schedule_Name: str

class HvactemplateSystemDualductType(TypedDict, total=False):
    """"dict for HvactemplateSystemDualduct"""
    Name: str
    System_Availability_Schedule_Name: str
    System_Configuration_Type: str
    Main_Supply_Fan_Maximum_Flow_Rate: str
    Main_Supply_Fan_Minimum_Flow_Fraction: str
    Main_Supply_Fan_Total_Efficiency: str
    Main_Supply_Fan_Delta_Pressure: str
    Main_Supply_Fan_Motor_Efficiency: str
    Main_Supply_Fan_Motor_in_Air_Stream_Fraction: str
    Main_Supply_Fan_PartLoad_Power_Coefficients: str
    Cold_Duct_Supply_Fan_Maximum_Flow_Rate: str
    Cold_Duct_Supply_Fan_Minimum_Flow_Fraction: str
    Cold_Duct_Supply_Fan_Total_Efficiency: str
    Cold_Duct_Supply_Fan_Delta_Pressure: str
    Cold_Duct_Supply_Fan_Motor_Efficiency: str
    Cold_Duct_Supply_Fan_Motor_in_Air_Stream_Fraction: str
    Cold_Duct_Supply_Fan_PartLoad_Power_Coefficients: str
    Cold_Duct_Supply_Fan_Placement: str
    Hot_Duct_Supply_Fan_Maximum_Flow_Rate: str
    Hot_Duct_Supply_Fan_Minimum_Flow_Fraction: str
    Hot_Duct_Supply_Fan_Total_Efficiency: str
    Hot_Duct_Supply_Fan_Delta_Pressure: str
    Hot_Duct_Supply_Fan_Motor_Efficiency: str
    Hot_Duct_Supply_Fan_Motor_in_Air_Stream_Fraction: str
    Hot_Duct_Supply_Fan_PartLoad_Power_Coefficients: str
    Hot_Duct_Supply_Fan_Placement: str
    Cooling_Coil_Type: str
    Cooling_Coil_Availability_Schedule_Name: str
    Cooling_Coil_Setpoint_Control_Type: str
    Cooling_Coil_Design_Setpoint_Temperature: str
    Cooling_Coil_Setpoint_Schedule_Name: str
    Cooling_Coil_Setpoint_at_Outdoor_DryBulb_Low: str
    Cooling_Coil_Reset_Outdoor_DryBulb_Low: str
    Cooling_Coil_Setpoint_at_Outdoor_DryBulb_High: str
    Cooling_Coil_Reset_Outdoor_DryBulb_High: str
    Heating_Coil_Type: str
    Heating_Coil_Availability_Schedule_Name: str
    Heating_Coil_Setpoint_Control_Type: str
    Heating_Coil_Design_Setpoint: str
    Heating_Coil_Setpoint_Schedule_Name: str
    Heating_Coil_Setpoint_at_Outdoor_DryBulb_Low: str
    Heating_Coil_Reset_Outdoor_DryBulb_Low: str
    Heating_Coil_Setpoint_at_Outdoor_DryBulb_High: str
    Heating_Coil_Reset_Outdoor_DryBulb_High: str
    Heating_Coil_Capacity: str
    Gas_Heating_Coil_Efficiency: str
    Gas_Heating_Coil_Parasitic_Electric_Load: str
    Preheat_Coil_Type: str
    Preheat_Coil_Availability_Schedule_Name: str
    Preheat_Coil_Design_Setpoint: str
    Preheat_Coil_Setpoint_Schedule_Name: str
    Gas_Preheat_Coil_Efficiency: str
    Gas_Preheat_Coil_Parasitic_Electric_Load: str
    Maximum_Outdoor_Air_Flow_Rate: str
    Minimum_Outdoor_Air_Flow_Rate: str
    Minimum_Outdoor_Air_Control_Type: str
    Minimum_Outdoor_Air_Schedule_Name: str
    Economizer_Type: str
    Economizer_Lockout: str
    Economizer_Upper_Temperature_Limit: str
    Economizer_Lower_Temperature_Limit: str
    Economizer_Upper_Enthalpy_Limit: str
    Economizer_Maximum_Limit_Dewpoint_Temperature: str
    Cold_Supply_Plenum_Name: str
    Hot_Supply_Plenum_Name: str
    Return_Plenum_Name: str
    Night_Cycle_Control: str
    Night_Cycle_Control_Zone_Name: str
    Heat_Recovery_Type: str
    Sensible_Heat_Recovery_Effectiveness: str
    Latent_Heat_Recovery_Effectiveness: str
    Heat_Recovery_Heat_Exchanger_Type: str
    Heat_Recovery_Frost_Control_Type: str
    Dehumidification_Control_Type: str
    Dehumidification_Control_Zone_Name: str
    Dehumidification_Relative_Humidity_Setpoint: str
    Dehumidification_Relative_Humidity_Setpoint_Schedule_Name: str
    Humidifier_Type: str
    Humidifier_Availability_Schedule_Name: str
    Humidifier_Rated_Capacity: str
    Humidifier_Rated_Electric_Power: str
    Humidifier_Control_Zone_Name: str
    Humidifier_Relative_Humidity_Setpoint: str
    Humidifier_Relative_Humidity_Setpoint_Schedule_Name: str
    Sizing_Option: str
    Return_Fan: str
    Return_Fan_Total_Efficiency: str
    Return_Fan_Delta_Pressure: str
    Return_Fan_Motor_Efficiency: str
    Return_Fan_Motor_in_Air_Stream_Fraction: str
    Return_Fan_PartLoad_Power_Coefficients: str

class HvactemplateSystemPackagedvavType(TypedDict, total=False):
    """"dict for HvactemplateSystemPackagedvav"""
    Name: str
    System_Availability_Schedule_Name: str
    Supply_Fan_Maximum_Flow_Rate: str
    Supply_Fan_Minimum_Flow_Rate: str
    Supply_Fan_Placement: str
    Supply_Fan_Total_Efficiency: str
    Supply_Fan_Delta_Pressure: str
    Supply_Fan_Motor_Efficiency: str
    Supply_Fan_Motor_in_Air_Stream_Fraction: str
    Cooling_Coil_Type: str
    Cooling_Coil_Availability_Schedule_Name: str
    Cooling_Coil_Setpoint_Schedule_Name: str
    Cooling_Coil_Design_Setpoint: str
    Cooling_Coil_Gross_Rated_Total_Capacity: str
    Cooling_Coil_Gross_Rated_Sensible_Heat_Ratio: str
    Cooling_Coil_Gross_Rated_COP: str
    Heating_Coil_Type: str
    Heating_Coil_Availability_Schedule_Name: str
    Heating_Coil_Setpoint_Schedule_Name: str
    Heating_Coil_Design_Setpoint: str
    Heating_Coil_Capacity: str
    Gas_Heating_Coil_Efficiency: str
    Gas_Heating_Coil_Parasitic_Electric_Load: str
    Maximum_Outdoor_Air_Flow_Rate: str
    Minimum_Outdoor_Air_Flow_Rate: str
    Minimum_Outdoor_Air_Control_Type: str
    Minimum_Outdoor_Air_Schedule_Name: str
    Economizer_Type: str
    Economizer_Lockout: str
    Economizer_Maximum_Limit_DryBulb_Temperature: str
    Economizer_Maximum_Limit_Enthalpy: str
    Economizer_Maximum_Limit_Dewpoint_Temperature: str
    Economizer_Minimum_Limit_DryBulb_Temperature: str
    Supply_Plenum_Name: str
    Return_Plenum_Name: str
    Supply_Fan_PartLoad_Power_Coefficients: str
    Night_Cycle_Control: str
    Night_Cycle_Control_Zone_Name: str
    Heat_Recovery_Type: str
    Sensible_Heat_Recovery_Effectiveness: str
    Latent_Heat_Recovery_Effectiveness: str
    Cooling_Coil_Setpoint_Reset_Type: str
    Heating_Coil_Setpoint_Reset_Type: str
    Dehumidification_Control_Type: str
    Dehumidification_Control_Zone_Name: str
    Dehumidification_Setpoint: str
    Humidifier_Type: str
    Humidifier_Availability_Schedule_Name: str
    Humidifier_Rated_Capacity: str
    Humidifier_Rated_Electric_Power: str
    Humidifier_Control_Zone_Name: str
    Humidifier_Setpoint: str
    Sizing_Option: str
    Return_Fan: str
    Return_Fan_Total_Efficiency: str
    Return_Fan_Delta_Pressure: str
    Return_Fan_Motor_Efficiency: str
    Return_Fan_Motor_in_Air_Stream_Fraction: str
    Return_Fan_PartLoad_Power_Coefficients: str

class HvactemplateSystemUnitaryType(TypedDict, total=False):
    """"dict for HvactemplateSystemUnitary"""
    Name: str
    System_Availability_Schedule_Name: str
    Control_Zone_or_Thermostat_Location_Name: str
    Supply_Fan_Maximum_Flow_Rate: str
    Supply_Fan_Operating_Mode_Schedule_Name: str
    Supply_Fan_Total_Efficiency: str
    Supply_Fan_Delta_Pressure: str
    Supply_Fan_Motor_Efficiency: str
    Supply_Fan_Motor_in_Air_Stream_Fraction: str
    Cooling_Coil_Type: str
    Cooling_Coil_Availability_Schedule_Name: str
    Cooling_Design_Supply_Air_Temperature: str
    Cooling_Coil_Gross_Rated_Total_Capacity: str
    Cooling_Coil_Gross_Rated_Sensible_Heat_Ratio: str
    Cooling_Coil_Gross_Rated_COP: str
    Heating_Coil_Type: str
    Heating_Coil_Availability_Schedule_Name: str
    Heating_Design_Supply_Air_Temperature: str
    Heating_Coil_Capacity: str
    Gas_Heating_Coil_Efficiency: str
    Gas_Heating_Coil_Parasitic_Electric_Load: str
    Maximum_Outdoor_Air_Flow_Rate: str
    Minimum_Outdoor_Air_Flow_Rate: str
    Minimum_Outdoor_Air_Schedule_Name: str
    Economizer_Type: str
    Economizer_Lockout: str
    Economizer_Upper_Temperature_Limit: str
    Economizer_Lower_Temperature_Limit: str
    Economizer_Upper_Enthalpy_Limit: str
    Economizer_Maximum_Limit_Dewpoint_Temperature: str
    Supply_Plenum_Name: str
    Return_Plenum_Name: str
    Supply_Fan_Placement: str
    Night_Cycle_Control: str
    Night_Cycle_Control_Zone_Name: str
    Heat_Recovery_Type: str
    Sensible_Heat_Recovery_Effectiveness: str
    Latent_Heat_Recovery_Effectiveness: str
    Dehumidification_Control_Type: str
    Dehumidification_Setpoint: str
    Humidifier_Type: str
    Humidifier_Availability_Schedule_Name: str
    Humidifier_Rated_Capacity: str
    Humidifier_Rated_Electric_Power: str
    Humidifier_Control_Zone_Name: str
    Humidifier_Setpoint: str
    Return_Fan: str
    Return_Fan_Total_Efficiency: str
    Return_Fan_Delta_Pressure: str
    Return_Fan_Motor_Efficiency: str
    Return_Fan_Motor_in_Air_Stream_Fraction: str

class HvactemplateSystemUnitaryheatpumpAirtoairType(TypedDict, total=False):
    """"dict for HvactemplateSystemUnitaryheatpumpAirtoair"""
    Name: str
    System_Availability_Schedule_Name: str
    Control_Zone_or_Thermostat_Location_Name: str
    Cooling_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate: str
    No_Load_Supply_Air_Flow_Rate: str
    Supply_Fan_Operating_Mode_Schedule_Name: str
    Supply_Fan_Placement: str
    Supply_Fan_Total_Efficiency: str
    Supply_Fan_Delta_Pressure: str
    Supply_Fan_Motor_Efficiency: str
    Supply_Fan_Motor_in_Air_Stream_Fraction: str
    Cooling_Coil_Type: str
    Cooling_Coil_Availability_Schedule_Name: str
    Cooling_Design_Supply_Air_Temperature: str
    Cooling_Coil_Gross_Rated_Total_Capacity: str
    Cooling_Coil_Gross_Rated_Sensible_Heat_Ratio: str
    Cooling_Coil_Gross_Rated_COP: str
    Heat_Pump_Heating_Coil_Type: str
    Heat_Pump_Heating_Coil_Availability_Schedule_Name: str
    Heating_Design_Supply_Air_Temperature: str
    Heat_Pump_Heating_Coil_Gross_Rated_Capacity: str
    Heat_Pump_Heating_Coil_Rated_COP: str
    Heat_Pump_Heating_Minimum_Outdoor_DryBulb_Temperature: str
    Heat_Pump_Defrost_Maximum_Outdoor_DryBulb_Temperature: str
    Heat_Pump_Defrost_Strategy: str
    Heat_Pump_Defrost_Control: str
    Heat_Pump_Defrost_Time_Period_Fraction: str
    Supplemental_Heating_Coil_Type: str
    Supplemental_Heating_Coil_Availability_Schedule_Name: str
    Supplemental_Heating_Coil_Capacity: str
    Supplemental_Heating_Coil_Maximum_Outdoor_DryBulb_Temperature: str
    Supplemental_Gas_Heating_Coil_Efficiency: str
    Supplemental_Gas_Heating_Coil_Parasitic_Electric_Load: str
    Maximum_Outdoor_Air_Flow_Rate: str
    Minimum_Outdoor_Air_Flow_Rate: str
    Minimum_Outdoor_Air_Schedule_Name: str
    Economizer_Type: str
    Economizer_Lockout: str
    Economizer_Maximum_Limit_DryBulb_Temperature: str
    Economizer_Maximum_Limit_Enthalpy: str
    Economizer_Maximum_Limit_Dewpoint_Temperature: str
    Economizer_Minimum_Limit_DryBulb_Temperature: str
    Supply_Plenum_Name: str
    Return_Plenum_Name: str
    Night_Cycle_Control: str
    Night_Cycle_Control_Zone_Name: str
    Heat_Recovery_Type: str
    Sensible_Heat_Recovery_Effectiveness: str
    Latent_Heat_Recovery_Effectiveness: str
    Humidifier_Type: str
    Humidifier_Availability_Schedule_Name: str
    Humidifier_Rated_Capacity: str
    Humidifier_Rated_Electric_Power: str
    Humidifier_Control_Zone_Name: str
    Humidifier_Setpoint: str
    Return_Fan: str
    Return_Fan_Total_Efficiency: str
    Return_Fan_Delta_Pressure: str
    Return_Fan_Motor_Efficiency: str
    Return_Fan_Motor_in_Air_Stream_Fraction: str

class HvactemplateSystemUnitarysystemType(TypedDict, total=False):
    """"dict for HvactemplateSystemUnitarysystem"""
    Name: str
    System_Availability_Schedule_Name: str
    Control_Type: str
    Control_Zone_or_Thermostat_Location_Name: str
    Cooling_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate: str
    No_Load_Supply_Air_Flow_Rate: str
    Supply_Fan_Operating_Mode_Schedule_Name: str
    Supply_Fan_Placement: str
    Supply_Fan_Total_Efficiency: str
    Supply_Fan_Delta_Pressure: str
    Supply_Fan_Motor_Efficiency: str
    Supply_Fan_Motor_in_Air_Stream_Fraction: str
    Cooling_Coil_Type: str
    Number_of_Speeds_for_Cooling: str
    Cooling_Coil_Availability_Schedule_Name: str
    Cooling_Design_Supply_Air_Temperature: str
    DX_Cooling_Coil_Gross_Rated_Total_Capacity: str
    DX_Cooling_Coil_Gross_Rated_Sensible_Heat_Ratio: str
    DX_Cooling_Coil_Gross_Rated_COP: str
    Heating_Coil_Type: str
    Number_of_Speeds_or_Stages_for_Heating: str
    Heating_Coil_Availability_Schedule_Name: str
    Heating_Design_Supply_Air_Temperature: str
    Heating_Coil_Gross_Rated_Capacity: str
    Gas_Heating_Coil_Efficiency: str
    Gas_Heating_Coil_Parasitic_Electric_Load: str
    Heat_Pump_Heating_Coil_Gross_Rated_COP: str
    Heat_Pump_Heating_Minimum_Outdoor_DryBulb_Temperature: str
    Heat_Pump_Defrost_Maximum_Outdoor_DryBulb_Temperature: str
    Heat_Pump_Defrost_Strategy: str
    Heat_Pump_Defrost_Control: str
    Heat_Pump_Defrost_Time_Period_Fraction: str
    Supplemental_Heating_or_Reheat_Coil_Type: str
    Supplemental_Heating_or_Reheat_Coil_Availability_Schedule_Name: str
    Supplemental_Heating_or_Reheat_Coil_Capacity: str
    Supplemental_Heating_or_Reheat_Coil_Maximum_Outdoor_DryBulb_Temperature: str
    Supplemental_Gas_Heating_or_Reheat_Coil_Efficiency: str
    Supplemental_Gas_Heating_or_Reheat_Coil_Parasitic_Electric_Load: str
    Maximum_Outdoor_Air_Flow_Rate: str
    Minimum_Outdoor_Air_Flow_Rate: str
    Minimum_Outdoor_Air_Schedule_Name: str
    Economizer_Type: str
    Economizer_Lockout: str
    Economizer_Maximum_Limit_DryBulb_Temperature: str
    Economizer_Maximum_Limit_Enthalpy: str
    Economizer_Maximum_Limit_Dewpoint_Temperature: str
    Economizer_Minimum_Limit_DryBulb_Temperature: str
    Supply_Plenum_Name: str
    Return_Plenum_Name: str
    Heat_Recovery_Type: str
    Sensible_Heat_Recovery_Effectiveness: str
    Latent_Heat_Recovery_Effectiveness: str
    Heat_Recovery_Heat_Exchanger_Type: str
    Heat_Recovery_Frost_Control_Type: str
    Dehumidification_Control_Type: str
    Dehumidification_Relative_Humidity_Setpoint: str
    Dehumidification_Relative_Humidity_Setpoint_Schedule_Name: str
    Humidifier_Type: str
    Humidifier_Availability_Schedule_Name: str
    Humidifier_Rated_Capacity: str
    Humidifier_Rated_Electric_Power: str
    Humidifier_Control_Zone_Name: str
    Humidifier_Relative_Humidity_Setpoint: str
    Humidifier_Relative_Humidity_Setpoint_Schedule_Name: str
    Sizing_Option: str
    Return_Fan: str
    Return_Fan_Total_Efficiency: str
    Return_Fan_Delta_Pressure: str
    Return_Fan_Motor_Efficiency: str
    Return_Fan_Motor_in_Air_Stream_Fraction: str

class HvactemplateSystemVavType(TypedDict, total=False):
    """"dict for HvactemplateSystemVav"""
    Name: str
    System_Availability_Schedule_Name: str
    Supply_Fan_Maximum_Flow_Rate: str
    Supply_Fan_Minimum_Flow_Rate: str
    Supply_Fan_Total_Efficiency: str
    Supply_Fan_Delta_Pressure: str
    Supply_Fan_Motor_Efficiency: str
    Supply_Fan_Motor_in_Air_Stream_Fraction: str
    Cooling_Coil_Type: str
    Cooling_Coil_Availability_Schedule_Name: str
    Cooling_Coil_Setpoint_Schedule_Name: str
    Cooling_Coil_Design_Setpoint: str
    Heating_Coil_Type: str
    Heating_Coil_Availability_Schedule_Name: str
    Heating_Coil_Setpoint_Schedule_Name: str
    Heating_Coil_Design_Setpoint: str
    Gas_Heating_Coil_Efficiency: str
    Gas_Heating_Coil_Parasitic_Electric_Load: str
    Preheat_Coil_Type: str
    Preheat_Coil_Availability_Schedule_Name: str
    Preheat_Coil_Setpoint_Schedule_Name: str
    Preheat_Coil_Design_Setpoint: str
    Gas_Preheat_Coil_Efficiency: str
    Gas_Preheat_Coil_Parasitic_Electric_Load: str
    Maximum_Outdoor_Air_Flow_Rate: str
    Minimum_Outdoor_Air_Flow_Rate: str
    Minimum_Outdoor_Air_Control_Type: str
    Minimum_Outdoor_Air_Schedule_Name: str
    Economizer_Type: str
    Economizer_Lockout: str
    Economizer_Upper_Temperature_Limit: str
    Economizer_Lower_Temperature_Limit: str
    Economizer_Upper_Enthalpy_Limit: str
    Economizer_Maximum_Limit_Dewpoint_Temperature: str
    Supply_Plenum_Name: str
    Return_Plenum_Name: str
    Supply_Fan_Placement: str
    Supply_Fan_PartLoad_Power_Coefficients: str
    Night_Cycle_Control: str
    Night_Cycle_Control_Zone_Name: str
    Heat_Recovery_Type: str
    Sensible_Heat_Recovery_Effectiveness: str
    Latent_Heat_Recovery_Effectiveness: str
    Cooling_Coil_Setpoint_Reset_Type: str
    Heating_Coil_Setpoint_Reset_Type: str
    Dehumidification_Control_Type: str
    Dehumidification_Control_Zone_Name: str
    Dehumidification_Setpoint: str
    Humidifier_Type: str
    Humidifier_Availability_Schedule_Name: str
    Humidifier_Rated_Capacity: str
    Humidifier_Rated_Electric_Power: str
    Humidifier_Control_Zone_Name: str
    Humidifier_Setpoint: str
    Sizing_Option: str
    Return_Fan: str
    Return_Fan_Total_Efficiency: str
    Return_Fan_Delta_Pressure: str
    Return_Fan_Motor_Efficiency: str
    Return_Fan_Motor_in_Air_Stream_Fraction: str
    Return_Fan_PartLoad_Power_Coefficients: str

class HvactemplateSystemVrfType(TypedDict, total=False):
    """"dict for HvactemplateSystemVrf"""
    Name: str
    System_Availability_Schedule_Name: str
    Gross_Rated_Total_Cooling_Capacity: str
    Gross_Rated_Cooling_COP: str
    Minimum_Outdoor_Temperature_in_Cooling_Mode: str
    Maximum_Outdoor_Temperature_in_Cooling_Mode: str
    Gross_Rated_Heating_Capacity: str
    Rated_Heating_Capacity_Sizing_Ratio: str
    Gross_Rated_Heating_COP: str
    Minimum_Outdoor_Temperature_in_Heating_Mode: str
    Maximum_Outdoor_Temperature_in_Heating_Mode: str
    Minimum_Heat_Pump_PartLoad_Ratio: str
    Zone_Name_for_Master_Thermostat_Location: str
    Master_Thermostat_Priority_Control_Type: str
    Thermostat_Priority_Schedule_Name: str
    Heat_Pump_Waste_Heat_Recovery: str
    Equivalent_Piping_Length_used_for_Piping_Correction_Factor_in_Cooling_Mode: str
    Vertical_Height_used_for_Piping_Correction_Factor: str
    Equivalent_Piping_Length_used_for_Piping_Correction_Factor_in_Heating_Mode: str
    Crankcase_Heater_Power_per_Compressor: str
    Number_of_Compressors: str
    Ratio_of_Compressor_Size_to_Total_Compressor_Capacity: str
    Maximum_Outdoor_Drybulb_Temperature_for_Crankcase_Heater: str
    Defrost_Strategy: str
    Defrost_Control: str
    Defrost_Time_Period_Fraction: str
    Resistive_Defrost_Heater_Capacity: str
    Maximum_Outdoor_Drybulb_Temperature_for_Defrost_Operation: str
    Condenser_Type: str
    Water_Condenser_Volume_Flow_Rate: str
    Evaporative_Condenser_Effectiveness: str
    Evaporative_Condenser_Air_Flow_Rate: str
    Evaporative_Condenser_Pump_Rated_Power_Consumption: str
    Basin_Heater_Capacity: str
    Basin_Heater_Setpoint_Temperature: str
    Basin_Heater_Operating_Schedule_Name: str
    Fuel_Type: str
    Minimum_Outdoor_Temperature_in_Heat_Recovery_Mode: str
    Maximum_Outdoor_Temperature_in_Heat_Recovery_Mode: str

class HvactemplateThermostatType(TypedDict, total=False):
    """"dict for HvactemplateThermostat"""
    Name: str
    Heating_Setpoint_Schedule_Name: str
    Constant_Heating_Setpoint: str
    Cooling_Setpoint_Schedule_Name: str
    Constant_Cooling_Setpoint: str

class HvactemplateZoneBaseboardheatType(TypedDict, total=False):
    """"dict for HvactemplateZoneBaseboardheat"""
    Zone_Name: str
    Template_Thermostat_Name: str
    Zone_Heating_Sizing_Factor: str
    Baseboard_Heating_Type: str
    Baseboard_Heating_Availability_Schedule_Name: str
    Baseboard_Heating_Capacity: str
    Dedicated_Outdoor_Air_System_Name: str
    Outdoor_Air_Method: str
    Outdoor_Air_Flow_Rate_per_Person: str
    Outdoor_Air_Flow_Rate_per_Zone_Floor_Area: str
    Outdoor_Air_Flow_Rate_per_Zone: str
    Design_Specification_Outdoor_Air_Object_name: str
    Design_Specification_Zone_Air_Distribution_Object_Name: str

class HvactemplateZoneConstantvolumeType(TypedDict, total=False):
    """"dict for HvactemplateZoneConstantvolume"""
    Zone_Name: str
    Template_Constant_Volume_System_Name: str
    Template_Thermostat_Name: str
    Supply_Air_Maximum_Flow_Rate: str
    Zone_Heating_Sizing_Factor: str
    Zone_Cooling_Sizing_Factor: str
    Outdoor_Air_Method: str
    Outdoor_Air_Flow_Rate_per_Person: str
    Outdoor_Air_Flow_Rate_per_Zone_Floor_Area: str
    Outdoor_Air_Flow_Rate_per_Zone: str
    Design_Specification_Outdoor_Air_Object_name: str
    Design_Specification_Zone_Air_Distribution_Object_Name: str
    Reheat_Coil_Type: str
    Reheat_Coil_Availability_Schedule_Name: str
    Maximum_Reheat_Air_Temperature: str
    Supply_Plenum_Name: str
    Return_Plenum_Name: str
    Baseboard_Heating_Type: str
    Baseboard_Heating_Availability_Schedule_Name: str
    Baseboard_Heating_Capacity: str
    Zone_Cooling_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Cooling_Design_Supply_Air_Temperature: str
    Zone_Cooling_Design_Supply_Air_Temperature_Difference: str
    Zone_Heating_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Heating_Design_Supply_Air_Temperature: str
    Zone_Heating_Design_Supply_Air_Temperature_Difference: str

class HvactemplateZoneDualductType(TypedDict, total=False):
    """"dict for HvactemplateZoneDualduct"""
    Zone_Name: str
    Template_Dual_Duct_System_Name: str
    Template_Thermostat_Name: str
    Supply_Air_Maximum_Flow_Rate: str
    Zone_Heating_Sizing_Factor: str
    Zone_Cooling_Sizing_Factor: str
    Zone_Minimum_Air_Flow_Fraction: str
    Outdoor_Air_Method: str
    Outdoor_Air_Flow_Rate_per_Person: str
    Outdoor_Air_Flow_Rate_per_Zone_Floor_Area: str
    Outdoor_Air_Flow_Rate_per_Zone: str
    Design_Specification_Outdoor_Air_Object_Name_for_Sizing: str
    Design_Specification_Zone_Air_Distribution_Object_Name: str
    Design_Specification_Outdoor_Air_Object_Name_for_Control: str
    Cold_Supply_Plenum_Name: str
    Hot_Supply_Plenum_Name: str
    Return_Plenum_Name: str
    Baseboard_Heating_Type: str
    Baseboard_Heating_Availability_Schedule_Name: str
    Baseboard_Heating_Capacity: str
    Zone_Cooling_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Cooling_Design_Supply_Air_Temperature: str
    Zone_Cooling_Design_Supply_Air_Temperature_Difference: str
    Zone_Heating_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Heating_Design_Supply_Air_Temperature: str
    Zone_Heating_Design_Supply_Air_Temperature_Difference: str

class HvactemplateZoneFancoilType(TypedDict, total=False):
    """"dict for HvactemplateZoneFancoil"""
    Zone_Name: str
    Template_Thermostat_Name: str
    Supply_Air_Maximum_Flow_Rate: str
    Zone_Heating_Sizing_Factor: str
    Zone_Cooling_Sizing_Factor: str
    Outdoor_Air_Method: str
    Outdoor_Air_Flow_Rate_per_Person: str
    Outdoor_Air_Flow_Rate_per_Zone_Floor_Area: str
    Outdoor_Air_Flow_Rate_per_Zone: str
    System_Availability_Schedule_Name: str
    Supply_Fan_Total_Efficiency: str
    Supply_Fan_Delta_Pressure: str
    Supply_Fan_Motor_Efficiency: str
    Supply_Fan_Motor_in_Air_Stream_Fraction: str
    Cooling_Coil_Type: str
    Cooling_Coil_Availability_Schedule_Name: str
    Cooling_Coil_Design_Setpoint: str
    Heating_Coil_Type: str
    Heating_Coil_Availability_Schedule_Name: str
    Heating_Coil_Design_Setpoint: str
    Dedicated_Outdoor_Air_System_Name: str
    Zone_Cooling_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Cooling_Design_Supply_Air_Temperature_Difference: str
    Zone_Heating_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Heating_Design_Supply_Air_Temperature_Difference: str
    Design_Specification_Outdoor_Air_Object_Name: str
    Design_Specification_Zone_Air_Distribution_Object_Name: str
    Capacity_Control_Method: str
    Low_Speed_Supply_Air_Flow_Ratio: str
    Medium_Speed_Supply_Air_Flow_Ratio: str
    Outdoor_Air_Schedule_Name: str
    Baseboard_Heating_Type: str
    Baseboard_Heating_Availability_Schedule_Name: str
    Baseboard_Heating_Capacity: str

class HvactemplateZoneIdealloadsairsystemType(TypedDict, total=False):
    """"dict for HvactemplateZoneIdealloadsairsystem"""
    Zone_Name: str
    Template_Thermostat_Name: str
    System_Availability_Schedule_Name: str
    Maximum_Heating_Supply_Air_Temperature: str
    Minimum_Cooling_Supply_Air_Temperature: str
    Maximum_Heating_Supply_Air_Humidity_Ratio: str
    Minimum_Cooling_Supply_Air_Humidity_Ratio: str
    Heating_Limit: str
    Maximum_Heating_Air_Flow_Rate: str
    Maximum_Sensible_Heating_Capacity: str
    Cooling_Limit: str
    Maximum_Cooling_Air_Flow_Rate: str
    Maximum_Total_Cooling_Capacity: str
    Heating_Availability_Schedule_Name: str
    Cooling_Availability_Schedule_Name: str
    Dehumidification_Control_Type: str
    Cooling_Sensible_Heat_Ratio: str
    Dehumidification_Setpoint: str
    Humidification_Control_Type: str
    Humidification_Setpoint: str
    Outdoor_Air_Method: str
    Outdoor_Air_Flow_Rate_per_Person: str
    Outdoor_Air_Flow_Rate_per_Zone_Floor_Area: str
    Outdoor_Air_Flow_Rate_per_Zone: str
    Design_Specification_Outdoor_Air_Object_Name: str
    Demand_Controlled_Ventilation_Type: str
    Outdoor_Air_Economizer_Type: str
    Heat_Recovery_Type: str
    Sensible_Heat_Recovery_Effectiveness: str
    Latent_Heat_Recovery_Effectiveness: str

class HvactemplateZonePtacType(TypedDict, total=False):
    """"dict for HvactemplateZonePtac"""
    Zone_Name: str
    Template_Thermostat_Name: str
    Cooling_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate: str
    No_Load_Supply_Air_Flow_Rate: str
    Zone_Heating_Sizing_Factor: str
    Zone_Cooling_Sizing_Factor: str
    Outdoor_Air_Method: str
    Outdoor_Air_Flow_Rate_per_Person: str
    Outdoor_Air_Flow_Rate_per_Zone_Floor_Area: str
    Outdoor_Air_Flow_Rate_per_Zone: str
    System_Availability_Schedule_Name: str
    Supply_Fan_Operating_Mode_Schedule_Name: str
    Supply_Fan_Placement: str
    Supply_Fan_Total_Efficiency: str
    Supply_Fan_Delta_Pressure: str
    Supply_Fan_Motor_Efficiency: str
    Cooling_Coil_Type: str
    Cooling_Coil_Availability_Schedule_Name: str
    Cooling_Coil_Gross_Rated_Total_Capacity: str
    Cooling_Coil_Gross_Rated_Sensible_Heat_Ratio: str
    Cooling_Coil_Gross_Rated_Cooling_COP: str
    Heating_Coil_Type: str
    Heating_Coil_Availability_Schedule_Name: str
    Heating_Coil_Capacity: str
    Gas_Heating_Coil_Efficiency: str
    Gas_Heating_Coil_Parasitic_Electric_Load: str
    Dedicated_Outdoor_Air_System_Name: str
    Zone_Cooling_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Cooling_Design_Supply_Air_Temperature: str
    Zone_Cooling_Design_Supply_Air_Temperature_Difference: str
    Zone_Heating_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Heating_Design_Supply_Air_Temperature: str
    Zone_Heating_Design_Supply_Air_Temperature_Difference: str
    Design_Specification_Outdoor_Air_Object_Name: str
    Design_Specification_Zone_Air_Distribution_Object_Name: str
    Baseboard_Heating_Type: str
    Baseboard_Heating_Availability_Schedule_Name: str
    Baseboard_Heating_Capacity: str
    Capacity_Control_Method: str

class HvactemplateZonePthpType(TypedDict, total=False):
    """"dict for HvactemplateZonePthp"""
    Zone_Name: str
    Template_Thermostat_Name: str
    Cooling_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate: str
    No_Load_Supply_Air_Flow_Rate: str
    Zone_Heating_Sizing_Factor: str
    Zone_Cooling_Sizing_Factor: str
    Outdoor_Air_Method: str
    Outdoor_Air_Flow_Rate_per_Person: str
    Outdoor_Air_Flow_Rate_per_Zone_Floor_Area: str
    Outdoor_Air_Flow_Rate_per_Zone: str
    System_Availability_Schedule_Name: str
    Supply_Fan_Operating_Mode_Schedule_Name: str
    Supply_Fan_Placement: str
    Supply_Fan_Total_Efficiency: str
    Supply_Fan_Delta_Pressure: str
    Supply_Fan_Motor_Efficiency: str
    Cooling_Coil_Type: str
    Cooling_Coil_Availability_Schedule_Name: str
    Cooling_Coil_Gross_Rated_Total_Capacity: str
    Cooling_Coil_Gross_Rated_Sensible_Heat_Ratio: str
    Cooling_Coil_Gross_Rated_COP: str
    Heat_Pump_Heating_Coil_Type: str
    Heat_Pump_Heating_Coil_Availability_Schedule_Name: str
    Heat_Pump_Heating_Coil_Gross_Rated_Capacity: str
    Heat_Pump_Heating_Coil_Gross_Rated_COP: str
    Heat_Pump_Heating_Minimum_Outdoor_DryBulb_Temperature: str
    Heat_Pump_Defrost_Maximum_Outdoor_DryBulb_Temperature: str
    Heat_Pump_Defrost_Strategy: str
    Heat_Pump_Defrost_Control: str
    Heat_Pump_Defrost_Time_Period_Fraction: str
    Supplemental_Heating_Coil_Type: str
    Supplemental_Heating_Coil_Availability_Schedule_Name: str
    Supplemental_Heating_Coil_Capacity: str
    Supplemental_Heating_Coil_Maximum_Outdoor_DryBulb_Temperature: str
    Supplemental_Gas_Heating_Coil_Efficiency: str
    Supplemental_Gas_Heating_Coil_Parasitic_Electric_Load: str
    Dedicated_Outdoor_Air_System_Name: str
    Zone_Cooling_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Cooling_Design_Supply_Air_Temperature: str
    Zone_Cooling_Design_Supply_Air_Temperature_Difference: str
    Zone_Heating_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Heating_Design_Supply_Air_Temperature: str
    Zone_Heating_Design_Supply_Air_Temperature_Difference: str
    Design_Specification_Outdoor_Air_Object_Name: str
    Design_Specification_Zone_Air_Distribution_Object_Name: str
    Baseboard_Heating_Type: str
    Baseboard_Heating_Availability_Schedule_Name: str
    Baseboard_Heating_Capacity: str
    Capacity_Control_Method: str

class HvactemplateZoneUnitaryType(TypedDict, total=False):
    """"dict for HvactemplateZoneUnitary"""
    Zone_Name: str
    Template_Unitary_System_Name: str
    Template_Thermostat_Name: str
    Supply_Air_Maximum_Flow_Rate: str
    Zone_Heating_Sizing_Factor: str
    Zone_Cooling_Sizing_Factor: str
    Outdoor_Air_Method: str
    Outdoor_Air_Flow_Rate_per_Person: str
    Outdoor_Air_Flow_Rate_per_Zone_Floor_Area: str
    Outdoor_Air_Flow_Rate_per_Zone: str
    Supply_Plenum_Name: str
    Return_Plenum_Name: str
    Baseboard_Heating_Type: str
    Baseboard_Heating_Availability_Schedule_Name: str
    Baseboard_Heating_Capacity: str
    Zone_Cooling_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Cooling_Design_Supply_Air_Temperature: str
    Zone_Cooling_Design_Supply_Air_Temperature_Difference: str
    Zone_Heating_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Heating_Design_Supply_Air_Temperature: str
    Zone_Heating_Design_Supply_Air_Temperature_Difference: str
    Design_Specification_Outdoor_Air_Object_Name: str
    Design_Specification_Zone_Air_Distribution_Object_Name: str

class HvactemplateZoneVavType(TypedDict, total=False):
    """"dict for HvactemplateZoneVav"""
    Zone_Name: str
    Template_VAV_System_Name: str
    Template_Thermostat_Name: str
    Supply_Air_Maximum_Flow_Rate: str
    Zone_Heating_Sizing_Factor: str
    Zone_Cooling_Sizing_Factor: str
    Zone_Minimum_Air_Flow_Input_Method: str
    Constant_Minimum_Air_Flow_Fraction: str
    Fixed_Minimum_Air_Flow_Rate: str
    Minimum_Air_Flow_Fraction_Schedule_Name: str
    Outdoor_Air_Method: str
    Outdoor_Air_Flow_Rate_per_Person: str
    Outdoor_Air_Flow_Rate_per_Zone_Floor_Area: str
    Outdoor_Air_Flow_Rate_per_Zone: str
    Reheat_Coil_Type: str
    Reheat_Coil_Availability_Schedule_Name: str
    Damper_Heating_Action: str
    Maximum_Flow_per_Zone_Floor_Area_During_Reheat: str
    Maximum_Flow_Fraction_During_Reheat: str
    Maximum_Reheat_Air_Temperature: str
    Design_Specification_Outdoor_Air_Object_Name_for_Control: str
    Supply_Plenum_Name: str
    Return_Plenum_Name: str
    Baseboard_Heating_Type: str
    Baseboard_Heating_Availability_Schedule_Name: str
    Baseboard_Heating_Capacity: str
    Zone_Cooling_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Cooling_Design_Supply_Air_Temperature: str
    Zone_Cooling_Design_Supply_Air_Temperature_Difference: str
    Zone_Heating_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Heating_Design_Supply_Air_Temperature: str
    Zone_Heating_Design_Supply_Air_Temperature_Difference: str
    Design_Specification_Outdoor_Air_Object_Name_for_Sizing: str
    Design_Specification_Zone_Air_Distribution_Object_Name: str

class HvactemplateZoneVavFanpoweredType(TypedDict, total=False):
    """"dict for HvactemplateZoneVavFanpowered"""
    Zone_Name: str
    Template_VAV_System_Name: str
    Template_Thermostat_Name: str
    Primary_Supply_Air_Maximum_Flow_Rate: str
    Zone_Heating_Sizing_Factor: str
    Zone_Cooling_Sizing_Factor: str
    Primary_Supply_Air_Minimum_Flow_Fraction: str
    Secondary_Supply_Air_Maximum_Flow_Rate: str
    Flow_Type: str
    Parallel_Fan_On_Flow_Fraction: str
    Outdoor_Air_Method: str
    Outdoor_Air_Flow_Rate_per_Person: str
    Outdoor_Air_Flow_Rate_per_Zone_Floor_Area: str
    Outdoor_Air_Flow_Rate_per_Zone: str
    Reheat_Coil_Type: str
    Reheat_Coil_Availability_Schedule_Name: str
    Fan_Total_Efficiency: str
    Fan_Delta_Pressure: str
    Fan_Motor_Efficiency: str
    Supply_Plenum_Name: str
    Return_Plenum_Name: str
    Baseboard_Heating_Type: str
    Baseboard_Heating_Availability_Schedule_Name: str
    Baseboard_Heating_Capacity: str
    Zone_Cooling_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Cooling_Design_Supply_Air_Temperature: str
    Zone_Cooling_Design_Supply_Air_Temperature_Difference: str
    Zone_Heating_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Heating_Design_Supply_Air_Temperature: str
    Zone_Heating_Design_Supply_Air_Temperature_Difference: str
    Zone_PIU_Fan_Schedule_Name: str
    Design_Specification_Outdoor_Air_Object_Name: str
    Design_Specification_Zone_Air_Distribution_Object_Name: str

class HvactemplateZoneVavHeatandcoolType(TypedDict, total=False):
    """"dict for HvactemplateZoneVavHeatandcool"""
    Zone_Name: str
    Template_VAV_System_Name: str
    Template_Thermostat_Name: str
    Supply_Air_Maximum_Flow_Rate: str
    Zone_Heating_Sizing_Factor: str
    Zone_Cooling_Sizing_Factor: str
    Constant_Minimum_Air_Flow_Fraction: str
    Outdoor_Air_Method: str
    Outdoor_Air_Flow_Rate_per_Person: str
    Outdoor_Air_Flow_Rate_per_Zone_Floor_Area: str
    Outdoor_Air_Flow_Rate_per_Zone: str
    Design_Specification_Outdoor_Air_Object_Name_for_Sizing: str
    Design_Specification_Zone_Air_Distribution_Object_Name: str
    Reheat_Coil_Type: str
    Reheat_Coil_Availability_Schedule_Name: str
    Maximum_Reheat_Air_Temperature: str
    Supply_Plenum_Name: str
    Return_Plenum_Name: str
    Baseboard_Heating_Type: str
    Baseboard_Heating_Availability_Schedule_Name: str
    Baseboard_Heating_Capacity: str
    Zone_Cooling_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Cooling_Design_Supply_Air_Temperature: str
    Zone_Cooling_Design_Supply_Air_Temperature_Difference: str
    Zone_Heating_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Heating_Design_Supply_Air_Temperature: str
    Zone_Heating_Design_Supply_Air_Temperature_Difference: str

class HvactemplateZoneVrfType(TypedDict, total=False):
    """"dict for HvactemplateZoneVrf"""
    Zone_Name: str
    Template_VRF_System_Name: str
    Template_Thermostat_Name: str
    Zone_Heating_Sizing_Factor: str
    Zone_Cooling_Sizing_Factor: str
    Rated_Total_Heating_Capacity_Sizing_Ratio: str
    Cooling_Supply_Air_Flow_Rate: str
    No_Cooling_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate: str
    No_Heating_Supply_Air_Flow_Rate: str
    Cooling_Outdoor_Air_Flow_Rate: str
    Heating_Outdoor_Air_Flow_Rate: str
    No_Load_Outdoor_Air_Flow_Rate: str
    Outdoor_Air_Method: str
    Outdoor_Air_Flow_Rate_per_Person: str
    Outdoor_Air_Flow_Rate_per_Zone_Floor_Area: str
    Outdoor_Air_Flow_Rate_per_Zone: str
    Design_Specification_Outdoor_Air_Object_Name: str
    Design_Specification_Zone_Air_Distribution_Object_Name: str
    System_Availability_Schedule_Name: str
    Supply_Fan_Operating_Mode_Schedule_Name: str
    Supply_Air_Fan_placement: str
    Supply_Fan_Total_Efficiency: str
    Supply_Fan_Delta_Pressure: str
    Supply_Fan_Motor_Efficiency: str
    Cooling_Coil_Type: str
    Cooling_Coil_Availability_Schedule_Name: str
    Cooling_Coil_Gross_Rated_Total_Capacity: str
    Cooling_Coil_Gross_Rated_Sensible_Heat_Ratio: str
    Heat_Pump_Heating_Coil_Type: str
    Heat_Pump_Heating_Coil_Availability_Schedule_Name: str
    Heat_Pump_Heating_Coil_Gross_Rated_Capacity: str
    Zone_Terminal_Unit_On_Parasitic_Electric_Energy_Use: str
    Zone_Terminal_Unit_Off_Parasitic_Electric_Energy_Use: str
    Dedicated_Outdoor_Air_System_Name: str
    Zone_Cooling_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Cooling_Design_Supply_Air_Temperature: str
    Zone_Cooling_Design_Supply_Air_Temperature_Difference: str
    Zone_Heating_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Heating_Design_Supply_Air_Temperature: str
    Zone_Heating_Design_Supply_Air_Temperature_Difference: str
    Baseboard_Heating_Type: str
    Baseboard_Heating_Availability_Schedule_Name: str
    Baseboard_Heating_Capacity: str

class HvactemplateZoneWatertoairheatpumpType(TypedDict, total=False):
    """"dict for HvactemplateZoneWatertoairheatpump"""
    Zone_Name: str
    Template_Thermostat_Name: str
    Cooling_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate: str
    No_Load_Supply_Air_Flow_Rate: str
    Zone_Heating_Sizing_Factor: str
    Zone_Cooling_Sizing_Factor: str
    Outdoor_Air_Method: str
    Outdoor_Air_Flow_Rate_per_Person: str
    Outdoor_Air_Flow_Rate_per_Zone_Floor_Area: str
    Outdoor_Air_Flow_Rate_per_Zone: str
    System_Availability_Schedule_Name: str
    Supply_Fan_Operating_Mode_Schedule_Name: str
    Supply_Fan_Placement: str
    Supply_Fan_Total_Efficiency: str
    Supply_Fan_Delta_Pressure: str
    Supply_Fan_Motor_Efficiency: str
    Cooling_Coil_Type: str
    Cooling_Coil_Gross_Rated_Total_Capacity: str
    Cooling_Coil_Gross_Rated_Sensible_Heat_Ratio: str
    Cooling_Coil_Gross_Rated_COP: str
    Heat_Pump_Heating_Coil_Type: str
    Heat_Pump_Heating_Coil_Gross_Rated_Capacity: str
    Heat_Pump_Heating_Coil_Gross_Rated_COP: str
    Supplemental_Heating_Coil_Availability_Schedule_Name: str
    Supplemental_Heating_Coil_Capacity: str
    Maximum_Cycling_Rate: str
    Latent_Capacity_Time_Constant: str
    Heat_Pump_Fan_Delay_Time: str
    Dedicated_Outdoor_Air_System_Name: str
    Supplemental_Heating_Coil_Type: str
    Zone_Cooling_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Cooling_Design_Supply_Air_Temperature: str
    Zone_Cooling_Design_Supply_Air_Temperature_Difference: str
    Zone_Heating_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Heating_Design_Supply_Air_Temperature: str
    Zone_Heating_Design_Supply_Air_Temperature_Difference: str
    Heat_Pump_Coil_Water_Flow_Mode: str
    Design_Specification_Outdoor_Air_Object_Name: str
    Design_Specification_Zone_Air_Distribution_Object_Name: str
    Baseboard_Heating_Type: str
    Baseboard_Heating_Availability_Schedule_Name: str
    Baseboard_Heating_Capacity: str

class HybridmodelZoneType(TypedDict, total=False):
    """"dict for HybridmodelZone"""
    Name: str
    Zone_Name: str
    Calculate_Zone_Internal_Thermal_Mass: str
    Calculate_Zone_Air_Infiltration_Rate: str
    Calculate_Zone_People_Count: str
    Zone_Measured_Air_Temperature_Schedule_Name: str
    Zone_Measured_Air_Humidity_Ratio_Schedule_Name: str
    Zone_Measured_Air_CO2_Concentration_Schedule_Name: str
    Zone_Input_People_Activity_Schedule_Name: str
    Zone_Input_People_Sensible_Heat_Fraction_Schedule_Name: str
    Zone_Input_People_Radiant_Heat_Fraction_Schedule_Name: str
    Zone_Input_People_CO2_Generation_Rate_Schedule_Name: str
    Zone_Input_Supply_Air_Temperature_Schedule_Name: str
    Zone_Input_Supply_Air_Mass_Flow_Rate_Schedule_Name: str
    Zone_Input_Supply_Air_Humidity_Ratio_Schedule_Name: str
    Zone_Input_Supply_Air_CO2_Concentration_Schedule_Name: str
    Begin_Month: str
    Begin_Day_of_Month: str
    End_Month: str
    End_Day_of_Month: str

class IndoorlivingwallType(TypedDict, total=False):
    """"dict for Indoorlivingwall"""
    Name: str
    Surface_Name: str
    Schedule_Name: str
    Evapotranspiration_Calculation_Method: str
    Lighting_Method: str
    LED_Intensity_Schedule_Name: str
    Daylighting_Control_Name: str
    LEDDaylight_Targeted_Lighting_Intensity_Schedule_Name: str
    Total_Leaf_Area: str
    LED_Nominal_Intensity: str
    LED_Nominal_Power: str
    Radiant_Fraction_of_LED_Lights: str

class InternalmassType(TypedDict, total=False):
    """"dict for Internalmass"""
    Name: str
    Construction_Name: str
    Zone_or_ZoneList_Name: str
    Space_or_SpaceList_Name: str
    Surface_Area: str

class LifecyclecostNonrecurringcostType(TypedDict, total=False):
    """"dict for LifecyclecostNonrecurringcost"""
    Name: str
    Category: str
    Cost: str
    Start_of_Costs: str
    Years_from_Start: str
    Months_from_Start: str

class LifecyclecostParametersType(TypedDict, total=False):
    """"dict for LifecyclecostParameters"""
    Name: str
    Discounting_Convention: str
    Inflation_Approach: str
    Real_Discount_Rate: str
    Nominal_Discount_Rate: str
    Inflation: str
    Base_Date_Month: str
    Base_Date_Year: str
    Service_Date_Month: str
    Service_Date_Year: str
    Length_of_Study_Period_in_Years: str
    Tax_rate: str
    Depreciation_Method: str

class LifecyclecostRecurringcostsType(TypedDict, total=False):
    """"dict for LifecyclecostRecurringcosts"""
    Name: str
    Category: str
    Cost: str
    Start_of_Costs: str
    Years_from_Start: str
    Months_from_Start: str
    Repeat_Period_Years: str
    Repeat_Period_Months: str
    Annual_escalation_rate: str

class LifecyclecostUseadjustmentType(TypedDict, total=False):
    """"dict for LifecyclecostUseadjustment"""
    Name: str
    Resource: str
    Year_1_Multiplier: str
    Year_2_Multiplier: str
    Year_3_Multiplier: str
    Year_4_Multiplier: str
    Year_5_Multiplier: str
    Year_6_Multiplier: str
    Year_7_Multiplier: str
    Year_8_Multiplier: str
    Year_9_Multiplier: str
    Year_10_Multiplier: str
    Year_11_Multiplier: str
    Year_12_Multiplier: str
    Year_13_Multiplier: str
    Year_14_Multiplier: str
    Year_15_Multiplier: str
    Year_16_Multiplier: str
    Year_17_Multiplier: str
    Year_18_Multiplier: str
    Year_19_Multiplier: str
    Year_20_Multiplier: str
    Year_21_Multiplier: str
    Year_22_Multiplier: str
    Year_23_Multiplier: str
    Year_24_Multiplier: str
    Year_25_Multiplier: str
    Year_26_Multiplier: str
    Year_27_Multiplier: str
    Year_28_Multiplier: str
    Year_29_Multiplier: str
    Year_30_Multiplier: str
    Year_31_Multiplier: str
    Year_32_Multiplier: str
    Year_33_Multiplier: str
    Year_34_Multiplier: str
    Year_35_Multiplier: str
    Year_36_Multiplier: str
    Year_37_Multiplier: str
    Year_38_Multiplier: str
    Year_39_Multiplier: str
    Year_40_Multiplier: str
    Year_41_Multiplier: str
    Year_42_Multiplier: str
    Year_43_Multiplier: str
    Year_44_Multiplier: str
    Year_45_Multiplier: str
    Year_46_Multiplier: str
    Year_47_Multiplier: str
    Year_48_Multiplier: str
    Year_49_Multiplier: str

class LifecyclecostUsepriceescalationType(TypedDict, total=False):
    """"dict for LifecyclecostUsepriceescalation"""
    LCC_Price_Escalation_Name: str
    Resource: str
    Escalation_Start_Year: str
    Escalation_Start_Month: str
    Year_1_Escalation: str
    Year_2_Escalation: str
    Year_3_Escalation: str
    Year_4_Escalation: str
    Year_5_Escalation: str
    Year_6_Escalation: str
    Year_7_Escalation: str
    Year_8_Escalation: str
    Year_9_Escalation: str
    Year_10_Escalation: str
    Year_11_Escalation: str
    Year_12_Escalation: str
    Year_13_Escalation: str
    Year_14_Escalation: str
    Year_15_Escalation: str
    Year_16_Escalation: str
    Year_17_Escalation: str
    Year_18_Escalation: str
    Year_19_Escalation: str
    Year_20_Escalation: str
    Year_21_Escalation: str
    Year_22_Escalation: str
    Year_23_Escalation: str
    Year_24_Escalation: str
    Year_25_Escalation: str
    Year_26_Escalation: str
    Year_27_Escalation: str
    Year_28_Escalation: str
    Year_29_Escalation: str
    Year_30_Escalation: str
    Year_31_Escalation: str
    Year_32_Escalation: str
    Year_33_Escalation: str
    Year_34_Escalation: str
    Year_35_Escalation: str
    Year_36_Escalation: str
    Year_37_Escalation: str
    Year_38_Escalation: str
    Year_39_Escalation: str
    Year_40_Escalation: str
    Year_41_Escalation: str
    Year_42_Escalation: str
    Year_43_Escalation: str
    Year_44_Escalation: str
    Year_45_Escalation: str
    Year_46_Escalation: str
    Year_47_Escalation: str
    Year_48_Escalation: str
    Year_49_Escalation: str

class LightsType(TypedDict, total=False):
    """"dict for Lights"""
    Name: str
    Zone_or_ZoneList_or_Space_or_SpaceList_Name: str
    Schedule_Name: str
    Design_Level_Calculation_Method: str
    Lighting_Level: str
    Watts_per_Floor_Area: str
    Watts_per_Person: str
    Return_Air_Fraction: str
    Fraction_Radiant: str
    Fraction_Visible: str
    Fraction_Replaceable: str
    EndUse_Subcategory: str
    Return_Air_Fraction_Calculated_from_Plenum_Temperature: str
    Return_Air_Fraction_Function_of_Plenum_Temperature_Coefficient_1: str
    Return_Air_Fraction_Function_of_Plenum_Temperature_Coefficient_2: str
    Return_Air_Heat_Gain_Node_Name: str
    Exhaust_Air_Heat_Gain_Node_Name: str

class LoadprofilePlantType(TypedDict, total=False):
    """"dict for LoadprofilePlant"""
    Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str
    Load_Schedule_Name: str
    Peak_Flow_Rate: str
    Flow_Rate_Fraction_Schedule_Name: str
    Plant_Loop_Fluid_Type: str
    Degree_of_SubCooling: str
    Degree_of_Loop_SubCooling: str

class MaterialType(TypedDict, total=False):
    """"dict for Material"""
    Name: str
    Roughness: str
    Thickness: str
    Conductivity: str
    Density: str
    Specific_Heat: str
    Thermal_Absorptance: str
    Solar_Absorptance: str
    Visible_Absorptance: str

class MaterialAirgapType(TypedDict, total=False):
    """"dict for MaterialAirgap"""
    Name: str
    Thermal_Resistance: str

class MaterialInfraredtransparentType(TypedDict, total=False):
    """"dict for MaterialInfraredtransparent"""
    Name: str

class MaterialNomassType(TypedDict, total=False):
    """"dict for MaterialNomass"""
    Name: str
    Roughness: str
    Thermal_Resistance: str
    Thermal_Absorptance: str
    Solar_Absorptance: str
    Visible_Absorptance: str

class MaterialRoofvegetationType(TypedDict, total=False):
    """"dict for MaterialRoofvegetation"""
    Name: str
    Height_of_Plants: str
    Leaf_Area_Index: str
    Leaf_Reflectivity: str
    Leaf_Emissivity: str
    Minimum_Stomatal_Resistance: str
    Soil_Layer_Name: str
    Roughness: str
    Thickness: str
    Conductivity_of_Dry_Soil: str
    Density_of_Dry_Soil: str
    Specific_Heat_of_Dry_Soil: str
    Thermal_Absorptance: str
    Solar_Absorptance: str
    Visible_Absorptance: str
    Saturation_Volumetric_Moisture_Content_of_the_Soil_Layer: str
    Residual_Volumetric_Moisture_Content_of_the_Soil_Layer: str
    Initial_Volumetric_Moisture_Content_of_the_Soil_Layer: str
    Moisture_Diffusion_Calculation_Method: str

class MaterialpropertyGlazingspectraldataType(TypedDict, total=False):
    """"dict for MaterialpropertyGlazingspectraldata"""
    Name: str
    Wavelength_1: str
    Transmittance_1: str
    Front_Reflectance_1: str
    Back_Reflectance_1: str
    Wavelength_2: str
    Transmittance_2: str
    Front_Reflectance_2: str
    Back_Reflectance_2: str
    Wavelength_3: str
    Transmittance_3: str
    Front_Reflectance_3: str
    Back_Reflectance_3: str
    Wavelength_4: str
    Transmittance_4: str
    Front_Reflectance_4: str
    Back_Reflectance_4: str
    Wavelength_5: str
    Transmittance_5: str
    Front_Reflectance_5: str
    Back_Reflectance_5: str
    Wavelength_6: str
    Transmittance_6: str
    Front_Reflectance_6: str
    Back_Reflectance_6: str
    Wavelength_7: str
    Transmittance_7: str
    Front_Reflectance_7: str
    Back_Reflectance_7: str
    Wavelength_8: str
    Transmittance_8: str
    Front_Reflectance_8: str
    Back_Reflectance_8: str
    Wavelength_9: str
    Transmittance_9: str
    Front_Reflectance_9: str
    Back_Reflectance_9: str
    Wavelength_10: str
    Transmittance_10: str
    Front_Reflectance_10: str
    Back_Reflectance_10: str
    Wavelength_11: str
    Transmittance_11: str
    Front_Reflectance_11: str
    Back_Reflectance_11: str
    Wavelength_12: str
    Transmittance_12: str
    Front_Reflectance_12: str
    Back_Reflectance_12: str
    Wavelength_13: str
    Transmittance_13: str
    Front_Reflectance_13: str
    Back_Reflectance_13: str
    Wavelength_14: str
    Transmittance_14: str
    Front_Reflectance_14: str
    Back_Reflectance_14: str
    Wavelength_15: str
    Transmittance_15: str
    Front_Reflectance_15: str
    Back_Reflectance_15: str
    Wavelength_16: str
    Transmittance_16: str
    Front_Reflectance_16: str
    Back_Reflectance_16: str
    Wavelength_17: str
    Transmittance_17: str
    Front_Reflectance_17: str
    Back_Reflectance_17: str
    Wavelength_18: str
    Transmittance_18: str
    Front_Reflectance_18: str
    Back_Reflectance_18: str
    Wavelength_19: str
    Transmittance_19: str
    Front_Reflectance_19: str
    Back_Reflectance_19: str
    Wavelength_20: str
    Transmittance_20: str
    Front_Reflectance_20: str
    Back_Reflectance_20: str
    Wavelength_21: str
    Transmittance_21: str
    Front_Reflectance_21: str
    Back_Reflectance_21: str
    Wavelength_22: str
    Transmittance_22: str
    Front_Reflectance_22: str
    Back_Reflectance_22: str
    Wavelength_23: str
    Transmittance_23: str
    Front_Reflectance_23: str
    Back_Reflectance_23: str
    Wavelength_24: str
    Transmittance_24: str
    Front_Reflectance_24: str
    Back_Reflectance_24: str
    Wavelength_25: str
    Transmittance_25: str
    Front_Reflectance_25: str
    Back_Reflectance_25: str
    Wavelength_26: str
    Transmittance_26: str
    Front_Reflectance_26: str
    Back_Reflectance_26: str
    Wavelength_27: str
    Transmittance_27: str
    Front_Reflectance_27: str
    Back_Reflectance_27: str
    Wavelength_28: str
    Transmittance_28: str
    Front_Reflectance_28: str
    Back_Reflectance_28: str
    Wavelength_29: str
    Transmittance_29: str
    Front_Reflectance_29: str
    Back_Reflectance_29: str
    Wavelength_30: str
    Transmittance_30: str
    Front_Reflectance_30: str
    Back_Reflectance_30: str
    Wavelength_31: str
    Transmittance_31: str
    Front_Reflectance_31: str
    Back_Reflectance_31: str
    Wavelength_32: str
    Transmittance_32: str
    Front_Reflectance_32: str
    Back_Reflectance_32: str
    Wavelength_33: str
    Transmittance_33: str
    Front_Reflectance_33: str
    Back_Reflectance_33: str
    Wavelength_34: str
    Transmittance_34: str
    Front_Reflectance_34: str
    Back_Reflectance_34: str
    Wavelength_35: str
    Transmittance_35: str
    Front_Reflectance_35: str
    Back_Reflectance_35: str
    Wavelength_36: str
    Transmittance_36: str
    Front_Reflectance_36: str
    Back_Reflectance_36: str
    Wavelength_37: str
    Transmittance_37: str
    Front_Reflectance_37: str
    Back_Reflectance_37: str
    Wavelength_38: str
    Transmittance_38: str
    Front_Reflectance_38: str
    Back_Reflectance_38: str
    Wavelength_39: str
    Transmittance_39: str
    Front_Reflectance_39: str
    Back_Reflectance_39: str
    Wavelength_40: str
    Transmittance_40: str
    Front_Reflectance_40: str
    Back_Reflectance_40: str
    Wavelength_41: str
    Transmittance_41: str
    Front_Reflectance_41: str
    Back_Reflectance_41: str
    Wavelength_42: str
    Transmittance_42: str
    Front_Reflectance_42: str
    Back_Reflectance_42: str
    Wavelength_43: str
    Transmittance_43: str
    Front_Reflectance_43: str
    Back_Reflectance_43: str
    Wavelength_44: str
    Transmittance_44: str
    Front_Reflectance_44: str
    Back_Reflectance_44: str
    Wavelength_45: str
    Transmittance_45: str
    Front_Reflectance_45: str
    Back_Reflectance_45: str
    Wavelength_46: str
    Transmittance_46: str
    Front_Reflectance_46: str
    Back_Reflectance_46: str
    Wavelength_47: str
    Transmittance_47: str
    Front_Reflectance_47: str
    Back_Reflectance_47: str
    Wavelength_48: str
    Transmittance_48: str
    Front_Reflectance_48: str
    Back_Reflectance_48: str
    Wavelength_49: str
    Transmittance_49: str
    Front_Reflectance_49: str
    Back_Reflectance_49: str

class MaterialpropertyHeatandmoisturetransferDiffusionType(TypedDict, total=False):
    """"dict for MaterialpropertyHeatandmoisturetransferDiffusion"""
    Material_Name: str
    Number_of_Data_Pairs: str
    Relative_Humidity_Fraction_1: str
    Water_Vapor_Diffusion_Resistance_Factor_1: str
    Relative_Humidity_Fraction_2: str
    Water_Vapor_Diffusion_Resistance_Factor_2: str
    Relative_Humidity_Fraction_3: str
    Water_Vapor_Diffusion_Resistance_Factor_3: str
    Relative_Humidity_Fraction_4: str
    Water_Vapor_Diffusion_Resistance_Factor_4: str
    Relative_Humidity_Fraction_5: str
    Water_Vapor_Diffusion_Resistance_Factor_5: str
    Relative_Humidity_Fraction_6: str
    Water_Vapor_Diffusion_Resistance_Factor_6: str
    Relative_Humidity_Fraction_7: str
    Water_Vapor_Diffusion_Resistance_Factor_7: str
    Relative_Humidity_Fraction_8: str
    Water_Vapor_Diffusion_Resistance_Factor_8: str
    Relative_Humidity_Fraction_9: str
    Water_Vapor_Diffusion_Resistance_Factor_9: str
    Relative_Humidity_Fraction_10: str
    Water_Vapor_Diffusion_Resistance_Factor_10: str
    Relative_Humidity_Fraction_11: str
    Water_Vapor_Diffusion_Resistance_Factor_11: str
    Relative_Humidity_Fraction_12: str
    Water_Vapor_Diffusion_Resistance_Factor_12: str
    Relative_Humidity_Fraction_13: str
    Water_Vapor_Diffusion_Resistance_Factor_13: str
    Relative_Humidity_Fraction_14: str
    Water_Vapor_Diffusion_Resistance_Factor_14: str
    Relative_Humidity_Fraction_15: str
    Water_Vapor_Diffusion_Resistance_Factor_15: str
    Relative_Humidity_Fraction_16: str
    Water_Vapor_Diffusion_Resistance_Factor_16: str
    Relative_Humidity_Fraction_17: str
    Water_Vapor_Diffusion_Resistance_Factor_17: str
    Relative_Humidity_Fraction_18: str
    Water_Vapor_Diffusion_Resistance_Factor_18: str
    Relative_Humidity_Fraction_19: str
    Water_Vapor_Diffusion_Resistance_Factor_19: str
    Relative_Humidity_Fraction_20: str
    Water_Vapor_Diffusion_Resistance_Factor_20: str
    Relative_Humidity_Fraction_21: str
    Water_Vapor_Diffusion_Resistance_Factor_21: str
    Relative_Humidity_Fraction_22: str
    Water_Vapor_Diffusion_Resistance_Factor_22: str
    Relative_Humidity_Fraction_23: str
    Water_Vapor_Diffusion_Resistance_Factor_23: str
    Relative_Humidity_Fraction_24: str
    Water_Vapor_Diffusion_Resistance_Factor_24: str
    Relative_Humidity_Fraction_25: str
    Water_Vapor_Diffusion_Resistance_Factor_25: str

class MaterialpropertyHeatandmoisturetransferRedistributionType(TypedDict, total=False):
    """"dict for MaterialpropertyHeatandmoisturetransferRedistribution"""
    Material_Name: str
    Number_of_Redistribution_points: str
    Moisture_Content_1: str
    Liquid_Transport_Coefficient_1: str
    Moisture_Content_2: str
    Liquid_Transport_Coefficient_2: str
    Moisture_Content_3: str
    Liquid_Transport_Coefficient_3: str
    Moisture_Content_4: str
    Liquid_Transport_Coefficient_4: str
    Moisture_Content_5: str
    Liquid_Transport_Coefficient_5: str
    Moisture_Content_6: str
    Liquid_Transport_Coefficient_6: str
    Moisture_Content_7: str
    Liquid_Transport_Coefficient_7: str
    Moisture_Content_8: str
    Liquid_Transport_Coefficient_8: str
    Moisture_Content_9: str
    Liquid_Transport_Coefficient_9: str
    Moisture_Content_10: str
    Liquid_Transport_Coefficient_10: str
    Moisture_Content_11: str
    Liquid_Transport_Coefficient_11: str
    Moisture_Content_12: str
    Liquid_Transport_Coefficient_12: str
    Moisture_Content_13: str
    Liquid_Transport_Coefficient_13: str
    Moisture_Content_14: str
    Liquid_Transport_Coefficient_14: str
    Moisture_Content_15: str
    Liquid_Transport_Coefficient_15: str
    Moisture_Content_16: str
    Liquid_Transport_Coefficient_16: str
    Moisture_Content_17: str
    Liquid_Transport_Coefficient_17: str
    Moisture_Content_18: str
    Liquid_Transport_Coefficient_18: str
    Moisture_Content_19: str
    Liquid_Transport_Coefficient_19: str
    Moisture_Content_20: str
    Liquid_Transport_Coefficient_20: str
    Moisture_Content_21: str
    Liquid_Transport_Coefficient_21: str
    Moisture_Content_22: str
    Liquid_Transport_Coefficient_22: str
    Moisture_Content_23: str
    Liquid_Transport_Coefficient_23: str
    Moisture_Content_24: str
    Liquid_Transport_Coefficient_24: str
    Moisture_Content_25: str
    Liquid_Transport_Coefficient_25: str

class MaterialpropertyHeatandmoisturetransferSettingsType(TypedDict, total=False):
    """"dict for MaterialpropertyHeatandmoisturetransferSettings"""
    Material_Name: str
    Porosity: str
    Initial_Water_Content_Ratio: str

class MaterialpropertyHeatandmoisturetransferSorptionisothermType(TypedDict, total=False):
    """"dict for MaterialpropertyHeatandmoisturetransferSorptionisotherm"""
    Material_Name: str
    Number_of_Isotherm_Coordinates: str
    Relative_Humidity_Fraction_1: str
    Moisture_Content_1: str
    Relative_Humidity_Fraction_2: str
    Moisture_Content_2: str
    Relative_Humidity_Fraction_3: str
    Moisture_Content_3: str
    Relative_Humidity_Fraction_4: str
    Moisture_Content_4: str
    Relative_Humidity_Fraction_5: str
    Moisture_Content_5: str
    Relative_Humidity_Fraction_6: str
    Moisture_Content_6: str
    Relative_Humidity_Fraction_7: str
    Moisture_Content_7: str
    Relative_Humidity_Fraction_8: str
    Moisture_Content_8: str
    Relative_Humidity_Fraction_9: str
    Moisture_Content_9: str
    Relative_Humidity_Fraction_10: str
    Moisture_Content_10: str
    Relative_Humidity_Fraction_11: str
    Moisture_Content_11: str
    Relative_Humidity_Fraction_12: str
    Moisture_Content_12: str
    Relative_Humidity_Fraction_13: str
    Moisture_Content_13: str
    Relative_Humidity_Fraction_14: str
    Moisture_Content_14: str
    Relative_Humidity_Fraction_15: str
    Moisture_Content_15: str
    Relative_Humidity_Fraction_16: str
    Moisture_Content_16: str
    Relative_Humidity_Fraction_17: str
    Moisture_Content_17: str
    Relative_Humidity_Fraction_18: str
    Moisture_Content_18: str
    Relative_Humidity_Fraction_19: str
    Moisture_Content_19: str
    Relative_Humidity_Fraction_20: str
    Moisture_Content_20: str
    Relative_Humidity_Fraction_21: str
    Moisture_Content_21: str
    Relative_Humidity_Fraction_22: str
    Moisture_Content_22: str
    Relative_Humidity_Fraction_23: str
    Moisture_Content_23: str
    Relative_Humidity_Fraction_24: str
    Moisture_Content_24: str
    Relative_Humidity_Fraction_25: str
    Moisture_Content_25: str

class MaterialpropertyHeatandmoisturetransferSuctionType(TypedDict, total=False):
    """"dict for MaterialpropertyHeatandmoisturetransferSuction"""
    Material_Name: str
    Number_of_Suction_points: str
    Moisture_Content_1: str
    Liquid_Transport_Coefficient_1: str
    Moisture_Content_2: str
    Liquid_Transport_Coefficient_2: str
    Moisture_Content_3: str
    Liquid_Transport_Coefficient_3: str
    Moisture_Content_4: str
    Liquid_Transport_Coefficient_4: str
    Moisture_Content_5: str
    Liquid_Transport_Coefficient_5: str
    Moisture_Content_6: str
    Liquid_Transport_Coefficient_6: str
    Moisture_Content_7: str
    Liquid_Transport_Coefficient_7: str
    Moisture_Content_8: str
    Liquid_Transport_Coefficient_8: str
    Moisture_Content_9: str
    Liquid_Transport_Coefficient_9: str
    Moisture_Content_10: str
    Liquid_Transport_Coefficient_10: str
    Moisture_Content_11: str
    Liquid_Transport_Coefficient_11: str
    Moisture_Content_12: str
    Liquid_Transport_Coefficient_12: str
    Moisture_Content_13: str
    Liquid_Transport_Coefficient_13: str
    Moisture_Content_14: str
    Liquid_Transport_Coefficient_14: str
    Moisture_Content_15: str
    Liquid_Transport_Coefficient_15: str
    Moisture_Content_16: str
    Liquid_Transport_Coefficient_16: str
    Moisture_Content_17: str
    Liquid_Transport_Coefficient_17: str
    Moisture_Content_18: str
    Liquid_Transport_Coefficient_18: str
    Moisture_Content_19: str
    Liquid_Transport_Coefficient_19: str
    Moisture_Content_20: str
    Liquid_Transport_Coefficient_20: str
    Moisture_Content_21: str
    Liquid_Transport_Coefficient_21: str
    Moisture_Content_22: str
    Liquid_Transport_Coefficient_22: str
    Moisture_Content_23: str
    Liquid_Transport_Coefficient_23: str
    Moisture_Content_24: str
    Liquid_Transport_Coefficient_24: str
    Moisture_Content_25: str
    Liquid_Transport_Coefficient_25: str

class MaterialpropertyHeatandmoisturetransferThermalconductivityType(TypedDict, total=False):
    """"dict for MaterialpropertyHeatandmoisturetransferThermalconductivity"""
    Material_Name: str
    Number_of_Thermal_Coordinates: str
    Moisture_Content_1: str
    Thermal_Conductivity_1: str
    Moisture_Content_2: str
    Thermal_Conductivity_2: str
    Moisture_Content_3: str
    Thermal_Conductivity_3: str
    Moisture_Content_4: str
    Thermal_Conductivity_4: str
    Moisture_Content_5: str
    Thermal_Conductivity_5: str
    Moisture_Content_6: str
    Thermal_Conductivity_6: str
    Moisture_Content_7: str
    Thermal_Conductivity_7: str
    Moisture_Content_8: str
    Thermal_Conductivity_8: str
    Moisture_Content_9: str
    Thermal_Conductivity_9: str
    Moisture_Content_10: str
    Thermal_Conductivity_10: str
    Moisture_Content_11: str
    Thermal_Conductivity_11: str
    Moisture_Content_12: str
    Thermal_Conductivity_12: str
    Moisture_Content_13: str
    Thermal_Conductivity_13: str
    Moisture_Content_14: str
    Thermal_Conductivity_14: str
    Moisture_Content_15: str
    Thermal_Conductivity_15: str
    Moisture_Content_16: str
    Thermal_Conductivity_16: str
    Moisture_Content_17: str
    Thermal_Conductivity_17: str
    Moisture_Content_18: str
    Thermal_Conductivity_18: str
    Moisture_Content_19: str
    Thermal_Conductivity_19: str
    Moisture_Content_20: str
    Thermal_Conductivity_20: str
    Moisture_Content_21: str
    Thermal_Conductivity_21: str
    Moisture_Content_22: str
    Thermal_Conductivity_22: str
    Moisture_Content_23: str
    Thermal_Conductivity_23: str
    Moisture_Content_24: str
    Thermal_Conductivity_24: str
    Moisture_Content_25: str
    Thermal_Conductivity_25: str

class MaterialpropertyMoisturepenetrationdepthSettingsType(TypedDict, total=False):
    """"dict for MaterialpropertyMoisturepenetrationdepthSettings"""
    Name: str
    Water_Vapor_Diffusion_Resistance_Factor: str
    Moisture_Equation_Coefficient_a: str
    Moisture_Equation_Coefficient_b: str
    Moisture_Equation_Coefficient_c: str
    Moisture_Equation_Coefficient_d: str
    Surface_Layer_Penetration_Depth: str
    Deep_Layer_Penetration_Depth: str
    Coating_Layer_Thickness: str
    Coating_Layer_Water_Vapor_Diffusion_Resistance_Factor: str

class MaterialpropertyPhasechangeType(TypedDict, total=False):
    """"dict for MaterialpropertyPhasechange"""
    Name: str
    Temperature_Coefficient_for_Thermal_Conductivity: str
    Temperature_1: str
    Enthalpy_1: str
    Temperature_2: str
    Enthalpy_2: str
    Temperature_3: str
    Enthalpy_3: str
    Temperature_4: str
    Enthalpy_4: str
    Temperature_5: str
    Enthalpy_5: str
    Temperature_6: str
    Enthalpy_6: str
    Temperature_7: str
    Enthalpy_7: str
    Temperature_8: str
    Enthalpy_8: str
    Temperature_9: str
    Enthalpy_9: str
    Temperature_10: str
    Enthalpy_10: str
    Temperature_11: str
    Enthalpy_11: str
    Temperature_12: str
    Enthalpy_12: str
    Temperature_13: str
    Enthalpy_13: str
    Temperature_14: str
    Enthalpy_14: str
    Temperature_15: str
    Enthalpy_15: str
    Temperature_16: str
    Enthalpy_16: str

class MaterialpropertyPhasechangehysteresisType(TypedDict, total=False):
    """"dict for MaterialpropertyPhasechangehysteresis"""
    Name: str
    Latent_Heat_during_the_Entire_Phase_Change_Process: str
    Liquid_State_Thermal_Conductivity: str
    Liquid_State_Density: str
    Liquid_State_Specific_Heat: str
    High_Temperature_Difference_of_Melting_Curve: str
    Peak_Melting_Temperature: str
    Low_Temperature_Difference_of_Melting_Curve: str
    Solid_State_Thermal_Conductivity: str
    Solid_State_Density: str
    Solid_State_Specific_Heat: str
    High_Temperature_Difference_of_Freezing_Curve: str
    Peak_Freezing_Temperature: str
    Low_Temperature_Difference_of_Freezing_Curve: str

class MaterialpropertyVariableabsorptanceType(TypedDict, total=False):
    """"dict for MaterialpropertyVariableabsorptance"""
    Name: str
    Reference_Material_Name: str
    Control_Signal: str
    Thermal_Absorptance_Function_Name: str
    Thermal_Absorptance_Schedule_Name: str
    Solar_Absorptance_Function_Name: str
    Solar_Absorptance_Schedule_Name: str

class MaterialpropertyVariablethermalconductivityType(TypedDict, total=False):
    """"dict for MaterialpropertyVariablethermalconductivity"""
    Name: str
    Temperature_1: str
    Thermal_Conductivity_1: str
    Temperature_2: str
    Thermal_Conductivity_2: str
    Temperature_3: str
    Thermal_Conductivity_3: str
    Temperature_4: str
    Thermal_Conductivity_4: str
    Temperature_5: str
    Thermal_Conductivity_5: str
    Temperature_6: str
    Thermal_Conductivity_6: str
    Temperature_7: str
    Thermal_Conductivity_7: str
    Temperature_8: str
    Thermal_Conductivity_8: str
    Temperature_9: str
    Thermal_Conductivity_9: str
    Temperature_10: str
    Thermal_Conductivity_10: str

class MatrixTwodimensionType(TypedDict, total=False):
    """"dict for MatrixTwodimension"""
    Name: str
    Number_of_Rows: str
    Number_of_Columns: str
    Value_1: str
    Value_2: str
    Value_3: str
    Value_4: str
    Value_5: str
    Value_6: str
    Value_7: str
    Value_8: str
    Value_9: str
    Value_10: str
    Value_11: str
    Value_12: str
    Value_13: str
    Value_14: str
    Value_15: str
    Value_16: str
    Value_17: str
    Value_18: str
    Value_19: str
    Value_20: str
    Value_21: str
    Value_22: str
    Value_23: str
    Value_24: str
    Value_25: str
    Value_26: str
    Value_27: str
    Value_28: str
    Value_29: str
    Value_30: str
    Value_31: str
    Value_32: str
    Value_33: str
    Value_34: str
    Value_35: str
    Value_36: str
    Value_37: str
    Value_38: str
    Value_39: str
    Value_40: str
    Value_41: str
    Value_42: str
    Value_43: str
    Value_44: str
    Value_45: str
    Value_46: str
    Value_47: str
    Value_48: str
    Value_49: str

class MeterCustomType(TypedDict, total=False):
    """"dict for MeterCustom"""
    Name: str
    Resource_Type: str
    Key_Name_1: str
    Output_Variable_or_Meter_Name_1: str
    Key_Name_2: str
    Output_Variable_or_Meter_Name_2: str
    Key_Name_3: str
    Output_Variable_or_Meter_Name_3: str
    Key_Name_4: str
    Output_Variable_or_Meter_Name_4: str
    Key_Name_5: str
    Output_Variable_or_Meter_Name_5: str
    Key_Name_6: str
    Output_Variable_or_Meter_Name_6: str
    Key_Name_7: str
    Output_Variable_or_Meter_Name_7: str
    Key_Name_8: str
    Output_Variable_or_Meter_Name_8: str
    Key_Name_9: str
    Output_Variable_or_Meter_Name_9: str
    Key_Name_10: str
    Output_Variable_or_Meter_Name_10: str
    Key_Name_11: str
    Output_Variable_or_Meter_Name_11: str
    Key_Name_12: str
    Output_Variable_or_Meter_Name_12: str
    Key_Name_13: str
    Output_Variable_or_Meter_Name_13: str
    Key_Name_14: str
    Output_Variable_or_Meter_Name_14: str
    Key_Name_15: str
    Output_Variable_or_Meter_Name_15: str
    Key_Name_16: str
    Output_Variable_or_Meter_Name_16: str
    Key_Name_17: str
    Output_Variable_or_Meter_Name_17: str
    Key_Name_18: str
    Output_Variable_or_Meter_Name_18: str
    Key_Name_19: str
    Output_Variable_or_Meter_Name_19: str
    Key_Name_20: str
    Output_Variable_or_Meter_Name_20: str
    Key_Name_21: str
    Output_Variable_or_Meter_Name_21: str
    Key_Name_22: str
    Output_Variable_or_Meter_Name_22: str
    Key_Name_23: str
    Output_Variable_or_Meter_Name_23: str
    Key_Name_24: str
    Output_Variable_or_Meter_Name_24: str
    Key_Name_25: str
    Output_Variable_or_Meter_Name_25: str
    Key_Name_26: str
    Output_Variable_or_Meter_Name_26: str
    Key_Name_27: str
    Output_Variable_or_Meter_Name_27: str
    Key_Name_28: str
    Output_Variable_or_Meter_Name_28: str
    Key_Name_29: str
    Output_Variable_or_Meter_Name_29: str
    Key_Name_30: str
    Output_Variable_or_Meter_Name_30: str
    Key_Name_31: str
    Output_Variable_or_Meter_Name_31: str
    Key_Name_32: str
    Output_Variable_or_Meter_Name_32: str
    Key_Name_33: str
    Output_Variable_or_Meter_Name_33: str
    Key_Name_34: str
    Output_Variable_or_Meter_Name_34: str
    Key_Name_35: str
    Output_Variable_or_Meter_Name_35: str
    Key_Name_36: str
    Output_Variable_or_Meter_Name_36: str
    Key_Name_37: str
    Output_Variable_or_Meter_Name_37: str
    Key_Name_38: str
    Output_Variable_or_Meter_Name_38: str
    Key_Name_39: str
    Output_Variable_or_Meter_Name_39: str
    Key_Name_40: str
    Output_Variable_or_Meter_Name_40: str
    Key_Name_41: str
    Output_Variable_or_Meter_Name_41: str
    Key_Name_42: str
    Output_Variable_or_Meter_Name_42: str
    Key_Name_43: str
    Output_Variable_or_Meter_Name_43: str
    Key_Name_44: str
    Output_Variable_or_Meter_Name_44: str
    Key_Name_45: str
    Output_Variable_or_Meter_Name_45: str
    Key_Name_46: str
    Output_Variable_or_Meter_Name_46: str
    Key_Name_47: str
    Output_Variable_or_Meter_Name_47: str
    Key_Name_48: str
    Output_Variable_or_Meter_Name_48: str
    Key_Name_49: str
    Output_Variable_or_Meter_Name_49: str

class MeterCustomdecrementType(TypedDict, total=False):
    """"dict for MeterCustomdecrement"""
    Name: str
    Resource_Type: str
    Source_Meter_Name: str
    Key_Name_1: str
    Output_Variable_or_Meter_Name_1: str
    Key_Name_2: str
    Output_Variable_or_Meter_Name_2: str
    Key_Name_3: str
    Output_Variable_or_Meter_Name_3: str
    Key_Name_4: str
    Output_Variable_or_Meter_Name_4: str
    Key_Name_5: str
    Output_Variable_or_Meter_Name_5: str
    Key_Name_6: str
    Output_Variable_or_Meter_Name_6: str
    Key_Name_7: str
    Output_Variable_or_Meter_Name_7: str
    Key_Name_8: str
    Output_Variable_or_Meter_Name_8: str
    Key_Name_9: str
    Output_Variable_or_Meter_Name_9: str
    Key_Name_10: str
    Output_Variable_or_Meter_Name_10: str
    Key_Name_11: str
    Output_Variable_or_Meter_Name_11: str
    Key_Name_12: str
    Output_Variable_or_Meter_Name_12: str
    Key_Name_13: str
    Output_Variable_or_Meter_Name_13: str
    Key_Name_14: str
    Output_Variable_or_Meter_Name_14: str
    Key_Name_15: str
    Output_Variable_or_Meter_Name_15: str
    Key_Name_16: str
    Output_Variable_or_Meter_Name_16: str
    Key_Name_17: str
    Output_Variable_or_Meter_Name_17: str
    Key_Name_18: str
    Output_Variable_or_Meter_Name_18: str
    Key_Name_19: str
    Output_Variable_or_Meter_Name_19: str
    Key_Name_20: str
    Output_Variable_or_Meter_Name_20: str
    Key_Name_21: str
    Output_Variable_or_Meter_Name_21: str
    Key_Name_22: str
    Output_Variable_or_Meter_Name_22: str

class NodelistType(TypedDict, total=False):
    """"dict for Nodelist"""
    Name: str
    Node_1_Name: str
    Node_2_Name: str
    Node_3_Name: str
    Node_4_Name: str
    Node_5_Name: str
    Node_6_Name: str
    Node_7_Name: str
    Node_8_Name: str
    Node_9_Name: str
    Node_10_Name: str
    Node_11_Name: str
    Node_12_Name: str
    Node_13_Name: str
    Node_14_Name: str
    Node_15_Name: str
    Node_16_Name: str
    Node_17_Name: str
    Node_18_Name: str
    Node_19_Name: str
    Node_20_Name: str
    Node_21_Name: str
    Node_22_Name: str
    Node_23_Name: str
    Node_24_Name: str
    Node_25_Name: str
    Node_26_Name: str
    Node_27_Name: str
    Node_28_Name: str
    Node_29_Name: str
    Node_30_Name: str
    Node_31_Name: str
    Node_32_Name: str
    Node_33_Name: str
    Node_34_Name: str
    Node_35_Name: str
    Node_36_Name: str
    Node_37_Name: str
    Node_38_Name: str
    Node_39_Name: str
    Node_40_Name: str
    Node_41_Name: str
    Node_42_Name: str
    Node_43_Name: str
    Node_44_Name: str
    Node_45_Name: str
    Node_46_Name: str
    Node_47_Name: str
    Node_48_Name: str
    Node_49_Name: str

class OtherequipmentType(TypedDict, total=False):
    """"dict for Otherequipment"""
    Name: str
    Fuel_Type: str
    Zone_or_ZoneList_or_Space_or_SpaceList_Name: str
    Schedule_Name: str
    Design_Level_Calculation_Method: str
    Design_Level: str
    Power_per_Floor_Area: str
    Power_per_Person: str
    Fraction_Latent: str
    Fraction_Radiant: str
    Fraction_Lost: str
    Carbon_Dioxide_Generation_Rate: str
    EndUse_Subcategory: str

class OutdoorairMixerType(TypedDict, total=False):
    """"dict for OutdoorairMixer"""
    Name: str
    Mixed_Air_Node_Name: str
    Outdoor_Air_Stream_Node_Name: str
    Relief_Air_Stream_Node_Name: str
    Return_Air_Stream_Node_Name: str

class OutdoorairNodeType(TypedDict, total=False):
    """"dict for OutdoorairNode"""
    Name: str
    Height_Above_Ground: str
    Drybulb_Temperature_Schedule_Name: str
    Wetbulb_Temperature_Schedule_Name: str
    Wind_Speed_Schedule_Name: str
    Wind_Direction_Schedule_Name: str
    Wind_Pressure_Coefficient_Curve_Name: str
    Symmetric_Wind_Pressure_Coefficient_Curve: str
    Wind_Angle_Type: str

class OutdoorairNodelistType(TypedDict, total=False):
    """"dict for OutdoorairNodelist"""
    Node_or_NodeList_Name_1: str
    Node_or_NodeList_Name_2: str
    Node_or_NodeList_Name_3: str
    Node_or_NodeList_Name_4: str
    Node_or_NodeList_Name_5: str
    Node_or_NodeList_Name_6: str
    Node_or_NodeList_Name_7: str
    Node_or_NodeList_Name_8: str
    Node_or_NodeList_Name_9: str
    Node_or_NodeList_Name_10: str
    Node_or_NodeList_Name_11: str
    Node_or_NodeList_Name_12: str
    Node_or_NodeList_Name_13: str
    Node_or_NodeList_Name_14: str
    Node_or_NodeList_Name_15: str
    Node_or_NodeList_Name_16: str
    Node_or_NodeList_Name_17: str
    Node_or_NodeList_Name_18: str
    Node_or_NodeList_Name_19: str
    Node_or_NodeList_Name_20: str
    Node_or_NodeList_Name_21: str
    Node_or_NodeList_Name_22: str
    Node_or_NodeList_Name_23: str
    Node_or_NodeList_Name_24: str
    Node_or_NodeList_Name_25: str
    Node_or_NodeList_Name_26: str
    Node_or_NodeList_Name_27: str
    Node_or_NodeList_Name_28: str
    Node_or_NodeList_Name_29: str
    Node_or_NodeList_Name_30: str
    Node_or_NodeList_Name_31: str
    Node_or_NodeList_Name_32: str
    Node_or_NodeList_Name_33: str
    Node_or_NodeList_Name_34: str
    Node_or_NodeList_Name_35: str
    Node_or_NodeList_Name_36: str
    Node_or_NodeList_Name_37: str
    Node_or_NodeList_Name_38: str
    Node_or_NodeList_Name_39: str
    Node_or_NodeList_Name_40: str
    Node_or_NodeList_Name_41: str
    Node_or_NodeList_Name_42: str
    Node_or_NodeList_Name_43: str
    Node_or_NodeList_Name_44: str
    Node_or_NodeList_Name_45: str
    Node_or_NodeList_Name_46: str
    Node_or_NodeList_Name_47: str
    Node_or_NodeList_Name_48: str
    Node_or_NodeList_Name_49: str

class OutputConstructionsType(TypedDict, total=False):
    """"dict for OutputConstructions"""
    Details_Type_1: str
    Details_Type_2: str

class OutputDaylightfactorsType(TypedDict, total=False):
    """"dict for OutputDaylightfactors"""
    Reporting_Days: str

class OutputDebuggingdataType(TypedDict, total=False):
    """"dict for OutputDebuggingdata"""
    Report_Debugging_Data: str
    Report_During_Warmup: str

class OutputDiagnosticsType(TypedDict, total=False):
    """"dict for OutputDiagnostics"""
    Key_1: str
    Key_2: str
    Key_3: str
    Key_4: str
    Key_5: str

class OutputEnergymanagementsystemType(TypedDict, total=False):
    """"dict for OutputEnergymanagementsystem"""
    Actuator_Availability_Dictionary_Reporting: str
    Internal_Variable_Availability_Dictionary_Reporting: str
    EMS_Runtime_Language_Debug_Output_Level: str

class OutputEnvironmentalimpactfactorsType(TypedDict, total=False):
    """"dict for OutputEnvironmentalimpactfactors"""
    Reporting_Frequency: str

class OutputIlluminancemapType(TypedDict, total=False):
    """"dict for OutputIlluminancemap"""
    Name: str
    Zone_Name: str
    Z_height: str
    X_Minimum_Coordinate: str
    X_Maximum_Coordinate: str
    Number_of_X_Grid_Points: str
    Y_Minimum_Coordinate: str
    Y_Maximum_Coordinate: str
    Number_of_Y_Grid_Points: str

class OutputJsonType(TypedDict, total=False):
    """"dict for OutputJson"""
    Option_Type: str
    Output_JSON: str
    Output_CBOR: str
    Output_MessagePack: str

class OutputMeterType(TypedDict, total=False):
    """"dict for OutputMeter"""
    Key_Name: str
    Reporting_Frequency: str

class OutputMeterCumulativeType(TypedDict, total=False):
    """"dict for OutputMeterCumulative"""
    Key_Name: str
    Reporting_Frequency: str

class OutputMeterCumulativeMeterfileonlyType(TypedDict, total=False):
    """"dict for OutputMeterCumulativeMeterfileonly"""
    Key_Name: str
    Reporting_Frequency: str

class OutputMeterMeterfileonlyType(TypedDict, total=False):
    """"dict for OutputMeterMeterfileonly"""
    Key_Name: str
    Reporting_Frequency: str

class OutputPreprocessormessageType(TypedDict, total=False):
    """"dict for OutputPreprocessormessage"""
    Preprocessor_Name: str
    Error_Severity: str
    Message_Line_1: str
    Message_Line_2: str
    Message_Line_3: str
    Message_Line_4: str
    Message_Line_5: str
    Message_Line_6: str
    Message_Line_7: str
    Message_Line_8: str
    Message_Line_9: str
    Message_Line_10: str

class OutputSchedulesType(TypedDict, total=False):
    """"dict for OutputSchedules"""
    Key_Field: str

class OutputSqliteType(TypedDict, total=False):
    """"dict for OutputSqlite"""
    Option_Type: str
    Unit_Conversion_for_Tabular_Data: str

class OutputSurfacesDrawingType(TypedDict, total=False):
    """"dict for OutputSurfacesDrawing"""
    Report_Type: str
    Report_Specifications_1: str
    Report_Specifications_2: str

class OutputSurfacesListType(TypedDict, total=False):
    """"dict for OutputSurfacesList"""
    Report_Type: str
    Report_Specifications: str

class OutputTableAnnualType(TypedDict, total=False):
    """"dict for OutputTableAnnual"""
    Name: str
    Filter: str
    Schedule_Name: str
    Variable_or_Meter_or_EMS_Variable_or_Field_1_Name: str
    Aggregation_Type_for_Variable_or_Meter_1: str
    Digits_After_Decimal_1: str
    Variable_or_Meter_or_EMS_Variable_or_Field_2_Name: str
    Aggregation_Type_for_Variable_or_Meter_2: str
    Digits_After_Decimal_2: str
    Variable_or_Meter_or_EMS_Variable_or_Field_3_Name: str
    Aggregation_Type_for_Variable_or_Meter_3: str
    Digits_After_Decimal_3: str
    Variable_or_Meter_or_EMS_Variable_or_Field_4_Name: str
    Aggregation_Type_for_Variable_or_Meter_4: str
    Digits_After_Decimal_4: str
    Variable_or_Meter_or_EMS_Variable_or_Field_5_Name: str
    Aggregation_Type_for_Variable_or_Meter_5: str
    Digits_After_Decimal_5: str
    Variable_or_Meter_or_EMS_Variable_or_Field_6_Name: str
    Aggregation_Type_for_Variable_or_Meter_6: str
    Digits_After_Decimal_6: str
    Variable_or_Meter_or_EMS_Variable_or_Field_7_Name: str
    Aggregation_Type_for_Variable_or_Meter_7: str
    Digits_After_Decimal_7: str
    Variable_or_Meter_or_EMS_Variable_or_Field_8_Name: str
    Aggregation_Type_for_Variable_or_Meter_8: str
    Digits_After_Decimal_8: str
    Variable_or_Meter_or_EMS_Variable_or_Field_9_Name: str
    Aggregation_Type_for_Variable_or_Meter_9: str
    Digits_After_Decimal_9: str
    Variable_or_Meter_or_EMS_Variable_or_Field_10_Name: str
    Aggregation_Type_for_Variable_or_Meter_10: str
    Digits_After_Decimal_10: str
    Variable_or_Meter_or_EMS_Variable_or_Field_11_Name: str
    Aggregation_Type_for_Variable_or_Meter_11: str
    Digits_After_Decimal_11: str
    Variable_or_Meter_or_EMS_Variable_or_Field_12_Name: str
    Aggregation_Type_for_Variable_or_Meter_12: str
    Digits_After_Decimal_12: str
    Variable_or_Meter_or_EMS_Variable_or_Field_13_Name: str
    Aggregation_Type_for_Variable_or_Meter_13: str
    Digits_After_Decimal_13: str
    Variable_or_Meter_or_EMS_Variable_or_Field_14_Name: str
    Aggregation_Type_for_Variable_or_Meter_14: str
    Digits_After_Decimal_14: str
    Variable_or_Meter_or_EMS_Variable_or_Field_15_Name: str
    Aggregation_Type_for_Variable_or_Meter_15: str
    Digits_After_Decimal_15: str

class OutputTableMonthlyType(TypedDict, total=False):
    """"dict for OutputTableMonthly"""
    Name: str
    Digits_After_Decimal: str
    Variable_or_Meter_1_Name: str
    Aggregation_Type_for_Variable_or_Meter_1: str
    Variable_or_Meter_2_Name: str
    Aggregation_Type_for_Variable_or_Meter_2: str
    Variable_or_Meter_3_Name: str
    Aggregation_Type_for_Variable_or_Meter_3: str
    Variable_or_Meter_4_Name: str
    Aggregation_Type_for_Variable_or_Meter_4: str
    Variable_or_Meter_5_Name: str
    Aggregation_Type_for_Variable_or_Meter_5: str
    Variable_or_Meter_6_Name: str
    Aggregation_Type_for_Variable_or_Meter_6: str
    Variable_or_Meter_7_Name: str
    Aggregation_Type_for_Variable_or_Meter_7: str
    Variable_or_Meter_8_Name: str
    Aggregation_Type_for_Variable_or_Meter_8: str
    Variable_or_Meter_9_Name: str
    Aggregation_Type_for_Variable_or_Meter_9: str
    Variable_or_Meter_10_Name: str
    Aggregation_Type_for_Variable_or_Meter_10: str
    Variable_or_Meter_11_Name: str
    Aggregation_Type_for_Variable_or_Meter_11: str
    Variable_or_Meter_12_Name: str
    Aggregation_Type_for_Variable_or_Meter_12: str
    Variable_or_Meter_13_Name: str
    Aggregation_Type_for_Variable_or_Meter_13: str
    Variable_or_Meter_14_Name: str
    Aggregation_Type_for_Variable_or_Meter_14: str
    Variable_or_Meter_15_Name: str
    Aggregation_Type_for_Variable_or_Meter_15: str
    Variable_or_Meter_16_Name: str
    Aggregation_Type_for_Variable_or_Meter_16: str
    Variable_or_Meter_17_Name: str
    Aggregation_Type_for_Variable_or_Meter_17: str
    Variable_or_Meter_18_Name: str
    Aggregation_Type_for_Variable_or_Meter_18: str
    Variable_or_Meter_19_Name: str
    Aggregation_Type_for_Variable_or_Meter_19: str
    Variable_or_Meter_20_Name: str
    Aggregation_Type_for_Variable_or_Meter_20: str
    Variable_or_Meter_21_Name: str
    Aggregation_Type_for_Variable_or_Meter_21: str
    Variable_or_Meter_22_Name: str
    Aggregation_Type_for_Variable_or_Meter_22: str
    Variable_or_Meter_23_Name: str
    Aggregation_Type_for_Variable_or_Meter_23: str
    Variable_or_Meter_24_Name: str
    Aggregation_Type_for_Variable_or_Meter_24: str
    Variable_or_Meter_25_Name: str
    Aggregation_Type_for_Variable_or_Meter_25: str

class OutputTableReportperiodType(TypedDict, total=False):
    """"dict for OutputTableReportperiod"""
    Name: str
    Report_Name: str
    Begin_Year: str
    Begin_Month: str
    Begin_Day_of_Month: str
    Begin_Hour_of_Day: str
    End_Year: str
    End_Month: str
    End_Day_of_Month: str
    End_Hour_of_Day: str

class OutputTableSummaryreportsType(TypedDict, total=False):
    """"dict for OutputTableSummaryreports"""
    Report_1_Name: str
    Report_2_Name: str
    Report_3_Name: str
    Report_4_Name: str
    Report_5_Name: str
    Report_6_Name: str
    Report_7_Name: str
    Report_8_Name: str
    Report_9_Name: str
    Report_10_Name: str
    Report_11_Name: str
    Report_12_Name: str
    Report_13_Name: str
    Report_14_Name: str
    Report_15_Name: str
    Report_16_Name: str
    Report_17_Name: str
    Report_18_Name: str
    Report_19_Name: str
    Report_20_Name: str
    Report_21_Name: str
    Report_22_Name: str
    Report_23_Name: str
    Report_24_Name: str
    Report_25_Name: str

class OutputTableTimebinsType(TypedDict, total=False):
    """"dict for OutputTableTimebins"""
    Key_Value: str
    Variable_Name: str
    Interval_Start: str
    Interval_Size: str
    Interval_Count: str
    Schedule_Name: str
    Variable_Type: str

class OutputVariableType(TypedDict, total=False):
    """"dict for OutputVariable"""
    Key_Value: str
    Variable_Name: str
    Reporting_Frequency: str
    Schedule_Name: str

class OutputVariabledictionaryType(TypedDict, total=False):
    """"dict for OutputVariabledictionary"""
    Key_Field: str
    Sort_Option: str

class OutputcontrolFilesType(TypedDict, total=False):
    """"dict for OutputcontrolFiles"""
    Output_CSV: str
    Output_MTR: str
    Output_ESO: str
    Output_EIO: str
    Output_Tabular: str
    Output_SQLite: str
    Output_JSON: str
    Output_AUDIT: str
    Output_Zone_Sizing: str
    Output_System_Sizing: str
    Output_DXF: str
    Output_BND: str
    Output_RDD: str
    Output_MDD: str
    Output_MTD: str
    Output_END: str
    Output_SHD: str
    Output_DFS: str
    Output_GLHE: str
    Output_DelightIn: str
    Output_DelightELdmp: str
    Output_DelightDFdmp: str
    Output_EDD: str
    Output_DBG: str
    Output_PerfLog: str
    Output_SLN: str
    Output_SCI: str
    Output_WRL: str
    Output_Screen: str
    Output_ExtShd: str
    Output_Tarcog: str

class OutputcontrolIlluminancemapStyleType(TypedDict, total=False):
    """"dict for OutputcontrolIlluminancemapStyle"""
    Column_Separator: str

class OutputcontrolReportingtolerancesType(TypedDict, total=False):
    """"dict for OutputcontrolReportingtolerances"""
    Tolerance_for_Time_Heating_Setpoint_Not_Met: str
    Tolerance_for_Time_Cooling_Setpoint_Not_Met: str

class OutputcontrolSizingStyleType(TypedDict, total=False):
    """"dict for OutputcontrolSizingStyle"""
    Column_Separator: str

class OutputcontrolSurfacecolorschemeType(TypedDict, total=False):
    """"dict for OutputcontrolSurfacecolorscheme"""
    Name: str
    Drawing_Element_1_Type: str
    Color_for_Drawing_Element_1: str
    Drawing_Element_2_Type: str
    Color_for_Drawing_Element_2: str
    Drawing_Element_3_Type: str
    Color_for_Drawing_Element_3: str
    Drawing_Element_4_Type: str
    Color_for_Drawing_Element_4: str
    Drawing_Element_5_Type: str
    Color_for_Drawing_Element_5: str
    Drawing_Element_6_Type: str
    Color_for_Drawing_Element_6: str
    Drawing_Element_7_Type: str
    Color_for_Drawing_Element_7: str
    Drawing_Element_8_Type: str
    Color_for_Drawing_Element_8: str
    Drawing_Element_9_Type: str
    Color_for_Drawing_Element_9: str
    Drawing_Element_10_Type: str
    Color_for_Drawing_Element_10: str
    Drawing_Element_11_Type: str
    Color_for_Drawing_Element_11: str
    Drawing_Element_12_Type: str
    Color_for_Drawing_Element_12: str
    Drawing_Element_13_Type: str
    Color_for_Drawing_Element_13: str
    Drawing_Element_14_Type: str
    Color_for_Drawing_Element_14: str
    Drawing_Element_15_Type: str
    Color_for_Drawing_Element_15: str

class OutputcontrolTableStyleType(TypedDict, total=False):
    """"dict for OutputcontrolTableStyle"""
    Column_Separator: str
    Unit_Conversion: str

class OutputcontrolTimestampType(TypedDict, total=False):
    """"dict for OutputcontrolTimestamp"""
    ISO_8601_Format: str
    Timestamp_at_Beginning_of_Interval: str

class ParametricFilenamesuffixType(TypedDict, total=False):
    """"dict for ParametricFilenamesuffix"""
    Name: str
    Suffix_for_File_Name_in_Run_1: str
    Suffix_for_File_Name_in_Run_2: str
    Suffix_for_File_Name_in_Run_3: str
    Suffix_for_File_Name_in_Run_4: str
    Suffix_for_File_Name_in_Run_5: str
    Suffix_for_File_Name_in_Run_6: str
    Suffix_for_File_Name_in_Run_7: str
    Suffix_for_File_Name_in_Run_8: str
    Suffix_for_File_Name_in_Run_9: str
    Suffix_for_File_Name_in_Run_10: str
    Suffix_for_File_Name_in_Run_11: str
    Suffix_for_File_Name_in_Run_12: str
    Suffix_for_File_Name_in_Run_13: str
    Suffix_for_File_Name_in_Run_14: str
    Suffix_for_File_Name_in_Run_15: str
    Suffix_for_File_Name_in_Run_16: str
    Suffix_for_File_Name_in_Run_17: str
    Suffix_for_File_Name_in_Run_18: str
    Suffix_for_File_Name_in_Run_19: str
    Suffix_for_File_Name_in_Run_20: str
    Suffix_for_File_Name_in_Run_21: str
    Suffix_for_File_Name_in_Run_22: str
    Suffix_for_File_Name_in_Run_23: str
    Suffix_for_File_Name_in_Run_24: str
    Suffix_for_File_Name_in_Run_25: str
    Suffix_for_File_Name_in_Run_26: str
    Suffix_for_File_Name_in_Run_27: str
    Suffix_for_File_Name_in_Run_28: str
    Suffix_for_File_Name_in_Run_29: str
    Suffix_for_File_Name_in_Run_30: str
    Suffix_for_File_Name_in_Run_31: str
    Suffix_for_File_Name_in_Run_32: str
    Suffix_for_File_Name_in_Run_33: str
    Suffix_for_File_Name_in_Run_34: str
    Suffix_for_File_Name_in_Run_35: str
    Suffix_for_File_Name_in_Run_36: str
    Suffix_for_File_Name_in_Run_37: str
    Suffix_for_File_Name_in_Run_38: str
    Suffix_for_File_Name_in_Run_39: str
    Suffix_for_File_Name_in_Run_40: str
    Suffix_for_File_Name_in_Run_41: str
    Suffix_for_File_Name_in_Run_42: str
    Suffix_for_File_Name_in_Run_43: str
    Suffix_for_File_Name_in_Run_44: str
    Suffix_for_File_Name_in_Run_45: str
    Suffix_for_File_Name_in_Run_46: str
    Suffix_for_File_Name_in_Run_47: str
    Suffix_for_File_Name_in_Run_48: str
    Suffix_for_File_Name_in_Run_49: str

class ParametricLogicType(TypedDict, total=False):
    """"dict for ParametricLogic"""
    Name: str
    Parametric_Logic_Line_1: str
    Parametric_Logic_Line_2: str
    Parametric_Logic_Line_3: str
    Parametric_Logic_Line_4: str
    Parametric_Logic_Line_5: str
    Parametric_Logic_Line_6: str
    Parametric_Logic_Line_7: str
    Parametric_Logic_Line_8: str
    Parametric_Logic_Line_9: str
    Parametric_Logic_Line_10: str
    Parametric_Logic_Line_11: str
    Parametric_Logic_Line_12: str
    Parametric_Logic_Line_13: str
    Parametric_Logic_Line_14: str
    Parametric_Logic_Line_15: str
    Parametric_Logic_Line_16: str
    Parametric_Logic_Line_17: str
    Parametric_Logic_Line_18: str
    Parametric_Logic_Line_19: str
    Parametric_Logic_Line_20: str
    Parametric_Logic_Line_21: str
    Parametric_Logic_Line_22: str
    Parametric_Logic_Line_23: str
    Parametric_Logic_Line_24: str
    Parametric_Logic_Line_25: str
    Parametric_Logic_Line_26: str
    Parametric_Logic_Line_27: str
    Parametric_Logic_Line_28: str
    Parametric_Logic_Line_29: str
    Parametric_Logic_Line_30: str
    Parametric_Logic_Line_31: str
    Parametric_Logic_Line_32: str
    Parametric_Logic_Line_33: str
    Parametric_Logic_Line_34: str
    Parametric_Logic_Line_35: str
    Parametric_Logic_Line_36: str
    Parametric_Logic_Line_37: str
    Parametric_Logic_Line_38: str
    Parametric_Logic_Line_39: str
    Parametric_Logic_Line_40: str
    Parametric_Logic_Line_41: str
    Parametric_Logic_Line_42: str
    Parametric_Logic_Line_43: str
    Parametric_Logic_Line_44: str
    Parametric_Logic_Line_45: str
    Parametric_Logic_Line_46: str
    Parametric_Logic_Line_47: str
    Parametric_Logic_Line_48: str
    Parametric_Logic_Line_49: str

class ParametricRuncontrolType(TypedDict, total=False):
    """"dict for ParametricRuncontrol"""
    Name: str
    Perform_Run_1: str
    Perform_Run_2: str
    Perform_Run_3: str
    Perform_Run_4: str
    Perform_Run_5: str
    Perform_Run_6: str
    Perform_Run_7: str
    Perform_Run_8: str
    Perform_Run_9: str
    Perform_Run_10: str
    Perform_Run_11: str
    Perform_Run_12: str
    Perform_Run_13: str
    Perform_Run_14: str
    Perform_Run_15: str
    Perform_Run_16: str
    Perform_Run_17: str
    Perform_Run_18: str
    Perform_Run_19: str
    Perform_Run_20: str
    Perform_Run_21: str
    Perform_Run_22: str
    Perform_Run_23: str
    Perform_Run_24: str
    Perform_Run_25: str
    Perform_Run_26: str
    Perform_Run_27: str
    Perform_Run_28: str
    Perform_Run_29: str
    Perform_Run_30: str
    Perform_Run_31: str
    Perform_Run_32: str
    Perform_Run_33: str
    Perform_Run_34: str
    Perform_Run_35: str
    Perform_Run_36: str
    Perform_Run_37: str
    Perform_Run_38: str
    Perform_Run_39: str
    Perform_Run_40: str
    Perform_Run_41: str
    Perform_Run_42: str
    Perform_Run_43: str
    Perform_Run_44: str
    Perform_Run_45: str
    Perform_Run_46: str
    Perform_Run_47: str
    Perform_Run_48: str
    Perform_Run_49: str

class ParametricSetvalueforrunType(TypedDict, total=False):
    """"dict for ParametricSetvalueforrun"""
    Name: str
    Value_for_Run_1: str
    Value_for_Run_2: str
    Value_for_Run_3: str
    Value_for_Run_4: str
    Value_for_Run_5: str
    Value_for_Run_6: str
    Value_for_Run_7: str
    Value_for_Run_8: str
    Value_for_Run_9: str
    Value_for_Run_10: str
    Value_for_Run_11: str
    Value_for_Run_12: str
    Value_for_Run_13: str
    Value_for_Run_14: str
    Value_for_Run_15: str
    Value_for_Run_16: str
    Value_for_Run_17: str
    Value_for_Run_18: str
    Value_for_Run_19: str
    Value_for_Run_20: str
    Value_for_Run_21: str
    Value_for_Run_22: str
    Value_for_Run_23: str
    Value_for_Run_24: str
    Value_for_Run_25: str
    Value_for_Run_26: str
    Value_for_Run_27: str
    Value_for_Run_28: str
    Value_for_Run_29: str
    Value_for_Run_30: str
    Value_for_Run_31: str
    Value_for_Run_32: str
    Value_for_Run_33: str
    Value_for_Run_34: str
    Value_for_Run_35: str
    Value_for_Run_36: str
    Value_for_Run_37: str
    Value_for_Run_38: str
    Value_for_Run_39: str
    Value_for_Run_40: str
    Value_for_Run_41: str
    Value_for_Run_42: str
    Value_for_Run_43: str
    Value_for_Run_44: str
    Value_for_Run_45: str
    Value_for_Run_46: str
    Value_for_Run_47: str
    Value_for_Run_48: str
    Value_for_Run_49: str

class PeopleType(TypedDict, total=False):
    """"dict for People"""
    Name: str
    Zone_or_ZoneList_or_Space_or_SpaceList_Name: str
    Number_of_People_Schedule_Name: str
    Number_of_People_Calculation_Method: str
    Number_of_People: str
    People_per_Floor_Area: str
    Floor_Area_per_Person: str
    Fraction_Radiant: str
    Sensible_Heat_Fraction: str
    Activity_Level_Schedule_Name: str
    Carbon_Dioxide_Generation_Rate: str
    Enable_ASHRAE_55_Comfort_Warnings: str
    Mean_Radiant_Temperature_Calculation_Type: str
    Surface_NameAngle_Factor_List_Name: str
    Work_Efficiency_Schedule_Name: str
    Clothing_Insulation_Calculation_Method: str
    Clothing_Insulation_Calculation_Method_Schedule_Name: str
    Clothing_Insulation_Schedule_Name: str
    Air_Velocity_Schedule_Name: str
    Thermal_Comfort_Model_1_Type: str
    Thermal_Comfort_Model_2_Type: str
    Thermal_Comfort_Model_3_Type: str
    Thermal_Comfort_Model_4_Type: str
    Thermal_Comfort_Model_5_Type: str
    Thermal_Comfort_Model_6_Type: str
    Thermal_Comfort_Model_7_Type: str
    Ankle_Level_Air_Velocity_Schedule_Name: str
    Cold_Stress_Temperature_Threshold: str
    Heat_Stress_Temperature_Threshold: str

class PerformanceprecisiontradeoffsType(TypedDict, total=False):
    """"dict for Performanceprecisiontradeoffs"""
    Use_Coil_Direct_Solutions: str
    Zone_Radiant_Exchange_Algorithm: str
    Override_Mode: str
    MaxZoneTempDiff: str
    MaxAllowedDelTemp: str
    Use_Representative_Surfaces_for_Calculations: str

class PhotovoltaicperformanceEquivalentonediodeType(TypedDict, total=False):
    """"dict for PhotovoltaicperformanceEquivalentonediode"""
    Name: str
    Cell_type: str
    Number_of_Cells_in_Series: str
    Active_Area: str
    Transmittance_Absorptance_Product: str
    Semiconductor_Bandgap: str
    Shunt_Resistance: str
    Short_Circuit_Current: str
    Open_Circuit_Voltage: str
    Reference_Temperature: str
    Reference_Insolation: str
    Module_Current_at_Maximum_Power: str
    Module_Voltage_at_Maximum_Power: str
    Temperature_Coefficient_of_Short_Circuit_Current: str
    Temperature_Coefficient_of_Open_Circuit_Voltage: str
    Nominal_Operating_Cell_Temperature_Test_Ambient_Temperature: str
    Nominal_Operating_Cell_Temperature_Test_Cell_Temperature: str
    Nominal_Operating_Cell_Temperature_Test_Insolation: str
    Module_Heat_Loss_Coefficient: str
    Total_Heat_Capacity: str

class PhotovoltaicperformanceSandiaType(TypedDict, total=False):
    """"dict for PhotovoltaicperformanceSandia"""
    Name: str
    Active_Area: str
    Number_of_Cells_in_Series: str
    Number_of_Cells_in_Parallel: str
    Short_Circuit_Current: str
    Open_Circuit_Voltage: str
    Current_at_Maximum_Power_Point: str
    Voltage_at_Maximum_Power_Point: str
    Sandia_Database_Parameter_aIsc: str
    Sandia_Database_Parameter_aImp: str
    Sandia_Database_Parameter_c0: str
    Sandia_Database_Parameter_c1: str
    Sandia_Database_Parameter_BVoc0: str
    Sandia_Database_Parameter_mBVoc: str
    Sandia_Database_Parameter_BVmp0: str
    Sandia_Database_Parameter_mBVmp: str
    Diode_Factor: str
    Sandia_Database_Parameter_c2: str
    Sandia_Database_Parameter_c3: str
    Sandia_Database_Parameter_a0: str
    Sandia_Database_Parameter_a1: str
    Sandia_Database_Parameter_a2: str
    Sandia_Database_Parameter_a3: str
    Sandia_Database_Parameter_a4: str
    Sandia_Database_Parameter_b0: str
    Sandia_Database_Parameter_b1: str
    Sandia_Database_Parameter_b2: str
    Sandia_Database_Parameter_b3: str
    Sandia_Database_Parameter_b4: str
    Sandia_Database_Parameter_b5: str
    Sandia_Database_Parameter_DeltaTc: str
    Sandia_Database_Parameter_fd: str
    Sandia_Database_Parameter_a: str
    Sandia_Database_Parameter_b: str
    Sandia_Database_Parameter_c4: str
    Sandia_Database_Parameter_c5: str
    Sandia_Database_Parameter_Ix0: str
    Sandia_Database_Parameter_Ixx0: str
    Sandia_Database_Parameter_c6: str
    Sandia_Database_Parameter_c7: str

class PhotovoltaicperformanceSimpleType(TypedDict, total=False):
    """"dict for PhotovoltaicperformanceSimple"""
    Name: str
    Fraction_of_Surface_Area_with_Active_Solar_Cells: str
    Conversion_Efficiency_Input_Mode: str
    Value_for_Cell_Efficiency_if_Fixed: str
    Efficiency_Schedule_Name: str

class PipeAdiabaticType(TypedDict, total=False):
    """"dict for PipeAdiabatic"""
    Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str

class PipeAdiabaticSteamType(TypedDict, total=False):
    """"dict for PipeAdiabaticSteam"""
    Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str

class PipeIndoorType(TypedDict, total=False):
    """"dict for PipeIndoor"""
    Name: str
    Construction_Name: str
    Fluid_Inlet_Node_Name: str
    Fluid_Outlet_Node_Name: str
    Environment_Type: str
    Ambient_Temperature_Zone_Name: str
    Ambient_Temperature_Schedule_Name: str
    Ambient_Air_Velocity_Schedule_Name: str
    Pipe_Inside_Diameter: str
    Pipe_Length: str

class PipeOutdoorType(TypedDict, total=False):
    """"dict for PipeOutdoor"""
    Name: str
    Construction_Name: str
    Fluid_Inlet_Node_Name: str
    Fluid_Outlet_Node_Name: str
    Ambient_Temperature_Outdoor_Air_Node_Name: str
    Pipe_Inside_Diameter: str
    Pipe_Length: str

class PipeUndergroundType(TypedDict, total=False):
    """"dict for PipeUnderground"""
    Name: str
    Construction_Name: str
    Fluid_Inlet_Node_Name: str
    Fluid_Outlet_Node_Name: str
    Sun_Exposure: str
    Pipe_Inside_Diameter: str
    Pipe_Length: str
    Soil_Material_Name: str
    Undisturbed_Ground_Temperature_Model_Type: str
    Undisturbed_Ground_Temperature_Model_Name: str

class PipingsystemUndergroundDomainType(TypedDict, total=False):
    """"dict for PipingsystemUndergroundDomain"""
    Name: str
    Xmax: str
    Ymax: str
    Zmax: str
    XDirection_Mesh_Density_Parameter: str
    XDirection_Mesh_Type: str
    XDirection_Geometric_Coefficient: str
    YDirection_Mesh_Density_Parameter: str
    YDirection_Mesh_Type: str
    YDirection_Geometric_Coefficient: str
    ZDirection_Mesh_Density_Parameter: str
    ZDirection_Mesh_Type: str
    ZDirection_Geometric_Coefficient: str
    Soil_Thermal_Conductivity: str
    Soil_Density: str
    Soil_Specific_Heat: str
    Soil_Moisture_Content_Volume_Fraction: str
    Soil_Moisture_Content_Volume_Fraction_at_Saturation: str
    Undisturbed_Ground_Temperature_Model_Type: str
    Undisturbed_Ground_Temperature_Model_Name: str
    This_Domain_Includes_Basement_Surface_Interaction: str
    Width_of_Basement_Floor_in_Ground_Domain: str
    Depth_of_Basement_Wall_In_Ground_Domain: str
    Shift_Pipe_X_Coordinates_By_Basement_Width: str
    Name_of_Basement_Wall_Boundary_Condition_Model: str
    Name_of_Basement_Floor_Boundary_Condition_Model: str
    Convergence_Criterion_for_the_Outer_Cartesian_Domain_Iteration_Loop: str
    Maximum_Iterations_in_the_Outer_Cartesian_Domain_Iteration_Loop: str
    Evapotranspiration_Ground_Cover_Parameter: str
    Number_of_Pipe_Circuits_Entered_for_this_Domain: str
    Pipe_Circuit_1: str
    Pipe_Circuit_2: str
    Pipe_Circuit_3: str
    Pipe_Circuit_4: str
    Pipe_Circuit_5: str
    Pipe_Circuit_6: str

class PipingsystemUndergroundPipecircuitType(TypedDict, total=False):
    """"dict for PipingsystemUndergroundPipecircuit"""
    Name: str
    Pipe_Thermal_Conductivity: str
    Pipe_Density: str
    Pipe_Specific_Heat: str
    Pipe_Inner_Diameter: str
    Pipe_Outer_Diameter: str
    Design_Flow_Rate: str
    Circuit_Inlet_Node: str
    Circuit_Outlet_Node: str
    Convergence_Criterion_for_the_Inner_Radial_Iteration_Loop: str
    Maximum_Iterations_in_the_Inner_Radial_Iteration_Loop: str
    Number_of_Soil_Nodes_in_the_Inner_Radial_Near_Pipe_Mesh_Region: str
    Radial_Thickness_of_Inner_Radial_Near_Pipe_Mesh_Region: str
    Number_of_Pipe_Segments_Entered_for_this_Pipe_Circuit: str
    Pipe_Segment_1: str
    Pipe_Segment_2: str
    Pipe_Segment_3: str
    Pipe_Segment_4: str
    Pipe_Segment_5: str
    Pipe_Segment_6: str

class PipingsystemUndergroundPipesegmentType(TypedDict, total=False):
    """"dict for PipingsystemUndergroundPipesegment"""
    Name: str
    X_Position: str
    Y_Position: str
    Flow_Direction: str

class PlantcomponentTemperaturesourceType(TypedDict, total=False):
    """"dict for PlantcomponentTemperaturesource"""
    Name: str
    Inlet_Node: str
    Outlet_Node: str
    Design_Volume_Flow_Rate: str
    Temperature_Specification_Type: str
    Source_Temperature: str
    Source_Temperature_Schedule_Name: str

class PlantcomponentUserdefinedType(TypedDict, total=False):
    """"dict for PlantcomponentUserdefined"""
    Name: str
    Main_Model_Program_Calling_Manager_Name: str
    Number_of_Plant_Loop_Connections: str
    Plant_Connection_1_Inlet_Node_Name: str
    Plant_Connection_1_Outlet_Node_Name: str
    Plant_Connection_1_Loading_Mode: str
    Plant_Connection_1_Loop_Flow_Request_Mode: str
    Plant_Connection_1_Initialization_Program_Calling_Manager_Name: str
    Plant_Connection_1_Simulation_Program_Calling_Manager_Name: str
    Plant_Connection_2_Inlet_Node_Name: str
    Plant_Connection_2_Outlet_Node_Name: str
    Plant_Connection_2_Loading_Mode: str
    Plant_Connection_2_Loop_Flow_Request_Mode: str
    Plant_Connection_2_Initialization_Program_Calling_Manager_Name: str
    Plant_Connection_2_Simulation_Program_Calling_Manager_Name: str
    Plant_Connection_3_Inlet_Node_Name: str
    Plant_Connection_3_Outlet_Node_Name: str
    Plant_Connection_3_Loading_Mode: str
    Plant_Connection_3_Loop_Flow_Request_Mode: str
    Plant_Connection_3_Initialization_Program_Calling_Manager_Name: str
    Plant_Connection_3_Simulation_Program_Calling_Manager_Name: str
    Plant_Connection_4_Inlet_Node_Name: str
    Plant_Connection_4_Outlet_Node_Name: str
    Plant_Connection_4_Loading_Mode: str
    Plant_Connection_4_Loop_Flow_Request_Mode: str
    Plant_Connection_4_Initialization_Program_Calling_Manager_Name: str
    Plant_Connection_4_Simulation_Program_Calling_Manager_Name: str
    Air_Connection_Inlet_Node_Name: str
    Air_Connection_Outlet_Node_Name: str
    Supply_Inlet_Water_Storage_Tank_Name: str
    Collection_Outlet_Water_Storage_Tank_Name: str
    Ambient_Zone_Name: str

class PlantequipmentlistType(TypedDict, total=False):
    """"dict for Plantequipmentlist"""
    Name: str
    Equipment_1_Object_Type: str
    Equipment_1_Name: str
    Equipment_2_Object_Type: str
    Equipment_2_Name: str
    Equipment_3_Object_Type: str
    Equipment_3_Name: str
    Equipment_4_Object_Type: str
    Equipment_4_Name: str
    Equipment_5_Object_Type: str
    Equipment_5_Name: str
    Equipment_6_Object_Type: str
    Equipment_6_Name: str
    Equipment_7_Object_Type: str
    Equipment_7_Name: str
    Equipment_8_Object_Type: str
    Equipment_8_Name: str
    Equipment_9_Object_Type: str
    Equipment_9_Name: str
    Equipment_10_Object_Type: str
    Equipment_10_Name: str

class PlantequipmentoperationChillerheaterchangeoverType(TypedDict, total=False):
    """"dict for PlantequipmentoperationChillerheaterchangeover"""
    Name: str
    Primary_Cooling_Plant_Setpoint_Temperature: str
    Secondary_Distribution_Cooling_Plant_Setpoint_Temperature: str
    Primary_Heating_Plant_Setpoint_at_Outdoor_High_Temperature: str
    Outdoor_High_Temperature: str
    Primary_Heating_Plant_Setpoint_at_Outdoor_Low_Temperature: str
    Outdoor_Low_Temperature: str
    Secondary_Distribution_Heating_Plant_Setpoint_Temperature: str
    Zone_Load_Polling_ZoneList_Name: str
    Cooling_Only_Load_Plant_Equipment_Operation_Cooling_Load_Name: str
    Heating_Only_Load_Plant_Equipment_Operation_Heating_Load_Name: str
    Simultaneous_Cooling_And_Heating_Plant_Equipment_Operation_Cooling_Load_Name: str
    Simultaneous_Cooling_And_Heating_Plant_Equipment_Operation_Heating_Load_Name: str
    Dedicated_Chilled_Water_Return_Recovery_Heat_Pump_Name: str
    Dedicated_Hot_Water_Return_Recovery_Heat_Pump_Name: str
    Boiler_Setpoint_Temperature_Offset: str
    Primary_Heating_Plant_Setpoint_at_Backup_Outdoor_Low_Temperature: str
    Backup_Outdoor_Low_Temperature: str

class PlantequipmentoperationComponentsetpointType(TypedDict, total=False):
    """"dict for PlantequipmentoperationComponentsetpoint"""
    Name: str
    Equipment_1_Object_Type: str
    Equipment_1_Name: str
    Demand_Calculation_1_Node_Name: str
    Setpoint_1_Node_Name: str
    Component_1_Flow_Rate: str
    Operation_1_Type: str
    Equipment_2_Object_Type: str
    Equipment_2_Name: str
    Demand_Calculation_2_Node_Name: str
    Setpoint_2_Node_Name: str
    Component_2_Flow_Rate: str
    Operation_2_Type: str
    Equipment_3_Object_Type: str
    Equipment_3_Name: str
    Demand_Calculation_3_Node_Name: str
    Setpoint_3_Node_Name: str
    Component_3_Flow_Rate: str
    Operation_3_Type: str
    Equipment_4_Object_Type: str
    Equipment_4_Name: str
    Demand_Calculation_4_Node_Name: str
    Setpoint_4_Node_Name: str
    Component_4_Flow_Rate: str
    Operation_4_Type: str
    Equipment_5_Object_Type: str
    Equipment_5_Name: str
    Demand_Calculation_5_Node_Name: str
    Setpoint_5_Node_Name: str
    Component_5_Flow_Rate: str
    Operation_5_Type: str
    Equipment_6_Object_Type: str
    Equipment_6_Name: str
    Demand_Calculation_6_Node_Name: str
    Setpoint_6_Node_Name: str
    Component_6_Flow_Rate: str
    Operation_6_Type: str
    Equipment_7_Object_Type: str
    Equipment_7_Name: str
    Demand_Calculation_7_Node_Name: str
    Setpoint_7_Node_Name: str
    Component_7_Flow_Rate: str
    Operation_7_Type: str
    Equipment_8_Object_Type: str
    Equipment_8_Name: str
    Demand_Calculation_8_Node_Name: str
    Setpoint_8_Node_Name: str
    Component_8_Flow_Rate: str
    Operation_8_Type: str
    Equipment_9_Object_Type: str
    Equipment_9_Name: str
    Demand_Calculation_9_Node_Name: str
    Setpoint_9_Node_Name: str
    Component_9_Flow_Rate: str
    Operation_9_Type: str
    Equipment_10_Object_Type: str
    Equipment_10_Name: str
    Demand_Calculation_10_Node_Name: str
    Setpoint_10_Node_Name: str
    Component_10_Flow_Rate: str
    Operation_10_Type: str

class PlantequipmentoperationCoolingloadType(TypedDict, total=False):
    """"dict for PlantequipmentoperationCoolingload"""
    Name: str
    Load_Range_1_Lower_Limit: str
    Load_Range_1_Upper_Limit: str
    Range_1_Equipment_List_Name: str
    Load_Range_2_Lower_Limit: str
    Load_Range_2_Upper_Limit: str
    Range_2_Equipment_List_Name: str
    Load_Range_3_Lower_Limit: str
    Load_Range_3_Upper_Limit: str
    Range_3_Equipment_List_Name: str
    Load_Range_4_Lower_Limit: str
    Load_Range_4_Upper_Limit: str
    Range_4_Equipment_List_Name: str
    Load_Range_5_Lower_Limit: str
    Load_Range_5_Upper_Limit: str
    Range_5_Equipment_List_Name: str
    Load_Range_6_Lower_Limit: str
    Load_Range_6_Upper_Limit: str
    Range_6_Equipment_List_Name: str
    Load_Range_7_Lower_Limit: str
    Load_Range_7_Upper_Limit: str
    Range_7_Equipment_List_Name: str
    Load_Range_8_Lower_Limit: str
    Load_Range_8_Upper_Limit: str
    Range_8_Equipment_List_Name: str
    Load_Range_9_Lower_Limit: str
    Load_Range_9_Upper_Limit: str
    Range_9_Equipment_List_Name: str
    Load_Range_10_Lower_Limit: str
    Load_Range_10_Upper_Limit: str
    Range_10_Equipment_List_Name: str

class PlantequipmentoperationHeatingloadType(TypedDict, total=False):
    """"dict for PlantequipmentoperationHeatingload"""
    Name: str
    Load_Range_1_Lower_Limit: str
    Load_Range_1_Upper_Limit: str
    Range_1_Equipment_List_Name: str
    Load_Range_2_Lower_Limit: str
    Load_Range_2_Upper_Limit: str
    Range_2_Equipment_List_Name: str
    Load_Range_3_Lower_Limit: str
    Load_Range_3_Upper_Limit: str
    Range_3_Equipment_List_Name: str
    Load_Range_4_Lower_Limit: str
    Load_Range_4_Upper_Limit: str
    Range_4_Equipment_List_Name: str
    Load_Range_5_Lower_Limit: str
    Load_Range_5_Upper_Limit: str
    Range_5_Equipment_List_Name: str
    Load_Range_6_Lower_Limit: str
    Load_Range_6_Upper_Limit: str
    Range_6_Equipment_List_Name: str
    Load_Range_7_Lower_Limit: str
    Load_Range_7_Upper_Limit: str
    Range_7_Equipment_List_Name: str
    Load_Range_8_Lower_Limit: str
    Load_Range_8_Upper_Limit: str
    Range_8_Equipment_List_Name: str
    Load_Range_9_Lower_Limit: str
    Load_Range_9_Upper_Limit: str
    Range_9_Equipment_List_Name: str
    Load_Range_10_Lower_Limit: str
    Load_Range_10_Upper_Limit: str
    Range_10_Equipment_List_Name: str

class PlantequipmentoperationOutdoordewpointType(TypedDict, total=False):
    """"dict for PlantequipmentoperationOutdoordewpoint"""
    Name: str
    Dewpoint_Temperature_Range_1_Lower_Limit: str
    Dewpoint_Temperature_Range_1_Upper_Limit: str
    Range_1_Equipment_List_Name: str
    Dewpoint_Temperature_Range_2_Lower_Limit: str
    Dewpoint_Temperature_Range_2_Upper_Limit: str
    Range_2_Equipment_List_Name: str
    Dewpoint_Temperature_Range_3_Lower_Limit: str
    Dewpoint_Temperature_Range_3_Upper_Limit: str
    Range_3_Equipment_List_Name: str
    Dewpoint_Temperature_Range_4_Lower_Limit: str
    Dewpoint_Temperature_Range_4_Upper_Limit: str
    Range_4_Equipment_List_Name: str
    Dewpoint_Temperature_Range_5_Lower_Limit: str
    Dewpoint_Temperature_Range_5_Upper_Limit: str
    Range_5_Equipment_List_Name: str
    Dewpoint_Temperature_Range_6_Lower_Limit: str
    Dewpoint_Temperature_Range_6_Upper_Limit: str
    Range_6_Equipment_List_Name: str
    Dewpoint_Temperature_Range_7_Lower_Limit: str
    Dewpoint_Temperature_Range_7_Upper_Limit: str
    Range_7_Equipment_List_Name: str
    Dewpoint_Temperature_Range_8_Lower_Limit: str
    Dewpoint_Temperature_Range_8_Upper_Limit: str
    Range_8_Equipment_List_Name: str
    Dewpoint_Temperature_Range_9_Lower_Limit: str
    Dewpoint_Temperature_Range_9_Upper_Limit: str
    Range_9_Equipment_List_Name: str
    Dewpoint_Temperature_Range_10_Lower_Limit: str
    Dewpoint_Temperature_Range_10_Upper_Limit: str
    Range_10_Equipment_List_Name: str

class PlantequipmentoperationOutdoordewpointdifferenceType(TypedDict, total=False):
    """"dict for PlantequipmentoperationOutdoordewpointdifference"""
    Name: str
    Reference_Temperature_Node_Name: str
    Dewpoint_Temperature_Difference_Range_1_Lower_Limit: str
    Dewpoint_Temperature_Difference_Range_1_Upper_Limit: str
    Range_1_Equipment_List_Name: str
    Dewpoint_Temperature_Difference_Range_2_Lower_Limit: str
    Dewpoint_Temperature_Difference_Range_2_Upper_Limit: str
    Range_2_Equipment_List_Name: str
    Dewpoint_Temperature_Difference_Range_3_Lower_Limit: str
    Dewpoint_Temperature_Difference_Range_3_Upper_Limit: str
    Range_3_Equipment_List_Name: str
    Dewpoint_Temperature_Difference_Range_4_Lower_Limit: str
    Dewpoint_Temperature_Difference_Range_4_Upper_Limit: str
    Range_4_Equipment_List_Name: str
    Dewpoint_Temperature_Difference_Range_5_Lower_Limit: str
    Dewpoint_Temperature_Difference_Range_5_Upper_Limit: str
    Range_5_Equipment_List_Name: str
    Dewpoint_Temperature_Difference_Range_6_Lower_Limit: str
    Dewpoint_Temperature_Difference_Range_6_Upper_Limit: str
    Range_6_Equipment_List_Name: str
    Dewpoint_Temperature_Difference_Range_7_Lower_Limit: str
    Dewpoint_Temperature_Difference_Range_7_Upper_Limit: str
    Range_7_Equipment_List_Name: str
    Dewpoint_Temperature_Difference_Range_8_Lower_Limit: str
    Dewpoint_Temperature_Difference_Range_8_Upper_Limit: str
    Range_8_Equipment_List_Name: str
    Dewpoint_Temperature_Difference_Range_9_Lower_Limit: str
    Dewpoint_Temperature_Difference_Range_9_Upper_Limit: str
    Range_9_Equipment_List_Name: str
    Dewpoint_Temperature_Difference_Range_10_Lower_Limit: str
    Dewpoint_Temperature_Difference_Range_10_Upper_Limit: str
    Range_10_Equipment_List_Name: str

class PlantequipmentoperationOutdoordrybulbType(TypedDict, total=False):
    """"dict for PlantequipmentoperationOutdoordrybulb"""
    Name: str
    DryBulb_Temperature_Range_1_Lower_Limit: str
    DryBulb_Temperature_Range_1_Upper_Limit: str
    Range_1_Equipment_List_Name: str
    DryBulb_Temperature_Range_2_Lower_Limit: str
    DryBulb_Temperature_Range_2_Upper_Limit: str
    Range_2_Equipment_List_Name: str
    DryBulb_Temperature_Range_3_Lower_Limit: str
    DryBulb_Temperature_Range_3_Upper_Limit: str
    Range_3_Equipment_List_Name: str
    DryBulb_Temperature_Range_4_Lower_Limit: str
    DryBulb_Temperature_Range_4_Upper_Limit: str
    Range_4_Equipment_List_Name: str
    DryBulb_Temperature_Range_5_Lower_Limit: str
    DryBulb_Temperature_Range_5_Upper_Limit: str
    Range_5_Equipment_List_Name: str
    DryBulb_Temperature_Range_6_Lower_Limit: str
    DryBulb_Temperature_Range_6_Upper_Limit: str
    Range_6_Equipment_List_Name: str
    DryBulb_Temperature_Range_7_Lower_Limit: str
    DryBulb_Temperature_Range_7_Upper_Limit: str
    Range_7_Equipment_List_Name: str
    DryBulb_Temperature_Range_8_Lower_Limit: str
    DryBulb_Temperature_Range_8_Upper_Limit: str
    Range_8_Equipment_List_Name: str
    DryBulb_Temperature_Range_9_Lower_Limit: str
    DryBulb_Temperature_Range_9_Upper_Limit: str
    Range_9_Equipment_List_Name: str
    DryBulb_Temperature_Range_10_Lower_Limit: str
    DryBulb_Temperature_Range_10_Upper_Limit: str
    Range_10_Equipment_List_Name: str

class PlantequipmentoperationOutdoordrybulbdifferenceType(TypedDict, total=False):
    """"dict for PlantequipmentoperationOutdoordrybulbdifference"""
    Name: str
    Reference_Temperature_Node_Name: str
    DryBulb_Temperature_Difference_Range_1_Lower_Limit: str
    DryBulb_Temperature_Difference_Range_1_Upper_Limit: str
    Range_1_Equipment_List_Name: str
    DryBulb_Temperature_Difference_Range_2_Lower_Limit: str
    DryBulb_Temperature_Difference_Range_2_Upper_Limit: str
    Range_2_Equipment_List_Name: str
    DryBulb_Temperature_Difference_Range_3_Lower_Limit: str
    DryBulb_Temperature_Difference_Range_3_Upper_Limit: str
    Range_3_Equipment_List_Name: str
    DryBulb_Temperature_Difference_Range_4_Lower_Limit: str
    DryBulb_Temperature_Difference_Range_4_Upper_Limit: str
    Range_4_Equipment_List_Name: str
    DryBulb_Temperature_Difference_Range_5_Lower_Limit: str
    DryBulb_Temperature_Difference_Range_5_Upper_Limit: str
    Range_5_Equipment_List_Name: str
    DryBulb_Temperature_Difference_Range_6_Lower_Limit: str
    DryBulb_Temperature_Difference_Range_6_Upper_Limit: str
    Range_6_Equipment_List_Name: str
    DryBulb_Temperature_Difference_Range_7_Lower_Limit: str
    DryBulb_Temperature_Difference_Range_7_Upper_Limit: str
    Range_7_Equipment_List_Name: str
    DryBulb_Temperature_Difference_Range_8_Lower_Limit: str
    DryBulb_Temperature_Difference_Range_8_Upper_Limit: str
    Range_8_Equipment_List_Name: str
    DryBulb_Temperature_Difference_Range_9_Lower_Limit: str
    DryBulb_Temperature_Difference_Range_9_Upper_Limit: str
    Range_9_Equipment_List_Name: str
    DryBulb_Temperature_Difference_Range_10_Lower_Limit: str
    DryBulb_Temperature_Difference_Range_10_Upper_Limit: str
    Range_10_Equipment_List_Name: str

class PlantequipmentoperationOutdoorrelativehumidityType(TypedDict, total=False):
    """"dict for PlantequipmentoperationOutdoorrelativehumidity"""
    Name: str
    Relative_Humidity_Range_1_Lower_Limit: str
    Relative_Humidity_Range_1_Upper_Limit: str
    Range_1_Equipment_List_Name: str
    Relative_Humidity_Range_2_Lower_Limit: str
    Relative_Humidity_Range_2_Upper_Limit: str
    Range_2_Equipment_List_Name: str
    Relative_Humidity_Range_3_Lower_Limit: str
    Relative_Humidity_Range_3_Upper_Limit: str
    Range_3_Equipment_List_Name: str
    Relative_Humidity_Range_4_Lower_Limit: str
    Relative_Humidity_Range_4_Upper_Limit: str
    Range_4_Equipment_List_Name: str
    Relative_Humidity_Range_5_Lower_Limit: str
    Relative_Humidity_Range_5_Upper_Limit: str
    Range_5_Equipment_List_Name: str
    Relative_Humidity_Range_6_Lower_Limit: str
    Relative_Humidity_Range_6_Upper_Limit: str
    Range_6_Equipment_List_Name: str
    Relative_Humidity_Range_7_Lower_Limit: str
    Relative_Humidity_Range_7_Upper_Limit: str
    Range_7_Equipment_List_Name: str
    Relative_Humidity_Range_8_Lower_Limit: str
    Relative_Humidity_Range_8_Upper_Limit: str
    Range_8_Equipment_List_Name: str
    Relative_Humidity_Range_9_Lower_Limit: str
    Relative_Humidity_Range_9_Upper_Limit: str
    Range_9_Equipment_List_Name: str
    Relative_Humidity_Range_10_Lower_Limit: str
    Relative_Humidity_Range_10_Upper_Limit: str
    Range_10_Equipment_List_Name: str

class PlantequipmentoperationOutdoorwetbulbType(TypedDict, total=False):
    """"dict for PlantequipmentoperationOutdoorwetbulb"""
    Name: str
    WetBulb_Temperature_Range_1_Lower_Limit: str
    WetBulb_Temperature_Range_1_Upper_Limit: str
    Range_1_Equipment_List_Name: str
    WetBulb_Temperature_Range_2_Lower_Limit: str
    WetBulb_Temperature_Range_2_Upper_Limit: str
    Range_2_Equipment_List_Name: str
    WetBulb_Temperature_Range_3_Lower_Limit: str
    WetBulb_Temperature_Range_3_Upper_Limit: str
    Range_3_Equipment_List_Name: str
    WetBulb_Temperature_Range_4_Lower_Limit: str
    WetBulb_Temperature_Range_4_Upper_Limit: str
    Range_4_Equipment_List_Name: str
    WetBulb_Temperature_Range_5_Lower_Limit: str
    WetBulb_Temperature_Range_5_Upper_Limit: str
    Range_5_Equipment_List_Name: str
    WetBulb_Temperature_Range_6_Lower_Limit: str
    WetBulb_Temperature_Range_6_Upper_Limit: str
    Range_6_Equipment_List_Name: str
    WetBulb_Temperature_Range_7_Lower_Limit: str
    WetBulb_Temperature_Range_7_Upper_Limit: str
    Range_7_Equipment_List_Name: str
    WetBulb_Temperature_Range_8_Lower_Limit: str
    WetBulb_Temperature_Range_8_Upper_Limit: str
    Range_8_Equipment_List_Name: str
    WetBulb_Temperature_Range_9_Lower_Limit: str
    WetBulb_Temperature_Range_9_Upper_Limit: str
    Range_9_Equipment_List_Name: str
    WetBulb_Temperature_Range_10_Lower_Limit: str
    WetBulb_Temperature_Range_10_Upper_Limit: str
    Range_10_Equipment_List_Name: str

class PlantequipmentoperationOutdoorwetbulbdifferenceType(TypedDict, total=False):
    """"dict for PlantequipmentoperationOutdoorwetbulbdifference"""
    Name: str
    Reference_Temperature_Node_Name: str
    WetBulb_Temperature_Difference_Range_1_Lower_Limit: str
    WetBulb_Temperature_Difference_Range_1_Upper_Limit: str
    Range_1_Equipment_List_Name: str
    WetBulb_Temperature_Difference_Range_2_Lower_Limit: str
    WetBulb_Temperature_Difference_Range_2_Upper_Limit: str
    Range_2_Equipment_List_Name: str
    WetBulb_Temperature_Difference_Range_3_Lower_Limit: str
    WetBulb_Temperature_Difference_Range_3_Upper_Limit: str
    Range_3_Equipment_List_Name: str
    WetBulb_Temperature_Difference_Range_4_Lower_Limit: str
    WetBulb_Temperature_Difference_Range_4_Upper_Limit: str
    Range_4_Equipment_List_Name: str
    WetBulb_Temperature_Difference_Range_5_Lower_Limit: str
    WetBulb_Temperature_Difference_Range_5_Upper_Limit: str
    Range_5_Equipment_List_Name: str
    WetBulb_Temperature_Difference_Range_6_Lower_Limit: str
    WetBulb_Temperature_Difference_Range_6_Upper_Limit: str
    Range_6_Equipment_List_Name: str
    WetBulb_Temperature_Difference_Range_7_Lower_Limit: str
    WetBulb_Temperature_Difference_Range_7_Upper_Limit: str
    Range_7_Equipment_List_Name: str
    WetBulb_Temperature_Difference_Range_8_Lower_Limit: str
    WetBulb_Temperature_Difference_Range_8_Upper_Limit: str
    Range_8_Equipment_List_Name: str
    WetBulb_Temperature_Difference_Range_9_Lower_Limit: str
    WetBulb_Temperature_Difference_Range_9_Upper_Limit: str
    Range_9_Equipment_List_Name: str
    WetBulb_Temperature_Difference_Range_10_Lower_Limit: str
    WetBulb_Temperature_Difference_Range_10_Upper_Limit: str
    Range_10_Equipment_List_Name: str

class PlantequipmentoperationThermalenergystorageType(TypedDict, total=False):
    """"dict for PlantequipmentoperationThermalenergystorage"""
    Name: str
    OnPeak_Schedule: str
    Charging_Availability_Schedule: str
    NonCharging_Chilled_Water_Temperature: str
    Charging_Chilled_Water_Temperature: str
    Component_1_Object_Type: str
    Component_1_Name: str
    Component_1_Demand_Calculation_Node_Name: str
    Component_1_Setpoint_Node_Name: str
    Component_1_Flow_Rate: str
    Component_1_Operation_Type: str
    Component_2_Object_Type: str
    Component_2_Name: str
    Component_2_Demand_Calculation_Node_Name: str
    Component_2_Setpoint_Node_Name: str
    Component_2_Flow_Rate: str
    Component_2_Operation_Type: str
    Component_3_Object_Type: str
    Component_3_Name: str
    Component_3_Demand_Calculation_Node_Name: str
    Component_3_Setpoint_Node_Name: str
    Component_3_Flow_Rate: str
    Component_3_Operation_Type: str
    Component_4_Object_Type: str
    Component_4_Name: str
    Component_4_Demand_Calculation_Node_Name: str
    Component_4_Setpoint_Node_Name: str
    Component_4_Flow_Rate: str
    Component_4_Operation_Type: str
    Component_5_Object_Type: str
    Component_5_Name: str
    Component_5_Demand_Calculation_Node_Name: str
    Component_5_Setpoint_Node_Name: str
    Component_5_Flow_Rate: str
    Component_5_Operation_Type: str
    Component_6_Object_Type: str
    Component_6_Name: str
    Component_6_Demand_Calculation_Node_Name: str
    Component_6_Setpoint_Node_Name: str
    Component_6_Flow_Rate: str
    Component_6_Operation_Type: str
    Component_7_Object_Type: str
    Component_7_Name: str
    Component_7_Demand_Calculation_Node_Name: str
    Component_7_Setpoint_Node_Name: str
    Component_7_Flow_Rate: str
    Component_7_Operation_Type: str
    Component_8_Object_Type: str
    Component_8_Name: str
    Component_8_Demand_Calculation_Node_Name: str
    Component_8_Setpoint_Node_Name: str
    Component_8_Flow_Rate: str
    Component_8_Operation_Type: str
    Component_9_Object_Type: str
    Component_9_Name: str
    Component_9_Demand_Calculation_Node_Name: str
    Component_9_Setpoint_Node_Name: str
    Component_9_Flow_Rate: str
    Component_9_Operation_Type: str
    Component_10_Object_Type: str
    Component_10_Name: str
    Component_10_Demand_Calculation_Node_Name: str
    Component_10_Setpoint_Node_Name: str
    Component_10_Flow_Rate: str
    Component_10_Operation_Type: str

class PlantequipmentoperationUncontrolledType(TypedDict, total=False):
    """"dict for PlantequipmentoperationUncontrolled"""
    Name: str
    Equipment_List_Name: str

class PlantequipmentoperationUserdefinedType(TypedDict, total=False):
    """"dict for PlantequipmentoperationUserdefined"""
    Name: str
    Main_Model_Program_Calling_Manager_Name: str
    Initialization_Program_Calling_Manager_Name: str
    Equipment_1_Object_Type: str
    Equipment_1_Name: str
    Equipment_2_Object_Type: str
    Equipment_2_Name: str
    Equipment_3_Object_Type: str
    Equipment_3_Name: str
    Equipment_4_Object_Type: str
    Equipment_4_Name: str
    Equipment_5_Object_Type: str
    Equipment_5_Name: str
    Equipment_6_Object_Type: str
    Equipment_6_Name: str
    Equipment_7_Object_Type: str
    Equipment_7_Name: str
    Equipment_8_Object_Type: str
    Equipment_8_Name: str
    Equipment_9_Object_Type: str
    Equipment_9_Name: str
    Equipment_10_Object_Type: str
    Equipment_10_Name: str

class PlantequipmentoperationschemesType(TypedDict, total=False):
    """"dict for Plantequipmentoperationschemes"""
    Name: str
    Control_Scheme_1_Object_Type: str
    Control_Scheme_1_Name: str
    Control_Scheme_1_Schedule_Name: str
    Control_Scheme_2_Object_Type: str
    Control_Scheme_2_Name: str
    Control_Scheme_2_Schedule_Name: str
    Control_Scheme_3_Object_Type: str
    Control_Scheme_3_Name: str
    Control_Scheme_3_Schedule_Name: str
    Control_Scheme_4_Object_Type: str
    Control_Scheme_4_Name: str
    Control_Scheme_4_Schedule_Name: str
    Control_Scheme_5_Object_Type: str
    Control_Scheme_5_Name: str
    Control_Scheme_5_Schedule_Name: str
    Control_Scheme_6_Object_Type: str
    Control_Scheme_6_Name: str
    Control_Scheme_6_Schedule_Name: str
    Control_Scheme_7_Object_Type: str
    Control_Scheme_7_Name: str
    Control_Scheme_7_Schedule_Name: str
    Control_Scheme_8_Object_Type: str
    Control_Scheme_8_Name: str
    Control_Scheme_8_Schedule_Name: str

class PlantloopType(TypedDict, total=False):
    """"dict for Plantloop"""
    Name: str
    Fluid_Type: str
    User_Defined_Fluid_Type: str
    Plant_Equipment_Operation_Scheme_Name: str
    Loop_Temperature_Setpoint_Node_Name: str
    Maximum_Loop_Temperature: str
    Minimum_Loop_Temperature: str
    Maximum_Loop_Flow_Rate: str
    Minimum_Loop_Flow_Rate: str
    Plant_Loop_Volume: str
    Plant_Side_Inlet_Node_Name: str
    Plant_Side_Outlet_Node_Name: str
    Plant_Side_Branch_List_Name: str
    Plant_Side_Connector_List_Name: str
    Demand_Side_Inlet_Node_Name: str
    Demand_Side_Outlet_Node_Name: str
    Demand_Side_Branch_List_Name: str
    Demand_Side_Connector_List_Name: str
    Load_Distribution_Scheme: str
    Availability_Manager_List_Name: str
    Plant_Loop_Demand_Calculation_Scheme: str
    Common_Pipe_Simulation: str
    Pressure_Simulation_Type: str
    Loop_Circulation_Time: str

class PumpConstantspeedType(TypedDict, total=False):
    """"dict for PumpConstantspeed"""
    Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str
    Design_Flow_Rate: str
    Design_Pump_Head: str
    Design_Power_Consumption: str
    Motor_Efficiency: str
    Fraction_of_Motor_Inefficiencies_to_Fluid_Stream: str
    Pump_Control_Type: str
    Pump_Flow_Rate_Schedule_Name: str
    Pump_Curve_Name: str
    Impeller_Diameter: str
    Rotational_Speed: str
    Zone_Name: str
    Skin_Loss_Radiative_Fraction: str
    Design_Power_Sizing_Method: str
    Design_Electric_Power_per_Unit_Flow_Rate: str
    Design_Shaft_Power_per_Unit_Flow_Rate_per_Unit_Head: str
    EndUse_Subcategory: str

class PumpVariablespeedType(TypedDict, total=False):
    """"dict for PumpVariablespeed"""
    Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str
    Design_Maximum_Flow_Rate: str
    Design_Pump_Head: str
    Design_Power_Consumption: str
    Motor_Efficiency: str
    Fraction_of_Motor_Inefficiencies_to_Fluid_Stream: str
    Coefficient_1_of_the_Part_Load_Performance_Curve: str
    Coefficient_2_of_the_Part_Load_Performance_Curve: str
    Coefficient_3_of_the_Part_Load_Performance_Curve: str
    Coefficient_4_of_the_Part_Load_Performance_Curve: str
    Design_Minimum_Flow_Rate: str
    Pump_Control_Type: str
    Pump_Flow_Rate_Schedule_Name: str
    Pump_Curve_Name: str
    Impeller_Diameter: str
    VFD_Control_Type: str
    Pump_RPM_Schedule_Name: str
    Minimum_Pressure_Schedule: str
    Maximum_Pressure_Schedule: str
    Minimum_RPM_Schedule: str
    Maximum_RPM_Schedule: str
    Zone_Name: str
    Skin_Loss_Radiative_Fraction: str
    Design_Power_Sizing_Method: str
    Design_Electric_Power_per_Unit_Flow_Rate: str
    Design_Shaft_Power_per_Unit_Flow_Rate_per_Unit_Head: str
    Design_Minimum_Flow_Rate_Fraction: str
    EndUse_Subcategory: str

class PumpVariablespeedCondensateType(TypedDict, total=False):
    """"dict for PumpVariablespeedCondensate"""
    Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str
    Design_Steam_Volume_Flow_Rate: str
    Design_Pump_Head: str
    Design_Power_Consumption: str
    Motor_Efficiency: str
    Fraction_of_Motor_Inefficiencies_to_Fluid_Stream: str
    Coefficient_1_of_the_Part_Load_Performance_Curve: str
    Coefficient_2_of_the_Part_Load_Performance_Curve: str
    Coefficient_3_of_the_Part_Load_Performance_Curve: str
    Coefficient_4_of_the_Part_Load_Performance_Curve: str
    Pump_Flow_Rate_Schedule_Name: str
    Zone_Name: str
    Skin_Loss_Radiative_Fraction: str
    Design_Power_Sizing_Method: str
    Design_Electric_Power_per_Unit_Flow_Rate: str
    Design_Shaft_Power_per_Unit_Flow_Rate_per_Unit_Head: str
    EndUse_Subcategory: str

class PythonpluginInstanceType(TypedDict, total=False):
    """"dict for PythonpluginInstance"""
    Name: str
    Run_During_Warmup_Days: str
    Python_Module_Name: str
    Plugin_Class_Name: str

class PythonpluginOutputvariableType(TypedDict, total=False):
    """"dict for PythonpluginOutputvariable"""
    Name: str
    Python_Plugin_Variable_Name: str
    Type_of_Data_in_Variable: str
    Update_Frequency: str
    Units: str
    Resource_Type: str
    Group_Type: str
    EndUse_Category: str
    EndUse_Subcategory: str

class PythonpluginSearchpathsType(TypedDict, total=False):
    """"dict for PythonpluginSearchpaths"""
    Name: str
    Add_Current_Working_Directory_to_Search_Path: str
    Add_Input_File_Directory_to_Search_Path: str
    Add_epin_Environment_Variable_to_Search_Path: str
    Search_Path_1: str
    Search_Path_2: str
    Search_Path_3: str
    Search_Path_4: str
    Search_Path_5: str
    Search_Path_6: str
    Search_Path_7: str
    Search_Path_8: str
    Search_Path_9: str
    Search_Path_10: str

class PythonpluginTrendvariableType(TypedDict, total=False):
    """"dict for PythonpluginTrendvariable"""
    Name: str
    Name_of_a_Python_Plugin_Variable: str
    Number_of_Timesteps_to_be_Logged: str

class PythonpluginVariablesType(TypedDict, total=False):
    """"dict for PythonpluginVariables"""
    Name: str
    Variable_Name_1: str
    Variable_Name_2: str
    Variable_Name_3: str
    Variable_Name_4: str
    Variable_Name_5: str
    Variable_Name_6: str
    Variable_Name_7: str
    Variable_Name_8: str
    Variable_Name_9: str
    Variable_Name_10: str

class RefrigerationAirchillerType(TypedDict, total=False):
    """"dict for RefrigerationAirchiller"""
    Name: str
    Availability_Schedule_Name: str
    Capacity_Rating_Type: str
    Rated_Unit_Load_Factor: str
    Rated_Capacity: str
    Rated_Relative_Humidity: str
    Rated_Cooling_Source_Temperature: str
    Rated_Temperature_Difference_DT1: str
    Maximum_Temperature_Difference_Between_Inlet_Air_and_Evaporating_Temperature: str
    Coil_Material_Correction_Factor: str
    Refrigerant_Correction_Factor: str
    Capacity_Correction_Curve_Type: str
    Capacity_Correction_Curve_Name: str
    SHR60_Correction_Factor: str
    Rated_Total_Heating_Power: str
    Heating_Power_Schedule_Name: str
    Fan_Speed_Control_Type: str
    Rated_Fan_Power: str
    Rated_Air_Flow: str
    Minimum_Fan_Air_Flow_Ratio: str
    Defrost_Type: str
    Defrost_Control_Type: str
    Defrost_Schedule_Name: str
    Defrost_DripDown_Schedule_Name: str
    Defrost_Power: str
    Temperature_Termination_Defrost_Fraction_to_Ice: str
    Vertical_Location: str
    Average_Refrigerant_Charge_Inventory: str

class RefrigerationCaseType(TypedDict, total=False):
    """"dict for RefrigerationCase"""
    Name: str
    Availability_Schedule_Name: str
    Zone_Name: str
    Rated_Ambient_Temperature: str
    Rated_Ambient_Relative_Humidity: str
    Rated_Total_Cooling_Capacity_per_Unit_Length: str
    Rated_Latent_Heat_Ratio: str
    Rated_Runtime_Fraction: str
    Case_Length: str
    Case_Operating_Temperature: str
    Latent_Case_Credit_Curve_Type: str
    Latent_Case_Credit_Curve_Name: str
    Standard_Case_Fan_Power_per_Unit_Length: str
    Operating_Case_Fan_Power_per_Unit_Length: str
    Standard_Case_Lighting_Power_per_Unit_Length: str
    Installed_Case_Lighting_Power_per_Unit_Length: str
    Case_Lighting_Schedule_Name: str
    Fraction_of_Lighting_Energy_to_Case: str
    Case_AntiSweat_Heater_Power_per_Unit_Length: str
    Minimum_AntiSweat_Heater_Power_per_Unit_Length: str
    AntiSweat_Heater_Control_Type: str
    Humidity_at_Zero_AntiSweat_Heater_Energy: str
    Case_Height: str
    Fraction_of_AntiSweat_Heater_Energy_to_Case: str
    Case_Defrost_Power_per_Unit_Length: str
    Case_Defrost_Type: str
    Case_Defrost_Schedule_Name: str
    Case_Defrost_DripDown_Schedule_Name: str
    Defrost_Energy_Correction_Curve_Type: str
    Defrost_Energy_Correction_Curve_Name: str
    Under_Case_HVAC_Return_Air_Fraction: str
    Refrigerated_Case_Restocking_Schedule_Name: str
    Case_Credit_Fraction_Schedule_Name: str
    Design_Evaporator_Temperature_or_Brine_Inlet_Temperature: str
    Average_Refrigerant_Charge_Inventory: str
    Under_Case_HVAC_Return_Air_Node_Name: str

class RefrigerationCaseandwalkinlistType(TypedDict, total=False):
    """"dict for RefrigerationCaseandwalkinlist"""
    Name: str
    Case_or_WalkIn_1_Name: str
    Case_or_WalkIn_2_Name: str
    Case_or_WalkIn_3_Name: str
    Case_or_WalkIn_4_Name: str
    Case_or_WalkIn_5_Name: str
    Case_or_WalkIn_6_Name: str
    Case_or_WalkIn_7_Name: str
    Case_or_WalkIn_8_Name: str
    Case_or_WalkIn_9_Name: str
    Case_or_WalkIn_10_Name: str
    Case_or_WalkIn_11_Name: str
    Case_or_WalkIn_12_Name: str
    Case_or_WalkIn_13_Name: str
    Case_or_WalkIn_14_Name: str
    Case_or_WalkIn_15_Name: str
    Case_or_WalkIn_16_Name: str
    Case_or_WalkIn_17_Name: str
    Case_or_WalkIn_18_Name: str
    Case_or_WalkIn_19_Name: str
    Case_or_WalkIn_20_Name: str
    Case_or_WalkIn_21_Name: str
    Case_or_WalkIn_22_Name: str
    Case_or_WalkIn_23_Name: str
    Case_or_WalkIn_24_Name: str
    Case_or_WalkIn_25_Name: str
    Case_or_WalkIn_26_Name: str
    Case_or_WalkIn_27_Name: str
    Case_or_WalkIn_28_Name: str
    Case_or_WalkIn_29_Name: str
    Case_or_WalkIn_30_Name: str
    Case_or_WalkIn_31_Name: str
    Case_or_WalkIn_32_Name: str
    Case_or_WalkIn_33_Name: str
    Case_or_WalkIn_34_Name: str
    Case_or_WalkIn_35_Name: str
    Case_or_WalkIn_36_Name: str
    Case_or_WalkIn_37_Name: str
    Case_or_WalkIn_38_Name: str
    Case_or_WalkIn_39_Name: str
    Case_or_WalkIn_40_Name: str

class RefrigerationCompressorType(TypedDict, total=False):
    """"dict for RefrigerationCompressor"""
    Name: str
    Refrigeration_Compressor_Power_Curve_Name: str
    Refrigeration_Compressor_Capacity_Curve_Name: str
    Rated_Superheat: str
    Rated_Return_Gas_Temperature: str
    Rated_Liquid_Temperature: str
    Rated_Subcooling: str
    EndUse_Subcategory: str
    Mode_of_Operation: str
    Transcritical_Compressor_Power_Curve_Name: str
    Transcritical_Compressor_Capacity_Curve_Name: str

class RefrigerationCompressorlistType(TypedDict, total=False):
    """"dict for RefrigerationCompressorlist"""
    Name: str
    Refrigeration_Compressor_1_Name: str
    Refrigeration_Compressor_2_Name: str
    Refrigeration_Compressor_3_Name: str
    Refrigeration_Compressor_4_Name: str
    Refrigeration_Compressor_5_Name: str
    Refrigeration_Compressor_6_Name: str
    Refrigeration_Compressor_7_Name: str
    Refrigeration_Compressor_8_Name: str
    Refrigeration_Compressor_9_Name: str
    Refrigeration_Compressor_10_Name: str
    Refrigeration_Compressor_11_Name: str
    Refrigeration_Compressor_12_Name: str
    Refrigeration_Compressor_13_Name: str
    Refrigeration_Compressor_14_Name: str
    Refrigeration_Compressor_15_Name: str
    Refrigeration_Compressor_16_Name: str
    Refrigeration_Compressor_17_Name: str
    Refrigeration_Compressor_18_Name: str
    Refrigeration_Compressor_19_Name: str
    Refrigeration_Compressor_20_Name: str
    Refrigeration_Compressor_21_Name: str
    Refrigeration_Compressor_22_Name: str
    Refrigeration_Compressor_23_Name: str
    Refrigeration_Compressor_24_Name: str
    Refrigeration_Compressor_25_Name: str
    Refrigeration_Compressor_26_Name: str
    Refrigeration_Compressor_27_Name: str
    Refrigeration_Compressor_28_Name: str
    Refrigeration_Compressor_29_Name: str
    Refrigeration_Compressor_30_Name: str
    Refrigeration_Compressor_31_Name: str
    Refrigeration_Compressor_32_Name: str
    Refrigeration_Compressor_33_Name: str
    Refrigeration_Compressor_34_Name: str
    Refrigeration_Compressor_35_Name: str
    Refrigeration_Compressor_36_Name: str
    Refrigeration_Compressor_37_Name: str
    Refrigeration_Compressor_38_Name: str
    Refrigeration_Compressor_39_Name: str
    Refrigeration_Compressor_40_Name: str

class RefrigerationCompressorrackType(TypedDict, total=False):
    """"dict for RefrigerationCompressorrack"""
    Name: str
    Heat_Rejection_Location: str
    Design_Compressor_Rack_COP: str
    Compressor_Rack_COP_Function_of_Temperature_Curve_Name: str
    Design_Condenser_Fan_Power: str
    Condenser_Fan_Power_Function_of_Temperature_Curve_Name: str
    Condenser_Type: str
    WaterCooled_Condenser_Inlet_Node_Name: str
    WaterCooled_Condenser_Outlet_Node_Name: str
    WaterCooled_Loop_Flow_Type: str
    WaterCooled_Condenser_Outlet_Temperature_Schedule_Name: str
    WaterCooled_Condenser_Design_Flow_Rate: str
    WaterCooled_Condenser_Maximum_Flow_Rate: str
    WaterCooled_Condenser_Maximum_Water_Outlet_Temperature: str
    WaterCooled_Condenser_Minimum_Water_Inlet_Temperature: str
    Evaporative_Condenser_Availability_Schedule_Name: str
    Evaporative_Condenser_Effectiveness: str
    Evaporative_Condenser_Air_Flow_Rate: str
    Basin_Heater_Capacity: str
    Basin_Heater_Setpoint_Temperature: str
    Design_Evaporative_Condenser_Water_Pump_Power: str
    Evaporative_Water_Supply_Tank_Name: str
    Condenser_Air_Inlet_Node_Name: str
    EndUse_Subcategory: str
    Refrigeration_Case_Name_or_WalkIn_Name_or_CaseAndWalkInList_Name: str
    Heat_Rejection_Zone_Name: str

class RefrigerationCondenserAircooledType(TypedDict, total=False):
    """"dict for RefrigerationCondenserAircooled"""
    Name: str
    Rated_Effective_Total_Heat_Rejection_Rate_Curve_Name: str
    Rated_Subcooling_Temperature_Difference: str
    Condenser_Fan_Speed_Control_Type: str
    Rated_Fan_Power: str
    Minimum_Fan_Air_Flow_Ratio: str
    Air_Inlet_Node_Name_or_Zone_Name: str
    EndUse_Subcategory: str
    Condenser_Refrigerant_Operating_Charge_Inventory: str
    Condensate_Receiver_Refrigerant_Inventory: str
    Condensate_Piping_Refrigerant_Inventory: str

class RefrigerationCondenserCascadeType(TypedDict, total=False):
    """"dict for RefrigerationCondenserCascade"""
    Name: str
    Rated_Condensing_Temperature: str
    Rated_Approach_Temperature_Difference: str
    Rated_Effective_Total_Heat_Rejection_Rate: str
    Condensing_Temperature_Control_Type: str
    Condenser_Refrigerant_Operating_Charge_Inventory: str
    Condensate_Receiver_Refrigerant_Inventory: str
    Condensate_Piping_Refrigerant_Inventory: str

class RefrigerationCondenserEvaporativecooledType(TypedDict, total=False):
    """"dict for RefrigerationCondenserEvaporativecooled"""
    Name: str
    Rated_Effective_Total_Heat_Rejection_Rate: str
    Rated_Subcooling_Temperature_Difference: str
    Fan_Speed_Control_Type: str
    Rated_Fan_Power: str
    Minimum_Fan_Air_Flow_Ratio: str
    Approach_Temperature_Constant_Term: str
    Approach_Temperature_Coefficient_2: str
    Approach_Temperature_Coefficient_3: str
    Approach_Temperature_Coefficient_4: str
    Minimum_Capacity_Factor: str
    Maximum_Capacity_Factor: str
    Air_Inlet_Node_Name: str
    Rated_Air_Flow_Rate: str
    Basin_Heater_Capacity: str
    Basin_Heater_Setpoint_Temperature: str
    Rated_Water_Pump_Power: str
    Evaporative_Water_Supply_Tank_Name: str
    Evaporative_Condenser_Availability_Schedule_Name: str
    EndUse_Subcategory: str
    Condenser_Refrigerant_Operating_Charge_Inventory: str
    Condensate_Receiver_Refrigerant_Inventory: str
    Condensate_Piping_Refrigerant_Inventory: str

class RefrigerationCondenserWatercooledType(TypedDict, total=False):
    """"dict for RefrigerationCondenserWatercooled"""
    Name: str
    Rated_Effective_Total_Heat_Rejection_Rate: str
    Rated_Condensing_Temperature: str
    Rated_Subcooling_Temperature_Difference: str
    Rated_Water_Inlet_Temperature: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    WaterCooled_Loop_Flow_Type: str
    Water_Outlet_Temperature_Schedule_Name: str
    Water_Design_Flow_Rate: str
    Water_Maximum_Flow_Rate: str
    Water_Maximum_Water_Outlet_Temperature: str
    Water_Minimum_Water_Inlet_Temperature: str
    EndUse_Subcategory: str
    Condenser_Refrigerant_Operating_Charge_Inventory: str
    Condensate_Receiver_Refrigerant_Inventory: str
    Condensate_Piping_Refrigerant_Inventory: str

class RefrigerationGascoolerAircooledType(TypedDict, total=False):
    """"dict for RefrigerationGascoolerAircooled"""
    Name: str
    Rated_Total_Heat_Rejection_Rate_Curve_Name: str
    Gas_Cooler_Fan_Speed_Control_Type: str
    Rated_Fan_Power: str
    Minimum_Fan_Air_Flow_Ratio: str
    Transition_Temperature: str
    Transcritical_Approach_Temperature: str
    Subcritical_Temperature_Difference: str
    Minimum_Condensing_Temperature: str
    Air_Inlet_Node_Name: str
    EndUse_Subcategory: str
    Gas_Cooler_Refrigerant_Operating_Charge_Inventory: str
    Gas_Cooler_Receiver_Refrigerant_Inventory: str
    Gas_Cooler_Outlet_Piping_Refrigerant_Inventory: str

class RefrigerationSecondarysystemType(TypedDict, total=False):
    """"dict for RefrigerationSecondarysystem"""
    Name: str
    Refrigerated_Case_or_Walkin_or_CaseAndWalkInList_Name: str
    Circulating_Fluid_Type: str
    Circulating_Fluid_Name: str
    Evaporator_Capacity: str
    Evaporator_Flow_Rate_for_Secondary_Fluid: str
    Evaporator_Evaporating_Temperature: str
    Evaporator_Approach_Temperature_Difference: str
    Evaporator_Range_Temperature_Difference: str
    Number_of_Pumps_in_Loop: str
    Total_Pump_Flow_Rate: str
    Total_Pump_Power: str
    Total_Pump_Head: str
    PhaseChange_Circulating_Rate: str
    Pump_Drive_Type: str
    Variable_Speed_Pump_Cubic_Curve_Name: str
    Pump_Motor_Heat_to_Fluid: str
    Sum_UA_Distribution_Piping: str
    Distribution_Piping_Zone_Name: str
    Sum_UA_ReceiverSeparator_Shell: str
    ReceiverSeparator_Zone_Name: str
    Evaporator_Refrigerant_Inventory: str
    EndUse_Subcategory: str

class RefrigerationSubcoolerType(TypedDict, total=False):
    """"dict for RefrigerationSubcooler"""
    Name: str
    Subcooler_Type: str
    Liquid_Suction_Design_Subcooling_Temperature_Difference: str
    Design_Liquid_Inlet_Temperature: str
    Design_Vapor_Inlet_Temperature: str
    CapacityProviding_System: str
    Outlet_Control_Temperature: str

class RefrigerationSystemType(TypedDict, total=False):
    """"dict for RefrigerationSystem"""
    Name: str
    Refrigerated_Case_or_Walkin_or_CaseAndWalkInList_Name: str
    Refrigeration_Transfer_Load_or_TransferLoad_List_Name: str
    Refrigeration_Condenser_Name: str
    Compressor_or_CompressorList_Name: str
    Minimum_Condensing_Temperature: str
    Refrigeration_System_Working_Fluid_Type: str
    Suction_Temperature_Control_Type: str
    Mechanical_Subcooler_Name: str
    Liquid_Suction_Heat_Exchanger_Subcooler_Name: str
    Sum_UA_Suction_Piping: str
    Suction_Piping_Zone_Name: str
    EndUse_Subcategory: str
    Number_of_Compressor_Stages: str
    Intercooler_Type: str
    ShellandCoil_Intercooler_Effectiveness: str
    HighStage_Compressor_or_CompressorList_Name: str

class RefrigerationTranscriticalsystemType(TypedDict, total=False):
    """"dict for RefrigerationTranscriticalsystem"""
    Name: str
    System_Type: str
    Medium_Temperature_Refrigerated_Case_or_Walkin_or_CaseAndWalkInList_Name: str
    Low_Temperature_Refrigerated_Case_or_Walkin_or_CaseAndWalkInList_Name: str
    Refrigeration_Gas_Cooler_Name: str
    High_Pressure_Compressor_or_CompressorList_Name: str
    Low_Pressure_Compressor_or_CompressorList_Name: str
    Receiver_Pressure: str
    Subcooler_Effectiveness: str
    Refrigeration_System_Working_Fluid_Type: str
    Sum_UA_Suction_Piping_for_Medium_Temperature_Loads: str
    Medium_Temperature_Suction_Piping_Zone_Name: str
    Sum_UA_Suction_Piping_for_Low_Temperature_Loads: str
    Low_Temperature_Suction_Piping_Zone_Name: str
    EndUse_Subcategory: str

class RefrigerationTransferloadlistType(TypedDict, total=False):
    """"dict for RefrigerationTransferloadlist"""
    Name: str
    Cascade_Condenser_Name_or_Secondary_System_1_Name: str
    Cascade_Condenser_Name_or_Secondary_System_2_Name: str
    Cascade_Condenser_Name_or_Secondary_System_3_Name: str
    Cascade_Condenser_Name_or_Secondary_System_4_Name: str
    Cascade_Condenser_Name_or_Secondary_System_5_Name: str
    Cascade_Condenser_Name_or_Secondary_System_6_Name: str
    Cascade_Condenser_Name_or_Secondary_System_7_Name: str
    Cascade_Condenser_Name_or_Secondary_System_8_Name: str
    Cascade_Condenser_Name_or_Secondary_System_9_Name: str

class RefrigerationWalkinType(TypedDict, total=False):
    """"dict for RefrigerationWalkin"""
    Name: str
    Availability_Schedule_Name: str
    Rated_Coil_Cooling_Capacity: str
    Operating_Temperature: str
    Rated_Cooling_Source_Temperature: str
    Rated_Total_Heating_Power: str
    Heating_Power_Schedule_Name: str
    Rated_Cooling_Coil_Fan_Power: str
    Rated_Circulation_Fan_Power: str
    Rated_Total_Lighting_Power: str
    Lighting_Schedule_Name: str
    Defrost_Type: str
    Defrost_Control_Type: str
    Defrost_Schedule_Name: str
    Defrost_DripDown_Schedule_Name: str
    Defrost_Power: str
    Temperature_Termination_Defrost_Fraction_to_Ice: str
    Restocking_Schedule_Name: str
    Average_Refrigerant_Charge_Inventory: str
    Insulated_Floor_Surface_Area: str
    Insulated_Floor_UValue: str
    Zone_1_Name: str
    Total_Insulated_Surface_Area_Facing_Zone_1: str
    Insulated_Surface_UValue_Facing_Zone_1: str
    Area_of_Glass_Reach_In_Doors_Facing_Zone_1: str
    Height_of_Glass_Reach_In_Doors_Facing_Zone_1: str
    Glass_Reach_In_Door_U_Value_Facing_Zone_1: str
    Glass_Reach_In_Door_Opening_Schedule_Name_Facing_Zone_1: str
    Area_of_Stocking_Doors_Facing_Zone_1: str
    Height_of_Stocking_Doors_Facing_Zone_1: str
    Stocking_Door_U_Value_Facing_Zone_1: str
    Stocking_Door_Opening_Schedule_Name_Facing_Zone_1: str
    Stocking_Door_Opening_Protection_Type_Facing_Zone_1: str
    Zone_2_Name: str
    Total_Insulated_Surface_Area_Facing_Zone_2: str
    Insulated_Surface_UValue_Facing_Zone_2: str
    Area_of_Glass_Reach_In_Doors_Facing_Zone_2: str
    Height_of_Glass_Reach_In_Doors_Facing_Zone_2: str
    Glass_Reach_In_Door_U_Value_Facing_Zone_2: str
    Glass_Reach_In_Door_Opening_Schedule_Name_Facing_Zone_2: str
    Area_of_Stocking_Doors_Facing_Zone_2: str
    Height_of_Stocking_Doors_Facing_Zone_2: str
    Stocking_Door_U_Value_Facing_Zone_2: str
    Stocking_Door_Opening_Schedule_Name_Facing_Zone_2: str
    Stocking_Door_Opening_Protection_Type_Facing_Zone_2: str
    Zone_3_Name: str
    Total_Insulated_Surface_Area_Facing_Zone_3: str
    Insulated_Surface_UValue_Facing_Zone_3: str
    Area_of_Glass_Reach_In_Doors_Facing_Zone_3: str
    Height_of_Glass_Reach_In_Doors_Facing_Zone_3: str
    Glass_Reach_In_Door_U_Value_Facing_Zone_3: str
    Glass_Reach_In_Door_Opening_Schedule_Name_Facing_Zone_3: str
    Area_of_Stocking_Doors_Facing_Zone_3: str
    Height_of_Stocking_Doors_Facing_Zone_3: str
    Stocking_Door_U_Value_Facing_Zone_3: str
    Stocking_Door_Opening_Schedule_Name_Facing_Zone_3: str
    Stocking_Door_Opening_Protection_Type_Facing_Zone_3: str

class RoofType(TypedDict, total=False):
    """"dict for Roof"""
    Name: str
    Construction_Name: str
    Zone_Name: str
    Space_Name: str
    Azimuth_Angle: str
    Tilt_Angle: str
    Starting_X_Coordinate: str
    Starting_Y_Coordinate: str
    Starting_Z_Coordinate: str
    Length: str
    Width: str

class RoofceilingDetailedType(TypedDict, total=False):
    """"dict for RoofceilingDetailed"""
    Name: str
    Construction_Name: str
    Zone_Name: str
    Space_Name: str
    Outside_Boundary_Condition: str
    Outside_Boundary_Condition_Object: str
    Sun_Exposure: str
    Wind_Exposure: str
    View_Factor_to_Ground: str
    Number_of_Vertices: str
    Vertex_1_Xcoordinate: str
    Vertex_1_Ycoordinate: str
    Vertex_1_Zcoordinate: str
    Vertex_2_Xcoordinate: str
    Vertex_2_Ycoordinate: str
    Vertex_2_Zcoordinate: str
    Vertex_3_Xcoordinate: str
    Vertex_3_Ycoordinate: str
    Vertex_3_Zcoordinate: str
    Vertex_4_Xcoordinate: str
    Vertex_4_Ycoordinate: str
    Vertex_4_Zcoordinate: str
    Vertex_5_Xcoordinate: str
    Vertex_5_Ycoordinate: str
    Vertex_5_Zcoordinate: str
    Vertex_6_Xcoordinate: str
    Vertex_6_Ycoordinate: str
    Vertex_6_Zcoordinate: str
    Vertex_7_Xcoordinate: str
    Vertex_7_Ycoordinate: str
    Vertex_7_Zcoordinate: str
    Vertex_8_Xcoordinate: str
    Vertex_8_Ycoordinate: str
    Vertex_8_Zcoordinate: str
    Vertex_9_Xcoordinate: str
    Vertex_9_Ycoordinate: str
    Vertex_9_Zcoordinate: str
    Vertex_10_Xcoordinate: str
    Vertex_10_Ycoordinate: str
    Vertex_10_Zcoordinate: str

class RoofirrigationType(TypedDict, total=False):
    """"dict for Roofirrigation"""
    Irrigation_Model_Type: str
    Irrigation_Rate_Schedule_Name: str
    Irrigation_Maximum_Saturation_Threshold: str

class RoomairNodeType(TypedDict, total=False):
    """"dict for RoomairNode"""
    Name: str
    Node_Type: str
    Zone_Name: str
    Height_of_Nodal_Control_Volume_Center: str
    Surface_1_Name: str
    Surface_2_Name: str
    Surface_3_Name: str
    Surface_4_Name: str
    Surface_5_Name: str
    Surface_6_Name: str
    Surface_7_Name: str
    Surface_8_Name: str
    Surface_9_Name: str
    Surface_10_Name: str
    Surface_11_Name: str
    Surface_12_Name: str
    Surface_13_Name: str
    Surface_14_Name: str
    Surface_15_Name: str
    Surface_16_Name: str
    Surface_17_Name: str
    Surface_18_Name: str
    Surface_19_Name: str
    Surface_20_Name: str
    Surface_21_Name: str

class RoomairNodeAirflownetworkType(TypedDict, total=False):
    """"dict for RoomairNodeAirflownetwork"""
    Name: str
    Zone_Name: str
    Fraction_of_Zone_Air_Volume: str
    RoomAirNodeAirflowNetworkAdjacentSurfaceList_Name: str
    RoomAirNodeAirflowNetworkInternalGains_Name: str
    RoomAirNodeAirflowNetworkHVACEquipment_Name: str

class RoomairNodeAirflownetworkAdjacentsurfacelistType(TypedDict, total=False):
    """"dict for RoomairNodeAirflownetworkAdjacentsurfacelist"""
    Name: str
    Surface_1_Name: str
    Surface_2_Name: str
    Surface_3_Name: str
    Surface_4_Name: str
    Surface_5_Name: str
    Surface_6_Name: str
    Surface_7_Name: str
    Surface_8_Name: str
    Surface_9_Name: str
    Surface_10_Name: str
    Surface_11_Name: str
    Surface_12_Name: str
    Surface_13_Name: str
    Surface_14_Name: str
    Surface_15_Name: str
    Surface_16_Name: str
    Surface_17_Name: str
    Surface_18_Name: str
    Surface_19_Name: str
    Surface_20_Name: str
    Surface_21_Name: str

class RoomairNodeAirflownetworkHvacequipmentType(TypedDict, total=False):
    """"dict for RoomairNodeAirflownetworkHvacequipment"""
    Name: str
    ZoneHVAC_or_Air_Terminal_Equipment_Object_Type_1: str
    ZoneHVAC_or_Air_Terminal_Equipment_Object_Name_1: str
    Fraction_of_Output_or_Supply_Air_from_HVAC_Equipment_1: str
    Fraction_of_Input_or_Return_Air_to_HVAC_Equipment_1: str
    ZoneHVAC_or_Air_Terminal_Equipment_Object_Type_2: str
    ZoneHVAC_or_Air_Terminal_Equipment_Object_Name_2: str
    Fraction_of_Output_or_Supply_Air_from_HVAC_Equipment_2: str
    Fraction_of_Input_or_Return_Air_to_HVAC_Equipment_2: str

class RoomairNodeAirflownetworkInternalgainsType(TypedDict, total=False):
    """"dict for RoomairNodeAirflownetworkInternalgains"""
    Name: str
    Internal_Gain_Object_1_Type: str
    Internal_Gain_Object_1_Name: str
    Fraction_of_Gains_to_Node_1: str
    Internal_Gain_Object_2_Type: str
    Internal_Gain_Object_2_Name: str
    Fraction_of_Gains_to_Node_2: str
    Internal_Gain_Object_3_Type: str
    Internal_Gain_Object_3_Name: str
    Fraction_of_Gains_to_Node_3: str

class RoomairTemperaturepatternConstantgradientType(TypedDict, total=False):
    """"dict for RoomairTemperaturepatternConstantgradient"""
    Room_Air_Temperature_Pattern_Constant_Gradient_Name: str
    Control_Integer_for_Pattern_Control_Schedule_Name: str
    Thermostat_Offset: str
    Return_Air_Offset: str
    Exhaust_Air_Offset: str
    Temperature_Gradient: str

class RoomairTemperaturepatternNondimensionalheightType(TypedDict, total=False):
    """"dict for RoomairTemperaturepatternNondimensionalheight"""
    Name: str
    Control_Integer_for_Pattern_Control_Schedule_Name: str
    Thermostat_Offset: str
    Return_Air_Offset: str
    Exhaust_Air_Offset: str
    Pair_1_Zeta_Nondimensional_Height: str
    Pair_1_Delta_Adjacent_Air_Temperature: str
    Pair_2_Zeta_Nondimensional_Height: str
    Pair_2_Delta_Adjacent_Air_Temperature: str
    Pair_3_Zeta_Nondimensional_Height: str
    Pair_3_Delta_Adjacent_Air_Temperature: str
    Pair_4_Zeta_Nondimensional_Height: str
    Pair_4_Delta_Adjacent_Air_Temperature: str
    Pair_5_Zeta_Nondimensional_Height: str
    Pair_5_Delta_Adjacent_Air_Temperature: str
    Pair_6_Zeta_Nondimensional_Height: str
    Pair_6_Delta_Adjacent_Air_Temperature: str
    Pair_7_Zeta_Nondimensional_Height: str
    Pair_7_Delta_Adjacent_Air_Temperature: str
    Pair_8_Zeta_Nondimensional_Height: str
    Pair_8_Delta_Adjacent_Air_Temperature: str
    Pair_9_Zeta_Nondimensional_Height: str
    Pair_9_Delta_Adjacent_Air_Temperature: str
    Pair_10_Zeta_Nondimensional_Height: str
    Pair_10_Delta_Adjacent_Air_Temperature: str
    Pair_11_Zeta_Nondimensional_Height: str
    Pair_11_Delta_Adjacent_Air_Temperature: str
    Pair_12_Zeta_Nondimensional_Height: str
    Pair_12_Delta_Adjacent_Air_Temperature: str
    Pair_13_Zeta_Nondimensional_Height: str
    Pair_13_Delta_Adjacent_Air_Temperature: str
    Pair_14_Zeta_Nondimensional_Height: str
    Pair_14_Delta_Adjacent_Air_Temperature: str
    Pair_15_Zeta_Nondimensional_Height: str
    Pair_15_Delta_Adjacent_Air_Temperature: str
    Pair_16_Zeta_Nondimensional_Height: str
    Pair_16_Delta_Adjacent_Air_Temperature: str
    Pair_17_Zeta_Nondimensional_Height: str
    Pair_17_Delta_Adjacent_Air_Temperature: str
    Pair_18_Zeta_Nondimensional_Height: str
    Pair_18_Delta_Adjacent_Air_Temperature: str
    Pair_19_Zeta_Nondimensional_Height: str
    Pair_19_Delta_Adjacent_Air_Temperature: str

class RoomairTemperaturepatternSurfacemappingType(TypedDict, total=False):
    """"dict for RoomairTemperaturepatternSurfacemapping"""
    Name: str
    Control_Integer_for_Pattern_Control_Schedule_Name: str
    Thermostat_Offset: str
    Return_Air_Offset: str
    Exhaust_Air_Offset: str
    Surface_Name_Pair_1: str
    Delta_Adjacent_Air_Temperature_Pair_1: str
    Surface_Name_Pair_2: str
    Delta_Adjacent_Air_Temperature_Pair_2: str
    Surface_Name_Pair_3: str
    Delta_Adjacent_Air_Temperature_Pair_3: str
    Surface_Name_Pair_4: str
    Delta_Adjacent_Air_Temperature_Pair_4: str
    Surface_Name_Pair_5: str
    Delta_Adjacent_Air_Temperature_Pair_5: str
    Surface_Name_Pair_6: str
    Delta_Adjacent_Air_Temperature_Pair_6: str
    Surface_Name_Pair_7: str
    Delta_Adjacent_Air_Temperature_Pair_7: str
    Surface_Name_Pair_8: str
    Delta_Adjacent_Air_Temperature_Pair_8: str
    Surface_Name_Pair_9: str
    Delta_Adjacent_Air_Temperature_Pair_9: str
    Surface_Name_Pair_10: str
    Delta_Adjacent_Air_Temperature_Pair_10: str
    Surface_Name_Pair_11: str
    Delta_Adjacent_Air_Temperature_Pair_11: str
    Surface_Name_Pair_12: str
    Delta_Adjacent_Air_Temperature_Pair_12: str
    Surface_Name_Pair_13: str
    Delta_Adjacent_Air_Temperature_Pair_13: str
    Surface_Name_Pair_14: str
    Delta_Adjacent_Air_Temperature_Pair_14: str
    Surface_Name_Pair_15: str
    Delta_Adjacent_Air_Temperature_Pair_15: str
    Surface_Name_Pair_16: str
    Delta_Adjacent_Air_Temperature_Pair_16: str
    Surface_Name_Pair_17: str
    Delta_Adjacent_Air_Temperature_Pair_17: str
    Surface_Name_Pair_18: str
    Delta_Adjacent_Air_Temperature_Pair_18: str
    Surface_Name_Pair_19: str
    Delta_Adjacent_Air_Temperature_Pair_19: str
    Surface_Name_Pair_20: str
    Delta_Adjacent_Air_Temperature_Pair_20: str
    Surface_Name_Pair_21: str
    Delta_Adjacent_Air_Temperature_Pair_21: str

class RoomairTemperaturepatternTwogradientType(TypedDict, total=False):
    """"dict for RoomairTemperaturepatternTwogradient"""
    Room_Air_Temperature_Pattern_Two_Gradient_Name: str
    Control_Integer_for_Pattern_Control_Schedule_Name: str
    Thermostat_Height: str
    Return_Air_Height: str
    Exhaust_Air_Height: str
    Temperature_Gradient_Lower_Bound: str
    Temperature_Gradient_Upper_Bound: str
    Gradient_Interpolation_Mode: str
    Upper_Temperature_Bound: str
    Lower_Temperature_Bound: str
    Upper_Heat_Rate_Bound: str
    Lower_Heat_Rate_Bound: str

class RoomairTemperaturepatternUserdefinedType(TypedDict, total=False):
    """"dict for RoomairTemperaturepatternUserdefined"""
    Name: str
    Zone_Name: str
    Availability_Schedule_Name: str
    Pattern_Control_Schedule_Name: str

class RoomairmodeltypeType(TypedDict, total=False):
    """"dict for Roomairmodeltype"""
    Name: str
    Zone_Name: str
    RoomAir_Modeling_Type: str
    Air_Temperature_Coupling_Strategy: str

class RoomairsettingsAirflownetworkType(TypedDict, total=False):
    """"dict for RoomairsettingsAirflownetwork"""
    Name: str
    Zone_Name: str
    Control_Point_RoomAirflowNetworkNode_Name: str
    RoomAirflowNetworkNode_Name_1: str
    RoomAirflowNetworkNode_Name_2: str
    RoomAirflowNetworkNode_Name_3: str
    RoomAirflowNetworkNode_Name_4: str
    RoomAirflowNetworkNode_Name_5: str
    RoomAirflowNetworkNode_Name_6: str

class RoomairsettingsCrossventilationType(TypedDict, total=False):
    """"dict for RoomairsettingsCrossventilation"""
    Zone_Name: str
    Gain_Distribution_Schedule_Name: str
    Airflow_Region_Used_for_Thermal_Comfort_Evaluation: str

class RoomairsettingsOnenodedisplacementventilationType(TypedDict, total=False):
    """"dict for RoomairsettingsOnenodedisplacementventilation"""
    Zone_Name: str
    Fraction_of_Convective_Internal_Loads_Added_to_Floor_Air: str
    Fraction_of_Infiltration_Internal_Loads_Added_to_Floor_Air: str

class RoomairsettingsThreenodedisplacementventilationType(TypedDict, total=False):
    """"dict for RoomairsettingsThreenodedisplacementventilation"""
    Zone_Name: str
    Gain_Distribution_Schedule_Name: str
    Number_of_Plumes_per_Occupant: str
    Thermostat_Height: str
    Comfort_Height: str
    Temperature_Difference_Threshold_for_Reporting: str

class RoomairsettingsUnderfloorairdistributionexteriorType(TypedDict, total=False):
    """"dict for RoomairsettingsUnderfloorairdistributionexterior"""
    Zone_Name: str
    Number_of_Diffusers_per_Zone: str
    Power_per_Plume: str
    Design_Effective_Area_of_Diffuser: str
    Diffuser_Slot_Angle_from_Vertical: str
    Thermostat_Height: str
    Comfort_Height: str
    Temperature_Difference_Threshold_for_Reporting: str
    Floor_Diffuser_Type: str
    Transition_Height: str
    Coefficient_A_in_formula_Kc__AGammaB__C__DGamma__EGamma2: str
    Coefficient_B_in_formula_Kc__AGammaB__C__DGamma__EGamma2: str
    Coefficient_C_in_formula_Kc__AGammaB__C__DGamma__EGamma2: str
    Coefficient_D_in_formula_Kc__AGammaB__C__DGamma__EGamma2: str
    Coefficient_E_in_formula_Kc__AGammaB__C__DGamma__EGamma2: str

class RoomairsettingsUnderfloorairdistributioninteriorType(TypedDict, total=False):
    """"dict for RoomairsettingsUnderfloorairdistributioninterior"""
    Zone_Name: str
    Number_of_Diffusers: str
    Power_per_Plume: str
    Design_Effective_Area_of_Diffuser: str
    Diffuser_Slot_Angle_from_Vertical: str
    Thermostat_Height: str
    Comfort_Height: str
    Temperature_Difference_Threshold_for_Reporting: str
    Floor_Diffuser_Type: str
    Transition_Height: str
    Coefficient_A: str
    Coefficient_B: str
    Coefficient_C: str
    Coefficient_D: str
    Coefficient_E: str

class RunperiodType(TypedDict, total=False):
    """"dict for Runperiod"""
    Name: str
    Begin_Month: str
    Begin_Day_of_Month: str
    Begin_Year: str
    End_Month: str
    End_Day_of_Month: str
    End_Year: str
    Day_of_Week_for_Start_Day: str
    Use_Weather_File_Holidays_and_Special_Days: str
    Use_Weather_File_Daylight_Saving_Period: str
    Apply_Weekend_Holiday_Rule: str
    Use_Weather_File_Rain_Indicators: str
    Use_Weather_File_Snow_Indicators: str
    Treat_Weather_as_Actual: str
    First_Hour_Interpolation_Starting_Values: str

class RunperiodcontrolDaylightsavingtimeType(TypedDict, total=False):
    """"dict for RunperiodcontrolDaylightsavingtime"""
    Start_Date: str
    End_Date: str

class RunperiodcontrolSpecialdaysType(TypedDict, total=False):
    """"dict for RunperiodcontrolSpecialdays"""
    Name: str
    Start_Date: str
    Duration: str
    Special_Day_Type: str

class ScheduleCompactType(TypedDict, total=False):
    """"dict for ScheduleCompact"""
    Name: str
    Schedule_Type_Limits_Name: str
    Field_1: str
    Field_2: str
    Field_3: str
    Field_4: str
    Field_5: str
    Field_6: str
    Field_7: str
    Field_8: str
    Field_9: str
    Field_10: str
    Field_11: str
    Field_12: str
    Field_13: str
    Field_14: str
    Field_15: str
    Field_16: str
    Field_17: str
    Field_18: str
    Field_19: str
    Field_20: str
    Field_21: str
    Field_22: str
    Field_23: str
    Field_24: str
    Field_25: str
    Field_26: str
    Field_27: str
    Field_28: str
    Field_29: str
    Field_30: str
    Field_31: str
    Field_32: str
    Field_33: str
    Field_34: str
    Field_35: str
    Field_36: str
    Field_37: str
    Field_38: str
    Field_39: str
    Field_40: str
    Field_41: str
    Field_42: str
    Field_43: str
    Field_44: str
    Field_45: str
    Field_46: str
    Field_47: str
    Field_48: str
    Field_49: str

class ScheduleConstantType(TypedDict, total=False):
    """"dict for ScheduleConstant"""
    Name: str
    Schedule_Type_Limits_Name: str
    Hourly_Value: str

class ScheduleDayHourlyType(TypedDict, total=False):
    """"dict for ScheduleDayHourly"""
    Name: str
    Schedule_Type_Limits_Name: str
    Hour_1: str
    Hour_2: str
    Hour_3: str
    Hour_4: str
    Hour_5: str
    Hour_6: str
    Hour_7: str
    Hour_8: str
    Hour_9: str
    Hour_10: str
    Hour_11: str
    Hour_12: str
    Hour_13: str
    Hour_14: str
    Hour_15: str
    Hour_16: str
    Hour_17: str
    Hour_18: str
    Hour_19: str
    Hour_20: str
    Hour_21: str
    Hour_22: str
    Hour_23: str
    Hour_24: str

class ScheduleDayIntervalType(TypedDict, total=False):
    """"dict for ScheduleDayInterval"""
    Name: str
    Schedule_Type_Limits_Name: str
    Interpolate_to_Timestep: str
    Time_1: str
    Value_Until_Time_1: str
    Time_2: str
    Value_Until_Time_2: str
    Time_3: str
    Value_Until_Time_3: str
    Time_4: str
    Value_Until_Time_4: str
    Time_5: str
    Value_Until_Time_5: str
    Time_6: str
    Value_Until_Time_6: str
    Time_7: str
    Value_Until_Time_7: str
    Time_8: str
    Value_Until_Time_8: str
    Time_9: str
    Value_Until_Time_9: str
    Time_10: str
    Value_Until_Time_10: str
    Time_11: str
    Value_Until_Time_11: str
    Time_12: str
    Value_Until_Time_12: str
    Time_13: str
    Value_Until_Time_13: str
    Time_14: str
    Value_Until_Time_14: str
    Time_15: str
    Value_Until_Time_15: str
    Time_16: str
    Value_Until_Time_16: str
    Time_17: str
    Value_Until_Time_17: str
    Time_18: str
    Value_Until_Time_18: str
    Time_19: str
    Value_Until_Time_19: str
    Time_20: str
    Value_Until_Time_20: str
    Time_21: str
    Value_Until_Time_21: str
    Time_22: str
    Value_Until_Time_22: str
    Time_23: str
    Value_Until_Time_23: str
    Time_24: str
    Value_Until_Time_24: str
    Time_25: str
    Value_Until_Time_25: str
    Time_26: str
    Value_Until_Time_26: str
    Time_27: str
    Value_Until_Time_27: str
    Time_28: str
    Value_Until_Time_28: str
    Time_29: str
    Value_Until_Time_29: str
    Time_30: str
    Value_Until_Time_30: str
    Time_31: str
    Value_Until_Time_31: str
    Time_32: str
    Value_Until_Time_32: str
    Time_33: str
    Value_Until_Time_33: str
    Time_34: str
    Value_Until_Time_34: str
    Time_35: str
    Value_Until_Time_35: str
    Time_36: str
    Value_Until_Time_36: str
    Time_37: str
    Value_Until_Time_37: str
    Time_38: str
    Value_Until_Time_38: str
    Time_39: str
    Value_Until_Time_39: str
    Time_40: str
    Value_Until_Time_40: str
    Time_41: str
    Value_Until_Time_41: str
    Time_42: str
    Value_Until_Time_42: str
    Time_43: str
    Value_Until_Time_43: str
    Time_44: str
    Value_Until_Time_44: str
    Time_45: str
    Value_Until_Time_45: str
    Time_46: str
    Value_Until_Time_46: str
    Time_47: str
    Value_Until_Time_47: str
    Time_48: str
    Value_Until_Time_48: str
    Time_49: str
    Value_Until_Time_49: str

class ScheduleDayListType(TypedDict, total=False):
    """"dict for ScheduleDayList"""
    Name: str
    Schedule_Type_Limits_Name: str
    Interpolate_to_Timestep: str
    Minutes_per_Item: str
    Value_1: str
    Value_2: str
    Value_3: str
    Value_4: str
    Value_5: str
    Value_6: str
    Value_7: str
    Value_8: str
    Value_9: str
    Value_10: str
    Value_11: str
    Value_12: str
    Value_13: str
    Value_14: str
    Value_15: str
    Value_16: str
    Value_17: str
    Value_18: str
    Value_19: str
    Value_20: str
    Value_21: str
    Value_22: str
    Value_23: str
    Value_24: str
    Value_25: str
    Value_26: str
    Value_27: str
    Value_28: str
    Value_29: str
    Value_30: str
    Value_31: str
    Value_32: str
    Value_33: str
    Value_34: str
    Value_35: str
    Value_36: str
    Value_37: str
    Value_38: str
    Value_39: str
    Value_40: str
    Value_41: str
    Value_42: str
    Value_43: str
    Value_44: str
    Value_45: str
    Value_46: str
    Value_47: str
    Value_48: str
    Value_49: str

class ScheduleFileType(TypedDict, total=False):
    """"dict for ScheduleFile"""
    Name: str
    Schedule_Type_Limits_Name: str
    File_Name: str
    Column_Number: str
    Rows_to_Skip_at_Top: str
    Number_of_Hours_of_Data: str
    Column_Separator: str
    Interpolate_to_Timestep: str
    Minutes_per_Item: str
    Adjust_Schedule_for_Daylight_Savings: str

class ScheduleFileShadingType(TypedDict, total=False):
    """"dict for ScheduleFileShading"""
    File_Name: str

class ScheduleWeekCompactType(TypedDict, total=False):
    """"dict for ScheduleWeekCompact"""
    Name: str
    DayType_List_1: str
    ScheduleDay_Name_1: str
    DayType_List_2: str
    ScheduleDay_Name_2: str
    DayType_List_3: str
    ScheduleDay_Name_3: str
    DayType_List_4: str
    ScheduleDay_Name_4: str
    DayType_List_5: str
    ScheduleDay_Name_5: str

class ScheduleWeekDailyType(TypedDict, total=False):
    """"dict for ScheduleWeekDaily"""
    Name: str
    Sunday_ScheduleDay_Name: str
    Monday_ScheduleDay_Name: str
    Tuesday_ScheduleDay_Name: str
    Wednesday_ScheduleDay_Name: str
    Thursday_ScheduleDay_Name: str
    Friday_ScheduleDay_Name: str
    Saturday_ScheduleDay_Name: str
    Holiday_ScheduleDay_Name: str
    SummerDesignDay_ScheduleDay_Name: str
    WinterDesignDay_ScheduleDay_Name: str
    CustomDay1_ScheduleDay_Name: str
    CustomDay2_ScheduleDay_Name: str

class ScheduleYearType(TypedDict, total=False):
    """"dict for ScheduleYear"""
    Name: str
    Schedule_Type_Limits_Name: str
    ScheduleWeek_Name_1: str
    Start_Month_1: str
    Start_Day_1: str
    End_Month_1: str
    End_Day_1: str
    ScheduleWeek_Name_2: str
    Start_Month_2: str
    Start_Day_2: str
    End_Month_2: str
    End_Day_2: str
    ScheduleWeek_Name_3: str
    Start_Month_3: str
    Start_Day_3: str
    End_Month_3: str
    End_Day_3: str
    ScheduleWeek_Name_4: str
    Start_Month_4: str
    Start_Day_4: str
    End_Month_4: str
    End_Day_4: str
    ScheduleWeek_Name_5: str
    Start_Month_5: str
    Start_Day_5: str
    End_Month_5: str
    End_Day_5: str
    ScheduleWeek_Name_6: str
    Start_Month_6: str
    Start_Day_6: str
    End_Month_6: str
    End_Day_6: str
    ScheduleWeek_Name_7: str
    Start_Month_7: str
    Start_Day_7: str
    End_Month_7: str
    End_Day_7: str
    ScheduleWeek_Name_8: str
    Start_Month_8: str
    Start_Day_8: str
    End_Month_8: str
    End_Day_8: str
    ScheduleWeek_Name_9: str
    Start_Month_9: str
    Start_Day_9: str
    End_Month_9: str
    End_Day_9: str
    ScheduleWeek_Name_10: str
    Start_Month_10: str
    Start_Day_10: str
    End_Month_10: str
    End_Day_10: str
    ScheduleWeek_Name_11: str
    Start_Month_11: str
    Start_Day_11: str
    End_Month_11: str
    End_Day_11: str
    ScheduleWeek_Name_12: str
    Start_Month_12: str
    Start_Day_12: str
    End_Month_12: str
    End_Day_12: str
    ScheduleWeek_Name_13: str
    Start_Month_13: str
    Start_Day_13: str
    End_Month_13: str
    End_Day_13: str
    ScheduleWeek_Name_14: str
    Start_Month_14: str
    Start_Day_14: str
    End_Month_14: str
    End_Day_14: str
    ScheduleWeek_Name_15: str
    Start_Month_15: str
    Start_Day_15: str
    End_Month_15: str
    End_Day_15: str
    ScheduleWeek_Name_16: str
    Start_Month_16: str
    Start_Day_16: str
    End_Month_16: str
    End_Day_16: str
    ScheduleWeek_Name_17: str
    Start_Month_17: str
    Start_Day_17: str
    End_Month_17: str
    End_Day_17: str
    ScheduleWeek_Name_18: str
    Start_Month_18: str
    Start_Day_18: str
    End_Month_18: str
    End_Day_18: str
    ScheduleWeek_Name_19: str
    Start_Month_19: str
    Start_Day_19: str
    End_Month_19: str
    End_Day_19: str
    ScheduleWeek_Name_20: str
    Start_Month_20: str
    Start_Day_20: str
    End_Month_20: str
    End_Day_20: str
    ScheduleWeek_Name_21: str
    Start_Month_21: str
    Start_Day_21: str
    End_Month_21: str
    End_Day_21: str
    ScheduleWeek_Name_22: str
    Start_Month_22: str
    Start_Day_22: str
    End_Month_22: str
    End_Day_22: str
    ScheduleWeek_Name_23: str
    Start_Month_23: str
    Start_Day_23: str
    End_Month_23: str
    End_Day_23: str
    ScheduleWeek_Name_24: str
    Start_Month_24: str
    Start_Day_24: str
    End_Month_24: str
    End_Day_24: str
    ScheduleWeek_Name_25: str
    Start_Month_25: str
    Start_Day_25: str
    End_Month_25: str
    End_Day_25: str
    ScheduleWeek_Name_26: str
    Start_Month_26: str
    Start_Day_26: str
    End_Month_26: str
    End_Day_26: str
    ScheduleWeek_Name_27: str
    Start_Month_27: str
    Start_Day_27: str
    End_Month_27: str
    End_Day_27: str
    ScheduleWeek_Name_28: str
    Start_Month_28: str
    Start_Day_28: str
    End_Month_28: str
    End_Day_28: str
    ScheduleWeek_Name_29: str
    Start_Month_29: str
    Start_Day_29: str
    End_Month_29: str
    End_Day_29: str
    ScheduleWeek_Name_30: str
    Start_Month_30: str
    Start_Day_30: str
    End_Month_30: str
    End_Day_30: str
    ScheduleWeek_Name_31: str
    Start_Month_31: str
    Start_Day_31: str
    End_Month_31: str
    End_Day_31: str
    ScheduleWeek_Name_32: str
    Start_Month_32: str
    Start_Day_32: str
    End_Month_32: str
    End_Day_32: str
    ScheduleWeek_Name_33: str
    Start_Month_33: str
    Start_Day_33: str
    End_Month_33: str
    End_Day_33: str
    ScheduleWeek_Name_34: str
    Start_Month_34: str
    Start_Day_34: str
    End_Month_34: str
    End_Day_34: str
    ScheduleWeek_Name_35: str
    Start_Month_35: str
    Start_Day_35: str
    End_Month_35: str
    End_Day_35: str
    ScheduleWeek_Name_36: str
    Start_Month_36: str
    Start_Day_36: str
    End_Month_36: str
    End_Day_36: str
    ScheduleWeek_Name_37: str
    Start_Month_37: str
    Start_Day_37: str
    End_Month_37: str
    End_Day_37: str
    ScheduleWeek_Name_38: str
    Start_Month_38: str
    Start_Day_38: str
    End_Month_38: str
    End_Day_38: str
    ScheduleWeek_Name_39: str
    Start_Month_39: str
    Start_Day_39: str
    End_Month_39: str
    End_Day_39: str
    ScheduleWeek_Name_40: str
    Start_Month_40: str
    Start_Day_40: str
    End_Month_40: str
    End_Day_40: str
    ScheduleWeek_Name_41: str
    Start_Month_41: str
    Start_Day_41: str
    End_Month_41: str
    End_Day_41: str
    ScheduleWeek_Name_42: str
    Start_Month_42: str
    Start_Day_42: str
    End_Month_42: str
    End_Day_42: str
    ScheduleWeek_Name_43: str
    Start_Month_43: str
    Start_Day_43: str
    End_Month_43: str
    End_Day_43: str
    ScheduleWeek_Name_44: str
    Start_Month_44: str
    Start_Day_44: str
    End_Month_44: str
    End_Day_44: str
    ScheduleWeek_Name_45: str
    Start_Month_45: str
    Start_Day_45: str
    End_Month_45: str
    End_Day_45: str
    ScheduleWeek_Name_46: str
    Start_Month_46: str
    Start_Day_46: str
    End_Month_46: str
    End_Day_46: str
    ScheduleWeek_Name_47: str
    Start_Month_47: str
    Start_Day_47: str
    End_Month_47: str
    End_Day_47: str
    ScheduleWeek_Name_48: str
    Start_Month_48: str
    Start_Day_48: str
    End_Month_48: str
    End_Day_48: str
    ScheduleWeek_Name_49: str
    Start_Month_49: str
    Start_Day_49: str
    End_Month_49: str
    End_Day_49: str

class ScheduletypelimitsType(TypedDict, total=False):
    """"dict for Scheduletypelimits"""
    Name: str
    Lower_Limit_Value: str
    Upper_Limit_Value: str
    Numeric_Type: str
    Unit_Type: str

class SetpointmanagerColdestType(TypedDict, total=False):
    """"dict for SetpointmanagerColdest"""
    Name: str
    Control_Variable: str
    HVAC_Air_Loop_Name: str
    Minimum_Setpoint_Temperature: str
    Maximum_Setpoint_Temperature: str
    Strategy: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerCondenserenteringresetType(TypedDict, total=False):
    """"dict for SetpointmanagerCondenserenteringreset"""
    Name: str
    Control_Variable: str
    Default_Condenser_Entering_Water_Temperature_Schedule_Name: str
    Minimum_Design_Wetbulb_Temperature_Curve_Name: str
    Minimum_Outside_Air_Wetbulb_Temperature_Curve_Name: str
    Optimized_Cond_Entering_Water_Temperature_Curve_Name: str
    Minimum_Lift: str
    Maximum_Condenser_Entering_Water_Temperature: str
    Cooling_Tower_Design_Inlet_Air_WetBulb_Temperature: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerCondenserenteringresetIdealType(TypedDict, total=False):
    """"dict for SetpointmanagerCondenserenteringresetIdeal"""
    Name: str
    Control_Variable: str
    Minimum_Lift: str
    Maximum_Condenser_Entering_Water_Temperature: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerFollowgroundtemperatureType(TypedDict, total=False):
    """"dict for SetpointmanagerFollowgroundtemperature"""
    Name: str
    Control_Variable: str
    Reference_Ground_Temperature_Object_Type: str
    Offset_Temperature_Difference: str
    Maximum_Setpoint_Temperature: str
    Minimum_Setpoint_Temperature: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerFollowoutdoorairtemperatureType(TypedDict, total=False):
    """"dict for SetpointmanagerFollowoutdoorairtemperature"""
    Name: str
    Control_Variable: str
    Reference_Temperature_Type: str
    Offset_Temperature_Difference: str
    Maximum_Setpoint_Temperature: str
    Minimum_Setpoint_Temperature: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerFollowsystemnodetemperatureType(TypedDict, total=False):
    """"dict for SetpointmanagerFollowsystemnodetemperature"""
    Name: str
    Control_Variable: str
    Reference_Node_Name: str
    Reference_Temperature_Type: str
    Offset_Temperature_Difference: str
    Maximum_Limit_Setpoint_Temperature: str
    Minimum_Limit_Setpoint_Temperature: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerMixedairType(TypedDict, total=False):
    """"dict for SetpointmanagerMixedair"""
    Name: str
    Control_Variable: str
    Reference_Setpoint_Node_Name: str
    Fan_Inlet_Node_Name: str
    Fan_Outlet_Node_Name: str
    Setpoint_Node_or_NodeList_Name: str
    Cooling_Coil_Inlet_Node_Name: str
    Cooling_coil_Outlet_Node_Name: str
    Minimum_Temperature_at_Cooling_Coil_Outlet_Node: str

class SetpointmanagerMultizoneCoolingAverageType(TypedDict, total=False):
    """"dict for SetpointmanagerMultizoneCoolingAverage"""
    Name: str
    HVAC_Air_Loop_Name: str
    Minimum_Setpoint_Temperature: str
    Maximum_Setpoint_Temperature: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerMultizoneHeatingAverageType(TypedDict, total=False):
    """"dict for SetpointmanagerMultizoneHeatingAverage"""
    Name: str
    HVAC_Air_Loop_Name: str
    Minimum_Setpoint_Temperature: str
    Maximum_Setpoint_Temperature: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerMultizoneHumidityMaximumType(TypedDict, total=False):
    """"dict for SetpointmanagerMultizoneHumidityMaximum"""
    Name: str
    HVAC_Air_Loop_Name: str
    Minimum_Setpoint_Humidity_Ratio: str
    Maximum_Setpoint_Humidity_Ratio: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerMultizoneHumidityMinimumType(TypedDict, total=False):
    """"dict for SetpointmanagerMultizoneHumidityMinimum"""
    Name: str
    HVAC_Air_Loop_Name: str
    Minimum_Setpoint_Humidity_Ratio: str
    Maximum_Setpoint_Humidity_Ratio: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerMultizoneMaximumhumidityAverageType(TypedDict, total=False):
    """"dict for SetpointmanagerMultizoneMaximumhumidityAverage"""
    Name: str
    HVAC_Air_Loop_Name: str
    Minimum_Setpoint_Humidity_Ratio: str
    Maximum_Setpoint_Humidity_Ratio: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerMultizoneMinimumhumidityAverageType(TypedDict, total=False):
    """"dict for SetpointmanagerMultizoneMinimumhumidityAverage"""
    Name: str
    HVAC_Air_Loop_Name: str
    Minimum_Setpoint_Humidity_Ratio: str
    Maximum_Setpoint_Humidity_Ratio: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerOutdoorairpretreatType(TypedDict, total=False):
    """"dict for SetpointmanagerOutdoorairpretreat"""
    Name: str
    Control_Variable: str
    Minimum_Setpoint_Temperature: str
    Maximum_Setpoint_Temperature: str
    Minimum_Setpoint_Humidity_Ratio: str
    Maximum_Setpoint_Humidity_Ratio: str
    Reference_Setpoint_Node_Name: str
    Mixed_Air_Stream_Node_Name: str
    Outdoor_Air_Stream_Node_Name: str
    Return_Air_Stream_Node_Name: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerOutdoorairresetType(TypedDict, total=False):
    """"dict for SetpointmanagerOutdoorairreset"""
    Name: str
    Control_Variable: str
    Setpoint_at_Outdoor_Low_Temperature: str
    Outdoor_Low_Temperature: str
    Setpoint_at_Outdoor_High_Temperature: str
    Outdoor_High_Temperature: str
    Setpoint_Node_or_NodeList_Name: str
    Schedule_Name: str
    Setpoint_at_Outdoor_Low_Temperature_2: str
    Outdoor_Low_Temperature_2: str
    Setpoint_at_Outdoor_High_Temperature_2: str
    Outdoor_High_Temperature_2: str

class SetpointmanagerReturnairbypassflowType(TypedDict, total=False):
    """"dict for SetpointmanagerReturnairbypassflow"""
    Name: str
    Control_Variable: str
    HVAC_Air_Loop_Name: str
    Temperature_Setpoint_Schedule_Name: str

class SetpointmanagerReturntemperatureChilledwaterType(TypedDict, total=False):
    """"dict for SetpointmanagerReturntemperatureChilledwater"""
    Name: str
    Plant_Loop_Supply_Outlet_Node: str
    Plant_Loop_Supply_Inlet_Node: str
    Minimum_Supply_Temperature_Setpoint: str
    Maximum_Supply_Temperature_Setpoint: str
    Return_Temperature_Setpoint_Input_Type: str
    Return_Temperature_Setpoint_Constant_Value: str
    Return_Temperature_Setpoint_Schedule_Name: str

class SetpointmanagerReturntemperatureHotwaterType(TypedDict, total=False):
    """"dict for SetpointmanagerReturntemperatureHotwater"""
    Name: str
    Plant_Loop_Supply_Outlet_Node: str
    Plant_Loop_Supply_Inlet_Node: str
    Minimum_Supply_Temperature_Setpoint: str
    Maximum_Supply_Temperature_Setpoint: str
    Return_Temperature_Setpoint_Input_Type: str
    Return_Temperature_Setpoint_Constant_Value: str
    Return_Temperature_Setpoint_Schedule_Name: str

class SetpointmanagerScheduledType(TypedDict, total=False):
    """"dict for SetpointmanagerScheduled"""
    Name: str
    Control_Variable: str
    Schedule_Name: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerScheduledDualsetpointType(TypedDict, total=False):
    """"dict for SetpointmanagerScheduledDualsetpoint"""
    Name: str
    Control_Variable: str
    High_Setpoint_Schedule_Name: str
    Low_Setpoint_Schedule_Name: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerSinglezoneCoolingType(TypedDict, total=False):
    """"dict for SetpointmanagerSinglezoneCooling"""
    Name: str
    Control_Variable: str
    Minimum_Supply_Air_Temperature: str
    Maximum_Supply_Air_Temperature: str
    Control_Zone_Name: str
    Zone_Node_Name: str
    Zone_Inlet_Node_Name: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerSinglezoneHeatingType(TypedDict, total=False):
    """"dict for SetpointmanagerSinglezoneHeating"""
    Name: str
    Control_Variable: str
    Minimum_Supply_Air_Temperature: str
    Maximum_Supply_Air_Temperature: str
    Control_Zone_Name: str
    Zone_Node_Name: str
    Zone_Inlet_Node_Name: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerSinglezoneHumidityMaximumType(TypedDict, total=False):
    """"dict for SetpointmanagerSinglezoneHumidityMaximum"""
    Name: str
    Setpoint_Node_or_NodeList_Name: str
    Control_Zone_Air_Node_Name: str

class SetpointmanagerSinglezoneHumidityMinimumType(TypedDict, total=False):
    """"dict for SetpointmanagerSinglezoneHumidityMinimum"""
    Name: str
    Setpoint_Node_or_NodeList_Name: str
    Control_Zone_Air_Node_Name: str

class SetpointmanagerSinglezoneOnestagecoolingType(TypedDict, total=False):
    """"dict for SetpointmanagerSinglezoneOnestagecooling"""
    Name: str
    Cooling_Stage_On_Supply_Air_Setpoint_Temperature: str
    Cooling_Stage_Off_Supply_Air_Setpoint_Temperature: str
    Control_Zone_Name: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerSinglezoneOnestageheatingType(TypedDict, total=False):
    """"dict for SetpointmanagerSinglezoneOnestageheating"""
    Name: str
    Heating_Stage_On_Supply_Air_Setpoint_Temperature: str
    Heating_Stage_Off_Supply_Air_Setpoint_Temperature: str
    Control_Zone_Name: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerSinglezoneReheatType(TypedDict, total=False):
    """"dict for SetpointmanagerSinglezoneReheat"""
    Name: str
    Control_Variable: str
    Minimum_Supply_Air_Temperature: str
    Maximum_Supply_Air_Temperature: str
    Control_Zone_Name: str
    Zone_Node_Name: str
    Zone_Inlet_Node_Name: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerSystemnoderesetHumidityType(TypedDict, total=False):
    """"dict for SetpointmanagerSystemnoderesetHumidity"""
    Name: str
    Control_Variable: str
    Setpoint_at_Low_Reference_Humidity_Ratio: str
    Setpoint_at_High_Reference_Humidity_Ratio: str
    Low_Reference_Humidity_Ratio: str
    High_Reference_Humidity_Ratio: str
    Reference_Node_Name: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerSystemnoderesetTemperatureType(TypedDict, total=False):
    """"dict for SetpointmanagerSystemnoderesetTemperature"""
    Name: str
    Control_Variable: str
    Setpoint_at_Low_Reference_Temperature: str
    Setpoint_at_High_Reference_Temperature: str
    Low_Reference_Temperature: str
    High_Reference_Temperature: str
    Reference_Node_Name: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerWarmestType(TypedDict, total=False):
    """"dict for SetpointmanagerWarmest"""
    Name: str
    Control_Variable: str
    HVAC_Air_Loop_Name: str
    Minimum_Setpoint_Temperature: str
    Maximum_Setpoint_Temperature: str
    Strategy: str
    Setpoint_Node_or_NodeList_Name: str

class SetpointmanagerWarmesttemperatureflowType(TypedDict, total=False):
    """"dict for SetpointmanagerWarmesttemperatureflow"""
    Name: str
    Control_Variable: str
    HVAC_Air_Loop_Name: str
    Minimum_Setpoint_Temperature: str
    Maximum_Setpoint_Temperature: str
    Strategy: str
    Setpoint_Node_or_NodeList_Name: str
    Minimum_Turndown_Ratio: str

class ShadingBuildingType(TypedDict, total=False):
    """"dict for ShadingBuilding"""
    Name: str
    Azimuth_Angle: str
    Tilt_Angle: str
    Starting_X_Coordinate: str
    Starting_Y_Coordinate: str
    Starting_Z_Coordinate: str
    Length: str
    Height: str

class ShadingBuildingDetailedType(TypedDict, total=False):
    """"dict for ShadingBuildingDetailed"""
    Name: str
    Transmittance_Schedule_Name: str
    Number_of_Vertices: str
    Vertex_1_Xcoordinate: str
    Vertex_1_Ycoordinate: str
    Vertex_1_Zcoordinate: str
    Vertex_2_Xcoordinate: str
    Vertex_2_Ycoordinate: str
    Vertex_2_Zcoordinate: str
    Vertex_3_Xcoordinate: str
    Vertex_3_Ycoordinate: str
    Vertex_3_Zcoordinate: str
    Vertex_4_Xcoordinate: str
    Vertex_4_Ycoordinate: str
    Vertex_4_Zcoordinate: str
    Vertex_5_Xcoordinate: str
    Vertex_5_Ycoordinate: str
    Vertex_5_Zcoordinate: str
    Vertex_6_Xcoordinate: str
    Vertex_6_Ycoordinate: str
    Vertex_6_Zcoordinate: str
    Vertex_7_Xcoordinate: str
    Vertex_7_Ycoordinate: str
    Vertex_7_Zcoordinate: str
    Vertex_8_Xcoordinate: str
    Vertex_8_Ycoordinate: str
    Vertex_8_Zcoordinate: str
    Vertex_9_Xcoordinate: str
    Vertex_9_Ycoordinate: str
    Vertex_9_Zcoordinate: str
    Vertex_10_Xcoordinate: str
    Vertex_10_Ycoordinate: str
    Vertex_10_Zcoordinate: str
    Vertex_11_Xcoordinate: str
    Vertex_11_Ycoordinate: str
    Vertex_11_Zcoordinate: str
    Vertex_12_Xcoordinate: str
    Vertex_12_Ycoordinate: str
    Vertex_12_Zcoordinate: str
    Vertex_13_Xcoordinate: str
    Vertex_13_Ycoordinate: str
    Vertex_13_Zcoordinate: str
    Vertex_14_Xcoordinate: str
    Vertex_14_Ycoordinate: str
    Vertex_14_Zcoordinate: str
    Vertex_15_Xcoordinate: str
    Vertex_15_Ycoordinate: str
    Vertex_15_Zcoordinate: str
    Vertex_16_Xcoordinate: str
    Vertex_16_Ycoordinate: str
    Vertex_16_Zcoordinate: str
    Vertex_17_Xcoordinate: str
    Vertex_17_Ycoordinate: str
    Vertex_17_Zcoordinate: str
    Vertex_18_Xcoordinate: str
    Vertex_18_Ycoordinate: str
    Vertex_18_Zcoordinate: str
    Vertex_19_Xcoordinate: str
    Vertex_19_Ycoordinate: str
    Vertex_19_Zcoordinate: str
    Vertex_20_Xcoordinate: str
    Vertex_20_Ycoordinate: str
    Vertex_20_Zcoordinate: str
    Vertex_21_Xcoordinate: str
    Vertex_21_Ycoordinate: str
    Vertex_21_Zcoordinate: str
    Vertex_22_Xcoordinate: str
    Vertex_22_Ycoordinate: str
    Vertex_22_Zcoordinate: str
    Vertex_23_Xcoordinate: str
    Vertex_23_Ycoordinate: str
    Vertex_23_Zcoordinate: str
    Vertex_24_Xcoordinate: str
    Vertex_24_Ycoordinate: str
    Vertex_24_Zcoordinate: str
    Vertex_25_Xcoordinate: str
    Vertex_25_Ycoordinate: str
    Vertex_25_Zcoordinate: str
    Vertex_26_Xcoordinate: str
    Vertex_26_Ycoordinate: str
    Vertex_26_Zcoordinate: str
    Vertex_27_Xcoordinate: str
    Vertex_27_Ycoordinate: str
    Vertex_27_Zcoordinate: str
    Vertex_28_Xcoordinate: str
    Vertex_28_Ycoordinate: str
    Vertex_28_Zcoordinate: str
    Vertex_29_Xcoordinate: str
    Vertex_29_Ycoordinate: str
    Vertex_29_Zcoordinate: str
    Vertex_30_Xcoordinate: str
    Vertex_30_Ycoordinate: str
    Vertex_30_Zcoordinate: str
    Vertex_31_Xcoordinate: str
    Vertex_31_Ycoordinate: str
    Vertex_31_Zcoordinate: str
    Vertex_32_Xcoordinate: str
    Vertex_32_Ycoordinate: str
    Vertex_32_Zcoordinate: str
    Vertex_33_Xcoordinate: str
    Vertex_33_Ycoordinate: str
    Vertex_33_Zcoordinate: str
    Vertex_34_Xcoordinate: str
    Vertex_34_Ycoordinate: str
    Vertex_34_Zcoordinate: str
    Vertex_35_Xcoordinate: str
    Vertex_35_Ycoordinate: str
    Vertex_35_Zcoordinate: str
    Vertex_36_Xcoordinate: str
    Vertex_36_Ycoordinate: str
    Vertex_36_Zcoordinate: str
    Vertex_37_Xcoordinate: str
    Vertex_37_Ycoordinate: str
    Vertex_37_Zcoordinate: str
    Vertex_38_Xcoordinate: str
    Vertex_38_Ycoordinate: str
    Vertex_38_Zcoordinate: str
    Vertex_39_Xcoordinate: str
    Vertex_39_Ycoordinate: str
    Vertex_39_Zcoordinate: str
    Vertex_40_Xcoordinate: str
    Vertex_40_Ycoordinate: str
    Vertex_40_Zcoordinate: str
    Vertex_41_Xcoordinate: str
    Vertex_41_Ycoordinate: str
    Vertex_41_Zcoordinate: str
    Vertex_42_Xcoordinate: str
    Vertex_42_Ycoordinate: str
    Vertex_42_Zcoordinate: str
    Vertex_43_Xcoordinate: str
    Vertex_43_Ycoordinate: str
    Vertex_43_Zcoordinate: str
    Vertex_44_Xcoordinate: str
    Vertex_44_Ycoordinate: str
    Vertex_44_Zcoordinate: str
    Vertex_45_Xcoordinate: str
    Vertex_45_Ycoordinate: str
    Vertex_45_Zcoordinate: str
    Vertex_46_Xcoordinate: str
    Vertex_46_Ycoordinate: str
    Vertex_46_Zcoordinate: str
    Vertex_47_Xcoordinate: str
    Vertex_47_Ycoordinate: str
    Vertex_47_Zcoordinate: str
    Vertex_48_Xcoordinate: str
    Vertex_48_Ycoordinate: str
    Vertex_48_Zcoordinate: str
    Vertex_49_Xcoordinate: str
    Vertex_49_Ycoordinate: str
    Vertex_49_Zcoordinate: str

class ShadingFinType(TypedDict, total=False):
    """"dict for ShadingFin"""
    Name: str
    Window_or_Door_Name: str
    Left_Extension_from_WindowDoor: str
    Left_Distance_Above_Top_of_Window: str
    Left_Distance_Below_Bottom_of_Window: str
    Left_Tilt_Angle_from_WindowDoor: str
    Left_Depth: str
    Right_Extension_from_WindowDoor: str
    Right_Distance_Above_Top_of_Window: str
    Right_Distance_Below_Bottom_of_Window: str
    Right_Tilt_Angle_from_WindowDoor: str
    Right_Depth: str

class ShadingFinProjectionType(TypedDict, total=False):
    """"dict for ShadingFinProjection"""
    Name: str
    Window_or_Door_Name: str
    Left_Extension_from_WindowDoor: str
    Left_Distance_Above_Top_of_Window: str
    Left_Distance_Below_Bottom_of_Window: str
    Left_Tilt_Angle_from_WindowDoor: str
    Left_Depth_as_Fraction_of_WindowDoor_Width: str
    Right_Extension_from_WindowDoor: str
    Right_Distance_Above_Top_of_Window: str
    Right_Distance_Below_Bottom_of_Window: str
    Right_Tilt_Angle_from_WindowDoor: str
    Right_Depth_as_Fraction_of_WindowDoor_Width: str

class ShadingOverhangType(TypedDict, total=False):
    """"dict for ShadingOverhang"""
    Name: str
    Window_or_Door_Name: str
    Height_above_Window_or_Door: str
    Tilt_Angle_from_WindowDoor: str
    Left_extension_from_WindowDoor_Width: str
    Right_extension_from_WindowDoor_Width: str
    Depth: str

class ShadingOverhangProjectionType(TypedDict, total=False):
    """"dict for ShadingOverhangProjection"""
    Name: str
    Window_or_Door_Name: str
    Height_above_Window_or_Door: str
    Tilt_Angle_from_WindowDoor: str
    Left_extension_from_WindowDoor_Width: str
    Right_extension_from_WindowDoor_Width: str
    Depth_as_Fraction_of_WindowDoor_Height: str

class ShadingSiteType(TypedDict, total=False):
    """"dict for ShadingSite"""
    Name: str
    Azimuth_Angle: str
    Tilt_Angle: str
    Starting_X_Coordinate: str
    Starting_Y_Coordinate: str
    Starting_Z_Coordinate: str
    Length: str
    Height: str

class ShadingSiteDetailedType(TypedDict, total=False):
    """"dict for ShadingSiteDetailed"""
    Name: str
    Transmittance_Schedule_Name: str
    Number_of_Vertices: str
    Vertex_1_Xcoordinate: str
    Vertex_1_Ycoordinate: str
    Vertex_1_Zcoordinate: str
    Vertex_2_Xcoordinate: str
    Vertex_2_Ycoordinate: str
    Vertex_2_Zcoordinate: str
    Vertex_3_Xcoordinate: str
    Vertex_3_Ycoordinate: str
    Vertex_3_Zcoordinate: str
    Vertex_4_Xcoordinate: str
    Vertex_4_Ycoordinate: str
    Vertex_4_Zcoordinate: str
    Vertex_5_Xcoordinate: str
    Vertex_5_Ycoordinate: str
    Vertex_5_Zcoordinate: str
    Vertex_6_Xcoordinate: str
    Vertex_6_Ycoordinate: str
    Vertex_6_Zcoordinate: str
    Vertex_7_Xcoordinate: str
    Vertex_7_Ycoordinate: str
    Vertex_7_Zcoordinate: str
    Vertex_8_Xcoordinate: str
    Vertex_8_Ycoordinate: str
    Vertex_8_Zcoordinate: str
    Vertex_9_Xcoordinate: str
    Vertex_9_Ycoordinate: str
    Vertex_9_Zcoordinate: str
    Vertex_10_Xcoordinate: str
    Vertex_10_Ycoordinate: str
    Vertex_10_Zcoordinate: str
    Vertex_11_Xcoordinate: str
    Vertex_11_Ycoordinate: str
    Vertex_11_Zcoordinate: str
    Vertex_12_Xcoordinate: str
    Vertex_12_Ycoordinate: str
    Vertex_12_Zcoordinate: str
    Vertex_13_Xcoordinate: str
    Vertex_13_Ycoordinate: str
    Vertex_13_Zcoordinate: str
    Vertex_14_Xcoordinate: str
    Vertex_14_Ycoordinate: str
    Vertex_14_Zcoordinate: str
    Vertex_15_Xcoordinate: str
    Vertex_15_Ycoordinate: str
    Vertex_15_Zcoordinate: str
    Vertex_16_Xcoordinate: str
    Vertex_16_Ycoordinate: str
    Vertex_16_Zcoordinate: str
    Vertex_17_Xcoordinate: str
    Vertex_17_Ycoordinate: str
    Vertex_17_Zcoordinate: str
    Vertex_18_Xcoordinate: str
    Vertex_18_Ycoordinate: str
    Vertex_18_Zcoordinate: str
    Vertex_19_Xcoordinate: str
    Vertex_19_Ycoordinate: str
    Vertex_19_Zcoordinate: str
    Vertex_20_Xcoordinate: str
    Vertex_20_Ycoordinate: str
    Vertex_20_Zcoordinate: str
    Vertex_21_Xcoordinate: str
    Vertex_21_Ycoordinate: str
    Vertex_21_Zcoordinate: str
    Vertex_22_Xcoordinate: str
    Vertex_22_Ycoordinate: str
    Vertex_22_Zcoordinate: str
    Vertex_23_Xcoordinate: str
    Vertex_23_Ycoordinate: str
    Vertex_23_Zcoordinate: str
    Vertex_24_Xcoordinate: str
    Vertex_24_Ycoordinate: str
    Vertex_24_Zcoordinate: str
    Vertex_25_Xcoordinate: str
    Vertex_25_Ycoordinate: str
    Vertex_25_Zcoordinate: str
    Vertex_26_Xcoordinate: str
    Vertex_26_Ycoordinate: str
    Vertex_26_Zcoordinate: str
    Vertex_27_Xcoordinate: str
    Vertex_27_Ycoordinate: str
    Vertex_27_Zcoordinate: str
    Vertex_28_Xcoordinate: str
    Vertex_28_Ycoordinate: str
    Vertex_28_Zcoordinate: str
    Vertex_29_Xcoordinate: str
    Vertex_29_Ycoordinate: str
    Vertex_29_Zcoordinate: str
    Vertex_30_Xcoordinate: str
    Vertex_30_Ycoordinate: str
    Vertex_30_Zcoordinate: str
    Vertex_31_Xcoordinate: str
    Vertex_31_Ycoordinate: str
    Vertex_31_Zcoordinate: str
    Vertex_32_Xcoordinate: str
    Vertex_32_Ycoordinate: str
    Vertex_32_Zcoordinate: str
    Vertex_33_Xcoordinate: str
    Vertex_33_Ycoordinate: str
    Vertex_33_Zcoordinate: str
    Vertex_34_Xcoordinate: str
    Vertex_34_Ycoordinate: str
    Vertex_34_Zcoordinate: str
    Vertex_35_Xcoordinate: str
    Vertex_35_Ycoordinate: str
    Vertex_35_Zcoordinate: str
    Vertex_36_Xcoordinate: str
    Vertex_36_Ycoordinate: str
    Vertex_36_Zcoordinate: str
    Vertex_37_Xcoordinate: str
    Vertex_37_Ycoordinate: str
    Vertex_37_Zcoordinate: str
    Vertex_38_Xcoordinate: str
    Vertex_38_Ycoordinate: str
    Vertex_38_Zcoordinate: str
    Vertex_39_Xcoordinate: str
    Vertex_39_Ycoordinate: str
    Vertex_39_Zcoordinate: str
    Vertex_40_Xcoordinate: str
    Vertex_40_Ycoordinate: str
    Vertex_40_Zcoordinate: str
    Vertex_41_Xcoordinate: str
    Vertex_41_Ycoordinate: str
    Vertex_41_Zcoordinate: str
    Vertex_42_Xcoordinate: str
    Vertex_42_Ycoordinate: str
    Vertex_42_Zcoordinate: str
    Vertex_43_Xcoordinate: str
    Vertex_43_Ycoordinate: str
    Vertex_43_Zcoordinate: str
    Vertex_44_Xcoordinate: str
    Vertex_44_Ycoordinate: str
    Vertex_44_Zcoordinate: str
    Vertex_45_Xcoordinate: str
    Vertex_45_Ycoordinate: str
    Vertex_45_Zcoordinate: str
    Vertex_46_Xcoordinate: str
    Vertex_46_Ycoordinate: str
    Vertex_46_Zcoordinate: str
    Vertex_47_Xcoordinate: str
    Vertex_47_Ycoordinate: str
    Vertex_47_Zcoordinate: str
    Vertex_48_Xcoordinate: str
    Vertex_48_Ycoordinate: str
    Vertex_48_Zcoordinate: str
    Vertex_49_Xcoordinate: str
    Vertex_49_Ycoordinate: str
    Vertex_49_Zcoordinate: str

class ShadingZoneDetailedType(TypedDict, total=False):
    """"dict for ShadingZoneDetailed"""
    Name: str
    Base_Surface_Name: str
    Transmittance_Schedule_Name: str
    Number_of_Vertices: str
    Vertex_1_Xcoordinate: str
    Vertex_1_Ycoordinate: str
    Vertex_1_Zcoordinate: str
    Vertex_2_Xcoordinate: str
    Vertex_2_Ycoordinate: str
    Vertex_2_Zcoordinate: str
    Vertex_3_Xcoordinate: str
    Vertex_3_Ycoordinate: str
    Vertex_3_Zcoordinate: str
    Vertex_4_Xcoordinate: str
    Vertex_4_Ycoordinate: str
    Vertex_4_Zcoordinate: str
    Vertex_5_Xcoordinate: str
    Vertex_5_Ycoordinate: str
    Vertex_5_Zcoordinate: str
    Vertex_6_Xcoordinate: str
    Vertex_6_Ycoordinate: str
    Vertex_6_Zcoordinate: str
    Vertex_7_Xcoordinate: str
    Vertex_7_Ycoordinate: str
    Vertex_7_Zcoordinate: str
    Vertex_8_Xcoordinate: str
    Vertex_8_Ycoordinate: str
    Vertex_8_Zcoordinate: str
    Vertex_9_Xcoordinate: str
    Vertex_9_Ycoordinate: str
    Vertex_9_Zcoordinate: str
    Vertex_10_Xcoordinate: str
    Vertex_10_Ycoordinate: str
    Vertex_10_Zcoordinate: str
    Vertex_11_Xcoordinate: str
    Vertex_11_Ycoordinate: str
    Vertex_11_Zcoordinate: str
    Vertex_12_Xcoordinate: str
    Vertex_12_Ycoordinate: str
    Vertex_12_Zcoordinate: str
    Vertex_13_Xcoordinate: str
    Vertex_13_Ycoordinate: str
    Vertex_13_Zcoordinate: str
    Vertex_14_Xcoordinate: str
    Vertex_14_Ycoordinate: str
    Vertex_14_Zcoordinate: str
    Vertex_15_Xcoordinate: str
    Vertex_15_Ycoordinate: str
    Vertex_15_Zcoordinate: str
    Vertex_16_Xcoordinate: str
    Vertex_16_Ycoordinate: str
    Vertex_16_Zcoordinate: str
    Vertex_17_Xcoordinate: str
    Vertex_17_Ycoordinate: str
    Vertex_17_Zcoordinate: str
    Vertex_18_Xcoordinate: str
    Vertex_18_Ycoordinate: str
    Vertex_18_Zcoordinate: str
    Vertex_19_Xcoordinate: str
    Vertex_19_Ycoordinate: str
    Vertex_19_Zcoordinate: str
    Vertex_20_Xcoordinate: str
    Vertex_20_Ycoordinate: str
    Vertex_20_Zcoordinate: str
    Vertex_21_Xcoordinate: str
    Vertex_21_Ycoordinate: str
    Vertex_21_Zcoordinate: str
    Vertex_22_Xcoordinate: str
    Vertex_22_Ycoordinate: str
    Vertex_22_Zcoordinate: str
    Vertex_23_Xcoordinate: str
    Vertex_23_Ycoordinate: str
    Vertex_23_Zcoordinate: str
    Vertex_24_Xcoordinate: str
    Vertex_24_Ycoordinate: str
    Vertex_24_Zcoordinate: str
    Vertex_25_Xcoordinate: str
    Vertex_25_Ycoordinate: str
    Vertex_25_Zcoordinate: str
    Vertex_26_Xcoordinate: str
    Vertex_26_Ycoordinate: str
    Vertex_26_Zcoordinate: str
    Vertex_27_Xcoordinate: str
    Vertex_27_Ycoordinate: str
    Vertex_27_Zcoordinate: str
    Vertex_28_Xcoordinate: str
    Vertex_28_Ycoordinate: str
    Vertex_28_Zcoordinate: str
    Vertex_29_Xcoordinate: str
    Vertex_29_Ycoordinate: str
    Vertex_29_Zcoordinate: str
    Vertex_30_Xcoordinate: str
    Vertex_30_Ycoordinate: str
    Vertex_30_Zcoordinate: str
    Vertex_31_Xcoordinate: str
    Vertex_31_Ycoordinate: str
    Vertex_31_Zcoordinate: str
    Vertex_32_Xcoordinate: str
    Vertex_32_Ycoordinate: str
    Vertex_32_Zcoordinate: str
    Vertex_33_Xcoordinate: str
    Vertex_33_Ycoordinate: str
    Vertex_33_Zcoordinate: str
    Vertex_34_Xcoordinate: str
    Vertex_34_Ycoordinate: str
    Vertex_34_Zcoordinate: str
    Vertex_35_Xcoordinate: str
    Vertex_35_Ycoordinate: str
    Vertex_35_Zcoordinate: str
    Vertex_36_Xcoordinate: str
    Vertex_36_Ycoordinate: str
    Vertex_36_Zcoordinate: str
    Vertex_37_Xcoordinate: str
    Vertex_37_Ycoordinate: str
    Vertex_37_Zcoordinate: str
    Vertex_38_Xcoordinate: str
    Vertex_38_Ycoordinate: str
    Vertex_38_Zcoordinate: str
    Vertex_39_Xcoordinate: str
    Vertex_39_Ycoordinate: str
    Vertex_39_Zcoordinate: str
    Vertex_40_Xcoordinate: str
    Vertex_40_Ycoordinate: str
    Vertex_40_Zcoordinate: str
    Vertex_41_Xcoordinate: str
    Vertex_41_Ycoordinate: str
    Vertex_41_Zcoordinate: str
    Vertex_42_Xcoordinate: str
    Vertex_42_Ycoordinate: str
    Vertex_42_Zcoordinate: str
    Vertex_43_Xcoordinate: str
    Vertex_43_Ycoordinate: str
    Vertex_43_Zcoordinate: str
    Vertex_44_Xcoordinate: str
    Vertex_44_Ycoordinate: str
    Vertex_44_Zcoordinate: str
    Vertex_45_Xcoordinate: str
    Vertex_45_Ycoordinate: str
    Vertex_45_Zcoordinate: str
    Vertex_46_Xcoordinate: str
    Vertex_46_Ycoordinate: str
    Vertex_46_Zcoordinate: str
    Vertex_47_Xcoordinate: str
    Vertex_47_Ycoordinate: str
    Vertex_47_Zcoordinate: str
    Vertex_48_Xcoordinate: str
    Vertex_48_Ycoordinate: str
    Vertex_48_Zcoordinate: str
    Vertex_49_Xcoordinate: str
    Vertex_49_Ycoordinate: str
    Vertex_49_Zcoordinate: str

class ShadingpropertyReflectanceType(TypedDict, total=False):
    """"dict for ShadingpropertyReflectance"""
    Shading_Surface_Name: str
    Diffuse_Solar_Reflectance_of_Unglazed_Part_of_Shading_Surface: str
    Diffuse_Visible_Reflectance_of_Unglazed_Part_of_Shading_Surface: str
    Fraction_of_Shading_Surface_That_Is_Glazed: str
    Glazing_Construction_Name: str

class ShadowcalculationType(TypedDict, total=False):
    """"dict for Shadowcalculation"""
    Shading_Calculation_Method: str
    Shading_Calculation_Update_Frequency_Method: str
    Shading_Calculation_Update_Frequency: str
    Maximum_Figures_in_Shadow_Overlap_Calculations: str
    Polygon_Clipping_Algorithm: str
    Pixel_Counting_Resolution: str
    Sky_Diffuse_Modeling_Algorithm: str
    Output_External_Shading_Calculation_Results: str
    Disable_SelfShading_Within_Shading_Zone_Groups: str
    Disable_SelfShading_From_Shading_Zone_Groups_to_Other_Zones: str
    Shading_Zone_Group_1_ZoneList_Name: str
    Shading_Zone_Group_2_ZoneList_Name: str
    Shading_Zone_Group_3_ZoneList_Name: str
    Shading_Zone_Group_4_ZoneList_Name: str
    Shading_Zone_Group_5_ZoneList_Name: str
    Shading_Zone_Group_6_ZoneList_Name: str

class SimulationcontrolType(TypedDict, total=False):
    """"dict for Simulationcontrol"""
    Do_Zone_Sizing_Calculation: str
    Do_System_Sizing_Calculation: str
    Do_Plant_Sizing_Calculation: str
    Run_Simulation_for_Sizing_Periods: str
    Run_Simulation_for_Weather_File_Run_Periods: str
    Do_HVAC_Sizing_Simulation_for_Sizing_Periods: str
    Maximum_Number_of_HVAC_Sizing_Simulation_Passes: str

class SiteGrounddomainBasementType(TypedDict, total=False):
    """"dict for SiteGrounddomainBasement"""
    Name: str
    Ground_Domain_Depth: str
    Aspect_Ratio: str
    Perimeter_Offset: str
    Soil_Thermal_Conductivity: str
    Soil_Density: str
    Soil_Specific_Heat: str
    Soil_Moisture_Content_Volume_Fraction: str
    Soil_Moisture_Content_Volume_Fraction_at_Saturation: str
    Undisturbed_Ground_Temperature_Model_Type: str
    Undisturbed_Ground_Temperature_Model_Name: str
    Evapotranspiration_Ground_Cover_Parameter: str
    Basement_Floor_Boundary_Condition_Model_Name: str
    Horizontal_Insulation: str
    Horizontal_Insulation_Material_Name: str
    Horizontal_Insulation_Extents: str
    Perimeter_Horizontal_Insulation_Width: str
    Basement_Wall_Depth: str
    Basement_Wall_Boundary_Condition_Model_Name: str
    Vertical_Insulation: str
    Basement_Wall_Vertical_Insulation_Material_Name: str
    Vertical_Insulation_Depth: str
    Simulation_Timestep: str
    Mesh_Density_Parameter: str

class SiteGrounddomainSlabType(TypedDict, total=False):
    """"dict for SiteGrounddomainSlab"""
    Name: str
    Ground_Domain_Depth: str
    Aspect_Ratio: str
    Perimeter_Offset: str
    Soil_Thermal_Conductivity: str
    Soil_Density: str
    Soil_Specific_Heat: str
    Soil_Moisture_Content_Volume_Fraction: str
    Soil_Moisture_Content_Volume_Fraction_at_Saturation: str
    Undisturbed_Ground_Temperature_Model_Type: str
    Undisturbed_Ground_Temperature_Model_Name: str
    Evapotranspiration_Ground_Cover_Parameter: str
    Slab_Boundary_Condition_Model_Name: str
    Slab_Location: str
    Slab_Material_Name: str
    Horizontal_Insulation: str
    Horizontal_Insulation_Material_Name: str
    Horizontal_Insulation_Extents: str
    Perimeter_Insulation_Width: str
    Vertical_Insulation: str
    Vertical_Insulation_Material_Name: str
    Vertical_Insulation_Depth: str
    Simulation_Timestep: str
    Geometric_Mesh_Coefficient: str
    Mesh_Density_Parameter: str

class SiteGroundreflectanceType(TypedDict, total=False):
    """"dict for SiteGroundreflectance"""
    January_Ground_Reflectance: str
    February_Ground_Reflectance: str
    March_Ground_Reflectance: str
    April_Ground_Reflectance: str
    May_Ground_Reflectance: str
    June_Ground_Reflectance: str
    July_Ground_Reflectance: str
    August_Ground_Reflectance: str
    September_Ground_Reflectance: str
    October_Ground_Reflectance: str
    November_Ground_Reflectance: str
    December_Ground_Reflectance: str

class SiteGroundreflectanceSnowmodifierType(TypedDict, total=False):
    """"dict for SiteGroundreflectanceSnowmodifier"""
    Ground_Reflected_Solar_Modifier: str
    Daylighting_Ground_Reflected_Solar_Modifier: str

class SiteGroundtemperatureBuildingsurfaceType(TypedDict, total=False):
    """"dict for SiteGroundtemperatureBuildingsurface"""
    January_Ground_Temperature: str
    February_Ground_Temperature: str
    March_Ground_Temperature: str
    April_Ground_Temperature: str
    May_Ground_Temperature: str
    June_Ground_Temperature: str
    July_Ground_Temperature: str
    August_Ground_Temperature: str
    September_Ground_Temperature: str
    October_Ground_Temperature: str
    November_Ground_Temperature: str
    December_Ground_Temperature: str

class SiteGroundtemperatureDeepType(TypedDict, total=False):
    """"dict for SiteGroundtemperatureDeep"""
    January_Deep_Ground_Temperature: str
    February_Deep_Ground_Temperature: str
    March_Deep_Ground_Temperature: str
    April_Deep_Ground_Temperature: str
    May_Deep_Ground_Temperature: str
    June_Deep_Ground_Temperature: str
    July_Deep_Ground_Temperature: str
    August_Deep_Ground_Temperature: str
    September_Deep_Ground_Temperature: str
    October_Deep_Ground_Temperature: str
    November_Deep_Ground_Temperature: str
    December_Deep_Ground_Temperature: str

class SiteGroundtemperatureFcfactormethodType(TypedDict, total=False):
    """"dict for SiteGroundtemperatureFcfactormethod"""
    January_Ground_Temperature: str
    February_Ground_Temperature: str
    March_Ground_Temperature: str
    April_Ground_Temperature: str
    May_Ground_Temperature: str
    June_Ground_Temperature: str
    July_Ground_Temperature: str
    August_Ground_Temperature: str
    September_Ground_Temperature: str
    October_Ground_Temperature: str
    November_Ground_Temperature: str
    December_Ground_Temperature: str

class SiteGroundtemperatureShallowType(TypedDict, total=False):
    """"dict for SiteGroundtemperatureShallow"""
    January_Surface_Ground_Temperature: str
    February_Surface_Ground_Temperature: str
    March_Surface_Ground_Temperature: str
    April_Surface_Ground_Temperature: str
    May_Surface_Ground_Temperature: str
    June_Surface_Ground_Temperature: str
    July_Surface_Ground_Temperature: str
    August_Surface_Ground_Temperature: str
    September_Surface_Ground_Temperature: str
    October_Surface_Ground_Temperature: str
    November_Surface_Ground_Temperature: str
    December_Surface_Ground_Temperature: str

class SiteGroundtemperatureUndisturbedFinitedifferenceType(TypedDict, total=False):
    """"dict for SiteGroundtemperatureUndisturbedFinitedifference"""
    Name: str
    Soil_Thermal_Conductivity: str
    Soil_Density: str
    Soil_Specific_Heat: str
    Soil_Moisture_Content_Volume_Fraction: str
    Soil_Moisture_Content_Volume_Fraction_at_Saturation: str
    Evapotranspiration_Ground_Cover_Parameter: str

class SiteGroundtemperatureUndisturbedKusudaachenbachType(TypedDict, total=False):
    """"dict for SiteGroundtemperatureUndisturbedKusudaachenbach"""
    Name: str
    Soil_Thermal_Conductivity: str
    Soil_Density: str
    Soil_Specific_Heat: str
    Average_Soil_Surface_Temperature: str
    Average_Amplitude_of_Surface_Temperature: str
    Phase_Shift_of_Minimum_Surface_Temperature: str

class SiteGroundtemperatureUndisturbedXingType(TypedDict, total=False):
    """"dict for SiteGroundtemperatureUndisturbedXing"""
    Name: str
    Soil_Thermal_Conductivity: str
    Soil_Density: str
    Soil_Specific_Heat: str
    Average_Soil_Surface_Temperature: str
    Soil_Surface_Temperature_Amplitude_1: str
    Soil_Surface_Temperature_Amplitude_2: str
    Phase_Shift_of_Temperature_Amplitude_1: str
    Phase_Shift_of_Temperature_Amplitude_2: str

class SiteHeightvariationType(TypedDict, total=False):
    """"dict for SiteHeightvariation"""
    Wind_Speed_Profile_Exponent: str
    Wind_Speed_Profile_Boundary_Layer_Thickness: str
    Air_Temperature_Gradient_Coefficient: str

class SiteLocationType(TypedDict, total=False):
    """"dict for SiteLocation"""
    Name: str
    Latitude: str
    Longitude: str
    Time_Zone: str
    Elevation: str

class SitePrecipitationType(TypedDict, total=False):
    """"dict for SitePrecipitation"""
    Precipitation_Model_Type: str
    Design_Level_for_Total_Annual_Precipitation: str
    Precipitation_Rates_Schedule_Name: str
    Average_Total_Annual_Precipitation: str

class SiteSolarandvisiblespectrumType(TypedDict, total=False):
    """"dict for SiteSolarandvisiblespectrum"""
    Name: str
    Spectrum_Data_Method: str
    Solar_Spectrum_Data_Object_Name: str
    Visible_Spectrum_Data_Object_Name: str

class SiteSpectrumdataType(TypedDict, total=False):
    """"dict for SiteSpectrumdata"""
    Name: str
    Spectrum_Data_Type: str
    Wavelength: str
    Spectrum: str
    Wavelength: str
    Spectrum: str
    Wavelength: str
    Spectrum: str
    N7: str
    N8: str
    N9: str
    N10: str
    N11: str
    N12: str
    N13: str
    N14: str
    N15: str
    N16: str
    N17: str
    N18: str
    N19: str
    N20: str
    N21: str
    N22: str
    N23: str
    N24: str
    N25: str
    N26: str
    N27: str
    N28: str
    N29: str
    N30: str
    N31: str
    N32: str
    N33: str
    N34: str
    N35: str
    N36: str
    N37: str
    N38: str
    N39: str
    N40: str
    N41: str
    N42: str
    N43: str
    N44: str
    N45: str
    N46: str
    N47: str
    N48: str
    N49: str
    N50: str
    N51: str
    N52: str
    N53: str
    N54: str
    N55: str
    N56: str
    N57: str
    N58: str
    N59: str
    N60: str
    N61: str
    N62: str
    N63: str
    N64: str
    N65: str
    N66: str
    N67: str
    N68: str
    N69: str
    N70: str
    N71: str
    N72: str
    N73: str
    N74: str
    N75: str
    N76: str
    N77: str
    N78: str
    N79: str
    N80: str
    N81: str
    N82: str
    N83: str
    N84: str
    N85: str
    N86: str
    N87: str
    N88: str
    N89: str
    N90: str
    N91: str
    N92: str
    N93: str
    N94: str
    N95: str
    N96: str
    N97: str
    N98: str
    N99: str
    N100: str
    N101: str
    N102: str
    N103: str
    N104: str
    N105: str
    N106: str
    N107: str
    N108: str
    N109: str
    N110: str
    N111: str
    N112: str
    N113: str
    N114: str
    N115: str
    N116: str
    N117: str
    N118: str
    N119: str
    N120: str
    N121: str
    N122: str
    N123: str
    N124: str
    N125: str
    N126: str
    N127: str
    N128: str
    N129: str
    N130: str
    N131: str
    N132: str
    N133: str
    N134: str
    N135: str
    N136: str
    N137: str
    N138: str
    N139: str
    N140: str
    N141: str
    N142: str
    N143: str
    N144: str
    N145: str
    N146: str
    N147: str
    N148: str
    N149: str
    N150: str
    N151: str
    N152: str
    N153: str
    N154: str
    N155: str
    N156: str
    N157: str
    N158: str
    N159: str
    N160: str
    N161: str
    N162: str
    N163: str
    N164: str
    N165: str
    N166: str
    N167: str
    N168: str
    N169: str
    N170: str
    N171: str
    N172: str
    N173: str
    N174: str
    N175: str
    N176: str
    N177: str
    N178: str
    N179: str
    N180: str
    N181: str
    N182: str
    N183: str
    N184: str
    N185: str
    N186: str
    N187: str
    N188: str
    N189: str
    N190: str
    N191: str
    N192: str
    N193: str
    N194: str
    N195: str
    N196: str
    N197: str
    N198: str
    N199: str
    N200: str
    N201: str
    N202: str
    N203: str
    N204: str
    N205: str
    N206: str
    N207: str
    N208: str
    N209: str
    N210: str
    N211: str
    N212: str
    N213: str
    N214: str

class SiteVariablelocationType(TypedDict, total=False):
    """"dict for SiteVariablelocation"""
    Name: str
    Building_Location_Latitude_Schedule: str
    Building_Location_Longitude_Schedule: str
    Building_Location_Orientation_Schedule: str

class SiteWatermainstemperatureType(TypedDict, total=False):
    """"dict for SiteWatermainstemperature"""
    Calculation_Method: str
    Temperature_Schedule_Name: str
    Annual_Average_Outdoor_Air_Temperature: str
    Maximum_Difference_In_Monthly_Average_Outdoor_Air_Temperatures: str

class SiteWeatherstationType(TypedDict, total=False):
    """"dict for SiteWeatherstation"""
    Wind_Sensor_Height_Above_Ground: str
    Wind_Speed_Profile_Exponent: str
    Wind_Speed_Profile_Boundary_Layer_Thickness: str
    Air_Temperature_Sensor_Height_Above_Ground: str

class SizingParametersType(TypedDict, total=False):
    """"dict for SizingParameters"""
    Heating_Sizing_Factor: str
    Cooling_Sizing_Factor: str
    Timesteps_in_Averaging_Window: str

class SizingPlantType(TypedDict, total=False):
    """"dict for SizingPlant"""
    Plant_or_Condenser_Loop_Name: str
    Loop_Type: str
    Design_Loop_Exit_Temperature: str
    Loop_Design_Temperature_Difference: str
    Sizing_Option: str
    Zone_Timesteps_in_Averaging_Window: str
    Coincident_Sizing_Factor_Mode: str

class SizingSystemType(TypedDict, total=False):
    """"dict for SizingSystem"""
    AirLoop_Name: str
    Type_of_Load_to_Size_On: str
    Design_Outdoor_Air_Flow_Rate: str
    Central_Heating_Maximum_System_Air_Flow_Ratio: str
    Preheat_Design_Temperature: str
    Preheat_Design_Humidity_Ratio: str
    Precool_Design_Temperature: str
    Precool_Design_Humidity_Ratio: str
    Central_Cooling_Design_Supply_Air_Temperature: str
    Central_Heating_Design_Supply_Air_Temperature: str
    Type_of_Zone_Sum_to_Use: str
    _100_Outdoor_Air_in_Cooling: str
    _100_Outdoor_Air_in_Heating: str
    Central_Cooling_Design_Supply_Air_Humidity_Ratio: str
    Central_Heating_Design_Supply_Air_Humidity_Ratio: str
    Cooling_Supply_Air_Flow_Rate_Method: str
    Cooling_Supply_Air_Flow_Rate: str
    Cooling_Supply_Air_Flow_Rate_Per_Floor_Area: str
    Cooling_Fraction_of_Autosized_Cooling_Supply_Air_Flow_Rate: str
    Cooling_Supply_Air_Flow_Rate_Per_Unit_Cooling_Capacity: str
    Heating_Supply_Air_Flow_Rate_Method: str
    Heating_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate_Per_Floor_Area: str
    Heating_Fraction_of_Autosized_Heating_Supply_Air_Flow_Rate: str
    Heating_Fraction_of_Autosized_Cooling_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate_Per_Unit_Heating_Capacity: str
    System_Outdoor_Air_Method: str
    Zone_Maximum_Outdoor_Air_Fraction: str
    Cooling_Design_Capacity_Method: str
    Cooling_Design_Capacity: str
    Cooling_Design_Capacity_Per_Floor_Area: str
    Fraction_of_Autosized_Cooling_Design_Capacity: str
    Heating_Design_Capacity_Method: str
    Heating_Design_Capacity: str
    Heating_Design_Capacity_Per_Floor_Area: str
    Fraction_of_Autosized_Heating_Design_Capacity: str
    Central_Cooling_Capacity_Control_Method: str
    Occupant_Diversity: str

class SizingZoneType(TypedDict, total=False):
    """"dict for SizingZone"""
    Zone_or_ZoneList_Name: str
    Zone_Cooling_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Cooling_Design_Supply_Air_Temperature: str
    Zone_Cooling_Design_Supply_Air_Temperature_Difference: str
    Zone_Heating_Design_Supply_Air_Temperature_Input_Method: str
    Zone_Heating_Design_Supply_Air_Temperature: str
    Zone_Heating_Design_Supply_Air_Temperature_Difference: str
    Zone_Cooling_Design_Supply_Air_Humidity_Ratio: str
    Zone_Heating_Design_Supply_Air_Humidity_Ratio: str
    Design_Specification_Outdoor_Air_Object_Name: str
    Zone_Heating_Sizing_Factor: str
    Zone_Cooling_Sizing_Factor: str
    Cooling_Design_Air_Flow_Method: str
    Cooling_Design_Air_Flow_Rate: str
    Cooling_Minimum_Air_Flow_per_Zone_Floor_Area: str
    Cooling_Minimum_Air_Flow: str
    Cooling_Minimum_Air_Flow_Fraction: str
    Heating_Design_Air_Flow_Method: str
    Heating_Design_Air_Flow_Rate: str
    Heating_Maximum_Air_Flow_per_Zone_Floor_Area: str
    Heating_Maximum_Air_Flow: str
    Heating_Maximum_Air_Flow_Fraction: str
    Design_Specification_Zone_Air_Distribution_Object_Name: str
    Account_for_Dedicated_Outdoor_Air_System: str
    Dedicated_Outdoor_Air_System_Control_Strategy: str
    Dedicated_Outdoor_Air_Low_Setpoint_Temperature_for_Design: str
    Dedicated_Outdoor_Air_High_Setpoint_Temperature_for_Design: str
    Zone_Load_Sizing_Method: str
    Zone_Latent_Cooling_Design_Supply_Air_Humidity_Ratio_Input_Method: str
    Zone_Dehumidification_Design_Supply_Air_Humidity_Ratio: str
    Zone_Cooling_Design_Supply_Air_Humidity_Ratio_Difference: str
    Zone_Latent_Heating_Design_Supply_Air_Humidity_Ratio_Input_Method: str
    Zone_Humidification_Design_Supply_Air_Humidity_Ratio: str
    Zone_Humidification_Design_Supply_Air_Humidity_Ratio_Difference: str
    Zone_Humidistat_Dehumidification_Set_Point_Schedule_Name: str
    Zone_Humidistat_Humidification_Set_Point_Schedule_Name: str

class SizingperiodDesigndayType(TypedDict, total=False):
    """"dict for SizingperiodDesignday"""
    Name: str
    Month: str
    Day_of_Month: str
    Day_Type: str
    Maximum_DryBulb_Temperature: str
    Daily_DryBulb_Temperature_Range: str
    DryBulb_Temperature_Range_Modifier_Type: str
    DryBulb_Temperature_Range_Modifier_Day_Schedule_Name: str
    Humidity_Condition_Type: str
    Wetbulb_or_DewPoint_at_Maximum_DryBulb: str
    Humidity_Condition_Day_Schedule_Name: str
    Humidity_Ratio_at_Maximum_DryBulb: str
    Enthalpy_at_Maximum_DryBulb: str
    Daily_WetBulb_Temperature_Range: str
    Barometric_Pressure: str
    Wind_Speed: str
    Wind_Direction: str
    Rain_Indicator: str
    Snow_Indicator: str
    Daylight_Saving_Time_Indicator: str
    Solar_Model_Indicator: str
    Beam_Solar_Day_Schedule_Name: str
    Diffuse_Solar_Day_Schedule_Name: str
    ASHRAE_Clear_Sky_Optical_Depth_for_Beam_Irradiance_taub: str
    ASHRAE_Clear_Sky_Optical_Depth_for_Diffuse_Irradiance_taud: str
    Sky_Clearness: str
    Maximum_Number_Warmup_Days: str
    Begin_Environment_Reset_Mode: str

class SizingperiodWeatherfileconditiontypeType(TypedDict, total=False):
    """"dict for SizingperiodWeatherfileconditiontype"""
    Name: str
    Period_Selection: str
    Day_of_Week_for_Start_Day: str
    Use_Weather_File_Daylight_Saving_Period: str
    Use_Weather_File_Rain_and_Snow_Indicators: str

class SizingperiodWeatherfiledaysType(TypedDict, total=False):
    """"dict for SizingperiodWeatherfiledays"""
    Name: str
    Begin_Month: str
    Begin_Day_of_Month: str
    End_Month: str
    End_Day_of_Month: str
    Day_of_Week_for_Start_Day: str
    Use_Weather_File_Daylight_Saving_Period: str
    Use_Weather_File_Rain_and_Snow_Indicators: str

class SolarcollectorFlatplatePhotovoltaicthermalType(TypedDict, total=False):
    """"dict for SolarcollectorFlatplatePhotovoltaicthermal"""
    Name: str
    Surface_Name: str
    PhotovoltaicThermal_Model_Performance_Name: str
    Photovoltaic_Name: str
    Thermal_Working_Fluid_Type: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Design_Flow_Rate: str

class SolarcollectorFlatplateWaterType(TypedDict, total=False):
    """"dict for SolarcollectorFlatplateWater"""
    Name: str
    SolarCollectorPerformance_Name: str
    Surface_Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str
    Maximum_Flow_Rate: str

class SolarcollectorIntegralcollectorstorageType(TypedDict, total=False):
    """"dict for SolarcollectorIntegralcollectorstorage"""
    Name: str
    IntegralCollectorStorageParameters_Name: str
    Surface_Name: str
    Bottom_Surface_Boundary_Conditions_Type: str
    Boundary_Condition_Model_Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str
    Maximum_Flow_Rate: str

class SolarcollectorUnglazedtranspiredType(TypedDict, total=False):
    """"dict for SolarcollectorUnglazedtranspired"""
    Name: str
    Boundary_Conditions_Model_Name: str
    Availability_Schedule_Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str
    Setpoint_Node_Name: str
    Zone_Node_Name: str
    Free_Heating_Setpoint_Schedule_Name: str
    Diameter_of_Perforations_in_Collector: str
    Distance_Between_Perforations_in_Collector: str
    Thermal_Emissivity_of_Collector_Surface: str
    Solar_Absorbtivity_of_Collector_Surface: str
    Effective_Overall_Height_of_Collector: str
    Effective_Gap_Thickness_of_Plenum_Behind_Collector: str
    Effective_Cross_Section_Area_of_Plenum_Behind_Collector: str
    Hole_Layout_Pattern_for_Pitch: str
    Heat_Exchange_Effectiveness_Correlation: str
    Ratio_of_Actual_Collector_Surface_Area_to_Projected_Surface_Area: str
    Roughness_of_Collector: str
    Collector_Thickness: str
    Effectiveness_for_Perforations_with_Respect_to_Wind: str
    Discharge_Coefficient_for_Openings_with_Respect_to_Buoyancy_Driven_Flow: str
    Surface_1_Name: str
    Surface_2_Name: str
    Surface_3_Name: str
    Surface_4_Name: str
    Surface_5_Name: str
    Surface_6_Name: str
    Surface_7_Name: str
    Surface_8_Name: str
    Surface_9_Name: str
    Surface_10_Name: str

class SolarcollectorUnglazedtranspiredMultisystemType(TypedDict, total=False):
    """"dict for SolarcollectorUnglazedtranspiredMultisystem"""
    Solar_Collector_Name: str
    Outdoor_Air_System_1_Collector_Inlet_Node: str
    Outdoor_Air_System_1_Collector_Outlet_Node: str
    Outdoor_Air_System_1_Mixed_Air_Node: str
    Outdoor_Air_System_1_Zone_Node: str
    Outdoor_Air_System_2_Collector_Inlet_Node: str
    Outdoor_Air_System_2_Collector_Outlet_Node: str
    Outdoor_Air_System_2_Mixed_Air_Node: str
    Outdoor_Air_System_2_Zone_Node: str
    Outdoor_Air_System_3_Collector_Inlet_Node: str
    Outdoor_Air_System_3_Collector_Outlet_Node: str
    Outdoor_Air_System_3_Mixed_Air_Node: str
    Outdoor_Air_System_3_Zone_Node: str
    Outdoor_Air_System_4_Collector_Inlet_Node: str
    Outdoor_Air_System_4_Collector_Outlet_Node: str
    Outdoor_Air_System_4_Mixed_Air_Node: str
    Outdoor_Air_System_4_Zone_Node: str
    Outdoor_Air_System_5_Collector_Inlet_Node: str
    Outdoor_Air_System_5_Collector_Outlet_Node: str
    Outdoor_Air_System_5_Mixed_Air_Node: str
    Outdoor_Air_System_5_Zone_Node: str

class SolarcollectorperformanceFlatplateType(TypedDict, total=False):
    """"dict for SolarcollectorperformanceFlatplate"""
    Name: str
    Gross_Area: str
    Test_Fluid: str
    Test_Flow_Rate: str
    Test_Correlation_Type: str
    Coefficient_1_of_Efficiency_Equation: str
    Coefficient_2_of_Efficiency_Equation: str
    Coefficient_3_of_Efficiency_Equation: str
    Coefficient_2_of_Incident_Angle_Modifier: str
    Coefficient_3_of_Incident_Angle_Modifier: str

class SolarcollectorperformanceIntegralcollectorstorageType(TypedDict, total=False):
    """"dict for SolarcollectorperformanceIntegralcollectorstorage"""
    Name: str
    ICS_Collector_Type: str
    Gross_Area: str
    Collector_Water_Volume: str
    Bottom_Heat_Loss_Conductance: str
    Side_Heat_Loss_Conductance: str
    Aspect_Ratio: str
    Collector_Side_Height: str
    Thermal_Mass_of_Absorber_Plate: str
    Number_of_Covers: str
    Cover_Spacing: str
    Refractive_Index_of_Outer_Cover: str
    Extinction_Coefficient_Times_Thickness_of_Outer_Cover: str
    Emissivity_of_Outer_Cover: str
    Refractive_Index_of_Inner_Cover: str
    Extinction_Coefficient_Times_Thickness_of_the_inner_Cover: str
    Emissivity_of_Inner_Cover: str
    Absorptance_of_Absorber_Plate: str
    Emissivity_of_Absorber_Plate: str

class SolarcollectorperformancePhotovoltaicthermalBipvtType(TypedDict, total=False):
    """"dict for SolarcollectorperformancePhotovoltaicthermalBipvt"""
    Name: str
    Boundary_Conditions_Model_Name: str
    Availability_Schedule_Name: str
    Effective_Plenum_Gap_Thickness_Behind_PV_Modules: str
    PV_Cell_Normal_TransmittanceAbsorptance_Product: str
    Backing_Material_Normal_TransmittanceAbsorptance_Product: str
    Cladding_Normal_TransmittanceAbsorptance_Product: str
    Fraction_of_Collector_Gross_Area_Covered_by_PV_Module: str
    Fraction_of_PV_Cell_Area_to_PV_Module_Area: str
    PV_Module_Top_Thermal_Resistance: str
    PV_Module_Bottom_Thermal_Resistance: str
    PV_Module_Front_Longwave_Emissivity: str
    PV_Module_Back_Longwave_Emissivity: str
    Glass_Thickness: str
    Glass_Refraction_Index: str
    Glass_Extinction_Coefficient: str

class SolarcollectorperformancePhotovoltaicthermalSimpleType(TypedDict, total=False):
    """"dict for SolarcollectorperformancePhotovoltaicthermalSimple"""
    Name: str
    Fraction_of_Surface_Area_with_Active_Thermal_Collector: str
    Thermal_Conversion_Efficiency_Input_Mode_Type: str
    Value_for_Thermal_Conversion_Efficiency_if_Fixed: str
    Thermal_Conversion_Efficiency_Schedule_Name: str
    Front_Surface_Emittance: str

class SpaceType(TypedDict, total=False):
    """"dict for Space"""
    Name: str
    Zone_Name: str
    Ceiling_Height: str
    Volume: str
    Floor_Area: str
    Space_Type: str
    Tag_1: str
    Tag_2: str
    Tag_3: str

class SpacehvacEquipmentconnectionsType(TypedDict, total=False):
    """"dict for SpacehvacEquipmentconnections"""
    Space_Name: str
    Space_Air_Inlet_Node_or_NodeList_Name: str
    Space_Air_Exhaust_Node_or_NodeList_Name: str
    Space_Air_Node_Name: str
    Space_Return_Air_Node_or_NodeList_Name: str
    Space_Return_Air_Node_1_Flow_Rate_Fraction_Schedule_Name: str
    Space_Return_Air_Node_1_Flow_Rate_Basis_Node_or_NodeList_Name: str

class SpacehvacZoneequipmentmixerType(TypedDict, total=False):
    """"dict for SpacehvacZoneequipmentmixer"""
    Name: str
    Zone_Name: str
    Zone_Equipment_Inlet_Node_Name: str
    Space_Fraction_Method: str
    Space_1_Name: str
    Space_1_Fraction: str
    Space_1_Node_Name: str
    Space_2_Name: str
    Space_2_Fraction: str
    Space_2_Node_Name: str
    Space_3_Name: str
    Space_3_Fraction: str
    Space_3_Node_Name: str

class SpacehvacZoneequipmentsplitterType(TypedDict, total=False):
    """"dict for SpacehvacZoneequipmentsplitter"""
    Name: str
    Zone_Name: str
    Zone_Equipment_Object_Type: str
    Zone_Equipment_Name: str
    Zone_Equipment_Outlet_Node_Name: str
    Thermostat_Control_Method: str
    Control_Space_Name: str
    Space_Fraction_Method: str
    Space_1_Name: str
    Space_1_Fraction: str
    Space_1_Supply_Node_Name: str
    Space_2_Name: str
    Space_2_Fraction: str
    Space_2_Supply_Node_Name: str
    Space_3_Name: str
    Space_3_Fraction: str
    Space_3_Supply_Node_Name: str

class SpacelistType(TypedDict, total=False):
    """"dict for Spacelist"""
    Name: str
    Space_1_Name: str
    Space_2_Name: str
    Space_3_Name: str
    Space_4_Name: str
    Space_5_Name: str
    Space_6_Name: str
    Space_7_Name: str
    Space_8_Name: str
    Space_9_Name: str
    Space_10_Name: str
    Space_11_Name: str
    Space_12_Name: str
    Space_13_Name: str
    Space_14_Name: str
    Space_15_Name: str
    Space_16_Name: str
    Space_17_Name: str
    Space_18_Name: str
    Space_19_Name: str
    Space_20_Name: str
    Space_21_Name: str
    Space_22_Name: str
    Space_23_Name: str
    Space_24_Name: str
    Space_25_Name: str
    Space_26_Name: str
    Space_27_Name: str
    Space_28_Name: str
    Space_29_Name: str
    Space_30_Name: str
    Space_31_Name: str
    Space_32_Name: str
    Space_33_Name: str
    Space_34_Name: str
    Space_35_Name: str
    Space_36_Name: str
    Space_37_Name: str
    Space_38_Name: str
    Space_39_Name: str
    Space_40_Name: str
    Space_41_Name: str
    Space_42_Name: str
    Space_43_Name: str
    Space_44_Name: str
    Space_45_Name: str
    Space_46_Name: str
    Space_47_Name: str
    Space_48_Name: str
    Space_49_Name: str

class SteamequipmentType(TypedDict, total=False):
    """"dict for Steamequipment"""
    Name: str
    Zone_or_ZoneList_or_Space_or_SpaceList_Name: str
    Schedule_Name: str
    Design_Level_Calculation_Method: str
    Design_Level: str
    Power_per_Floor_Area: str
    Power_per_Person: str
    Fraction_Latent: str
    Fraction_Radiant: str
    Fraction_Lost: str
    EndUse_Subcategory: str

class SurfacecontaminantsourceandsinkGenericBoundarylayerdiffusionType(TypedDict, total=False):
    """"dict for SurfacecontaminantsourceandsinkGenericBoundarylayerdiffusion"""
    Name: str
    Surface_Name: str
    Mass_Transfer_Coefficient: str
    Schedule_Name: str
    Henry_Adsorption_Constant_or_Partition_Coefficient: str

class SurfacecontaminantsourceandsinkGenericDepositionvelocitysinkType(TypedDict, total=False):
    """"dict for SurfacecontaminantsourceandsinkGenericDepositionvelocitysink"""
    Name: str
    Surface_Name: str
    Deposition_Velocity: str
    Schedule_Name: str

class SurfacecontaminantsourceandsinkGenericPressuredrivenType(TypedDict, total=False):
    """"dict for SurfacecontaminantsourceandsinkGenericPressuredriven"""
    Name: str
    Surface_Name: str
    Design_Generation_Rate_Coefficient: str
    Generation_Schedule_Name: str
    Generation_Exponent: str

class SurfacecontrolMovableinsulationType(TypedDict, total=False):
    """"dict for SurfacecontrolMovableinsulation"""
    Insulation_Type: str
    Surface_Name: str
    Material_Name: str
    Schedule_Name: str

class SurfaceconvectionalgorithmInsideType(TypedDict, total=False):
    """"dict for SurfaceconvectionalgorithmInside"""
    Algorithm: str

class SurfaceconvectionalgorithmInsideAdaptivemodelselectionsType(TypedDict, total=False):
    """"dict for SurfaceconvectionalgorithmInsideAdaptivemodelselections"""
    Name: str
    Simple_Buoyancy_Vertical_Wall_Equation_Source: str
    Simple_Buoyancy_Vertical_Wall_User_Curve_Name: str
    Simple_Buoyancy_Stable_Horizontal_Equation_Source: str
    Simple_Buoyancy_Stable_Horizontal_Equation_User_Curve_Name: str
    Simple_Buoyancy_Unstable_Horizontal_Equation_Source: str
    Simple_Buoyancy_Unstable_Horizontal_Equation_User_Curve_Name: str
    Simple_Buoyancy_Stable_Tilted_Equation_Source: str
    Simple_Buoyancy_Stable_Tilted_Equation_User_Curve_Name: str
    Simple_Buoyancy_Unstable_Tilted_Equation_Source: str
    Simple_Buoyancy_Unstable_Tilted_Equation_User_Curve_Name: str
    Simple_Buoyancy_Windows_Equation_Source: str
    Simple_Buoyancy_Windows_Equation_User_Curve_Name: str
    Floor_Heat_Ceiling_Cool_Vertical_Wall_Equation_Source: str
    Floor_Heat_Ceiling_Cool_Vertical_Wall_Equation_User_Curve_Name: str
    Floor_Heat_Ceiling_Cool_Stable_Horizontal_Equation_Source: str
    Floor_Heat_Ceiling_Cool_Stable_Horizontal_Equation_User_Curve_Name: str
    Floor_Heat_Ceiling_Cool_Unstable_Horizontal_Equation_Source: str
    Floor_Heat_Ceiling_Cool_Unstable_Horizontal_Equation_User_Curve_Name: str
    Floor_Heat_Ceiling_Cool_Heated_Floor_Equation_Source: str
    Floor_Heat_Ceiling_Cool_Heated_Floor_Equation_User_Curve_Name: str
    Floor_Heat_Ceiling_Cool_Chilled_Ceiling_Equation_Source: str
    Floor_Heat_Ceiling_Cool_Chilled_Ceiling_Equation_User_Curve_Name: str
    Floor_Heat_Ceiling_Cool_Stable_Tilted_Equation_Source: str
    Floor_Heat_Ceiling_Cool_Stable_Tilted_Equation_User_Curve_Name: str
    Floor_Heat_Ceiling_Cool_Unstable_Tilted_Equation_Source: str
    Floor_Heat_Ceiling_Cool_Unstable_Tilted_Equation_User_Curve_Name: str
    Floor_Heat_Ceiling_Cool_Window_Equation_Source: str
    Floor_Heat_Ceiling_Cool_Window_Equation_User_Curve_Name: str
    Wall_Panel_Heating_Vertical_Wall_Equation_Source: str
    Wall_Panel_Heating_Vertical_Wall_Equation_User_Curve_Name: str
    Wall_Panel_Heating_Heated_Wall_Equation_Source: str
    Wall_Panel_Heating_Heated_Wall_Equation_User_Curve_Name: str
    Wall_Panel_Heating_Stable_Horizontal_Equation_Source: str
    Wall_Panel_Heating_Stable_Horizontal_Equation_User_Curve_Name: str
    Wall_Panel_Heating_Unstable_Horizontal_Equation_Source: str
    Wall_Panel_Heating_Unstable_Horizontal_Equation_User_Curve_Name: str
    Wall_Panel_Heating_Stable_Tilted_Equation_Source: str
    Wall_Panel_Heating_Stable_Tilted_Equation_User_Curve_Name: str
    Wall_Panel_Heating_Unstable_Tilted_Equation_Source: str
    Wall_Panel_Heating_Unstable_Tilted_Equation_User_Curve_Name: str
    Wall_Panel_Heating_Window_Equation_Source: str
    Wall_Panel_Heating_Window_Equation_User_Curve_Name: str
    Convective_Zone_Heater_Vertical_Wall_Equation_Source: str
    Convective_Zone_Heater_Vertical_Wall_Equation_User_Curve_Name: str
    Convective_Zone_Heater_Vertical_Walls_Near_Heater_Equation_Source: str
    Convective_Zone_Heater_Vertical_Walls_Near_Heater_Equation_User_Curve_Name: str
    Convective_Zone_Heater_Stable_Horizontal_Equation_Source: str
    Convective_Zone_Heater_Stable_Horizontal_Equation_User_Curve_Name: str
    Convective_Zone_Heater_Unstable_Horizontal_Equation_Source: str
    Convective_Zone_Heater_Unstable_Horizontal_Equation_User_Curve_Name: str
    Convective_Zone_Heater_Stable_Tilted_Equation_Source: str
    Convective_Zone_Heater_Stable_Tilted_Equation_User_Curve_Name: str
    Convective_Zone_Heater_Unstable_Tilted_Equation_Source: str
    Convective_Zone_Heater_Unstable_Tilted_Equation_User_Curve_Name: str
    Convective_Zone_Heater_Windows_Equation_Source: str
    Convective_Zone_Heater_Windows_Equation_User_Curve_Name: str
    Central_Air_Diffuser_Wall_Equation_Source: str
    Central_Air_Diffuser_Wall_Equation_User_Curve_Name: str
    Central_Air_Diffuser_Ceiling_Equation_Source: str
    Central_Air_Diffuser_Ceiling_Equation_User_Curve_Name: str
    Central_Air_Diffuser_Floor_Equation_Source: str
    Central_Air_Diffuser_Floor_Equation_User_Curve_Name: str
    Central_Air_Diffuser_Window_Equation_Source: str
    Central_Air_Diffuser_Window_Equation_User_Curve_Name: str
    Mechanical_Zone_Fan_Circulation_Vertical_Wall_Equation_Source: str
    Mechanical_Zone_Fan_Circulation_Vertical_Wall_Equation_User_Curve_Name: str
    Mechanical_Zone_Fan_Circulation_Stable_Horizontal_Equation_Source: str
    Mechanical_Zone_Fan_Circulation_Stable_Horizontal_Equation_User_Curve_Name: str
    Mechanical_Zone_Fan_Circulation_Unstable_Horizontal_Equation_Source: str
    Mechanical_Zone_Fan_Circulation_Unstable_Horizontal_Equation_User_Curve_Name: str
    Mechanical_Zone_Fan_Circulation_Stable_Tilted_Equation_Source: str
    Mechanical_Zone_Fan_Circulation_Stable_Tilted_Equation_User_Curve_Name: str
    Mechanical_Zone_Fan_Circulation_Unstable_Tilted_Equation_Source: str
    Mechanical_Zone_Fan_Circulation_Unstable_Tilted_Equation_User_Curve_Name: str
    Mechanical_Zone_Fan_Circulation_Window_Equation_Source: str
    Mechanical_Zone_Fan_Circulation_Window_Equation_User_Curve_Name: str
    Mixed_Regime_Buoyancy_Assisting_Flow_on_Walls_Equation_Source: str
    Mixed_Regime_Buoyancy_Assisting_Flow_on_Walls_Equation_User_Curve_Name: str
    Mixed_Regime_Buoyancy_Opposing_Flow_on_Walls_Equation_Source: str
    Mixed_Regime_Buoyancy_Opposing_Flow_on_Walls_Equation_User_Curve_Name: str
    Mixed_Regime_Stable_Floor_Equation_Source: str
    Mixed_Regime_Stable_Floor_Equation_User_Curve_Name: str
    Mixed_Regime_Unstable_Floor_Equation_Source: str
    Mixed_Regime_Unstable_Floor_Equation_User_Curve_Name: str
    Mixed_Regime_Stable_Ceiling_Equation_Source: str
    Mixed_Regime_Stable_Ceiling_Equation_User_Curve_Name: str
    Mixed_Regime_Unstable_Ceiling_Equation_Source: str
    Mixed_Regime_Unstable_Ceiling_Equation_User_Curve_Name: str
    Mixed_Regime_Window_Equation_Source: str
    Mixed_Regime_Window_Equation_User_Curve_Name: str

class SurfaceconvectionalgorithmInsideUsercurveType(TypedDict, total=False):
    """"dict for SurfaceconvectionalgorithmInsideUsercurve"""
    Name: str
    Reference_Temperature_for_Convection_Heat_Transfer: str
    Hc_Function_of_Temperature_Difference_Curve_Name: str
    Hc_Function_of_Temperature_Difference_Divided_by_Height_Curve_Name: str
    Hc_Function_of_Air_Change_Rate_Curve_Name: str
    Hc_Function_of_Air_System_Volume_Flow_Rate_Divided_by_Zone_Perimeter_Length_Curve_Name: str

class SurfaceconvectionalgorithmOutsideType(TypedDict, total=False):
    """"dict for SurfaceconvectionalgorithmOutside"""
    Algorithm: str

class SurfaceconvectionalgorithmOutsideAdaptivemodelselectionsType(TypedDict, total=False):
    """"dict for SurfaceconvectionalgorithmOutsideAdaptivemodelselections"""
    Name: str
    Wind_Convection_Windward_Vertical_Wall_Equation_Source: str
    Wind_Convection_Windward_Equation_Vertical_Wall_User_Curve_Name: str
    Wind_Convection_Leeward_Vertical_Wall_Equation_Source: str
    Wind_Convection_Leeward_Vertical_Wall_Equation_User_Curve_Name: str
    Wind_Convection_Horizontal_Roof_Equation_Source: str
    Wind_Convection_Horizontal_Roof_User_Curve_Name: str
    Natural_Convection_Vertical_Wall_Equation_Source: str
    Natural_Convection_Vertical_Wall_Equation_User_Curve_Name: str
    Natural_Convection_Stable_Horizontal_Equation_Source: str
    Natural_Convection_Stable_Horizontal_Equation_User_Curve_Name: str
    Natural_Convection_Unstable_Horizontal_Equation_Source: str
    Natural_Convection_Unstable_Horizontal_Equation_User_Curve_Name: str

class SurfaceconvectionalgorithmOutsideUsercurveType(TypedDict, total=False):
    """"dict for SurfaceconvectionalgorithmOutsideUsercurve"""
    Name: str
    Wind_Speed_Type_for_Curve: str
    Hf_Function_of_Wind_Speed_Curve_Name: str
    Hn_Function_of_Temperature_Difference_Curve_Name: str
    Hn_Function_of_Temperature_Difference_Divided_by_Height_Curve_Name: str

class SurfacepropertiesVaporcoefficientsType(TypedDict, total=False):
    """"dict for SurfacepropertiesVaporcoefficients"""
    Surface_Name: str
    Constant_External_Vapor_Transfer_Coefficient: str
    External_Vapor_Coefficient_Value: str
    Constant_Internal_vapor_Transfer_Coefficient: str
    Internal_Vapor_Coefficient_Value: str

class SurfacepropertyConvectioncoefficientsType(TypedDict, total=False):
    """"dict for SurfacepropertyConvectioncoefficients"""
    Surface_Name: str
    Convection_Coefficient_1_Location: str
    Convection_Coefficient_1_Type: str
    Convection_Coefficient_1: str
    Convection_Coefficient_1_Schedule_Name: str
    Convection_Coefficient_1_User_Curve_Name: str
    Convection_Coefficient_2_Location: str
    Convection_Coefficient_2_Type: str
    Convection_Coefficient_2: str
    Convection_Coefficient_2_Schedule_Name: str
    Convection_Coefficient_2_User_Curve_Name: str

class SurfacepropertyConvectioncoefficientsMultiplesurfaceType(TypedDict, total=False):
    """"dict for SurfacepropertyConvectioncoefficientsMultiplesurface"""
    Surface_Type: str
    Convection_Coefficient_1_Location: str
    Convection_Coefficient_1_Type: str
    Convection_Coefficient_1: str
    Convection_Coefficient_1_Schedule_Name: str
    Convection_Coefficient_1_User_Curve_Name: str
    Convection_Coefficient_2_Location: str
    Convection_Coefficient_2_Type: str
    Convection_Coefficient_2: str
    Convection_Coefficient_2_Schedule_Name: str
    Convection_Coefficient_2_User_Curve_Name: str

class SurfacepropertyExposedfoundationperimeterType(TypedDict, total=False):
    """"dict for SurfacepropertyExposedfoundationperimeter"""
    Surface_Name: str
    Exposed_Perimeter_Calculation_Method: str
    Total_Exposed_Perimeter: str
    Exposed_Perimeter_Fraction: str
    Surface_Segment_1_Exposed: str
    Surface_Segment_2_Exposed: str
    Surface_Segment_3_Exposed: str
    Surface_Segment_4_Exposed: str
    Surface_Segment_5_Exposed: str
    Surface_Segment_6_Exposed: str
    Surface_Segment_7_Exposed: str
    Surface_Segment_8_Exposed: str
    Surface_Segment_9_Exposed: str
    Surface_Segment_10_Exposed: str

class SurfacepropertyExteriornaturalventedcavityType(TypedDict, total=False):
    """"dict for SurfacepropertyExteriornaturalventedcavity"""
    Name: str
    Boundary_Conditions_Model_Name: str
    Area_Fraction_of_Openings: str
    Thermal_Emissivity_of_Exterior_Baffle_Material: str
    Solar_Absorbtivity_of_Exterior_Baffle: str
    Height_Scale_for_BuoyancyDriven_Ventilation: str
    Effective_Thickness_of_Cavity_Behind_Exterior_Baffle: str
    Ratio_of_Actual_Surface_Area_to_Projected_Surface_Area: str
    Roughness_of_Exterior_Surface: str
    Effectiveness_for_Perforations_with_Respect_to_Wind: str
    Discharge_Coefficient_for_Openings_with_Respect_to_Buoyancy_Driven_Flow: str
    Surface_1_Name: str
    Surface_2_Name: str
    Surface_3_Name: str
    Surface_4_Name: str
    Surface_5_Name: str
    Surface_6_Name: str
    Surface_7_Name: str
    Surface_8_Name: str
    Surface_9_Name: str
    Surface_10_Name: str

class SurfacepropertyGroundsurfacesType(TypedDict, total=False):
    """"dict for SurfacepropertyGroundsurfaces"""
    Name: str
    Ground_Surface_1_Name: str
    Ground_Surface_1_View_Factor: str
    Ground_Surface_1_Temperature_Schedule_Name: str
    Ground_Surface_1_Reflectance_Schedule_Name: str
    Ground_Surface_2_Name: str
    Ground_Surface_2_View_Factor: str
    Ground_Surface_2_Temperature_Schedule_Name: str
    Ground_Surface_2_Reflectance_Schedule_Name: str
    Ground_Surface_3_Name: str
    Ground_Surface_3_View_Factor: str
    Ground_Surface_3_Temperature_Schedule_Name: str
    Ground_Surface_3_Reflectance_Schedule_Name: str
    Ground_Surface_4_Name: str
    Ground_Surface_4_View_Factor: str
    Ground_Surface_4_Temperature_Schedule_Name: str
    Ground_Surface_4_Reflectance_Schedule_Name: str
    Ground_Surface_5_Name: str
    Ground_Surface_5_View_Factor: str
    Ground_Surface_5_Temperature_Schedule_Name: str
    Ground_Surface_5_Reflectance_Schedule_Name: str

class SurfacepropertyHeatbalancesourcetermType(TypedDict, total=False):
    """"dict for SurfacepropertyHeatbalancesourceterm"""
    Surface_Name: str
    Inside_Face_Heat_Source_Term_Schedule_Name: str
    Outside_Face_Heat_Source_Term_Schedule_Name: str

class SurfacepropertyHeattransferalgorithmType(TypedDict, total=False):
    """"dict for SurfacepropertyHeattransferalgorithm"""
    Surface_Name: str
    Algorithm: str

class SurfacepropertyHeattransferalgorithmConstructionType(TypedDict, total=False):
    """"dict for SurfacepropertyHeattransferalgorithmConstruction"""
    Name: str
    Algorithm: str
    Construction_Name: str

class SurfacepropertyHeattransferalgorithmMultiplesurfaceType(TypedDict, total=False):
    """"dict for SurfacepropertyHeattransferalgorithmMultiplesurface"""
    Name: str
    Surface_Type: str
    Algorithm: str

class SurfacepropertyHeattransferalgorithmSurfacelistType(TypedDict, total=False):
    """"dict for SurfacepropertyHeattransferalgorithmSurfacelist"""
    Name: str
    Algorithm: str
    Surface_Name_1: str
    Surface_Name_2: str
    Surface_Name_3: str
    Surface_Name_4: str
    Surface_Name_5: str
    Surface_Name_6: str

class SurfacepropertyIncidentsolarmultiplierType(TypedDict, total=False):
    """"dict for SurfacepropertyIncidentsolarmultiplier"""
    Surface_Name: str
    Incident_Solar_Multiplier: str
    Incident_Solar_Multiplier_Schedule_Name: str

class SurfacepropertyLocalenvironmentType(TypedDict, total=False):
    """"dict for SurfacepropertyLocalenvironment"""
    Name: str
    Exterior_Surface_Name: str
    Sunlit_Fraction_Schedule_Name: str
    Surrounding_Surfaces_Object_Name: str
    Outdoor_Air_Node_Name: str
    Ground_Surfaces_Object_Name: str

class SurfacepropertyOthersidecoefficientsType(TypedDict, total=False):
    """"dict for SurfacepropertyOthersidecoefficients"""
    Name: str
    Combined_ConvectiveRadiative_Film_Coefficient: str
    Constant_Temperature: str
    Constant_Temperature_Coefficient: str
    External_DryBulb_Temperature_Coefficient: str
    Ground_Temperature_Coefficient: str
    Wind_Speed_Coefficient: str
    Zone_Air_Temperature_Coefficient: str
    Constant_Temperature_Schedule_Name: str
    Sinusoidal_Variation_of_Constant_Temperature_Coefficient: str
    Period_of_Sinusoidal_Variation: str
    Previous_Other_Side_Temperature_Coefficient: str
    Minimum_Other_Side_Temperature_Limit: str
    Maximum_Other_Side_Temperature_Limit: str

class SurfacepropertyOthersideconditionsmodelType(TypedDict, total=False):
    """"dict for SurfacepropertyOthersideconditionsmodel"""
    Name: str
    Type_of_Modeling: str

class SurfacepropertySolarincidentinsideType(TypedDict, total=False):
    """"dict for SurfacepropertySolarincidentinside"""
    Name: str
    Surface_Name: str
    Construction_Name: str
    Inside_Surface_Incident_Sun_Solar_Radiation_Schedule_Name: str

class SurfacepropertySurroundingsurfacesType(TypedDict, total=False):
    """"dict for SurfacepropertySurroundingsurfaces"""
    Name: str
    Sky_View_Factor: str
    Sky_Temperature_Schedule_Name: str
    Ground_View_Factor: str
    Ground_Temperature_Schedule_Name: str
    Surrounding_Surface_1_Name: str
    Surrounding_Surface_1_View_Factor: str
    Surrounding_Surface_1_Temperature_Schedule_Name: str
    Surrounding_Surface_2_Name: str
    Surrounding_Surface_2_View_Factor: str
    Surrounding_Surface_2_Temperature_Schedule_Name: str
    Surrounding_Surface_3_Name: str
    Surrounding_Surface_3_View_Factor: str
    Surrounding_Surface_3_Temperature_Schedule_Name: str
    Surrounding_Surface_4_Name: str
    Surrounding_Surface_4_View_Factor: str
    Surrounding_Surface_4_Temperature_Schedule_Name: str
    Surrounding_Surface_5_Name: str
    Surrounding_Surface_5_View_Factor: str
    Surrounding_Surface_5_Temperature_Schedule_Name: str
    Surrounding_Surface_6_Name: str
    Surrounding_Surface_6_View_Factor: str
    Surrounding_Surface_6_Temperature_Schedule_Name: str
    Surrounding_Surface_7_Name: str
    Surrounding_Surface_7_View_Factor: str
    Surrounding_Surface_7_Temperature_Schedule_Name: str
    Surrounding_Surface_8_Name: str
    Surrounding_Surface_8_View_Factor: str
    Surrounding_Surface_8_Temperature_Schedule_Name: str
    Surrounding_Surface_9_Name: str
    Surrounding_Surface_9_View_Factor: str
    Surrounding_Surface_9_Temperature_Schedule_Name: str
    Surrounding_Surface_10_Name: str
    Surrounding_Surface_10_View_Factor: str
    Surrounding_Surface_10_Temperature_Schedule_Name: str

class SurfacepropertyUnderwaterType(TypedDict, total=False):
    """"dict for SurfacepropertyUnderwater"""
    Name: str
    Distance_from_Surface_Centroid_to_Leading_Edge_of_Boundary_Layer: str
    Free_Stream_Water_Temperature_Schedule: str
    Free_Stream_Water_Velocity_Schedule: str

class SwimmingpoolIndoorType(TypedDict, total=False):
    """"dict for SwimmingpoolIndoor"""
    Name: str
    Surface_Name: str
    Average_Depth: str
    Activity_Factor_Schedule_Name: str
    Makeup_Water_Supply_Schedule_Name: str
    Cover_Schedule_Name: str
    Cover_Evaporation_Factor: str
    Cover_Convection_Factor: str
    Cover_ShortWavelength_Radiation_Factor: str
    Cover_LongWavelength_Radiation_Factor: str
    Pool_Water_Inlet_Node: str
    Pool_Water_Outlet_Node: str
    Pool_Heating_System_Maximum_Water_Flow_Rate: str
    Pool_Miscellaneous_Equipment_Power: str
    Setpoint_Temperature_Schedule: str
    Maximum_Number_of_People: str
    People_Schedule: str
    People_Heat_Gain_Schedule: str

class TableIndependentvariableType(TypedDict, total=False):
    """"dict for TableIndependentvariable"""
    Name: str
    Interpolation_Method: str
    Extrapolation_Method: str
    Minimum_Value: str
    Maximum_Value: str
    Normalization_Reference_Value: str
    Unit_Type: str
    External_File_Name: str
    External_File_Column_Number: str
    External_File_Starting_Row_Number: str
    Value_1: str
    Value_2: str
    Value_3: str
    Value_4: str
    Value_5: str
    Value_6: str
    Value_7: str
    Value_8: str
    Value_9: str
    Value_10: str
    Value_11: str
    Value_12: str
    Value_13: str
    Value_14: str
    Value_15: str

class TableIndependentvariablelistType(TypedDict, total=False):
    """"dict for TableIndependentvariablelist"""
    Name: str
    Independent_Variable_1_Name: str
    Independent_Variable_2_Name: str
    Independent_Variable_3_Name: str
    Independent_Variable_4_Name: str
    Independent_Variable_5_Name: str
    Independent_Variable_6_Name: str

class TableLookupType(TypedDict, total=False):
    """"dict for TableLookup"""
    Name: str
    Independent_Variable_List_Name: str
    Normalization_Method: str
    Normalization_Divisor: str
    Minimum_Output: str
    Maximum_Output: str
    Output_Unit_Type: str
    External_File_Name: str
    External_File_Column_Number: str
    External_File_Starting_Row_Number: str
    Output_Value_1: str
    Output_Value_2: str
    Output_Value_3: str
    Output_Value_4: str
    Output_Value_5: str
    Output_Value_6: str
    Output_Value_7: str
    Output_Value_8: str
    Output_Value_9: str
    Output_Value_10: str
    Output_Value_11: str
    Output_Value_12: str
    Output_Value_13: str
    Output_Value_14: str
    Output_Value_15: str
    Output_Value_16: str
    Output_Value_17: str
    Output_Value_18: str
    Output_Value_19: str
    Output_Value_20: str
    Output_Value_21: str
    Output_Value_22: str
    Output_Value_23: str
    Output_Value_24: str
    Output_Value_25: str
    Output_Value_26: str
    Output_Value_27: str
    Output_Value_28: str
    Output_Value_29: str
    Output_Value_30: str
    Output_Value_31: str
    Output_Value_32: str
    Output_Value_33: str
    Output_Value_34: str
    Output_Value_35: str
    Output_Value_36: str
    Output_Value_37: str
    Output_Value_38: str
    Output_Value_39: str
    Output_Value_40: str
    Output_Value_41: str
    Output_Value_42: str
    Output_Value_43: str
    Output_Value_44: str
    Output_Value_45: str
    Output_Value_46: str
    Output_Value_47: str
    Output_Value_48: str
    Output_Value_49: str

class TemperingvalveType(TypedDict, total=False):
    """"dict for Temperingvalve"""
    Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str
    Stream_2_Source_Node_Name: str
    Temperature_Setpoint_Node_Name: str
    Pump_Outlet_Node_Name: str

class ThermalstorageChilledwaterMixedType(TypedDict, total=False):
    """"dict for ThermalstorageChilledwaterMixed"""
    Name: str
    Tank_Volume: str
    Setpoint_Temperature_Schedule_Name: str
    Deadband_Temperature_Difference: str
    Minimum_Temperature_Limit: str
    Nominal_Cooling_Capacity: str
    Ambient_Temperature_Indicator: str
    Ambient_Temperature_Schedule_Name: str
    Ambient_Temperature_Zone_Name: str
    Ambient_Temperature_Outdoor_Air_Node_Name: str
    Heat_Gain_Coefficient_from_Ambient_Temperature: str
    Use_Side_Inlet_Node_Name: str
    Use_Side_Outlet_Node_Name: str
    Use_Side_Heat_Transfer_Effectiveness: str
    Use_Side_Availability_Schedule_Name: str
    Use_Side_Design_Flow_Rate: str
    Source_Side_Inlet_Node_Name: str
    Source_Side_Outlet_Node_Name: str
    Source_Side_Heat_Transfer_Effectiveness: str
    Source_Side_Availability_Schedule_Name: str
    Source_Side_Design_Flow_Rate: str
    Tank_Recovery_Time: str

class ThermalstorageChilledwaterStratifiedType(TypedDict, total=False):
    """"dict for ThermalstorageChilledwaterStratified"""
    Name: str
    Tank_Volume: str
    Tank_Height: str
    Tank_Shape: str
    Tank_Perimeter: str
    Setpoint_Temperature_Schedule_Name: str
    Deadband_Temperature_Difference: str
    Temperature_Sensor_Height: str
    Minimum_Temperature_Limit: str
    Nominal_Cooling_Capacity: str
    Ambient_Temperature_Indicator: str
    Ambient_Temperature_Schedule_Name: str
    Ambient_Temperature_Zone_Name: str
    Ambient_Temperature_Outdoor_Air_Node_Name: str
    Uniform_Skin_Loss_Coefficient_per_Unit_Area_to_Ambient_Temperature: str
    Use_Side_Inlet_Node_Name: str
    Use_Side_Outlet_Node_Name: str
    Use_Side_Heat_Transfer_Effectiveness: str
    Use_Side_Availability_Schedule_Name: str
    Use_Side_Inlet_Height: str
    Use_Side_Outlet_Height: str
    Use_Side_Design_Flow_Rate: str
    Source_Side_Inlet_Node_Name: str
    Source_Side_Outlet_Node_Name: str
    Source_Side_Heat_Transfer_Effectiveness: str
    Source_Side_Availability_Schedule_Name: str
    Source_Side_Inlet_Height: str
    Source_Side_Outlet_Height: str
    Source_Side_Design_Flow_Rate: str
    Tank_Recovery_Time: str
    Inlet_Mode: str
    Number_of_Nodes: str
    Additional_Destratification_Conductivity: str
    Node_1_Additional_Loss_Coefficient: str
    Node_2_Additional_Loss_Coefficient: str
    Node_3_Additional_Loss_Coefficient: str
    Node_4_Additional_Loss_Coefficient: str
    Node_5_Additional_Loss_Coefficient: str
    Node_6_Additional_Loss_Coefficient: str
    Node_7_Additional_Loss_Coefficient: str
    Node_8_Additional_Loss_Coefficient: str
    Node_9_Additional_Loss_Coefficient: str
    Node_10_Additional_Loss_Coefficient: str

class ThermalstorageIceDetailedType(TypedDict, total=False):
    """"dict for ThermalstorageIceDetailed"""
    Name: str
    Availability_Schedule_Name: str
    Capacity: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str
    Discharging_Curve_Variable_Specifications: str
    Discharging_Curve_Name: str
    Charging_Curve_Variable_Specifications: str
    Charging_Curve_Name: str
    Timestep_of_the_Curve_Data: str
    Parasitic_Electric_Load_During_Discharging: str
    Parasitic_Electric_Load_During_Charging: str
    Tank_Loss_Coefficient: str
    Freezing_Temperature_of_Storage_Medium: str
    Thaw_Process_Indicator: str

class ThermalstorageIceSimpleType(TypedDict, total=False):
    """"dict for ThermalstorageIceSimple"""
    Name: str
    Ice_Storage_Type: str
    Capacity: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str

class ThermostatsetpointDualsetpointType(TypedDict, total=False):
    """"dict for ThermostatsetpointDualsetpoint"""
    Name: str
    Heating_Setpoint_Temperature_Schedule_Name: str
    Cooling_Setpoint_Temperature_Schedule_Name: str

class ThermostatsetpointSinglecoolingType(TypedDict, total=False):
    """"dict for ThermostatsetpointSinglecooling"""
    Name: str
    Setpoint_Temperature_Schedule_Name: str

class ThermostatsetpointSingleheatingType(TypedDict, total=False):
    """"dict for ThermostatsetpointSingleheating"""
    Name: str
    Setpoint_Temperature_Schedule_Name: str

class ThermostatsetpointSingleheatingorcoolingType(TypedDict, total=False):
    """"dict for ThermostatsetpointSingleheatingorcooling"""
    Name: str
    Setpoint_Temperature_Schedule_Name: str

class ThermostatsetpointThermalcomfortFangerDualsetpointType(TypedDict, total=False):
    """"dict for ThermostatsetpointThermalcomfortFangerDualsetpoint"""
    Name: str
    Fanger_Thermal_Comfort_Heating_Schedule_Name: str
    Fanger_Thermal_Comfort_Cooling_Schedule_Name: str

class ThermostatsetpointThermalcomfortFangerSinglecoolingType(TypedDict, total=False):
    """"dict for ThermostatsetpointThermalcomfortFangerSinglecooling"""
    Name: str
    Fanger_Thermal_Comfort_Schedule_Name: str

class ThermostatsetpointThermalcomfortFangerSingleheatingType(TypedDict, total=False):
    """"dict for ThermostatsetpointThermalcomfortFangerSingleheating"""
    Name: str
    Fanger_Thermal_Comfort_Schedule_Name: str

class ThermostatsetpointThermalcomfortFangerSingleheatingorcoolingType(TypedDict, total=False):
    """"dict for ThermostatsetpointThermalcomfortFangerSingleheatingorcooling"""
    Name: str
    Fanger_Thermal_Comfort_Schedule_Name: str

class TimestepType(TypedDict, total=False):
    """"dict for Timestep"""
    Number_of_Timesteps_per_Hour: str

class UnitarysystemperformanceMultispeedType(TypedDict, total=False):
    """"dict for UnitarysystemperformanceMultispeed"""
    Name: str
    Number_of_Speeds_for_Heating: str
    Number_of_Speeds_for_Cooling: str
    Single_Mode_Operation: str
    No_Load_Supply_Air_Flow_Rate_Ratio: str
    Heating_Speed_1_Supply_Air_Flow_Ratio: str
    Cooling_Speed_1_Supply_Air_Flow_Ratio: str
    Heating_Speed_2_Supply_Air_Flow_Ratio: str
    Cooling_Speed_2_Supply_Air_Flow_Ratio: str
    Heating_Speed_3_Supply_Air_Flow_Ratio: str
    Cooling_Speed_3_Supply_Air_Flow_Ratio: str
    Heating_Speed_4_Supply_Air_Flow_Ratio: str
    Cooling_Speed_4_Supply_Air_Flow_Ratio: str
    Heating_Speed_5_Supply_Air_Flow_Ratio: str
    Cooling_Speed_5_Supply_Air_Flow_Ratio: str
    Heating_Speed_6_Supply_Air_Flow_Ratio: str
    Cooling_Speed_6_Supply_Air_Flow_Ratio: str
    Heating_Speed_7_Supply_Air_Flow_Ratio: str
    Cooling_Speed_7_Supply_Air_Flow_Ratio: str
    Heating_Speed_8_Supply_Air_Flow_Ratio: str
    Cooling_Speed_8_Supply_Air_Flow_Ratio: str
    Heating_Speed_9_Supply_Air_Flow_Ratio: str
    Cooling_Speed_9_Supply_Air_Flow_Ratio: str
    Heating_Speed_10_Supply_Air_Flow_Ratio: str
    Cooling_Speed_10_Supply_Air_Flow_Ratio: str

class UtilitycostChargeBlockType(TypedDict, total=False):
    """"dict for UtilitycostChargeBlock"""
    Utility_Cost_Charge_Block_Name: str
    Tariff_Name: str
    Source_Variable: str
    Season: str
    Category_Variable_Name: str
    Remaining_Into_Variable: str
    Block_Size_Multiplier_Value_or_Variable_Name: str
    Block_Size_1_Value_or_Variable_Name: str
    Block_1_Cost_per_Unit_Value_or_Variable_Name: str
    Block_Size_2_Value_or_Variable_Name: str
    Block_2_Cost_per_Unit_Value_or_Variable_Name: str
    Block_Size_3_Value_or_Variable_Name: str
    Block_3_Cost_per_Unit_Value_or_Variable_Name: str
    Block_Size_4_Value_or_Variable_Name: str
    Block_4_Cost_per_Unit_Value_or_Variable_Name: str
    Block_Size_5_Value_or_Variable_Name: str
    Block_5_Cost_per_Unit_Value_or_Variable_Name: str
    Block_Size_6_Value_or_Variable_Name: str
    Block_6_Cost_per_Unit_Value_or_Variable_Name: str
    Block_Size_7_Value_or_Variable_Name: str
    Block_7_Cost_per_Unit_Value_or_Variable_Name: str
    Block_Size_8_Value_or_Variable_Name: str
    Block_8_Cost_per_Unit_Value_or_Variable_Name: str
    Block_Size_9_Value_or_Variable_Name: str
    Block_9_Cost_per_Unit_Value_or_Variable_Name: str
    Block_Size_10_Value_or_Variable_Name: str
    Block_10_Cost_per_Unit_Value_or_Variable_Name: str
    Block_Size_11_Value_or_Variable_Name: str
    Block_11_Cost_per_Unit_Value_or_Variable_Name: str
    Block_Size_12_Value_or_Variable_Name: str
    Block_12_Cost_per_Unit_Value_or_Variable_Name: str
    Block_Size_13_Value_or_Variable_Name: str
    Block_13_Cost_per_Unit_Value_or_Variable_Name: str
    Block_Size_14_Value_or_Variable_Name: str
    Block_14_Cost_per_Unit_Value_or_Variable_Name: str
    Block_Size_15_Value_or_Variable_Name: str
    Block_15_Cost_per_Unit_Value_or_Variable_Name: str

class UtilitycostChargeSimpleType(TypedDict, total=False):
    """"dict for UtilitycostChargeSimple"""
    Utility_Cost_Charge_Simple_Name: str
    Tariff_Name: str
    Source_Variable: str
    Season: str
    Category_Variable_Name: str
    Cost_per_Unit_Value_or_Variable_Name: str

class UtilitycostComputationType(TypedDict, total=False):
    """"dict for UtilitycostComputation"""
    Name: str
    Tariff_Name: str
    Compute_Step_1: str
    Compute_Step_2: str
    Compute_Step_3: str
    Compute_Step_4: str
    Compute_Step_5: str
    Compute_Step_6: str
    Compute_Step_7: str
    Compute_Step_8: str
    Compute_Step_9: str
    Compute_Step_10: str
    Compute_Step_11: str
    Compute_Step_12: str
    Compute_Step_13: str
    Compute_Step_14: str
    Compute_Step_15: str
    Compute_Step_16: str
    Compute_Step_17: str
    Compute_Step_18: str
    Compute_Step_19: str
    Compute_Step_20: str
    Compute_Step_21: str
    Compute_Step_22: str
    Compute_Step_23: str
    Compute_Step_24: str
    Compute_Step_25: str
    Compute_Step_26: str
    Compute_Step_27: str
    Compute_Step_28: str
    Compute_Step_29: str
    Compute_Step_30: str

class UtilitycostQualifyType(TypedDict, total=False):
    """"dict for UtilitycostQualify"""
    Utility_Cost_Qualify_Name: str
    Tariff_Name: str
    Variable_Name: str
    Qualify_Type: str
    Threshold_Value_or_Variable_Name: str
    Season: str
    Threshold_Test: str
    Number_of_Months: str

class UtilitycostRatchetType(TypedDict, total=False):
    """"dict for UtilitycostRatchet"""
    Name: str
    Tariff_Name: str
    Baseline_Source_Variable: str
    Adjustment_Source_Variable: str
    Season_From: str
    Season_To: str
    Multiplier_Value_or_Variable_Name: str
    Offset_Value_or_Variable_Name: str

class UtilitycostTariffType(TypedDict, total=False):
    """"dict for UtilitycostTariff"""
    Name: str
    Output_Meter_Name: str
    Conversion_Factor_Choice: str
    Energy_Conversion_Factor: str
    Demand_Conversion_Factor: str
    Time_of_Use_Period_Schedule_Name: str
    Season_Schedule_Name: str
    Month_Schedule_Name: str
    Demand_Window_Length: str
    Monthly_Charge_or_Variable_Name: str
    Minimum_Monthly_Charge_or_Variable_Name: str
    Real_Time_Pricing_Charge_Schedule_Name: str
    Customer_Baseline_Load_Schedule_Name: str
    Group_Name: str
    Buy_Or_Sell: str

class UtilitycostVariableType(TypedDict, total=False):
    """"dict for UtilitycostVariable"""
    Name: str
    Tariff_Name: str
    Variable_Type: str
    January_Value: str
    February_Value: str
    March_Value: str
    April_Value: str
    May_Value: str
    June_Value: str
    July_Value: str
    August_Value: str
    September_Value: str
    October_Value: str
    November_Value: str
    December_Value: str

class VersionType(TypedDict, total=False):
    """"dict for Version"""
    Version_Identifier: str

class WallAdiabaticType(TypedDict, total=False):
    """"dict for WallAdiabatic"""
    Name: str
    Construction_Name: str
    Zone_Name: str
    Space_Name: str
    Azimuth_Angle: str
    Tilt_Angle: str
    Starting_X_Coordinate: str
    Starting_Y_Coordinate: str
    Starting_Z_Coordinate: str
    Length: str
    Height: str

class WallDetailedType(TypedDict, total=False):
    """"dict for WallDetailed"""
    Name: str
    Construction_Name: str
    Zone_Name: str
    Space_Name: str
    Outside_Boundary_Condition: str
    Outside_Boundary_Condition_Object: str
    Sun_Exposure: str
    Wind_Exposure: str
    View_Factor_to_Ground: str
    Number_of_Vertices: str
    Vertex_1_Xcoordinate: str
    Vertex_1_Ycoordinate: str
    Vertex_1_Zcoordinate: str
    Vertex_2_Xcoordinate: str
    Vertex_2_Ycoordinate: str
    Vertex_2_Zcoordinate: str
    Vertex_3_Xcoordinate: str
    Vertex_3_Ycoordinate: str
    Vertex_3_Zcoordinate: str
    Vertex_4_Xcoordinate: str
    Vertex_4_Ycoordinate: str
    Vertex_4_Zcoordinate: str
    Vertex_5_Xcoordinate: str
    Vertex_5_Ycoordinate: str
    Vertex_5_Zcoordinate: str
    Vertex_6_Xcoordinate: str
    Vertex_6_Ycoordinate: str
    Vertex_6_Zcoordinate: str
    Vertex_7_Xcoordinate: str
    Vertex_7_Ycoordinate: str
    Vertex_7_Zcoordinate: str
    Vertex_8_Xcoordinate: str
    Vertex_8_Ycoordinate: str
    Vertex_8_Zcoordinate: str
    Vertex_9_Xcoordinate: str
    Vertex_9_Ycoordinate: str
    Vertex_9_Zcoordinate: str
    Vertex_10_Xcoordinate: str
    Vertex_10_Ycoordinate: str
    Vertex_10_Zcoordinate: str

class WallExteriorType(TypedDict, total=False):
    """"dict for WallExterior"""
    Name: str
    Construction_Name: str
    Zone_Name: str
    Space_Name: str
    Azimuth_Angle: str
    Tilt_Angle: str
    Starting_X_Coordinate: str
    Starting_Y_Coordinate: str
    Starting_Z_Coordinate: str
    Length: str
    Height: str

class WallInterzoneType(TypedDict, total=False):
    """"dict for WallInterzone"""
    Name: str
    Construction_Name: str
    Zone_Name: str
    Space_Name: str
    Outside_Boundary_Condition_Object: str
    Azimuth_Angle: str
    Tilt_Angle: str
    Starting_X_Coordinate: str
    Starting_Y_Coordinate: str
    Starting_Z_Coordinate: str
    Length: str
    Height: str

class WallUndergroundType(TypedDict, total=False):
    """"dict for WallUnderground"""
    Name: str
    Construction_Name: str
    Zone_Name: str
    Space_Name: str
    Azimuth_Angle: str
    Tilt_Angle: str
    Starting_X_Coordinate: str
    Starting_Y_Coordinate: str
    Starting_Z_Coordinate: str
    Length: str
    Height: str

class WaterheaterHeatpumpPumpedcondenserType(TypedDict, total=False):
    """"dict for WaterheaterHeatpumpPumpedcondenser"""
    Name: str
    Availability_Schedule_Name: str
    Compressor_Setpoint_Temperature_Schedule_Name: str
    Dead_Band_Temperature_Difference: str
    Condenser_Water_Inlet_Node_Name: str
    Condenser_Water_Outlet_Node_Name: str
    Condenser_Water_Flow_Rate: str
    Evaporator_Air_Flow_Rate: str
    Inlet_Air_Configuration: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Outdoor_Air_Node_Name: str
    Exhaust_Air_Node_Name: str
    Inlet_Air_Temperature_Schedule_Name: str
    Inlet_Air_Humidity_Schedule_Name: str
    Inlet_Air_Zone_Name: str
    Tank_Object_Type: str
    Tank_Name: str
    Tank_Use_Side_Inlet_Node_Name: str
    Tank_Use_Side_Outlet_Node_Name: str
    DX_Coil_Object_Type: str
    DX_Coil_Name: str
    Minimum_Inlet_Air_Temperature_for_Compressor_Operation: str
    Maximum_Inlet_Air_Temperature_for_Compressor_Operation: str
    Compressor_Location: str
    Compressor_Ambient_Temperature_Schedule_Name: str
    Fan_Object_Type: str
    Fan_Name: str
    Fan_Placement: str
    On_Cycle_Parasitic_Electric_Load: str
    Off_Cycle_Parasitic_Electric_Load: str
    Parasitic_Heat_Rejection_Location: str
    Inlet_Air_Mixer_Node_Name: str
    Outlet_Air_Splitter_Node_Name: str
    Inlet_Air_Mixer_Schedule_Name: str
    Tank_Element_Control_Logic: str
    Control_Sensor_1_Height_In_Stratified_Tank: str
    Control_Sensor_1_Weight: str
    Control_Sensor_2_Height_In_Stratified_Tank: str

class WaterheaterHeatpumpWrappedcondenserType(TypedDict, total=False):
    """"dict for WaterheaterHeatpumpWrappedcondenser"""
    Name: str
    Availability_Schedule_Name: str
    Compressor_Setpoint_Temperature_Schedule_Name: str
    Dead_Band_Temperature_Difference: str
    Condenser_Bottom_Location: str
    Condenser_Top_Location: str
    Evaporator_Air_Flow_Rate: str
    Inlet_Air_Configuration: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Outdoor_Air_Node_Name: str
    Exhaust_Air_Node_Name: str
    Inlet_Air_Temperature_Schedule_Name: str
    Inlet_Air_Humidity_Schedule_Name: str
    Inlet_Air_Zone_Name: str
    Tank_Object_Type: str
    Tank_Name: str
    Tank_Use_Side_Inlet_Node_Name: str
    Tank_Use_Side_Outlet_Node_Name: str
    DX_Coil_Object_Type: str
    DX_Coil_Name: str
    Minimum_Inlet_Air_Temperature_for_Compressor_Operation: str
    Maximum_Inlet_Air_Temperature_for_Compressor_Operation: str
    Compressor_Location: str
    Compressor_Ambient_Temperature_Schedule_Name: str
    Fan_Object_Type: str
    Fan_Name: str
    Fan_Placement: str
    On_Cycle_Parasitic_Electric_Load: str
    Off_Cycle_Parasitic_Electric_Load: str
    Parasitic_Heat_Rejection_Location: str
    Inlet_Air_Mixer_Node_Name: str
    Outlet_Air_Splitter_Node_Name: str
    Inlet_Air_Mixer_Schedule_Name: str
    Tank_Element_Control_Logic: str
    Control_Sensor_1_Height_In_Stratified_Tank: str
    Control_Sensor_1_Weight: str
    Control_Sensor_2_Height_In_Stratified_Tank: str

class WaterheaterMixedType(TypedDict, total=False):
    """"dict for WaterheaterMixed"""
    Name: str
    Tank_Volume: str
    Setpoint_Temperature_Schedule_Name: str
    Deadband_Temperature_Difference: str
    Maximum_Temperature_Limit: str
    Heater_Control_Type: str
    Heater_Maximum_Capacity: str
    Heater_Minimum_Capacity: str
    Heater_Ignition_Minimum_Flow_Rate: str
    Heater_Ignition_Delay: str
    Heater_Fuel_Type: str
    Heater_Thermal_Efficiency: str
    Part_Load_Factor_Curve_Name: str
    Off_Cycle_Parasitic_Fuel_Consumption_Rate: str
    Off_Cycle_Parasitic_Fuel_Type: str
    Off_Cycle_Parasitic_Heat_Fraction_to_Tank: str
    On_Cycle_Parasitic_Fuel_Consumption_Rate: str
    On_Cycle_Parasitic_Fuel_Type: str
    On_Cycle_Parasitic_Heat_Fraction_to_Tank: str
    Ambient_Temperature_Indicator: str
    Ambient_Temperature_Schedule_Name: str
    Ambient_Temperature_Zone_Name: str
    Ambient_Temperature_Outdoor_Air_Node_Name: str
    Off_Cycle_Loss_Coefficient_to_Ambient_Temperature: str
    Off_Cycle_Loss_Fraction_to_Zone: str
    On_Cycle_Loss_Coefficient_to_Ambient_Temperature: str
    On_Cycle_Loss_Fraction_to_Zone: str
    Peak_Use_Flow_Rate: str
    Use_Flow_Rate_Fraction_Schedule_Name: str
    Cold_Water_Supply_Temperature_Schedule_Name: str
    Use_Side_Inlet_Node_Name: str
    Use_Side_Outlet_Node_Name: str
    Use_Side_Effectiveness: str
    Source_Side_Inlet_Node_Name: str
    Source_Side_Outlet_Node_Name: str
    Source_Side_Effectiveness: str
    Use_Side_Design_Flow_Rate: str
    Source_Side_Design_Flow_Rate: str
    Indirect_Water_Heating_Recovery_Time: str
    Source_Side_Flow_Control_Mode: str
    Indirect_Alternate_Setpoint_Temperature_Schedule_Name: str
    EndUse_Subcategory: str

class WaterheaterSizingType(TypedDict, total=False):
    """"dict for WaterheaterSizing"""
    WaterHeater_Name: str
    Design_Mode: str
    Time_Storage_Can_Meet_Peak_Draw: str
    Time_for_Tank_Recovery: str
    Nominal_Tank_Volume_for_Autosizing_Plant_Connections: str
    Number_of_Bedrooms: str
    Number_of_Bathrooms: str
    Storage_Capacity_per_Person: str
    Recovery_Capacity_per_Person: str
    Storage_Capacity_per_Floor_Area: str
    Recovery_Capacity_per_Floor_Area: str
    Number_of_Units: str
    Storage_Capacity_per_Unit: str
    Recovery_Capacity_PerUnit: str
    Storage_Capacity_per_Collector_Area: str
    Height_Aspect_Ratio: str

class WaterheaterStratifiedType(TypedDict, total=False):
    """"dict for WaterheaterStratified"""
    Name: str
    EndUse_Subcategory: str
    Tank_Volume: str
    Tank_Height: str
    Tank_Shape: str
    Tank_Perimeter: str
    Maximum_Temperature_Limit: str
    Heater_Priority_Control: str
    Heater_1_Setpoint_Temperature_Schedule_Name: str
    Heater_1_Deadband_Temperature_Difference: str
    Heater_1_Capacity: str
    Heater_1_Height: str
    Heater_2_Setpoint_Temperature_Schedule_Name: str
    Heater_2_Deadband_Temperature_Difference: str
    Heater_2_Capacity: str
    Heater_2_Height: str
    Heater_Fuel_Type: str
    Heater_Thermal_Efficiency: str
    Off_Cycle_Parasitic_Fuel_Consumption_Rate: str
    Off_Cycle_Parasitic_Fuel_Type: str
    Off_Cycle_Parasitic_Heat_Fraction_to_Tank: str
    Off_Cycle_Parasitic_Height: str
    On_Cycle_Parasitic_Fuel_Consumption_Rate: str
    On_Cycle_Parasitic_Fuel_Type: str
    On_Cycle_Parasitic_Heat_Fraction_to_Tank: str
    On_Cycle_Parasitic_Height: str
    Ambient_Temperature_Indicator: str
    Ambient_Temperature_Schedule_Name: str
    Ambient_Temperature_Zone_Name: str
    Ambient_Temperature_Outdoor_Air_Node_Name: str
    Uniform_Skin_Loss_Coefficient_per_Unit_Area_to_Ambient_Temperature: str
    Skin_Loss_Fraction_to_Zone: str
    Off_Cycle_Flue_Loss_Coefficient_to_Ambient_Temperature: str
    Off_Cycle_Flue_Loss_Fraction_to_Zone: str
    Peak_Use_Flow_Rate: str
    Use_Flow_Rate_Fraction_Schedule_Name: str
    Cold_Water_Supply_Temperature_Schedule_Name: str
    Use_Side_Inlet_Node_Name: str
    Use_Side_Outlet_Node_Name: str
    Use_Side_Effectiveness: str
    Use_Side_Inlet_Height: str
    Use_Side_Outlet_Height: str
    Source_Side_Inlet_Node_Name: str
    Source_Side_Outlet_Node_Name: str
    Source_Side_Effectiveness: str
    Source_Side_Inlet_Height: str
    Source_Side_Outlet_Height: str
    Inlet_Mode: str
    Use_Side_Design_Flow_Rate: str
    Source_Side_Design_Flow_Rate: str
    Indirect_Water_Heating_Recovery_Time: str
    Number_of_Nodes: str
    Additional_Destratification_Conductivity: str
    Node_1_Additional_Loss_Coefficient: str
    Node_2_Additional_Loss_Coefficient: str
    Node_3_Additional_Loss_Coefficient: str
    Node_4_Additional_Loss_Coefficient: str
    Node_5_Additional_Loss_Coefficient: str
    Node_6_Additional_Loss_Coefficient: str
    Node_7_Additional_Loss_Coefficient: str
    Node_8_Additional_Loss_Coefficient: str
    Node_9_Additional_Loss_Coefficient: str
    Node_10_Additional_Loss_Coefficient: str
    Node_11_Additional_Loss_Coefficient: str
    Node_12_Additional_Loss_Coefficient: str
    Source_Side_Flow_Control_Mode: str
    Indirect_Alternate_Setpoint_Temperature_Schedule_Name: str

class WateruseConnectionsType(TypedDict, total=False):
    """"dict for WateruseConnections"""
    Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str
    Supply_Water_Storage_Tank_Name: str
    Reclamation_Water_Storage_Tank_Name: str
    Hot_Water_Supply_Temperature_Schedule_Name: str
    Cold_Water_Supply_Temperature_Schedule_Name: str
    Drain_Water_Heat_Exchanger_Type: str
    Drain_Water_Heat_Exchanger_Destination: str
    Drain_Water_Heat_Exchanger_UFactor_Times_Area: str
    Water_Use_Equipment_1_Name: str
    Water_Use_Equipment_2_Name: str
    Water_Use_Equipment_3_Name: str
    Water_Use_Equipment_4_Name: str
    Water_Use_Equipment_5_Name: str
    Water_Use_Equipment_6_Name: str
    Water_Use_Equipment_7_Name: str
    Water_Use_Equipment_8_Name: str
    Water_Use_Equipment_9_Name: str
    Water_Use_Equipment_10_Name: str

class WateruseEquipmentType(TypedDict, total=False):
    """"dict for WateruseEquipment"""
    Name: str
    EndUse_Subcategory: str
    Peak_Flow_Rate: str
    Flow_Rate_Fraction_Schedule_Name: str
    Target_Temperature_Schedule_Name: str
    Hot_Water_Supply_Temperature_Schedule_Name: str
    Cold_Water_Supply_Temperature_Schedule_Name: str
    Zone_Name: str
    Sensible_Fraction_Schedule_Name: str
    Latent_Fraction_Schedule_Name: str

class WateruseRaincollectorType(TypedDict, total=False):
    """"dict for WateruseRaincollector"""
    Name: str
    Storage_Tank_Name: str
    Loss_Factor_Mode: str
    Collection_Loss_Factor: str
    Collection_Loss_Factor_Schedule_Name: str
    Maximum_Collection_Rate: str
    Collection_Surface_1_Name: str
    Collection_Surface_2_Name: str
    Collection_Surface_3_Name: str
    Collection_Surface_4_Name: str
    Collection_Surface_5_Name: str
    Collection_Surface_6_Name: str
    Collection_Surface_7_Name: str
    Collection_Surface_8_Name: str
    Collection_Surface_9_Name: str
    Collection_Surface_10_Name: str

class WateruseStorageType(TypedDict, total=False):
    """"dict for WateruseStorage"""
    Name: str
    Water_Quality_Subcategory: str
    Maximum_Capacity: str
    Initial_Volume: str
    Design_In_Flow_Rate: str
    Design_Out_Flow_Rate: str
    Overflow_Destination: str
    Type_of_Supply_Controlled_by_Float_Valve: str
    Float_Valve_On_Capacity: str
    Float_Valve_Off_Capacity: str
    Backup_Mains_Capacity: str
    Other_Tank_Name: str
    Water_Thermal_Mode: str
    Water_Temperature_Schedule_Name: str
    Ambient_Temperature_Indicator: str
    Ambient_Temperature_Schedule_Name: str
    Zone_Name: str
    Tank_Surface_Area: str
    Tank_U_Value: str
    Tank_Outside_Surface_Material_Name: str

class WateruseWellType(TypedDict, total=False):
    """"dict for WateruseWell"""
    Name: str
    Storage_Tank_Name: str
    Pump_Depth: str
    Pump_Rated_Flow_Rate: str
    Pump_Rated_Head: str
    Pump_Rated_Power_Consumption: str
    Pump_Efficiency: str
    Well_Recovery_Rate: str
    Nominal_Well_Storage_Volume: str
    Water_Table_Depth_Mode: str
    Water_Table_Depth: str
    Water_Table_Depth_Schedule_Name: str

class WeatherpropertySkytemperatureType(TypedDict, total=False):
    """"dict for WeatherpropertySkytemperature"""
    Name: str
    Calculation_Type: str
    Schedule_Name: str
    Use_Weather_File_Horizontal_IR: str

class WindowType(TypedDict, total=False):
    """"dict for Window"""
    Name: str
    Construction_Name: str
    Building_Surface_Name: str
    Frame_and_Divider_Name: str
    Multiplier: str
    Starting_X_Coordinate: str
    Starting_Z_Coordinate: str
    Length: str
    Height: str

class WindowInterzoneType(TypedDict, total=False):
    """"dict for WindowInterzone"""
    Name: str
    Construction_Name: str
    Building_Surface_Name: str
    Outside_Boundary_Condition_Object: str
    Multiplier: str
    Starting_X_Coordinate: str
    Starting_Z_Coordinate: str
    Length: str
    Height: str

class WindowgapDeflectionstateType(TypedDict, total=False):
    """"dict for WindowgapDeflectionstate"""
    Name: str
    Deflected_Thickness: str
    Initial_Temperature: str
    Initial_Pressure: str

class WindowgapSupportpillarType(TypedDict, total=False):
    """"dict for WindowgapSupportpillar"""
    Name: str
    Spacing: str
    Radius: str

class WindowmaterialBlindType(TypedDict, total=False):
    """"dict for WindowmaterialBlind"""
    Name: str
    Slat_Orientation: str
    Slat_Width: str
    Slat_Separation: str
    Slat_Thickness: str
    Slat_Angle: str
    Slat_Conductivity: str
    Slat_Beam_Solar_Transmittance: str
    Front_Side_Slat_Beam_Solar_Reflectance: str
    Back_Side_Slat_Beam_Solar_Reflectance: str
    Slat_Diffuse_Solar_Transmittance: str
    Front_Side_Slat_Diffuse_Solar_Reflectance: str
    Back_Side_Slat_Diffuse_Solar_Reflectance: str
    Slat_Beam_Visible_Transmittance: str
    Front_Side_Slat_Beam_Visible_Reflectance: str
    Back_Side_Slat_Beam_Visible_Reflectance: str
    Slat_Diffuse_Visible_Transmittance: str
    Front_Side_Slat_Diffuse_Visible_Reflectance: str
    Back_Side_Slat_Diffuse_Visible_Reflectance: str
    Slat_Infrared_Hemispherical_Transmittance: str
    Front_Side_Slat_Infrared_Hemispherical_Emissivity: str
    Back_Side_Slat_Infrared_Hemispherical_Emissivity: str
    Blind_to_Glass_Distance: str
    Blind_Top_Opening_Multiplier: str
    Blind_Bottom_Opening_Multiplier: str
    Blind_Left_Side_Opening_Multiplier: str
    Blind_Right_Side_Opening_Multiplier: str
    Minimum_Slat_Angle: str
    Maximum_Slat_Angle: str

class WindowmaterialBlindEquivalentlayerType(TypedDict, total=False):
    """"dict for WindowmaterialBlindEquivalentlayer"""
    Name: str
    Slat_Orientation: str
    Slat_Width: str
    Slat_Separation: str
    Slat_Crown: str
    Slat_Angle: str
    Front_Side_Slat_BeamDiffuse_Solar_Transmittance: str
    Back_Side_Slat_BeamDiffuse_Solar_Transmittance: str
    Front_Side_Slat_BeamDiffuse_Solar_Reflectance: str
    Back_Side_Slat_BeamDiffuse_Solar_Reflectance: str
    Front_Side_Slat_BeamDiffuse_Visible_Transmittance: str
    Back_Side_Slat_BeamDiffuse_Visible_Transmittance: str
    Front_Side_Slat_BeamDiffuse_Visible_Reflectance: str
    Back_Side_Slat_BeamDiffuse_Visible_Reflectance: str
    Slat_DiffuseDiffuse_Solar_Transmittance: str
    Front_Side_Slat_DiffuseDiffuse_Solar_Reflectance: str
    Back_Side_Slat_DiffuseDiffuse_Solar_Reflectance: str
    Slat_DiffuseDiffuse_Visible_Transmittance: str
    Front_Side_Slat_DiffuseDiffuse_Visible_Reflectance: str
    Back_Side_Slat_DiffuseDiffuse_Visible_Reflectance: str
    Slat_Infrared_Transmittance: str
    Front_Side_Slat_Infrared_Emissivity: str
    Back_Side_Slat_Infrared_Emissivity: str
    Slat_Angle_Control: str

class WindowmaterialComplexshadeType(TypedDict, total=False):
    """"dict for WindowmaterialComplexshade"""
    Name: str
    Layer_Type: str
    Thickness: str
    Conductivity: str
    IR_Transmittance: str
    Front_Emissivity: str
    Back_Emissivity: str
    Top_Opening_Multiplier: str
    Bottom_Opening_Multiplier: str
    Left_Side_Opening_Multiplier: str
    Right_Side_Opening_Multiplier: str
    Front_Opening_Multiplier: str
    Slat_Width: str
    Slat_Spacing: str
    Slat_Thickness: str
    Slat_Angle: str
    Slat_Conductivity: str
    Slat_Curve: str

class WindowmaterialDrapeEquivalentlayerType(TypedDict, total=False):
    """"dict for WindowmaterialDrapeEquivalentlayer"""
    Name: str
    Drape_BeamBeam_Solar_Transmittance_at_Normal_Incidence: str
    Front_Side_Drape_BeamDiffuse_Solar_Transmittance: str
    Back_Side_Drape_BeamDiffuse_Solar_Transmittance: str
    Front_Side_Drape_BeamDiffuse_Solar_Reflectance: str
    Back_Side_Drape_BeamDiffuse_Solar_Reflectance: str
    Drape_BeamBeam_Visible_Transmittance: str
    Drape_BeamDiffuse_Visible_Transmittance: str
    Drape_BeamDiffuse_Visible_Reflectance: str
    Drape_Material_Infrared_Transmittance: str
    Front_Side_Drape_Material_Infrared_Emissivity: str
    Back_Side_Drape_Material_Infrared_Emissivity: str
    Width_of_Pleated_Fabric: str
    Length_of_Pleated_Fabric: str

class WindowmaterialGapType(TypedDict, total=False):
    """"dict for WindowmaterialGap"""
    Name: str
    Thickness: str
    Gas_or_Gas_Mixture: str
    Pressure: str
    Deflection_State: str
    Support_Pillar: str

class WindowmaterialGapEquivalentlayerType(TypedDict, total=False):
    """"dict for WindowmaterialGapEquivalentlayer"""
    Name: str
    Gas_Type: str
    Thickness: str
    Gap_Vent_Type: str
    Conductivity_Coefficient_A: str
    Conductivity_Coefficient_B: str
    Conductivity_Coefficient_C: str
    Viscosity_Coefficient_A: str
    Viscosity_Coefficient_B: str
    Viscosity_Coefficient_C: str
    Specific_Heat_Coefficient_A: str
    Specific_Heat_Coefficient_B: str
    Specific_Heat_Coefficient_C: str
    Molecular_Weight: str
    Specific_Heat_Ratio: str

class WindowmaterialGasType(TypedDict, total=False):
    """"dict for WindowmaterialGas"""
    Name: str
    Gas_Type: str
    Thickness: str
    Conductivity_Coefficient_A: str
    Conductivity_Coefficient_B: str
    Conductivity_Coefficient_C: str
    Viscosity_Coefficient_A: str
    Viscosity_Coefficient_B: str
    Viscosity_Coefficient_C: str
    Specific_Heat_Coefficient_A: str
    Specific_Heat_Coefficient_B: str
    Specific_Heat_Coefficient_C: str
    Molecular_Weight: str
    Specific_Heat_Ratio: str

class WindowmaterialGasmixtureType(TypedDict, total=False):
    """"dict for WindowmaterialGasmixture"""
    Name: str
    Thickness: str
    Number_of_Gases_in_Mixture: str
    Gas_1_Type: str
    Gas_1_Fraction: str
    Gas_2_Type: str
    Gas_2_Fraction: str
    Gas_3_Type: str
    Gas_3_Fraction: str
    Gas_4_Type: str
    Gas_4_Fraction: str

class WindowmaterialGlazingType(TypedDict, total=False):
    """"dict for WindowmaterialGlazing"""
    Name: str
    Optical_Data_Type: str
    Window_Glass_Spectral_Data_Set_Name: str
    Thickness: str
    Solar_Transmittance_at_Normal_Incidence: str
    Front_Side_Solar_Reflectance_at_Normal_Incidence: str
    Back_Side_Solar_Reflectance_at_Normal_Incidence: str
    Visible_Transmittance_at_Normal_Incidence: str
    Front_Side_Visible_Reflectance_at_Normal_Incidence: str
    Back_Side_Visible_Reflectance_at_Normal_Incidence: str
    Infrared_Transmittance_at_Normal_Incidence: str
    Front_Side_Infrared_Hemispherical_Emissivity: str
    Back_Side_Infrared_Hemispherical_Emissivity: str
    Conductivity: str
    Dirt_Correction_Factor_for_Solar_and_Visible_Transmittance: str
    Solar_Diffusing: str
    Youngs_modulus: str
    Poissons_ratio: str
    Window_Glass_Spectral_and_Incident_Angle_Transmittance_Data_Set_Table_Name: str
    Window_Glass_Spectral_and_Incident_Angle_Front_Reflectance_Data_Set_Table_Name: str
    Window_Glass_Spectral_and_Incident_Angle_Back_Reflectance_Data_Set_Table_Name: str

class WindowmaterialGlazingEquivalentlayerType(TypedDict, total=False):
    """"dict for WindowmaterialGlazingEquivalentlayer"""
    Name: str
    Optical_Data_Type: str
    Window_Glass_Spectral_Data_Set_Name: str
    Front_Side_BeamBeam_Solar_Transmittance: str
    Back_Side_BeamBeam_Solar_Transmittance: str
    Front_Side_BeamBeam_Solar_Reflectance: str
    Back_Side_BeamBeam_Solar_Reflectance: str
    Front_Side_BeamBeam_Visible_Solar_Transmittance: str
    Back_Side_BeamBeam_Visible_Solar_Transmittance: str
    Front_Side_BeamBeam_Visible_Solar_Reflectance: str
    Back_Side_BeamBeam_Visible_Solar_Reflectance: str
    Front_Side_BeamDiffuse_Solar_Transmittance: str
    Back_Side_BeamDiffuse_Solar_Transmittance: str
    Front_Side_BeamDiffuse_Solar_Reflectance: str
    Back_Side_BeamDiffuse_Solar_Reflectance: str
    Front_Side_BeamDiffuse_Visible_Solar_Transmittance: str
    Back_Side_BeamDiffuse_Visible_Solar_Transmittance: str
    Front_Side_BeamDiffuse_Visible_Solar_Reflectance: str
    Back_Side_BeamDiffuse_Visible_Solar_Reflectance: str
    DiffuseDiffuse_Solar_Transmittance: str
    Front_Side_DiffuseDiffuse_Solar_Reflectance: str
    Back_Side_DiffuseDiffuse_Solar_Reflectance: str
    DiffuseDiffuse_Visible_Solar_Transmittance: str
    Front_Side_DiffuseDiffuse_Visible_Solar_Reflectance: str
    Back_Side_DiffuseDiffuse_Visible_Solar_Reflectance: str
    Infrared_Transmittance_applies_to_front_and_back: str
    Front_Side_Infrared_Emissivity: str
    Back_Side_Infrared_Emissivity: str
    Thermal_Resistance: str

class WindowmaterialGlazingRefractionextinctionmethodType(TypedDict, total=False):
    """"dict for WindowmaterialGlazingRefractionextinctionmethod"""
    Name: str
    Thickness: str
    Solar_Index_of_Refraction: str
    Solar_Extinction_Coefficient: str
    Visible_Index_of_Refraction: str
    Visible_Extinction_Coefficient: str
    Infrared_Transmittance_at_Normal_Incidence: str
    Infrared_Hemispherical_Emissivity: str
    Conductivity: str
    Dirt_Correction_Factor_for_Solar_and_Visible_Transmittance: str
    Solar_Diffusing: str

class WindowmaterialGlazinggroupThermochromicType(TypedDict, total=False):
    """"dict for WindowmaterialGlazinggroupThermochromic"""
    Name: str
    Optical_Data_Temperature_1: str
    Window_Material_Glazing_Name_1: str
    Optical_Data_Temperature_2: str
    Window_Material_Glazing_Name_2: str
    Optical_Data_Temperature_3: str
    Window_Material_Glazing_Name_3: str
    Optical_Data_Temperature_4: str
    Window_Material_Glazing_Name_4: str
    Optical_Data_Temperature_5: str
    Window_Material_Glazing_Name_5: str
    Optical_Data_Temperature_6: str
    Window_Material_Glazing_Name_6: str
    Optical_Data_Temperature_7: str
    Window_Material_Glazing_Name_7: str
    Optical_Data_Temperature_8: str
    Window_Material_Glazing_Name_8: str
    Optical_Data_Temperature_9: str
    Window_Material_Glazing_Name_9: str
    Optical_Data_Temperature_10: str
    Window_Material_Glazing_Name_10: str
    Optical_Data_Temperature_11: str
    Window_Material_Glazing_Name_11: str
    Optical_Data_Temperature_12: str
    Window_Material_Glazing_Name_12: str
    Optical_Data_Temperature_13: str
    Window_Material_Glazing_Name_13: str
    Optical_Data_Temperature_14: str
    Window_Material_Glazing_Name_14: str
    Optical_Data_Temperature_15: str
    Window_Material_Glazing_Name_15: str
    Optical_Data_Temperature_16: str
    Window_Material_Glazing_Name_16: str
    Optical_Data_Temperature_17: str
    Window_Material_Glazing_Name_17: str
    Optical_Data_Temperature_18: str
    Window_Material_Glazing_Name_18: str
    Optical_Data_Temperature_19: str
    Window_Material_Glazing_Name_19: str
    Optical_Data_Temperature_20: str
    Window_Material_Glazing_Name_20: str
    Optical_Data_Temperature_21: str
    Window_Material_Glazing_Name_21: str
    Optical_Data_Temperature_22: str
    Window_Material_Glazing_Name_22: str
    Optical_Data_Temperature_23: str
    Window_Material_Glazing_Name_23: str
    Optical_Data_Temperature_24: str
    Window_Material_Glazing_Name_24: str
    Optical_Data_Temperature_25: str
    Window_Material_Glazing_Name_25: str
    Optical_Data_Temperature_26: str
    Window_Material_Glazing_Name_26: str
    Optical_Data_Temperature_27: str
    Window_Material_Glazing_Name_27: str
    Optical_Data_Temperature_28: str
    Window_Material_Glazing_Name_28: str
    Optical_Data_Temperature_29: str
    Window_Material_Glazing_Name_29: str
    Optical_Data_Temperature_30: str
    Window_Material_Glazing_Name_30: str
    Optical_Data_Temperature_31: str
    Window_Material_Glazing_Name_31: str
    Optical_Data_Temperature_32: str
    Window_Material_Glazing_Name_32: str
    Optical_Data_Temperature_33: str
    Window_Material_Glazing_Name_33: str
    Optical_Data_Temperature_34: str
    Window_Material_Glazing_Name_34: str
    Optical_Data_Temperature_35: str
    Window_Material_Glazing_Name_35: str
    Optical_Data_Temperature_36: str
    Window_Material_Glazing_Name_36: str
    Optical_Data_Temperature_37: str
    Window_Material_Glazing_Name_37: str
    Optical_Data_Temperature_38: str
    Window_Material_Glazing_Name_38: str
    Optical_Data_Temperature_39: str
    Window_Material_Glazing_Name_39: str
    Optical_Data_Temperature_40: str
    Window_Material_Glazing_Name_40: str
    Optical_Data_Temperature_41: str
    Window_Material_Glazing_Name_41: str
    Optical_Data_Temperature_42: str
    Window_Material_Glazing_Name_42: str
    Optical_Data_Temperature_43: str
    Window_Material_Glazing_Name_43: str
    Optical_Data_Temperature_44: str
    Window_Material_Glazing_Name_44: str
    Optical_Data_Temperature_45: str
    Window_Material_Glazing_Name_45: str

class WindowmaterialScreenType(TypedDict, total=False):
    """"dict for WindowmaterialScreen"""
    Name: str
    Reflected_Beam_Transmittance_Accounting_Method: str
    Diffuse_Solar_Reflectance: str
    Diffuse_Visible_Reflectance: str
    Thermal_Hemispherical_Emissivity: str
    Conductivity: str
    Screen_Material_Spacing: str
    Screen_Material_Diameter: str
    Screen_to_Glass_Distance: str
    Top_Opening_Multiplier: str
    Bottom_Opening_Multiplier: str
    Left_Side_Opening_Multiplier: str
    Right_Side_Opening_Multiplier: str
    Angle_of_Resolution_for_Screen_Transmittance_Output_Map: str

class WindowmaterialScreenEquivalentlayerType(TypedDict, total=False):
    """"dict for WindowmaterialScreenEquivalentlayer"""
    Name: str
    Screen_BeamBeam_Solar_Transmittance: str
    Screen_BeamDiffuse_Solar_Transmittance: str
    Screen_BeamDiffuse_Solar_Reflectance: str
    Screen_BeamBeam_Visible_Transmittance: str
    Screen_BeamDiffuse_Visible_Transmittance: str
    Screen_BeamDiffuse_Visible_Reflectance: str
    Screen_Infrared_Transmittance: str
    Screen_Infrared_Emissivity: str
    Screen_Wire_Spacing: str
    Screen_Wire_Diameter: str

class WindowmaterialShadeType(TypedDict, total=False):
    """"dict for WindowmaterialShade"""
    Name: str
    Solar_Transmittance: str
    Solar_Reflectance: str
    Visible_Transmittance: str
    Visible_Reflectance: str
    Infrared_Hemispherical_Emissivity: str
    Infrared_Transmittance: str
    Thickness: str
    Conductivity: str
    Shade_to_Glass_Distance: str
    Top_Opening_Multiplier: str
    Bottom_Opening_Multiplier: str
    LeftSide_Opening_Multiplier: str
    RightSide_Opening_Multiplier: str
    Airflow_Permeability: str

class WindowmaterialShadeEquivalentlayerType(TypedDict, total=False):
    """"dict for WindowmaterialShadeEquivalentlayer"""
    Name: str
    Shade_BeamBeam_Solar_Transmittance: str
    Front_Side_Shade_BeamDiffuse_Solar_Transmittance: str
    Back_Side_Shade_BeamDiffuse_Solar_Transmittance: str
    Front_Side_Shade_BeamDiffuse_Solar_Reflectance: str
    Back_Side_Shade_BeamDiffuse_Solar_Reflectance: str
    Shade_BeamBeam_Visible_Transmittance_at_Normal_Incidence: str
    Shade_BeamDiffuse_Visible_Transmittance_at_Normal_Incidence: str
    Shade_BeamDiffuse_Visible_Reflectance_at_Normal_Incidence: str
    Shade_Material_Infrared_Transmittance: str
    Front_Side_Shade_Material_Infrared_Emissivity: str
    Back_Side_Shade_Material_Infrared_Emissivity: str

class WindowmaterialSimpleglazingsystemType(TypedDict, total=False):
    """"dict for WindowmaterialSimpleglazingsystem"""
    Name: str
    UFactor: str
    Solar_Heat_Gain_Coefficient: str
    Visible_Transmittance: str

class WindowpropertyAirflowcontrolType(TypedDict, total=False):
    """"dict for WindowpropertyAirflowcontrol"""
    Name: str
    Airflow_Source: str
    Airflow_Destination: str
    Maximum_Flow_Rate: str
    Airflow_Control_Type: str
    Airflow_Is_Scheduled: str
    Airflow_Multiplier_Schedule_Name: str
    Airflow_Return_Air_Node_Name: str

class WindowpropertyFrameanddividerType(TypedDict, total=False):
    """"dict for WindowpropertyFrameanddivider"""
    Name: str
    Frame_Width: str
    Frame_Outside_Projection: str
    Frame_Inside_Projection: str
    Frame_Conductance: str
    Ratio_of_FrameEdge_Glass_Conductance_to_CenterOfGlass_Conductance: str
    Frame_Solar_Absorptance: str
    Frame_Visible_Absorptance: str
    Frame_Thermal_Hemispherical_Emissivity: str
    Divider_Type: str
    Divider_Width: str
    Number_of_Horizontal_Dividers: str
    Number_of_Vertical_Dividers: str
    Divider_Outside_Projection: str
    Divider_Inside_Projection: str
    Divider_Conductance: str
    Ratio_of_DividerEdge_Glass_Conductance_to_CenterOfGlass_Conductance: str
    Divider_Solar_Absorptance: str
    Divider_Visible_Absorptance: str
    Divider_Thermal_Hemispherical_Emissivity: str
    Outside_Reveal_Solar_Absorptance: str
    Inside_Sill_Depth: str
    Inside_Sill_Solar_Absorptance: str
    Inside_Reveal_Depth: str
    Inside_Reveal_Solar_Absorptance: str
    NFRC_Product_Type_for_Assembly_Calculations: str

class WindowpropertyStormwindowType(TypedDict, total=False):
    """"dict for WindowpropertyStormwindow"""
    Window_Name: str
    Storm_Glass_Layer_Name: str
    Distance_Between_Storm_Glass_Layer_and_Adjacent_Glass: str
    Month_that_Storm_Glass_Layer_is_Put_On: str
    Day_of_Month_that_Storm_Glass_Layer_is_Put_On: str
    Month_that_Storm_Glass_Layer_is_Taken_Off: str
    Day_of_Month_that_Storm_Glass_Layer_is_Taken_Off: str

class WindowscalculationengineType(TypedDict, total=False):
    """"dict for Windowscalculationengine"""
    Windows_engine: str

class WindowshadingcontrolType(TypedDict, total=False):
    """"dict for Windowshadingcontrol"""
    Name: str
    Zone_Name: str
    Shading_Control_Sequence_Number: str
    Shading_Type: str
    Construction_with_Shading_Name: str
    Shading_Control_Type: str
    Schedule_Name: str
    Setpoint: str
    Shading_Control_Is_Scheduled: str
    Glare_Control_Is_Active: str
    Shading_Device_Material_Name: str
    Type_of_Slat_Angle_Control_for_Blinds: str
    Slat_Angle_Schedule_Name: str
    Setpoint_2: str
    Daylighting_Control_Object_Name: str
    Multiple_Surface_Control_Type: str
    Fenestration_Surface_1_Name: str
    Fenestration_Surface_2_Name: str
    Fenestration_Surface_3_Name: str
    Fenestration_Surface_4_Name: str
    Fenestration_Surface_5_Name: str
    Fenestration_Surface_6_Name: str
    Fenestration_Surface_7_Name: str
    Fenestration_Surface_8_Name: str
    Fenestration_Surface_9_Name: str
    Fenestration_Surface_10_Name: str

class WindowthermalmodelParamsType(TypedDict, total=False):
    """"dict for WindowthermalmodelParams"""
    Name: str
    standard: str
    Thermal_Model: str
    SDScalar: str
    Deflection_Model: str
    Vacuum_Pressure_Limit: str
    Initial_temperature: str
    Initial_pressure: str

class ZoneType(TypedDict, total=False):
    """"dict for Zone"""
    Name: str
    Direction_of_Relative_North: str
    X_Origin: str
    Y_Origin: str
    Z_Origin: str
    Type: str
    Multiplier: str
    Ceiling_Height: str
    Volume: str
    Floor_Area: str
    Zone_Inside_Convection_Algorithm: str
    Zone_Outside_Convection_Algorithm: str
    Part_of_Total_Floor_Area: str

class ZoneairbalanceOutdoorairType(TypedDict, total=False):
    """"dict for ZoneairbalanceOutdoorair"""
    Name: str
    Zone_Name: str
    Air_Balance_Method: str
    Induced_Outdoor_Air_Due_to_Unbalanced_Duct_Leakage: str
    Induced_Outdoor_Air_Schedule_Name: str

class ZoneaircontaminantbalanceType(TypedDict, total=False):
    """"dict for Zoneaircontaminantbalance"""
    Carbon_Dioxide_Concentration: str
    Outdoor_Carbon_Dioxide_Schedule_Name: str
    Generic_Contaminant_Concentration: str
    Outdoor_Generic_Contaminant_Schedule_Name: str

class ZoneairheatbalancealgorithmType(TypedDict, total=False):
    """"dict for Zoneairheatbalancealgorithm"""
    Algorithm: str
    Do_Space_Heat_Balance_for_Sizing: str
    Do_Space_Heat_Balance_for_Simulation: str

class ZoneairmassflowconservationType(TypedDict, total=False):
    """"dict for Zoneairmassflowconservation"""
    Adjust_Zone_Mixing_and_Return_For_Air_Mass_Flow_Balance: str
    Infiltration_Balancing_Method: str
    Infiltration_Balancing_Zones: str

class ZonebaseboardOutdoortemperaturecontrolledType(TypedDict, total=False):
    """"dict for ZonebaseboardOutdoortemperaturecontrolled"""
    Name: str
    Zone_or_ZoneList_or_Space_or_SpaceList_Name: str
    Schedule_Name: str
    Capacity_at_Low_Temperature: str
    Low_Temperature: str
    Capacity_at_High_Temperature: str
    High_Temperature: str
    Fraction_Radiant: str
    EndUse_Subcategory: str

class ZonecapacitancemultiplierResearchspecialType(TypedDict, total=False):
    """"dict for ZonecapacitancemultiplierResearchspecial"""
    Name: str
    Zone_or_ZoneList_Name: str
    Temperature_Capacity_Multiplier: str
    Humidity_Capacity_Multiplier: str
    Carbon_Dioxide_Capacity_Multiplier: str
    Generic_Contaminant_Capacity_Multiplier: str

class ZonecontaminantsourceandsinkCarbondioxideType(TypedDict, total=False):
    """"dict for ZonecontaminantsourceandsinkCarbondioxide"""
    Name: str
    Zone_Name: str
    Design_Generation_Rate: str
    Schedule_Name: str

class ZonecontaminantsourceandsinkGenericConstantType(TypedDict, total=False):
    """"dict for ZonecontaminantsourceandsinkGenericConstant"""
    Name: str
    Zone_Name: str
    Design_Generation_Rate: str
    Generation_Schedule_Name: str
    Design_Removal_Coefficient: str
    Removal_Schedule_Name: str

class ZonecontaminantsourceandsinkGenericCutoffmodelType(TypedDict, total=False):
    """"dict for ZonecontaminantsourceandsinkGenericCutoffmodel"""
    Name: str
    Zone_Name: str
    Design_Generation_Rate_Coefficient: str
    Schedule_Name: str
    Cutoff_Generic_Contaminant_at_which_Emission_Ceases: str

class ZonecontaminantsourceandsinkGenericDecaysourceType(TypedDict, total=False):
    """"dict for ZonecontaminantsourceandsinkGenericDecaysource"""
    Name: str
    Zone_Name: str
    Initial_Emission_Rate: str
    Schedule_Name: str
    Delay_Time_Constant: str

class ZonecontaminantsourceandsinkGenericDepositionratesinkType(TypedDict, total=False):
    """"dict for ZonecontaminantsourceandsinkGenericDepositionratesink"""
    Name: str
    Zone_Name: str
    Deposition_Rate: str
    Schedule_Name: str

class ZonecontrolContaminantcontrollerType(TypedDict, total=False):
    """"dict for ZonecontrolContaminantcontroller"""
    Name: str
    Zone_Name: str
    Carbon_Dioxide_Control_Availability_Schedule_Name: str
    Carbon_Dioxide_Setpoint_Schedule_Name: str
    Minimum_Carbon_Dioxide_Concentration_Schedule_Name: str
    Maximum_Carbon_Dioxide_Concentration_Schedule_Name: str
    Generic_Contaminant_Control_Availability_Schedule_Name: str
    Generic_Contaminant_Setpoint_Schedule_Name: str

class ZonecontrolHumidistatType(TypedDict, total=False):
    """"dict for ZonecontrolHumidistat"""
    Name: str
    Zone_Name: str
    Humidifying_Relative_Humidity_Setpoint_Schedule_Name: str
    Dehumidifying_Relative_Humidity_Setpoint_Schedule_Name: str

class ZonecontrolThermostatType(TypedDict, total=False):
    """"dict for ZonecontrolThermostat"""
    Name: str
    Zone_or_ZoneList_Name: str
    Control_Type_Schedule_Name: str
    Control_1_Object_Type: str
    Control_1_Name: str
    Control_2_Object_Type: str
    Control_2_Name: str
    Control_3_Object_Type: str
    Control_3_Name: str
    Control_4_Object_Type: str
    Control_4_Name: str
    Temperature_Difference_Between_Cutout_And_Setpoint: str

class ZonecontrolThermostatOperativetemperatureType(TypedDict, total=False):
    """"dict for ZonecontrolThermostatOperativetemperature"""
    Thermostat_Name: str
    Radiative_Fraction_Input_Mode: str
    Fixed_Radiative_Fraction: str
    Radiative_Fraction_Schedule_Name: str
    Adaptive_Comfort_Model_Type: str

class ZonecontrolThermostatStageddualsetpointType(TypedDict, total=False):
    """"dict for ZonecontrolThermostatStageddualsetpoint"""
    Name: str
    Zone_or_ZoneList_Name: str
    Number_of_Heating_Stages: str
    Heating_Temperature_Setpoint_Schedule_Name: str
    Heating_Throttling_Temperature_Range: str
    Stage_1_Heating_Temperature_Offset: str
    Stage_2_Heating_Temperature_Offset: str
    Stage_3_Heating_Temperature_Offset: str
    Stage_4_Heating_Temperature_Offset: str
    Number_of_Cooling_Stages: str
    Cooling_Temperature_Setpoint_Base_Schedule_Name: str
    Cooling_Throttling_Temperature_Range: str
    Stage_1_Cooling_Temperature_Offset: str
    Stage_2_Cooling_Temperature_Offset: str
    Stage_3_Cooling_Temperature_Offset: str
    Stage_4_Cooling_Temperature_Offset: str

class ZonecontrolThermostatTemperatureandhumidityType(TypedDict, total=False):
    """"dict for ZonecontrolThermostatTemperatureandhumidity"""
    Thermostat_Name: str
    Dehumidifying_Relative_Humidity_Setpoint_Schedule_Name: str
    Dehumidification_Control_Type: str
    Overcool_Range_Input_Method: str
    Overcool_Constant_Range: str
    Overcool_Range_Schedule_Name: str
    Overcool_Control_Ratio: str

class ZonecontrolThermostatThermalcomfortType(TypedDict, total=False):
    """"dict for ZonecontrolThermostatThermalcomfort"""
    Name: str
    Zone_or_ZoneList_Name: str
    Averaging_Method: str
    Specific_People_Name: str
    Minimum_DryBulb_Temperature_Setpoint: str
    Maximum_DryBulb_Temperature_Setpoint: str
    Thermal_Comfort_Control_Type_Schedule_Name: str
    Thermal_Comfort_Control_1_Object_Type: str
    Thermal_Comfort_Control_1_Name: str
    Thermal_Comfort_Control_2_Object_Type: str
    Thermal_Comfort_Control_2_Name: str
    Thermal_Comfort_Control_3_Object_Type: str
    Thermal_Comfort_Control_3_Name: str
    Thermal_Comfort_Control_4_Object_Type: str
    Thermal_Comfort_Control_4_Name: str

class ZonecooltowerShowerType(TypedDict, total=False):
    """"dict for ZonecooltowerShower"""
    Name: str
    Availability_Schedule_Name: str
    Zone_Name: str
    Water_Supply_Storage_Tank_Name: str
    Flow_Control_Type: str
    Pump_Flow_Rate_Schedule_Name: str
    Maximum_Water_Flow_Rate: str
    Effective_Tower_Height: str
    Airflow_Outlet_Area: str
    Maximum_Air_Flow_Rate: str
    Minimum_Indoor_Temperature: str
    Fraction_of_Water_Loss: str
    Fraction_of_Flow_Schedule: str
    Rated_Power_Consumption: str

class ZonecrossmixingType(TypedDict, total=False):
    """"dict for Zonecrossmixing"""
    Name: str
    Zone_or_Space_Name: str
    Schedule_Name: str
    Design_Flow_Rate_Calculation_Method: str
    Design_Flow_Rate: str
    Flow_Rate_per_Floor_Area: str
    Flow_Rate_per_Person: str
    Air_Changes_per_Hour: str
    Source_Zone_or_Space_Name: str
    Delta_Temperature: str
    Delta_Temperature_Schedule_Name: str
    Minimum_Receiving_Temperature_Schedule_Name: str
    Maximum_Receiving_Temperature_Schedule_Name: str
    Minimum_Source_Temperature_Schedule_Name: str
    Maximum_Source_Temperature_Schedule_Name: str
    Minimum_Outdoor_Temperature_Schedule_Name: str
    Maximum_Outdoor_Temperature_Schedule_Name: str

class ZoneearthtubeType(TypedDict, total=False):
    """"dict for Zoneearthtube"""
    Zone_Name: str
    Schedule_Name: str
    Design_Flow_Rate: str
    Minimum_Zone_Temperature_when_Cooling: str
    Maximum_Zone_Temperature_when_Heating: str
    Delta_Temperature: str
    Earthtube_Type: str
    Fan_Pressure_Rise: str
    Fan_Total_Efficiency: str
    Pipe_Radius: str
    Pipe_Thickness: str
    Pipe_Length: str
    Pipe_Thermal_Conductivity: str
    Pipe_Depth_Under_Ground_Surface: str
    Soil_Condition: str
    Average_Soil_Surface_Temperature: str
    Amplitude_of_Soil_Surface_Temperature: str
    Phase_Constant_of_Soil_Surface_Temperature: str
    Constant_Term_Flow_Coefficient: str
    Temperature_Term_Flow_Coefficient: str
    Velocity_Term_Flow_Coefficient: str
    Velocity_Squared_Term_Flow_Coefficient: str
    Earth_Tube_Model_Type: str
    Earth_Tube_Model_Parameters: str

class ZoneearthtubeParametersType(TypedDict, total=False):
    """"dict for ZoneearthtubeParameters"""
    Earth_Tube_Model_Parameters_Name: str
    Nodes_Above_Earth_Tube: str
    Nodes_Below_Earth_Tube: str
    Earth_Tube_Dimensionless_Boundary_Above: str
    Earth_Tube_Dimensionless_Boundary_Below: str
    Earth_Tube_Solution_Space_Width: str

class ZonegroupType(TypedDict, total=False):
    """"dict for Zonegroup"""
    Name: str
    Zone_List_Name: str
    Zone_List_Multiplier: str

class ZonehvacAirdistributionunitType(TypedDict, total=False):
    """"dict for ZonehvacAirdistributionunit"""
    Name: str
    Air_Distribution_Unit_Outlet_Node_Name: str
    Air_Terminal_Object_Type: str
    Air_Terminal_Name: str
    Nominal_Upstream_Leakage_Fraction: str
    Constant_Downstream_Leakage_Fraction: str
    Design_Specification_Air_Terminal_Sizing_Object_Name: str

class ZonehvacBaseboardConvectiveElectricType(TypedDict, total=False):
    """"dict for ZonehvacBaseboardConvectiveElectric"""
    Name: str
    Availability_Schedule_Name: str
    Heating_Design_Capacity_Method: str
    Heating_Design_Capacity: str
    Heating_Design_Capacity_Per_Floor_Area: str
    Fraction_of_Autosized_Heating_Design_Capacity: str
    Efficiency: str

class ZonehvacBaseboardConvectiveWaterType(TypedDict, total=False):
    """"dict for ZonehvacBaseboardConvectiveWater"""
    Name: str
    Availability_Schedule_Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str
    Heating_Design_Capacity_Method: str
    Heating_Design_Capacity: str
    Heating_Design_Capacity_Per_Floor_Area: str
    Fraction_of_Autosized_Heating_Design_Capacity: str
    UFactor_Times_Area_Value: str
    Maximum_Water_Flow_Rate: str
    Convergence_Tolerance: str

class ZonehvacBaseboardRadiantconvectiveElectricType(TypedDict, total=False):
    """"dict for ZonehvacBaseboardRadiantconvectiveElectric"""
    Name: str
    Availability_Schedule_Name: str
    Heating_Design_Capacity_Method: str
    Heating_Design_Capacity: str
    Heating_Design_Capacity_Per_Floor_Area: str
    Fraction_of_Autosized_Heating_Design_Capacity: str
    Efficiency: str
    Fraction_Radiant: str
    Fraction_of_Radiant_Energy_Incident_on_People: str
    Surface_1_Name: str
    Fraction_of_Radiant_Energy_to_Surface_1: str
    Surface_2_Name: str
    Fraction_of_Radiant_Energy_to_Surface_2: str
    Surface_3_Name: str
    Fraction_of_Radiant_Energy_to_Surface_3: str
    Surface_4_Name: str
    Fraction_of_Radiant_Energy_to_Surface_4: str
    Surface_5_Name: str
    Fraction_of_Radiant_Energy_to_Surface_5: str
    Surface_6_Name: str
    Fraction_of_Radiant_Energy_to_Surface_6: str
    Surface_7_Name: str
    Fraction_of_Radiant_Energy_to_Surface_7: str
    Surface_8_Name: str
    Fraction_of_Radiant_Energy_to_Surface_8: str
    Surface_9_Name: str
    Fraction_of_Radiant_Energy_to_Surface_9: str
    Surface_10_Name: str
    Fraction_of_Radiant_Energy_to_Surface_10: str
    Surface_11_Name: str
    Fraction_of_Radiant_Energy_to_Surface_11: str
    Surface_12_Name: str
    Fraction_of_Radiant_Energy_to_Surface_12: str
    Surface_13_Name: str
    Fraction_of_Radiant_Energy_to_Surface_13: str
    Surface_14_Name: str
    Fraction_of_Radiant_Energy_to_Surface_14: str
    Surface_15_Name: str
    Fraction_of_Radiant_Energy_to_Surface_15: str
    Surface_16_Name: str
    Fraction_of_Radiant_Energy_to_Surface_16: str
    Surface_17_Name: str
    Fraction_of_Radiant_Energy_to_Surface_17: str
    Surface_18_Name: str
    Fraction_of_Radiant_Energy_to_Surface_18: str
    Surface_19_Name: str
    Fraction_of_Radiant_Energy_to_Surface_19: str
    Surface_20_Name: str
    Fraction_of_Radiant_Energy_to_Surface_20: str
    Surface_21_Name: str
    Fraction_of_Radiant_Energy_to_Surface_21: str
    Surface_22_Name: str
    Fraction_of_Radiant_Energy_to_Surface_22: str
    Surface_23_Name: str
    Fraction_of_Radiant_Energy_to_Surface_23: str
    Surface_24_Name: str
    Fraction_of_Radiant_Energy_to_Surface_24: str
    Surface_25_Name: str
    Fraction_of_Radiant_Energy_to_Surface_25: str
    Surface_26_Name: str
    Fraction_of_Radiant_Energy_to_Surface_26: str
    Surface_27_Name: str
    Fraction_of_Radiant_Energy_to_Surface_27: str
    Surface_28_Name: str
    Fraction_of_Radiant_Energy_to_Surface_28: str
    Surface_29_Name: str
    Fraction_of_Radiant_Energy_to_Surface_29: str
    Surface_30_Name: str
    Fraction_of_Radiant_Energy_to_Surface_30: str
    Surface_31_Name: str
    Fraction_of_Radiant_Energy_to_Surface_31: str
    Surface_32_Name: str
    Fraction_of_Radiant_Energy_to_Surface_32: str
    Surface_33_Name: str
    Fraction_of_Radiant_Energy_to_Surface_33: str
    Surface_34_Name: str
    Fraction_of_Radiant_Energy_to_Surface_34: str
    Surface_35_Name: str
    Fraction_of_Radiant_Energy_to_Surface_35: str
    Surface_36_Name: str
    Fraction_of_Radiant_Energy_to_Surface_36: str
    Surface_37_Name: str
    Fraction_of_Radiant_Energy_to_Surface_37: str
    Surface_38_Name: str
    Fraction_of_Radiant_Energy_to_Surface_38: str
    Surface_39_Name: str
    Fraction_of_Radiant_Energy_to_Surface_39: str
    Surface_40_Name: str
    Fraction_of_Radiant_Energy_to_Surface_40: str
    Surface_41_Name: str
    Fraction_of_Radiant_Energy_to_Surface_41: str
    Surface_42_Name: str
    Fraction_of_Radiant_Energy_to_Surface_42: str
    Surface_43_Name: str
    Fraction_of_Radiant_Energy_to_Surface_43: str
    Surface_44_Name: str
    Fraction_of_Radiant_Energy_to_Surface_44: str
    Surface_45_Name: str
    Fraction_of_Radiant_Energy_to_Surface_45: str
    Surface_46_Name: str
    Fraction_of_Radiant_Energy_to_Surface_46: str
    Surface_47_Name: str
    Fraction_of_Radiant_Energy_to_Surface_47: str
    Surface_48_Name: str
    Fraction_of_Radiant_Energy_to_Surface_48: str
    Surface_49_Name: str
    Fraction_of_Radiant_Energy_to_Surface_49: str

class ZonehvacBaseboardRadiantconvectiveSteamType(TypedDict, total=False):
    """"dict for ZonehvacBaseboardRadiantconvectiveSteam"""
    Name: str
    Design_Object: str
    Availability_Schedule_Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str
    Heating_Design_Capacity: str
    Degree_of_SubCooling: str
    Maximum_Steam_Flow_Rate: str
    Surface_1_Name: str
    Fraction_of_Radiant_Energy_to_Surface_1: str
    Surface_2_Name: str
    Fraction_of_Radiant_Energy_to_Surface_2: str
    Surface_3_Name: str
    Fraction_of_Radiant_Energy_to_Surface_3: str
    Surface_4_Name: str
    Fraction_of_Radiant_Energy_to_Surface_4: str
    Surface_5_Name: str
    Fraction_of_Radiant_Energy_to_Surface_5: str
    Surface_6_Name: str
    Fraction_of_Radiant_Energy_to_Surface_6: str
    Surface_7_Name: str
    Fraction_of_Radiant_Energy_to_Surface_7: str
    Surface_8_Name: str
    Fraction_of_Radiant_Energy_to_Surface_8: str
    Surface_9_Name: str
    Fraction_of_Radiant_Energy_to_Surface_9: str
    Surface_10_Name: str
    Fraction_of_Radiant_Energy_to_Surface_10: str
    Surface_11_Name: str
    Fraction_of_Radiant_Energy_to_Surface_11: str
    Surface_12_Name: str
    Fraction_of_Radiant_Energy_to_Surface_12: str
    Surface_13_Name: str
    Fraction_of_Radiant_Energy_to_Surface_13: str
    Surface_14_Name: str
    Fraction_of_Radiant_Energy_to_Surface_14: str
    Surface_15_Name: str
    Fraction_of_Radiant_Energy_to_Surface_15: str
    Surface_16_Name: str
    Fraction_of_Radiant_Energy_to_Surface_16: str
    Surface_17_Name: str
    Fraction_of_Radiant_Energy_to_Surface_17: str
    Surface_18_Name: str
    Fraction_of_Radiant_Energy_to_Surface_18: str
    Surface_19_Name: str
    Fraction_of_Radiant_Energy_to_Surface_19: str
    Surface_20_Name: str
    Fraction_of_Radiant_Energy_to_Surface_20: str
    Surface_21_Name: str
    Fraction_of_Radiant_Energy_to_Surface_21: str
    Surface_22_Name: str
    Fraction_of_Radiant_Energy_to_Surface_22: str
    Surface_23_Name: str
    Fraction_of_Radiant_Energy_to_Surface_23: str
    Surface_24_Name: str
    Fraction_of_Radiant_Energy_to_Surface_24: str
    Surface_25_Name: str
    Fraction_of_Radiant_Energy_to_Surface_25: str
    Surface_26_Name: str
    Fraction_of_Radiant_Energy_to_Surface_26: str
    Surface_27_Name: str
    Fraction_of_Radiant_Energy_to_Surface_27: str
    Surface_28_Name: str
    Fraction_of_Radiant_Energy_to_Surface_28: str
    Surface_29_Name: str
    Fraction_of_Radiant_Energy_to_Surface_29: str
    Surface_30_Name: str
    Fraction_of_Radiant_Energy_to_Surface_30: str
    Surface_31_Name: str
    Fraction_of_Radiant_Energy_to_Surface_31: str
    Surface_32_Name: str
    Fraction_of_Radiant_Energy_to_Surface_32: str
    Surface_33_Name: str
    Fraction_of_Radiant_Energy_to_Surface_33: str
    Surface_34_Name: str
    Fraction_of_Radiant_Energy_to_Surface_34: str
    Surface_35_Name: str
    Fraction_of_Radiant_Energy_to_Surface_35: str
    Surface_36_Name: str
    Fraction_of_Radiant_Energy_to_Surface_36: str
    Surface_37_Name: str
    Fraction_of_Radiant_Energy_to_Surface_37: str
    Surface_38_Name: str
    Fraction_of_Radiant_Energy_to_Surface_38: str
    Surface_39_Name: str
    Fraction_of_Radiant_Energy_to_Surface_39: str
    Surface_40_Name: str
    Fraction_of_Radiant_Energy_to_Surface_40: str
    Surface_41_Name: str
    Fraction_of_Radiant_Energy_to_Surface_41: str
    Surface_42_Name: str
    Fraction_of_Radiant_Energy_to_Surface_42: str
    Surface_43_Name: str
    Fraction_of_Radiant_Energy_to_Surface_43: str
    Surface_44_Name: str
    Fraction_of_Radiant_Energy_to_Surface_44: str
    Surface_45_Name: str
    Fraction_of_Radiant_Energy_to_Surface_45: str
    Surface_46_Name: str
    Fraction_of_Radiant_Energy_to_Surface_46: str
    Surface_47_Name: str
    Fraction_of_Radiant_Energy_to_Surface_47: str
    Surface_48_Name: str
    Fraction_of_Radiant_Energy_to_Surface_48: str
    Surface_49_Name: str
    Fraction_of_Radiant_Energy_to_Surface_49: str

class ZonehvacBaseboardRadiantconvectiveSteamDesignType(TypedDict, total=False):
    """"dict for ZonehvacBaseboardRadiantconvectiveSteamDesign"""
    Name: str
    Heating_Design_Capacity_Method: str
    Heating_Design_Capacity_Per_Floor_Area: str
    Fraction_of_Autosized_Heating_Design_Capacity: str
    Convergence_Tolerance: str
    Fraction_Radiant: str
    Fraction_of_Radiant_Energy_Incident_on_People: str

class ZonehvacBaseboardRadiantconvectiveWaterType(TypedDict, total=False):
    """"dict for ZonehvacBaseboardRadiantconvectiveWater"""
    Name: str
    Design_Object: str
    Availability_Schedule_Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str
    Rated_Average_Water_Temperature: str
    Rated_Water_Mass_Flow_Rate: str
    Heating_Design_Capacity: str
    Maximum_Water_Flow_Rate: str
    Surface_1_Name: str
    Fraction_of_Radiant_Energy_to_Surface_1: str
    Surface_2_Name: str
    Fraction_of_Radiant_Energy_to_Surface_2: str
    Surface_3_Name: str
    Fraction_of_Radiant_Energy_to_Surface_3: str
    Surface_4_Name: str
    Fraction_of_Radiant_Energy_to_Surface_4: str
    Surface_5_Name: str
    Fraction_of_Radiant_Energy_to_Surface_5: str
    Surface_6_Name: str
    Fraction_of_Radiant_Energy_to_Surface_6: str
    Surface_7_Name: str
    Fraction_of_Radiant_Energy_to_Surface_7: str
    Surface_8_Name: str
    Fraction_of_Radiant_Energy_to_Surface_8: str
    Surface_9_Name: str
    Fraction_of_Radiant_Energy_to_Surface_9: str
    Surface_10_Name: str
    Fraction_of_Radiant_Energy_to_Surface_10: str
    Surface_11_Name: str
    Fraction_of_Radiant_Energy_to_Surface_11: str
    Surface_12_Name: str
    Fraction_of_Radiant_Energy_to_Surface_12: str
    Surface_13_Name: str
    Fraction_of_Radiant_Energy_to_Surface_13: str
    Surface_14_Name: str
    Fraction_of_Radiant_Energy_to_Surface_14: str
    Surface_15_Name: str
    Fraction_of_Radiant_Energy_to_Surface_15: str
    Surface_16_Name: str
    Fraction_of_Radiant_Energy_to_Surface_16: str
    Surface_17_Name: str
    Fraction_of_Radiant_Energy_to_Surface_17: str
    Surface_18_Name: str
    Fraction_of_Radiant_Energy_to_Surface_18: str
    Surface_19_Name: str
    Fraction_of_Radiant_Energy_to_Surface_19: str
    Surface_20_Name: str
    Fraction_of_Radiant_Energy_to_Surface_20: str
    Surface_21_Name: str
    Fraction_of_Radiant_Energy_to_Surface_21: str
    Surface_22_Name: str
    Fraction_of_Radiant_Energy_to_Surface_22: str
    Surface_23_Name: str
    Fraction_of_Radiant_Energy_to_Surface_23: str
    Surface_24_Name: str
    Fraction_of_Radiant_Energy_to_Surface_24: str
    Surface_25_Name: str
    Fraction_of_Radiant_Energy_to_Surface_25: str
    Surface_26_Name: str
    Fraction_of_Radiant_Energy_to_Surface_26: str
    Surface_27_Name: str
    Fraction_of_Radiant_Energy_to_Surface_27: str
    Surface_28_Name: str
    Fraction_of_Radiant_Energy_to_Surface_28: str
    Surface_29_Name: str
    Fraction_of_Radiant_Energy_to_Surface_29: str
    Surface_30_Name: str
    Fraction_of_Radiant_Energy_to_Surface_30: str
    Surface_31_Name: str
    Fraction_of_Radiant_Energy_to_Surface_31: str
    Surface_32_Name: str
    Fraction_of_Radiant_Energy_to_Surface_32: str
    Surface_33_Name: str
    Fraction_of_Radiant_Energy_to_Surface_33: str
    Surface_34_Name: str
    Fraction_of_Radiant_Energy_to_Surface_34: str
    Surface_35_Name: str
    Fraction_of_Radiant_Energy_to_Surface_35: str
    Surface_36_Name: str
    Fraction_of_Radiant_Energy_to_Surface_36: str
    Surface_37_Name: str
    Fraction_of_Radiant_Energy_to_Surface_37: str
    Surface_38_Name: str
    Fraction_of_Radiant_Energy_to_Surface_38: str
    Surface_39_Name: str
    Fraction_of_Radiant_Energy_to_Surface_39: str
    Surface_40_Name: str
    Fraction_of_Radiant_Energy_to_Surface_40: str
    Surface_41_Name: str
    Fraction_of_Radiant_Energy_to_Surface_41: str
    Surface_42_Name: str
    Fraction_of_Radiant_Energy_to_Surface_42: str
    Surface_43_Name: str
    Fraction_of_Radiant_Energy_to_Surface_43: str
    Surface_44_Name: str
    Fraction_of_Radiant_Energy_to_Surface_44: str
    Surface_45_Name: str
    Fraction_of_Radiant_Energy_to_Surface_45: str
    Surface_46_Name: str
    Fraction_of_Radiant_Energy_to_Surface_46: str
    Surface_47_Name: str
    Fraction_of_Radiant_Energy_to_Surface_47: str
    Surface_48_Name: str
    Fraction_of_Radiant_Energy_to_Surface_48: str
    Surface_49_Name: str
    Fraction_of_Radiant_Energy_to_Surface_49: str

class ZonehvacBaseboardRadiantconvectiveWaterDesignType(TypedDict, total=False):
    """"dict for ZonehvacBaseboardRadiantconvectiveWaterDesign"""
    Name: str
    Heating_Design_Capacity_Method: str
    Heating_Design_Capacity_Per_Floor_Area: str
    Fraction_of_Autosized_Heating_Design_Capacity: str
    Convergence_Tolerance: str
    Fraction_Radiant: str
    Fraction_of_Radiant_Energy_Incident_on_People: str

class ZonehvacCoolingpanelRadiantconvectiveWaterType(TypedDict, total=False):
    """"dict for ZonehvacCoolingpanelRadiantconvectiveWater"""
    Name: str
    Availability_Schedule_Name: str
    Water_Inlet_Node_Name: str
    Water_Outlet_Node_Name: str
    Rated_Inlet_Water_Temperature: str
    Rated_Inlet_Space_Temperature: str
    Rated_Water_Mass_Flow_Rate: str
    Cooling_Design_Capacity_Method: str
    Cooling_Design_Capacity: str
    Cooling_Design_Capacity_Per_Floor_Area: str
    Fraction_of_Autosized_Cooling_Design_Capacity: str
    Maximum_Chilled_Water_Flow_Rate: str
    Control_Type: str
    Cooling_Control_Throttling_Range: str
    Cooling_Control_Temperature_Schedule_Name: str
    Condensation_Control_Type: str
    Condensation_Control_Dewpoint_Offset: str
    Fraction_Radiant: str
    Fraction_of_Radiant_Energy_Incident_on_People: str
    Surface_1_Name: str
    Fraction_of_Radiant_Energy_to_Surface_1: str
    Surface_2_Name: str
    Fraction_of_Radiant_Energy_to_Surface_2: str
    Surface_3_Name: str
    Fraction_of_Radiant_Energy_to_Surface_3: str
    Surface_4_Name: str
    Fraction_of_Radiant_Energy_to_Surface_4: str
    Surface_5_Name: str
    Fraction_of_Radiant_Energy_to_Surface_5: str
    Surface_6_Name: str
    Fraction_of_Radiant_Energy_to_Surface_6: str
    Surface_7_Name: str
    Fraction_of_Radiant_Energy_to_Surface_7: str
    Surface_8_Name: str
    Fraction_of_Radiant_Energy_to_Surface_8: str
    Surface_9_Name: str
    Fraction_of_Radiant_Energy_to_Surface_9: str
    Surface_10_Name: str
    Fraction_of_Radiant_Energy_to_Surface_10: str
    Surface_11_Name: str
    Fraction_of_Radiant_Energy_to_Surface_11: str
    Surface_12_Name: str
    Fraction_of_Radiant_Energy_to_Surface_12: str
    Surface_13_Name: str
    Fraction_of_Radiant_Energy_to_Surface_13: str
    Surface_14_Name: str
    Fraction_of_Radiant_Energy_to_Surface_14: str
    Surface_15_Name: str
    Fraction_of_Radiant_Energy_to_Surface_15: str
    Surface_16_Name: str
    Fraction_of_Radiant_Energy_to_Surface_16: str
    Surface_17_Name: str
    Fraction_of_Radiant_Energy_to_Surface_17: str
    Surface_18_Name: str
    Fraction_of_Radiant_Energy_to_Surface_18: str
    Surface_19_Name: str
    Fraction_of_Radiant_Energy_to_Surface_19: str
    Surface_20_Name: str
    Fraction_of_Radiant_Energy_to_Surface_20: str
    Surface_21_Name: str
    Fraction_of_Radiant_Energy_to_Surface_21: str
    Surface_22_Name: str
    Fraction_of_Radiant_Energy_to_Surface_22: str
    Surface_23_Name: str
    Fraction_of_Radiant_Energy_to_Surface_23: str
    Surface_24_Name: str
    Fraction_of_Radiant_Energy_to_Surface_24: str
    Surface_25_Name: str
    Fraction_of_Radiant_Energy_to_Surface_25: str
    Surface_26_Name: str
    Fraction_of_Radiant_Energy_to_Surface_26: str
    Surface_27_Name: str
    Fraction_of_Radiant_Energy_to_Surface_27: str
    Surface_28_Name: str
    Fraction_of_Radiant_Energy_to_Surface_28: str
    Surface_29_Name: str
    Fraction_of_Radiant_Energy_to_Surface_29: str
    Surface_30_Name: str
    Fraction_of_Radiant_Energy_to_Surface_30: str
    Surface_31_Name: str
    Fraction_of_Radiant_Energy_to_Surface_31: str
    Surface_32_Name: str
    Fraction_of_Radiant_Energy_to_Surface_32: str
    Surface_33_Name: str
    Fraction_of_Radiant_Energy_to_Surface_33: str
    Surface_34_Name: str
    Fraction_of_Radiant_Energy_to_Surface_34: str
    Surface_35_Name: str
    Fraction_of_Radiant_Energy_to_Surface_35: str
    Surface_36_Name: str
    Fraction_of_Radiant_Energy_to_Surface_36: str
    Surface_37_Name: str
    Fraction_of_Radiant_Energy_to_Surface_37: str
    Surface_38_Name: str
    Fraction_of_Radiant_Energy_to_Surface_38: str
    Surface_39_Name: str
    Fraction_of_Radiant_Energy_to_Surface_39: str
    Surface_40_Name: str
    Fraction_of_Radiant_Energy_to_Surface_40: str
    Surface_41_Name: str
    Fraction_of_Radiant_Energy_to_Surface_41: str
    Surface_42_Name: str
    Fraction_of_Radiant_Energy_to_Surface_42: str
    Surface_43_Name: str
    Fraction_of_Radiant_Energy_to_Surface_43: str
    Surface_44_Name: str
    Fraction_of_Radiant_Energy_to_Surface_44: str
    Surface_45_Name: str
    Fraction_of_Radiant_Energy_to_Surface_45: str
    Surface_46_Name: str
    Fraction_of_Radiant_Energy_to_Surface_46: str
    Surface_47_Name: str
    Fraction_of_Radiant_Energy_to_Surface_47: str
    Surface_48_Name: str
    Fraction_of_Radiant_Energy_to_Surface_48: str
    Surface_49_Name: str
    Fraction_of_Radiant_Energy_to_Surface_49: str

class ZonehvacDehumidifierDxType(TypedDict, total=False):
    """"dict for ZonehvacDehumidifierDx"""
    Name: str
    Availability_Schedule_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Rated_Water_Removal: str
    Rated_Energy_Factor: str
    Rated_Air_Flow_Rate: str
    Water_Removal_Curve_Name: str
    Energy_Factor_Curve_Name: str
    Part_Load_Fraction_Correlation_Curve_Name: str
    Minimum_DryBulb_Temperature_for_Dehumidifier_Operation: str
    Maximum_DryBulb_Temperature_for_Dehumidifier_Operation: str
    OffCycle_Parasitic_Electric_Load: str
    Condensate_Collection_Water_Storage_Tank_Name: str

class ZonehvacEnergyrecoveryventilatorType(TypedDict, total=False):
    """"dict for ZonehvacEnergyrecoveryventilator"""
    Name: str
    Availability_Schedule_Name: str
    Heat_Exchanger_Name: str
    Supply_Air_Flow_Rate: str
    Exhaust_Air_Flow_Rate: str
    Supply_Air_Fan_Name: str
    Exhaust_Air_Fan_Name: str
    Controller_Name: str
    Ventilation_Rate_per_Unit_Floor_Area: str
    Ventilation_Rate_per_Occupant: str
    Availability_Manager_List_Name: str

class ZonehvacEnergyrecoveryventilatorControllerType(TypedDict, total=False):
    """"dict for ZonehvacEnergyrecoveryventilatorController"""
    Name: str
    Temperature_High_Limit: str
    Temperature_Low_Limit: str
    Enthalpy_High_Limit: str
    Dewpoint_Temperature_Limit: str
    Electronic_Enthalpy_Limit_Curve_Name: str
    Exhaust_Air_Temperature_Limit: str
    Exhaust_Air_Enthalpy_Limit: str
    Time_of_Day_Economizer_Flow_Control_Schedule_Name: str
    High_Humidity_Control_Flag: str
    Humidistat_Control_Zone_Name: str
    High_Humidity_Outdoor_Air_Flow_Ratio: str
    Control_High_Indoor_Humidity_Based_on_Outdoor_Humidity_Ratio: str

class ZonehvacEquipmentconnectionsType(TypedDict, total=False):
    """"dict for ZonehvacEquipmentconnections"""
    Zone_Name: str
    Zone_Conditioning_Equipment_List_Name: str
    Zone_Air_Inlet_Node_or_NodeList_Name: str
    Zone_Air_Exhaust_Node_or_NodeList_Name: str
    Zone_Air_Node_Name: str
    Zone_Return_Air_Node_or_NodeList_Name: str
    Zone_Return_Air_Node_1_Flow_Rate_Fraction_Schedule_Name: str
    Zone_Return_Air_Node_1_Flow_Rate_Basis_Node_or_NodeList_Name: str

class ZonehvacEquipmentlistType(TypedDict, total=False):
    """"dict for ZonehvacEquipmentlist"""
    Name: str
    Load_Distribution_Scheme: str
    Zone_Equipment_1_Object_Type: str
    Zone_Equipment_1_Name: str
    Zone_Equipment_1_Cooling_Sequence: str
    Zone_Equipment_1_Heating_or_NoLoad_Sequence: str
    Zone_Equipment_1_Sequential_Cooling_Fraction_Schedule_Name: str
    Zone_Equipment_1_Sequential_Heating_Fraction_Schedule_Name: str
    Zone_Equipment_2_Object_Type: str
    Zone_Equipment_2_Name: str
    Zone_Equipment_2_Cooling_Sequence: str
    Zone_Equipment_2_Heating_or_NoLoad_Sequence: str
    Zone_Equipment_2_Sequential_Cooling_Fraction_Schedule_Name: str
    Zone_Equipment_2_Sequential_Heating_Fraction_Schedule_Name: str
    Zone_Equipment_3_Object_Type: str
    Zone_Equipment_3_Name: str
    Zone_Equipment_3_Cooling_Sequence: str
    Zone_Equipment_3_Heating_or_NoLoad_Sequence: str
    Zone_Equipment_3_Sequential_Cooling_Fraction_Schedule_Name: str
    Zone_Equipment_3_Sequential_Heating_Fraction_Schedule_Name: str
    Zone_Equipment_4_Object_Type: str
    Zone_Equipment_4_Name: str
    Zone_Equipment_4_Cooling_Sequence: str
    Zone_Equipment_4_Heating_or_NoLoad_Sequence: str
    Zone_Equipment_4_Sequential_Cooling_Fraction_Schedule_Name: str
    Zone_Equipment_4_Sequential_Heating_Fraction_Schedule_Name: str
    Zone_Equipment_5_Object_Type: str
    Zone_Equipment_5_Name: str
    Zone_Equipment_5_Cooling_Sequence: str
    Zone_Equipment_5_Heating_or_NoLoad_Sequence: str
    Zone_Equipment_5_Sequential_Cooling_Fraction_Schedule_Name: str
    Zone_Equipment_5_Sequential_Heating_Fraction_Schedule_Name: str
    Zone_Equipment_6_Object_Type: str
    Zone_Equipment_6_Name: str
    Zone_Equipment_6_Cooling_Sequence: str
    Zone_Equipment_6_Heating_or_NoLoad_Sequence: str
    Zone_Equipment_6_Sequential_Cooling_Fraction_Schedule_Name: str
    Zone_Equipment_6_Sequential_Heating_Fraction_Schedule_Name: str
    Zone_Equipment_7_Object_Type: str
    Zone_Equipment_7_Name: str
    Zone_Equipment_7_Cooling_Sequence: str
    Zone_Equipment_7_Heating_or_NoLoad_Sequence: str
    Zone_Equipment_7_Sequential_Cooling_Fraction_Schedule_Name: str
    Zone_Equipment_7_Sequential_Heating_Fraction_Schedule_Name: str
    Zone_Equipment_8_Object_Type: str
    Zone_Equipment_8_Name: str
    Zone_Equipment_8_Cooling_Sequence: str
    Zone_Equipment_8_Heating_or_NoLoad_Sequence: str
    Zone_Equipment_8_Sequential_Cooling_Fraction_Schedule_Name: str
    Zone_Equipment_8_Sequential_Heating_Fraction_Schedule_Name: str
    Zone_Equipment_9_Object_Type: str
    Zone_Equipment_9_Name: str
    Zone_Equipment_9_Cooling_Sequence: str
    Zone_Equipment_9_Heating_or_NoLoad_Sequence: str
    Zone_Equipment_9_Sequential_Cooling_Fraction_Schedule_Name: str
    Zone_Equipment_9_Sequential_Heating_Fraction_Schedule_Name: str
    Zone_Equipment_10_Object_Type: str
    Zone_Equipment_10_Name: str
    Zone_Equipment_10_Cooling_Sequence: str
    Zone_Equipment_10_Heating_or_NoLoad_Sequence: str
    Zone_Equipment_10_Sequential_Cooling_Fraction_Schedule_Name: str
    Zone_Equipment_10_Sequential_Heating_Fraction_Schedule_Name: str
    Zone_Equipment_11_Object_Type: str
    Zone_Equipment_11_Name: str
    Zone_Equipment_11_Cooling_Sequence: str
    Zone_Equipment_11_Heating_or_NoLoad_Sequence: str
    Zone_Equipment_11_Sequential_Cooling_Fraction_Schedule_Name: str
    Zone_Equipment_11_Sequential_Heating_Fraction_Schedule_Name: str
    Zone_Equipment_12_Object_Type: str
    Zone_Equipment_12_Name: str
    Zone_Equipment_12_Cooling_Sequence: str
    Zone_Equipment_12_Heating_or_NoLoad_Sequence: str
    Zone_Equipment_12_Sequential_Cooling_Fraction_Schedule_Name: str
    Zone_Equipment_12_Sequential_Heating_Fraction_Schedule_Name: str
    Zone_Equipment_13_Object_Type: str
    Zone_Equipment_13_Name: str
    Zone_Equipment_13_Cooling_Sequence: str
    Zone_Equipment_13_Heating_or_NoLoad_Sequence: str
    Zone_Equipment_13_Sequential_Cooling_Fraction_Schedule_Name: str
    Zone_Equipment_13_Sequential_Heating_Fraction_Schedule_Name: str
    Zone_Equipment_14_Object_Type: str
    Zone_Equipment_14_Name: str
    Zone_Equipment_14_Cooling_Sequence: str
    Zone_Equipment_14_Heating_or_NoLoad_Sequence: str
    Zone_Equipment_14_Sequential_Cooling_Fraction_Schedule_Name: str
    Zone_Equipment_14_Sequential_Heating_Fraction_Schedule_Name: str
    Zone_Equipment_15_Object_Type: str
    Zone_Equipment_15_Name: str
    Zone_Equipment_15_Cooling_Sequence: str
    Zone_Equipment_15_Heating_or_NoLoad_Sequence: str
    Zone_Equipment_15_Sequential_Cooling_Fraction_Schedule_Name: str
    Zone_Equipment_15_Sequential_Heating_Fraction_Schedule_Name: str
    Zone_Equipment_16_Object_Type: str
    Zone_Equipment_16_Name: str
    Zone_Equipment_16_Cooling_Sequence: str
    Zone_Equipment_16_Heating_or_NoLoad_Sequence: str
    Zone_Equipment_16_Sequential_Cooling_Fraction_Schedule_Name: str
    Zone_Equipment_16_Sequential_Heating_Fraction_Schedule_Name: str
    Zone_Equipment_17_Object_Type: str
    Zone_Equipment_17_Name: str
    Zone_Equipment_17_Cooling_Sequence: str
    Zone_Equipment_17_Heating_or_NoLoad_Sequence: str
    Zone_Equipment_17_Sequential_Cooling_Fraction_Schedule_Name: str
    Zone_Equipment_17_Sequential_Heating_Fraction_Schedule_Name: str
    Zone_Equipment_18_Object_Type: str
    Zone_Equipment_18_Name: str
    Zone_Equipment_18_Cooling_Sequence: str
    Zone_Equipment_18_Heating_or_NoLoad_Sequence: str
    Zone_Equipment_18_Sequential_Cooling_Fraction_Schedule_Name: str
    Zone_Equipment_18_Sequential_Heating_Fraction_Schedule_Name: str

class ZonehvacEvaporativecoolerunitType(TypedDict, total=False):
    """"dict for ZonehvacEvaporativecoolerunit"""
    Name: str
    Availability_Schedule_Name: str
    Availability_Manager_List_Name: str
    Outdoor_Air_Inlet_Node_Name: str
    Cooler_Outlet_Node_Name: str
    Zone_Relief_Air_Node_Name: str
    Supply_Air_Fan_Object_Type: str
    Supply_Air_Fan_Name: str
    Design_Supply_Air_Flow_Rate: str
    Fan_Placement: str
    Cooler_Unit_Control_Method: str
    Throttling_Range_Temperature_Difference: str
    Cooling_Load_Control_Threshold_Heat_Transfer_Rate: str
    First_Evaporative_Cooler_Object_Type: str
    First_Evaporative_Cooler_Object_Name: str
    Second_Evaporative_Cooler_Object_Type: str
    Second_Evaporative_Cooler_Name: str
    Design_Specification_ZoneHVAC_Sizing_Object_Name: str
    Shut_Off_Relative_Humidity: str

class ZonehvacExhaustcontrolType(TypedDict, total=False):
    """"dict for ZonehvacExhaustcontrol"""
    Name: str
    Availability_Schedule_Name: str
    Zone_Name: str
    Inlet_Node_Name: str
    Outlet_Node_Name: str
    Design_Exhaust_Flow_Rate: str
    Flow_Control_Type: str
    Exhaust_Flow_Fraction_Schedule_Name: str
    Supply_Node_or_NodeList_Name: str
    Minimum_Zone_Temperature_Limit_Schedule_Name: str
    Minimum_Exhaust_Flow_Fraction_Schedule_Name: str
    Balanced_Exhaust_Fraction_Schedule_Name: str

class ZonehvacForcedairUserdefinedType(TypedDict, total=False):
    """"dict for ZonehvacForcedairUserdefined"""
    Name: str
    Overall_Model_Simulation_Program_Calling_Manager_Name: str
    Model_Setup_and_Sizing_Program_Calling_Manager_Name: str
    Primary_Air_Inlet_Node_Name: str
    Primary_Air_Outlet_Node_Name: str
    Secondary_Air_Inlet_Node_Name: str
    Secondary_Air_Outlet_Node_Name: str
    Number_of_Plant_Loop_Connections: str
    Plant_Connection_1_Inlet_Node_Name: str
    Plant_Connection_1_Outlet_Node_Name: str
    Plant_Connection_2_Inlet_Node_Name: str
    Plant_Connection_2_Outlet_Node_Name: str
    Plant_Connection_3_Inlet_Node_Name: str
    Plant_Connection_3_Outlet_Node_Name: str
    Supply_Inlet_Water_Storage_Tank_Name: str
    Collection_Outlet_Water_Storage_Tank_Name: str
    Ambient_Zone_Name: str

class ZonehvacFourpipefancoilType(TypedDict, total=False):
    """"dict for ZonehvacFourpipefancoil"""
    Name: str
    Availability_Schedule_Name: str
    Capacity_Control_Method: str
    Maximum_Supply_Air_Flow_Rate: str
    Low_Speed_Supply_Air_Flow_Ratio: str
    Medium_Speed_Supply_Air_Flow_Ratio: str
    Maximum_Outdoor_Air_Flow_Rate: str
    Outdoor_Air_Schedule_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Outdoor_Air_Mixer_Object_Type: str
    Outdoor_Air_Mixer_Name: str
    Supply_Air_Fan_Object_Type: str
    Supply_Air_Fan_Name: str
    Cooling_Coil_Object_Type: str
    Cooling_Coil_Name: str
    Maximum_Cold_Water_Flow_Rate: str
    Minimum_Cold_Water_Flow_Rate: str
    Cooling_Convergence_Tolerance: str
    Heating_Coil_Object_Type: str
    Heating_Coil_Name: str
    Maximum_Hot_Water_Flow_Rate: str
    Minimum_Hot_Water_Flow_Rate: str
    Heating_Convergence_Tolerance: str
    Availability_Manager_List_Name: str
    Design_Specification_ZoneHVAC_Sizing_Object_Name: str
    Supply_Air_Fan_Operating_Mode_Schedule_Name: str
    Minimum_Supply_Air_Temperature_in_Cooling_Mode: str
    Maximum_Supply_Air_Temperature_in_Heating_Mode: str

class ZonehvacHightemperatureradiantType(TypedDict, total=False):
    """"dict for ZonehvacHightemperatureradiant"""
    Name: str
    Availability_Schedule_Name: str
    Zone_Name: str
    Heating_Design_Capacity_Method: str
    Heating_Design_Capacity: str
    Heating_Design_Capacity_Per_Floor_Area: str
    Fraction_of_Autosized_Heating_Design_Capacity: str
    Fuel_Type: str
    Combustion_Efficiency: str
    Fraction_of_Input_Converted_to_Radiant_Energy: str
    Fraction_of_Input_Converted_to_Latent_Energy: str
    Fraction_of_Input_that_Is_Lost: str
    Temperature_Control_Type: str
    Heating_Throttling_Range: str
    Heating_Setpoint_Temperature_Schedule_Name: str
    Fraction_of_Radiant_Energy_Incident_on_People: str
    Surface_1_Name: str
    Fraction_of_Radiant_Energy_to_Surface_1: str
    Surface_2_Name: str
    Fraction_of_Radiant_Energy_to_Surface_2: str
    Surface_3_Name: str
    Fraction_of_Radiant_Energy_to_Surface_3: str
    Surface_4_Name: str
    Fraction_of_Radiant_Energy_to_Surface_4: str
    Surface_5_Name: str
    Fraction_of_Radiant_Energy_to_Surface_5: str
    Surface_6_Name: str
    Fraction_of_Radiant_Energy_to_Surface_6: str
    Surface_7_Name: str
    Fraction_of_Radiant_Energy_to_Surface_7: str
    Surface_8_Name: str
    Fraction_of_Radiant_Energy_to_Surface_8: str
    Surface_9_Name: str
    Fraction_of_Radiant_Energy_to_Surface_9: str
    Surface_10_Name: str
    Fraction_of_Radiant_Energy_to_Surface_10: str
    Surface_11_Name: str
    Fraction_of_Radiant_Energy_to_Surface_11: str
    Surface_12_Name: str
    Fraction_of_Radiant_Energy_to_Surface_12: str
    Surface_13_Name: str
    Fraction_of_Radiant_Energy_to_Surface_13: str
    Surface_14_Name: str
    Fraction_of_Radiant_Energy_to_Surface_14: str
    Surface_15_Name: str
    Fraction_of_Radiant_Energy_to_Surface_15: str
    Surface_16_Name: str
    Fraction_of_Radiant_Energy_to_Surface_16: str
    Surface_17_Name: str
    Fraction_of_Radiant_Energy_to_Surface_17: str
    Surface_18_Name: str
    Fraction_of_Radiant_Energy_to_Surface_18: str
    Surface_19_Name: str
    Fraction_of_Radiant_Energy_to_Surface_19: str
    Surface_20_Name: str
    Fraction_of_Radiant_Energy_to_Surface_20: str
    Surface_21_Name: str
    Fraction_of_Radiant_Energy_to_Surface_21: str
    Surface_22_Name: str
    Fraction_of_Radiant_Energy_to_Surface_22: str
    Surface_23_Name: str
    Fraction_of_Radiant_Energy_to_Surface_23: str
    Surface_24_Name: str
    Fraction_of_Radiant_Energy_to_Surface_24: str
    Surface_25_Name: str
    Fraction_of_Radiant_Energy_to_Surface_25: str
    Surface_26_Name: str
    Fraction_of_Radiant_Energy_to_Surface_26: str
    Surface_27_Name: str
    Fraction_of_Radiant_Energy_to_Surface_27: str
    Surface_28_Name: str
    Fraction_of_Radiant_Energy_to_Surface_28: str
    Surface_29_Name: str
    Fraction_of_Radiant_Energy_to_Surface_29: str
    Surface_30_Name: str
    Fraction_of_Radiant_Energy_to_Surface_30: str
    Surface_31_Name: str
    Fraction_of_Radiant_Energy_to_Surface_31: str
    Surface_32_Name: str
    Fraction_of_Radiant_Energy_to_Surface_32: str
    Surface_33_Name: str
    Fraction_of_Radiant_Energy_to_Surface_33: str
    Surface_34_Name: str
    Fraction_of_Radiant_Energy_to_Surface_34: str
    Surface_35_Name: str
    Fraction_of_Radiant_Energy_to_Surface_35: str
    Surface_36_Name: str
    Fraction_of_Radiant_Energy_to_Surface_36: str
    Surface_37_Name: str
    Fraction_of_Radiant_Energy_to_Surface_37: str
    Surface_38_Name: str
    Fraction_of_Radiant_Energy_to_Surface_38: str
    Surface_39_Name: str
    Fraction_of_Radiant_Energy_to_Surface_39: str
    Surface_40_Name: str
    Fraction_of_Radiant_Energy_to_Surface_40: str
    Surface_41_Name: str
    Fraction_of_Radiant_Energy_to_Surface_41: str
    Surface_42_Name: str
    Fraction_of_Radiant_Energy_to_Surface_42: str
    Surface_43_Name: str
    Fraction_of_Radiant_Energy_to_Surface_43: str
    Surface_44_Name: str
    Fraction_of_Radiant_Energy_to_Surface_44: str
    Surface_45_Name: str
    Fraction_of_Radiant_Energy_to_Surface_45: str
    Surface_46_Name: str
    Fraction_of_Radiant_Energy_to_Surface_46: str
    Surface_47_Name: str
    Fraction_of_Radiant_Energy_to_Surface_47: str
    Surface_48_Name: str
    Fraction_of_Radiant_Energy_to_Surface_48: str
    Surface_49_Name: str
    Fraction_of_Radiant_Energy_to_Surface_49: str

class ZonehvacHybridunitaryhvacType(TypedDict, total=False):
    """"dict for ZonehvacHybridunitaryhvac"""
    Name: str
    Availability_Schedule_Name: str
    Availability_Manager_List_Name: str
    Minimum_Supply_Air_Temperature_Schedule_Name: str
    Maximum_Supply_Air_Temperature_Schedule_Name: str
    Minimum_Supply_Air_Humidity_Ratio_Schedule_Name: str
    Maximum_Supply_Air_Humidity_Ratio_Schedule_Name: str
    Method_to_Choose_Controlled_Inputs_and_Part_Runtime_Fraction: str
    Return_Air_Node_Name: str
    Outdoor_Air_Node_Name: str
    Supply_Air_Node_Name: str
    Relief_Node_Name: str
    System_Maximum_Supply_Air_Flow_Rate: str
    External_Static_Pressure_at_System_Maximum_Supply_Air_Flow_Rate: str
    Fan_Heat_Included_in_Lookup_Tables: str
    Fan_Heat_Gain_Location: str
    Fan_Heat_In_Air_Stream_Fraction: str
    Scaling_Factor: str
    Minimum_Time_Between_Mode_Change: str
    First_Fuel_Type: str
    Second_Fuel_Type: str
    Third_Fuel_Type: str
    Objective_Function_to_Minimize: str
    Design_Specification_Outdoor_Air_Object_Name: str
    Mode_0_Name: str
    Mode_0_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_0_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_0_System_Electric_Power_Lookup_Table_Name: str
    Mode_0_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_0_External_Static_Pressure_Lookup_Table_Name: str
    Mode_0_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_0_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_0_System_Water_Use_Lookup_Table_Name: str
    Mode_0_Outdoor_Air_Fraction: str
    Mode_0_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_1_Name: str
    Mode_1_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_1_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_1_System_Electric_Power_Lookup_Table_Name: str
    Mode_1_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_1_External_Static_Pressure_Lookup_Table_Name: str
    Mode_1_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_1_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_1_System_Water_Use_Lookup_Table_Name: str
    Mode_1_Minimum_Outdoor_Air_Temperature: str
    Mode_1_Maximum_Outdoor_Air_Temperature: str
    Mode_1_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_1_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_1_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_1_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_1_Minimum_Return_Air_Temperature: str
    Mode_1_Maximum_Return_Air_Temperature: str
    Mode_1_Minimum_Return_Air_Humidity_Ratio: str
    Mode_1_Maximum_Return_Air_Humidity_Ratio: str
    Mode_1_Minimum_Return_Air_Relative_Humidity: str
    Mode_1_Maximum_Return_Air_Relative_Humidity: str
    Mode_1_Minimum_Outdoor_Air_Fraction: str
    Mode_1_Maximum_Outdoor_Air_Fraction: str
    Mode_1_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_1_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_2_Name: str
    Mode_2_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_2_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_2_System_Electric_Power_Lookup_Table_Name: str
    Mode_2_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_2_External_Static_Pressure_Lookup_Table_Name: str
    Mode_2_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_2_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_2_System_Water_Use_Lookup_Table_Name: str
    Mode_2_Minimum_Outdoor_Air_Temperature: str
    Mode_2_Maximum_Outdoor_Air_Temperature: str
    Mode_2_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_2_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_2_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_2_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_2_Minimum_Return_Air_Temperature: str
    Mode_2_Maximum_Return_Air_Temperature: str
    Mode_2_Minimum_Return_Air_Humidity_Ratio: str
    Mode_2_Maximum_Return_Air_Humidity_Ratio: str
    Mode_2_Minimum_Return_Air_Relative_Humidity: str
    Mode_2_Maximum_Return_Air_Relative_Humidity: str
    Mode_2_Minimum_Outdoor_Air_Fraction: str
    Mode_2_Maximum_Outdoor_Air_Fraction: str
    Mode_2_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_2_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_3_Name: str
    Mode_3_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_3_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_3_System_Electric_Power_Lookup_Table_Name: str
    Mode_3_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_3_External_Static_Pressure_Lookup_Table_Name: str
    Mode_3_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_3_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_3_System_Water_Use_Lookup_Table_Name: str
    Mode_3_Minimum_Outdoor_Air_Temperature: str
    Mode_3_Maximum_Outdoor_Air_Temperature: str
    Mode_3_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_3_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_3_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_3_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_3_Minimum_Return_Air_Temperature: str
    Mode_3_Maximum_Return_Air_Temperature: str
    Mode_3_Minimum_Return_Air_Humidity_Ratio: str
    Mode_3_Maximum_Return_Air_Humidity_Ratio: str
    Mode_3_Minimum_Return_Air_Relative_Humidity: str
    Mode_3_Maximum_Return_Air_Relative_Humidity: str
    Mode_3_Minimum_Outdoor_Air_Fraction: str
    Mode_3_Maximum_Outdoor_Air_Fraction: str
    Mode_3_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_3_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_4_Name: str
    Mode_4_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_4_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_4_System_Electric_Power_Lookup_Table_Name: str
    Mode_4_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_4_External_Static_Pressure_Lookup_Table_Name: str
    Mode_4_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_4_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_4_System_Water_Use_Lookup_Table_Name: str
    Mode_4_Minimum_Outdoor_Air_Temperature: str
    Mode_4_Maximum_Outdoor_Air_Temperature: str
    Mode_4_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_4_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_4_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_4_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_4_Minimum_Return_Air_Temperature: str
    Mode_4_Maximum_Return_Air_Temperature: str
    Mode_4_Minimum_Return_Air_Humidity_Ratio: str
    Mode_4_Maximum_Return_Air_Humidity_Ratio: str
    Mode_4_Minimum_Return_Air_Relative_Humidity: str
    Mode_4_Maximum_Return_Air_Relative_Humidity: str
    Mode_4_Minimum_Outdoor_Air_Fraction: str
    Mode_4_Maximum_Outdoor_Air_Fraction: str
    Mode_4_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_4_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_5_Name: str
    Mode_5_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_5_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_5_System_Electric_Power_Lookup_Table_Name: str
    Mode_5_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_5_External_Static_Pressure_Lookup_Table_Name: str
    Mode_5_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_5_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_5_System_Water_Use_Lookup_Table_Name: str
    Mode_5_Minimum_Outdoor_Air_Temperature: str
    Mode_5_Maximum_Outdoor_Air_Temperature: str
    Mode_5_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_5_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_5_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_5_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_5_Minimum_Return_Air_Temperature: str
    Mode_5_Maximum_Return_Air_Temperature: str
    Mode_5_Minimum_Return_Air_Humidity_Ratio: str
    Mode_5_Maximum_Return_Air_Humidity_Ratio: str
    Mode_5_Minimum_Return_Air_Relative_Humidity: str
    Mode_5_Maximum_Return_Air_Relative_Humidity: str
    Mode_5_Minimum_Outdoor_Air_Fraction: str
    Mode_5_Maximum_Outdoor_Air_Fraction: str
    Mode_5_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_5_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_6_Name: str
    Mode_6_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_6_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_6_System_Electric_Power_Lookup_Table_Name: str
    Mode_6_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_6_External_Static_Pressure_Lookup_Table_Name: str
    Mode_6_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_6_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_6_System_Water_Use_Lookup_Table_Name: str
    Mode_6_Minimum_Outdoor_Air_Temperature: str
    Mode_6_Maximum_Outdoor_Air_Temperature: str
    Mode_6_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_6_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_6_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_6_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_6_Minimum_Return_Air_Temperature: str
    Mode_6_Maximum_Return_Air_Temperature: str
    Mode_6_Minimum_Return_Air_Humidity_Ratio: str
    Mode_6_Maximum_Return_Air_Humidity_Ratio: str
    Mode_6_Minimum_Return_Air_Relative_Humidity: str
    Mode_6_Maximum_Return_Air_Relative_Humidity: str
    Mode_6_Minimum_Outdoor_Air_Fraction: str
    Mode_6_Maximum_Outdoor_Air_Fraction: str
    Mode_6_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_6_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_7_Name: str
    Mode_7_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_7_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_7_System_Electric_Power_Lookup_Table_Name: str
    Mode_7_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_7_External_Static_Pressure_Lookup_Table_Name: str
    Mode_7_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_7_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_7_System_Water_Use_Lookup_Table_Name: str
    Mode_7_Minimum_Outdoor_Air_Temperature: str
    Mode_7_Maximum_Outdoor_Air_Temperature: str
    Mode_7_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_7_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_7_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_7_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_7_Minimum_Return_Air_Temperature: str
    Mode_7_Maximum_Return_Air_Temperature: str
    Mode_7_Minimum_Return_Air_Humidity_Ratio: str
    Mode_7_Maximum_Return_Air_Humidity_Ratio: str
    Mode_7_Minimum_Return_Air_Relative_Humidity: str
    Mode_7_Maximum_Return_Air_Relative_Humidity: str
    Mode_7_Minimum_Outdoor_Air_Fraction: str
    Mode_7_Maximum_Outdoor_Air_Fraction: str
    Mode_7_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_7_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_8_Name: str
    Mode_8_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_8_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_8_System_Electric_Power_Lookup_Table_Name: str
    Mode_8_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_8_External_Static_Pressure_Lookup_Table_Name: str
    Mode_8_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_8_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_8_System_Water_Use_Lookup_Table_Name: str
    Mode_8_Minimum_Outdoor_Air_Temperature: str
    Mode_8_Maximum_Outdoor_Air_Temperature: str
    Mode_8_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_8_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_8_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_8_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_8_Minimum_Return_Air_Temperature: str
    Mode_8_Maximum_Return_Air_Temperature: str
    Mode_8_Minimum_Return_Air_Humidity_Ratio: str
    Mode_8_Maximum_Return_Air_Humidity_Ratio: str
    Mode_8_Minimum_Return_Air_Relative_Humidity: str
    Mode_8_Maximum_Return_Air_Relative_Humidity: str
    Mode_8_Minimum_Outdoor_Air_Fraction: str
    Mode_8_Maximum_Outdoor_Air_Fraction: str
    Mode_8_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_8_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_9_Name: str
    Mode_9_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_9_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_9_System_Electric_Power_Lookup_Table_Name: str
    Mode_9_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_9_External_Static_Pressure_Lookup_Table_Name: str
    Mode_9_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_9_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_9_System_Water_Use_Lookup_Table_Name: str
    Mode_9_Minimum_Outdoor_Air_Temperature: str
    Mode_9_Maximum_Outdoor_Air_Temperature: str
    Mode_9_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_9_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_9_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_9_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_9_Minimum_Return_Air_Temperature: str
    Mode_9_Maximum_Return_Air_Temperature: str
    Mode_9_Minimum_Return_Air_Humidity_Ratio: str
    Mode_9_Maximum_Return_Air_Humidity_Ratio: str
    Mode_9_Minimum_Return_Air_Relative_Humidity: str
    Mode_9_Maximum_Return_Air_Relative_Humidity: str
    Mode_9_Minimum_Outdoor_Air_Fraction: str
    Mode_9_Maximum_Outdoor_Air_Fraction: str
    Mode_9_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_9_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_10_Name: str
    Mode_10_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_10_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_10_System_Electric_Power_Lookup_Table_Name: str
    Mode_10_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_10_External_Static_Pressure_Lookup_Table_Name: str
    Mode_10_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_10_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_10_System_Water_Use_Lookup_Table_Name: str
    Mode_10_Minimum_Outdoor_Air_Temperature: str
    Mode_10_Maximum_Outdoor_Air_Temperature: str
    Mode_10_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_10_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_10_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_10_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_10_Minimum_Return_Air_Temperature: str
    Mode_10_Maximum_Return_Air_Temperature: str
    Mode_10_Minimum_Return_Air_Humidity_Ratio: str
    Mode_10_Maximum_Return_Air_Humidity_Ratio: str
    Mode_10_Minimum_Return_Air_Relative_Humidity: str
    Mode_10_Maximum_Return_Air_Relative_Humidity: str
    Mode_10_Minimum_Outdoor_Air_Fraction: str
    Mode_10_Maximum_Outdoor_Air_Fraction: str
    Mode_10_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_10_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_11_Name: str
    Mode_11_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_11_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_11_System_Electric_Power_Lookup_Table_Name: str
    Mode_11_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_11_External_Static_Pressure_Lookup_Table_Name: str
    Mode_11_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_11_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_11_System_Water_Use_Lookup_Table_Name: str
    Mode_11_Minimum_Outdoor_Air_Temperature: str
    Mode_11_Maximum_Outdoor_Air_Temperature: str
    Mode_11_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_11_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_11_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_11_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_11_Minimum_Return_Air_Temperature: str
    Mode_11_Maximum_Return_Air_Temperature: str
    Mode_11_Minimum_Return_Air_Humidity_Ratio: str
    Mode_11_Maximum_Return_Air_Humidity_Ratio: str
    Mode_11_Minimum_Return_Air_Relative_Humidity: str
    Mode_11_Maximum_Return_Air_Relative_Humidity: str
    Mode_11_Minimum_Outdoor_Air_Fraction: str
    Mode_11_Maximum_Outdoor_Air_Fraction: str
    Mode_11_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_11_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_12_Name: str
    Mode_12_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_12_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_12_System_Electric_Power_Lookup_Table_Name: str
    Mode_12_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_12_External_Static_Pressure_Lookup_Table_Name: str
    Mode_12_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_12_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_12_System_Water_Use_Lookup_Table_Name: str
    Mode_12_Minimum_Outdoor_Air_Temperature: str
    Mode_12_Maximum_Outdoor_Air_Temperature: str
    Mode_12_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_12_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_12_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_12_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_12_Minimum_Return_Air_Temperature: str
    Mode_12_Maximum_Return_Air_Temperature: str
    Mode_12_Minimum_Return_Air_Humidity_Ratio: str
    Mode_12_Maximum_Return_Air_Humidity_Ratio: str
    Mode_12_Minimum_Return_Air_Relative_Humidity: str
    Mode_12_Maximum_Return_Air_Relative_Humidity: str
    Mode_12_Minimum_Outdoor_Air_Fraction: str
    Mode_12_Maximum_Outdoor_Air_Fraction: str
    Mode_12_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_12_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_13_Name: str
    Mode_13_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_13_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_13_System_Electric_Power_Lookup_Table_Name: str
    Mode_13_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_13_External_Static_Pressure_Lookup_Table_Name: str
    Mode_13_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_13_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_13_System_Water_Use_Lookup_Table_Name: str
    Mode_13_Minimum_Outdoor_Air_Temperature: str
    Mode_13_Maximum_Outdoor_Air_Temperature: str
    Mode_13_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_13_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_13_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_13_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_13_Minimum_Return_Air_Temperature: str
    Mode_13_Maximum_Return_Air_Temperature: str
    Mode_13_Minimum_Return_Air_Humidity_Ratio: str
    Mode_13_Maximum_Return_Air_Humidity_Ratio: str
    Mode_13_Minimum_Return_Air_Relative_Humidity: str
    Mode_13_Maximum_Return_Air_Relative_Humidity: str
    Mode_13_Minimum_Outdoor_Air_Fraction: str
    Mode_13_Maximum_Outdoor_Air_Fraction: str
    Mode_13_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_13_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_14_Name: str
    Mode_14_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_14_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_14_System_Electric_Power_Lookup_Table_Name: str
    Mode_14_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_14_External_Static_Pressure_Lookup_Table_Name: str
    Mode_14_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_14_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_14_System_Water_Use_Lookup_Table_Name: str
    Mode_14_Minimum_Outdoor_Air_Temperature: str
    Mode_14_Maximum_Outdoor_Air_Temperature: str
    Mode_14_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_14_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_14_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_14_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_14_Minimum_Return_Air_Temperature: str
    Mode_14_Maximum_Return_Air_Temperature: str
    Mode_14_Minimum_Return_Air_Humidity_Ratio: str
    Mode_14_Maximum_Return_Air_Humidity_Ratio: str
    Mode_14_Minimum_Return_Air_Relative_Humidity: str
    Mode_14_Maximum_Return_Air_Relative_Humidity: str
    Mode_14_Minimum_Outdoor_Air_Fraction: str
    Mode_14_Maximum_Outdoor_Air_Fraction: str
    Mode_14_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_14_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_15_Name: str
    Mode_15_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_15_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_15_System_Electric_Power_Lookup_Table_Name: str
    Mode_15_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_15_External_Static_Pressure_Lookup_Table_Name: str
    Mode_15_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_15_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_15_System_Water_Use_Lookup_Table_Name: str
    Mode_15_Minimum_Outdoor_Air_Temperature: str
    Mode_15_Maximum_Outdoor_Air_Temperature: str
    Mode_15_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_15_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_15_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_15_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_15_Minimum_Return_Air_Temperature: str
    Mode_15_Maximum_Return_Air_Temperature: str
    Mode_15_Minimum_Return_Air_Humidity_Ratio: str
    Mode_15_Maximum_Return_Air_Humidity_Ratio: str
    Mode_15_Minimum_Return_Air_Relative_Humidity: str
    Mode_15_Maximum_Return_Air_Relative_Humidity: str
    Mode_15_Minimum_Outdoor_Air_Fraction: str
    Mode_15_Maximum_Outdoor_Air_Fraction: str
    Mode_15_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_15_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_16_Name: str
    Mode_16_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_16_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_16_System_Electric_Power_Lookup_Table_Name: str
    Mode_16_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_16_External_Static_Pressure_Lookup_Table_Name: str
    Mode_16_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_16_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_16_System_Water_Use_Lookup_Table_Name: str
    Mode_16_Minimum_Outdoor_Air_Temperature: str
    Mode_16_Maximum_Outdoor_Air_Temperature: str
    Mode_16_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_16_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_16_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_16_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_16_Minimum_Return_Air_Temperature: str
    Mode_16_Maximum_Return_Air_Temperature: str
    Mode_16_Minimum_Return_Air_Humidity_Ratio: str
    Mode_16_Maximum_Return_Air_Humidity_Ratio: str
    Mode_16_Minimum_Return_Air_Relative_Humidity: str
    Mode_16_Maximum_Return_Air_Relative_Humidity: str
    Mode_16_Minimum_Outdoor_Air_Fraction: str
    Mode_16_Maximum_Outdoor_Air_Fraction: str
    Mode_16_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_16_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_17_Name: str
    Mode_17_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_17_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_17_System_Electric_Power_Lookup_Table_Name: str
    Mode_17_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_17_External_Static_Pressure_Lookup_Table_Name: str
    Mode_17_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_17_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_17_System_Water_Use_Lookup_Table_Name: str
    Mode_17_Minimum_Outdoor_Air_Temperature: str
    Mode_17_Maximum_Outdoor_Air_Temperature: str
    Mode_17_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_17_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_17_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_17_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_17_Minimum_Return_Air_Temperature: str
    Mode_17_Maximum_Return_Air_Temperature: str
    Mode_17_Minimum_Return_Air_Humidity_Ratio: str
    Mode_17_Maximum_Return_Air_Humidity_Ratio: str
    Mode_17_Minimum_Return_Air_Relative_Humidity: str
    Mode_17_Maximum_Return_Air_Relative_Humidity: str
    Mode_17_Minimum_Outdoor_Air_Fraction: str
    Mode_17_Maximum_Outdoor_Air_Fraction: str
    Mode_17_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_17_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_18_Name: str
    Mode_18_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_18_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_18_System_Electric_Power_Lookup_Table_Name: str
    Mode_18_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_18_External_Static_Pressure_Lookup_Table_Name: str
    Mode_18_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_18_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_18_System_Water_Use_Lookup_Table_Name: str
    Mode_18_Minimum_Outdoor_Air_Temperature: str
    Mode_18_Maximum_Outdoor_Air_Temperature: str
    Mode_18_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_18_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_18_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_18_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_18_Minimum_Return_Air_Temperature: str
    Mode_18_Maximum_Return_Air_Temperature: str
    Mode_18_Minimum_Return_Air_Humidity_Ratio: str
    Mode_18_Maximum_Return_Air_Humidity_Ratio: str
    Mode_18_Minimum_Return_Air_Relative_Humidity: str
    Mode_18_Maximum_Return_Air_Relative_Humidity: str
    Mode_18_Minimum_Outdoor_Air_Fraction: str
    Mode_18_Maximum_Outdoor_Air_Fraction: str
    Mode_18_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_18_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_19_Name: str
    Mode_19_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_19_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_19_System_Electric_Power_Lookup_Table_Name: str
    Mode_19_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_19_External_Static_Pressure_Lookup_Table_Name: str
    Mode_19_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_19_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_19_System_Water_Use_Lookup_Table_Name: str
    Mode_19_Minimum_Outdoor_Air_Temperature: str
    Mode_19_Maximum_Outdoor_Air_Temperature: str
    Mode_19_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_19_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_19_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_19_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_19_Minimum_Return_Air_Temperature: str
    Mode_19_Maximum_Return_Air_Temperature: str
    Mode_19_Minimum_Return_Air_Humidity_Ratio: str
    Mode_19_Maximum_Return_Air_Humidity_Ratio: str
    Mode_19_Minimum_Return_Air_Relative_Humidity: str
    Mode_19_Maximum_Return_Air_Relative_Humidity: str
    Mode_19_Minimum_Outdoor_Air_Fraction: str
    Mode_19_Maximum_Outdoor_Air_Fraction: str
    Mode_19_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_19_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_20_Name: str
    Mode_20_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_20_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_20_System_Electric_Power_Lookup_Table_Name: str
    Mode_20_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_20_External_Static_Pressure_Lookup_Table_Name: str
    Mode_20_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_20_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_20_System_Water_Use_Lookup_Table_Name: str
    Mode_20_Minimum_Outdoor_Air_Temperature: str
    Mode_20_Maximum_Outdoor_Air_Temperature: str
    Mode_20_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_20_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_20_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_20_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_20_Minimum_Return_Air_Temperature: str
    Mode_20_Maximum_Return_Air_Temperature: str
    Mode_20_Minimum_Return_Air_Humidity_Ratio: str
    Mode_20_Maximum_Return_Air_Humidity_Ratio: str
    Mode_20_Minimum_Return_Air_Relative_Humidity: str
    Mode_20_Maximum_Return_Air_Relative_Humidity: str
    Mode_20_Minimum_Outdoor_Air_Fraction: str
    Mode_20_Maximum_Outdoor_Air_Fraction: str
    Mode_20_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_20_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_21_Name: str
    Mode_21_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_21_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_21_System_Electric_Power_Lookup_Table_Name: str
    Mode_21_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_21_External_Static_Pressure_Lookup_Table_Name: str
    Mode_21_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_21_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_21_System_Water_Use_Lookup_Table_Name: str
    Mode_21_Minimum_Outdoor_Air_Temperature: str
    Mode_21_Maximum_Outdoor_Air_Temperature: str
    Mode_21_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_21_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_21_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_21_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_21_Minimum_Return_Air_Temperature: str
    Mode_21_Maximum_Return_Air_Temperature: str
    Mode_21_Minimum_Return_Air_Humidity_Ratio: str
    Mode_21_Maximum_Return_Air_Humidity_Ratio: str
    Mode_21_Minimum_Return_Air_Relative_Humidity: str
    Mode_21_Maximum_Return_Air_Relative_Humidity: str
    Mode_21_Minimum_Outdoor_Air_Fraction: str
    Mode_21_Maximum_Outdoor_Air_Fraction: str
    Mode_21_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_21_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_22_Name: str
    Mode_22_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_22_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_22_System_Electric_Power_Lookup_Table_Name: str
    Mode_22_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_22_External_Static_Pressure_Lookup_Table_Name: str
    Mode_22_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_22_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_22_System_Water_Use_Lookup_Table_Name: str
    Mode_22_Minimum_Outdoor_Air_Temperature: str
    Mode_22_Maximum_Outdoor_Air_Temperature: str
    Mode_22_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_22_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_22_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_22_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_22_Minimum_Return_Air_Temperature: str
    Mode_22_Maximum_Return_Air_Temperature: str
    Mode_22_Minimum_Return_Air_Humidity_Ratio: str
    Mode_22_Maximum_Return_Air_Humidity_Ratio: str
    Mode_22_Minimum_Return_Air_Relative_Humidity: str
    Mode_22_Maximum_Return_Air_Relative_Humidity: str
    Mode_22_Minimum_Outdoor_Air_Fraction: str
    Mode_22_Maximum_Outdoor_Air_Fraction: str
    Mode_22_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_22_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_23_Name: str
    Mode_23_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_23_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_23_System_Electric_Power_Lookup_Table_Name: str
    Mode_23_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_23_External_Static_Pressure_Lookup_Table_Name: str
    Mode_23_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_23_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_23_System_Water_Use_Lookup_Table_Name: str
    Mode_23_Minimum_Outdoor_Air_Temperature: str
    Mode_23_Maximum_Outdoor_Air_Temperature: str
    Mode_23_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_23_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_23_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_23_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_23_Minimum_Return_Air_Temperature: str
    Mode_23_Maximum_Return_Air_Temperature: str
    Mode_23_Minimum_Return_Air_Humidity_Ratio: str
    Mode_23_Maximum_Return_Air_Humidity_Ratio: str
    Mode_23_Minimum_Return_Air_Relative_Humidity: str
    Mode_23_Maximum_Return_Air_Relative_Humidity: str
    Mode_23_Minimum_Outdoor_Air_Fraction: str
    Mode_23_Maximum_Outdoor_Air_Fraction: str
    Mode_23_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_23_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_24_Name: str
    Mode_24_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_24_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_24_System_Electric_Power_Lookup_Table_Name: str
    Mode_24_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_24_External_Static_Pressure_Lookup_Table_Name: str
    Mode_24_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_24_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_24_System_Water_Use_Lookup_Table_Name: str
    Mode_24_Minimum_Outdoor_Air_Temperature: str
    Mode_24_Maximum_Outdoor_Air_Temperature: str
    Mode_24_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_24_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_24_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_24_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_24_Minimum_Return_Air_Temperature: str
    Mode_24_Maximum_Return_Air_Temperature: str
    Mode_24_Minimum_Return_Air_Humidity_Ratio: str
    Mode_24_Maximum_Return_Air_Humidity_Ratio: str
    Mode_24_Minimum_Return_Air_Relative_Humidity: str
    Mode_24_Maximum_Return_Air_Relative_Humidity: str
    Mode_24_Minimum_Outdoor_Air_Fraction: str
    Mode_24_Maximum_Outdoor_Air_Fraction: str
    Mode_24_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_24_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_25_Name: str
    Mode_25_Supply_Air_Temperature_Lookup_Table_Name: str
    Mode_25_Supply_Air_Humidity_Ratio_Lookup_Table_Name: str
    Mode_25_System_Electric_Power_Lookup_Table_Name: str
    Mode_25_Supply_Fan_Electric_Power_Lookup_Table_Name: str
    Mode_25_External_Static_Pressure_Lookup_Table_Name: str
    Mode_25_System_Second_Fuel_Consumption_Lookup_Table_Name: str
    Mode_25_System_Third_Fuel_Consumption_Lookup_Table_Name: str
    Mode_25_System_Water_Use_Lookup_Table_Name: str
    Mode_25_Minimum_Outdoor_Air_Temperature: str
    Mode_25_Maximum_Outdoor_Air_Temperature: str
    Mode_25_Minimum_Outdoor_Air_Humidity_Ratio: str
    Mode_25_Maximum_Outdoor_Air_Humidity_Ratio: str
    Mode_25_Minimum_Outdoor_Air_Relative_Humidity: str
    Mode_25_Maximum_Outdoor_Air_Relative_Humidity: str
    Mode_25_Minimum_Return_Air_Temperature: str
    Mode_25_Maximum_Return_Air_Temperature: str
    Mode_25_Minimum_Return_Air_Humidity_Ratio: str
    Mode_25_Maximum_Return_Air_Humidity_Ratio: str
    Mode_25_Minimum_Return_Air_Relative_Humidity: str
    Mode_25_Maximum_Return_Air_Relative_Humidity: str
    Mode_25_Minimum_Outdoor_Air_Fraction: str
    Mode_25_Maximum_Outdoor_Air_Fraction: str
    Mode_25_Minimum_Supply_Air_Mass_Flow_Rate_Ratio: str
    Mode_25_Maximum_Supply_Air_Mass_Flow_Rate_Ratio: str

class ZonehvacIdealloadsairsystemType(TypedDict, total=False):
    """"dict for ZonehvacIdealloadsairsystem"""
    Name: str
    Availability_Schedule_Name: str
    Zone_Supply_Air_Node_Name: str
    Zone_Exhaust_Air_Node_Name: str
    System_Inlet_Air_Node_Name: str
    Maximum_Heating_Supply_Air_Temperature: str
    Minimum_Cooling_Supply_Air_Temperature: str
    Maximum_Heating_Supply_Air_Humidity_Ratio: str
    Minimum_Cooling_Supply_Air_Humidity_Ratio: str
    Heating_Limit: str
    Maximum_Heating_Air_Flow_Rate: str
    Maximum_Sensible_Heating_Capacity: str
    Cooling_Limit: str
    Maximum_Cooling_Air_Flow_Rate: str
    Maximum_Total_Cooling_Capacity: str
    Heating_Availability_Schedule_Name: str
    Cooling_Availability_Schedule_Name: str
    Dehumidification_Control_Type: str
    Cooling_Sensible_Heat_Ratio: str
    Humidification_Control_Type: str
    Design_Specification_Outdoor_Air_Object_Name: str
    Outdoor_Air_Inlet_Node_Name: str
    Demand_Controlled_Ventilation_Type: str
    Outdoor_Air_Economizer_Type: str
    Heat_Recovery_Type: str
    Sensible_Heat_Recovery_Effectiveness: str
    Latent_Heat_Recovery_Effectiveness: str
    Design_Specification_ZoneHVAC_Sizing_Object_Name: str

class ZonehvacLowtemperatureradiantConstantflowType(TypedDict, total=False):
    """"dict for ZonehvacLowtemperatureradiantConstantflow"""
    Name: str
    Design_Object: str
    Availability_Schedule_Name: str
    Zone_Name: str
    Surface_Name_or_Radiant_Surface_Group_Name: str
    Hydronic_Tubing_Length: str
    Rated_Flow_Rate: str
    Pump_Flow_Rate_Schedule_Name: str
    Rated_Pump_Head: str
    Rated_Power_Consumption: str
    Heating_Water_Inlet_Node_Name: str
    Heating_Water_Outlet_Node_Name: str
    Heating_High_Water_Temperature_Schedule_Name: str
    Heating_Low_Water_Temperature_Schedule_Name: str
    Heating_High_Control_Temperature_Schedule_Name: str
    Heating_Low_Control_Temperature_Schedule_Name: str
    Cooling_Water_Inlet_Node_Name: str
    Cooling_Water_Outlet_Node_Name: str
    Cooling_High_Water_Temperature_Schedule_Name: str
    Cooling_Low_Water_Temperature_Schedule_Name: str
    Cooling_High_Control_Temperature_Schedule_Name: str
    Cooling_Low_Control_Temperature_Schedule_Name: str
    Number_of_Circuits: str
    Circuit_Length: str

class ZonehvacLowtemperatureradiantConstantflowDesignType(TypedDict, total=False):
    """"dict for ZonehvacLowtemperatureradiantConstantflowDesign"""
    Name: str
    Fluid_to_Radiant_Surface_Heat_Transfer_Model: str
    Hydronic_Tubing_Inside_Diameter: str
    Hydronic_Tubing_Outside_Diameter: str
    Hydronic_Tubing_Conductivity: str
    Temperature_Control_Type: str
    Running_Mean_Outdoor_DryBulb_Temperature_Weighting_Factor: str
    Motor_Efficiency: str
    Fraction_of_Motor_Inefficiencies_to_Fluid_Stream: str
    Condensation_Control_Type: str
    Condensation_Control_Dewpoint_Offset: str
    Changeover_Delay_Time_Period_Schedule: str

class ZonehvacLowtemperatureradiantElectricType(TypedDict, total=False):
    """"dict for ZonehvacLowtemperatureradiantElectric"""
    Name: str
    Availability_Schedule_Name: str
    Zone_Name: str
    Surface_Name_or_Radiant_Surface_Group_Name: str
    Heating_Design_Capacity_Method: str
    Heating_Design_Capacity: str
    Heating_Design_Capacity_Per_Floor_Area: str
    Fraction_of_Autosized_Heating_Design_Capacity: str
    Temperature_Control_Type: str
    Setpoint_Control_Type: str
    Heating_Throttling_Range: str
    Heating_Setpoint_Temperature_Schedule_Name: str

class ZonehvacLowtemperatureradiantSurfacegroupType(TypedDict, total=False):
    """"dict for ZonehvacLowtemperatureradiantSurfacegroup"""
    Name: str
    Surface_1_Name: str
    Flow_Fraction_for_Surface_1: str
    Surface_2_Name: str
    Flow_Fraction_for_Surface_2: str
    Surface_3_Name: str
    Flow_Fraction_for_Surface_3: str
    Surface_4_Name: str
    Flow_Fraction_for_Surface_4: str
    Surface_5_Name: str
    Flow_Fraction_for_Surface_5: str
    Surface_6_Name: str
    Flow_Fraction_for_Surface_6: str
    Surface_7_Name: str
    Flow_Fraction_for_Surface_7: str
    Surface_8_Name: str
    Flow_Fraction_for_Surface_8: str
    Surface_9_Name: str
    Flow_Fraction_for_Surface_9: str
    Surface_10_Name: str
    Flow_Fraction_for_Surface_10: str
    Surface_11_Name: str
    Flow_Fraction_for_Surface_11: str
    Surface_12_Name: str
    Flow_Fraction_for_Surface_12: str
    Surface_13_Name: str
    Flow_Fraction_for_Surface_13: str
    Surface_14_Name: str
    Flow_Fraction_for_Surface_14: str
    Surface_15_Name: str
    Flow_Fraction_for_Surface_15: str
    Surface_16_Name: str
    Flow_Fraction_for_Surface_16: str
    Surface_17_Name: str
    Flow_Fraction_for_Surface_17: str
    Surface_18_Name: str
    Flow_Fraction_for_Surface_18: str
    Surface_19_Name: str
    Flow_Fraction_for_Surface_19: str
    Surface_20_Name: str
    Flow_Fraction_for_Surface_20: str
    Surface_21_Name: str
    Flow_Fraction_for_Surface_21: str
    Surface_22_Name: str
    Flow_Fraction_for_Surface_22: str
    Surface_23_Name: str
    Flow_Fraction_for_Surface_23: str
    Surface_24_Name: str
    Flow_Fraction_for_Surface_24: str
    Surface_25_Name: str
    Flow_Fraction_for_Surface_25: str
    Surface_26_Name: str
    Flow_Fraction_for_Surface_26: str
    Surface_27_Name: str
    Flow_Fraction_for_Surface_27: str
    Surface_28_Name: str
    Flow_Fraction_for_Surface_28: str
    Surface_29_Name: str
    Flow_Fraction_for_Surface_29: str
    Surface_30_Name: str
    Flow_Fraction_for_Surface_30: str
    Surface_31_Name: str
    Flow_Fraction_for_Surface_31: str
    Surface_32_Name: str
    Flow_Fraction_for_Surface_32: str
    Surface_33_Name: str
    Flow_Fraction_for_Surface_33: str
    Surface_34_Name: str
    Flow_Fraction_for_Surface_34: str
    Surface_35_Name: str
    Flow_Fraction_for_Surface_35: str
    Surface_36_Name: str
    Flow_Fraction_for_Surface_36: str
    Surface_37_Name: str
    Flow_Fraction_for_Surface_37: str
    Surface_38_Name: str
    Flow_Fraction_for_Surface_38: str
    Surface_39_Name: str
    Flow_Fraction_for_Surface_39: str
    Surface_40_Name: str
    Flow_Fraction_for_Surface_40: str
    Surface_41_Name: str
    Flow_Fraction_for_Surface_41: str
    Surface_42_Name: str
    Flow_Fraction_for_Surface_42: str
    Surface_43_Name: str
    Flow_Fraction_for_Surface_43: str
    Surface_44_Name: str
    Flow_Fraction_for_Surface_44: str
    Surface_45_Name: str
    Flow_Fraction_for_Surface_45: str
    Surface_46_Name: str
    Flow_Fraction_for_Surface_46: str
    Surface_47_Name: str
    Flow_Fraction_for_Surface_47: str
    Surface_48_Name: str
    Flow_Fraction_for_Surface_48: str
    Surface_49_Name: str
    Flow_Fraction_for_Surface_49: str

class ZonehvacLowtemperatureradiantVariableflowType(TypedDict, total=False):
    """"dict for ZonehvacLowtemperatureradiantVariableflow"""
    Name: str
    Design_Object: str
    Availability_Schedule_Name: str
    Zone_Name: str
    Surface_Name_or_Radiant_Surface_Group_Name: str
    Hydronic_Tubing_Length: str
    Heating_Design_Capacity: str
    Maximum_Hot_Water_Flow: str
    Heating_Water_Inlet_Node_Name: str
    Heating_Water_Outlet_Node_Name: str
    Cooling_Design_Capacity: str
    Maximum_Cold_Water_Flow: str
    Cooling_Water_Inlet_Node_Name: str
    Cooling_Water_Outlet_Node_Name: str
    Number_of_Circuits: str
    Circuit_Length: str

class ZonehvacLowtemperatureradiantVariableflowDesignType(TypedDict, total=False):
    """"dict for ZonehvacLowtemperatureradiantVariableflowDesign"""
    Name: str
    Fluid_to_Radiant_Surface_Heat_Transfer_Model: str
    Hydronic_Tubing_Inside_Diameter: str
    Hydronic_Tubing_Outside_Diameter: str
    Hydronic_Tubing_Conductivity: str
    Temperature_Control_Type: str
    Setpoint_Control_Type: str
    Heating_Design_Capacity_Method: str
    Heating_Design_Capacity_Per_Floor_Area: str
    Fraction_of_Autosized_Heating_Design_Capacity: str
    Heating_Control_Throttling_Range: str
    Heating_Control_Temperature_Schedule_Name: str
    Cooling_Design_Capacity_Method: str
    Cooling_Design_Capacity_Per_Floor_Area: str
    Fraction_of_Autosized_Cooling_Design_Capacity: str
    Cooling_Control_Throttling_Range: str
    Cooling_Control_Temperature_Schedule_Name: str
    Condensation_Control_Type: str
    Condensation_Control_Dewpoint_Offset: str
    Changeover_Delay_Time_Period_Schedule: str

class ZonehvacOutdoorairunitType(TypedDict, total=False):
    """"dict for ZonehvacOutdoorairunit"""
    Name: str
    Availability_Schedule_Name: str
    Zone_Name: str
    Outdoor_Air_Flow_Rate: str
    Outdoor_Air_Schedule_Name: str
    Supply_Fan_Name: str
    Supply_Fan_Placement: str
    Exhaust_Fan_Name: str
    Exhaust_Air_Flow_Rate: str
    Exhaust_Air_Schedule_Name: str
    Unit_Control_Type: str
    High_Air_Control_Temperature_Schedule_Name: str
    Low_Air_Control_Temperature_Schedule_Name: str
    Outdoor_Air_Node_Name: str
    AirOutlet_Node_Name: str
    AirInlet_Node_Name: str
    Supply_FanOutlet_Node_Name: str
    Outdoor_Air_Unit_List_Name: str
    Availability_Manager_List_Name: str

class ZonehvacOutdoorairunitEquipmentlistType(TypedDict, total=False):
    """"dict for ZonehvacOutdoorairunitEquipmentlist"""
    Name: str
    Component_1_Object_Type: str
    Component_1_Name: str
    Component_2_Object_Type: str
    Component_2_Name: str
    Component_3_Object_Type: str
    Component_3_Name: str
    Component_4_Object_Type: str
    Component_4_Name: str
    Component_5_Object_Type: str
    Component_5_Name: str
    Component_6_Object_Type: str
    Component_6_Name: str
    Component_7_Object_Type: str
    Component_7_Name: str
    Component_8_Object_Type: str
    Component_8_Name: str

class ZonehvacPackagedterminalairconditionerType(TypedDict, total=False):
    """"dict for ZonehvacPackagedterminalairconditioner"""
    Name: str
    Availability_Schedule_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Outdoor_Air_Mixer_Object_Type: str
    Outdoor_Air_Mixer_Name: str
    Cooling_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate: str
    No_Load_Supply_Air_Flow_Rate: str
    No_Load_Supply_Air_Flow_Rate_Control_Set_To_Low_Speed: str
    Cooling_Outdoor_Air_Flow_Rate: str
    Heating_Outdoor_Air_Flow_Rate: str
    No_Load_Outdoor_Air_Flow_Rate: str
    Supply_Air_Fan_Object_Type: str
    Supply_Air_Fan_Name: str
    Heating_Coil_Object_Type: str
    Heating_Coil_Name: str
    Cooling_Coil_Object_Type: str
    Cooling_Coil_Name: str
    Fan_Placement: str
    Supply_Air_Fan_Operating_Mode_Schedule_Name: str
    Availability_Manager_List_Name: str
    Design_Specification_ZoneHVAC_Sizing_Object_Name: str
    Capacity_Control_Method: str
    Minimum_Supply_Air_Temperature_in_Cooling_Mode: str
    Maximum_Supply_Air_Temperature_in_Heating_Mode: str

class ZonehvacPackagedterminalheatpumpType(TypedDict, total=False):
    """"dict for ZonehvacPackagedterminalheatpump"""
    Name: str
    Availability_Schedule_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Outdoor_Air_Mixer_Object_Type: str
    Outdoor_Air_Mixer_Name: str
    Cooling_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate: str
    No_Load_Supply_Air_Flow_Rate: str
    No_Load_Supply_Air_Flow_Rate_Control_Set_To_Low_Speed: str
    Cooling_Outdoor_Air_Flow_Rate: str
    Heating_Outdoor_Air_Flow_Rate: str
    No_Load_Outdoor_Air_Flow_Rate: str
    Supply_Air_Fan_Object_Type: str
    Supply_Air_Fan_Name: str
    Heating_Coil_Object_Type: str
    Heating_Coil_Name: str
    Heating_Convergence_Tolerance: str
    Cooling_Coil_Object_Type: str
    Cooling_Coil_Name: str
    Cooling_Convergence_Tolerance: str
    Supplemental_Heating_Coil_Object_Type: str
    Supplemental_Heating_Coil_Name: str
    Maximum_Supply_Air_Temperature_from_Supplemental_Heater: str
    Maximum_Outdoor_DryBulb_Temperature_for_Supplemental_Heater_Operation: str
    Fan_Placement: str
    Supply_Air_Fan_Operating_Mode_Schedule_Name: str
    Availability_Manager_List_Name: str
    Design_Specification_ZoneHVAC_Sizing_Object_Name: str
    Capacity_Control_Method: str
    Minimum_Supply_Air_Temperature_in_Cooling_Mode: str
    Maximum_Supply_Air_Temperature_in_Heating_Mode: str

class ZonehvacRefrigerationchillersetType(TypedDict, total=False):
    """"dict for ZonehvacRefrigerationchillerset"""
    Name: str
    Availability_Schedule_Name: str
    Zone_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Air_Chiller_1_Name: str
    Air_Chiller_2_Name: str
    Air_Chiller_3_Name: str
    Air_Chiller_4_Name: str
    Air_Chiller_5_Name: str
    Air_Chiller_6_Name: str
    Air_Chiller_7_Name: str
    Air_Chiller_8_Name: str
    Air_Chiller_9_Name: str
    Air_Chiller_10_Name: str
    Air_Chiller_11_Name: str
    Air_Chiller_12_Name: str
    Air_Chiller_13_Name: str
    Air_Chiller_14_Name: str
    Air_Chiller_15_Name: str
    Air_Chiller_16_Name: str
    Air_Chiller_17_Name: str
    Air_Chiller_18_Name: str
    Air_Chiller_19_Name: str
    Air_Chiller_20_Name: str
    Air_Chiller_21_Name: str
    Air_Chiller_22_Name: str
    Air_Chiller_23_Name: str
    Air_Chiller_24_Name: str
    Air_Chiller_25_Name: str
    Air_Chiller_26_Name: str
    Air_Chiller_27_Name: str
    Air_Chiller_28_Name: str
    Air_Chiller_29_Name: str
    Air_Chiller_30_Name: str
    Air_Chiller_31_Name: str
    Air_Chiller_32_Name: str
    Air_Chiller_33_Name: str
    Air_Chiller_34_Name: str
    Air_Chiller_35_Name: str
    Air_Chiller_36_Name: str
    Air_Chiller_37_Name: str
    Air_Chiller_38_Name: str
    Air_Chiller_39_Name: str
    Air_Chiller_40_Name: str
    Air_Chiller_41_Name: str
    Air_Chiller_42_Name: str
    Air_Chiller_43_Name: str
    Air_Chiller_44_Name: str
    Air_Chiller_45_Name: str
    Air_Chiller_46_Name: str
    Air_Chiller_47_Name: str
    Air_Chiller_48_Name: str
    Air_Chiller_49_Name: str

class ZonehvacTerminalunitVariablerefrigerantflowType(TypedDict, total=False):
    """"dict for ZonehvacTerminalunitVariablerefrigerantflow"""
    Zone_Terminal_Unit_Name: str
    Terminal_Unit_Availability_Schedule: str
    Terminal_Unit_Air_Inlet_Node_Name: str
    Terminal_Unit_Air_Outlet_Node_Name: str
    Cooling_Supply_Air_Flow_Rate: str
    No_Cooling_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate: str
    No_Heating_Supply_Air_Flow_Rate: str
    Cooling_Outdoor_Air_Flow_Rate: str
    Heating_Outdoor_Air_Flow_Rate: str
    No_Load_Outdoor_Air_Flow_Rate: str
    Supply_Air_Fan_Operating_Mode_Schedule_Name: str
    Supply_Air_Fan_Placement: str
    Supply_Air_Fan_Object_Type: str
    Supply_Air_Fan_Object_Name: str
    Outside_Air_Mixer_Object_Type: str
    Outside_Air_Mixer_Object_Name: str
    Cooling_Coil_Object_Type: str
    Cooling_Coil_Object_Name: str
    Heating_Coil_Object_Type: str
    Heating_Coil_Object_Name: str
    Zone_Terminal_Unit_On_Parasitic_Electric_Energy_Use: str
    Zone_Terminal_Unit_Off_Parasitic_Electric_Energy_Use: str
    Rated_Heating_Capacity_Sizing_Ratio: str
    Availability_Manager_List_Name: str
    Design_Specification_ZoneHVAC_Sizing_Object_Name: str
    Supplemental_Heating_Coil_Object_Type: str
    Supplemental_Heating_Coil_Name: str
    Maximum_Supply_Air_Temperature_from_Supplemental_Heater: str
    Maximum_Outdoor_DryBulb_Temperature_for_Supplemental_Heater_Operation: str
    Controlling_Zone_or_Thermostat_Location: str
    Design_Specification_Multispeed_Object_Type: str
    Design_Specification_Multispeed_Object_Name: str

class ZonehvacUnitheaterType(TypedDict, total=False):
    """"dict for ZonehvacUnitheater"""
    Name: str
    Availability_Schedule_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Supply_Air_Fan_Object_Type: str
    Supply_Air_Fan_Name: str
    Maximum_Supply_Air_Flow_Rate: str
    Heating_Coil_Object_Type: str
    Heating_Coil_Name: str
    Supply_Air_Fan_Operating_Mode_Schedule_Name: str
    Supply_Air_Fan_Operation_During_No_Heating: str
    Maximum_Hot_Water_or_Steam_Flow_Rate: str
    Minimum_Hot_Water_or_Steam_Flow_Rate: str
    Heating_Convergence_Tolerance: str
    Availability_Manager_List_Name: str
    Design_Specification_ZoneHVAC_Sizing_Object_Name: str

class ZonehvacUnitventilatorType(TypedDict, total=False):
    """"dict for ZonehvacUnitventilator"""
    Name: str
    Availability_Schedule_Name: str
    Maximum_Supply_Air_Flow_Rate: str
    Outdoor_Air_Control_Type: str
    Minimum_Outdoor_Air_Flow_Rate: str
    Minimum_Outdoor_Air_Schedule_Name: str
    Maximum_Outdoor_Air_Flow_Rate: str
    Maximum_Outdoor_Air_Fraction_or_Temperature_Schedule_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Outdoor_Air_Node_Name: str
    Exhaust_Air_Node_Name: str
    Mixed_Air_Node_Name: str
    Supply_Air_Fan_Object_Type: str
    Supply_Air_Fan_Name: str
    Coil_Option: str
    Supply_Air_Fan_Operating_Mode_Schedule_Name: str
    Heating_Coil_Object_Type: str
    Heating_Coil_Name: str
    Heating_Convergence_Tolerance: str
    Cooling_Coil_Object_Type: str
    Cooling_Coil_Name: str
    Cooling_Convergence_Tolerance: str
    Availability_Manager_List_Name: str
    Design_Specification_ZoneHVAC_Sizing_Object_Name: str

class ZonehvacVentilatedslabType(TypedDict, total=False):
    """"dict for ZonehvacVentilatedslab"""
    Name: str
    Availability_Schedule_Name: str
    Zone_Name: str
    Surface_Name_or_Radiant_Surface_Group_Name: str
    Maximum_Air_Flow_Rate: str
    Outdoor_Air_Control_Type: str
    Minimum_Outdoor_Air_Flow_Rate: str
    Minimum_Outdoor_Air_Schedule_Name: str
    Maximum_Outdoor_Air_Flow_Rate: str
    Maximum_Outdoor_Air_Fraction_or_Temperature_Schedule_Name: str
    System_Configuration_Type: str
    Hollow_Core_Inside_Diameter: str
    Hollow_Core_Length: str
    Number_of_Cores: str
    Temperature_Control_Type: str
    Heating_High_Air_Temperature_Schedule_Name: str
    Heating_Low_Air_Temperature_Schedule_Name: str
    Heating_High_Control_Temperature_Schedule_Name: str
    Heating_Low_Control_Temperature_Schedule_Name: str
    Cooling_High_Air_Temperature_Schedule_Name: str
    Cooling_Low_Air_Temperature_Schedule_Name: str
    Cooling_High_Control_Temperature_Schedule_Name: str
    Cooling_Low_Control_Temperature_Schedule_Name: str
    Return_Air_Node_Name: str
    Slab_In_Node_Name: str
    Zone_Supply_Air_Node_Name: str
    Outdoor_Air_Node_Name: str
    Relief_Air_Node_Name: str
    Outdoor_Air_Mixer_Outlet_Node_Name: str
    Fan_Outlet_Node_Name: str
    Fan_Name: str
    Coil_Option_Type: str
    Heating_Coil_Object_Type: str
    Heating_Coil_Name: str
    Hot_Water_or_Steam_Inlet_Node_Name: str
    Cooling_Coil_Object_Type: str
    Cooling_Coil_Name: str
    Cold_Water_Inlet_Node_Name: str
    Availability_Manager_List_Name: str
    Design_Specification_ZoneHVAC_Sizing_Object_Name: str

class ZonehvacVentilatedslabSlabgroupType(TypedDict, total=False):
    """"dict for ZonehvacVentilatedslabSlabgroup"""
    Name: str
    Zone_1_Name: str
    Surface_1_Name: str
    Core_Diameter_for_Surface_1: str
    Core_Length_for_Surface_1: str
    Core_Numbers_for_Surface_1: str
    Slab_Inlet_Node_Name_for_Surface_1: str
    Slab_Outlet_Node_Name_for_Surface_1: str
    Zone_2_Name: str
    Surface_2_Name: str
    Core_Diameter_for_Surface_2: str
    Core_Length_for_Surface_2: str
    Core_Numbers_for_Surface_2: str
    Slab_Inlet_Node_Name_for_Surface_2: str
    Slab_Outlet_Node_Name_for_Surface_2: str
    Zone_3_Name: str
    Surface_3_Name: str
    Core_Diameter_for_Surface_3: str
    Core_Length_for_Surface_3: str
    Core_Numbers_for_Surface_3: str
    Slab_Inlet_Node_Name_for_Surface_3: str
    Slab_Outlet_Node_Name_for_Surface_3: str
    Zone_4_Name: str
    Surface_4_Name: str
    Core_Diameter_for_Surface_4: str
    Core_Length_for_Surface_4: str
    Core_Numbers_for_Surface_4: str
    Slab_Inlet_Node_Name_for_Surface_4: str
    Slab_Outlet_Node_Name_for_Surface_4: str
    Zone_5_Name: str
    Surface_5_Name: str
    Core_Diameter_for_Surface_5: str
    Core_Length_for_Surface_5: str
    Core_Numbers_for_Surface_5: str
    Slab_Inlet_Node_Name_for_Surface_5: str
    Slab_Outlet_Node_Name_for_Surface_5: str
    Zone_6_Name: str
    Surface_6_Name: str
    Core_Diameter_for_Surface_6: str
    Core_Length_for_Surface_6: str
    Core_Numbers_for_Surface_6: str
    Slab_Inlet_Node_Name_for_Surface_6: str
    Slab_Outlet_Node_Name_for_Surface_6: str
    Zone_7_Name: str
    Surface_7_Name: str
    Core_Diameter_for_Surface_7: str
    Core_Length_for_Surface_7: str
    Core_Numbers_for_Surface_7: str
    Slab_Inlet_Node_Name_for_Surface_7: str
    Slab_Outlet_Node_Name_for_Surface_7: str
    Zone_8_Name: str
    Surface_8_Name: str
    Core_Diameter_for_Surface_8: str
    Core_Length_for_Surface_8: str
    Core_Numbers_for_Surface_8: str
    Slab_Inlet_Node_Name_for_Surface_8: str
    Slab_Outlet_Node_Name_for_Surface_8: str
    Zone_9_Name: str
    Surface_9_Name: str
    Core_Diameter_for_Surface_9: str
    Core_Length_for_Surface_9: str
    Core_Numbers_for_Surface_9: str
    Slab_Inlet_Node_Name_for_Surface_9: str
    Slab_Outlet_Node_Name_for_Surface_9: str
    Zone_10_Name: str
    Surface_10_Name: str
    Core_Diameter_for_Surface_10: str
    Core_Length_for_Surface_10: str
    Core_Numbers_for_Surface_10: str
    Slab_Inlet_Node_Name_for_Surface_10: str
    Slab_Outlet_Node_Name_for_Surface_10: str

class ZonehvacWatertoairheatpumpType(TypedDict, total=False):
    """"dict for ZonehvacWatertoairheatpump"""
    Name: str
    Availability_Schedule_Name: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Outdoor_Air_Mixer_Object_Type: str
    Outdoor_Air_Mixer_Name: str
    Cooling_Supply_Air_Flow_Rate: str
    Heating_Supply_Air_Flow_Rate: str
    No_Load_Supply_Air_Flow_Rate: str
    No_Load_Supply_Air_Flow_Rate_Control_Set_To_Low_Speed: str
    Cooling_Outdoor_Air_Flow_Rate: str
    Heating_Outdoor_Air_Flow_Rate: str
    No_Load_Outdoor_Air_Flow_Rate: str
    Supply_Air_Fan_Object_Type: str
    Supply_Air_Fan_Name: str
    Heating_Coil_Object_Type: str
    Heating_Coil_Name: str
    Cooling_Coil_Object_Type: str
    Cooling_Coil_Name: str
    Supplemental_Heating_Coil_Object_Type: str
    Supplemental_Heating_Coil_Name: str
    Maximum_Supply_Air_Temperature_from_Supplemental_Heater: str
    Maximum_Outdoor_DryBulb_Temperature_for_Supplemental_Heater_Operation: str
    Outdoor_DryBulb_Temperature_Sensor_Node_Name: str
    Fan_Placement: str
    Supply_Air_Fan_Operating_Mode_Schedule_Name: str
    Availability_Manager_List_Name: str
    Heat_Pump_Coil_Water_Flow_Mode: str
    Design_Specification_ZoneHVAC_Sizing_Object_Name: str
    Design_Specification_Multispeed_Object_Type: str
    Design_Specification_Multispeed_Object_Name: str

class ZonehvacWindowairconditionerType(TypedDict, total=False):
    """"dict for ZonehvacWindowairconditioner"""
    Name: str
    Availability_Schedule_Name: str
    Maximum_Supply_Air_Flow_Rate: str
    Maximum_Outdoor_Air_Flow_Rate: str
    Air_Inlet_Node_Name: str
    Air_Outlet_Node_Name: str
    Outdoor_Air_Mixer_Object_Type: str
    Outdoor_Air_Mixer_Name: str
    Supply_Air_Fan_Object_Type: str
    Supply_Air_Fan_Name: str
    Cooling_Coil_Object_Type: str
    DX_Cooling_Coil_Name: str
    Supply_Air_Fan_Operating_Mode_Schedule_Name: str
    Fan_Placement: str
    Cooling_Convergence_Tolerance: str
    Availability_Manager_List_Name: str
    Design_Specification_ZoneHVAC_Sizing_Object_Name: str

class ZoneinfiltrationDesignflowrateType(TypedDict, total=False):
    """"dict for ZoneinfiltrationDesignflowrate"""
    Name: str
    Zone_or_ZoneList_or_Space_or_SpaceList_Name: str
    Schedule_Name: str
    Design_Flow_Rate_Calculation_Method: str
    Design_Flow_Rate: str
    Flow_Rate_per_Floor_Area: str
    Flow_Rate_per_Exterior_Surface_Area: str
    Air_Changes_per_Hour: str
    Constant_Term_Coefficient: str
    Temperature_Term_Coefficient: str
    Velocity_Term_Coefficient: str
    Velocity_Squared_Term_Coefficient: str

class ZoneinfiltrationEffectiveleakageareaType(TypedDict, total=False):
    """"dict for ZoneinfiltrationEffectiveleakagearea"""
    Name: str
    Zone_or_Space_Name: str
    Schedule_Name: str
    Effective_Air_Leakage_Area: str
    Stack_Coefficient: str
    Wind_Coefficient: str

class ZoneinfiltrationFlowcoefficientType(TypedDict, total=False):
    """"dict for ZoneinfiltrationFlowcoefficient"""
    Name: str
    Zone_or_Space_Name: str
    Schedule_Name: str
    Flow_Coefficient: str
    Stack_Coefficient: str
    Pressure_Exponent: str
    Wind_Coefficient: str
    Shelter_Factor: str

class ZonelistType(TypedDict, total=False):
    """"dict for Zonelist"""
    Name: str
    Zone_1_Name: str
    Zone_2_Name: str
    Zone_3_Name: str
    Zone_4_Name: str
    Zone_5_Name: str
    Zone_6_Name: str
    Zone_7_Name: str
    Zone_8_Name: str
    Zone_9_Name: str
    Zone_10_Name: str
    Zone_11_Name: str
    Zone_12_Name: str
    Zone_13_Name: str
    Zone_14_Name: str
    Zone_15_Name: str
    Zone_16_Name: str
    Zone_17_Name: str
    Zone_18_Name: str
    Zone_19_Name: str
    Zone_20_Name: str
    Zone_21_Name: str
    Zone_22_Name: str
    Zone_23_Name: str
    Zone_24_Name: str
    Zone_25_Name: str
    Zone_26_Name: str
    Zone_27_Name: str
    Zone_28_Name: str
    Zone_29_Name: str
    Zone_30_Name: str
    Zone_31_Name: str
    Zone_32_Name: str
    Zone_33_Name: str
    Zone_34_Name: str
    Zone_35_Name: str
    Zone_36_Name: str
    Zone_37_Name: str
    Zone_38_Name: str
    Zone_39_Name: str
    Zone_40_Name: str
    Zone_41_Name: str
    Zone_42_Name: str
    Zone_43_Name: str
    Zone_44_Name: str
    Zone_45_Name: str
    Zone_46_Name: str
    Zone_47_Name: str
    Zone_48_Name: str
    Zone_49_Name: str

class ZonemixingType(TypedDict, total=False):
    """"dict for Zonemixing"""
    Name: str
    Zone_or_Space_Name: str
    Schedule_Name: str
    Design_Flow_Rate_Calculation_Method: str
    Design_Flow_Rate: str
    Flow_Rate_per_Floor_Area: str
    Flow_Rate_per_Person: str
    Air_Changes_per_Hour: str
    Source_Zone_or_Space_Name: str
    Delta_Temperature: str
    Delta_Temperature_Schedule_Name: str
    Minimum_Receiving_Temperature_Schedule_Name: str
    Maximum_Receiving_Temperature_Schedule_Name: str
    Minimum_Source_Temperature_Schedule_Name: str
    Maximum_Source_Temperature_Schedule_Name: str
    Minimum_Outdoor_Temperature_Schedule_Name: str
    Maximum_Outdoor_Temperature_Schedule_Name: str

class ZonepropertyLocalenvironmentType(TypedDict, total=False):
    """"dict for ZonepropertyLocalenvironment"""
    Name: str
    Zone_Name: str
    Outdoor_Air_Node_Name: str

class ZonepropertyUserviewfactorsBysurfacenameType(TypedDict, total=False):
    """"dict for ZonepropertyUserviewfactorsBysurfacename"""
    Zone_or_ZoneList_or_Space_or_SpaceList_Name: str
    From_Surface_1: str
    To_Surface_1: str
    View_Factor_1: str
    From_Surface_2: str
    To_Surface_2: str
    View_Factor_2: str
    From_Surface_3: str
    To_Surface_3: str
    View_Factor_3: str
    From_Surface_4: str
    To_Surface_4: str
    View_Factor_4: str
    From_Surface_5: str
    To_Surface_5: str
    View_Factor_5: str
    From_Surface_6: str
    To_Surface_6: str
    View_Factor_6: str
    From_Surface_7: str
    To_Surface_7: str
    View_Factor_7: str
    From_Surface_8: str
    To_Surface_8: str
    View_Factor_8: str
    From_Surface_9: str
    To_Surface_9: str
    View_Factor_9: str
    From_Surface_10: str
    To_Surface_10: str
    View_Factor_10: str
    From_Surface_11: str
    To_Surface_11: str
    View_Factor_11: str
    From_Surface_12: str
    To_Surface_12: str
    View_Factor_12: str
    From_Surface_13: str
    To_Surface_13: str
    View_Factor_13: str
    From_Surface_14: str
    To_Surface_14: str
    View_Factor_14: str
    From_Surface_15: str
    To_Surface_15: str
    View_Factor_15: str
    From_Surface_16: str
    To_Surface_16: str
    View_Factor_16: str
    From_Surface_17: str
    To_Surface_17: str
    View_Factor_17: str
    From_Surface_18: str
    To_Surface_18: str
    View_Factor_18: str
    From_Surface_19: str
    To_Surface_19: str
    View_Factor_19: str
    From_Surface_20: str
    To_Surface_20: str
    View_Factor_20: str
    From_Surface_21: str
    To_Surface_21: str
    View_Factor_21: str
    From_Surface_22: str
    To_Surface_22: str
    View_Factor_22: str
    From_Surface_23: str
    To_Surface_23: str
    View_Factor_23: str
    From_Surface_24: str
    To_Surface_24: str
    View_Factor_24: str
    From_Surface_25: str
    To_Surface_25: str
    View_Factor_25: str
    From_Surface_26: str
    To_Surface_26: str
    View_Factor_26: str
    From_Surface_27: str
    To_Surface_27: str
    View_Factor_27: str
    From_Surface_28: str
    To_Surface_28: str
    View_Factor_28: str
    From_Surface_29: str
    To_Surface_29: str
    View_Factor_29: str
    From_Surface_30: str
    To_Surface_30: str
    View_Factor_30: str
    From_Surface_31: str
    To_Surface_31: str
    View_Factor_31: str
    From_Surface_32: str
    To_Surface_32: str
    View_Factor_32: str
    From_Surface_33: str
    To_Surface_33: str
    View_Factor_33: str
    From_Surface_34: str
    To_Surface_34: str
    View_Factor_34: str
    From_Surface_35: str
    To_Surface_35: str
    View_Factor_35: str
    From_Surface_36: str
    To_Surface_36: str
    View_Factor_36: str
    From_Surface_37: str
    To_Surface_37: str
    View_Factor_37: str
    From_Surface_38: str
    To_Surface_38: str
    View_Factor_38: str
    From_Surface_39: str
    To_Surface_39: str
    View_Factor_39: str
    From_Surface_40: str
    To_Surface_40: str
    View_Factor_40: str
    From_Surface_41: str
    To_Surface_41: str
    View_Factor_41: str
    From_Surface_42: str
    To_Surface_42: str
    View_Factor_42: str
    From_Surface_43: str
    To_Surface_43: str
    View_Factor_43: str
    From_Surface_44: str
    To_Surface_44: str
    View_Factor_44: str
    From_Surface_45: str
    To_Surface_45: str
    View_Factor_45: str
    From_Surface_46: str
    To_Surface_46: str
    View_Factor_46: str
    From_Surface_47: str
    To_Surface_47: str
    View_Factor_47: str
    From_Surface_48: str
    To_Surface_48: str
    View_Factor_48: str
    From_Surface_49: str
    To_Surface_49: str
    View_Factor_49: str

class ZonerefrigerationdoormixingType(TypedDict, total=False):
    """"dict for Zonerefrigerationdoormixing"""
    Name: str
    Zone_1_Name: str
    Zone_2_Name: str
    Schedule_Name: str
    Door_Height: str
    Door_Area: str
    Door_Protection_Type: str

class ZoneterminalunitlistType(TypedDict, total=False):
    """"dict for Zoneterminalunitlist"""
    Zone_Terminal_Unit_List_Name: str
    Zone_Terminal_Unit_Name_1: str
    Zone_Terminal_Unit_Name_2: str
    Zone_Terminal_Unit_Name_3: str
    Zone_Terminal_Unit_Name_4: str
    Zone_Terminal_Unit_Name_5: str
    Zone_Terminal_Unit_Name_6: str
    Zone_Terminal_Unit_Name_7: str
    Zone_Terminal_Unit_Name_8: str
    Zone_Terminal_Unit_Name_9: str
    Zone_Terminal_Unit_Name_10: str
    Zone_Terminal_Unit_Name_11: str
    Zone_Terminal_Unit_Name_12: str
    Zone_Terminal_Unit_Name_13: str
    Zone_Terminal_Unit_Name_14: str
    Zone_Terminal_Unit_Name_15: str
    Zone_Terminal_Unit_Name_16: str
    Zone_Terminal_Unit_Name_17: str
    Zone_Terminal_Unit_Name_18: str
    Zone_Terminal_Unit_Name_19: str
    Zone_Terminal_Unit_Name_20: str

class ZonethermalchimneyType(TypedDict, total=False):
    """"dict for Zonethermalchimney"""
    Name: str
    Zone_Name: str
    Availability_Schedule_Name: str
    Width_of_the_Absorber_Wall: str
    Cross_Sectional_Area_of_Air_Channel_Outlet: str
    Discharge_Coefficient: str
    Zone_1_Name: str
    Distance_from_Top_of_Thermal_Chimney_to_Inlet_1: str
    Relative_Ratios_of_Air_Flow_Rates_Passing_through_Zone_1: str
    Cross_Sectional_Areas_of_Air_Channel_Inlet_1: str
    Zone_2_Name: str
    Distance_from_Top_of_Thermal_Chimney_to_Inlet_2: str
    Relative_Ratios_of_Air_Flow_Rates_Passing_through_Zone_2: str
    Cross_Sectional_Areas_of_Air_Channel_Inlet_2: str
    Zone_3_Name: str
    Distance_from_Top_of_Thermal_Chimney_to_Inlet_3: str
    Relative_Ratios_of_Air_Flow_Rates_Passing_through_Zone_3: str
    Cross_Sectional_Areas_of_Air_Channel_Inlet_3: str
    Zone_4_Name: str
    Distance_from_Top_of_Thermal_Chimney_to_Inlet_4: str
    Relative_Ratios_of_Air_Flow_Rates_Passing_through_Zone_4: str
    Cross_Sectional_Areas_of_Air_Channel_Inlet_4: str
    Zone_5_Name: str
    Distance_from_Top_of_Thermal_Chimney_to_Inlet_5: str
    Relative_Ratios_of_Air_Flow_Rates_Passing_through_Zone_5: str
    Cross_Sectional_Areas_of_Air_Channel_Inlet_5: str
    Zone_6_Name: str
    Distance_from_Top_of_Thermal_Chimney_to_Inlet_6: str
    Relative_Ratios_of_Air_Flow_Rates_Passing_through_Zone_6: str
    Cross_Sectional_Areas_of_Air_Channel_Inlet_6: str
    Zone_7_Name: str
    Distance_from_Top_of_Thermal_Chimney_to_Inlet_7: str
    Relative_Ratios_of_Air_Flow_Rates_Passing_through_Zone_7: str
    Cross_Sectional_Areas_of_Air_Channel_Inlet_7: str
    Zone_8_Name: str
    Distance_from_Top_of_Thermal_Chimney_to_Inlet_8: str
    Relative_Ratios_of_Air_Flow_Rates_Passing_through_Zone_8: str
    Cross_Sectional_Areas_of_Air_Channel_Inlet_8: str
    Zone_9_Name: str
    Distance_from_Top_of_Thermal_Chimney_to_Inlet_9: str
    Relative_Ratios_of_Air_Flow_Rates_Passing_through_Zone_9: str
    Cross_Sectional_Areas_of_Air_Channel_Inlet_9: str
    Zone_10_Name: str
    Distance_from_Top_of_Thermal_Chimney_to_Inlet_10: str
    Relative_Ratios_of_Air_Flow_Rates_Passing_through_Zone_10: str
    Cross_Sectional_Areas_of_Air_Channel_Inlet_10: str
    Zone_11_Name: str
    Distance_from_Top_of_Thermal_Chimney_to_Inlet_11: str
    Relative_Ratios_of_Air_Flow_Rates_Passing_through_Zone_11: str
    Cross_Sectional_Areas_of_Air_Channel_Inlet_11: str
    Zone_12_Name: str
    Distance_from_Top_of_Thermal_Chimney_to_Inlet_12: str
    Relative_Ratios_of_Air_Flow_Rates_Passing_through_Zone_12: str
    Cross_Sectional_Areas_of_Air_Channel_Inlet_12: str
    Zone_13_Name: str
    Distance_from_Top_of_Thermal_Chimney_to_Inlet_13: str
    Relative_Ratios_of_Air_Flow_Rates_Passing_through_Zone_13: str
    Cross_Sectional_Areas_of_Air_Channel_Inlet_13: str
    Zone_14_Name: str
    Distance_from_Top_of_Thermal_Chimney_to_Inlet_14: str
    Relative_Ratios_of_Air_Flow_Rates_Passing_through_Zone_14: str
    Cross_Sectional_Areas_of_Air_Channel_Inlet_14: str
    Zone_15_Name: str
    Distance_from_Top_of_Thermal_Chimney_to_Inlet_15: str
    Relative_Ratios_of_Air_Flow_Rates_Passing_through_Zone_15: str
    Cross_Sectional_Areas_of_Air_Channel_Inlet_15: str
    Zone_16_Name: str
    Distance_from_Top_of_Thermal_Chimney_to_Inlet_16: str
    Relative_Ratios_of_Air_Flow_Rates_Passing_through_Zone_16: str
    Cross_Sectional_Areas_of_Air_Channel_Inlet_16: str
    Zone_17_Name: str
    Distance_from_Top_of_Thermal_Chimney_to_Inlet_17: str
    Relative_Ratios_of_Air_Flow_Rates_Passing_through_Zone_17: str
    Cross_Sectional_Areas_of_Air_Channel_Inlet_17: str
    Zone_18_Name: str
    Distance_from_Top_of_Thermal_Chimney_to_Inlet_18: str
    Relative_Ratios_of_Air_Flow_Rates_Passing_through_Zone_18: str
    Cross_Sectional_Areas_of_Air_Channel_Inlet_18: str
    Zone_19_Name: str
    Distance_from_Top_of_Thermal_Chimney_to_Inlet_19: str
    Relative_Ratios_of_Air_Flow_Rates_Passing_through_Zone_19: str
    Cross_Sectional_Areas_of_Air_Channel_Inlet_19: str
    Zone_20_Name: str
    Distance_from_Top_of_Thermal_Chimney_to_Inlet_20: str
    Relative_Ratios_of_Air_Flow_Rates_Passing_through_Zone_20: str
    Cross_Sectional_Areas_of_Air_Channel_Inlet_20: str

class ZoneventilationDesignflowrateType(TypedDict, total=False):
    """"dict for ZoneventilationDesignflowrate"""
    Name: str
    Zone_or_ZoneList_or_Space_or_SpaceList_Name: str
    Schedule_Name: str
    Design_Flow_Rate_Calculation_Method: str
    Design_Flow_Rate: str
    Flow_Rate_per_Floor_Area: str
    Flow_Rate_per_Person: str
    Air_Changes_per_Hour: str
    Ventilation_Type: str
    Fan_Pressure_Rise: str
    Fan_Total_Efficiency: str
    Constant_Term_Coefficient: str
    Temperature_Term_Coefficient: str
    Velocity_Term_Coefficient: str
    Velocity_Squared_Term_Coefficient: str
    Minimum_Indoor_Temperature: str
    Minimum_Indoor_Temperature_Schedule_Name: str
    Maximum_Indoor_Temperature: str
    Maximum_Indoor_Temperature_Schedule_Name: str
    Delta_Temperature: str
    Delta_Temperature_Schedule_Name: str
    Minimum_Outdoor_Temperature: str
    Minimum_Outdoor_Temperature_Schedule_Name: str
    Maximum_Outdoor_Temperature: str
    Maximum_Outdoor_Temperature_Schedule_Name: str
    Maximum_Wind_Speed: str

class ZoneventilationWindandstackopenareaType(TypedDict, total=False):
    """"dict for ZoneventilationWindandstackopenarea"""
    Name: str
    Zone_or_Space_Name: str
    Opening_Area: str
    Opening_Area_Fraction_Schedule_Name: str
    Opening_Effectiveness: str
    Effective_Angle: str
    Height_Difference: str
    Discharge_Coefficient_for_Opening: str
    Minimum_Indoor_Temperature: str
    Minimum_Indoor_Temperature_Schedule_Name: str
    Maximum_Indoor_Temperature: str
    Maximum_Indoor_Temperature_Schedule_Name: str
    Delta_Temperature: str
    Delta_Temperature_Schedule_Name: str
    Minimum_Outdoor_Temperature: str
    Minimum_Outdoor_Temperature_Schedule_Name: str
    Maximum_Outdoor_Temperature: str
    Maximum_Outdoor_Temperature_Schedule_Name: str
    Maximum_Wind_Speed: str
