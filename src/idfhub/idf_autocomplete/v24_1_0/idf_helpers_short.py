from __future__ import annotations
from .idf_types_short import *

def AirconditionerVariablerefrigerantflow(idf, **kwargs: Unpack[AirconditionerVariablerefrigerantflowType]):
    """"helper for AirconditionerVariablerefrigerantflow"""
    return idf.newidfobject('AIRCONDITIONER:VARIABLEREFRIGERANTFLOW', **kwargs)

def AirconditionerVariablerefrigerantflowFluidtemperaturecontrol(idf, **kwargs: Unpack[AirconditionerVariablerefrigerantflowFluidtemperaturecontrolType]):
    """"helper for AirconditionerVariablerefrigerantflowFluidtemperaturecontrol"""
    return idf.newidfobject('AIRCONDITIONER:VARIABLEREFRIGERANTFLOW:FLUIDTEMPERATURECONTROL', **kwargs)

def AirconditionerVariablerefrigerantflowFluidtemperaturecontrolHr(idf, **kwargs: Unpack[AirconditionerVariablerefrigerantflowFluidtemperaturecontrolHrType]):
    """"helper for AirconditionerVariablerefrigerantflowFluidtemperaturecontrolHr"""
    return idf.newidfobject('AIRCONDITIONER:VARIABLEREFRIGERANTFLOW:FLUIDTEMPERATURECONTROL:HR', **kwargs)

def AirflownetworkDistributionComponentCoil(idf, **kwargs: Unpack[AirflownetworkDistributionComponentCoilType]):
    """"helper for AirflownetworkDistributionComponentCoil"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:COIL', **kwargs)

def AirflownetworkDistributionComponentConstantpressuredrop(idf, **kwargs: Unpack[AirflownetworkDistributionComponentConstantpressuredropType]):
    """"helper for AirflownetworkDistributionComponentConstantpressuredrop"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:CONSTANTPRESSUREDROP', **kwargs)

def AirflownetworkDistributionComponentDuct(idf, **kwargs: Unpack[AirflownetworkDistributionComponentDuctType]):
    """"helper for AirflownetworkDistributionComponentDuct"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:DUCT', **kwargs)

def AirflownetworkDistributionComponentFan(idf, **kwargs: Unpack[AirflownetworkDistributionComponentFanType]):
    """"helper for AirflownetworkDistributionComponentFan"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:FAN', **kwargs)

def AirflownetworkDistributionComponentHeatexchanger(idf, **kwargs: Unpack[AirflownetworkDistributionComponentHeatexchangerType]):
    """"helper for AirflownetworkDistributionComponentHeatexchanger"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:HEATEXCHANGER', **kwargs)

def AirflownetworkDistributionComponentLeak(idf, **kwargs: Unpack[AirflownetworkDistributionComponentLeakType]):
    """"helper for AirflownetworkDistributionComponentLeak"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:LEAK', **kwargs)

def AirflownetworkDistributionComponentLeakageratio(idf, **kwargs: Unpack[AirflownetworkDistributionComponentLeakageratioType]):
    """"helper for AirflownetworkDistributionComponentLeakageratio"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:LEAKAGERATIO', **kwargs)

def AirflownetworkDistributionComponentOutdoorairflow(idf, **kwargs: Unpack[AirflownetworkDistributionComponentOutdoorairflowType]):
    """"helper for AirflownetworkDistributionComponentOutdoorairflow"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:OUTDOORAIRFLOW', **kwargs)

def AirflownetworkDistributionComponentReliefairflow(idf, **kwargs: Unpack[AirflownetworkDistributionComponentReliefairflowType]):
    """"helper for AirflownetworkDistributionComponentReliefairflow"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:RELIEFAIRFLOW', **kwargs)

def AirflownetworkDistributionComponentTerminalunit(idf, **kwargs: Unpack[AirflownetworkDistributionComponentTerminalunitType]):
    """"helper for AirflownetworkDistributionComponentTerminalunit"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:TERMINALUNIT', **kwargs)

def AirflownetworkDistributionDuctsizing(idf, **kwargs: Unpack[AirflownetworkDistributionDuctsizingType]):
    """"helper for AirflownetworkDistributionDuctsizing"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:DUCTSIZING', **kwargs)

def AirflownetworkDistributionDuctviewfactors(idf, **kwargs: Unpack[AirflownetworkDistributionDuctviewfactorsType]):
    """"helper for AirflownetworkDistributionDuctviewfactors"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:DUCTVIEWFACTORS', **kwargs)

def AirflownetworkDistributionLinkage(idf, **kwargs: Unpack[AirflownetworkDistributionLinkageType]):
    """"helper for AirflownetworkDistributionLinkage"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:LINKAGE', **kwargs)

def AirflownetworkDistributionNode(idf, **kwargs: Unpack[AirflownetworkDistributionNodeType]):
    """"helper for AirflownetworkDistributionNode"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:NODE', **kwargs)

def AirflownetworkIntrazoneLinkage(idf, **kwargs: Unpack[AirflownetworkIntrazoneLinkageType]):
    """"helper for AirflownetworkIntrazoneLinkage"""
    return idf.newidfobject('AIRFLOWNETWORK:INTRAZONE:LINKAGE', **kwargs)

def AirflownetworkIntrazoneNode(idf, **kwargs: Unpack[AirflownetworkIntrazoneNodeType]):
    """"helper for AirflownetworkIntrazoneNode"""
    return idf.newidfobject('AIRFLOWNETWORK:INTRAZONE:NODE', **kwargs)

def AirflownetworkMultizoneComponentDetailedopening(idf, **kwargs: Unpack[AirflownetworkMultizoneComponentDetailedopeningType]):
    """"helper for AirflownetworkMultizoneComponentDetailedopening"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:COMPONENT:DETAILEDOPENING', **kwargs)

def AirflownetworkMultizoneComponentHorizontalopening(idf, **kwargs: Unpack[AirflownetworkMultizoneComponentHorizontalopeningType]):
    """"helper for AirflownetworkMultizoneComponentHorizontalopening"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:COMPONENT:HORIZONTALOPENING', **kwargs)

def AirflownetworkMultizoneComponentSimpleopening(idf, **kwargs: Unpack[AirflownetworkMultizoneComponentSimpleopeningType]):
    """"helper for AirflownetworkMultizoneComponentSimpleopening"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:COMPONENT:SIMPLEOPENING', **kwargs)

def AirflownetworkMultizoneComponentZoneexhaustfan(idf, **kwargs: Unpack[AirflownetworkMultizoneComponentZoneexhaustfanType]):
    """"helper for AirflownetworkMultizoneComponentZoneexhaustfan"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:COMPONENT:ZONEEXHAUSTFAN', **kwargs)

def AirflownetworkMultizoneExternalnode(idf, **kwargs: Unpack[AirflownetworkMultizoneExternalnodeType]):
    """"helper for AirflownetworkMultizoneExternalnode"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:EXTERNALNODE', **kwargs)

def AirflownetworkMultizoneReferencecrackconditions(idf, **kwargs: Unpack[AirflownetworkMultizoneReferencecrackconditionsType]):
    """"helper for AirflownetworkMultizoneReferencecrackconditions"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:REFERENCECRACKCONDITIONS', **kwargs)

def AirflownetworkMultizoneSpecifiedflowrate(idf, **kwargs: Unpack[AirflownetworkMultizoneSpecifiedflowrateType]):
    """"helper for AirflownetworkMultizoneSpecifiedflowrate"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:SPECIFIEDFLOWRATE', **kwargs)

def AirflownetworkMultizoneSurface(idf, **kwargs: Unpack[AirflownetworkMultizoneSurfaceType]):
    """"helper for AirflownetworkMultizoneSurface"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:SURFACE', **kwargs)

def AirflownetworkMultizoneSurfaceCrack(idf, **kwargs: Unpack[AirflownetworkMultizoneSurfaceCrackType]):
    """"helper for AirflownetworkMultizoneSurfaceCrack"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:SURFACE:CRACK', **kwargs)

def AirflownetworkMultizoneSurfaceEffectiveleakagearea(idf, **kwargs: Unpack[AirflownetworkMultizoneSurfaceEffectiveleakageareaType]):
    """"helper for AirflownetworkMultizoneSurfaceEffectiveleakagearea"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:SURFACE:EFFECTIVELEAKAGEAREA', **kwargs)

def AirflownetworkMultizoneWindpressurecoefficientarray(idf, **kwargs: Unpack[AirflownetworkMultizoneWindpressurecoefficientarrayType]):
    """"helper for AirflownetworkMultizoneWindpressurecoefficientarray"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:WINDPRESSURECOEFFICIENTARRAY', **kwargs)

def AirflownetworkMultizoneWindpressurecoefficientvalues(idf, **kwargs: Unpack[AirflownetworkMultizoneWindpressurecoefficientvaluesType]):
    """"helper for AirflownetworkMultizoneWindpressurecoefficientvalues"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:WINDPRESSURECOEFFICIENTVALUES', **kwargs)

def AirflownetworkMultizoneZone(idf, **kwargs: Unpack[AirflownetworkMultizoneZoneType]):
    """"helper for AirflownetworkMultizoneZone"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:ZONE', **kwargs)

def AirflownetworkOccupantventilationcontrol(idf, **kwargs: Unpack[AirflownetworkOccupantventilationcontrolType]):
    """"helper for AirflownetworkOccupantventilationcontrol"""
    return idf.newidfobject('AIRFLOWNETWORK:OCCUPANTVENTILATIONCONTROL', **kwargs)

def AirflownetworkSimulationcontrol(idf, **kwargs: Unpack[AirflownetworkSimulationcontrolType]):
    """"helper for AirflownetworkSimulationcontrol"""
    return idf.newidfobject('AIRFLOWNETWORK:SIMULATIONCONTROL', **kwargs)

def AirflownetworkZonecontrolPressurecontroller(idf, **kwargs: Unpack[AirflownetworkZonecontrolPressurecontrollerType]):
    """"helper for AirflownetworkZonecontrolPressurecontroller"""
    return idf.newidfobject('AIRFLOWNETWORK:ZONECONTROL:PRESSURECONTROLLER', **kwargs)

def Airloophvac(idf, **kwargs: Unpack[AirloophvacType]):
    """"helper for Airloophvac"""
    return idf.newidfobject('AIRLOOPHVAC', **kwargs)

def AirloophvacControllerlist(idf, **kwargs: Unpack[AirloophvacControllerlistType]):
    """"helper for AirloophvacControllerlist"""
    return idf.newidfobject('AIRLOOPHVAC:CONTROLLERLIST', **kwargs)

def AirloophvacDedicatedoutdoorairsystem(idf, **kwargs: Unpack[AirloophvacDedicatedoutdoorairsystemType]):
    """"helper for AirloophvacDedicatedoutdoorairsystem"""
    return idf.newidfobject('AIRLOOPHVAC:DEDICATEDOUTDOORAIRSYSTEM', **kwargs)

def AirloophvacExhaustsystem(idf, **kwargs: Unpack[AirloophvacExhaustsystemType]):
    """"helper for AirloophvacExhaustsystem"""
    return idf.newidfobject('AIRLOOPHVAC:EXHAUSTSYSTEM', **kwargs)

def AirloophvacMixer(idf, **kwargs: Unpack[AirloophvacMixerType]):
    """"helper for AirloophvacMixer"""
    return idf.newidfobject('AIRLOOPHVAC:MIXER', **kwargs)

def AirloophvacOutdoorairsystem(idf, **kwargs: Unpack[AirloophvacOutdoorairsystemType]):
    """"helper for AirloophvacOutdoorairsystem"""
    return idf.newidfobject('AIRLOOPHVAC:OUTDOORAIRSYSTEM', **kwargs)

def AirloophvacOutdoorairsystemEquipmentlist(idf, **kwargs: Unpack[AirloophvacOutdoorairsystemEquipmentlistType]):
    """"helper for AirloophvacOutdoorairsystemEquipmentlist"""
    return idf.newidfobject('AIRLOOPHVAC:OUTDOORAIRSYSTEM:EQUIPMENTLIST', **kwargs)

def AirloophvacReturnpath(idf, **kwargs: Unpack[AirloophvacReturnpathType]):
    """"helper for AirloophvacReturnpath"""
    return idf.newidfobject('AIRLOOPHVAC:RETURNPATH', **kwargs)

def AirloophvacReturnplenum(idf, **kwargs: Unpack[AirloophvacReturnplenumType]):
    """"helper for AirloophvacReturnplenum"""
    return idf.newidfobject('AIRLOOPHVAC:RETURNPLENUM', **kwargs)

def AirloophvacSplitter(idf, **kwargs: Unpack[AirloophvacSplitterType]):
    """"helper for AirloophvacSplitter"""
    return idf.newidfobject('AIRLOOPHVAC:SPLITTER', **kwargs)

def AirloophvacSupplypath(idf, **kwargs: Unpack[AirloophvacSupplypathType]):
    """"helper for AirloophvacSupplypath"""
    return idf.newidfobject('AIRLOOPHVAC:SUPPLYPATH', **kwargs)

def AirloophvacSupplyplenum(idf, **kwargs: Unpack[AirloophvacSupplyplenumType]):
    """"helper for AirloophvacSupplyplenum"""
    return idf.newidfobject('AIRLOOPHVAC:SUPPLYPLENUM', **kwargs)

def AirloophvacUnitaryFurnaceHeatcool(idf, **kwargs: Unpack[AirloophvacUnitaryFurnaceHeatcoolType]):
    """"helper for AirloophvacUnitaryFurnaceHeatcool"""
    return idf.newidfobject('AIRLOOPHVAC:UNITARY:FURNACE:HEATCOOL', **kwargs)

def AirloophvacUnitaryFurnaceHeatonly(idf, **kwargs: Unpack[AirloophvacUnitaryFurnaceHeatonlyType]):
    """"helper for AirloophvacUnitaryFurnaceHeatonly"""
    return idf.newidfobject('AIRLOOPHVAC:UNITARY:FURNACE:HEATONLY', **kwargs)

def AirloophvacUnitaryheatcool(idf, **kwargs: Unpack[AirloophvacUnitaryheatcoolType]):
    """"helper for AirloophvacUnitaryheatcool"""
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATCOOL', **kwargs)

def AirloophvacUnitaryheatcoolVavchangeoverbypass(idf, **kwargs: Unpack[AirloophvacUnitaryheatcoolVavchangeoverbypassType]):
    """"helper for AirloophvacUnitaryheatcoolVavchangeoverbypass"""
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATCOOL:VAVCHANGEOVERBYPASS', **kwargs)

def AirloophvacUnitaryheatonly(idf, **kwargs: Unpack[AirloophvacUnitaryheatonlyType]):
    """"helper for AirloophvacUnitaryheatonly"""
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATONLY', **kwargs)

def AirloophvacUnitaryheatpumpAirtoair(idf, **kwargs: Unpack[AirloophvacUnitaryheatpumpAirtoairType]):
    """"helper for AirloophvacUnitaryheatpumpAirtoair"""
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATPUMP:AIRTOAIR', **kwargs)

def AirloophvacUnitaryheatpumpAirtoairMultispeed(idf, **kwargs: Unpack[AirloophvacUnitaryheatpumpAirtoairMultispeedType]):
    """"helper for AirloophvacUnitaryheatpumpAirtoairMultispeed"""
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATPUMP:AIRTOAIR:MULTISPEED', **kwargs)

def AirloophvacUnitaryheatpumpWatertoair(idf, **kwargs: Unpack[AirloophvacUnitaryheatpumpWatertoairType]):
    """"helper for AirloophvacUnitaryheatpumpWatertoair"""
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATPUMP:WATERTOAIR', **kwargs)

def AirloophvacUnitarysystem(idf, **kwargs: Unpack[AirloophvacUnitarysystemType]):
    """"helper for AirloophvacUnitarysystem"""
    return idf.newidfobject('AIRLOOPHVAC:UNITARYSYSTEM', **kwargs)

def AirloophvacZonemixer(idf, **kwargs: Unpack[AirloophvacZonemixerType]):
    """"helper for AirloophvacZonemixer"""
    return idf.newidfobject('AIRLOOPHVAC:ZONEMIXER', **kwargs)

def AirloophvacZonesplitter(idf, **kwargs: Unpack[AirloophvacZonesplitterType]):
    """"helper for AirloophvacZonesplitter"""
    return idf.newidfobject('AIRLOOPHVAC:ZONESPLITTER', **kwargs)

def AirterminalDualductConstantvolume(idf, **kwargs: Unpack[AirterminalDualductConstantvolumeType]):
    """"helper for AirterminalDualductConstantvolume"""
    return idf.newidfobject('AIRTERMINAL:DUALDUCT:CONSTANTVOLUME', **kwargs)

def AirterminalDualductVav(idf, **kwargs: Unpack[AirterminalDualductVavType]):
    """"helper for AirterminalDualductVav"""
    return idf.newidfobject('AIRTERMINAL:DUALDUCT:VAV', **kwargs)

def AirterminalDualductVavOutdoorair(idf, **kwargs: Unpack[AirterminalDualductVavOutdoorairType]):
    """"helper for AirterminalDualductVavOutdoorair"""
    return idf.newidfobject('AIRTERMINAL:DUALDUCT:VAV:OUTDOORAIR', **kwargs)

def AirterminalSingleductConstantvolumeCooledbeam(idf, **kwargs: Unpack[AirterminalSingleductConstantvolumeCooledbeamType]):
    """"helper for AirterminalSingleductConstantvolumeCooledbeam"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:COOLEDBEAM', **kwargs)

def AirterminalSingleductConstantvolumeFourpipebeam(idf, **kwargs: Unpack[AirterminalSingleductConstantvolumeFourpipebeamType]):
    """"helper for AirterminalSingleductConstantvolumeFourpipebeam"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:FOURPIPEBEAM', **kwargs)

def AirterminalSingleductConstantvolumeFourpipeinduction(idf, **kwargs: Unpack[AirterminalSingleductConstantvolumeFourpipeinductionType]):
    """"helper for AirterminalSingleductConstantvolumeFourpipeinduction"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:FOURPIPEINDUCTION', **kwargs)

def AirterminalSingleductConstantvolumeNoreheat(idf, **kwargs: Unpack[AirterminalSingleductConstantvolumeNoreheatType]):
    """"helper for AirterminalSingleductConstantvolumeNoreheat"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:NOREHEAT', **kwargs)

def AirterminalSingleductConstantvolumeReheat(idf, **kwargs: Unpack[AirterminalSingleductConstantvolumeReheatType]):
    """"helper for AirterminalSingleductConstantvolumeReheat"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:REHEAT', **kwargs)

def AirterminalSingleductMixer(idf, **kwargs: Unpack[AirterminalSingleductMixerType]):
    """"helper for AirterminalSingleductMixer"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:MIXER', **kwargs)

def AirterminalSingleductParallelpiuReheat(idf, **kwargs: Unpack[AirterminalSingleductParallelpiuReheatType]):
    """"helper for AirterminalSingleductParallelpiuReheat"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:PARALLELPIU:REHEAT', **kwargs)

def AirterminalSingleductSeriespiuReheat(idf, **kwargs: Unpack[AirterminalSingleductSeriespiuReheatType]):
    """"helper for AirterminalSingleductSeriespiuReheat"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:SERIESPIU:REHEAT', **kwargs)

def AirterminalSingleductUserdefined(idf, **kwargs: Unpack[AirterminalSingleductUserdefinedType]):
    """"helper for AirterminalSingleductUserdefined"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:USERDEFINED', **kwargs)

def AirterminalSingleductVavHeatandcoolNoreheat(idf, **kwargs: Unpack[AirterminalSingleductVavHeatandcoolNoreheatType]):
    """"helper for AirterminalSingleductVavHeatandcoolNoreheat"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:VAV:HEATANDCOOL:NOREHEAT', **kwargs)

def AirterminalSingleductVavHeatandcoolReheat(idf, **kwargs: Unpack[AirterminalSingleductVavHeatandcoolReheatType]):
    """"helper for AirterminalSingleductVavHeatandcoolReheat"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:VAV:HEATANDCOOL:REHEAT', **kwargs)

def AirterminalSingleductVavNoreheat(idf, **kwargs: Unpack[AirterminalSingleductVavNoreheatType]):
    """"helper for AirterminalSingleductVavNoreheat"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:VAV:NOREHEAT', **kwargs)

def AirterminalSingleductVavReheat(idf, **kwargs: Unpack[AirterminalSingleductVavReheatType]):
    """"helper for AirterminalSingleductVavReheat"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:VAV:REHEAT', **kwargs)

def AirterminalSingleductVavReheatVariablespeedfan(idf, **kwargs: Unpack[AirterminalSingleductVavReheatVariablespeedfanType]):
    """"helper for AirterminalSingleductVavReheatVariablespeedfan"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:VAV:REHEAT:VARIABLESPEEDFAN', **kwargs)

def AvailabilitymanagerDifferentialthermostat(idf, **kwargs: Unpack[AvailabilitymanagerDifferentialthermostatType]):
    """"helper for AvailabilitymanagerDifferentialthermostat"""
    return idf.newidfobject('AVAILABILITYMANAGER:DIFFERENTIALTHERMOSTAT', **kwargs)

def AvailabilitymanagerHightemperatureturnoff(idf, **kwargs: Unpack[AvailabilitymanagerHightemperatureturnoffType]):
    """"helper for AvailabilitymanagerHightemperatureturnoff"""
    return idf.newidfobject('AVAILABILITYMANAGER:HIGHTEMPERATURETURNOFF', **kwargs)

def AvailabilitymanagerHightemperatureturnon(idf, **kwargs: Unpack[AvailabilitymanagerHightemperatureturnonType]):
    """"helper for AvailabilitymanagerHightemperatureturnon"""
    return idf.newidfobject('AVAILABILITYMANAGER:HIGHTEMPERATURETURNON', **kwargs)

def AvailabilitymanagerHybridventilation(idf, **kwargs: Unpack[AvailabilitymanagerHybridventilationType]):
    """"helper for AvailabilitymanagerHybridventilation"""
    return idf.newidfobject('AVAILABILITYMANAGER:HYBRIDVENTILATION', **kwargs)

def AvailabilitymanagerLowtemperatureturnoff(idf, **kwargs: Unpack[AvailabilitymanagerLowtemperatureturnoffType]):
    """"helper for AvailabilitymanagerLowtemperatureturnoff"""
    return idf.newidfobject('AVAILABILITYMANAGER:LOWTEMPERATURETURNOFF', **kwargs)

def AvailabilitymanagerLowtemperatureturnon(idf, **kwargs: Unpack[AvailabilitymanagerLowtemperatureturnonType]):
    """"helper for AvailabilitymanagerLowtemperatureturnon"""
    return idf.newidfobject('AVAILABILITYMANAGER:LOWTEMPERATURETURNON', **kwargs)

def AvailabilitymanagerNightcycle(idf, **kwargs: Unpack[AvailabilitymanagerNightcycleType]):
    """"helper for AvailabilitymanagerNightcycle"""
    return idf.newidfobject('AVAILABILITYMANAGER:NIGHTCYCLE', **kwargs)

def AvailabilitymanagerNightventilation(idf, **kwargs: Unpack[AvailabilitymanagerNightventilationType]):
    """"helper for AvailabilitymanagerNightventilation"""
    return idf.newidfobject('AVAILABILITYMANAGER:NIGHTVENTILATION', **kwargs)

def AvailabilitymanagerOptimumstart(idf, **kwargs: Unpack[AvailabilitymanagerOptimumstartType]):
    """"helper for AvailabilitymanagerOptimumstart"""
    return idf.newidfobject('AVAILABILITYMANAGER:OPTIMUMSTART', **kwargs)

def AvailabilitymanagerScheduled(idf, **kwargs: Unpack[AvailabilitymanagerScheduledType]):
    """"helper for AvailabilitymanagerScheduled"""
    return idf.newidfobject('AVAILABILITYMANAGER:SCHEDULED', **kwargs)

def AvailabilitymanagerScheduledoff(idf, **kwargs: Unpack[AvailabilitymanagerScheduledoffType]):
    """"helper for AvailabilitymanagerScheduledoff"""
    return idf.newidfobject('AVAILABILITYMANAGER:SCHEDULEDOFF', **kwargs)

def AvailabilitymanagerScheduledon(idf, **kwargs: Unpack[AvailabilitymanagerScheduledonType]):
    """"helper for AvailabilitymanagerScheduledon"""
    return idf.newidfobject('AVAILABILITYMANAGER:SCHEDULEDON', **kwargs)

def Availabilitymanagerassignmentlist(idf, **kwargs: Unpack[AvailabilitymanagerassignmentlistType]):
    """"helper for Availabilitymanagerassignmentlist"""
    return idf.newidfobject('AVAILABILITYMANAGERASSIGNMENTLIST', **kwargs)

def BoilerHotwater(idf, **kwargs: Unpack[BoilerHotwaterType]):
    """"helper for BoilerHotwater"""
    return idf.newidfobject('BOILER:HOTWATER', **kwargs)

def BoilerSteam(idf, **kwargs: Unpack[BoilerSteamType]):
    """"helper for BoilerSteam"""
    return idf.newidfobject('BOILER:STEAM', **kwargs)

def Branch(idf, **kwargs: Unpack[BranchType]):
    """"helper for Branch"""
    return idf.newidfobject('BRANCH', **kwargs)

def Branchlist(idf, **kwargs: Unpack[BranchlistType]):
    """"helper for Branchlist"""
    return idf.newidfobject('BRANCHLIST', **kwargs)

def Building(idf, **kwargs: Unpack[BuildingType]):
    """"helper for Building"""
    return idf.newidfobject('BUILDING', **kwargs)

def BuildingsurfaceDetailed(idf, **kwargs: Unpack[BuildingsurfaceDetailedType]):
    """"helper for BuildingsurfaceDetailed"""
    return idf.newidfobject('BUILDINGSURFACE:DETAILED', **kwargs)

def CeilingAdiabatic(idf, **kwargs: Unpack[CeilingAdiabaticType]):
    """"helper for CeilingAdiabatic"""
    return idf.newidfobject('CEILING:ADIABATIC', **kwargs)

def CeilingInterzone(idf, **kwargs: Unpack[CeilingInterzoneType]):
    """"helper for CeilingInterzone"""
    return idf.newidfobject('CEILING:INTERZONE', **kwargs)

def Centralheatpumpsystem(idf, **kwargs: Unpack[CentralheatpumpsystemType]):
    """"helper for Centralheatpumpsystem"""
    return idf.newidfobject('CENTRALHEATPUMPSYSTEM', **kwargs)

def ChillerAbsorption(idf, **kwargs: Unpack[ChillerAbsorptionType]):
    """"helper for ChillerAbsorption"""
    return idf.newidfobject('CHILLER:ABSORPTION', **kwargs)

def ChillerAbsorptionIndirect(idf, **kwargs: Unpack[ChillerAbsorptionIndirectType]):
    """"helper for ChillerAbsorptionIndirect"""
    return idf.newidfobject('CHILLER:ABSORPTION:INDIRECT', **kwargs)

def ChillerCombustionturbine(idf, **kwargs: Unpack[ChillerCombustionturbineType]):
    """"helper for ChillerCombustionturbine"""
    return idf.newidfobject('CHILLER:COMBUSTIONTURBINE', **kwargs)

def ChillerConstantcop(idf, **kwargs: Unpack[ChillerConstantcopType]):
    """"helper for ChillerConstantcop"""
    return idf.newidfobject('CHILLER:CONSTANTCOP', **kwargs)

def ChillerElectric(idf, **kwargs: Unpack[ChillerElectricType]):
    """"helper for ChillerElectric"""
    return idf.newidfobject('CHILLER:ELECTRIC', **kwargs)

def ChillerElectricAshrae205(idf, **kwargs: Unpack[ChillerElectricAshrae205Type]):
    """"helper for ChillerElectricAshrae205"""
    return idf.newidfobject('CHILLER:ELECTRIC:ASHRAE205', **kwargs)

def ChillerElectricEir(idf, **kwargs: Unpack[ChillerElectricEirType]):
    """"helper for ChillerElectricEir"""
    return idf.newidfobject('CHILLER:ELECTRIC:EIR', **kwargs)

def ChillerElectricReformulatedeir(idf, **kwargs: Unpack[ChillerElectricReformulatedeirType]):
    """"helper for ChillerElectricReformulatedeir"""
    return idf.newidfobject('CHILLER:ELECTRIC:REFORMULATEDEIR', **kwargs)

def ChillerEnginedriven(idf, **kwargs: Unpack[ChillerEnginedrivenType]):
    """"helper for ChillerEnginedriven"""
    return idf.newidfobject('CHILLER:ENGINEDRIVEN', **kwargs)

def ChillerheaterAbsorptionDirectfired(idf, **kwargs: Unpack[ChillerheaterAbsorptionDirectfiredType]):
    """"helper for ChillerheaterAbsorptionDirectfired"""
    return idf.newidfobject('CHILLERHEATER:ABSORPTION:DIRECTFIRED', **kwargs)

def ChillerheaterAbsorptionDoubleeffect(idf, **kwargs: Unpack[ChillerheaterAbsorptionDoubleeffectType]):
    """"helper for ChillerheaterAbsorptionDoubleeffect"""
    return idf.newidfobject('CHILLERHEATER:ABSORPTION:DOUBLEEFFECT', **kwargs)

def ChillerheaterperformanceElectricEir(idf, **kwargs: Unpack[ChillerheaterperformanceElectricEirType]):
    """"helper for ChillerheaterperformanceElectricEir"""
    return idf.newidfobject('CHILLERHEATERPERFORMANCE:ELECTRIC:EIR', **kwargs)

def CoilCoolingDx(idf, **kwargs: Unpack[CoilCoolingDxType]):
    """"helper for CoilCoolingDx"""
    return idf.newidfobject('COIL:COOLING:DX', **kwargs)

def CoilCoolingDxCurvefitOperatingmode(idf, **kwargs: Unpack[CoilCoolingDxCurvefitOperatingmodeType]):
    """"helper for CoilCoolingDxCurvefitOperatingmode"""
    return idf.newidfobject('COIL:COOLING:DX:CURVEFIT:OPERATINGMODE', **kwargs)

def CoilCoolingDxCurvefitPerformance(idf, **kwargs: Unpack[CoilCoolingDxCurvefitPerformanceType]):
    """"helper for CoilCoolingDxCurvefitPerformance"""
    return idf.newidfobject('COIL:COOLING:DX:CURVEFIT:PERFORMANCE', **kwargs)

def CoilCoolingDxCurvefitSpeed(idf, **kwargs: Unpack[CoilCoolingDxCurvefitSpeedType]):
    """"helper for CoilCoolingDxCurvefitSpeed"""
    return idf.newidfobject('COIL:COOLING:DX:CURVEFIT:SPEED', **kwargs)

def CoilCoolingDxMultispeed(idf, **kwargs: Unpack[CoilCoolingDxMultispeedType]):
    """"helper for CoilCoolingDxMultispeed"""
    return idf.newidfobject('COIL:COOLING:DX:MULTISPEED', **kwargs)

def CoilCoolingDxSinglespeed(idf, **kwargs: Unpack[CoilCoolingDxSinglespeedType]):
    """"helper for CoilCoolingDxSinglespeed"""
    return idf.newidfobject('COIL:COOLING:DX:SINGLESPEED', **kwargs)

def CoilCoolingDxSinglespeedThermalstorage(idf, **kwargs: Unpack[CoilCoolingDxSinglespeedThermalstorageType]):
    """"helper for CoilCoolingDxSinglespeedThermalstorage"""
    return idf.newidfobject('COIL:COOLING:DX:SINGLESPEED:THERMALSTORAGE', **kwargs)

def CoilCoolingDxTwospeed(idf, **kwargs: Unpack[CoilCoolingDxTwospeedType]):
    """"helper for CoilCoolingDxTwospeed"""
    return idf.newidfobject('COIL:COOLING:DX:TWOSPEED', **kwargs)

def CoilCoolingDxTwostagewithhumiditycontrolmode(idf, **kwargs: Unpack[CoilCoolingDxTwostagewithhumiditycontrolmodeType]):
    """"helper for CoilCoolingDxTwostagewithhumiditycontrolmode"""
    return idf.newidfobject('COIL:COOLING:DX:TWOSTAGEWITHHUMIDITYCONTROLMODE', **kwargs)

def CoilCoolingDxVariablerefrigerantflow(idf, **kwargs: Unpack[CoilCoolingDxVariablerefrigerantflowType]):
    """"helper for CoilCoolingDxVariablerefrigerantflow"""
    return idf.newidfobject('COIL:COOLING:DX:VARIABLEREFRIGERANTFLOW', **kwargs)

def CoilCoolingDxVariablerefrigerantflowFluidtemperaturecontrol(idf, **kwargs: Unpack[CoilCoolingDxVariablerefrigerantflowFluidtemperaturecontrolType]):
    """"helper for CoilCoolingDxVariablerefrigerantflowFluidtemperaturecontrol"""
    return idf.newidfobject('COIL:COOLING:DX:VARIABLEREFRIGERANTFLOW:FLUIDTEMPERATURECONTROL', **kwargs)

def CoilCoolingDxVariablespeed(idf, **kwargs: Unpack[CoilCoolingDxVariablespeedType]):
    """"helper for CoilCoolingDxVariablespeed"""
    return idf.newidfobject('COIL:COOLING:DX:VARIABLESPEED', **kwargs)

def CoilCoolingWater(idf, **kwargs: Unpack[CoilCoolingWaterType]):
    """"helper for CoilCoolingWater"""
    return idf.newidfobject('COIL:COOLING:WATER', **kwargs)

def CoilCoolingWaterDetailedgeometry(idf, **kwargs: Unpack[CoilCoolingWaterDetailedgeometryType]):
    """"helper for CoilCoolingWaterDetailedgeometry"""
    return idf.newidfobject('COIL:COOLING:WATER:DETAILEDGEOMETRY', **kwargs)

def CoilCoolingWatertoairheatpumpEquationfit(idf, **kwargs: Unpack[CoilCoolingWatertoairheatpumpEquationfitType]):
    """"helper for CoilCoolingWatertoairheatpumpEquationfit"""
    return idf.newidfobject('COIL:COOLING:WATERTOAIRHEATPUMP:EQUATIONFIT', **kwargs)

def CoilCoolingWatertoairheatpumpParameterestimation(idf, **kwargs: Unpack[CoilCoolingWatertoairheatpumpParameterestimationType]):
    """"helper for CoilCoolingWatertoairheatpumpParameterestimation"""
    return idf.newidfobject('COIL:COOLING:WATERTOAIRHEATPUMP:PARAMETERESTIMATION', **kwargs)

def CoilCoolingWatertoairheatpumpVariablespeedequationfit(idf, **kwargs: Unpack[CoilCoolingWatertoairheatpumpVariablespeedequationfitType]):
    """"helper for CoilCoolingWatertoairheatpumpVariablespeedequationfit"""
    return idf.newidfobject('COIL:COOLING:WATERTOAIRHEATPUMP:VARIABLESPEEDEQUATIONFIT', **kwargs)

def CoilHeatingDesuperheater(idf, **kwargs: Unpack[CoilHeatingDesuperheaterType]):
    """"helper for CoilHeatingDesuperheater"""
    return idf.newidfobject('COIL:HEATING:DESUPERHEATER', **kwargs)

def CoilHeatingDxMultispeed(idf, **kwargs: Unpack[CoilHeatingDxMultispeedType]):
    """"helper for CoilHeatingDxMultispeed"""
    return idf.newidfobject('COIL:HEATING:DX:MULTISPEED', **kwargs)

def CoilHeatingDxSinglespeed(idf, **kwargs: Unpack[CoilHeatingDxSinglespeedType]):
    """"helper for CoilHeatingDxSinglespeed"""
    return idf.newidfobject('COIL:HEATING:DX:SINGLESPEED', **kwargs)

def CoilHeatingDxVariablerefrigerantflow(idf, **kwargs: Unpack[CoilHeatingDxVariablerefrigerantflowType]):
    """"helper for CoilHeatingDxVariablerefrigerantflow"""
    return idf.newidfobject('COIL:HEATING:DX:VARIABLEREFRIGERANTFLOW', **kwargs)

def CoilHeatingDxVariablerefrigerantflowFluidtemperaturecontrol(idf, **kwargs: Unpack[CoilHeatingDxVariablerefrigerantflowFluidtemperaturecontrolType]):
    """"helper for CoilHeatingDxVariablerefrigerantflowFluidtemperaturecontrol"""
    return idf.newidfobject('COIL:HEATING:DX:VARIABLEREFRIGERANTFLOW:FLUIDTEMPERATURECONTROL', **kwargs)

def CoilHeatingDxVariablespeed(idf, **kwargs: Unpack[CoilHeatingDxVariablespeedType]):
    """"helper for CoilHeatingDxVariablespeed"""
    return idf.newidfobject('COIL:HEATING:DX:VARIABLESPEED', **kwargs)

def CoilHeatingElectric(idf, **kwargs: Unpack[CoilHeatingElectricType]):
    """"helper for CoilHeatingElectric"""
    return idf.newidfobject('COIL:HEATING:ELECTRIC', **kwargs)

def CoilHeatingElectricMultistage(idf, **kwargs: Unpack[CoilHeatingElectricMultistageType]):
    """"helper for CoilHeatingElectricMultistage"""
    return idf.newidfobject('COIL:HEATING:ELECTRIC:MULTISTAGE', **kwargs)

def CoilHeatingFuel(idf, **kwargs: Unpack[CoilHeatingFuelType]):
    """"helper for CoilHeatingFuel"""
    return idf.newidfobject('COIL:HEATING:FUEL', **kwargs)

def CoilHeatingGasMultistage(idf, **kwargs: Unpack[CoilHeatingGasMultistageType]):
    """"helper for CoilHeatingGasMultistage"""
    return idf.newidfobject('COIL:HEATING:GAS:MULTISTAGE', **kwargs)

def CoilHeatingSteam(idf, **kwargs: Unpack[CoilHeatingSteamType]):
    """"helper for CoilHeatingSteam"""
    return idf.newidfobject('COIL:HEATING:STEAM', **kwargs)

def CoilHeatingWater(idf, **kwargs: Unpack[CoilHeatingWaterType]):
    """"helper for CoilHeatingWater"""
    return idf.newidfobject('COIL:HEATING:WATER', **kwargs)

def CoilHeatingWatertoairheatpumpEquationfit(idf, **kwargs: Unpack[CoilHeatingWatertoairheatpumpEquationfitType]):
    """"helper for CoilHeatingWatertoairheatpumpEquationfit"""
    return idf.newidfobject('COIL:HEATING:WATERTOAIRHEATPUMP:EQUATIONFIT', **kwargs)

def CoilHeatingWatertoairheatpumpParameterestimation(idf, **kwargs: Unpack[CoilHeatingWatertoairheatpumpParameterestimationType]):
    """"helper for CoilHeatingWatertoairheatpumpParameterestimation"""
    return idf.newidfobject('COIL:HEATING:WATERTOAIRHEATPUMP:PARAMETERESTIMATION', **kwargs)

def CoilHeatingWatertoairheatpumpVariablespeedequationfit(idf, **kwargs: Unpack[CoilHeatingWatertoairheatpumpVariablespeedequationfitType]):
    """"helper for CoilHeatingWatertoairheatpumpVariablespeedequationfit"""
    return idf.newidfobject('COIL:HEATING:WATERTOAIRHEATPUMP:VARIABLESPEEDEQUATIONFIT', **kwargs)

def CoilUserdefined(idf, **kwargs: Unpack[CoilUserdefinedType]):
    """"helper for CoilUserdefined"""
    return idf.newidfobject('COIL:USERDEFINED', **kwargs)

def CoilWaterheatingAirtowaterheatpumpPumped(idf, **kwargs: Unpack[CoilWaterheatingAirtowaterheatpumpPumpedType]):
    """"helper for CoilWaterheatingAirtowaterheatpumpPumped"""
    return idf.newidfobject('COIL:WATERHEATING:AIRTOWATERHEATPUMP:PUMPED', **kwargs)

def CoilWaterheatingAirtowaterheatpumpVariablespeed(idf, **kwargs: Unpack[CoilWaterheatingAirtowaterheatpumpVariablespeedType]):
    """"helper for CoilWaterheatingAirtowaterheatpumpVariablespeed"""
    return idf.newidfobject('COIL:WATERHEATING:AIRTOWATERHEATPUMP:VARIABLESPEED', **kwargs)

def CoilWaterheatingAirtowaterheatpumpWrapped(idf, **kwargs: Unpack[CoilWaterheatingAirtowaterheatpumpWrappedType]):
    """"helper for CoilWaterheatingAirtowaterheatpumpWrapped"""
    return idf.newidfobject('COIL:WATERHEATING:AIRTOWATERHEATPUMP:WRAPPED', **kwargs)

def CoilWaterheatingDesuperheater(idf, **kwargs: Unpack[CoilWaterheatingDesuperheaterType]):
    """"helper for CoilWaterheatingDesuperheater"""
    return idf.newidfobject('COIL:WATERHEATING:DESUPERHEATER', **kwargs)

def CoilperformanceDxCooling(idf, **kwargs: Unpack[CoilperformanceDxCoolingType]):
    """"helper for CoilperformanceDxCooling"""
    return idf.newidfobject('COILPERFORMANCE:DX:COOLING', **kwargs)

def CoilsystemCoolingDx(idf, **kwargs: Unpack[CoilsystemCoolingDxType]):
    """"helper for CoilsystemCoolingDx"""
    return idf.newidfobject('COILSYSTEM:COOLING:DX', **kwargs)

def CoilsystemCoolingDxHeatexchangerassisted(idf, **kwargs: Unpack[CoilsystemCoolingDxHeatexchangerassistedType]):
    """"helper for CoilsystemCoolingDxHeatexchangerassisted"""
    return idf.newidfobject('COILSYSTEM:COOLING:DX:HEATEXCHANGERASSISTED', **kwargs)

def CoilsystemCoolingWater(idf, **kwargs: Unpack[CoilsystemCoolingWaterType]):
    """"helper for CoilsystemCoolingWater"""
    return idf.newidfobject('COILSYSTEM:COOLING:WATER', **kwargs)

def CoilsystemCoolingWaterHeatexchangerassisted(idf, **kwargs: Unpack[CoilsystemCoolingWaterHeatexchangerassistedType]):
    """"helper for CoilsystemCoolingWaterHeatexchangerassisted"""
    return idf.newidfobject('COILSYSTEM:COOLING:WATER:HEATEXCHANGERASSISTED', **kwargs)

def CoilsystemHeatingDx(idf, **kwargs: Unpack[CoilsystemHeatingDxType]):
    """"helper for CoilsystemHeatingDx"""
    return idf.newidfobject('COILSYSTEM:HEATING:DX', **kwargs)

def CoilsystemIntegratedheatpumpAirsource(idf, **kwargs: Unpack[CoilsystemIntegratedheatpumpAirsourceType]):
    """"helper for CoilsystemIntegratedheatpumpAirsource"""
    return idf.newidfobject('COILSYSTEM:INTEGRATEDHEATPUMP:AIRSOURCE', **kwargs)

def Comfortviewfactorangles(idf, **kwargs: Unpack[ComfortviewfactoranglesType]):
    """"helper for Comfortviewfactorangles"""
    return idf.newidfobject('COMFORTVIEWFACTORANGLES', **kwargs)

def ComplexfenestrationpropertySolarabsorbedlayers(idf, **kwargs: Unpack[ComplexfenestrationpropertySolarabsorbedlayersType]):
    """"helper for ComplexfenestrationpropertySolarabsorbedlayers"""
    return idf.newidfobject('COMPLEXFENESTRATIONPROPERTY:SOLARABSORBEDLAYERS', **kwargs)

def ComplianceBuilding(idf, **kwargs: Unpack[ComplianceBuildingType]):
    """"helper for ComplianceBuilding"""
    return idf.newidfobject('COMPLIANCE:BUILDING', **kwargs)

def ComponentcostAdjustments(idf, **kwargs: Unpack[ComponentcostAdjustmentsType]):
    """"helper for ComponentcostAdjustments"""
    return idf.newidfobject('COMPONENTCOST:ADJUSTMENTS', **kwargs)

def ComponentcostLineitem(idf, **kwargs: Unpack[ComponentcostLineitemType]):
    """"helper for ComponentcostLineitem"""
    return idf.newidfobject('COMPONENTCOST:LINEITEM', **kwargs)

def ComponentcostReference(idf, **kwargs: Unpack[ComponentcostReferenceType]):
    """"helper for ComponentcostReference"""
    return idf.newidfobject('COMPONENTCOST:REFERENCE', **kwargs)

def Condenserequipmentlist(idf, **kwargs: Unpack[CondenserequipmentlistType]):
    """"helper for Condenserequipmentlist"""
    return idf.newidfobject('CONDENSEREQUIPMENTLIST', **kwargs)

def Condenserequipmentoperationschemes(idf, **kwargs: Unpack[CondenserequipmentoperationschemesType]):
    """"helper for Condenserequipmentoperationschemes"""
    return idf.newidfobject('CONDENSEREQUIPMENTOPERATIONSCHEMES', **kwargs)

def Condenserloop(idf, **kwargs: Unpack[CondenserloopType]):
    """"helper for Condenserloop"""
    return idf.newidfobject('CONDENSERLOOP', **kwargs)

def ConnectorMixer(idf, **kwargs: Unpack[ConnectorMixerType]):
    """"helper for ConnectorMixer"""
    return idf.newidfobject('CONNECTOR:MIXER', **kwargs)

def ConnectorSplitter(idf, **kwargs: Unpack[ConnectorSplitterType]):
    """"helper for ConnectorSplitter"""
    return idf.newidfobject('CONNECTOR:SPLITTER', **kwargs)

def Connectorlist(idf, **kwargs: Unpack[ConnectorlistType]):
    """"helper for Connectorlist"""
    return idf.newidfobject('CONNECTORLIST', **kwargs)

def Construction(idf, **kwargs: Unpack[ConstructionType]):
    """"helper for Construction"""
    return idf.newidfobject('CONSTRUCTION', **kwargs)

def ConstructionAirboundary(idf, **kwargs: Unpack[ConstructionAirboundaryType]):
    """"helper for ConstructionAirboundary"""
    return idf.newidfobject('CONSTRUCTION:AIRBOUNDARY', **kwargs)

def ConstructionCfactorundergroundwall(idf, **kwargs: Unpack[ConstructionCfactorundergroundwallType]):
    """"helper for ConstructionCfactorundergroundwall"""
    return idf.newidfobject('CONSTRUCTION:CFACTORUNDERGROUNDWALL', **kwargs)

def ConstructionComplexfenestrationstate(idf, **kwargs: Unpack[ConstructionComplexfenestrationstateType]):
    """"helper for ConstructionComplexfenestrationstate"""
    return idf.newidfobject('CONSTRUCTION:COMPLEXFENESTRATIONSTATE', **kwargs)

def ConstructionFfactorgroundfloor(idf, **kwargs: Unpack[ConstructionFfactorgroundfloorType]):
    """"helper for ConstructionFfactorgroundfloor"""
    return idf.newidfobject('CONSTRUCTION:FFACTORGROUNDFLOOR', **kwargs)

def ConstructionWindowdatafile(idf, **kwargs: Unpack[ConstructionWindowdatafileType]):
    """"helper for ConstructionWindowdatafile"""
    return idf.newidfobject('CONSTRUCTION:WINDOWDATAFILE', **kwargs)

def ConstructionWindowequivalentlayer(idf, **kwargs: Unpack[ConstructionWindowequivalentlayerType]):
    """"helper for ConstructionWindowequivalentlayer"""
    return idf.newidfobject('CONSTRUCTION:WINDOWEQUIVALENTLAYER', **kwargs)

def ConstructionpropertyInternalheatsource(idf, **kwargs: Unpack[ConstructionpropertyInternalheatsourceType]):
    """"helper for ConstructionpropertyInternalheatsource"""
    return idf.newidfobject('CONSTRUCTIONPROPERTY:INTERNALHEATSOURCE', **kwargs)

def ControllerMechanicalventilation(idf, **kwargs: Unpack[ControllerMechanicalventilationType]):
    """"helper for ControllerMechanicalventilation"""
    return idf.newidfobject('CONTROLLER:MECHANICALVENTILATION', **kwargs)

def ControllerOutdoorair(idf, **kwargs: Unpack[ControllerOutdoorairType]):
    """"helper for ControllerOutdoorair"""
    return idf.newidfobject('CONTROLLER:OUTDOORAIR', **kwargs)

def ControllerWatercoil(idf, **kwargs: Unpack[ControllerWatercoilType]):
    """"helper for ControllerWatercoil"""
    return idf.newidfobject('CONTROLLER:WATERCOIL', **kwargs)

def Convergencelimits(idf, **kwargs: Unpack[ConvergencelimitsType]):
    """"helper for Convergencelimits"""
    return idf.newidfobject('CONVERGENCELIMITS', **kwargs)

def CoolingtowerSinglespeed(idf, **kwargs: Unpack[CoolingtowerSinglespeedType]):
    """"helper for CoolingtowerSinglespeed"""
    return idf.newidfobject('COOLINGTOWER:SINGLESPEED', **kwargs)

def CoolingtowerTwospeed(idf, **kwargs: Unpack[CoolingtowerTwospeedType]):
    """"helper for CoolingtowerTwospeed"""
    return idf.newidfobject('COOLINGTOWER:TWOSPEED', **kwargs)

def CoolingtowerVariablespeed(idf, **kwargs: Unpack[CoolingtowerVariablespeedType]):
    """"helper for CoolingtowerVariablespeed"""
    return idf.newidfobject('COOLINGTOWER:VARIABLESPEED', **kwargs)

def CoolingtowerVariablespeedMerkel(idf, **kwargs: Unpack[CoolingtowerVariablespeedMerkelType]):
    """"helper for CoolingtowerVariablespeedMerkel"""
    return idf.newidfobject('COOLINGTOWER:VARIABLESPEED:MERKEL', **kwargs)

def CoolingtowerperformanceCooltools(idf, **kwargs: Unpack[CoolingtowerperformanceCooltoolsType]):
    """"helper for CoolingtowerperformanceCooltools"""
    return idf.newidfobject('COOLINGTOWERPERFORMANCE:COOLTOOLS', **kwargs)

def CoolingtowerperformanceYorkcalc(idf, **kwargs: Unpack[CoolingtowerperformanceYorkcalcType]):
    """"helper for CoolingtowerperformanceYorkcalc"""
    return idf.newidfobject('COOLINGTOWERPERFORMANCE:YORKCALC', **kwargs)

def Currencytype(idf, **kwargs: Unpack[CurrencytypeType]):
    """"helper for Currencytype"""
    return idf.newidfobject('CURRENCYTYPE', **kwargs)

def CurveBicubic(idf, **kwargs: Unpack[CurveBicubicType]):
    """"helper for CurveBicubic"""
    return idf.newidfobject('CURVE:BICUBIC', **kwargs)

def CurveBiquadratic(idf, **kwargs: Unpack[CurveBiquadraticType]):
    """"helper for CurveBiquadratic"""
    return idf.newidfobject('CURVE:BIQUADRATIC', **kwargs)

def CurveChillerpartloadwithlift(idf, **kwargs: Unpack[CurveChillerpartloadwithliftType]):
    """"helper for CurveChillerpartloadwithlift"""
    return idf.newidfobject('CURVE:CHILLERPARTLOADWITHLIFT', **kwargs)

def CurveCubic(idf, **kwargs: Unpack[CurveCubicType]):
    """"helper for CurveCubic"""
    return idf.newidfobject('CURVE:CUBIC', **kwargs)

def CurveCubiclinear(idf, **kwargs: Unpack[CurveCubiclinearType]):
    """"helper for CurveCubiclinear"""
    return idf.newidfobject('CURVE:CUBICLINEAR', **kwargs)

def CurveDoubleexponentialdecay(idf, **kwargs: Unpack[CurveDoubleexponentialdecayType]):
    """"helper for CurveDoubleexponentialdecay"""
    return idf.newidfobject('CURVE:DOUBLEEXPONENTIALDECAY', **kwargs)

def CurveExponent(idf, **kwargs: Unpack[CurveExponentType]):
    """"helper for CurveExponent"""
    return idf.newidfobject('CURVE:EXPONENT', **kwargs)

def CurveExponentialdecay(idf, **kwargs: Unpack[CurveExponentialdecayType]):
    """"helper for CurveExponentialdecay"""
    return idf.newidfobject('CURVE:EXPONENTIALDECAY', **kwargs)

def CurveExponentialskewnormal(idf, **kwargs: Unpack[CurveExponentialskewnormalType]):
    """"helper for CurveExponentialskewnormal"""
    return idf.newidfobject('CURVE:EXPONENTIALSKEWNORMAL', **kwargs)

def CurveFanpressurerise(idf, **kwargs: Unpack[CurveFanpressureriseType]):
    """"helper for CurveFanpressurerise"""
    return idf.newidfobject('CURVE:FANPRESSURERISE', **kwargs)

def CurveFunctionalPressuredrop(idf, **kwargs: Unpack[CurveFunctionalPressuredropType]):
    """"helper for CurveFunctionalPressuredrop"""
    return idf.newidfobject('CURVE:FUNCTIONAL:PRESSUREDROP', **kwargs)

def CurveLinear(idf, **kwargs: Unpack[CurveLinearType]):
    """"helper for CurveLinear"""
    return idf.newidfobject('CURVE:LINEAR', **kwargs)

def CurveQuadlinear(idf, **kwargs: Unpack[CurveQuadlinearType]):
    """"helper for CurveQuadlinear"""
    return idf.newidfobject('CURVE:QUADLINEAR', **kwargs)

def CurveQuadratic(idf, **kwargs: Unpack[CurveQuadraticType]):
    """"helper for CurveQuadratic"""
    return idf.newidfobject('CURVE:QUADRATIC', **kwargs)

def CurveQuadraticlinear(idf, **kwargs: Unpack[CurveQuadraticlinearType]):
    """"helper for CurveQuadraticlinear"""
    return idf.newidfobject('CURVE:QUADRATICLINEAR', **kwargs)

def CurveQuartic(idf, **kwargs: Unpack[CurveQuarticType]):
    """"helper for CurveQuartic"""
    return idf.newidfobject('CURVE:QUARTIC', **kwargs)

def CurveQuintlinear(idf, **kwargs: Unpack[CurveQuintlinearType]):
    """"helper for CurveQuintlinear"""
    return idf.newidfobject('CURVE:QUINTLINEAR', **kwargs)

def CurveRectangularhyperbola1(idf, **kwargs: Unpack[CurveRectangularhyperbola1Type]):
    """"helper for CurveRectangularhyperbola1"""
    return idf.newidfobject('CURVE:RECTANGULARHYPERBOLA1', **kwargs)

def CurveRectangularhyperbola2(idf, **kwargs: Unpack[CurveRectangularhyperbola2Type]):
    """"helper for CurveRectangularhyperbola2"""
    return idf.newidfobject('CURVE:RECTANGULARHYPERBOLA2', **kwargs)

def CurveSigmoid(idf, **kwargs: Unpack[CurveSigmoidType]):
    """"helper for CurveSigmoid"""
    return idf.newidfobject('CURVE:SIGMOID', **kwargs)

def CurveTriquadratic(idf, **kwargs: Unpack[CurveTriquadraticType]):
    """"helper for CurveTriquadratic"""
    return idf.newidfobject('CURVE:TRIQUADRATIC', **kwargs)

def DaylightingControls(idf, **kwargs: Unpack[DaylightingControlsType]):
    """"helper for DaylightingControls"""
    return idf.newidfobject('DAYLIGHTING:CONTROLS', **kwargs)

def DaylightingDelightComplexfenestration(idf, **kwargs: Unpack[DaylightingDelightComplexfenestrationType]):
    """"helper for DaylightingDelightComplexfenestration"""
    return idf.newidfobject('DAYLIGHTING:DELIGHT:COMPLEXFENESTRATION', **kwargs)

def DaylightingReferencepoint(idf, **kwargs: Unpack[DaylightingReferencepointType]):
    """"helper for DaylightingReferencepoint"""
    return idf.newidfobject('DAYLIGHTING:REFERENCEPOINT', **kwargs)

def DaylightingdeviceLightwell(idf, **kwargs: Unpack[DaylightingdeviceLightwellType]):
    """"helper for DaylightingdeviceLightwell"""
    return idf.newidfobject('DAYLIGHTINGDEVICE:LIGHTWELL', **kwargs)

def DaylightingdeviceShelf(idf, **kwargs: Unpack[DaylightingdeviceShelfType]):
    """"helper for DaylightingdeviceShelf"""
    return idf.newidfobject('DAYLIGHTINGDEVICE:SHELF', **kwargs)

def DaylightingdeviceTubular(idf, **kwargs: Unpack[DaylightingdeviceTubularType]):
    """"helper for DaylightingdeviceTubular"""
    return idf.newidfobject('DAYLIGHTINGDEVICE:TUBULAR', **kwargs)

def DehumidifierDesiccantNofans(idf, **kwargs: Unpack[DehumidifierDesiccantNofansType]):
    """"helper for DehumidifierDesiccantNofans"""
    return idf.newidfobject('DEHUMIDIFIER:DESICCANT:NOFANS', **kwargs)

def DehumidifierDesiccantSystem(idf, **kwargs: Unpack[DehumidifierDesiccantSystemType]):
    """"helper for DehumidifierDesiccantSystem"""
    return idf.newidfobject('DEHUMIDIFIER:DESICCANT:SYSTEM', **kwargs)

def DemandmanagerElectricequipment(idf, **kwargs: Unpack[DemandmanagerElectricequipmentType]):
    """"helper for DemandmanagerElectricequipment"""
    return idf.newidfobject('DEMANDMANAGER:ELECTRICEQUIPMENT', **kwargs)

def DemandmanagerExteriorlights(idf, **kwargs: Unpack[DemandmanagerExteriorlightsType]):
    """"helper for DemandmanagerExteriorlights"""
    return idf.newidfobject('DEMANDMANAGER:EXTERIORLIGHTS', **kwargs)

def DemandmanagerLights(idf, **kwargs: Unpack[DemandmanagerLightsType]):
    """"helper for DemandmanagerLights"""
    return idf.newidfobject('DEMANDMANAGER:LIGHTS', **kwargs)

def DemandmanagerThermostats(idf, **kwargs: Unpack[DemandmanagerThermostatsType]):
    """"helper for DemandmanagerThermostats"""
    return idf.newidfobject('DEMANDMANAGER:THERMOSTATS', **kwargs)

def DemandmanagerVentilation(idf, **kwargs: Unpack[DemandmanagerVentilationType]):
    """"helper for DemandmanagerVentilation"""
    return idf.newidfobject('DEMANDMANAGER:VENTILATION', **kwargs)

def Demandmanagerassignmentlist(idf, **kwargs: Unpack[DemandmanagerassignmentlistType]):
    """"helper for Demandmanagerassignmentlist"""
    return idf.newidfobject('DEMANDMANAGERASSIGNMENTLIST', **kwargs)

def DesignspecificationAirterminalSizing(idf, **kwargs: Unpack[DesignspecificationAirterminalSizingType]):
    """"helper for DesignspecificationAirterminalSizing"""
    return idf.newidfobject('DESIGNSPECIFICATION:AIRTERMINAL:SIZING', **kwargs)

def DesignspecificationOutdoorair(idf, **kwargs: Unpack[DesignspecificationOutdoorairType]):
    """"helper for DesignspecificationOutdoorair"""
    return idf.newidfobject('DESIGNSPECIFICATION:OUTDOORAIR', **kwargs)

def DesignspecificationOutdoorairSpacelist(idf, **kwargs: Unpack[DesignspecificationOutdoorairSpacelistType]):
    """"helper for DesignspecificationOutdoorairSpacelist"""
    return idf.newidfobject('DESIGNSPECIFICATION:OUTDOORAIR:SPACELIST', **kwargs)

def DesignspecificationZoneairdistribution(idf, **kwargs: Unpack[DesignspecificationZoneairdistributionType]):
    """"helper for DesignspecificationZoneairdistribution"""
    return idf.newidfobject('DESIGNSPECIFICATION:ZONEAIRDISTRIBUTION', **kwargs)

def DesignspecificationZonehvacSizing(idf, **kwargs: Unpack[DesignspecificationZonehvacSizingType]):
    """"helper for DesignspecificationZonehvacSizing"""
    return idf.newidfobject('DESIGNSPECIFICATION:ZONEHVAC:SIZING', **kwargs)

def Districtcooling(idf, **kwargs: Unpack[DistrictcoolingType]):
    """"helper for Districtcooling"""
    return idf.newidfobject('DISTRICTCOOLING', **kwargs)

def DistrictheatingSteam(idf, **kwargs: Unpack[DistrictheatingSteamType]):
    """"helper for DistrictheatingSteam"""
    return idf.newidfobject('DISTRICTHEATING:STEAM', **kwargs)

def DistrictheatingWater(idf, **kwargs: Unpack[DistrictheatingWaterType]):
    """"helper for DistrictheatingWater"""
    return idf.newidfobject('DISTRICTHEATING:WATER', **kwargs)

def Door(idf, **kwargs: Unpack[DoorType]):
    """"helper for Door"""
    return idf.newidfobject('DOOR', **kwargs)

def DoorInterzone(idf, **kwargs: Unpack[DoorInterzoneType]):
    """"helper for DoorInterzone"""
    return idf.newidfobject('DOOR:INTERZONE', **kwargs)

def Duct(idf, **kwargs: Unpack[DuctType]):
    """"helper for Duct"""
    return idf.newidfobject('DUCT', **kwargs)

def Electricequipment(idf, **kwargs: Unpack[ElectricequipmentType]):
    """"helper for Electricequipment"""
    return idf.newidfobject('ELECTRICEQUIPMENT', **kwargs)

def ElectricequipmentIteAircooled(idf, **kwargs: Unpack[ElectricequipmentIteAircooledType]):
    """"helper for ElectricequipmentIteAircooled"""
    return idf.newidfobject('ELECTRICEQUIPMENT:ITE:AIRCOOLED', **kwargs)

def ElectricloadcenterDistribution(idf, **kwargs: Unpack[ElectricloadcenterDistributionType]):
    """"helper for ElectricloadcenterDistribution"""
    return idf.newidfobject('ELECTRICLOADCENTER:DISTRIBUTION', **kwargs)

def ElectricloadcenterGenerators(idf, **kwargs: Unpack[ElectricloadcenterGeneratorsType]):
    """"helper for ElectricloadcenterGenerators"""
    return idf.newidfobject('ELECTRICLOADCENTER:GENERATORS', **kwargs)

def ElectricloadcenterInverterFunctionofpower(idf, **kwargs: Unpack[ElectricloadcenterInverterFunctionofpowerType]):
    """"helper for ElectricloadcenterInverterFunctionofpower"""
    return idf.newidfobject('ELECTRICLOADCENTER:INVERTER:FUNCTIONOFPOWER', **kwargs)

def ElectricloadcenterInverterLookuptable(idf, **kwargs: Unpack[ElectricloadcenterInverterLookuptableType]):
    """"helper for ElectricloadcenterInverterLookuptable"""
    return idf.newidfobject('ELECTRICLOADCENTER:INVERTER:LOOKUPTABLE', **kwargs)

def ElectricloadcenterInverterPvwatts(idf, **kwargs: Unpack[ElectricloadcenterInverterPvwattsType]):
    """"helper for ElectricloadcenterInverterPvwatts"""
    return idf.newidfobject('ELECTRICLOADCENTER:INVERTER:PVWATTS', **kwargs)

def ElectricloadcenterInverterSimple(idf, **kwargs: Unpack[ElectricloadcenterInverterSimpleType]):
    """"helper for ElectricloadcenterInverterSimple"""
    return idf.newidfobject('ELECTRICLOADCENTER:INVERTER:SIMPLE', **kwargs)

def ElectricloadcenterStorageBattery(idf, **kwargs: Unpack[ElectricloadcenterStorageBatteryType]):
    """"helper for ElectricloadcenterStorageBattery"""
    return idf.newidfobject('ELECTRICLOADCENTER:STORAGE:BATTERY', **kwargs)

def ElectricloadcenterStorageConverter(idf, **kwargs: Unpack[ElectricloadcenterStorageConverterType]):
    """"helper for ElectricloadcenterStorageConverter"""
    return idf.newidfobject('ELECTRICLOADCENTER:STORAGE:CONVERTER', **kwargs)

def ElectricloadcenterStorageLiionnmcbattery(idf, **kwargs: Unpack[ElectricloadcenterStorageLiionnmcbatteryType]):
    """"helper for ElectricloadcenterStorageLiionnmcbattery"""
    return idf.newidfobject('ELECTRICLOADCENTER:STORAGE:LIIONNMCBATTERY', **kwargs)

def ElectricloadcenterStorageSimple(idf, **kwargs: Unpack[ElectricloadcenterStorageSimpleType]):
    """"helper for ElectricloadcenterStorageSimple"""
    return idf.newidfobject('ELECTRICLOADCENTER:STORAGE:SIMPLE', **kwargs)

def ElectricloadcenterTransformer(idf, **kwargs: Unpack[ElectricloadcenterTransformerType]):
    """"helper for ElectricloadcenterTransformer"""
    return idf.newidfobject('ELECTRICLOADCENTER:TRANSFORMER', **kwargs)

def EnergymanagementsystemActuator(idf, **kwargs: Unpack[EnergymanagementsystemActuatorType]):
    """"helper for EnergymanagementsystemActuator"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:ACTUATOR', **kwargs)

def EnergymanagementsystemConstructionindexvariable(idf, **kwargs: Unpack[EnergymanagementsystemConstructionindexvariableType]):
    """"helper for EnergymanagementsystemConstructionindexvariable"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:CONSTRUCTIONINDEXVARIABLE', **kwargs)

def EnergymanagementsystemCurveortableindexvariable(idf, **kwargs: Unpack[EnergymanagementsystemCurveortableindexvariableType]):
    """"helper for EnergymanagementsystemCurveortableindexvariable"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:CURVEORTABLEINDEXVARIABLE', **kwargs)

def EnergymanagementsystemGlobalvariable(idf, **kwargs: Unpack[EnergymanagementsystemGlobalvariableType]):
    """"helper for EnergymanagementsystemGlobalvariable"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:GLOBALVARIABLE', **kwargs)

def EnergymanagementsystemInternalvariable(idf, **kwargs: Unpack[EnergymanagementsystemInternalvariableType]):
    """"helper for EnergymanagementsystemInternalvariable"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:INTERNALVARIABLE', **kwargs)

def EnergymanagementsystemMeteredoutputvariable(idf, **kwargs: Unpack[EnergymanagementsystemMeteredoutputvariableType]):
    """"helper for EnergymanagementsystemMeteredoutputvariable"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:METEREDOUTPUTVARIABLE', **kwargs)

def EnergymanagementsystemOutputvariable(idf, **kwargs: Unpack[EnergymanagementsystemOutputvariableType]):
    """"helper for EnergymanagementsystemOutputvariable"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:OUTPUTVARIABLE', **kwargs)

def EnergymanagementsystemProgram(idf, **kwargs: Unpack[EnergymanagementsystemProgramType]):
    """"helper for EnergymanagementsystemProgram"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:PROGRAM', **kwargs)

def EnergymanagementsystemProgramcallingmanager(idf, **kwargs: Unpack[EnergymanagementsystemProgramcallingmanagerType]):
    """"helper for EnergymanagementsystemProgramcallingmanager"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:PROGRAMCALLINGMANAGER', **kwargs)

def EnergymanagementsystemSensor(idf, **kwargs: Unpack[EnergymanagementsystemSensorType]):
    """"helper for EnergymanagementsystemSensor"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:SENSOR', **kwargs)

def EnergymanagementsystemSubroutine(idf, **kwargs: Unpack[EnergymanagementsystemSubroutineType]):
    """"helper for EnergymanagementsystemSubroutine"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:SUBROUTINE', **kwargs)

def EnergymanagementsystemTrendvariable(idf, **kwargs: Unpack[EnergymanagementsystemTrendvariableType]):
    """"helper for EnergymanagementsystemTrendvariable"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:TRENDVARIABLE', **kwargs)

def Environmentalimpactfactors(idf, **kwargs: Unpack[EnvironmentalimpactfactorsType]):
    """"helper for Environmentalimpactfactors"""
    return idf.newidfobject('ENVIRONMENTALIMPACTFACTORS', **kwargs)

def EvaporativecoolerDirectCeldekpad(idf, **kwargs: Unpack[EvaporativecoolerDirectCeldekpadType]):
    """"helper for EvaporativecoolerDirectCeldekpad"""
    return idf.newidfobject('EVAPORATIVECOOLER:DIRECT:CELDEKPAD', **kwargs)

def EvaporativecoolerDirectResearchspecial(idf, **kwargs: Unpack[EvaporativecoolerDirectResearchspecialType]):
    """"helper for EvaporativecoolerDirectResearchspecial"""
    return idf.newidfobject('EVAPORATIVECOOLER:DIRECT:RESEARCHSPECIAL', **kwargs)

def EvaporativecoolerIndirectCeldekpad(idf, **kwargs: Unpack[EvaporativecoolerIndirectCeldekpadType]):
    """"helper for EvaporativecoolerIndirectCeldekpad"""
    return idf.newidfobject('EVAPORATIVECOOLER:INDIRECT:CELDEKPAD', **kwargs)

def EvaporativecoolerIndirectResearchspecial(idf, **kwargs: Unpack[EvaporativecoolerIndirectResearchspecialType]):
    """"helper for EvaporativecoolerIndirectResearchspecial"""
    return idf.newidfobject('EVAPORATIVECOOLER:INDIRECT:RESEARCHSPECIAL', **kwargs)

def EvaporativecoolerIndirectWetcoil(idf, **kwargs: Unpack[EvaporativecoolerIndirectWetcoilType]):
    """"helper for EvaporativecoolerIndirectWetcoil"""
    return idf.newidfobject('EVAPORATIVECOOLER:INDIRECT:WETCOIL', **kwargs)

def EvaporativefluidcoolerSinglespeed(idf, **kwargs: Unpack[EvaporativefluidcoolerSinglespeedType]):
    """"helper for EvaporativefluidcoolerSinglespeed"""
    return idf.newidfobject('EVAPORATIVEFLUIDCOOLER:SINGLESPEED', **kwargs)

def EvaporativefluidcoolerTwospeed(idf, **kwargs: Unpack[EvaporativefluidcoolerTwospeedType]):
    """"helper for EvaporativefluidcoolerTwospeed"""
    return idf.newidfobject('EVAPORATIVEFLUIDCOOLER:TWOSPEED', **kwargs)

def ExteriorFuelequipment(idf, **kwargs: Unpack[ExteriorFuelequipmentType]):
    """"helper for ExteriorFuelequipment"""
    return idf.newidfobject('EXTERIOR:FUELEQUIPMENT', **kwargs)

def ExteriorLights(idf, **kwargs: Unpack[ExteriorLightsType]):
    """"helper for ExteriorLights"""
    return idf.newidfobject('EXTERIOR:LIGHTS', **kwargs)

def ExteriorWaterequipment(idf, **kwargs: Unpack[ExteriorWaterequipmentType]):
    """"helper for ExteriorWaterequipment"""
    return idf.newidfobject('EXTERIOR:WATEREQUIPMENT', **kwargs)

def Externalinterface(idf, **kwargs: Unpack[ExternalinterfaceType]):
    """"helper for Externalinterface"""
    return idf.newidfobject('EXTERNALINTERFACE', **kwargs)

def ExternalinterfaceActuator(idf, **kwargs: Unpack[ExternalinterfaceActuatorType]):
    """"helper for ExternalinterfaceActuator"""
    return idf.newidfobject('EXTERNALINTERFACE:ACTUATOR', **kwargs)

def ExternalinterfaceFunctionalmockupunitexportFromVariable(idf, **kwargs: Unpack[ExternalinterfaceFunctionalmockupunitexportFromVariableType]):
    """"helper for ExternalinterfaceFunctionalmockupunitexportFromVariable"""
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITEXPORT:FROM:VARIABLE', **kwargs)

def ExternalinterfaceFunctionalmockupunitexportToActuator(idf, **kwargs: Unpack[ExternalinterfaceFunctionalmockupunitexportToActuatorType]):
    """"helper for ExternalinterfaceFunctionalmockupunitexportToActuator"""
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITEXPORT:TO:ACTUATOR', **kwargs)

def ExternalinterfaceFunctionalmockupunitexportToSchedule(idf, **kwargs: Unpack[ExternalinterfaceFunctionalmockupunitexportToScheduleType]):
    """"helper for ExternalinterfaceFunctionalmockupunitexportToSchedule"""
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITEXPORT:TO:SCHEDULE', **kwargs)

def ExternalinterfaceFunctionalmockupunitexportToVariable(idf, **kwargs: Unpack[ExternalinterfaceFunctionalmockupunitexportToVariableType]):
    """"helper for ExternalinterfaceFunctionalmockupunitexportToVariable"""
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITEXPORT:TO:VARIABLE', **kwargs)

def ExternalinterfaceFunctionalmockupunitimport(idf, **kwargs: Unpack[ExternalinterfaceFunctionalmockupunitimportType]):
    """"helper for ExternalinterfaceFunctionalmockupunitimport"""
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT', **kwargs)

def ExternalinterfaceFunctionalmockupunitimportFromVariable(idf, **kwargs: Unpack[ExternalinterfaceFunctionalmockupunitimportFromVariableType]):
    """"helper for ExternalinterfaceFunctionalmockupunitimportFromVariable"""
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT:FROM:VARIABLE', **kwargs)

def ExternalinterfaceFunctionalmockupunitimportToActuator(idf, **kwargs: Unpack[ExternalinterfaceFunctionalmockupunitimportToActuatorType]):
    """"helper for ExternalinterfaceFunctionalmockupunitimportToActuator"""
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT:TO:ACTUATOR', **kwargs)

def ExternalinterfaceFunctionalmockupunitimportToSchedule(idf, **kwargs: Unpack[ExternalinterfaceFunctionalmockupunitimportToScheduleType]):
    """"helper for ExternalinterfaceFunctionalmockupunitimportToSchedule"""
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT:TO:SCHEDULE', **kwargs)

def ExternalinterfaceFunctionalmockupunitimportToVariable(idf, **kwargs: Unpack[ExternalinterfaceFunctionalmockupunitimportToVariableType]):
    """"helper for ExternalinterfaceFunctionalmockupunitimportToVariable"""
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT:TO:VARIABLE', **kwargs)

def ExternalinterfaceSchedule(idf, **kwargs: Unpack[ExternalinterfaceScheduleType]):
    """"helper for ExternalinterfaceSchedule"""
    return idf.newidfobject('EXTERNALINTERFACE:SCHEDULE', **kwargs)

def ExternalinterfaceVariable(idf, **kwargs: Unpack[ExternalinterfaceVariableType]):
    """"helper for ExternalinterfaceVariable"""
    return idf.newidfobject('EXTERNALINTERFACE:VARIABLE', **kwargs)

def FanComponentmodel(idf, **kwargs: Unpack[FanComponentmodelType]):
    """"helper for FanComponentmodel"""
    return idf.newidfobject('FAN:COMPONENTMODEL', **kwargs)

def FanConstantvolume(idf, **kwargs: Unpack[FanConstantvolumeType]):
    """"helper for FanConstantvolume"""
    return idf.newidfobject('FAN:CONSTANTVOLUME', **kwargs)

def FanOnoff(idf, **kwargs: Unpack[FanOnoffType]):
    """"helper for FanOnoff"""
    return idf.newidfobject('FAN:ONOFF', **kwargs)

def FanSystemmodel(idf, **kwargs: Unpack[FanSystemmodelType]):
    """"helper for FanSystemmodel"""
    return idf.newidfobject('FAN:SYSTEMMODEL', **kwargs)

def FanVariablevolume(idf, **kwargs: Unpack[FanVariablevolumeType]):
    """"helper for FanVariablevolume"""
    return idf.newidfobject('FAN:VARIABLEVOLUME', **kwargs)

def FanZoneexhaust(idf, **kwargs: Unpack[FanZoneexhaustType]):
    """"helper for FanZoneexhaust"""
    return idf.newidfobject('FAN:ZONEEXHAUST', **kwargs)

def FanperformanceNightventilation(idf, **kwargs: Unpack[FanperformanceNightventilationType]):
    """"helper for FanperformanceNightventilation"""
    return idf.newidfobject('FANPERFORMANCE:NIGHTVENTILATION', **kwargs)

def FaultmodelEnthalpysensoroffsetOutdoorair(idf, **kwargs: Unpack[FaultmodelEnthalpysensoroffsetOutdoorairType]):
    """"helper for FaultmodelEnthalpysensoroffsetOutdoorair"""
    return idf.newidfobject('FAULTMODEL:ENTHALPYSENSOROFFSET:OUTDOORAIR', **kwargs)

def FaultmodelEnthalpysensoroffsetReturnair(idf, **kwargs: Unpack[FaultmodelEnthalpysensoroffsetReturnairType]):
    """"helper for FaultmodelEnthalpysensoroffsetReturnair"""
    return idf.newidfobject('FAULTMODEL:ENTHALPYSENSOROFFSET:RETURNAIR', **kwargs)

def FaultmodelFoulingAirfilter(idf, **kwargs: Unpack[FaultmodelFoulingAirfilterType]):
    """"helper for FaultmodelFoulingAirfilter"""
    return idf.newidfobject('FAULTMODEL:FOULING:AIRFILTER', **kwargs)

def FaultmodelFoulingBoiler(idf, **kwargs: Unpack[FaultmodelFoulingBoilerType]):
    """"helper for FaultmodelFoulingBoiler"""
    return idf.newidfobject('FAULTMODEL:FOULING:BOILER', **kwargs)

def FaultmodelFoulingChiller(idf, **kwargs: Unpack[FaultmodelFoulingChillerType]):
    """"helper for FaultmodelFoulingChiller"""
    return idf.newidfobject('FAULTMODEL:FOULING:CHILLER', **kwargs)

def FaultmodelFoulingCoil(idf, **kwargs: Unpack[FaultmodelFoulingCoilType]):
    """"helper for FaultmodelFoulingCoil"""
    return idf.newidfobject('FAULTMODEL:FOULING:COIL', **kwargs)

def FaultmodelFoulingCoolingtower(idf, **kwargs: Unpack[FaultmodelFoulingCoolingtowerType]):
    """"helper for FaultmodelFoulingCoolingtower"""
    return idf.newidfobject('FAULTMODEL:FOULING:COOLINGTOWER', **kwargs)

def FaultmodelFoulingEvaporativecooler(idf, **kwargs: Unpack[FaultmodelFoulingEvaporativecoolerType]):
    """"helper for FaultmodelFoulingEvaporativecooler"""
    return idf.newidfobject('FAULTMODEL:FOULING:EVAPORATIVECOOLER', **kwargs)

def FaultmodelHumidistatoffset(idf, **kwargs: Unpack[FaultmodelHumidistatoffsetType]):
    """"helper for FaultmodelHumidistatoffset"""
    return idf.newidfobject('FAULTMODEL:HUMIDISTATOFFSET', **kwargs)

def FaultmodelHumiditysensoroffsetOutdoorair(idf, **kwargs: Unpack[FaultmodelHumiditysensoroffsetOutdoorairType]):
    """"helper for FaultmodelHumiditysensoroffsetOutdoorair"""
    return idf.newidfobject('FAULTMODEL:HUMIDITYSENSOROFFSET:OUTDOORAIR', **kwargs)

def FaultmodelTemperaturesensoroffsetChillersupplywater(idf, **kwargs: Unpack[FaultmodelTemperaturesensoroffsetChillersupplywaterType]):
    """"helper for FaultmodelTemperaturesensoroffsetChillersupplywater"""
    return idf.newidfobject('FAULTMODEL:TEMPERATURESENSOROFFSET:CHILLERSUPPLYWATER', **kwargs)

def FaultmodelTemperaturesensoroffsetCoilsupplyair(idf, **kwargs: Unpack[FaultmodelTemperaturesensoroffsetCoilsupplyairType]):
    """"helper for FaultmodelTemperaturesensoroffsetCoilsupplyair"""
    return idf.newidfobject('FAULTMODEL:TEMPERATURESENSOROFFSET:COILSUPPLYAIR', **kwargs)

def FaultmodelTemperaturesensoroffsetCondensersupplywater(idf, **kwargs: Unpack[FaultmodelTemperaturesensoroffsetCondensersupplywaterType]):
    """"helper for FaultmodelTemperaturesensoroffsetCondensersupplywater"""
    return idf.newidfobject('FAULTMODEL:TEMPERATURESENSOROFFSET:CONDENSERSUPPLYWATER', **kwargs)

def FaultmodelTemperaturesensoroffsetOutdoorair(idf, **kwargs: Unpack[FaultmodelTemperaturesensoroffsetOutdoorairType]):
    """"helper for FaultmodelTemperaturesensoroffsetOutdoorair"""
    return idf.newidfobject('FAULTMODEL:TEMPERATURESENSOROFFSET:OUTDOORAIR', **kwargs)

def FaultmodelTemperaturesensoroffsetReturnair(idf, **kwargs: Unpack[FaultmodelTemperaturesensoroffsetReturnairType]):
    """"helper for FaultmodelTemperaturesensoroffsetReturnair"""
    return idf.newidfobject('FAULTMODEL:TEMPERATURESENSOROFFSET:RETURNAIR', **kwargs)

def FaultmodelThermostatoffset(idf, **kwargs: Unpack[FaultmodelThermostatoffsetType]):
    """"helper for FaultmodelThermostatoffset"""
    return idf.newidfobject('FAULTMODEL:THERMOSTATOFFSET', **kwargs)

def FenestrationsurfaceDetailed(idf, **kwargs: Unpack[FenestrationsurfaceDetailedType]):
    """"helper for FenestrationsurfaceDetailed"""
    return idf.newidfobject('FENESTRATIONSURFACE:DETAILED', **kwargs)

def FloorAdiabatic(idf, **kwargs: Unpack[FloorAdiabaticType]):
    """"helper for FloorAdiabatic"""
    return idf.newidfobject('FLOOR:ADIABATIC', **kwargs)

def FloorDetailed(idf, **kwargs: Unpack[FloorDetailedType]):
    """"helper for FloorDetailed"""
    return idf.newidfobject('FLOOR:DETAILED', **kwargs)

def FloorGroundcontact(idf, **kwargs: Unpack[FloorGroundcontactType]):
    """"helper for FloorGroundcontact"""
    return idf.newidfobject('FLOOR:GROUNDCONTACT', **kwargs)

def FloorInterzone(idf, **kwargs: Unpack[FloorInterzoneType]):
    """"helper for FloorInterzone"""
    return idf.newidfobject('FLOOR:INTERZONE', **kwargs)

def FluidcoolerSinglespeed(idf, **kwargs: Unpack[FluidcoolerSinglespeedType]):
    """"helper for FluidcoolerSinglespeed"""
    return idf.newidfobject('FLUIDCOOLER:SINGLESPEED', **kwargs)

def FluidcoolerTwospeed(idf, **kwargs: Unpack[FluidcoolerTwospeedType]):
    """"helper for FluidcoolerTwospeed"""
    return idf.newidfobject('FLUIDCOOLER:TWOSPEED', **kwargs)

def FluidpropertiesConcentration(idf, **kwargs: Unpack[FluidpropertiesConcentrationType]):
    """"helper for FluidpropertiesConcentration"""
    return idf.newidfobject('FLUIDPROPERTIES:CONCENTRATION', **kwargs)

def FluidpropertiesGlycolconcentration(idf, **kwargs: Unpack[FluidpropertiesGlycolconcentrationType]):
    """"helper for FluidpropertiesGlycolconcentration"""
    return idf.newidfobject('FLUIDPROPERTIES:GLYCOLCONCENTRATION', **kwargs)

def FluidpropertiesName(idf, **kwargs: Unpack[FluidpropertiesNameType]):
    """"helper for FluidpropertiesName"""
    return idf.newidfobject('FLUIDPROPERTIES:NAME', **kwargs)

def FluidpropertiesSaturated(idf, **kwargs: Unpack[FluidpropertiesSaturatedType]):
    """"helper for FluidpropertiesSaturated"""
    return idf.newidfobject('FLUIDPROPERTIES:SATURATED', **kwargs)

def FluidpropertiesSuperheated(idf, **kwargs: Unpack[FluidpropertiesSuperheatedType]):
    """"helper for FluidpropertiesSuperheated"""
    return idf.newidfobject('FLUIDPROPERTIES:SUPERHEATED', **kwargs)

def FluidpropertiesTemperatures(idf, **kwargs: Unpack[FluidpropertiesTemperaturesType]):
    """"helper for FluidpropertiesTemperatures"""
    return idf.newidfobject('FLUIDPROPERTIES:TEMPERATURES', **kwargs)

def FoundationKiva(idf, **kwargs: Unpack[FoundationKivaType]):
    """"helper for FoundationKiva"""
    return idf.newidfobject('FOUNDATION:KIVA', **kwargs)

def FoundationKivaSettings(idf, **kwargs: Unpack[FoundationKivaSettingsType]):
    """"helper for FoundationKivaSettings"""
    return idf.newidfobject('FOUNDATION:KIVA:SETTINGS', **kwargs)

def Fuelfactors(idf, **kwargs: Unpack[FuelfactorsType]):
    """"helper for Fuelfactors"""
    return idf.newidfobject('FUELFACTORS', **kwargs)

def Gasequipment(idf, **kwargs: Unpack[GasequipmentType]):
    """"helper for Gasequipment"""
    return idf.newidfobject('GASEQUIPMENT', **kwargs)

def GeneratorCombustionturbine(idf, **kwargs: Unpack[GeneratorCombustionturbineType]):
    """"helper for GeneratorCombustionturbine"""
    return idf.newidfobject('GENERATOR:COMBUSTIONTURBINE', **kwargs)

def GeneratorFuelcell(idf, **kwargs: Unpack[GeneratorFuelcellType]):
    """"helper for GeneratorFuelcell"""
    return idf.newidfobject('GENERATOR:FUELCELL', **kwargs)

def GeneratorFuelcellAirsupply(idf, **kwargs: Unpack[GeneratorFuelcellAirsupplyType]):
    """"helper for GeneratorFuelcellAirsupply"""
    return idf.newidfobject('GENERATOR:FUELCELL:AIRSUPPLY', **kwargs)

def GeneratorFuelcellAuxiliaryheater(idf, **kwargs: Unpack[GeneratorFuelcellAuxiliaryheaterType]):
    """"helper for GeneratorFuelcellAuxiliaryheater"""
    return idf.newidfobject('GENERATOR:FUELCELL:AUXILIARYHEATER', **kwargs)

def GeneratorFuelcellElectricalstorage(idf, **kwargs: Unpack[GeneratorFuelcellElectricalstorageType]):
    """"helper for GeneratorFuelcellElectricalstorage"""
    return idf.newidfobject('GENERATOR:FUELCELL:ELECTRICALSTORAGE', **kwargs)

def GeneratorFuelcellExhaustgastowaterheatexchanger(idf, **kwargs: Unpack[GeneratorFuelcellExhaustgastowaterheatexchangerType]):
    """"helper for GeneratorFuelcellExhaustgastowaterheatexchanger"""
    return idf.newidfobject('GENERATOR:FUELCELL:EXHAUSTGASTOWATERHEATEXCHANGER', **kwargs)

def GeneratorFuelcellInverter(idf, **kwargs: Unpack[GeneratorFuelcellInverterType]):
    """"helper for GeneratorFuelcellInverter"""
    return idf.newidfobject('GENERATOR:FUELCELL:INVERTER', **kwargs)

def GeneratorFuelcellPowermodule(idf, **kwargs: Unpack[GeneratorFuelcellPowermoduleType]):
    """"helper for GeneratorFuelcellPowermodule"""
    return idf.newidfobject('GENERATOR:FUELCELL:POWERMODULE', **kwargs)

def GeneratorFuelcellStackcooler(idf, **kwargs: Unpack[GeneratorFuelcellStackcoolerType]):
    """"helper for GeneratorFuelcellStackcooler"""
    return idf.newidfobject('GENERATOR:FUELCELL:STACKCOOLER', **kwargs)

def GeneratorFuelcellWatersupply(idf, **kwargs: Unpack[GeneratorFuelcellWatersupplyType]):
    """"helper for GeneratorFuelcellWatersupply"""
    return idf.newidfobject('GENERATOR:FUELCELL:WATERSUPPLY', **kwargs)

def GeneratorFuelsupply(idf, **kwargs: Unpack[GeneratorFuelsupplyType]):
    """"helper for GeneratorFuelsupply"""
    return idf.newidfobject('GENERATOR:FUELSUPPLY', **kwargs)

def GeneratorInternalcombustionengine(idf, **kwargs: Unpack[GeneratorInternalcombustionengineType]):
    """"helper for GeneratorInternalcombustionengine"""
    return idf.newidfobject('GENERATOR:INTERNALCOMBUSTIONENGINE', **kwargs)

def GeneratorMicrochp(idf, **kwargs: Unpack[GeneratorMicrochpType]):
    """"helper for GeneratorMicrochp"""
    return idf.newidfobject('GENERATOR:MICROCHP', **kwargs)

def GeneratorMicrochpNonnormalizedparameters(idf, **kwargs: Unpack[GeneratorMicrochpNonnormalizedparametersType]):
    """"helper for GeneratorMicrochpNonnormalizedparameters"""
    return idf.newidfobject('GENERATOR:MICROCHP:NONNORMALIZEDPARAMETERS', **kwargs)

def GeneratorMicroturbine(idf, **kwargs: Unpack[GeneratorMicroturbineType]):
    """"helper for GeneratorMicroturbine"""
    return idf.newidfobject('GENERATOR:MICROTURBINE', **kwargs)

def GeneratorPhotovoltaic(idf, **kwargs: Unpack[GeneratorPhotovoltaicType]):
    """"helper for GeneratorPhotovoltaic"""
    return idf.newidfobject('GENERATOR:PHOTOVOLTAIC', **kwargs)

def GeneratorPvwatts(idf, **kwargs: Unpack[GeneratorPvwattsType]):
    """"helper for GeneratorPvwatts"""
    return idf.newidfobject('GENERATOR:PVWATTS', **kwargs)

def GeneratorWindturbine(idf, **kwargs: Unpack[GeneratorWindturbineType]):
    """"helper for GeneratorWindturbine"""
    return idf.newidfobject('GENERATOR:WINDTURBINE', **kwargs)

def Geometrytransform(idf, **kwargs: Unpack[GeometrytransformType]):
    """"helper for Geometrytransform"""
    return idf.newidfobject('GEOMETRYTRANSFORM', **kwargs)

def Glazeddoor(idf, **kwargs: Unpack[GlazeddoorType]):
    """"helper for Glazeddoor"""
    return idf.newidfobject('GLAZEDDOOR', **kwargs)

def GlazeddoorInterzone(idf, **kwargs: Unpack[GlazeddoorInterzoneType]):
    """"helper for GlazeddoorInterzone"""
    return idf.newidfobject('GLAZEDDOOR:INTERZONE', **kwargs)

def Globalgeometryrules(idf, **kwargs: Unpack[GlobalgeometryrulesType]):
    """"helper for Globalgeometryrules"""
    return idf.newidfobject('GLOBALGEOMETRYRULES', **kwargs)

def GroundheatexchangerHorizontaltrench(idf, **kwargs: Unpack[GroundheatexchangerHorizontaltrenchType]):
    """"helper for GroundheatexchangerHorizontaltrench"""
    return idf.newidfobject('GROUNDHEATEXCHANGER:HORIZONTALTRENCH', **kwargs)

def GroundheatexchangerPond(idf, **kwargs: Unpack[GroundheatexchangerPondType]):
    """"helper for GroundheatexchangerPond"""
    return idf.newidfobject('GROUNDHEATEXCHANGER:POND', **kwargs)

def GroundheatexchangerResponsefactors(idf, **kwargs: Unpack[GroundheatexchangerResponsefactorsType]):
    """"helper for GroundheatexchangerResponsefactors"""
    return idf.newidfobject('GROUNDHEATEXCHANGER:RESPONSEFACTORS', **kwargs)

def GroundheatexchangerSlinky(idf, **kwargs: Unpack[GroundheatexchangerSlinkyType]):
    """"helper for GroundheatexchangerSlinky"""
    return idf.newidfobject('GROUNDHEATEXCHANGER:SLINKY', **kwargs)

def GroundheatexchangerSurface(idf, **kwargs: Unpack[GroundheatexchangerSurfaceType]):
    """"helper for GroundheatexchangerSurface"""
    return idf.newidfobject('GROUNDHEATEXCHANGER:SURFACE', **kwargs)

def GroundheatexchangerSystem(idf, **kwargs: Unpack[GroundheatexchangerSystemType]):
    """"helper for GroundheatexchangerSystem"""
    return idf.newidfobject('GROUNDHEATEXCHANGER:SYSTEM', **kwargs)

def GroundheatexchangerVerticalArray(idf, **kwargs: Unpack[GroundheatexchangerVerticalArrayType]):
    """"helper for GroundheatexchangerVerticalArray"""
    return idf.newidfobject('GROUNDHEATEXCHANGER:VERTICAL:ARRAY', **kwargs)

def GroundheatexchangerVerticalProperties(idf, **kwargs: Unpack[GroundheatexchangerVerticalPropertiesType]):
    """"helper for GroundheatexchangerVerticalProperties"""
    return idf.newidfobject('GROUNDHEATEXCHANGER:VERTICAL:PROPERTIES', **kwargs)

def GroundheatexchangerVerticalSingle(idf, **kwargs: Unpack[GroundheatexchangerVerticalSingleType]):
    """"helper for GroundheatexchangerVerticalSingle"""
    return idf.newidfobject('GROUNDHEATEXCHANGER:VERTICAL:SINGLE', **kwargs)

def GroundheattransferBasementAutogrid(idf, **kwargs: Unpack[GroundheattransferBasementAutogridType]):
    """"helper for GroundheattransferBasementAutogrid"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:AUTOGRID', **kwargs)

def GroundheattransferBasementBldgdata(idf, **kwargs: Unpack[GroundheattransferBasementBldgdataType]):
    """"helper for GroundheattransferBasementBldgdata"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:BLDGDATA', **kwargs)

def GroundheattransferBasementCombldg(idf, **kwargs: Unpack[GroundheattransferBasementCombldgType]):
    """"helper for GroundheattransferBasementCombldg"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:COMBLDG', **kwargs)

def GroundheattransferBasementEquivautogrid(idf, **kwargs: Unpack[GroundheattransferBasementEquivautogridType]):
    """"helper for GroundheattransferBasementEquivautogrid"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:EQUIVAUTOGRID', **kwargs)

def GroundheattransferBasementEquivslab(idf, **kwargs: Unpack[GroundheattransferBasementEquivslabType]):
    """"helper for GroundheattransferBasementEquivslab"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:EQUIVSLAB', **kwargs)

def GroundheattransferBasementInsulation(idf, **kwargs: Unpack[GroundheattransferBasementInsulationType]):
    """"helper for GroundheattransferBasementInsulation"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:INSULATION', **kwargs)

def GroundheattransferBasementInterior(idf, **kwargs: Unpack[GroundheattransferBasementInteriorType]):
    """"helper for GroundheattransferBasementInterior"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:INTERIOR', **kwargs)

def GroundheattransferBasementManualgrid(idf, **kwargs: Unpack[GroundheattransferBasementManualgridType]):
    """"helper for GroundheattransferBasementManualgrid"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:MANUALGRID', **kwargs)

def GroundheattransferBasementMatlprops(idf, **kwargs: Unpack[GroundheattransferBasementMatlpropsType]):
    """"helper for GroundheattransferBasementMatlprops"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:MATLPROPS', **kwargs)

def GroundheattransferBasementSimparameters(idf, **kwargs: Unpack[GroundheattransferBasementSimparametersType]):
    """"helper for GroundheattransferBasementSimparameters"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:SIMPARAMETERS', **kwargs)

def GroundheattransferBasementSurfaceprops(idf, **kwargs: Unpack[GroundheattransferBasementSurfacepropsType]):
    """"helper for GroundheattransferBasementSurfaceprops"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:SURFACEPROPS', **kwargs)

def GroundheattransferBasementXface(idf, **kwargs: Unpack[GroundheattransferBasementXfaceType]):
    """"helper for GroundheattransferBasementXface"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:XFACE', **kwargs)

def GroundheattransferBasementYface(idf, **kwargs: Unpack[GroundheattransferBasementYfaceType]):
    """"helper for GroundheattransferBasementYface"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:YFACE', **kwargs)

def GroundheattransferBasementZface(idf, **kwargs: Unpack[GroundheattransferBasementZfaceType]):
    """"helper for GroundheattransferBasementZface"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:ZFACE', **kwargs)

def GroundheattransferControl(idf, **kwargs: Unpack[GroundheattransferControlType]):
    """"helper for GroundheattransferControl"""
    return idf.newidfobject('GROUNDHEATTRANSFER:CONTROL', **kwargs)

def GroundheattransferSlabAutogrid(idf, **kwargs: Unpack[GroundheattransferSlabAutogridType]):
    """"helper for GroundheattransferSlabAutogrid"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:AUTOGRID', **kwargs)

def GroundheattransferSlabBldgprops(idf, **kwargs: Unpack[GroundheattransferSlabBldgpropsType]):
    """"helper for GroundheattransferSlabBldgprops"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:BLDGPROPS', **kwargs)

def GroundheattransferSlabBoundconds(idf, **kwargs: Unpack[GroundheattransferSlabBoundcondsType]):
    """"helper for GroundheattransferSlabBoundconds"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:BOUNDCONDS', **kwargs)

def GroundheattransferSlabEquivalentslab(idf, **kwargs: Unpack[GroundheattransferSlabEquivalentslabType]):
    """"helper for GroundheattransferSlabEquivalentslab"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:EQUIVALENTSLAB', **kwargs)

def GroundheattransferSlabInsulation(idf, **kwargs: Unpack[GroundheattransferSlabInsulationType]):
    """"helper for GroundheattransferSlabInsulation"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:INSULATION', **kwargs)

def GroundheattransferSlabManualgrid(idf, **kwargs: Unpack[GroundheattransferSlabManualgridType]):
    """"helper for GroundheattransferSlabManualgrid"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:MANUALGRID', **kwargs)

def GroundheattransferSlabMaterials(idf, **kwargs: Unpack[GroundheattransferSlabMaterialsType]):
    """"helper for GroundheattransferSlabMaterials"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:MATERIALS', **kwargs)

def GroundheattransferSlabMatlprops(idf, **kwargs: Unpack[GroundheattransferSlabMatlpropsType]):
    """"helper for GroundheattransferSlabMatlprops"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:MATLPROPS', **kwargs)

def GroundheattransferSlabXface(idf, **kwargs: Unpack[GroundheattransferSlabXfaceType]):
    """"helper for GroundheattransferSlabXface"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:XFACE', **kwargs)

def GroundheattransferSlabYface(idf, **kwargs: Unpack[GroundheattransferSlabYfaceType]):
    """"helper for GroundheattransferSlabYface"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:YFACE', **kwargs)

def GroundheattransferSlabZface(idf, **kwargs: Unpack[GroundheattransferSlabZfaceType]):
    """"helper for GroundheattransferSlabZface"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:ZFACE', **kwargs)

def HeaderedpumpsConstantspeed(idf, **kwargs: Unpack[HeaderedpumpsConstantspeedType]):
    """"helper for HeaderedpumpsConstantspeed"""
    return idf.newidfobject('HEADEREDPUMPS:CONSTANTSPEED', **kwargs)

def HeaderedpumpsVariablespeed(idf, **kwargs: Unpack[HeaderedpumpsVariablespeedType]):
    """"helper for HeaderedpumpsVariablespeed"""
    return idf.newidfobject('HEADEREDPUMPS:VARIABLESPEED', **kwargs)

def Heatbalancealgorithm(idf, **kwargs: Unpack[HeatbalancealgorithmType]):
    """"helper for Heatbalancealgorithm"""
    return idf.newidfobject('HEATBALANCEALGORITHM', **kwargs)

def HeatbalancesettingsConductionfinitedifference(idf, **kwargs: Unpack[HeatbalancesettingsConductionfinitedifferenceType]):
    """"helper for HeatbalancesettingsConductionfinitedifference"""
    return idf.newidfobject('HEATBALANCESETTINGS:CONDUCTIONFINITEDIFFERENCE', **kwargs)

def HeatexchangerAirtoairFlatplate(idf, **kwargs: Unpack[HeatexchangerAirtoairFlatplateType]):
    """"helper for HeatexchangerAirtoairFlatplate"""
    return idf.newidfobject('HEATEXCHANGER:AIRTOAIR:FLATPLATE', **kwargs)

def HeatexchangerAirtoairSensibleandlatent(idf, **kwargs: Unpack[HeatexchangerAirtoairSensibleandlatentType]):
    """"helper for HeatexchangerAirtoairSensibleandlatent"""
    return idf.newidfobject('HEATEXCHANGER:AIRTOAIR:SENSIBLEANDLATENT', **kwargs)

def HeatexchangerDesiccantBalancedflow(idf, **kwargs: Unpack[HeatexchangerDesiccantBalancedflowType]):
    """"helper for HeatexchangerDesiccantBalancedflow"""
    return idf.newidfobject('HEATEXCHANGER:DESICCANT:BALANCEDFLOW', **kwargs)

def HeatexchangerDesiccantBalancedflowPerformancedatatype1(idf, **kwargs: Unpack[HeatexchangerDesiccantBalancedflowPerformancedatatype1Type]):
    """"helper for HeatexchangerDesiccantBalancedflowPerformancedatatype1"""
    return idf.newidfobject('HEATEXCHANGER:DESICCANT:BALANCEDFLOW:PERFORMANCEDATATYPE1', **kwargs)

def HeatexchangerFluidtofluid(idf, **kwargs: Unpack[HeatexchangerFluidtofluidType]):
    """"helper for HeatexchangerFluidtofluid"""
    return idf.newidfobject('HEATEXCHANGER:FLUIDTOFLUID', **kwargs)

def HeatpumpAirtowaterFuelfiredCooling(idf, **kwargs: Unpack[HeatpumpAirtowaterFuelfiredCoolingType]):
    """"helper for HeatpumpAirtowaterFuelfiredCooling"""
    return idf.newidfobject('HEATPUMP:AIRTOWATER:FUELFIRED:COOLING', **kwargs)

def HeatpumpAirtowaterFuelfiredHeating(idf, **kwargs: Unpack[HeatpumpAirtowaterFuelfiredHeatingType]):
    """"helper for HeatpumpAirtowaterFuelfiredHeating"""
    return idf.newidfobject('HEATPUMP:AIRTOWATER:FUELFIRED:HEATING', **kwargs)

def HeatpumpPlantloopEirCooling(idf, **kwargs: Unpack[HeatpumpPlantloopEirCoolingType]):
    """"helper for HeatpumpPlantloopEirCooling"""
    return idf.newidfobject('HEATPUMP:PLANTLOOP:EIR:COOLING', **kwargs)

def HeatpumpPlantloopEirHeating(idf, **kwargs: Unpack[HeatpumpPlantloopEirHeatingType]):
    """"helper for HeatpumpPlantloopEirHeating"""
    return idf.newidfobject('HEATPUMP:PLANTLOOP:EIR:HEATING', **kwargs)

def HeatpumpWatertowaterEquationfitCooling(idf, **kwargs: Unpack[HeatpumpWatertowaterEquationfitCoolingType]):
    """"helper for HeatpumpWatertowaterEquationfitCooling"""
    return idf.newidfobject('HEATPUMP:WATERTOWATER:EQUATIONFIT:COOLING', **kwargs)

def HeatpumpWatertowaterEquationfitHeating(idf, **kwargs: Unpack[HeatpumpWatertowaterEquationfitHeatingType]):
    """"helper for HeatpumpWatertowaterEquationfitHeating"""
    return idf.newidfobject('HEATPUMP:WATERTOWATER:EQUATIONFIT:HEATING', **kwargs)

def HeatpumpWatertowaterParameterestimationCooling(idf, **kwargs: Unpack[HeatpumpWatertowaterParameterestimationCoolingType]):
    """"helper for HeatpumpWatertowaterParameterestimationCooling"""
    return idf.newidfobject('HEATPUMP:WATERTOWATER:PARAMETERESTIMATION:COOLING', **kwargs)

def HeatpumpWatertowaterParameterestimationHeating(idf, **kwargs: Unpack[HeatpumpWatertowaterParameterestimationHeatingType]):
    """"helper for HeatpumpWatertowaterParameterestimationHeating"""
    return idf.newidfobject('HEATPUMP:WATERTOWATER:PARAMETERESTIMATION:HEATING', **kwargs)

def Hotwaterequipment(idf, **kwargs: Unpack[HotwaterequipmentType]):
    """"helper for Hotwaterequipment"""
    return idf.newidfobject('HOTWATEREQUIPMENT', **kwargs)

def HumidifierSteamElectric(idf, **kwargs: Unpack[HumidifierSteamElectricType]):
    """"helper for HumidifierSteamElectric"""
    return idf.newidfobject('HUMIDIFIER:STEAM:ELECTRIC', **kwargs)

def HumidifierSteamGas(idf, **kwargs: Unpack[HumidifierSteamGasType]):
    """"helper for HumidifierSteamGas"""
    return idf.newidfobject('HUMIDIFIER:STEAM:GAS', **kwargs)

def Hvacsystemrootfindingalgorithm(idf, **kwargs: Unpack[HvacsystemrootfindingalgorithmType]):
    """"helper for Hvacsystemrootfindingalgorithm"""
    return idf.newidfobject('HVACSYSTEMROOTFINDINGALGORITHM', **kwargs)

def HvactemplatePlantBoiler(idf, **kwargs: Unpack[HvactemplatePlantBoilerType]):
    """"helper for HvactemplatePlantBoiler"""
    return idf.newidfobject('HVACTEMPLATE:PLANT:BOILER', **kwargs)

def HvactemplatePlantBoilerObjectreference(idf, **kwargs: Unpack[HvactemplatePlantBoilerObjectreferenceType]):
    """"helper for HvactemplatePlantBoilerObjectreference"""
    return idf.newidfobject('HVACTEMPLATE:PLANT:BOILER:OBJECTREFERENCE', **kwargs)

def HvactemplatePlantChilledwaterloop(idf, **kwargs: Unpack[HvactemplatePlantChilledwaterloopType]):
    """"helper for HvactemplatePlantChilledwaterloop"""
    return idf.newidfobject('HVACTEMPLATE:PLANT:CHILLEDWATERLOOP', **kwargs)

def HvactemplatePlantChiller(idf, **kwargs: Unpack[HvactemplatePlantChillerType]):
    """"helper for HvactemplatePlantChiller"""
    return idf.newidfobject('HVACTEMPLATE:PLANT:CHILLER', **kwargs)

def HvactemplatePlantChillerObjectreference(idf, **kwargs: Unpack[HvactemplatePlantChillerObjectreferenceType]):
    """"helper for HvactemplatePlantChillerObjectreference"""
    return idf.newidfobject('HVACTEMPLATE:PLANT:CHILLER:OBJECTREFERENCE', **kwargs)

def HvactemplatePlantHotwaterloop(idf, **kwargs: Unpack[HvactemplatePlantHotwaterloopType]):
    """"helper for HvactemplatePlantHotwaterloop"""
    return idf.newidfobject('HVACTEMPLATE:PLANT:HOTWATERLOOP', **kwargs)

def HvactemplatePlantMixedwaterloop(idf, **kwargs: Unpack[HvactemplatePlantMixedwaterloopType]):
    """"helper for HvactemplatePlantMixedwaterloop"""
    return idf.newidfobject('HVACTEMPLATE:PLANT:MIXEDWATERLOOP', **kwargs)

def HvactemplatePlantTower(idf, **kwargs: Unpack[HvactemplatePlantTowerType]):
    """"helper for HvactemplatePlantTower"""
    return idf.newidfobject('HVACTEMPLATE:PLANT:TOWER', **kwargs)

def HvactemplatePlantTowerObjectreference(idf, **kwargs: Unpack[HvactemplatePlantTowerObjectreferenceType]):
    """"helper for HvactemplatePlantTowerObjectreference"""
    return idf.newidfobject('HVACTEMPLATE:PLANT:TOWER:OBJECTREFERENCE', **kwargs)

def HvactemplateSystemConstantvolume(idf, **kwargs: Unpack[HvactemplateSystemConstantvolumeType]):
    """"helper for HvactemplateSystemConstantvolume"""
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:CONSTANTVOLUME', **kwargs)

def HvactemplateSystemDedicatedoutdoorair(idf, **kwargs: Unpack[HvactemplateSystemDedicatedoutdoorairType]):
    """"helper for HvactemplateSystemDedicatedoutdoorair"""
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:DEDICATEDOUTDOORAIR', **kwargs)

def HvactemplateSystemDualduct(idf, **kwargs: Unpack[HvactemplateSystemDualductType]):
    """"helper for HvactemplateSystemDualduct"""
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:DUALDUCT', **kwargs)

def HvactemplateSystemPackagedvav(idf, **kwargs: Unpack[HvactemplateSystemPackagedvavType]):
    """"helper for HvactemplateSystemPackagedvav"""
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:PACKAGEDVAV', **kwargs)

def HvactemplateSystemUnitary(idf, **kwargs: Unpack[HvactemplateSystemUnitaryType]):
    """"helper for HvactemplateSystemUnitary"""
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:UNITARY', **kwargs)

def HvactemplateSystemUnitaryheatpumpAirtoair(idf, **kwargs: Unpack[HvactemplateSystemUnitaryheatpumpAirtoairType]):
    """"helper for HvactemplateSystemUnitaryheatpumpAirtoair"""
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:UNITARYHEATPUMP:AIRTOAIR', **kwargs)

def HvactemplateSystemUnitarysystem(idf, **kwargs: Unpack[HvactemplateSystemUnitarysystemType]):
    """"helper for HvactemplateSystemUnitarysystem"""
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:UNITARYSYSTEM', **kwargs)

def HvactemplateSystemVav(idf, **kwargs: Unpack[HvactemplateSystemVavType]):
    """"helper for HvactemplateSystemVav"""
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:VAV', **kwargs)

def HvactemplateSystemVrf(idf, **kwargs: Unpack[HvactemplateSystemVrfType]):
    """"helper for HvactemplateSystemVrf"""
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:VRF', **kwargs)

def HvactemplateThermostat(idf, **kwargs: Unpack[HvactemplateThermostatType]):
    """"helper for HvactemplateThermostat"""
    return idf.newidfobject('HVACTEMPLATE:THERMOSTAT', **kwargs)

def HvactemplateZoneBaseboardheat(idf, **kwargs: Unpack[HvactemplateZoneBaseboardheatType]):
    """"helper for HvactemplateZoneBaseboardheat"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:BASEBOARDHEAT', **kwargs)

def HvactemplateZoneConstantvolume(idf, **kwargs: Unpack[HvactemplateZoneConstantvolumeType]):
    """"helper for HvactemplateZoneConstantvolume"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:CONSTANTVOLUME', **kwargs)

def HvactemplateZoneDualduct(idf, **kwargs: Unpack[HvactemplateZoneDualductType]):
    """"helper for HvactemplateZoneDualduct"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:DUALDUCT', **kwargs)

def HvactemplateZoneFancoil(idf, **kwargs: Unpack[HvactemplateZoneFancoilType]):
    """"helper for HvactemplateZoneFancoil"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:FANCOIL', **kwargs)

def HvactemplateZoneIdealloadsairsystem(idf, **kwargs: Unpack[HvactemplateZoneIdealloadsairsystemType]):
    """"helper for HvactemplateZoneIdealloadsairsystem"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:IDEALLOADSAIRSYSTEM', **kwargs)

def HvactemplateZonePtac(idf, **kwargs: Unpack[HvactemplateZonePtacType]):
    """"helper for HvactemplateZonePtac"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:PTAC', **kwargs)

def HvactemplateZonePthp(idf, **kwargs: Unpack[HvactemplateZonePthpType]):
    """"helper for HvactemplateZonePthp"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:PTHP', **kwargs)

def HvactemplateZoneUnitary(idf, **kwargs: Unpack[HvactemplateZoneUnitaryType]):
    """"helper for HvactemplateZoneUnitary"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:UNITARY', **kwargs)

def HvactemplateZoneVav(idf, **kwargs: Unpack[HvactemplateZoneVavType]):
    """"helper for HvactemplateZoneVav"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:VAV', **kwargs)

def HvactemplateZoneVavFanpowered(idf, **kwargs: Unpack[HvactemplateZoneVavFanpoweredType]):
    """"helper for HvactemplateZoneVavFanpowered"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:VAV:FANPOWERED', **kwargs)

def HvactemplateZoneVavHeatandcool(idf, **kwargs: Unpack[HvactemplateZoneVavHeatandcoolType]):
    """"helper for HvactemplateZoneVavHeatandcool"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:VAV:HEATANDCOOL', **kwargs)

def HvactemplateZoneVrf(idf, **kwargs: Unpack[HvactemplateZoneVrfType]):
    """"helper for HvactemplateZoneVrf"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:VRF', **kwargs)

def HvactemplateZoneWatertoairheatpump(idf, **kwargs: Unpack[HvactemplateZoneWatertoairheatpumpType]):
    """"helper for HvactemplateZoneWatertoairheatpump"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:WATERTOAIRHEATPUMP', **kwargs)

def HybridmodelZone(idf, **kwargs: Unpack[HybridmodelZoneType]):
    """"helper for HybridmodelZone"""
    return idf.newidfobject('HYBRIDMODEL:ZONE', **kwargs)

def Indoorlivingwall(idf, **kwargs: Unpack[IndoorlivingwallType]):
    """"helper for Indoorlivingwall"""
    return idf.newidfobject('INDOORLIVINGWALL', **kwargs)

def Internalmass(idf, **kwargs: Unpack[InternalmassType]):
    """"helper for Internalmass"""
    return idf.newidfobject('INTERNALMASS', **kwargs)

def LifecyclecostNonrecurringcost(idf, **kwargs: Unpack[LifecyclecostNonrecurringcostType]):
    """"helper for LifecyclecostNonrecurringcost"""
    return idf.newidfobject('LIFECYCLECOST:NONRECURRINGCOST', **kwargs)

def LifecyclecostParameters(idf, **kwargs: Unpack[LifecyclecostParametersType]):
    """"helper for LifecyclecostParameters"""
    return idf.newidfobject('LIFECYCLECOST:PARAMETERS', **kwargs)

def LifecyclecostRecurringcosts(idf, **kwargs: Unpack[LifecyclecostRecurringcostsType]):
    """"helper for LifecyclecostRecurringcosts"""
    return idf.newidfobject('LIFECYCLECOST:RECURRINGCOSTS', **kwargs)

def LifecyclecostUseadjustment(idf, **kwargs: Unpack[LifecyclecostUseadjustmentType]):
    """"helper for LifecyclecostUseadjustment"""
    return idf.newidfobject('LIFECYCLECOST:USEADJUSTMENT', **kwargs)

def LifecyclecostUsepriceescalation(idf, **kwargs: Unpack[LifecyclecostUsepriceescalationType]):
    """"helper for LifecyclecostUsepriceescalation"""
    return idf.newidfobject('LIFECYCLECOST:USEPRICEESCALATION', **kwargs)

def Lights(idf, **kwargs: Unpack[LightsType]):
    """"helper for Lights"""
    return idf.newidfobject('LIGHTS', **kwargs)

def LoadprofilePlant(idf, **kwargs: Unpack[LoadprofilePlantType]):
    """"helper for LoadprofilePlant"""
    return idf.newidfobject('LOADPROFILE:PLANT', **kwargs)

def Material(idf, **kwargs: Unpack[MaterialType]):
    """"helper for Material"""
    return idf.newidfobject('MATERIAL', **kwargs)

def MaterialAirgap(idf, **kwargs: Unpack[MaterialAirgapType]):
    """"helper for MaterialAirgap"""
    return idf.newidfobject('MATERIAL:AIRGAP', **kwargs)

def MaterialInfraredtransparent(idf, **kwargs: Unpack[MaterialInfraredtransparentType]):
    """"helper for MaterialInfraredtransparent"""
    return idf.newidfobject('MATERIAL:INFRAREDTRANSPARENT', **kwargs)

def MaterialNomass(idf, **kwargs: Unpack[MaterialNomassType]):
    """"helper for MaterialNomass"""
    return idf.newidfobject('MATERIAL:NOMASS', **kwargs)

def MaterialRoofvegetation(idf, **kwargs: Unpack[MaterialRoofvegetationType]):
    """"helper for MaterialRoofvegetation"""
    return idf.newidfobject('MATERIAL:ROOFVEGETATION', **kwargs)

def MaterialpropertyGlazingspectraldata(idf, **kwargs: Unpack[MaterialpropertyGlazingspectraldataType]):
    """"helper for MaterialpropertyGlazingspectraldata"""
    return idf.newidfobject('MATERIALPROPERTY:GLAZINGSPECTRALDATA', **kwargs)

def MaterialpropertyHeatandmoisturetransferDiffusion(idf, **kwargs: Unpack[MaterialpropertyHeatandmoisturetransferDiffusionType]):
    """"helper for MaterialpropertyHeatandmoisturetransferDiffusion"""
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:DIFFUSION', **kwargs)

def MaterialpropertyHeatandmoisturetransferRedistribution(idf, **kwargs: Unpack[MaterialpropertyHeatandmoisturetransferRedistributionType]):
    """"helper for MaterialpropertyHeatandmoisturetransferRedistribution"""
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:REDISTRIBUTION', **kwargs)

def MaterialpropertyHeatandmoisturetransferSettings(idf, **kwargs: Unpack[MaterialpropertyHeatandmoisturetransferSettingsType]):
    """"helper for MaterialpropertyHeatandmoisturetransferSettings"""
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:SETTINGS', **kwargs)

def MaterialpropertyHeatandmoisturetransferSorptionisotherm(idf, **kwargs: Unpack[MaterialpropertyHeatandmoisturetransferSorptionisothermType]):
    """"helper for MaterialpropertyHeatandmoisturetransferSorptionisotherm"""
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:SORPTIONISOTHERM', **kwargs)

def MaterialpropertyHeatandmoisturetransferSuction(idf, **kwargs: Unpack[MaterialpropertyHeatandmoisturetransferSuctionType]):
    """"helper for MaterialpropertyHeatandmoisturetransferSuction"""
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:SUCTION', **kwargs)

def MaterialpropertyHeatandmoisturetransferThermalconductivity(idf, **kwargs: Unpack[MaterialpropertyHeatandmoisturetransferThermalconductivityType]):
    """"helper for MaterialpropertyHeatandmoisturetransferThermalconductivity"""
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:THERMALCONDUCTIVITY', **kwargs)

def MaterialpropertyMoisturepenetrationdepthSettings(idf, **kwargs: Unpack[MaterialpropertyMoisturepenetrationdepthSettingsType]):
    """"helper for MaterialpropertyMoisturepenetrationdepthSettings"""
    return idf.newidfobject('MATERIALPROPERTY:MOISTUREPENETRATIONDEPTH:SETTINGS', **kwargs)

def MaterialpropertyPhasechange(idf, **kwargs: Unpack[MaterialpropertyPhasechangeType]):
    """"helper for MaterialpropertyPhasechange"""
    return idf.newidfobject('MATERIALPROPERTY:PHASECHANGE', **kwargs)

def MaterialpropertyPhasechangehysteresis(idf, **kwargs: Unpack[MaterialpropertyPhasechangehysteresisType]):
    """"helper for MaterialpropertyPhasechangehysteresis"""
    return idf.newidfobject('MATERIALPROPERTY:PHASECHANGEHYSTERESIS', **kwargs)

def MaterialpropertyVariableabsorptance(idf, **kwargs: Unpack[MaterialpropertyVariableabsorptanceType]):
    """"helper for MaterialpropertyVariableabsorptance"""
    return idf.newidfobject('MATERIALPROPERTY:VARIABLEABSORPTANCE', **kwargs)

def MaterialpropertyVariablethermalconductivity(idf, **kwargs: Unpack[MaterialpropertyVariablethermalconductivityType]):
    """"helper for MaterialpropertyVariablethermalconductivity"""
    return idf.newidfobject('MATERIALPROPERTY:VARIABLETHERMALCONDUCTIVITY', **kwargs)

def MatrixTwodimension(idf, **kwargs: Unpack[MatrixTwodimensionType]):
    """"helper for MatrixTwodimension"""
    return idf.newidfobject('MATRIX:TWODIMENSION', **kwargs)

def MeterCustom(idf, **kwargs: Unpack[MeterCustomType]):
    """"helper for MeterCustom"""
    return idf.newidfobject('METER:CUSTOM', **kwargs)

def MeterCustomdecrement(idf, **kwargs: Unpack[MeterCustomdecrementType]):
    """"helper for MeterCustomdecrement"""
    return idf.newidfobject('METER:CUSTOMDECREMENT', **kwargs)

def Nodelist(idf, **kwargs: Unpack[NodelistType]):
    """"helper for Nodelist"""
    return idf.newidfobject('NODELIST', **kwargs)

def Otherequipment(idf, **kwargs: Unpack[OtherequipmentType]):
    """"helper for Otherequipment"""
    return idf.newidfobject('OTHEREQUIPMENT', **kwargs)

def OutdoorairMixer(idf, **kwargs: Unpack[OutdoorairMixerType]):
    """"helper for OutdoorairMixer"""
    return idf.newidfobject('OUTDOORAIR:MIXER', **kwargs)

def OutdoorairNode(idf, **kwargs: Unpack[OutdoorairNodeType]):
    """"helper for OutdoorairNode"""
    return idf.newidfobject('OUTDOORAIR:NODE', **kwargs)

def OutdoorairNodelist(idf, **kwargs: Unpack[OutdoorairNodelistType]):
    """"helper for OutdoorairNodelist"""
    return idf.newidfobject('OUTDOORAIR:NODELIST', **kwargs)

def OutputConstructions(idf, **kwargs: Unpack[OutputConstructionsType]):
    """"helper for OutputConstructions"""
    return idf.newidfobject('OUTPUT:CONSTRUCTIONS', **kwargs)

def OutputDaylightfactors(idf, **kwargs: Unpack[OutputDaylightfactorsType]):
    """"helper for OutputDaylightfactors"""
    return idf.newidfobject('OUTPUT:DAYLIGHTFACTORS', **kwargs)

def OutputDebuggingdata(idf, **kwargs: Unpack[OutputDebuggingdataType]):
    """"helper for OutputDebuggingdata"""
    return idf.newidfobject('OUTPUT:DEBUGGINGDATA', **kwargs)

def OutputDiagnostics(idf, **kwargs: Unpack[OutputDiagnosticsType]):
    """"helper for OutputDiagnostics"""
    return idf.newidfobject('OUTPUT:DIAGNOSTICS', **kwargs)

def OutputEnergymanagementsystem(idf, **kwargs: Unpack[OutputEnergymanagementsystemType]):
    """"helper for OutputEnergymanagementsystem"""
    return idf.newidfobject('OUTPUT:ENERGYMANAGEMENTSYSTEM', **kwargs)

def OutputEnvironmentalimpactfactors(idf, **kwargs: Unpack[OutputEnvironmentalimpactfactorsType]):
    """"helper for OutputEnvironmentalimpactfactors"""
    return idf.newidfobject('OUTPUT:ENVIRONMENTALIMPACTFACTORS', **kwargs)

def OutputIlluminancemap(idf, **kwargs: Unpack[OutputIlluminancemapType]):
    """"helper for OutputIlluminancemap"""
    return idf.newidfobject('OUTPUT:ILLUMINANCEMAP', **kwargs)

def OutputJson(idf, **kwargs: Unpack[OutputJsonType]):
    """"helper for OutputJson"""
    return idf.newidfobject('OUTPUT:JSON', **kwargs)

def OutputMeter(idf, **kwargs: Unpack[OutputMeterType]):
    """"helper for OutputMeter"""
    return idf.newidfobject('OUTPUT:METER', **kwargs)

def OutputMeterCumulative(idf, **kwargs: Unpack[OutputMeterCumulativeType]):
    """"helper for OutputMeterCumulative"""
    return idf.newidfobject('OUTPUT:METER:CUMULATIVE', **kwargs)

def OutputMeterCumulativeMeterfileonly(idf, **kwargs: Unpack[OutputMeterCumulativeMeterfileonlyType]):
    """"helper for OutputMeterCumulativeMeterfileonly"""
    return idf.newidfobject('OUTPUT:METER:CUMULATIVE:METERFILEONLY', **kwargs)

def OutputMeterMeterfileonly(idf, **kwargs: Unpack[OutputMeterMeterfileonlyType]):
    """"helper for OutputMeterMeterfileonly"""
    return idf.newidfobject('OUTPUT:METER:METERFILEONLY', **kwargs)

def OutputPreprocessormessage(idf, **kwargs: Unpack[OutputPreprocessormessageType]):
    """"helper for OutputPreprocessormessage"""
    return idf.newidfobject('OUTPUT:PREPROCESSORMESSAGE', **kwargs)

def OutputSchedules(idf, **kwargs: Unpack[OutputSchedulesType]):
    """"helper for OutputSchedules"""
    return idf.newidfobject('OUTPUT:SCHEDULES', **kwargs)

def OutputSqlite(idf, **kwargs: Unpack[OutputSqliteType]):
    """"helper for OutputSqlite"""
    return idf.newidfobject('OUTPUT:SQLITE', **kwargs)

def OutputSurfacesDrawing(idf, **kwargs: Unpack[OutputSurfacesDrawingType]):
    """"helper for OutputSurfacesDrawing"""
    return idf.newidfobject('OUTPUT:SURFACES:DRAWING', **kwargs)

def OutputSurfacesList(idf, **kwargs: Unpack[OutputSurfacesListType]):
    """"helper for OutputSurfacesList"""
    return idf.newidfobject('OUTPUT:SURFACES:LIST', **kwargs)

def OutputTableAnnual(idf, **kwargs: Unpack[OutputTableAnnualType]):
    """"helper for OutputTableAnnual"""
    return idf.newidfobject('OUTPUT:TABLE:ANNUAL', **kwargs)

def OutputTableMonthly(idf, **kwargs: Unpack[OutputTableMonthlyType]):
    """"helper for OutputTableMonthly"""
    return idf.newidfobject('OUTPUT:TABLE:MONTHLY', **kwargs)

def OutputTableReportperiod(idf, **kwargs: Unpack[OutputTableReportperiodType]):
    """"helper for OutputTableReportperiod"""
    return idf.newidfobject('OUTPUT:TABLE:REPORTPERIOD', **kwargs)

def OutputTableSummaryreports(idf, **kwargs: Unpack[OutputTableSummaryreportsType]):
    """"helper for OutputTableSummaryreports"""
    return idf.newidfobject('OUTPUT:TABLE:SUMMARYREPORTS', **kwargs)

def OutputTableTimebins(idf, **kwargs: Unpack[OutputTableTimebinsType]):
    """"helper for OutputTableTimebins"""
    return idf.newidfobject('OUTPUT:TABLE:TIMEBINS', **kwargs)

def OutputVariable(idf, **kwargs: Unpack[OutputVariableType]):
    """"helper for OutputVariable"""
    return idf.newidfobject('OUTPUT:VARIABLE', **kwargs)

def OutputVariabledictionary(idf, **kwargs: Unpack[OutputVariabledictionaryType]):
    """"helper for OutputVariabledictionary"""
    return idf.newidfobject('OUTPUT:VARIABLEDICTIONARY', **kwargs)

def OutputcontrolFiles(idf, **kwargs: Unpack[OutputcontrolFilesType]):
    """"helper for OutputcontrolFiles"""
    return idf.newidfobject('OUTPUTCONTROL:FILES', **kwargs)

def OutputcontrolIlluminancemapStyle(idf, **kwargs: Unpack[OutputcontrolIlluminancemapStyleType]):
    """"helper for OutputcontrolIlluminancemapStyle"""
    return idf.newidfobject('OUTPUTCONTROL:ILLUMINANCEMAP:STYLE', **kwargs)

def OutputcontrolReportingtolerances(idf, **kwargs: Unpack[OutputcontrolReportingtolerancesType]):
    """"helper for OutputcontrolReportingtolerances"""
    return idf.newidfobject('OUTPUTCONTROL:REPORTINGTOLERANCES', **kwargs)

def OutputcontrolSizingStyle(idf, **kwargs: Unpack[OutputcontrolSizingStyleType]):
    """"helper for OutputcontrolSizingStyle"""
    return idf.newidfobject('OUTPUTCONTROL:SIZING:STYLE', **kwargs)

def OutputcontrolSurfacecolorscheme(idf, **kwargs: Unpack[OutputcontrolSurfacecolorschemeType]):
    """"helper for OutputcontrolSurfacecolorscheme"""
    return idf.newidfobject('OUTPUTCONTROL:SURFACECOLORSCHEME', **kwargs)

def OutputcontrolTableStyle(idf, **kwargs: Unpack[OutputcontrolTableStyleType]):
    """"helper for OutputcontrolTableStyle"""
    return idf.newidfobject('OUTPUTCONTROL:TABLE:STYLE', **kwargs)

def OutputcontrolTimestamp(idf, **kwargs: Unpack[OutputcontrolTimestampType]):
    """"helper for OutputcontrolTimestamp"""
    return idf.newidfobject('OUTPUTCONTROL:TIMESTAMP', **kwargs)

def ParametricFilenamesuffix(idf, **kwargs: Unpack[ParametricFilenamesuffixType]):
    """"helper for ParametricFilenamesuffix"""
    return idf.newidfobject('PARAMETRIC:FILENAMESUFFIX', **kwargs)

def ParametricLogic(idf, **kwargs: Unpack[ParametricLogicType]):
    """"helper for ParametricLogic"""
    return idf.newidfobject('PARAMETRIC:LOGIC', **kwargs)

def ParametricRuncontrol(idf, **kwargs: Unpack[ParametricRuncontrolType]):
    """"helper for ParametricRuncontrol"""
    return idf.newidfobject('PARAMETRIC:RUNCONTROL', **kwargs)

def ParametricSetvalueforrun(idf, **kwargs: Unpack[ParametricSetvalueforrunType]):
    """"helper for ParametricSetvalueforrun"""
    return idf.newidfobject('PARAMETRIC:SETVALUEFORRUN', **kwargs)

def People(idf, **kwargs: Unpack[PeopleType]):
    """"helper for People"""
    return idf.newidfobject('PEOPLE', **kwargs)

def Performanceprecisiontradeoffs(idf, **kwargs: Unpack[PerformanceprecisiontradeoffsType]):
    """"helper for Performanceprecisiontradeoffs"""
    return idf.newidfobject('PERFORMANCEPRECISIONTRADEOFFS', **kwargs)

def PhotovoltaicperformanceEquivalentonediode(idf, **kwargs: Unpack[PhotovoltaicperformanceEquivalentonediodeType]):
    """"helper for PhotovoltaicperformanceEquivalentonediode"""
    return idf.newidfobject('PHOTOVOLTAICPERFORMANCE:EQUIVALENTONE-DIODE', **kwargs)

def PhotovoltaicperformanceSandia(idf, **kwargs: Unpack[PhotovoltaicperformanceSandiaType]):
    """"helper for PhotovoltaicperformanceSandia"""
    return idf.newidfobject('PHOTOVOLTAICPERFORMANCE:SANDIA', **kwargs)

def PhotovoltaicperformanceSimple(idf, **kwargs: Unpack[PhotovoltaicperformanceSimpleType]):
    """"helper for PhotovoltaicperformanceSimple"""
    return idf.newidfobject('PHOTOVOLTAICPERFORMANCE:SIMPLE', **kwargs)

def PipeAdiabatic(idf, **kwargs: Unpack[PipeAdiabaticType]):
    """"helper for PipeAdiabatic"""
    return idf.newidfobject('PIPE:ADIABATIC', **kwargs)

def PipeAdiabaticSteam(idf, **kwargs: Unpack[PipeAdiabaticSteamType]):
    """"helper for PipeAdiabaticSteam"""
    return idf.newidfobject('PIPE:ADIABATIC:STEAM', **kwargs)

def PipeIndoor(idf, **kwargs: Unpack[PipeIndoorType]):
    """"helper for PipeIndoor"""
    return idf.newidfobject('PIPE:INDOOR', **kwargs)

def PipeOutdoor(idf, **kwargs: Unpack[PipeOutdoorType]):
    """"helper for PipeOutdoor"""
    return idf.newidfobject('PIPE:OUTDOOR', **kwargs)

def PipeUnderground(idf, **kwargs: Unpack[PipeUndergroundType]):
    """"helper for PipeUnderground"""
    return idf.newidfobject('PIPE:UNDERGROUND', **kwargs)

def PipingsystemUndergroundDomain(idf, **kwargs: Unpack[PipingsystemUndergroundDomainType]):
    """"helper for PipingsystemUndergroundDomain"""
    return idf.newidfobject('PIPINGSYSTEM:UNDERGROUND:DOMAIN', **kwargs)

def PipingsystemUndergroundPipecircuit(idf, **kwargs: Unpack[PipingsystemUndergroundPipecircuitType]):
    """"helper for PipingsystemUndergroundPipecircuit"""
    return idf.newidfobject('PIPINGSYSTEM:UNDERGROUND:PIPECIRCUIT', **kwargs)

def PipingsystemUndergroundPipesegment(idf, **kwargs: Unpack[PipingsystemUndergroundPipesegmentType]):
    """"helper for PipingsystemUndergroundPipesegment"""
    return idf.newidfobject('PIPINGSYSTEM:UNDERGROUND:PIPESEGMENT', **kwargs)

def PlantcomponentTemperaturesource(idf, **kwargs: Unpack[PlantcomponentTemperaturesourceType]):
    """"helper for PlantcomponentTemperaturesource"""
    return idf.newidfobject('PLANTCOMPONENT:TEMPERATURESOURCE', **kwargs)

def PlantcomponentUserdefined(idf, **kwargs: Unpack[PlantcomponentUserdefinedType]):
    """"helper for PlantcomponentUserdefined"""
    return idf.newidfobject('PLANTCOMPONENT:USERDEFINED', **kwargs)

def Plantequipmentlist(idf, **kwargs: Unpack[PlantequipmentlistType]):
    """"helper for Plantequipmentlist"""
    return idf.newidfobject('PLANTEQUIPMENTLIST', **kwargs)

def PlantequipmentoperationChillerheaterchangeover(idf, **kwargs: Unpack[PlantequipmentoperationChillerheaterchangeoverType]):
    """"helper for PlantequipmentoperationChillerheaterchangeover"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:CHILLERHEATERCHANGEOVER', **kwargs)

def PlantequipmentoperationComponentsetpoint(idf, **kwargs: Unpack[PlantequipmentoperationComponentsetpointType]):
    """"helper for PlantequipmentoperationComponentsetpoint"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:COMPONENTSETPOINT', **kwargs)

def PlantequipmentoperationCoolingload(idf, **kwargs: Unpack[PlantequipmentoperationCoolingloadType]):
    """"helper for PlantequipmentoperationCoolingload"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:COOLINGLOAD', **kwargs)

def PlantequipmentoperationHeatingload(idf, **kwargs: Unpack[PlantequipmentoperationHeatingloadType]):
    """"helper for PlantequipmentoperationHeatingload"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:HEATINGLOAD', **kwargs)

def PlantequipmentoperationOutdoordewpoint(idf, **kwargs: Unpack[PlantequipmentoperationOutdoordewpointType]):
    """"helper for PlantequipmentoperationOutdoordewpoint"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORDEWPOINT', **kwargs)

def PlantequipmentoperationOutdoordewpointdifference(idf, **kwargs: Unpack[PlantequipmentoperationOutdoordewpointdifferenceType]):
    """"helper for PlantequipmentoperationOutdoordewpointdifference"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORDEWPOINTDIFFERENCE', **kwargs)

def PlantequipmentoperationOutdoordrybulb(idf, **kwargs: Unpack[PlantequipmentoperationOutdoordrybulbType]):
    """"helper for PlantequipmentoperationOutdoordrybulb"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORDRYBULB', **kwargs)

def PlantequipmentoperationOutdoordrybulbdifference(idf, **kwargs: Unpack[PlantequipmentoperationOutdoordrybulbdifferenceType]):
    """"helper for PlantequipmentoperationOutdoordrybulbdifference"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORDRYBULBDIFFERENCE', **kwargs)

def PlantequipmentoperationOutdoorrelativehumidity(idf, **kwargs: Unpack[PlantequipmentoperationOutdoorrelativehumidityType]):
    """"helper for PlantequipmentoperationOutdoorrelativehumidity"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORRELATIVEHUMIDITY', **kwargs)

def PlantequipmentoperationOutdoorwetbulb(idf, **kwargs: Unpack[PlantequipmentoperationOutdoorwetbulbType]):
    """"helper for PlantequipmentoperationOutdoorwetbulb"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORWETBULB', **kwargs)

def PlantequipmentoperationOutdoorwetbulbdifference(idf, **kwargs: Unpack[PlantequipmentoperationOutdoorwetbulbdifferenceType]):
    """"helper for PlantequipmentoperationOutdoorwetbulbdifference"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORWETBULBDIFFERENCE', **kwargs)

def PlantequipmentoperationThermalenergystorage(idf, **kwargs: Unpack[PlantequipmentoperationThermalenergystorageType]):
    """"helper for PlantequipmentoperationThermalenergystorage"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:THERMALENERGYSTORAGE', **kwargs)

def PlantequipmentoperationUncontrolled(idf, **kwargs: Unpack[PlantequipmentoperationUncontrolledType]):
    """"helper for PlantequipmentoperationUncontrolled"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:UNCONTROLLED', **kwargs)

def PlantequipmentoperationUserdefined(idf, **kwargs: Unpack[PlantequipmentoperationUserdefinedType]):
    """"helper for PlantequipmentoperationUserdefined"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:USERDEFINED', **kwargs)

def Plantequipmentoperationschemes(idf, **kwargs: Unpack[PlantequipmentoperationschemesType]):
    """"helper for Plantequipmentoperationschemes"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATIONSCHEMES', **kwargs)

def Plantloop(idf, **kwargs: Unpack[PlantloopType]):
    """"helper for Plantloop"""
    return idf.newidfobject('PLANTLOOP', **kwargs)

def PumpConstantspeed(idf, **kwargs: Unpack[PumpConstantspeedType]):
    """"helper for PumpConstantspeed"""
    return idf.newidfobject('PUMP:CONSTANTSPEED', **kwargs)

def PumpVariablespeed(idf, **kwargs: Unpack[PumpVariablespeedType]):
    """"helper for PumpVariablespeed"""
    return idf.newidfobject('PUMP:VARIABLESPEED', **kwargs)

def PumpVariablespeedCondensate(idf, **kwargs: Unpack[PumpVariablespeedCondensateType]):
    """"helper for PumpVariablespeedCondensate"""
    return idf.newidfobject('PUMP:VARIABLESPEED:CONDENSATE', **kwargs)

def PythonpluginInstance(idf, **kwargs: Unpack[PythonpluginInstanceType]):
    """"helper for PythonpluginInstance"""
    return idf.newidfobject('PYTHONPLUGIN:INSTANCE', **kwargs)

def PythonpluginOutputvariable(idf, **kwargs: Unpack[PythonpluginOutputvariableType]):
    """"helper for PythonpluginOutputvariable"""
    return idf.newidfobject('PYTHONPLUGIN:OUTPUTVARIABLE', **kwargs)

def PythonpluginSearchpaths(idf, **kwargs: Unpack[PythonpluginSearchpathsType]):
    """"helper for PythonpluginSearchpaths"""
    return idf.newidfobject('PYTHONPLUGIN:SEARCHPATHS', **kwargs)

def PythonpluginTrendvariable(idf, **kwargs: Unpack[PythonpluginTrendvariableType]):
    """"helper for PythonpluginTrendvariable"""
    return idf.newidfobject('PYTHONPLUGIN:TRENDVARIABLE', **kwargs)

def PythonpluginVariables(idf, **kwargs: Unpack[PythonpluginVariablesType]):
    """"helper for PythonpluginVariables"""
    return idf.newidfobject('PYTHONPLUGIN:VARIABLES', **kwargs)

def RefrigerationAirchiller(idf, **kwargs: Unpack[RefrigerationAirchillerType]):
    """"helper for RefrigerationAirchiller"""
    return idf.newidfobject('REFRIGERATION:AIRCHILLER', **kwargs)

def RefrigerationCase(idf, **kwargs: Unpack[RefrigerationCaseType]):
    """"helper for RefrigerationCase"""
    return idf.newidfobject('REFRIGERATION:CASE', **kwargs)

def RefrigerationCaseandwalkinlist(idf, **kwargs: Unpack[RefrigerationCaseandwalkinlistType]):
    """"helper for RefrigerationCaseandwalkinlist"""
    return idf.newidfobject('REFRIGERATION:CASEANDWALKINLIST', **kwargs)

def RefrigerationCompressor(idf, **kwargs: Unpack[RefrigerationCompressorType]):
    """"helper for RefrigerationCompressor"""
    return idf.newidfobject('REFRIGERATION:COMPRESSOR', **kwargs)

def RefrigerationCompressorlist(idf, **kwargs: Unpack[RefrigerationCompressorlistType]):
    """"helper for RefrigerationCompressorlist"""
    return idf.newidfobject('REFRIGERATION:COMPRESSORLIST', **kwargs)

def RefrigerationCompressorrack(idf, **kwargs: Unpack[RefrigerationCompressorrackType]):
    """"helper for RefrigerationCompressorrack"""
    return idf.newidfobject('REFRIGERATION:COMPRESSORRACK', **kwargs)

def RefrigerationCondenserAircooled(idf, **kwargs: Unpack[RefrigerationCondenserAircooledType]):
    """"helper for RefrigerationCondenserAircooled"""
    return idf.newidfobject('REFRIGERATION:CONDENSER:AIRCOOLED', **kwargs)

def RefrigerationCondenserCascade(idf, **kwargs: Unpack[RefrigerationCondenserCascadeType]):
    """"helper for RefrigerationCondenserCascade"""
    return idf.newidfobject('REFRIGERATION:CONDENSER:CASCADE', **kwargs)

def RefrigerationCondenserEvaporativecooled(idf, **kwargs: Unpack[RefrigerationCondenserEvaporativecooledType]):
    """"helper for RefrigerationCondenserEvaporativecooled"""
    return idf.newidfobject('REFRIGERATION:CONDENSER:EVAPORATIVECOOLED', **kwargs)

def RefrigerationCondenserWatercooled(idf, **kwargs: Unpack[RefrigerationCondenserWatercooledType]):
    """"helper for RefrigerationCondenserWatercooled"""
    return idf.newidfobject('REFRIGERATION:CONDENSER:WATERCOOLED', **kwargs)

def RefrigerationGascoolerAircooled(idf, **kwargs: Unpack[RefrigerationGascoolerAircooledType]):
    """"helper for RefrigerationGascoolerAircooled"""
    return idf.newidfobject('REFRIGERATION:GASCOOLER:AIRCOOLED', **kwargs)

def RefrigerationSecondarysystem(idf, **kwargs: Unpack[RefrigerationSecondarysystemType]):
    """"helper for RefrigerationSecondarysystem"""
    return idf.newidfobject('REFRIGERATION:SECONDARYSYSTEM', **kwargs)

def RefrigerationSubcooler(idf, **kwargs: Unpack[RefrigerationSubcoolerType]):
    """"helper for RefrigerationSubcooler"""
    return idf.newidfobject('REFRIGERATION:SUBCOOLER', **kwargs)

def RefrigerationSystem(idf, **kwargs: Unpack[RefrigerationSystemType]):
    """"helper for RefrigerationSystem"""
    return idf.newidfobject('REFRIGERATION:SYSTEM', **kwargs)

def RefrigerationTranscriticalsystem(idf, **kwargs: Unpack[RefrigerationTranscriticalsystemType]):
    """"helper for RefrigerationTranscriticalsystem"""
    return idf.newidfobject('REFRIGERATION:TRANSCRITICALSYSTEM', **kwargs)

def RefrigerationTransferloadlist(idf, **kwargs: Unpack[RefrigerationTransferloadlistType]):
    """"helper for RefrigerationTransferloadlist"""
    return idf.newidfobject('REFRIGERATION:TRANSFERLOADLIST', **kwargs)

def RefrigerationWalkin(idf, **kwargs: Unpack[RefrigerationWalkinType]):
    """"helper for RefrigerationWalkin"""
    return idf.newidfobject('REFRIGERATION:WALKIN', **kwargs)

def Roof(idf, **kwargs: Unpack[RoofType]):
    """"helper for Roof"""
    return idf.newidfobject('ROOF', **kwargs)

def RoofceilingDetailed(idf, **kwargs: Unpack[RoofceilingDetailedType]):
    """"helper for RoofceilingDetailed"""
    return idf.newidfobject('ROOFCEILING:DETAILED', **kwargs)

def Roofirrigation(idf, **kwargs: Unpack[RoofirrigationType]):
    """"helper for Roofirrigation"""
    return idf.newidfobject('ROOFIRRIGATION', **kwargs)

def RoomairNode(idf, **kwargs: Unpack[RoomairNodeType]):
    """"helper for RoomairNode"""
    return idf.newidfobject('ROOMAIR:NODE', **kwargs)

def RoomairNodeAirflownetwork(idf, **kwargs: Unpack[RoomairNodeAirflownetworkType]):
    """"helper for RoomairNodeAirflownetwork"""
    return idf.newidfobject('ROOMAIR:NODE:AIRFLOWNETWORK', **kwargs)

def RoomairNodeAirflownetworkAdjacentsurfacelist(idf, **kwargs: Unpack[RoomairNodeAirflownetworkAdjacentsurfacelistType]):
    """"helper for RoomairNodeAirflownetworkAdjacentsurfacelist"""
    return idf.newidfobject('ROOMAIR:NODE:AIRFLOWNETWORK:ADJACENTSURFACELIST', **kwargs)

def RoomairNodeAirflownetworkHvacequipment(idf, **kwargs: Unpack[RoomairNodeAirflownetworkHvacequipmentType]):
    """"helper for RoomairNodeAirflownetworkHvacequipment"""
    return idf.newidfobject('ROOMAIR:NODE:AIRFLOWNETWORK:HVACEQUIPMENT', **kwargs)

def RoomairNodeAirflownetworkInternalgains(idf, **kwargs: Unpack[RoomairNodeAirflownetworkInternalgainsType]):
    """"helper for RoomairNodeAirflownetworkInternalgains"""
    return idf.newidfobject('ROOMAIR:NODE:AIRFLOWNETWORK:INTERNALGAINS', **kwargs)

def RoomairTemperaturepatternConstantgradient(idf, **kwargs: Unpack[RoomairTemperaturepatternConstantgradientType]):
    """"helper for RoomairTemperaturepatternConstantgradient"""
    return idf.newidfobject('ROOMAIR:TEMPERATUREPATTERN:CONSTANTGRADIENT', **kwargs)

def RoomairTemperaturepatternNondimensionalheight(idf, **kwargs: Unpack[RoomairTemperaturepatternNondimensionalheightType]):
    """"helper for RoomairTemperaturepatternNondimensionalheight"""
    return idf.newidfobject('ROOMAIR:TEMPERATUREPATTERN:NONDIMENSIONALHEIGHT', **kwargs)

def RoomairTemperaturepatternSurfacemapping(idf, **kwargs: Unpack[RoomairTemperaturepatternSurfacemappingType]):
    """"helper for RoomairTemperaturepatternSurfacemapping"""
    return idf.newidfobject('ROOMAIR:TEMPERATUREPATTERN:SURFACEMAPPING', **kwargs)

def RoomairTemperaturepatternTwogradient(idf, **kwargs: Unpack[RoomairTemperaturepatternTwogradientType]):
    """"helper for RoomairTemperaturepatternTwogradient"""
    return idf.newidfobject('ROOMAIR:TEMPERATUREPATTERN:TWOGRADIENT', **kwargs)

def RoomairTemperaturepatternUserdefined(idf, **kwargs: Unpack[RoomairTemperaturepatternUserdefinedType]):
    """"helper for RoomairTemperaturepatternUserdefined"""
    return idf.newidfobject('ROOMAIR:TEMPERATUREPATTERN:USERDEFINED', **kwargs)

def Roomairmodeltype(idf, **kwargs: Unpack[RoomairmodeltypeType]):
    """"helper for Roomairmodeltype"""
    return idf.newidfobject('ROOMAIRMODELTYPE', **kwargs)

def RoomairsettingsAirflownetwork(idf, **kwargs: Unpack[RoomairsettingsAirflownetworkType]):
    """"helper for RoomairsettingsAirflownetwork"""
    return idf.newidfobject('ROOMAIRSETTINGS:AIRFLOWNETWORK', **kwargs)

def RoomairsettingsCrossventilation(idf, **kwargs: Unpack[RoomairsettingsCrossventilationType]):
    """"helper for RoomairsettingsCrossventilation"""
    return idf.newidfobject('ROOMAIRSETTINGS:CROSSVENTILATION', **kwargs)

def RoomairsettingsOnenodedisplacementventilation(idf, **kwargs: Unpack[RoomairsettingsOnenodedisplacementventilationType]):
    """"helper for RoomairsettingsOnenodedisplacementventilation"""
    return idf.newidfobject('ROOMAIRSETTINGS:ONENODEDISPLACEMENTVENTILATION', **kwargs)

def RoomairsettingsThreenodedisplacementventilation(idf, **kwargs: Unpack[RoomairsettingsThreenodedisplacementventilationType]):
    """"helper for RoomairsettingsThreenodedisplacementventilation"""
    return idf.newidfobject('ROOMAIRSETTINGS:THREENODEDISPLACEMENTVENTILATION', **kwargs)

def RoomairsettingsUnderfloorairdistributionexterior(idf, **kwargs: Unpack[RoomairsettingsUnderfloorairdistributionexteriorType]):
    """"helper for RoomairsettingsUnderfloorairdistributionexterior"""
    return idf.newidfobject('ROOMAIRSETTINGS:UNDERFLOORAIRDISTRIBUTIONEXTERIOR', **kwargs)

def RoomairsettingsUnderfloorairdistributioninterior(idf, **kwargs: Unpack[RoomairsettingsUnderfloorairdistributioninteriorType]):
    """"helper for RoomairsettingsUnderfloorairdistributioninterior"""
    return idf.newidfobject('ROOMAIRSETTINGS:UNDERFLOORAIRDISTRIBUTIONINTERIOR', **kwargs)

def Runperiod(idf, **kwargs: Unpack[RunperiodType]):
    """"helper for Runperiod"""
    return idf.newidfobject('RUNPERIOD', **kwargs)

def RunperiodcontrolDaylightsavingtime(idf, **kwargs: Unpack[RunperiodcontrolDaylightsavingtimeType]):
    """"helper for RunperiodcontrolDaylightsavingtime"""
    return idf.newidfobject('RUNPERIODCONTROL:DAYLIGHTSAVINGTIME', **kwargs)

def RunperiodcontrolSpecialdays(idf, **kwargs: Unpack[RunperiodcontrolSpecialdaysType]):
    """"helper for RunperiodcontrolSpecialdays"""
    return idf.newidfobject('RUNPERIODCONTROL:SPECIALDAYS', **kwargs)

def ScheduleCompact(idf, **kwargs: Unpack[ScheduleCompactType]):
    """"helper for ScheduleCompact"""
    return idf.newidfobject('SCHEDULE:COMPACT', **kwargs)

def ScheduleConstant(idf, **kwargs: Unpack[ScheduleConstantType]):
    """"helper for ScheduleConstant"""
    return idf.newidfobject('SCHEDULE:CONSTANT', **kwargs)

def ScheduleDayHourly(idf, **kwargs: Unpack[ScheduleDayHourlyType]):
    """"helper for ScheduleDayHourly"""
    return idf.newidfobject('SCHEDULE:DAY:HOURLY', **kwargs)

def ScheduleDayInterval(idf, **kwargs: Unpack[ScheduleDayIntervalType]):
    """"helper for ScheduleDayInterval"""
    return idf.newidfobject('SCHEDULE:DAY:INTERVAL', **kwargs)

def ScheduleDayList(idf, **kwargs: Unpack[ScheduleDayListType]):
    """"helper for ScheduleDayList"""
    return idf.newidfobject('SCHEDULE:DAY:LIST', **kwargs)

def ScheduleFile(idf, **kwargs: Unpack[ScheduleFileType]):
    """"helper for ScheduleFile"""
    return idf.newidfobject('SCHEDULE:FILE', **kwargs)

def ScheduleFileShading(idf, **kwargs: Unpack[ScheduleFileShadingType]):
    """"helper for ScheduleFileShading"""
    return idf.newidfobject('SCHEDULE:FILE:SHADING', **kwargs)

def ScheduleWeekCompact(idf, **kwargs: Unpack[ScheduleWeekCompactType]):
    """"helper for ScheduleWeekCompact"""
    return idf.newidfobject('SCHEDULE:WEEK:COMPACT', **kwargs)

def ScheduleWeekDaily(idf, **kwargs: Unpack[ScheduleWeekDailyType]):
    """"helper for ScheduleWeekDaily"""
    return idf.newidfobject('SCHEDULE:WEEK:DAILY', **kwargs)

def ScheduleYear(idf, **kwargs: Unpack[ScheduleYearType]):
    """"helper for ScheduleYear"""
    return idf.newidfobject('SCHEDULE:YEAR', **kwargs)

def Scheduletypelimits(idf, **kwargs: Unpack[ScheduletypelimitsType]):
    """"helper for Scheduletypelimits"""
    return idf.newidfobject('SCHEDULETYPELIMITS', **kwargs)

def SetpointmanagerColdest(idf, **kwargs: Unpack[SetpointmanagerColdestType]):
    """"helper for SetpointmanagerColdest"""
    return idf.newidfobject('SETPOINTMANAGER:COLDEST', **kwargs)

def SetpointmanagerCondenserenteringreset(idf, **kwargs: Unpack[SetpointmanagerCondenserenteringresetType]):
    """"helper for SetpointmanagerCondenserenteringreset"""
    return idf.newidfobject('SETPOINTMANAGER:CONDENSERENTERINGRESET', **kwargs)

def SetpointmanagerCondenserenteringresetIdeal(idf, **kwargs: Unpack[SetpointmanagerCondenserenteringresetIdealType]):
    """"helper for SetpointmanagerCondenserenteringresetIdeal"""
    return idf.newidfobject('SETPOINTMANAGER:CONDENSERENTERINGRESET:IDEAL', **kwargs)

def SetpointmanagerFollowgroundtemperature(idf, **kwargs: Unpack[SetpointmanagerFollowgroundtemperatureType]):
    """"helper for SetpointmanagerFollowgroundtemperature"""
    return idf.newidfobject('SETPOINTMANAGER:FOLLOWGROUNDTEMPERATURE', **kwargs)

def SetpointmanagerFollowoutdoorairtemperature(idf, **kwargs: Unpack[SetpointmanagerFollowoutdoorairtemperatureType]):
    """"helper for SetpointmanagerFollowoutdoorairtemperature"""
    return idf.newidfobject('SETPOINTMANAGER:FOLLOWOUTDOORAIRTEMPERATURE', **kwargs)

def SetpointmanagerFollowsystemnodetemperature(idf, **kwargs: Unpack[SetpointmanagerFollowsystemnodetemperatureType]):
    """"helper for SetpointmanagerFollowsystemnodetemperature"""
    return idf.newidfobject('SETPOINTMANAGER:FOLLOWSYSTEMNODETEMPERATURE', **kwargs)

def SetpointmanagerMixedair(idf, **kwargs: Unpack[SetpointmanagerMixedairType]):
    """"helper for SetpointmanagerMixedair"""
    return idf.newidfobject('SETPOINTMANAGER:MIXEDAIR', **kwargs)

def SetpointmanagerMultizoneCoolingAverage(idf, **kwargs: Unpack[SetpointmanagerMultizoneCoolingAverageType]):
    """"helper for SetpointmanagerMultizoneCoolingAverage"""
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:COOLING:AVERAGE', **kwargs)

def SetpointmanagerMultizoneHeatingAverage(idf, **kwargs: Unpack[SetpointmanagerMultizoneHeatingAverageType]):
    """"helper for SetpointmanagerMultizoneHeatingAverage"""
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:HEATING:AVERAGE', **kwargs)

def SetpointmanagerMultizoneHumidityMaximum(idf, **kwargs: Unpack[SetpointmanagerMultizoneHumidityMaximumType]):
    """"helper for SetpointmanagerMultizoneHumidityMaximum"""
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:HUMIDITY:MAXIMUM', **kwargs)

def SetpointmanagerMultizoneHumidityMinimum(idf, **kwargs: Unpack[SetpointmanagerMultizoneHumidityMinimumType]):
    """"helper for SetpointmanagerMultizoneHumidityMinimum"""
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:HUMIDITY:MINIMUM', **kwargs)

def SetpointmanagerMultizoneMaximumhumidityAverage(idf, **kwargs: Unpack[SetpointmanagerMultizoneMaximumhumidityAverageType]):
    """"helper for SetpointmanagerMultizoneMaximumhumidityAverage"""
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:MAXIMUMHUMIDITY:AVERAGE', **kwargs)

def SetpointmanagerMultizoneMinimumhumidityAverage(idf, **kwargs: Unpack[SetpointmanagerMultizoneMinimumhumidityAverageType]):
    """"helper for SetpointmanagerMultizoneMinimumhumidityAverage"""
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:MINIMUMHUMIDITY:AVERAGE', **kwargs)

def SetpointmanagerOutdoorairpretreat(idf, **kwargs: Unpack[SetpointmanagerOutdoorairpretreatType]):
    """"helper for SetpointmanagerOutdoorairpretreat"""
    return idf.newidfobject('SETPOINTMANAGER:OUTDOORAIRPRETREAT', **kwargs)

def SetpointmanagerOutdoorairreset(idf, **kwargs: Unpack[SetpointmanagerOutdoorairresetType]):
    """"helper for SetpointmanagerOutdoorairreset"""
    return idf.newidfobject('SETPOINTMANAGER:OUTDOORAIRRESET', **kwargs)

def SetpointmanagerReturnairbypassflow(idf, **kwargs: Unpack[SetpointmanagerReturnairbypassflowType]):
    """"helper for SetpointmanagerReturnairbypassflow"""
    return idf.newidfobject('SETPOINTMANAGER:RETURNAIRBYPASSFLOW', **kwargs)

def SetpointmanagerReturntemperatureChilledwater(idf, **kwargs: Unpack[SetpointmanagerReturntemperatureChilledwaterType]):
    """"helper for SetpointmanagerReturntemperatureChilledwater"""
    return idf.newidfobject('SETPOINTMANAGER:RETURNTEMPERATURE:CHILLEDWATER', **kwargs)

def SetpointmanagerReturntemperatureHotwater(idf, **kwargs: Unpack[SetpointmanagerReturntemperatureHotwaterType]):
    """"helper for SetpointmanagerReturntemperatureHotwater"""
    return idf.newidfobject('SETPOINTMANAGER:RETURNTEMPERATURE:HOTWATER', **kwargs)

def SetpointmanagerScheduled(idf, **kwargs: Unpack[SetpointmanagerScheduledType]):
    """"helper for SetpointmanagerScheduled"""
    return idf.newidfobject('SETPOINTMANAGER:SCHEDULED', **kwargs)

def SetpointmanagerScheduledDualsetpoint(idf, **kwargs: Unpack[SetpointmanagerScheduledDualsetpointType]):
    """"helper for SetpointmanagerScheduledDualsetpoint"""
    return idf.newidfobject('SETPOINTMANAGER:SCHEDULED:DUALSETPOINT', **kwargs)

def SetpointmanagerSinglezoneCooling(idf, **kwargs: Unpack[SetpointmanagerSinglezoneCoolingType]):
    """"helper for SetpointmanagerSinglezoneCooling"""
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:COOLING', **kwargs)

def SetpointmanagerSinglezoneHeating(idf, **kwargs: Unpack[SetpointmanagerSinglezoneHeatingType]):
    """"helper for SetpointmanagerSinglezoneHeating"""
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:HEATING', **kwargs)

def SetpointmanagerSinglezoneHumidityMaximum(idf, **kwargs: Unpack[SetpointmanagerSinglezoneHumidityMaximumType]):
    """"helper for SetpointmanagerSinglezoneHumidityMaximum"""
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:HUMIDITY:MAXIMUM', **kwargs)

def SetpointmanagerSinglezoneHumidityMinimum(idf, **kwargs: Unpack[SetpointmanagerSinglezoneHumidityMinimumType]):
    """"helper for SetpointmanagerSinglezoneHumidityMinimum"""
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:HUMIDITY:MINIMUM', **kwargs)

def SetpointmanagerSinglezoneOnestagecooling(idf, **kwargs: Unpack[SetpointmanagerSinglezoneOnestagecoolingType]):
    """"helper for SetpointmanagerSinglezoneOnestagecooling"""
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:ONESTAGECOOLING', **kwargs)

def SetpointmanagerSinglezoneOnestageheating(idf, **kwargs: Unpack[SetpointmanagerSinglezoneOnestageheatingType]):
    """"helper for SetpointmanagerSinglezoneOnestageheating"""
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:ONESTAGEHEATING', **kwargs)

def SetpointmanagerSinglezoneReheat(idf, **kwargs: Unpack[SetpointmanagerSinglezoneReheatType]):
    """"helper for SetpointmanagerSinglezoneReheat"""
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:REHEAT', **kwargs)

def SetpointmanagerSystemnoderesetHumidity(idf, **kwargs: Unpack[SetpointmanagerSystemnoderesetHumidityType]):
    """"helper for SetpointmanagerSystemnoderesetHumidity"""
    return idf.newidfobject('SETPOINTMANAGER:SYSTEMNODERESET:HUMIDITY', **kwargs)

def SetpointmanagerSystemnoderesetTemperature(idf, **kwargs: Unpack[SetpointmanagerSystemnoderesetTemperatureType]):
    """"helper for SetpointmanagerSystemnoderesetTemperature"""
    return idf.newidfobject('SETPOINTMANAGER:SYSTEMNODERESET:TEMPERATURE', **kwargs)

def SetpointmanagerWarmest(idf, **kwargs: Unpack[SetpointmanagerWarmestType]):
    """"helper for SetpointmanagerWarmest"""
    return idf.newidfobject('SETPOINTMANAGER:WARMEST', **kwargs)

def SetpointmanagerWarmesttemperatureflow(idf, **kwargs: Unpack[SetpointmanagerWarmesttemperatureflowType]):
    """"helper for SetpointmanagerWarmesttemperatureflow"""
    return idf.newidfobject('SETPOINTMANAGER:WARMESTTEMPERATUREFLOW', **kwargs)

def ShadingBuilding(idf, **kwargs: Unpack[ShadingBuildingType]):
    """"helper for ShadingBuilding"""
    return idf.newidfobject('SHADING:BUILDING', **kwargs)

def ShadingBuildingDetailed(idf, **kwargs: Unpack[ShadingBuildingDetailedType]):
    """"helper for ShadingBuildingDetailed"""
    return idf.newidfobject('SHADING:BUILDING:DETAILED', **kwargs)

def ShadingFin(idf, **kwargs: Unpack[ShadingFinType]):
    """"helper for ShadingFin"""
    return idf.newidfobject('SHADING:FIN', **kwargs)

def ShadingFinProjection(idf, **kwargs: Unpack[ShadingFinProjectionType]):
    """"helper for ShadingFinProjection"""
    return idf.newidfobject('SHADING:FIN:PROJECTION', **kwargs)

def ShadingOverhang(idf, **kwargs: Unpack[ShadingOverhangType]):
    """"helper for ShadingOverhang"""
    return idf.newidfobject('SHADING:OVERHANG', **kwargs)

def ShadingOverhangProjection(idf, **kwargs: Unpack[ShadingOverhangProjectionType]):
    """"helper for ShadingOverhangProjection"""
    return idf.newidfobject('SHADING:OVERHANG:PROJECTION', **kwargs)

def ShadingSite(idf, **kwargs: Unpack[ShadingSiteType]):
    """"helper for ShadingSite"""
    return idf.newidfobject('SHADING:SITE', **kwargs)

def ShadingSiteDetailed(idf, **kwargs: Unpack[ShadingSiteDetailedType]):
    """"helper for ShadingSiteDetailed"""
    return idf.newidfobject('SHADING:SITE:DETAILED', **kwargs)

def ShadingZoneDetailed(idf, **kwargs: Unpack[ShadingZoneDetailedType]):
    """"helper for ShadingZoneDetailed"""
    return idf.newidfobject('SHADING:ZONE:DETAILED', **kwargs)

def ShadingpropertyReflectance(idf, **kwargs: Unpack[ShadingpropertyReflectanceType]):
    """"helper for ShadingpropertyReflectance"""
    return idf.newidfobject('SHADINGPROPERTY:REFLECTANCE', **kwargs)

def Shadowcalculation(idf, **kwargs: Unpack[ShadowcalculationType]):
    """"helper for Shadowcalculation"""
    return idf.newidfobject('SHADOWCALCULATION', **kwargs)

def Simulationcontrol(idf, **kwargs: Unpack[SimulationcontrolType]):
    """"helper for Simulationcontrol"""
    return idf.newidfobject('SIMULATIONCONTROL', **kwargs)

def SiteGrounddomainBasement(idf, **kwargs: Unpack[SiteGrounddomainBasementType]):
    """"helper for SiteGrounddomainBasement"""
    return idf.newidfobject('SITE:GROUNDDOMAIN:BASEMENT', **kwargs)

def SiteGrounddomainSlab(idf, **kwargs: Unpack[SiteGrounddomainSlabType]):
    """"helper for SiteGrounddomainSlab"""
    return idf.newidfobject('SITE:GROUNDDOMAIN:SLAB', **kwargs)

def SiteGroundreflectance(idf, **kwargs: Unpack[SiteGroundreflectanceType]):
    """"helper for SiteGroundreflectance"""
    return idf.newidfobject('SITE:GROUNDREFLECTANCE', **kwargs)

def SiteGroundreflectanceSnowmodifier(idf, **kwargs: Unpack[SiteGroundreflectanceSnowmodifierType]):
    """"helper for SiteGroundreflectanceSnowmodifier"""
    return idf.newidfobject('SITE:GROUNDREFLECTANCE:SNOWMODIFIER', **kwargs)

def SiteGroundtemperatureBuildingsurface(idf, **kwargs: Unpack[SiteGroundtemperatureBuildingsurfaceType]):
    """"helper for SiteGroundtemperatureBuildingsurface"""
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:BUILDINGSURFACE', **kwargs)

def SiteGroundtemperatureDeep(idf, **kwargs: Unpack[SiteGroundtemperatureDeepType]):
    """"helper for SiteGroundtemperatureDeep"""
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:DEEP', **kwargs)

def SiteGroundtemperatureFcfactormethod(idf, **kwargs: Unpack[SiteGroundtemperatureFcfactormethodType]):
    """"helper for SiteGroundtemperatureFcfactormethod"""
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:FCFACTORMETHOD', **kwargs)

def SiteGroundtemperatureShallow(idf, **kwargs: Unpack[SiteGroundtemperatureShallowType]):
    """"helper for SiteGroundtemperatureShallow"""
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:SHALLOW', **kwargs)

def SiteGroundtemperatureUndisturbedFinitedifference(idf, **kwargs: Unpack[SiteGroundtemperatureUndisturbedFinitedifferenceType]):
    """"helper for SiteGroundtemperatureUndisturbedFinitedifference"""
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:UNDISTURBED:FINITEDIFFERENCE', **kwargs)

def SiteGroundtemperatureUndisturbedKusudaachenbach(idf, **kwargs: Unpack[SiteGroundtemperatureUndisturbedKusudaachenbachType]):
    """"helper for SiteGroundtemperatureUndisturbedKusudaachenbach"""
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:UNDISTURBED:KUSUDAACHENBACH', **kwargs)

def SiteGroundtemperatureUndisturbedXing(idf, **kwargs: Unpack[SiteGroundtemperatureUndisturbedXingType]):
    """"helper for SiteGroundtemperatureUndisturbedXing"""
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:UNDISTURBED:XING', **kwargs)

def SiteHeightvariation(idf, **kwargs: Unpack[SiteHeightvariationType]):
    """"helper for SiteHeightvariation"""
    return idf.newidfobject('SITE:HEIGHTVARIATION', **kwargs)

def SiteLocation(idf, **kwargs: Unpack[SiteLocationType]):
    """"helper for SiteLocation"""
    return idf.newidfobject('SITE:LOCATION', **kwargs)

def SitePrecipitation(idf, **kwargs: Unpack[SitePrecipitationType]):
    """"helper for SitePrecipitation"""
    return idf.newidfobject('SITE:PRECIPITATION', **kwargs)

def SiteSolarandvisiblespectrum(idf, **kwargs: Unpack[SiteSolarandvisiblespectrumType]):
    """"helper for SiteSolarandvisiblespectrum"""
    return idf.newidfobject('SITE:SOLARANDVISIBLESPECTRUM', **kwargs)

def SiteSpectrumdata(idf, **kwargs: Unpack[SiteSpectrumdataType]):
    """"helper for SiteSpectrumdata"""
    return idf.newidfobject('SITE:SPECTRUMDATA', **kwargs)

def SiteVariablelocation(idf, **kwargs: Unpack[SiteVariablelocationType]):
    """"helper for SiteVariablelocation"""
    return idf.newidfobject('SITE:VARIABLELOCATION', **kwargs)

def SiteWatermainstemperature(idf, **kwargs: Unpack[SiteWatermainstemperatureType]):
    """"helper for SiteWatermainstemperature"""
    return idf.newidfobject('SITE:WATERMAINSTEMPERATURE', **kwargs)

def SiteWeatherstation(idf, **kwargs: Unpack[SiteWeatherstationType]):
    """"helper for SiteWeatherstation"""
    return idf.newidfobject('SITE:WEATHERSTATION', **kwargs)

def SizingParameters(idf, **kwargs: Unpack[SizingParametersType]):
    """"helper for SizingParameters"""
    return idf.newidfobject('SIZING:PARAMETERS', **kwargs)

def SizingPlant(idf, **kwargs: Unpack[SizingPlantType]):
    """"helper for SizingPlant"""
    return idf.newidfobject('SIZING:PLANT', **kwargs)

def SizingSystem(idf, **kwargs: Unpack[SizingSystemType]):
    """"helper for SizingSystem"""
    return idf.newidfobject('SIZING:SYSTEM', **kwargs)

def SizingZone(idf, **kwargs: Unpack[SizingZoneType]):
    """"helper for SizingZone"""
    return idf.newidfobject('SIZING:ZONE', **kwargs)

def SizingperiodDesignday(idf, **kwargs: Unpack[SizingperiodDesigndayType]):
    """"helper for SizingperiodDesignday"""
    return idf.newidfobject('SIZINGPERIOD:DESIGNDAY', **kwargs)

def SizingperiodWeatherfileconditiontype(idf, **kwargs: Unpack[SizingperiodWeatherfileconditiontypeType]):
    """"helper for SizingperiodWeatherfileconditiontype"""
    return idf.newidfobject('SIZINGPERIOD:WEATHERFILECONDITIONTYPE', **kwargs)

def SizingperiodWeatherfiledays(idf, **kwargs: Unpack[SizingperiodWeatherfiledaysType]):
    """"helper for SizingperiodWeatherfiledays"""
    return idf.newidfobject('SIZINGPERIOD:WEATHERFILEDAYS', **kwargs)

def SolarcollectorFlatplatePhotovoltaicthermal(idf, **kwargs: Unpack[SolarcollectorFlatplatePhotovoltaicthermalType]):
    """"helper for SolarcollectorFlatplatePhotovoltaicthermal"""
    return idf.newidfobject('SOLARCOLLECTOR:FLATPLATE:PHOTOVOLTAICTHERMAL', **kwargs)

def SolarcollectorFlatplateWater(idf, **kwargs: Unpack[SolarcollectorFlatplateWaterType]):
    """"helper for SolarcollectorFlatplateWater"""
    return idf.newidfobject('SOLARCOLLECTOR:FLATPLATE:WATER', **kwargs)

def SolarcollectorIntegralcollectorstorage(idf, **kwargs: Unpack[SolarcollectorIntegralcollectorstorageType]):
    """"helper for SolarcollectorIntegralcollectorstorage"""
    return idf.newidfobject('SOLARCOLLECTOR:INTEGRALCOLLECTORSTORAGE', **kwargs)

def SolarcollectorUnglazedtranspired(idf, **kwargs: Unpack[SolarcollectorUnglazedtranspiredType]):
    """"helper for SolarcollectorUnglazedtranspired"""
    return idf.newidfobject('SOLARCOLLECTOR:UNGLAZEDTRANSPIRED', **kwargs)

def SolarcollectorUnglazedtranspiredMultisystem(idf, **kwargs: Unpack[SolarcollectorUnglazedtranspiredMultisystemType]):
    """"helper for SolarcollectorUnglazedtranspiredMultisystem"""
    return idf.newidfobject('SOLARCOLLECTOR:UNGLAZEDTRANSPIRED:MULTISYSTEM', **kwargs)

def SolarcollectorperformanceFlatplate(idf, **kwargs: Unpack[SolarcollectorperformanceFlatplateType]):
    """"helper for SolarcollectorperformanceFlatplate"""
    return idf.newidfobject('SOLARCOLLECTORPERFORMANCE:FLATPLATE', **kwargs)

def SolarcollectorperformanceIntegralcollectorstorage(idf, **kwargs: Unpack[SolarcollectorperformanceIntegralcollectorstorageType]):
    """"helper for SolarcollectorperformanceIntegralcollectorstorage"""
    return idf.newidfobject('SOLARCOLLECTORPERFORMANCE:INTEGRALCOLLECTORSTORAGE', **kwargs)

def SolarcollectorperformancePhotovoltaicthermalBipvt(idf, **kwargs: Unpack[SolarcollectorperformancePhotovoltaicthermalBipvtType]):
    """"helper for SolarcollectorperformancePhotovoltaicthermalBipvt"""
    return idf.newidfobject('SOLARCOLLECTORPERFORMANCE:PHOTOVOLTAICTHERMAL:BIPVT', **kwargs)

def SolarcollectorperformancePhotovoltaicthermalSimple(idf, **kwargs: Unpack[SolarcollectorperformancePhotovoltaicthermalSimpleType]):
    """"helper for SolarcollectorperformancePhotovoltaicthermalSimple"""
    return idf.newidfobject('SOLARCOLLECTORPERFORMANCE:PHOTOVOLTAICTHERMAL:SIMPLE', **kwargs)

def Space(idf, **kwargs: Unpack[SpaceType]):
    """"helper for Space"""
    return idf.newidfobject('SPACE', **kwargs)

def SpacehvacEquipmentconnections(idf, **kwargs: Unpack[SpacehvacEquipmentconnectionsType]):
    """"helper for SpacehvacEquipmentconnections"""
    return idf.newidfobject('SPACEHVAC:EQUIPMENTCONNECTIONS', **kwargs)

def SpacehvacZoneequipmentmixer(idf, **kwargs: Unpack[SpacehvacZoneequipmentmixerType]):
    """"helper for SpacehvacZoneequipmentmixer"""
    return idf.newidfobject('SPACEHVAC:ZONEEQUIPMENTMIXER', **kwargs)

def SpacehvacZoneequipmentsplitter(idf, **kwargs: Unpack[SpacehvacZoneequipmentsplitterType]):
    """"helper for SpacehvacZoneequipmentsplitter"""
    return idf.newidfobject('SPACEHVAC:ZONEEQUIPMENTSPLITTER', **kwargs)

def Spacelist(idf, **kwargs: Unpack[SpacelistType]):
    """"helper for Spacelist"""
    return idf.newidfobject('SPACELIST', **kwargs)

def Steamequipment(idf, **kwargs: Unpack[SteamequipmentType]):
    """"helper for Steamequipment"""
    return idf.newidfobject('STEAMEQUIPMENT', **kwargs)

def SurfacecontaminantsourceandsinkGenericBoundarylayerdiffusion(idf, **kwargs: Unpack[SurfacecontaminantsourceandsinkGenericBoundarylayerdiffusionType]):
    """"helper for SurfacecontaminantsourceandsinkGenericBoundarylayerdiffusion"""
    return idf.newidfobject('SURFACECONTAMINANTSOURCEANDSINK:GENERIC:BOUNDARYLAYERDIFFUSION', **kwargs)

def SurfacecontaminantsourceandsinkGenericDepositionvelocitysink(idf, **kwargs: Unpack[SurfacecontaminantsourceandsinkGenericDepositionvelocitysinkType]):
    """"helper for SurfacecontaminantsourceandsinkGenericDepositionvelocitysink"""
    return idf.newidfobject('SURFACECONTAMINANTSOURCEANDSINK:GENERIC:DEPOSITIONVELOCITYSINK', **kwargs)

def SurfacecontaminantsourceandsinkGenericPressuredriven(idf, **kwargs: Unpack[SurfacecontaminantsourceandsinkGenericPressuredrivenType]):
    """"helper for SurfacecontaminantsourceandsinkGenericPressuredriven"""
    return idf.newidfobject('SURFACECONTAMINANTSOURCEANDSINK:GENERIC:PRESSUREDRIVEN', **kwargs)

def SurfacecontrolMovableinsulation(idf, **kwargs: Unpack[SurfacecontrolMovableinsulationType]):
    """"helper for SurfacecontrolMovableinsulation"""
    return idf.newidfobject('SURFACECONTROL:MOVABLEINSULATION', **kwargs)

def SurfaceconvectionalgorithmInside(idf, **kwargs: Unpack[SurfaceconvectionalgorithmInsideType]):
    """"helper for SurfaceconvectionalgorithmInside"""
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:INSIDE', **kwargs)

def SurfaceconvectionalgorithmInsideAdaptivemodelselections(idf, **kwargs: Unpack[SurfaceconvectionalgorithmInsideAdaptivemodelselectionsType]):
    """"helper for SurfaceconvectionalgorithmInsideAdaptivemodelselections"""
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:INSIDE:ADAPTIVEMODELSELECTIONS', **kwargs)

def SurfaceconvectionalgorithmInsideUsercurve(idf, **kwargs: Unpack[SurfaceconvectionalgorithmInsideUsercurveType]):
    """"helper for SurfaceconvectionalgorithmInsideUsercurve"""
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:INSIDE:USERCURVE', **kwargs)

def SurfaceconvectionalgorithmOutside(idf, **kwargs: Unpack[SurfaceconvectionalgorithmOutsideType]):
    """"helper for SurfaceconvectionalgorithmOutside"""
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:OUTSIDE', **kwargs)

def SurfaceconvectionalgorithmOutsideAdaptivemodelselections(idf, **kwargs: Unpack[SurfaceconvectionalgorithmOutsideAdaptivemodelselectionsType]):
    """"helper for SurfaceconvectionalgorithmOutsideAdaptivemodelselections"""
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:OUTSIDE:ADAPTIVEMODELSELECTIONS', **kwargs)

def SurfaceconvectionalgorithmOutsideUsercurve(idf, **kwargs: Unpack[SurfaceconvectionalgorithmOutsideUsercurveType]):
    """"helper for SurfaceconvectionalgorithmOutsideUsercurve"""
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:OUTSIDE:USERCURVE', **kwargs)

def SurfacepropertiesVaporcoefficients(idf, **kwargs: Unpack[SurfacepropertiesVaporcoefficientsType]):
    """"helper for SurfacepropertiesVaporcoefficients"""
    return idf.newidfobject('SURFACEPROPERTIES:VAPORCOEFFICIENTS', **kwargs)

def SurfacepropertyConvectioncoefficients(idf, **kwargs: Unpack[SurfacepropertyConvectioncoefficientsType]):
    """"helper for SurfacepropertyConvectioncoefficients"""
    return idf.newidfobject('SURFACEPROPERTY:CONVECTIONCOEFFICIENTS', **kwargs)

def SurfacepropertyConvectioncoefficientsMultiplesurface(idf, **kwargs: Unpack[SurfacepropertyConvectioncoefficientsMultiplesurfaceType]):
    """"helper for SurfacepropertyConvectioncoefficientsMultiplesurface"""
    return idf.newidfobject('SURFACEPROPERTY:CONVECTIONCOEFFICIENTS:MULTIPLESURFACE', **kwargs)

def SurfacepropertyExposedfoundationperimeter(idf, **kwargs: Unpack[SurfacepropertyExposedfoundationperimeterType]):
    """"helper for SurfacepropertyExposedfoundationperimeter"""
    return idf.newidfobject('SURFACEPROPERTY:EXPOSEDFOUNDATIONPERIMETER', **kwargs)

def SurfacepropertyExteriornaturalventedcavity(idf, **kwargs: Unpack[SurfacepropertyExteriornaturalventedcavityType]):
    """"helper for SurfacepropertyExteriornaturalventedcavity"""
    return idf.newidfobject('SURFACEPROPERTY:EXTERIORNATURALVENTEDCAVITY', **kwargs)

def SurfacepropertyGroundsurfaces(idf, **kwargs: Unpack[SurfacepropertyGroundsurfacesType]):
    """"helper for SurfacepropertyGroundsurfaces"""
    return idf.newidfobject('SURFACEPROPERTY:GROUNDSURFACES', **kwargs)

def SurfacepropertyHeatbalancesourceterm(idf, **kwargs: Unpack[SurfacepropertyHeatbalancesourcetermType]):
    """"helper for SurfacepropertyHeatbalancesourceterm"""
    return idf.newidfobject('SURFACEPROPERTY:HEATBALANCESOURCETERM', **kwargs)

def SurfacepropertyHeattransferalgorithm(idf, **kwargs: Unpack[SurfacepropertyHeattransferalgorithmType]):
    """"helper for SurfacepropertyHeattransferalgorithm"""
    return idf.newidfobject('SURFACEPROPERTY:HEATTRANSFERALGORITHM', **kwargs)

def SurfacepropertyHeattransferalgorithmConstruction(idf, **kwargs: Unpack[SurfacepropertyHeattransferalgorithmConstructionType]):
    """"helper for SurfacepropertyHeattransferalgorithmConstruction"""
    return idf.newidfobject('SURFACEPROPERTY:HEATTRANSFERALGORITHM:CONSTRUCTION', **kwargs)

def SurfacepropertyHeattransferalgorithmMultiplesurface(idf, **kwargs: Unpack[SurfacepropertyHeattransferalgorithmMultiplesurfaceType]):
    """"helper for SurfacepropertyHeattransferalgorithmMultiplesurface"""
    return idf.newidfobject('SURFACEPROPERTY:HEATTRANSFERALGORITHM:MULTIPLESURFACE', **kwargs)

def SurfacepropertyHeattransferalgorithmSurfacelist(idf, **kwargs: Unpack[SurfacepropertyHeattransferalgorithmSurfacelistType]):
    """"helper for SurfacepropertyHeattransferalgorithmSurfacelist"""
    return idf.newidfobject('SURFACEPROPERTY:HEATTRANSFERALGORITHM:SURFACELIST', **kwargs)

def SurfacepropertyIncidentsolarmultiplier(idf, **kwargs: Unpack[SurfacepropertyIncidentsolarmultiplierType]):
    """"helper for SurfacepropertyIncidentsolarmultiplier"""
    return idf.newidfobject('SURFACEPROPERTY:INCIDENTSOLARMULTIPLIER', **kwargs)

def SurfacepropertyLocalenvironment(idf, **kwargs: Unpack[SurfacepropertyLocalenvironmentType]):
    """"helper for SurfacepropertyLocalenvironment"""
    return idf.newidfobject('SURFACEPROPERTY:LOCALENVIRONMENT', **kwargs)

def SurfacepropertyOthersidecoefficients(idf, **kwargs: Unpack[SurfacepropertyOthersidecoefficientsType]):
    """"helper for SurfacepropertyOthersidecoefficients"""
    return idf.newidfobject('SURFACEPROPERTY:OTHERSIDECOEFFICIENTS', **kwargs)

def SurfacepropertyOthersideconditionsmodel(idf, **kwargs: Unpack[SurfacepropertyOthersideconditionsmodelType]):
    """"helper for SurfacepropertyOthersideconditionsmodel"""
    return idf.newidfobject('SURFACEPROPERTY:OTHERSIDECONDITIONSMODEL', **kwargs)

def SurfacepropertySolarincidentinside(idf, **kwargs: Unpack[SurfacepropertySolarincidentinsideType]):
    """"helper for SurfacepropertySolarincidentinside"""
    return idf.newidfobject('SURFACEPROPERTY:SOLARINCIDENTINSIDE', **kwargs)

def SurfacepropertySurroundingsurfaces(idf, **kwargs: Unpack[SurfacepropertySurroundingsurfacesType]):
    """"helper for SurfacepropertySurroundingsurfaces"""
    return idf.newidfobject('SURFACEPROPERTY:SURROUNDINGSURFACES', **kwargs)

def SurfacepropertyUnderwater(idf, **kwargs: Unpack[SurfacepropertyUnderwaterType]):
    """"helper for SurfacepropertyUnderwater"""
    return idf.newidfobject('SURFACEPROPERTY:UNDERWATER', **kwargs)

def SwimmingpoolIndoor(idf, **kwargs: Unpack[SwimmingpoolIndoorType]):
    """"helper for SwimmingpoolIndoor"""
    return idf.newidfobject('SWIMMINGPOOL:INDOOR', **kwargs)

def TableIndependentvariable(idf, **kwargs: Unpack[TableIndependentvariableType]):
    """"helper for TableIndependentvariable"""
    return idf.newidfobject('TABLE:INDEPENDENTVARIABLE', **kwargs)

def TableIndependentvariablelist(idf, **kwargs: Unpack[TableIndependentvariablelistType]):
    """"helper for TableIndependentvariablelist"""
    return idf.newidfobject('TABLE:INDEPENDENTVARIABLELIST', **kwargs)

def TableLookup(idf, **kwargs: Unpack[TableLookupType]):
    """"helper for TableLookup"""
    return idf.newidfobject('TABLE:LOOKUP', **kwargs)

def Temperingvalve(idf, **kwargs: Unpack[TemperingvalveType]):
    """"helper for Temperingvalve"""
    return idf.newidfobject('TEMPERINGVALVE', **kwargs)

def ThermalstorageChilledwaterMixed(idf, **kwargs: Unpack[ThermalstorageChilledwaterMixedType]):
    """"helper for ThermalstorageChilledwaterMixed"""
    return idf.newidfobject('THERMALSTORAGE:CHILLEDWATER:MIXED', **kwargs)

def ThermalstorageChilledwaterStratified(idf, **kwargs: Unpack[ThermalstorageChilledwaterStratifiedType]):
    """"helper for ThermalstorageChilledwaterStratified"""
    return idf.newidfobject('THERMALSTORAGE:CHILLEDWATER:STRATIFIED', **kwargs)

def ThermalstorageIceDetailed(idf, **kwargs: Unpack[ThermalstorageIceDetailedType]):
    """"helper for ThermalstorageIceDetailed"""
    return idf.newidfobject('THERMALSTORAGE:ICE:DETAILED', **kwargs)

def ThermalstorageIceSimple(idf, **kwargs: Unpack[ThermalstorageIceSimpleType]):
    """"helper for ThermalstorageIceSimple"""
    return idf.newidfobject('THERMALSTORAGE:ICE:SIMPLE', **kwargs)

def ThermostatsetpointDualsetpoint(idf, **kwargs: Unpack[ThermostatsetpointDualsetpointType]):
    """"helper for ThermostatsetpointDualsetpoint"""
    return idf.newidfobject('THERMOSTATSETPOINT:DUALSETPOINT', **kwargs)

def ThermostatsetpointSinglecooling(idf, **kwargs: Unpack[ThermostatsetpointSinglecoolingType]):
    """"helper for ThermostatsetpointSinglecooling"""
    return idf.newidfobject('THERMOSTATSETPOINT:SINGLECOOLING', **kwargs)

def ThermostatsetpointSingleheating(idf, **kwargs: Unpack[ThermostatsetpointSingleheatingType]):
    """"helper for ThermostatsetpointSingleheating"""
    return idf.newidfobject('THERMOSTATSETPOINT:SINGLEHEATING', **kwargs)

def ThermostatsetpointSingleheatingorcooling(idf, **kwargs: Unpack[ThermostatsetpointSingleheatingorcoolingType]):
    """"helper for ThermostatsetpointSingleheatingorcooling"""
    return idf.newidfobject('THERMOSTATSETPOINT:SINGLEHEATINGORCOOLING', **kwargs)

def ThermostatsetpointThermalcomfortFangerDualsetpoint(idf, **kwargs: Unpack[ThermostatsetpointThermalcomfortFangerDualsetpointType]):
    """"helper for ThermostatsetpointThermalcomfortFangerDualsetpoint"""
    return idf.newidfobject('THERMOSTATSETPOINT:THERMALCOMFORT:FANGER:DUALSETPOINT', **kwargs)

def ThermostatsetpointThermalcomfortFangerSinglecooling(idf, **kwargs: Unpack[ThermostatsetpointThermalcomfortFangerSinglecoolingType]):
    """"helper for ThermostatsetpointThermalcomfortFangerSinglecooling"""
    return idf.newidfobject('THERMOSTATSETPOINT:THERMALCOMFORT:FANGER:SINGLECOOLING', **kwargs)

def ThermostatsetpointThermalcomfortFangerSingleheating(idf, **kwargs: Unpack[ThermostatsetpointThermalcomfortFangerSingleheatingType]):
    """"helper for ThermostatsetpointThermalcomfortFangerSingleheating"""
    return idf.newidfobject('THERMOSTATSETPOINT:THERMALCOMFORT:FANGER:SINGLEHEATING', **kwargs)

def ThermostatsetpointThermalcomfortFangerSingleheatingorcooling(idf, **kwargs: Unpack[ThermostatsetpointThermalcomfortFangerSingleheatingorcoolingType]):
    """"helper for ThermostatsetpointThermalcomfortFangerSingleheatingorcooling"""
    return idf.newidfobject('THERMOSTATSETPOINT:THERMALCOMFORT:FANGER:SINGLEHEATINGORCOOLING', **kwargs)

def Timestep(idf, **kwargs: Unpack[TimestepType]):
    """"helper for Timestep"""
    return idf.newidfobject('TIMESTEP', **kwargs)

def UnitarysystemperformanceMultispeed(idf, **kwargs: Unpack[UnitarysystemperformanceMultispeedType]):
    """"helper for UnitarysystemperformanceMultispeed"""
    return idf.newidfobject('UNITARYSYSTEMPERFORMANCE:MULTISPEED', **kwargs)

def UtilitycostChargeBlock(idf, **kwargs: Unpack[UtilitycostChargeBlockType]):
    """"helper for UtilitycostChargeBlock"""
    return idf.newidfobject('UTILITYCOST:CHARGE:BLOCK', **kwargs)

def UtilitycostChargeSimple(idf, **kwargs: Unpack[UtilitycostChargeSimpleType]):
    """"helper for UtilitycostChargeSimple"""
    return idf.newidfobject('UTILITYCOST:CHARGE:SIMPLE', **kwargs)

def UtilitycostComputation(idf, **kwargs: Unpack[UtilitycostComputationType]):
    """"helper for UtilitycostComputation"""
    return idf.newidfobject('UTILITYCOST:COMPUTATION', **kwargs)

def UtilitycostQualify(idf, **kwargs: Unpack[UtilitycostQualifyType]):
    """"helper for UtilitycostQualify"""
    return idf.newidfobject('UTILITYCOST:QUALIFY', **kwargs)

def UtilitycostRatchet(idf, **kwargs: Unpack[UtilitycostRatchetType]):
    """"helper for UtilitycostRatchet"""
    return idf.newidfobject('UTILITYCOST:RATCHET', **kwargs)

def UtilitycostTariff(idf, **kwargs: Unpack[UtilitycostTariffType]):
    """"helper for UtilitycostTariff"""
    return idf.newidfobject('UTILITYCOST:TARIFF', **kwargs)

def UtilitycostVariable(idf, **kwargs: Unpack[UtilitycostVariableType]):
    """"helper for UtilitycostVariable"""
    return idf.newidfobject('UTILITYCOST:VARIABLE', **kwargs)

def Version(idf, **kwargs: Unpack[VersionType]):
    """"helper for Version"""
    return idf.newidfobject('VERSION', **kwargs)

def WallAdiabatic(idf, **kwargs: Unpack[WallAdiabaticType]):
    """"helper for WallAdiabatic"""
    return idf.newidfobject('WALL:ADIABATIC', **kwargs)

def WallDetailed(idf, **kwargs: Unpack[WallDetailedType]):
    """"helper for WallDetailed"""
    return idf.newidfobject('WALL:DETAILED', **kwargs)

def WallExterior(idf, **kwargs: Unpack[WallExteriorType]):
    """"helper for WallExterior"""
    return idf.newidfobject('WALL:EXTERIOR', **kwargs)

def WallInterzone(idf, **kwargs: Unpack[WallInterzoneType]):
    """"helper for WallInterzone"""
    return idf.newidfobject('WALL:INTERZONE', **kwargs)

def WallUnderground(idf, **kwargs: Unpack[WallUndergroundType]):
    """"helper for WallUnderground"""
    return idf.newidfobject('WALL:UNDERGROUND', **kwargs)

def WaterheaterHeatpumpPumpedcondenser(idf, **kwargs: Unpack[WaterheaterHeatpumpPumpedcondenserType]):
    """"helper for WaterheaterHeatpumpPumpedcondenser"""
    return idf.newidfobject('WATERHEATER:HEATPUMP:PUMPEDCONDENSER', **kwargs)

def WaterheaterHeatpumpWrappedcondenser(idf, **kwargs: Unpack[WaterheaterHeatpumpWrappedcondenserType]):
    """"helper for WaterheaterHeatpumpWrappedcondenser"""
    return idf.newidfobject('WATERHEATER:HEATPUMP:WRAPPEDCONDENSER', **kwargs)

def WaterheaterMixed(idf, **kwargs: Unpack[WaterheaterMixedType]):
    """"helper for WaterheaterMixed"""
    return idf.newidfobject('WATERHEATER:MIXED', **kwargs)

def WaterheaterSizing(idf, **kwargs: Unpack[WaterheaterSizingType]):
    """"helper for WaterheaterSizing"""
    return idf.newidfobject('WATERHEATER:SIZING', **kwargs)

def WaterheaterStratified(idf, **kwargs: Unpack[WaterheaterStratifiedType]):
    """"helper for WaterheaterStratified"""
    return idf.newidfobject('WATERHEATER:STRATIFIED', **kwargs)

def WateruseConnections(idf, **kwargs: Unpack[WateruseConnectionsType]):
    """"helper for WateruseConnections"""
    return idf.newidfobject('WATERUSE:CONNECTIONS', **kwargs)

def WateruseEquipment(idf, **kwargs: Unpack[WateruseEquipmentType]):
    """"helper for WateruseEquipment"""
    return idf.newidfobject('WATERUSE:EQUIPMENT', **kwargs)

def WateruseRaincollector(idf, **kwargs: Unpack[WateruseRaincollectorType]):
    """"helper for WateruseRaincollector"""
    return idf.newidfobject('WATERUSE:RAINCOLLECTOR', **kwargs)

def WateruseStorage(idf, **kwargs: Unpack[WateruseStorageType]):
    """"helper for WateruseStorage"""
    return idf.newidfobject('WATERUSE:STORAGE', **kwargs)

def WateruseWell(idf, **kwargs: Unpack[WateruseWellType]):
    """"helper for WateruseWell"""
    return idf.newidfobject('WATERUSE:WELL', **kwargs)

def WeatherpropertySkytemperature(idf, **kwargs: Unpack[WeatherpropertySkytemperatureType]):
    """"helper for WeatherpropertySkytemperature"""
    return idf.newidfobject('WEATHERPROPERTY:SKYTEMPERATURE', **kwargs)

def Window(idf, **kwargs: Unpack[WindowType]):
    """"helper for Window"""
    return idf.newidfobject('WINDOW', **kwargs)

def WindowInterzone(idf, **kwargs: Unpack[WindowInterzoneType]):
    """"helper for WindowInterzone"""
    return idf.newidfobject('WINDOW:INTERZONE', **kwargs)

def WindowgapDeflectionstate(idf, **kwargs: Unpack[WindowgapDeflectionstateType]):
    """"helper for WindowgapDeflectionstate"""
    return idf.newidfobject('WINDOWGAP:DEFLECTIONSTATE', **kwargs)

def WindowgapSupportpillar(idf, **kwargs: Unpack[WindowgapSupportpillarType]):
    """"helper for WindowgapSupportpillar"""
    return idf.newidfobject('WINDOWGAP:SUPPORTPILLAR', **kwargs)

def WindowmaterialBlind(idf, **kwargs: Unpack[WindowmaterialBlindType]):
    """"helper for WindowmaterialBlind"""
    return idf.newidfobject('WINDOWMATERIAL:BLIND', **kwargs)

def WindowmaterialBlindEquivalentlayer(idf, **kwargs: Unpack[WindowmaterialBlindEquivalentlayerType]):
    """"helper for WindowmaterialBlindEquivalentlayer"""
    return idf.newidfobject('WINDOWMATERIAL:BLIND:EQUIVALENTLAYER', **kwargs)

def WindowmaterialComplexshade(idf, **kwargs: Unpack[WindowmaterialComplexshadeType]):
    """"helper for WindowmaterialComplexshade"""
    return idf.newidfobject('WINDOWMATERIAL:COMPLEXSHADE', **kwargs)

def WindowmaterialDrapeEquivalentlayer(idf, **kwargs: Unpack[WindowmaterialDrapeEquivalentlayerType]):
    """"helper for WindowmaterialDrapeEquivalentlayer"""
    return idf.newidfobject('WINDOWMATERIAL:DRAPE:EQUIVALENTLAYER', **kwargs)

def WindowmaterialGap(idf, **kwargs: Unpack[WindowmaterialGapType]):
    """"helper for WindowmaterialGap"""
    return idf.newidfobject('WINDOWMATERIAL:GAP', **kwargs)

def WindowmaterialGapEquivalentlayer(idf, **kwargs: Unpack[WindowmaterialGapEquivalentlayerType]):
    """"helper for WindowmaterialGapEquivalentlayer"""
    return idf.newidfobject('WINDOWMATERIAL:GAP:EQUIVALENTLAYER', **kwargs)

def WindowmaterialGas(idf, **kwargs: Unpack[WindowmaterialGasType]):
    """"helper for WindowmaterialGas"""
    return idf.newidfobject('WINDOWMATERIAL:GAS', **kwargs)

def WindowmaterialGasmixture(idf, **kwargs: Unpack[WindowmaterialGasmixtureType]):
    """"helper for WindowmaterialGasmixture"""
    return idf.newidfobject('WINDOWMATERIAL:GASMIXTURE', **kwargs)

def WindowmaterialGlazing(idf, **kwargs: Unpack[WindowmaterialGlazingType]):
    """"helper for WindowmaterialGlazing"""
    return idf.newidfobject('WINDOWMATERIAL:GLAZING', **kwargs)

def WindowmaterialGlazingEquivalentlayer(idf, **kwargs: Unpack[WindowmaterialGlazingEquivalentlayerType]):
    """"helper for WindowmaterialGlazingEquivalentlayer"""
    return idf.newidfobject('WINDOWMATERIAL:GLAZING:EQUIVALENTLAYER', **kwargs)

def WindowmaterialGlazingRefractionextinctionmethod(idf, **kwargs: Unpack[WindowmaterialGlazingRefractionextinctionmethodType]):
    """"helper for WindowmaterialGlazingRefractionextinctionmethod"""
    return idf.newidfobject('WINDOWMATERIAL:GLAZING:REFRACTIONEXTINCTIONMETHOD', **kwargs)

def WindowmaterialGlazinggroupThermochromic(idf, **kwargs: Unpack[WindowmaterialGlazinggroupThermochromicType]):
    """"helper for WindowmaterialGlazinggroupThermochromic"""
    return idf.newidfobject('WINDOWMATERIAL:GLAZINGGROUP:THERMOCHROMIC', **kwargs)

def WindowmaterialScreen(idf, **kwargs: Unpack[WindowmaterialScreenType]):
    """"helper for WindowmaterialScreen"""
    return idf.newidfobject('WINDOWMATERIAL:SCREEN', **kwargs)

def WindowmaterialScreenEquivalentlayer(idf, **kwargs: Unpack[WindowmaterialScreenEquivalentlayerType]):
    """"helper for WindowmaterialScreenEquivalentlayer"""
    return idf.newidfobject('WINDOWMATERIAL:SCREEN:EQUIVALENTLAYER', **kwargs)

def WindowmaterialShade(idf, **kwargs: Unpack[WindowmaterialShadeType]):
    """"helper for WindowmaterialShade"""
    return idf.newidfobject('WINDOWMATERIAL:SHADE', **kwargs)

def WindowmaterialShadeEquivalentlayer(idf, **kwargs: Unpack[WindowmaterialShadeEquivalentlayerType]):
    """"helper for WindowmaterialShadeEquivalentlayer"""
    return idf.newidfobject('WINDOWMATERIAL:SHADE:EQUIVALENTLAYER', **kwargs)

def WindowmaterialSimpleglazingsystem(idf, **kwargs: Unpack[WindowmaterialSimpleglazingsystemType]):
    """"helper for WindowmaterialSimpleglazingsystem"""
    return idf.newidfobject('WINDOWMATERIAL:SIMPLEGLAZINGSYSTEM', **kwargs)

def WindowpropertyAirflowcontrol(idf, **kwargs: Unpack[WindowpropertyAirflowcontrolType]):
    """"helper for WindowpropertyAirflowcontrol"""
    return idf.newidfobject('WINDOWPROPERTY:AIRFLOWCONTROL', **kwargs)

def WindowpropertyFrameanddivider(idf, **kwargs: Unpack[WindowpropertyFrameanddividerType]):
    """"helper for WindowpropertyFrameanddivider"""
    return idf.newidfobject('WINDOWPROPERTY:FRAMEANDDIVIDER', **kwargs)

def WindowpropertyStormwindow(idf, **kwargs: Unpack[WindowpropertyStormwindowType]):
    """"helper for WindowpropertyStormwindow"""
    return idf.newidfobject('WINDOWPROPERTY:STORMWINDOW', **kwargs)

def Windowscalculationengine(idf, **kwargs: Unpack[WindowscalculationengineType]):
    """"helper for Windowscalculationengine"""
    return idf.newidfobject('WINDOWSCALCULATIONENGINE', **kwargs)

def Windowshadingcontrol(idf, **kwargs: Unpack[WindowshadingcontrolType]):
    """"helper for Windowshadingcontrol"""
    return idf.newidfobject('WINDOWSHADINGCONTROL', **kwargs)

def WindowthermalmodelParams(idf, **kwargs: Unpack[WindowthermalmodelParamsType]):
    """"helper for WindowthermalmodelParams"""
    return idf.newidfobject('WINDOWTHERMALMODEL:PARAMS', **kwargs)

def Zone(idf, **kwargs: Unpack[ZoneType]):
    """"helper for Zone"""
    return idf.newidfobject('ZONE', **kwargs)

def ZoneairbalanceOutdoorair(idf, **kwargs: Unpack[ZoneairbalanceOutdoorairType]):
    """"helper for ZoneairbalanceOutdoorair"""
    return idf.newidfobject('ZONEAIRBALANCE:OUTDOORAIR', **kwargs)

def Zoneaircontaminantbalance(idf, **kwargs: Unpack[ZoneaircontaminantbalanceType]):
    """"helper for Zoneaircontaminantbalance"""
    return idf.newidfobject('ZONEAIRCONTAMINANTBALANCE', **kwargs)

def Zoneairheatbalancealgorithm(idf, **kwargs: Unpack[ZoneairheatbalancealgorithmType]):
    """"helper for Zoneairheatbalancealgorithm"""
    return idf.newidfobject('ZONEAIRHEATBALANCEALGORITHM', **kwargs)

def Zoneairmassflowconservation(idf, **kwargs: Unpack[ZoneairmassflowconservationType]):
    """"helper for Zoneairmassflowconservation"""
    return idf.newidfobject('ZONEAIRMASSFLOWCONSERVATION', **kwargs)

def ZonebaseboardOutdoortemperaturecontrolled(idf, **kwargs: Unpack[ZonebaseboardOutdoortemperaturecontrolledType]):
    """"helper for ZonebaseboardOutdoortemperaturecontrolled"""
    return idf.newidfobject('ZONEBASEBOARD:OUTDOORTEMPERATURECONTROLLED', **kwargs)

def ZonecapacitancemultiplierResearchspecial(idf, **kwargs: Unpack[ZonecapacitancemultiplierResearchspecialType]):
    """"helper for ZonecapacitancemultiplierResearchspecial"""
    return idf.newidfobject('ZONECAPACITANCEMULTIPLIER:RESEARCHSPECIAL', **kwargs)

def ZonecontaminantsourceandsinkCarbondioxide(idf, **kwargs: Unpack[ZonecontaminantsourceandsinkCarbondioxideType]):
    """"helper for ZonecontaminantsourceandsinkCarbondioxide"""
    return idf.newidfobject('ZONECONTAMINANTSOURCEANDSINK:CARBONDIOXIDE', **kwargs)

def ZonecontaminantsourceandsinkGenericConstant(idf, **kwargs: Unpack[ZonecontaminantsourceandsinkGenericConstantType]):
    """"helper for ZonecontaminantsourceandsinkGenericConstant"""
    return idf.newidfobject('ZONECONTAMINANTSOURCEANDSINK:GENERIC:CONSTANT', **kwargs)

def ZonecontaminantsourceandsinkGenericCutoffmodel(idf, **kwargs: Unpack[ZonecontaminantsourceandsinkGenericCutoffmodelType]):
    """"helper for ZonecontaminantsourceandsinkGenericCutoffmodel"""
    return idf.newidfobject('ZONECONTAMINANTSOURCEANDSINK:GENERIC:CUTOFFMODEL', **kwargs)

def ZonecontaminantsourceandsinkGenericDecaysource(idf, **kwargs: Unpack[ZonecontaminantsourceandsinkGenericDecaysourceType]):
    """"helper for ZonecontaminantsourceandsinkGenericDecaysource"""
    return idf.newidfobject('ZONECONTAMINANTSOURCEANDSINK:GENERIC:DECAYSOURCE', **kwargs)

def ZonecontaminantsourceandsinkGenericDepositionratesink(idf, **kwargs: Unpack[ZonecontaminantsourceandsinkGenericDepositionratesinkType]):
    """"helper for ZonecontaminantsourceandsinkGenericDepositionratesink"""
    return idf.newidfobject('ZONECONTAMINANTSOURCEANDSINK:GENERIC:DEPOSITIONRATESINK', **kwargs)

def ZonecontrolContaminantcontroller(idf, **kwargs: Unpack[ZonecontrolContaminantcontrollerType]):
    """"helper for ZonecontrolContaminantcontroller"""
    return idf.newidfobject('ZONECONTROL:CONTAMINANTCONTROLLER', **kwargs)

def ZonecontrolHumidistat(idf, **kwargs: Unpack[ZonecontrolHumidistatType]):
    """"helper for ZonecontrolHumidistat"""
    return idf.newidfobject('ZONECONTROL:HUMIDISTAT', **kwargs)

def ZonecontrolThermostat(idf, **kwargs: Unpack[ZonecontrolThermostatType]):
    """"helper for ZonecontrolThermostat"""
    return idf.newidfobject('ZONECONTROL:THERMOSTAT', **kwargs)

def ZonecontrolThermostatOperativetemperature(idf, **kwargs: Unpack[ZonecontrolThermostatOperativetemperatureType]):
    """"helper for ZonecontrolThermostatOperativetemperature"""
    return idf.newidfobject('ZONECONTROL:THERMOSTAT:OPERATIVETEMPERATURE', **kwargs)

def ZonecontrolThermostatStageddualsetpoint(idf, **kwargs: Unpack[ZonecontrolThermostatStageddualsetpointType]):
    """"helper for ZonecontrolThermostatStageddualsetpoint"""
    return idf.newidfobject('ZONECONTROL:THERMOSTAT:STAGEDDUALSETPOINT', **kwargs)

def ZonecontrolThermostatTemperatureandhumidity(idf, **kwargs: Unpack[ZonecontrolThermostatTemperatureandhumidityType]):
    """"helper for ZonecontrolThermostatTemperatureandhumidity"""
    return idf.newidfobject('ZONECONTROL:THERMOSTAT:TEMPERATUREANDHUMIDITY', **kwargs)

def ZonecontrolThermostatThermalcomfort(idf, **kwargs: Unpack[ZonecontrolThermostatThermalcomfortType]):
    """"helper for ZonecontrolThermostatThermalcomfort"""
    return idf.newidfobject('ZONECONTROL:THERMOSTAT:THERMALCOMFORT', **kwargs)

def ZonecooltowerShower(idf, **kwargs: Unpack[ZonecooltowerShowerType]):
    """"helper for ZonecooltowerShower"""
    return idf.newidfobject('ZONECOOLTOWER:SHOWER', **kwargs)

def Zonecrossmixing(idf, **kwargs: Unpack[ZonecrossmixingType]):
    """"helper for Zonecrossmixing"""
    return idf.newidfobject('ZONECROSSMIXING', **kwargs)

def Zoneearthtube(idf, **kwargs: Unpack[ZoneearthtubeType]):
    """"helper for Zoneearthtube"""
    return idf.newidfobject('ZONEEARTHTUBE', **kwargs)

def ZoneearthtubeParameters(idf, **kwargs: Unpack[ZoneearthtubeParametersType]):
    """"helper for ZoneearthtubeParameters"""
    return idf.newidfobject('ZONEEARTHTUBE:PARAMETERS', **kwargs)

def Zonegroup(idf, **kwargs: Unpack[ZonegroupType]):
    """"helper for Zonegroup"""
    return idf.newidfobject('ZONEGROUP', **kwargs)

def ZonehvacAirdistributionunit(idf, **kwargs: Unpack[ZonehvacAirdistributionunitType]):
    """"helper for ZonehvacAirdistributionunit"""
    return idf.newidfobject('ZONEHVAC:AIRDISTRIBUTIONUNIT', **kwargs)

def ZonehvacBaseboardConvectiveElectric(idf, **kwargs: Unpack[ZonehvacBaseboardConvectiveElectricType]):
    """"helper for ZonehvacBaseboardConvectiveElectric"""
    return idf.newidfobject('ZONEHVAC:BASEBOARD:CONVECTIVE:ELECTRIC', **kwargs)

def ZonehvacBaseboardConvectiveWater(idf, **kwargs: Unpack[ZonehvacBaseboardConvectiveWaterType]):
    """"helper for ZonehvacBaseboardConvectiveWater"""
    return idf.newidfobject('ZONEHVAC:BASEBOARD:CONVECTIVE:WATER', **kwargs)

def ZonehvacBaseboardRadiantconvectiveElectric(idf, **kwargs: Unpack[ZonehvacBaseboardRadiantconvectiveElectricType]):
    """"helper for ZonehvacBaseboardRadiantconvectiveElectric"""
    return idf.newidfobject('ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:ELECTRIC', **kwargs)

def ZonehvacBaseboardRadiantconvectiveSteam(idf, **kwargs: Unpack[ZonehvacBaseboardRadiantconvectiveSteamType]):
    """"helper for ZonehvacBaseboardRadiantconvectiveSteam"""
    return idf.newidfobject('ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:STEAM', **kwargs)

def ZonehvacBaseboardRadiantconvectiveSteamDesign(idf, **kwargs: Unpack[ZonehvacBaseboardRadiantconvectiveSteamDesignType]):
    """"helper for ZonehvacBaseboardRadiantconvectiveSteamDesign"""
    return idf.newidfobject('ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:STEAM:DESIGN', **kwargs)

def ZonehvacBaseboardRadiantconvectiveWater(idf, **kwargs: Unpack[ZonehvacBaseboardRadiantconvectiveWaterType]):
    """"helper for ZonehvacBaseboardRadiantconvectiveWater"""
    return idf.newidfobject('ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:WATER', **kwargs)

def ZonehvacBaseboardRadiantconvectiveWaterDesign(idf, **kwargs: Unpack[ZonehvacBaseboardRadiantconvectiveWaterDesignType]):
    """"helper for ZonehvacBaseboardRadiantconvectiveWaterDesign"""
    return idf.newidfobject('ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:WATER:DESIGN', **kwargs)

def ZonehvacCoolingpanelRadiantconvectiveWater(idf, **kwargs: Unpack[ZonehvacCoolingpanelRadiantconvectiveWaterType]):
    """"helper for ZonehvacCoolingpanelRadiantconvectiveWater"""
    return idf.newidfobject('ZONEHVAC:COOLINGPANEL:RADIANTCONVECTIVE:WATER', **kwargs)

def ZonehvacDehumidifierDx(idf, **kwargs: Unpack[ZonehvacDehumidifierDxType]):
    """"helper for ZonehvacDehumidifierDx"""
    return idf.newidfobject('ZONEHVAC:DEHUMIDIFIER:DX', **kwargs)

def ZonehvacEnergyrecoveryventilator(idf, **kwargs: Unpack[ZonehvacEnergyrecoveryventilatorType]):
    """"helper for ZonehvacEnergyrecoveryventilator"""
    return idf.newidfobject('ZONEHVAC:ENERGYRECOVERYVENTILATOR', **kwargs)

def ZonehvacEnergyrecoveryventilatorController(idf, **kwargs: Unpack[ZonehvacEnergyrecoveryventilatorControllerType]):
    """"helper for ZonehvacEnergyrecoveryventilatorController"""
    return idf.newidfobject('ZONEHVAC:ENERGYRECOVERYVENTILATOR:CONTROLLER', **kwargs)

def ZonehvacEquipmentconnections(idf, **kwargs: Unpack[ZonehvacEquipmentconnectionsType]):
    """"helper for ZonehvacEquipmentconnections"""
    return idf.newidfobject('ZONEHVAC:EQUIPMENTCONNECTIONS', **kwargs)

def ZonehvacEquipmentlist(idf, **kwargs: Unpack[ZonehvacEquipmentlistType]):
    """"helper for ZonehvacEquipmentlist"""
    return idf.newidfobject('ZONEHVAC:EQUIPMENTLIST', **kwargs)

def ZonehvacEvaporativecoolerunit(idf, **kwargs: Unpack[ZonehvacEvaporativecoolerunitType]):
    """"helper for ZonehvacEvaporativecoolerunit"""
    return idf.newidfobject('ZONEHVAC:EVAPORATIVECOOLERUNIT', **kwargs)

def ZonehvacExhaustcontrol(idf, **kwargs: Unpack[ZonehvacExhaustcontrolType]):
    """"helper for ZonehvacExhaustcontrol"""
    return idf.newidfobject('ZONEHVAC:EXHAUSTCONTROL', **kwargs)

def ZonehvacForcedairUserdefined(idf, **kwargs: Unpack[ZonehvacForcedairUserdefinedType]):
    """"helper for ZonehvacForcedairUserdefined"""
    return idf.newidfobject('ZONEHVAC:FORCEDAIR:USERDEFINED', **kwargs)

def ZonehvacFourpipefancoil(idf, **kwargs: Unpack[ZonehvacFourpipefancoilType]):
    """"helper for ZonehvacFourpipefancoil"""
    return idf.newidfobject('ZONEHVAC:FOURPIPEFANCOIL', **kwargs)

def ZonehvacHightemperatureradiant(idf, **kwargs: Unpack[ZonehvacHightemperatureradiantType]):
    """"helper for ZonehvacHightemperatureradiant"""
    return idf.newidfobject('ZONEHVAC:HIGHTEMPERATURERADIANT', **kwargs)

def ZonehvacHybridunitaryhvac(idf, **kwargs: Unpack[ZonehvacHybridunitaryhvacType]):
    """"helper for ZonehvacHybridunitaryhvac"""
    return idf.newidfobject('ZONEHVAC:HYBRIDUNITARYHVAC', **kwargs)

def ZonehvacIdealloadsairsystem(idf, **kwargs: Unpack[ZonehvacIdealloadsairsystemType]):
    """"helper for ZonehvacIdealloadsairsystem"""
    return idf.newidfobject('ZONEHVAC:IDEALLOADSAIRSYSTEM', **kwargs)

def ZonehvacLowtemperatureradiantConstantflow(idf, **kwargs: Unpack[ZonehvacLowtemperatureradiantConstantflowType]):
    """"helper for ZonehvacLowtemperatureradiantConstantflow"""
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:CONSTANTFLOW', **kwargs)

def ZonehvacLowtemperatureradiantConstantflowDesign(idf, **kwargs: Unpack[ZonehvacLowtemperatureradiantConstantflowDesignType]):
    """"helper for ZonehvacLowtemperatureradiantConstantflowDesign"""
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:CONSTANTFLOW:DESIGN', **kwargs)

def ZonehvacLowtemperatureradiantElectric(idf, **kwargs: Unpack[ZonehvacLowtemperatureradiantElectricType]):
    """"helper for ZonehvacLowtemperatureradiantElectric"""
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:ELECTRIC', **kwargs)

def ZonehvacLowtemperatureradiantSurfacegroup(idf, **kwargs: Unpack[ZonehvacLowtemperatureradiantSurfacegroupType]):
    """"helper for ZonehvacLowtemperatureradiantSurfacegroup"""
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:SURFACEGROUP', **kwargs)

def ZonehvacLowtemperatureradiantVariableflow(idf, **kwargs: Unpack[ZonehvacLowtemperatureradiantVariableflowType]):
    """"helper for ZonehvacLowtemperatureradiantVariableflow"""
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:VARIABLEFLOW', **kwargs)

def ZonehvacLowtemperatureradiantVariableflowDesign(idf, **kwargs: Unpack[ZonehvacLowtemperatureradiantVariableflowDesignType]):
    """"helper for ZonehvacLowtemperatureradiantVariableflowDesign"""
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:VARIABLEFLOW:DESIGN', **kwargs)

def ZonehvacOutdoorairunit(idf, **kwargs: Unpack[ZonehvacOutdoorairunitType]):
    """"helper for ZonehvacOutdoorairunit"""
    return idf.newidfobject('ZONEHVAC:OUTDOORAIRUNIT', **kwargs)

def ZonehvacOutdoorairunitEquipmentlist(idf, **kwargs: Unpack[ZonehvacOutdoorairunitEquipmentlistType]):
    """"helper for ZonehvacOutdoorairunitEquipmentlist"""
    return idf.newidfobject('ZONEHVAC:OUTDOORAIRUNIT:EQUIPMENTLIST', **kwargs)

def ZonehvacPackagedterminalairconditioner(idf, **kwargs: Unpack[ZonehvacPackagedterminalairconditionerType]):
    """"helper for ZonehvacPackagedterminalairconditioner"""
    return idf.newidfobject('ZONEHVAC:PACKAGEDTERMINALAIRCONDITIONER', **kwargs)

def ZonehvacPackagedterminalheatpump(idf, **kwargs: Unpack[ZonehvacPackagedterminalheatpumpType]):
    """"helper for ZonehvacPackagedterminalheatpump"""
    return idf.newidfobject('ZONEHVAC:PACKAGEDTERMINALHEATPUMP', **kwargs)

def ZonehvacRefrigerationchillerset(idf, **kwargs: Unpack[ZonehvacRefrigerationchillersetType]):
    """"helper for ZonehvacRefrigerationchillerset"""
    return idf.newidfobject('ZONEHVAC:REFRIGERATIONCHILLERSET', **kwargs)

def ZonehvacTerminalunitVariablerefrigerantflow(idf, **kwargs: Unpack[ZonehvacTerminalunitVariablerefrigerantflowType]):
    """"helper for ZonehvacTerminalunitVariablerefrigerantflow"""
    return idf.newidfobject('ZONEHVAC:TERMINALUNIT:VARIABLEREFRIGERANTFLOW', **kwargs)

def ZonehvacUnitheater(idf, **kwargs: Unpack[ZonehvacUnitheaterType]):
    """"helper for ZonehvacUnitheater"""
    return idf.newidfobject('ZONEHVAC:UNITHEATER', **kwargs)

def ZonehvacUnitventilator(idf, **kwargs: Unpack[ZonehvacUnitventilatorType]):
    """"helper for ZonehvacUnitventilator"""
    return idf.newidfobject('ZONEHVAC:UNITVENTILATOR', **kwargs)

def ZonehvacVentilatedslab(idf, **kwargs: Unpack[ZonehvacVentilatedslabType]):
    """"helper for ZonehvacVentilatedslab"""
    return idf.newidfobject('ZONEHVAC:VENTILATEDSLAB', **kwargs)

def ZonehvacVentilatedslabSlabgroup(idf, **kwargs: Unpack[ZonehvacVentilatedslabSlabgroupType]):
    """"helper for ZonehvacVentilatedslabSlabgroup"""
    return idf.newidfobject('ZONEHVAC:VENTILATEDSLAB:SLABGROUP', **kwargs)

def ZonehvacWatertoairheatpump(idf, **kwargs: Unpack[ZonehvacWatertoairheatpumpType]):
    """"helper for ZonehvacWatertoairheatpump"""
    return idf.newidfobject('ZONEHVAC:WATERTOAIRHEATPUMP', **kwargs)

def ZonehvacWindowairconditioner(idf, **kwargs: Unpack[ZonehvacWindowairconditionerType]):
    """"helper for ZonehvacWindowairconditioner"""
    return idf.newidfobject('ZONEHVAC:WINDOWAIRCONDITIONER', **kwargs)

def ZoneinfiltrationDesignflowrate(idf, **kwargs: Unpack[ZoneinfiltrationDesignflowrateType]):
    """"helper for ZoneinfiltrationDesignflowrate"""
    return idf.newidfobject('ZONEINFILTRATION:DESIGNFLOWRATE', **kwargs)

def ZoneinfiltrationEffectiveleakagearea(idf, **kwargs: Unpack[ZoneinfiltrationEffectiveleakageareaType]):
    """"helper for ZoneinfiltrationEffectiveleakagearea"""
    return idf.newidfobject('ZONEINFILTRATION:EFFECTIVELEAKAGEAREA', **kwargs)

def ZoneinfiltrationFlowcoefficient(idf, **kwargs: Unpack[ZoneinfiltrationFlowcoefficientType]):
    """"helper for ZoneinfiltrationFlowcoefficient"""
    return idf.newidfobject('ZONEINFILTRATION:FLOWCOEFFICIENT', **kwargs)

def Zonelist(idf, **kwargs: Unpack[ZonelistType]):
    """"helper for Zonelist"""
    return idf.newidfobject('ZONELIST', **kwargs)

def Zonemixing(idf, **kwargs: Unpack[ZonemixingType]):
    """"helper for Zonemixing"""
    return idf.newidfobject('ZONEMIXING', **kwargs)

def ZonepropertyLocalenvironment(idf, **kwargs: Unpack[ZonepropertyLocalenvironmentType]):
    """"helper for ZonepropertyLocalenvironment"""
    return idf.newidfobject('ZONEPROPERTY:LOCALENVIRONMENT', **kwargs)

def ZonepropertyUserviewfactorsBysurfacename(idf, **kwargs: Unpack[ZonepropertyUserviewfactorsBysurfacenameType]):
    """"helper for ZonepropertyUserviewfactorsBysurfacename"""
    return idf.newidfobject('ZONEPROPERTY:USERVIEWFACTORS:BYSURFACENAME', **kwargs)

def Zonerefrigerationdoormixing(idf, **kwargs: Unpack[ZonerefrigerationdoormixingType]):
    """"helper for Zonerefrigerationdoormixing"""
    return idf.newidfobject('ZONEREFRIGERATIONDOORMIXING', **kwargs)

def Zoneterminalunitlist(idf, **kwargs: Unpack[ZoneterminalunitlistType]):
    """"helper for Zoneterminalunitlist"""
    return idf.newidfobject('ZONETERMINALUNITLIST', **kwargs)

def Zonethermalchimney(idf, **kwargs: Unpack[ZonethermalchimneyType]):
    """"helper for Zonethermalchimney"""
    return idf.newidfobject('ZONETHERMALCHIMNEY', **kwargs)

def ZoneventilationDesignflowrate(idf, **kwargs: Unpack[ZoneventilationDesignflowrateType]):
    """"helper for ZoneventilationDesignflowrate"""
    return idf.newidfobject('ZONEVENTILATION:DESIGNFLOWRATE', **kwargs)

def ZoneventilationWindandstackopenarea(idf, **kwargs: Unpack[ZoneventilationWindandstackopenareaType]):
    """"helper for ZoneventilationWindandstackopenarea"""
    return idf.newidfobject('ZONEVENTILATION:WINDANDSTACKOPENAREA', **kwargs)
