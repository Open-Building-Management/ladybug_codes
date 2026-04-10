from __future__ import annotations
from .idf_types_short import *

def AirconditionerVariablerefrigerantflow(idf, **kwargs: Unpack[AirconditionerVariablerefrigerantflowType]):
    """"helper for AirconditionerVariablerefrigerantflow"""
    return idf.newidfobject('AIRCONDITIONER:VARIABLEREFRIGERANTFLOW', **kwargs)
class AirconditionerVariablerefrigerantflowMeta:
    idf_name = 'AIRCONDITIONER:VARIABLEREFRIGERANTFLOW'

def AirconditionerVariablerefrigerantflowFluidtemperaturecontrol(idf, **kwargs: Unpack[AirconditionerVariablerefrigerantflowFluidtemperaturecontrolType]):
    """"helper for AirconditionerVariablerefrigerantflowFluidtemperaturecontrol"""
    return idf.newidfobject('AIRCONDITIONER:VARIABLEREFRIGERANTFLOW:FLUIDTEMPERATURECONTROL', **kwargs)
class AirconditionerVariablerefrigerantflowFluidtemperaturecontrolMeta:
    idf_name = 'AIRCONDITIONER:VARIABLEREFRIGERANTFLOW:FLUIDTEMPERATURECONTROL'

def AirconditionerVariablerefrigerantflowFluidtemperaturecontrolHr(idf, **kwargs: Unpack[AirconditionerVariablerefrigerantflowFluidtemperaturecontrolHrType]):
    """"helper for AirconditionerVariablerefrigerantflowFluidtemperaturecontrolHr"""
    return idf.newidfobject('AIRCONDITIONER:VARIABLEREFRIGERANTFLOW:FLUIDTEMPERATURECONTROL:HR', **kwargs)
class AirconditionerVariablerefrigerantflowFluidtemperaturecontrolHrMeta:
    idf_name = 'AIRCONDITIONER:VARIABLEREFRIGERANTFLOW:FLUIDTEMPERATURECONTROL:HR'

def AirflownetworkDistributionComponentCoil(idf, **kwargs: Unpack[AirflownetworkDistributionComponentCoilType]):
    """"helper for AirflownetworkDistributionComponentCoil"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:COIL', **kwargs)
class AirflownetworkDistributionComponentCoilMeta:
    idf_name = 'AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:COIL'

def AirflownetworkDistributionComponentConstantpressuredrop(idf, **kwargs: Unpack[AirflownetworkDistributionComponentConstantpressuredropType]):
    """"helper for AirflownetworkDistributionComponentConstantpressuredrop"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:CONSTANTPRESSUREDROP', **kwargs)
class AirflownetworkDistributionComponentConstantpressuredropMeta:
    idf_name = 'AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:CONSTANTPRESSUREDROP'

def AirflownetworkDistributionComponentDuct(idf, **kwargs: Unpack[AirflownetworkDistributionComponentDuctType]):
    """"helper for AirflownetworkDistributionComponentDuct"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:DUCT', **kwargs)
class AirflownetworkDistributionComponentDuctMeta:
    idf_name = 'AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:DUCT'

def AirflownetworkDistributionComponentFan(idf, **kwargs: Unpack[AirflownetworkDistributionComponentFanType]):
    """"helper for AirflownetworkDistributionComponentFan"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:FAN', **kwargs)
class AirflownetworkDistributionComponentFanMeta:
    idf_name = 'AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:FAN'

def AirflownetworkDistributionComponentHeatexchanger(idf, **kwargs: Unpack[AirflownetworkDistributionComponentHeatexchangerType]):
    """"helper for AirflownetworkDistributionComponentHeatexchanger"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:HEATEXCHANGER', **kwargs)
class AirflownetworkDistributionComponentHeatexchangerMeta:
    idf_name = 'AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:HEATEXCHANGER'

def AirflownetworkDistributionComponentLeak(idf, **kwargs: Unpack[AirflownetworkDistributionComponentLeakType]):
    """"helper for AirflownetworkDistributionComponentLeak"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:LEAK', **kwargs)
class AirflownetworkDistributionComponentLeakMeta:
    idf_name = 'AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:LEAK'

def AirflownetworkDistributionComponentLeakageratio(idf, **kwargs: Unpack[AirflownetworkDistributionComponentLeakageratioType]):
    """"helper for AirflownetworkDistributionComponentLeakageratio"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:LEAKAGERATIO', **kwargs)
class AirflownetworkDistributionComponentLeakageratioMeta:
    idf_name = 'AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:LEAKAGERATIO'

def AirflownetworkDistributionComponentOutdoorairflow(idf, **kwargs: Unpack[AirflownetworkDistributionComponentOutdoorairflowType]):
    """"helper for AirflownetworkDistributionComponentOutdoorairflow"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:OUTDOORAIRFLOW', **kwargs)
class AirflownetworkDistributionComponentOutdoorairflowMeta:
    idf_name = 'AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:OUTDOORAIRFLOW'

def AirflownetworkDistributionComponentReliefairflow(idf, **kwargs: Unpack[AirflownetworkDistributionComponentReliefairflowType]):
    """"helper for AirflownetworkDistributionComponentReliefairflow"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:RELIEFAIRFLOW', **kwargs)
class AirflownetworkDistributionComponentReliefairflowMeta:
    idf_name = 'AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:RELIEFAIRFLOW'

def AirflownetworkDistributionComponentTerminalunit(idf, **kwargs: Unpack[AirflownetworkDistributionComponentTerminalunitType]):
    """"helper for AirflownetworkDistributionComponentTerminalunit"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:TERMINALUNIT', **kwargs)
class AirflownetworkDistributionComponentTerminalunitMeta:
    idf_name = 'AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:TERMINALUNIT'

def AirflownetworkDistributionDuctsizing(idf, **kwargs: Unpack[AirflownetworkDistributionDuctsizingType]):
    """"helper for AirflownetworkDistributionDuctsizing"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:DUCTSIZING', **kwargs)
class AirflownetworkDistributionDuctsizingMeta:
    idf_name = 'AIRFLOWNETWORK:DISTRIBUTION:DUCTSIZING'

def AirflownetworkDistributionDuctviewfactors(idf, **kwargs: Unpack[AirflownetworkDistributionDuctviewfactorsType]):
    """"helper for AirflownetworkDistributionDuctviewfactors"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:DUCTVIEWFACTORS', **kwargs)
class AirflownetworkDistributionDuctviewfactorsMeta:
    idf_name = 'AIRFLOWNETWORK:DISTRIBUTION:DUCTVIEWFACTORS'

def AirflownetworkDistributionLinkage(idf, **kwargs: Unpack[AirflownetworkDistributionLinkageType]):
    """"helper for AirflownetworkDistributionLinkage"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:LINKAGE', **kwargs)
class AirflownetworkDistributionLinkageMeta:
    idf_name = 'AIRFLOWNETWORK:DISTRIBUTION:LINKAGE'

def AirflownetworkDistributionNode(idf, **kwargs: Unpack[AirflownetworkDistributionNodeType]):
    """"helper for AirflownetworkDistributionNode"""
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:NODE', **kwargs)
class AirflownetworkDistributionNodeMeta:
    idf_name = 'AIRFLOWNETWORK:DISTRIBUTION:NODE'

def AirflownetworkIntrazoneLinkage(idf, **kwargs: Unpack[AirflownetworkIntrazoneLinkageType]):
    """"helper for AirflownetworkIntrazoneLinkage"""
    return idf.newidfobject('AIRFLOWNETWORK:INTRAZONE:LINKAGE', **kwargs)
class AirflownetworkIntrazoneLinkageMeta:
    idf_name = 'AIRFLOWNETWORK:INTRAZONE:LINKAGE'

def AirflownetworkIntrazoneNode(idf, **kwargs: Unpack[AirflownetworkIntrazoneNodeType]):
    """"helper for AirflownetworkIntrazoneNode"""
    return idf.newidfobject('AIRFLOWNETWORK:INTRAZONE:NODE', **kwargs)
class AirflownetworkIntrazoneNodeMeta:
    idf_name = 'AIRFLOWNETWORK:INTRAZONE:NODE'

def AirflownetworkMultizoneComponentDetailedopening(idf, **kwargs: Unpack[AirflownetworkMultizoneComponentDetailedopeningType]):
    """"helper for AirflownetworkMultizoneComponentDetailedopening"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:COMPONENT:DETAILEDOPENING', **kwargs)
class AirflownetworkMultizoneComponentDetailedopeningMeta:
    idf_name = 'AIRFLOWNETWORK:MULTIZONE:COMPONENT:DETAILEDOPENING'

def AirflownetworkMultizoneComponentHorizontalopening(idf, **kwargs: Unpack[AirflownetworkMultizoneComponentHorizontalopeningType]):
    """"helper for AirflownetworkMultizoneComponentHorizontalopening"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:COMPONENT:HORIZONTALOPENING', **kwargs)
class AirflownetworkMultizoneComponentHorizontalopeningMeta:
    idf_name = 'AIRFLOWNETWORK:MULTIZONE:COMPONENT:HORIZONTALOPENING'

def AirflownetworkMultizoneComponentSimpleopening(idf, **kwargs: Unpack[AirflownetworkMultizoneComponentSimpleopeningType]):
    """"helper for AirflownetworkMultizoneComponentSimpleopening"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:COMPONENT:SIMPLEOPENING', **kwargs)
class AirflownetworkMultizoneComponentSimpleopeningMeta:
    idf_name = 'AIRFLOWNETWORK:MULTIZONE:COMPONENT:SIMPLEOPENING'

def AirflownetworkMultizoneComponentZoneexhaustfan(idf, **kwargs: Unpack[AirflownetworkMultizoneComponentZoneexhaustfanType]):
    """"helper for AirflownetworkMultizoneComponentZoneexhaustfan"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:COMPONENT:ZONEEXHAUSTFAN', **kwargs)
class AirflownetworkMultizoneComponentZoneexhaustfanMeta:
    idf_name = 'AIRFLOWNETWORK:MULTIZONE:COMPONENT:ZONEEXHAUSTFAN'

def AirflownetworkMultizoneExternalnode(idf, **kwargs: Unpack[AirflownetworkMultizoneExternalnodeType]):
    """"helper for AirflownetworkMultizoneExternalnode"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:EXTERNALNODE', **kwargs)
class AirflownetworkMultizoneExternalnodeMeta:
    idf_name = 'AIRFLOWNETWORK:MULTIZONE:EXTERNALNODE'

def AirflownetworkMultizoneReferencecrackconditions(idf, **kwargs: Unpack[AirflownetworkMultizoneReferencecrackconditionsType]):
    """"helper for AirflownetworkMultizoneReferencecrackconditions"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:REFERENCECRACKCONDITIONS', **kwargs)
class AirflownetworkMultizoneReferencecrackconditionsMeta:
    idf_name = 'AIRFLOWNETWORK:MULTIZONE:REFERENCECRACKCONDITIONS'

def AirflownetworkMultizoneSpecifiedflowrate(idf, **kwargs: Unpack[AirflownetworkMultizoneSpecifiedflowrateType]):
    """"helper for AirflownetworkMultizoneSpecifiedflowrate"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:SPECIFIEDFLOWRATE', **kwargs)
class AirflownetworkMultizoneSpecifiedflowrateMeta:
    idf_name = 'AIRFLOWNETWORK:MULTIZONE:SPECIFIEDFLOWRATE'

def AirflownetworkMultizoneSurface(idf, **kwargs: Unpack[AirflownetworkMultizoneSurfaceType]):
    """"helper for AirflownetworkMultizoneSurface"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:SURFACE', **kwargs)
class AirflownetworkMultizoneSurfaceMeta:
    idf_name = 'AIRFLOWNETWORK:MULTIZONE:SURFACE'

def AirflownetworkMultizoneSurfaceCrack(idf, **kwargs: Unpack[AirflownetworkMultizoneSurfaceCrackType]):
    """"helper for AirflownetworkMultizoneSurfaceCrack"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:SURFACE:CRACK', **kwargs)
class AirflownetworkMultizoneSurfaceCrackMeta:
    idf_name = 'AIRFLOWNETWORK:MULTIZONE:SURFACE:CRACK'

def AirflownetworkMultizoneSurfaceEffectiveleakagearea(idf, **kwargs: Unpack[AirflownetworkMultizoneSurfaceEffectiveleakageareaType]):
    """"helper for AirflownetworkMultizoneSurfaceEffectiveleakagearea"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:SURFACE:EFFECTIVELEAKAGEAREA', **kwargs)
class AirflownetworkMultizoneSurfaceEffectiveleakageareaMeta:
    idf_name = 'AIRFLOWNETWORK:MULTIZONE:SURFACE:EFFECTIVELEAKAGEAREA'

def AirflownetworkMultizoneWindpressurecoefficientarray(idf, **kwargs: Unpack[AirflownetworkMultizoneWindpressurecoefficientarrayType]):
    """"helper for AirflownetworkMultizoneWindpressurecoefficientarray"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:WINDPRESSURECOEFFICIENTARRAY', **kwargs)
class AirflownetworkMultizoneWindpressurecoefficientarrayMeta:
    idf_name = 'AIRFLOWNETWORK:MULTIZONE:WINDPRESSURECOEFFICIENTARRAY'

def AirflownetworkMultizoneWindpressurecoefficientvalues(idf, **kwargs: Unpack[AirflownetworkMultizoneWindpressurecoefficientvaluesType]):
    """"helper for AirflownetworkMultizoneWindpressurecoefficientvalues"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:WINDPRESSURECOEFFICIENTVALUES', **kwargs)
class AirflownetworkMultizoneWindpressurecoefficientvaluesMeta:
    idf_name = 'AIRFLOWNETWORK:MULTIZONE:WINDPRESSURECOEFFICIENTVALUES'

def AirflownetworkMultizoneZone(idf, **kwargs: Unpack[AirflownetworkMultizoneZoneType]):
    """"helper for AirflownetworkMultizoneZone"""
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:ZONE', **kwargs)
class AirflownetworkMultizoneZoneMeta:
    idf_name = 'AIRFLOWNETWORK:MULTIZONE:ZONE'

def AirflownetworkOccupantventilationcontrol(idf, **kwargs: Unpack[AirflownetworkOccupantventilationcontrolType]):
    """"helper for AirflownetworkOccupantventilationcontrol"""
    return idf.newidfobject('AIRFLOWNETWORK:OCCUPANTVENTILATIONCONTROL', **kwargs)
class AirflownetworkOccupantventilationcontrolMeta:
    idf_name = 'AIRFLOWNETWORK:OCCUPANTVENTILATIONCONTROL'

def AirflownetworkSimulationcontrol(idf, **kwargs: Unpack[AirflownetworkSimulationcontrolType]):
    """"helper for AirflownetworkSimulationcontrol"""
    return idf.newidfobject('AIRFLOWNETWORK:SIMULATIONCONTROL', **kwargs)
class AirflownetworkSimulationcontrolMeta:
    idf_name = 'AIRFLOWNETWORK:SIMULATIONCONTROL'

def AirflownetworkZonecontrolPressurecontroller(idf, **kwargs: Unpack[AirflownetworkZonecontrolPressurecontrollerType]):
    """"helper for AirflownetworkZonecontrolPressurecontroller"""
    return idf.newidfobject('AIRFLOWNETWORK:ZONECONTROL:PRESSURECONTROLLER', **kwargs)
class AirflownetworkZonecontrolPressurecontrollerMeta:
    idf_name = 'AIRFLOWNETWORK:ZONECONTROL:PRESSURECONTROLLER'

def Airloophvac(idf, **kwargs: Unpack[AirloophvacType]):
    """"helper for Airloophvac"""
    return idf.newidfobject('AIRLOOPHVAC', **kwargs)
class AirloophvacMeta:
    idf_name = 'AIRLOOPHVAC'

def AirloophvacControllerlist(idf, **kwargs: Unpack[AirloophvacControllerlistType]):
    """"helper for AirloophvacControllerlist"""
    return idf.newidfobject('AIRLOOPHVAC:CONTROLLERLIST', **kwargs)
class AirloophvacControllerlistMeta:
    idf_name = 'AIRLOOPHVAC:CONTROLLERLIST'

def AirloophvacDedicatedoutdoorairsystem(idf, **kwargs: Unpack[AirloophvacDedicatedoutdoorairsystemType]):
    """"helper for AirloophvacDedicatedoutdoorairsystem"""
    return idf.newidfobject('AIRLOOPHVAC:DEDICATEDOUTDOORAIRSYSTEM', **kwargs)
class AirloophvacDedicatedoutdoorairsystemMeta:
    idf_name = 'AIRLOOPHVAC:DEDICATEDOUTDOORAIRSYSTEM'

def AirloophvacExhaustsystem(idf, **kwargs: Unpack[AirloophvacExhaustsystemType]):
    """"helper for AirloophvacExhaustsystem"""
    return idf.newidfobject('AIRLOOPHVAC:EXHAUSTSYSTEM', **kwargs)
class AirloophvacExhaustsystemMeta:
    idf_name = 'AIRLOOPHVAC:EXHAUSTSYSTEM'

def AirloophvacMixer(idf, **kwargs: Unpack[AirloophvacMixerType]):
    """"helper for AirloophvacMixer"""
    return idf.newidfobject('AIRLOOPHVAC:MIXER', **kwargs)
class AirloophvacMixerMeta:
    idf_name = 'AIRLOOPHVAC:MIXER'

def AirloophvacOutdoorairsystem(idf, **kwargs: Unpack[AirloophvacOutdoorairsystemType]):
    """"helper for AirloophvacOutdoorairsystem"""
    return idf.newidfobject('AIRLOOPHVAC:OUTDOORAIRSYSTEM', **kwargs)
class AirloophvacOutdoorairsystemMeta:
    idf_name = 'AIRLOOPHVAC:OUTDOORAIRSYSTEM'

def AirloophvacOutdoorairsystemEquipmentlist(idf, **kwargs: Unpack[AirloophvacOutdoorairsystemEquipmentlistType]):
    """"helper for AirloophvacOutdoorairsystemEquipmentlist"""
    return idf.newidfobject('AIRLOOPHVAC:OUTDOORAIRSYSTEM:EQUIPMENTLIST', **kwargs)
class AirloophvacOutdoorairsystemEquipmentlistMeta:
    idf_name = 'AIRLOOPHVAC:OUTDOORAIRSYSTEM:EQUIPMENTLIST'

def AirloophvacReturnpath(idf, **kwargs: Unpack[AirloophvacReturnpathType]):
    """"helper for AirloophvacReturnpath"""
    return idf.newidfobject('AIRLOOPHVAC:RETURNPATH', **kwargs)
class AirloophvacReturnpathMeta:
    idf_name = 'AIRLOOPHVAC:RETURNPATH'

def AirloophvacReturnplenum(idf, **kwargs: Unpack[AirloophvacReturnplenumType]):
    """"helper for AirloophvacReturnplenum"""
    return idf.newidfobject('AIRLOOPHVAC:RETURNPLENUM', **kwargs)
class AirloophvacReturnplenumMeta:
    idf_name = 'AIRLOOPHVAC:RETURNPLENUM'

def AirloophvacSplitter(idf, **kwargs: Unpack[AirloophvacSplitterType]):
    """"helper for AirloophvacSplitter"""
    return idf.newidfobject('AIRLOOPHVAC:SPLITTER', **kwargs)
class AirloophvacSplitterMeta:
    idf_name = 'AIRLOOPHVAC:SPLITTER'

def AirloophvacSupplypath(idf, **kwargs: Unpack[AirloophvacSupplypathType]):
    """"helper for AirloophvacSupplypath"""
    return idf.newidfobject('AIRLOOPHVAC:SUPPLYPATH', **kwargs)
class AirloophvacSupplypathMeta:
    idf_name = 'AIRLOOPHVAC:SUPPLYPATH'

def AirloophvacSupplyplenum(idf, **kwargs: Unpack[AirloophvacSupplyplenumType]):
    """"helper for AirloophvacSupplyplenum"""
    return idf.newidfobject('AIRLOOPHVAC:SUPPLYPLENUM', **kwargs)
class AirloophvacSupplyplenumMeta:
    idf_name = 'AIRLOOPHVAC:SUPPLYPLENUM'

def AirloophvacUnitaryFurnaceHeatcool(idf, **kwargs: Unpack[AirloophvacUnitaryFurnaceHeatcoolType]):
    """"helper for AirloophvacUnitaryFurnaceHeatcool"""
    return idf.newidfobject('AIRLOOPHVAC:UNITARY:FURNACE:HEATCOOL', **kwargs)
class AirloophvacUnitaryFurnaceHeatcoolMeta:
    idf_name = 'AIRLOOPHVAC:UNITARY:FURNACE:HEATCOOL'

def AirloophvacUnitaryFurnaceHeatonly(idf, **kwargs: Unpack[AirloophvacUnitaryFurnaceHeatonlyType]):
    """"helper for AirloophvacUnitaryFurnaceHeatonly"""
    return idf.newidfobject('AIRLOOPHVAC:UNITARY:FURNACE:HEATONLY', **kwargs)
class AirloophvacUnitaryFurnaceHeatonlyMeta:
    idf_name = 'AIRLOOPHVAC:UNITARY:FURNACE:HEATONLY'

def AirloophvacUnitaryheatcool(idf, **kwargs: Unpack[AirloophvacUnitaryheatcoolType]):
    """"helper for AirloophvacUnitaryheatcool"""
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATCOOL', **kwargs)
class AirloophvacUnitaryheatcoolMeta:
    idf_name = 'AIRLOOPHVAC:UNITARYHEATCOOL'

def AirloophvacUnitaryheatcoolVavchangeoverbypass(idf, **kwargs: Unpack[AirloophvacUnitaryheatcoolVavchangeoverbypassType]):
    """"helper for AirloophvacUnitaryheatcoolVavchangeoverbypass"""
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATCOOL:VAVCHANGEOVERBYPASS', **kwargs)
class AirloophvacUnitaryheatcoolVavchangeoverbypassMeta:
    idf_name = 'AIRLOOPHVAC:UNITARYHEATCOOL:VAVCHANGEOVERBYPASS'

def AirloophvacUnitaryheatonly(idf, **kwargs: Unpack[AirloophvacUnitaryheatonlyType]):
    """"helper for AirloophvacUnitaryheatonly"""
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATONLY', **kwargs)
class AirloophvacUnitaryheatonlyMeta:
    idf_name = 'AIRLOOPHVAC:UNITARYHEATONLY'

def AirloophvacUnitaryheatpumpAirtoair(idf, **kwargs: Unpack[AirloophvacUnitaryheatpumpAirtoairType]):
    """"helper for AirloophvacUnitaryheatpumpAirtoair"""
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATPUMP:AIRTOAIR', **kwargs)
class AirloophvacUnitaryheatpumpAirtoairMeta:
    idf_name = 'AIRLOOPHVAC:UNITARYHEATPUMP:AIRTOAIR'

def AirloophvacUnitaryheatpumpAirtoairMultispeed(idf, **kwargs: Unpack[AirloophvacUnitaryheatpumpAirtoairMultispeedType]):
    """"helper for AirloophvacUnitaryheatpumpAirtoairMultispeed"""
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATPUMP:AIRTOAIR:MULTISPEED', **kwargs)
class AirloophvacUnitaryheatpumpAirtoairMultispeedMeta:
    idf_name = 'AIRLOOPHVAC:UNITARYHEATPUMP:AIRTOAIR:MULTISPEED'

def AirloophvacUnitaryheatpumpWatertoair(idf, **kwargs: Unpack[AirloophvacUnitaryheatpumpWatertoairType]):
    """"helper for AirloophvacUnitaryheatpumpWatertoair"""
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATPUMP:WATERTOAIR', **kwargs)
class AirloophvacUnitaryheatpumpWatertoairMeta:
    idf_name = 'AIRLOOPHVAC:UNITARYHEATPUMP:WATERTOAIR'

def AirloophvacUnitarysystem(idf, **kwargs: Unpack[AirloophvacUnitarysystemType]):
    """"helper for AirloophvacUnitarysystem"""
    return idf.newidfobject('AIRLOOPHVAC:UNITARYSYSTEM', **kwargs)
class AirloophvacUnitarysystemMeta:
    idf_name = 'AIRLOOPHVAC:UNITARYSYSTEM'

def AirloophvacZonemixer(idf, **kwargs: Unpack[AirloophvacZonemixerType]):
    """"helper for AirloophvacZonemixer"""
    return idf.newidfobject('AIRLOOPHVAC:ZONEMIXER', **kwargs)
class AirloophvacZonemixerMeta:
    idf_name = 'AIRLOOPHVAC:ZONEMIXER'

def AirloophvacZonesplitter(idf, **kwargs: Unpack[AirloophvacZonesplitterType]):
    """"helper for AirloophvacZonesplitter"""
    return idf.newidfobject('AIRLOOPHVAC:ZONESPLITTER', **kwargs)
class AirloophvacZonesplitterMeta:
    idf_name = 'AIRLOOPHVAC:ZONESPLITTER'

def AirterminalDualductConstantvolume(idf, **kwargs: Unpack[AirterminalDualductConstantvolumeType]):
    """"helper for AirterminalDualductConstantvolume"""
    return idf.newidfobject('AIRTERMINAL:DUALDUCT:CONSTANTVOLUME', **kwargs)
class AirterminalDualductConstantvolumeMeta:
    idf_name = 'AIRTERMINAL:DUALDUCT:CONSTANTVOLUME'

def AirterminalDualductVav(idf, **kwargs: Unpack[AirterminalDualductVavType]):
    """"helper for AirterminalDualductVav"""
    return idf.newidfobject('AIRTERMINAL:DUALDUCT:VAV', **kwargs)
class AirterminalDualductVavMeta:
    idf_name = 'AIRTERMINAL:DUALDUCT:VAV'

def AirterminalDualductVavOutdoorair(idf, **kwargs: Unpack[AirterminalDualductVavOutdoorairType]):
    """"helper for AirterminalDualductVavOutdoorair"""
    return idf.newidfobject('AIRTERMINAL:DUALDUCT:VAV:OUTDOORAIR', **kwargs)
class AirterminalDualductVavOutdoorairMeta:
    idf_name = 'AIRTERMINAL:DUALDUCT:VAV:OUTDOORAIR'

def AirterminalSingleductConstantvolumeCooledbeam(idf, **kwargs: Unpack[AirterminalSingleductConstantvolumeCooledbeamType]):
    """"helper for AirterminalSingleductConstantvolumeCooledbeam"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:COOLEDBEAM', **kwargs)
class AirterminalSingleductConstantvolumeCooledbeamMeta:
    idf_name = 'AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:COOLEDBEAM'

def AirterminalSingleductConstantvolumeFourpipebeam(idf, **kwargs: Unpack[AirterminalSingleductConstantvolumeFourpipebeamType]):
    """"helper for AirterminalSingleductConstantvolumeFourpipebeam"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:FOURPIPEBEAM', **kwargs)
class AirterminalSingleductConstantvolumeFourpipebeamMeta:
    idf_name = 'AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:FOURPIPEBEAM'

def AirterminalSingleductConstantvolumeFourpipeinduction(idf, **kwargs: Unpack[AirterminalSingleductConstantvolumeFourpipeinductionType]):
    """"helper for AirterminalSingleductConstantvolumeFourpipeinduction"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:FOURPIPEINDUCTION', **kwargs)
class AirterminalSingleductConstantvolumeFourpipeinductionMeta:
    idf_name = 'AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:FOURPIPEINDUCTION'

def AirterminalSingleductConstantvolumeNoreheat(idf, **kwargs: Unpack[AirterminalSingleductConstantvolumeNoreheatType]):
    """"helper for AirterminalSingleductConstantvolumeNoreheat"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:NOREHEAT', **kwargs)
class AirterminalSingleductConstantvolumeNoreheatMeta:
    idf_name = 'AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:NOREHEAT'

def AirterminalSingleductConstantvolumeReheat(idf, **kwargs: Unpack[AirterminalSingleductConstantvolumeReheatType]):
    """"helper for AirterminalSingleductConstantvolumeReheat"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:REHEAT', **kwargs)
class AirterminalSingleductConstantvolumeReheatMeta:
    idf_name = 'AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:REHEAT'

def AirterminalSingleductMixer(idf, **kwargs: Unpack[AirterminalSingleductMixerType]):
    """"helper for AirterminalSingleductMixer"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:MIXER', **kwargs)
class AirterminalSingleductMixerMeta:
    idf_name = 'AIRTERMINAL:SINGLEDUCT:MIXER'

def AirterminalSingleductParallelpiuReheat(idf, **kwargs: Unpack[AirterminalSingleductParallelpiuReheatType]):
    """"helper for AirterminalSingleductParallelpiuReheat"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:PARALLELPIU:REHEAT', **kwargs)
class AirterminalSingleductParallelpiuReheatMeta:
    idf_name = 'AIRTERMINAL:SINGLEDUCT:PARALLELPIU:REHEAT'

def AirterminalSingleductSeriespiuReheat(idf, **kwargs: Unpack[AirterminalSingleductSeriespiuReheatType]):
    """"helper for AirterminalSingleductSeriespiuReheat"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:SERIESPIU:REHEAT', **kwargs)
class AirterminalSingleductSeriespiuReheatMeta:
    idf_name = 'AIRTERMINAL:SINGLEDUCT:SERIESPIU:REHEAT'

def AirterminalSingleductUserdefined(idf, **kwargs: Unpack[AirterminalSingleductUserdefinedType]):
    """"helper for AirterminalSingleductUserdefined"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:USERDEFINED', **kwargs)
class AirterminalSingleductUserdefinedMeta:
    idf_name = 'AIRTERMINAL:SINGLEDUCT:USERDEFINED'

def AirterminalSingleductVavHeatandcoolNoreheat(idf, **kwargs: Unpack[AirterminalSingleductVavHeatandcoolNoreheatType]):
    """"helper for AirterminalSingleductVavHeatandcoolNoreheat"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:VAV:HEATANDCOOL:NOREHEAT', **kwargs)
class AirterminalSingleductVavHeatandcoolNoreheatMeta:
    idf_name = 'AIRTERMINAL:SINGLEDUCT:VAV:HEATANDCOOL:NOREHEAT'

def AirterminalSingleductVavHeatandcoolReheat(idf, **kwargs: Unpack[AirterminalSingleductVavHeatandcoolReheatType]):
    """"helper for AirterminalSingleductVavHeatandcoolReheat"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:VAV:HEATANDCOOL:REHEAT', **kwargs)
class AirterminalSingleductVavHeatandcoolReheatMeta:
    idf_name = 'AIRTERMINAL:SINGLEDUCT:VAV:HEATANDCOOL:REHEAT'

def AirterminalSingleductVavNoreheat(idf, **kwargs: Unpack[AirterminalSingleductVavNoreheatType]):
    """"helper for AirterminalSingleductVavNoreheat"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:VAV:NOREHEAT', **kwargs)
class AirterminalSingleductVavNoreheatMeta:
    idf_name = 'AIRTERMINAL:SINGLEDUCT:VAV:NOREHEAT'

def AirterminalSingleductVavReheat(idf, **kwargs: Unpack[AirterminalSingleductVavReheatType]):
    """"helper for AirterminalSingleductVavReheat"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:VAV:REHEAT', **kwargs)
class AirterminalSingleductVavReheatMeta:
    idf_name = 'AIRTERMINAL:SINGLEDUCT:VAV:REHEAT'

def AirterminalSingleductVavReheatVariablespeedfan(idf, **kwargs: Unpack[AirterminalSingleductVavReheatVariablespeedfanType]):
    """"helper for AirterminalSingleductVavReheatVariablespeedfan"""
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:VAV:REHEAT:VARIABLESPEEDFAN', **kwargs)
class AirterminalSingleductVavReheatVariablespeedfanMeta:
    idf_name = 'AIRTERMINAL:SINGLEDUCT:VAV:REHEAT:VARIABLESPEEDFAN'

def AvailabilitymanagerDifferentialthermostat(idf, **kwargs: Unpack[AvailabilitymanagerDifferentialthermostatType]):
    """"helper for AvailabilitymanagerDifferentialthermostat"""
    return idf.newidfobject('AVAILABILITYMANAGER:DIFFERENTIALTHERMOSTAT', **kwargs)
class AvailabilitymanagerDifferentialthermostatMeta:
    idf_name = 'AVAILABILITYMANAGER:DIFFERENTIALTHERMOSTAT'

def AvailabilitymanagerHightemperatureturnoff(idf, **kwargs: Unpack[AvailabilitymanagerHightemperatureturnoffType]):
    """"helper for AvailabilitymanagerHightemperatureturnoff"""
    return idf.newidfobject('AVAILABILITYMANAGER:HIGHTEMPERATURETURNOFF', **kwargs)
class AvailabilitymanagerHightemperatureturnoffMeta:
    idf_name = 'AVAILABILITYMANAGER:HIGHTEMPERATURETURNOFF'

def AvailabilitymanagerHightemperatureturnon(idf, **kwargs: Unpack[AvailabilitymanagerHightemperatureturnonType]):
    """"helper for AvailabilitymanagerHightemperatureturnon"""
    return idf.newidfobject('AVAILABILITYMANAGER:HIGHTEMPERATURETURNON', **kwargs)
class AvailabilitymanagerHightemperatureturnonMeta:
    idf_name = 'AVAILABILITYMANAGER:HIGHTEMPERATURETURNON'

def AvailabilitymanagerHybridventilation(idf, **kwargs: Unpack[AvailabilitymanagerHybridventilationType]):
    """"helper for AvailabilitymanagerHybridventilation"""
    return idf.newidfobject('AVAILABILITYMANAGER:HYBRIDVENTILATION', **kwargs)
class AvailabilitymanagerHybridventilationMeta:
    idf_name = 'AVAILABILITYMANAGER:HYBRIDVENTILATION'

def AvailabilitymanagerLowtemperatureturnoff(idf, **kwargs: Unpack[AvailabilitymanagerLowtemperatureturnoffType]):
    """"helper for AvailabilitymanagerLowtemperatureturnoff"""
    return idf.newidfobject('AVAILABILITYMANAGER:LOWTEMPERATURETURNOFF', **kwargs)
class AvailabilitymanagerLowtemperatureturnoffMeta:
    idf_name = 'AVAILABILITYMANAGER:LOWTEMPERATURETURNOFF'

def AvailabilitymanagerLowtemperatureturnon(idf, **kwargs: Unpack[AvailabilitymanagerLowtemperatureturnonType]):
    """"helper for AvailabilitymanagerLowtemperatureturnon"""
    return idf.newidfobject('AVAILABILITYMANAGER:LOWTEMPERATURETURNON', **kwargs)
class AvailabilitymanagerLowtemperatureturnonMeta:
    idf_name = 'AVAILABILITYMANAGER:LOWTEMPERATURETURNON'

def AvailabilitymanagerNightcycle(idf, **kwargs: Unpack[AvailabilitymanagerNightcycleType]):
    """"helper for AvailabilitymanagerNightcycle"""
    return idf.newidfobject('AVAILABILITYMANAGER:NIGHTCYCLE', **kwargs)
class AvailabilitymanagerNightcycleMeta:
    idf_name = 'AVAILABILITYMANAGER:NIGHTCYCLE'

def AvailabilitymanagerNightventilation(idf, **kwargs: Unpack[AvailabilitymanagerNightventilationType]):
    """"helper for AvailabilitymanagerNightventilation"""
    return idf.newidfobject('AVAILABILITYMANAGER:NIGHTVENTILATION', **kwargs)
class AvailabilitymanagerNightventilationMeta:
    idf_name = 'AVAILABILITYMANAGER:NIGHTVENTILATION'

def AvailabilitymanagerOptimumstart(idf, **kwargs: Unpack[AvailabilitymanagerOptimumstartType]):
    """"helper for AvailabilitymanagerOptimumstart"""
    return idf.newidfobject('AVAILABILITYMANAGER:OPTIMUMSTART', **kwargs)
class AvailabilitymanagerOptimumstartMeta:
    idf_name = 'AVAILABILITYMANAGER:OPTIMUMSTART'

def AvailabilitymanagerScheduled(idf, **kwargs: Unpack[AvailabilitymanagerScheduledType]):
    """"helper for AvailabilitymanagerScheduled"""
    return idf.newidfobject('AVAILABILITYMANAGER:SCHEDULED', **kwargs)
class AvailabilitymanagerScheduledMeta:
    idf_name = 'AVAILABILITYMANAGER:SCHEDULED'

def AvailabilitymanagerScheduledoff(idf, **kwargs: Unpack[AvailabilitymanagerScheduledoffType]):
    """"helper for AvailabilitymanagerScheduledoff"""
    return idf.newidfobject('AVAILABILITYMANAGER:SCHEDULEDOFF', **kwargs)
class AvailabilitymanagerScheduledoffMeta:
    idf_name = 'AVAILABILITYMANAGER:SCHEDULEDOFF'

def AvailabilitymanagerScheduledon(idf, **kwargs: Unpack[AvailabilitymanagerScheduledonType]):
    """"helper for AvailabilitymanagerScheduledon"""
    return idf.newidfobject('AVAILABILITYMANAGER:SCHEDULEDON', **kwargs)
class AvailabilitymanagerScheduledonMeta:
    idf_name = 'AVAILABILITYMANAGER:SCHEDULEDON'

def Availabilitymanagerassignmentlist(idf, **kwargs: Unpack[AvailabilitymanagerassignmentlistType]):
    """"helper for Availabilitymanagerassignmentlist"""
    return idf.newidfobject('AVAILABILITYMANAGERASSIGNMENTLIST', **kwargs)
class AvailabilitymanagerassignmentlistMeta:
    idf_name = 'AVAILABILITYMANAGERASSIGNMENTLIST'

def BoilerHotwater(idf, **kwargs: Unpack[BoilerHotwaterType]):
    """"helper for BoilerHotwater"""
    return idf.newidfobject('BOILER:HOTWATER', **kwargs)
class BoilerHotwaterMeta:
    idf_name = 'BOILER:HOTWATER'

def BoilerSteam(idf, **kwargs: Unpack[BoilerSteamType]):
    """"helper for BoilerSteam"""
    return idf.newidfobject('BOILER:STEAM', **kwargs)
class BoilerSteamMeta:
    idf_name = 'BOILER:STEAM'

def Branch(idf, **kwargs: Unpack[BranchType]):
    """"helper for Branch"""
    return idf.newidfobject('BRANCH', **kwargs)
class BranchMeta:
    idf_name = 'BRANCH'

def Branchlist(idf, **kwargs: Unpack[BranchlistType]):
    """"helper for Branchlist"""
    return idf.newidfobject('BRANCHLIST', **kwargs)
class BranchlistMeta:
    idf_name = 'BRANCHLIST'

def Building(idf, **kwargs: Unpack[BuildingType]):
    """"helper for Building"""
    return idf.newidfobject('BUILDING', **kwargs)
class BuildingMeta:
    idf_name = 'BUILDING'

def BuildingsurfaceDetailed(idf, **kwargs: Unpack[BuildingsurfaceDetailedType]):
    """"helper for BuildingsurfaceDetailed"""
    return idf.newidfobject('BUILDINGSURFACE:DETAILED', **kwargs)
class BuildingsurfaceDetailedMeta:
    idf_name = 'BUILDINGSURFACE:DETAILED'

def CeilingAdiabatic(idf, **kwargs: Unpack[CeilingAdiabaticType]):
    """"helper for CeilingAdiabatic"""
    return idf.newidfobject('CEILING:ADIABATIC', **kwargs)
class CeilingAdiabaticMeta:
    idf_name = 'CEILING:ADIABATIC'

def CeilingInterzone(idf, **kwargs: Unpack[CeilingInterzoneType]):
    """"helper for CeilingInterzone"""
    return idf.newidfobject('CEILING:INTERZONE', **kwargs)
class CeilingInterzoneMeta:
    idf_name = 'CEILING:INTERZONE'

def Centralheatpumpsystem(idf, **kwargs: Unpack[CentralheatpumpsystemType]):
    """"helper for Centralheatpumpsystem"""
    return idf.newidfobject('CENTRALHEATPUMPSYSTEM', **kwargs)
class CentralheatpumpsystemMeta:
    idf_name = 'CENTRALHEATPUMPSYSTEM'

def ChillerAbsorption(idf, **kwargs: Unpack[ChillerAbsorptionType]):
    """"helper for ChillerAbsorption"""
    return idf.newidfobject('CHILLER:ABSORPTION', **kwargs)
class ChillerAbsorptionMeta:
    idf_name = 'CHILLER:ABSORPTION'

def ChillerAbsorptionIndirect(idf, **kwargs: Unpack[ChillerAbsorptionIndirectType]):
    """"helper for ChillerAbsorptionIndirect"""
    return idf.newidfobject('CHILLER:ABSORPTION:INDIRECT', **kwargs)
class ChillerAbsorptionIndirectMeta:
    idf_name = 'CHILLER:ABSORPTION:INDIRECT'

def ChillerCombustionturbine(idf, **kwargs: Unpack[ChillerCombustionturbineType]):
    """"helper for ChillerCombustionturbine"""
    return idf.newidfobject('CHILLER:COMBUSTIONTURBINE', **kwargs)
class ChillerCombustionturbineMeta:
    idf_name = 'CHILLER:COMBUSTIONTURBINE'

def ChillerConstantcop(idf, **kwargs: Unpack[ChillerConstantcopType]):
    """"helper for ChillerConstantcop"""
    return idf.newidfobject('CHILLER:CONSTANTCOP', **kwargs)
class ChillerConstantcopMeta:
    idf_name = 'CHILLER:CONSTANTCOP'

def ChillerElectric(idf, **kwargs: Unpack[ChillerElectricType]):
    """"helper for ChillerElectric"""
    return idf.newidfobject('CHILLER:ELECTRIC', **kwargs)
class ChillerElectricMeta:
    idf_name = 'CHILLER:ELECTRIC'

def ChillerElectricAshrae205(idf, **kwargs: Unpack[ChillerElectricAshrae205Type]):
    """"helper for ChillerElectricAshrae205"""
    return idf.newidfobject('CHILLER:ELECTRIC:ASHRAE205', **kwargs)
class ChillerElectricAshrae205Meta:
    idf_name = 'CHILLER:ELECTRIC:ASHRAE205'

def ChillerElectricEir(idf, **kwargs: Unpack[ChillerElectricEirType]):
    """"helper for ChillerElectricEir"""
    return idf.newidfobject('CHILLER:ELECTRIC:EIR', **kwargs)
class ChillerElectricEirMeta:
    idf_name = 'CHILLER:ELECTRIC:EIR'

def ChillerElectricReformulatedeir(idf, **kwargs: Unpack[ChillerElectricReformulatedeirType]):
    """"helper for ChillerElectricReformulatedeir"""
    return idf.newidfobject('CHILLER:ELECTRIC:REFORMULATEDEIR', **kwargs)
class ChillerElectricReformulatedeirMeta:
    idf_name = 'CHILLER:ELECTRIC:REFORMULATEDEIR'

def ChillerEnginedriven(idf, **kwargs: Unpack[ChillerEnginedrivenType]):
    """"helper for ChillerEnginedriven"""
    return idf.newidfobject('CHILLER:ENGINEDRIVEN', **kwargs)
class ChillerEnginedrivenMeta:
    idf_name = 'CHILLER:ENGINEDRIVEN'

def ChillerheaterAbsorptionDirectfired(idf, **kwargs: Unpack[ChillerheaterAbsorptionDirectfiredType]):
    """"helper for ChillerheaterAbsorptionDirectfired"""
    return idf.newidfobject('CHILLERHEATER:ABSORPTION:DIRECTFIRED', **kwargs)
class ChillerheaterAbsorptionDirectfiredMeta:
    idf_name = 'CHILLERHEATER:ABSORPTION:DIRECTFIRED'

def ChillerheaterAbsorptionDoubleeffect(idf, **kwargs: Unpack[ChillerheaterAbsorptionDoubleeffectType]):
    """"helper for ChillerheaterAbsorptionDoubleeffect"""
    return idf.newidfobject('CHILLERHEATER:ABSORPTION:DOUBLEEFFECT', **kwargs)
class ChillerheaterAbsorptionDoubleeffectMeta:
    idf_name = 'CHILLERHEATER:ABSORPTION:DOUBLEEFFECT'

def ChillerheaterperformanceElectricEir(idf, **kwargs: Unpack[ChillerheaterperformanceElectricEirType]):
    """"helper for ChillerheaterperformanceElectricEir"""
    return idf.newidfobject('CHILLERHEATERPERFORMANCE:ELECTRIC:EIR', **kwargs)
class ChillerheaterperformanceElectricEirMeta:
    idf_name = 'CHILLERHEATERPERFORMANCE:ELECTRIC:EIR'

def CoilCoolingDx(idf, **kwargs: Unpack[CoilCoolingDxType]):
    """"helper for CoilCoolingDx"""
    return idf.newidfobject('COIL:COOLING:DX', **kwargs)
class CoilCoolingDxMeta:
    idf_name = 'COIL:COOLING:DX'

def CoilCoolingDxCurvefitOperatingmode(idf, **kwargs: Unpack[CoilCoolingDxCurvefitOperatingmodeType]):
    """"helper for CoilCoolingDxCurvefitOperatingmode"""
    return idf.newidfobject('COIL:COOLING:DX:CURVEFIT:OPERATINGMODE', **kwargs)
class CoilCoolingDxCurvefitOperatingmodeMeta:
    idf_name = 'COIL:COOLING:DX:CURVEFIT:OPERATINGMODE'

def CoilCoolingDxCurvefitPerformance(idf, **kwargs: Unpack[CoilCoolingDxCurvefitPerformanceType]):
    """"helper for CoilCoolingDxCurvefitPerformance"""
    return idf.newidfobject('COIL:COOLING:DX:CURVEFIT:PERFORMANCE', **kwargs)
class CoilCoolingDxCurvefitPerformanceMeta:
    idf_name = 'COIL:COOLING:DX:CURVEFIT:PERFORMANCE'

def CoilCoolingDxCurvefitSpeed(idf, **kwargs: Unpack[CoilCoolingDxCurvefitSpeedType]):
    """"helper for CoilCoolingDxCurvefitSpeed"""
    return idf.newidfobject('COIL:COOLING:DX:CURVEFIT:SPEED', **kwargs)
class CoilCoolingDxCurvefitSpeedMeta:
    idf_name = 'COIL:COOLING:DX:CURVEFIT:SPEED'

def CoilCoolingDxMultispeed(idf, **kwargs: Unpack[CoilCoolingDxMultispeedType]):
    """"helper for CoilCoolingDxMultispeed"""
    return idf.newidfobject('COIL:COOLING:DX:MULTISPEED', **kwargs)
class CoilCoolingDxMultispeedMeta:
    idf_name = 'COIL:COOLING:DX:MULTISPEED'

def CoilCoolingDxSinglespeed(idf, **kwargs: Unpack[CoilCoolingDxSinglespeedType]):
    """"helper for CoilCoolingDxSinglespeed"""
    return idf.newidfobject('COIL:COOLING:DX:SINGLESPEED', **kwargs)
class CoilCoolingDxSinglespeedMeta:
    idf_name = 'COIL:COOLING:DX:SINGLESPEED'

def CoilCoolingDxSinglespeedThermalstorage(idf, **kwargs: Unpack[CoilCoolingDxSinglespeedThermalstorageType]):
    """"helper for CoilCoolingDxSinglespeedThermalstorage"""
    return idf.newidfobject('COIL:COOLING:DX:SINGLESPEED:THERMALSTORAGE', **kwargs)
class CoilCoolingDxSinglespeedThermalstorageMeta:
    idf_name = 'COIL:COOLING:DX:SINGLESPEED:THERMALSTORAGE'

def CoilCoolingDxTwospeed(idf, **kwargs: Unpack[CoilCoolingDxTwospeedType]):
    """"helper for CoilCoolingDxTwospeed"""
    return idf.newidfobject('COIL:COOLING:DX:TWOSPEED', **kwargs)
class CoilCoolingDxTwospeedMeta:
    idf_name = 'COIL:COOLING:DX:TWOSPEED'

def CoilCoolingDxTwostagewithhumiditycontrolmode(idf, **kwargs: Unpack[CoilCoolingDxTwostagewithhumiditycontrolmodeType]):
    """"helper for CoilCoolingDxTwostagewithhumiditycontrolmode"""
    return idf.newidfobject('COIL:COOLING:DX:TWOSTAGEWITHHUMIDITYCONTROLMODE', **kwargs)
class CoilCoolingDxTwostagewithhumiditycontrolmodeMeta:
    idf_name = 'COIL:COOLING:DX:TWOSTAGEWITHHUMIDITYCONTROLMODE'

def CoilCoolingDxVariablerefrigerantflow(idf, **kwargs: Unpack[CoilCoolingDxVariablerefrigerantflowType]):
    """"helper for CoilCoolingDxVariablerefrigerantflow"""
    return idf.newidfobject('COIL:COOLING:DX:VARIABLEREFRIGERANTFLOW', **kwargs)
class CoilCoolingDxVariablerefrigerantflowMeta:
    idf_name = 'COIL:COOLING:DX:VARIABLEREFRIGERANTFLOW'

def CoilCoolingDxVariablerefrigerantflowFluidtemperaturecontrol(idf, **kwargs: Unpack[CoilCoolingDxVariablerefrigerantflowFluidtemperaturecontrolType]):
    """"helper for CoilCoolingDxVariablerefrigerantflowFluidtemperaturecontrol"""
    return idf.newidfobject('COIL:COOLING:DX:VARIABLEREFRIGERANTFLOW:FLUIDTEMPERATURECONTROL', **kwargs)
class CoilCoolingDxVariablerefrigerantflowFluidtemperaturecontrolMeta:
    idf_name = 'COIL:COOLING:DX:VARIABLEREFRIGERANTFLOW:FLUIDTEMPERATURECONTROL'

def CoilCoolingDxVariablespeed(idf, **kwargs: Unpack[CoilCoolingDxVariablespeedType]):
    """"helper for CoilCoolingDxVariablespeed"""
    return idf.newidfobject('COIL:COOLING:DX:VARIABLESPEED', **kwargs)
class CoilCoolingDxVariablespeedMeta:
    idf_name = 'COIL:COOLING:DX:VARIABLESPEED'

def CoilCoolingWater(idf, **kwargs: Unpack[CoilCoolingWaterType]):
    """"helper for CoilCoolingWater"""
    return idf.newidfobject('COIL:COOLING:WATER', **kwargs)
class CoilCoolingWaterMeta:
    idf_name = 'COIL:COOLING:WATER'

def CoilCoolingWaterDetailedgeometry(idf, **kwargs: Unpack[CoilCoolingWaterDetailedgeometryType]):
    """"helper for CoilCoolingWaterDetailedgeometry"""
    return idf.newidfobject('COIL:COOLING:WATER:DETAILEDGEOMETRY', **kwargs)
class CoilCoolingWaterDetailedgeometryMeta:
    idf_name = 'COIL:COOLING:WATER:DETAILEDGEOMETRY'

def CoilCoolingWatertoairheatpumpEquationfit(idf, **kwargs: Unpack[CoilCoolingWatertoairheatpumpEquationfitType]):
    """"helper for CoilCoolingWatertoairheatpumpEquationfit"""
    return idf.newidfobject('COIL:COOLING:WATERTOAIRHEATPUMP:EQUATIONFIT', **kwargs)
class CoilCoolingWatertoairheatpumpEquationfitMeta:
    idf_name = 'COIL:COOLING:WATERTOAIRHEATPUMP:EQUATIONFIT'

def CoilCoolingWatertoairheatpumpParameterestimation(idf, **kwargs: Unpack[CoilCoolingWatertoairheatpumpParameterestimationType]):
    """"helper for CoilCoolingWatertoairheatpumpParameterestimation"""
    return idf.newidfobject('COIL:COOLING:WATERTOAIRHEATPUMP:PARAMETERESTIMATION', **kwargs)
class CoilCoolingWatertoairheatpumpParameterestimationMeta:
    idf_name = 'COIL:COOLING:WATERTOAIRHEATPUMP:PARAMETERESTIMATION'

def CoilCoolingWatertoairheatpumpVariablespeedequationfit(idf, **kwargs: Unpack[CoilCoolingWatertoairheatpumpVariablespeedequationfitType]):
    """"helper for CoilCoolingWatertoairheatpumpVariablespeedequationfit"""
    return idf.newidfobject('COIL:COOLING:WATERTOAIRHEATPUMP:VARIABLESPEEDEQUATIONFIT', **kwargs)
class CoilCoolingWatertoairheatpumpVariablespeedequationfitMeta:
    idf_name = 'COIL:COOLING:WATERTOAIRHEATPUMP:VARIABLESPEEDEQUATIONFIT'

def CoilHeatingDesuperheater(idf, **kwargs: Unpack[CoilHeatingDesuperheaterType]):
    """"helper for CoilHeatingDesuperheater"""
    return idf.newidfobject('COIL:HEATING:DESUPERHEATER', **kwargs)
class CoilHeatingDesuperheaterMeta:
    idf_name = 'COIL:HEATING:DESUPERHEATER'

def CoilHeatingDxMultispeed(idf, **kwargs: Unpack[CoilHeatingDxMultispeedType]):
    """"helper for CoilHeatingDxMultispeed"""
    return idf.newidfobject('COIL:HEATING:DX:MULTISPEED', **kwargs)
class CoilHeatingDxMultispeedMeta:
    idf_name = 'COIL:HEATING:DX:MULTISPEED'

def CoilHeatingDxSinglespeed(idf, **kwargs: Unpack[CoilHeatingDxSinglespeedType]):
    """"helper for CoilHeatingDxSinglespeed"""
    return idf.newidfobject('COIL:HEATING:DX:SINGLESPEED', **kwargs)
class CoilHeatingDxSinglespeedMeta:
    idf_name = 'COIL:HEATING:DX:SINGLESPEED'

def CoilHeatingDxVariablerefrigerantflow(idf, **kwargs: Unpack[CoilHeatingDxVariablerefrigerantflowType]):
    """"helper for CoilHeatingDxVariablerefrigerantflow"""
    return idf.newidfobject('COIL:HEATING:DX:VARIABLEREFRIGERANTFLOW', **kwargs)
class CoilHeatingDxVariablerefrigerantflowMeta:
    idf_name = 'COIL:HEATING:DX:VARIABLEREFRIGERANTFLOW'

def CoilHeatingDxVariablerefrigerantflowFluidtemperaturecontrol(idf, **kwargs: Unpack[CoilHeatingDxVariablerefrigerantflowFluidtemperaturecontrolType]):
    """"helper for CoilHeatingDxVariablerefrigerantflowFluidtemperaturecontrol"""
    return idf.newidfobject('COIL:HEATING:DX:VARIABLEREFRIGERANTFLOW:FLUIDTEMPERATURECONTROL', **kwargs)
class CoilHeatingDxVariablerefrigerantflowFluidtemperaturecontrolMeta:
    idf_name = 'COIL:HEATING:DX:VARIABLEREFRIGERANTFLOW:FLUIDTEMPERATURECONTROL'

def CoilHeatingDxVariablespeed(idf, **kwargs: Unpack[CoilHeatingDxVariablespeedType]):
    """"helper for CoilHeatingDxVariablespeed"""
    return idf.newidfobject('COIL:HEATING:DX:VARIABLESPEED', **kwargs)
class CoilHeatingDxVariablespeedMeta:
    idf_name = 'COIL:HEATING:DX:VARIABLESPEED'

def CoilHeatingElectric(idf, **kwargs: Unpack[CoilHeatingElectricType]):
    """"helper for CoilHeatingElectric"""
    return idf.newidfobject('COIL:HEATING:ELECTRIC', **kwargs)
class CoilHeatingElectricMeta:
    idf_name = 'COIL:HEATING:ELECTRIC'

def CoilHeatingElectricMultistage(idf, **kwargs: Unpack[CoilHeatingElectricMultistageType]):
    """"helper for CoilHeatingElectricMultistage"""
    return idf.newidfobject('COIL:HEATING:ELECTRIC:MULTISTAGE', **kwargs)
class CoilHeatingElectricMultistageMeta:
    idf_name = 'COIL:HEATING:ELECTRIC:MULTISTAGE'

def CoilHeatingFuel(idf, **kwargs: Unpack[CoilHeatingFuelType]):
    """"helper for CoilHeatingFuel"""
    return idf.newidfobject('COIL:HEATING:FUEL', **kwargs)
class CoilHeatingFuelMeta:
    idf_name = 'COIL:HEATING:FUEL'

def CoilHeatingGasMultistage(idf, **kwargs: Unpack[CoilHeatingGasMultistageType]):
    """"helper for CoilHeatingGasMultistage"""
    return idf.newidfobject('COIL:HEATING:GAS:MULTISTAGE', **kwargs)
class CoilHeatingGasMultistageMeta:
    idf_name = 'COIL:HEATING:GAS:MULTISTAGE'

def CoilHeatingSteam(idf, **kwargs: Unpack[CoilHeatingSteamType]):
    """"helper for CoilHeatingSteam"""
    return idf.newidfobject('COIL:HEATING:STEAM', **kwargs)
class CoilHeatingSteamMeta:
    idf_name = 'COIL:HEATING:STEAM'

def CoilHeatingWater(idf, **kwargs: Unpack[CoilHeatingWaterType]):
    """"helper for CoilHeatingWater"""
    return idf.newidfobject('COIL:HEATING:WATER', **kwargs)
class CoilHeatingWaterMeta:
    idf_name = 'COIL:HEATING:WATER'

def CoilHeatingWatertoairheatpumpEquationfit(idf, **kwargs: Unpack[CoilHeatingWatertoairheatpumpEquationfitType]):
    """"helper for CoilHeatingWatertoairheatpumpEquationfit"""
    return idf.newidfobject('COIL:HEATING:WATERTOAIRHEATPUMP:EQUATIONFIT', **kwargs)
class CoilHeatingWatertoairheatpumpEquationfitMeta:
    idf_name = 'COIL:HEATING:WATERTOAIRHEATPUMP:EQUATIONFIT'

def CoilHeatingWatertoairheatpumpParameterestimation(idf, **kwargs: Unpack[CoilHeatingWatertoairheatpumpParameterestimationType]):
    """"helper for CoilHeatingWatertoairheatpumpParameterestimation"""
    return idf.newidfobject('COIL:HEATING:WATERTOAIRHEATPUMP:PARAMETERESTIMATION', **kwargs)
class CoilHeatingWatertoairheatpumpParameterestimationMeta:
    idf_name = 'COIL:HEATING:WATERTOAIRHEATPUMP:PARAMETERESTIMATION'

def CoilHeatingWatertoairheatpumpVariablespeedequationfit(idf, **kwargs: Unpack[CoilHeatingWatertoairheatpumpVariablespeedequationfitType]):
    """"helper for CoilHeatingWatertoairheatpumpVariablespeedequationfit"""
    return idf.newidfobject('COIL:HEATING:WATERTOAIRHEATPUMP:VARIABLESPEEDEQUATIONFIT', **kwargs)
class CoilHeatingWatertoairheatpumpVariablespeedequationfitMeta:
    idf_name = 'COIL:HEATING:WATERTOAIRHEATPUMP:VARIABLESPEEDEQUATIONFIT'

def CoilUserdefined(idf, **kwargs: Unpack[CoilUserdefinedType]):
    """"helper for CoilUserdefined"""
    return idf.newidfobject('COIL:USERDEFINED', **kwargs)
class CoilUserdefinedMeta:
    idf_name = 'COIL:USERDEFINED'

def CoilWaterheatingAirtowaterheatpumpPumped(idf, **kwargs: Unpack[CoilWaterheatingAirtowaterheatpumpPumpedType]):
    """"helper for CoilWaterheatingAirtowaterheatpumpPumped"""
    return idf.newidfobject('COIL:WATERHEATING:AIRTOWATERHEATPUMP:PUMPED', **kwargs)
class CoilWaterheatingAirtowaterheatpumpPumpedMeta:
    idf_name = 'COIL:WATERHEATING:AIRTOWATERHEATPUMP:PUMPED'

def CoilWaterheatingAirtowaterheatpumpVariablespeed(idf, **kwargs: Unpack[CoilWaterheatingAirtowaterheatpumpVariablespeedType]):
    """"helper for CoilWaterheatingAirtowaterheatpumpVariablespeed"""
    return idf.newidfobject('COIL:WATERHEATING:AIRTOWATERHEATPUMP:VARIABLESPEED', **kwargs)
class CoilWaterheatingAirtowaterheatpumpVariablespeedMeta:
    idf_name = 'COIL:WATERHEATING:AIRTOWATERHEATPUMP:VARIABLESPEED'

def CoilWaterheatingAirtowaterheatpumpWrapped(idf, **kwargs: Unpack[CoilWaterheatingAirtowaterheatpumpWrappedType]):
    """"helper for CoilWaterheatingAirtowaterheatpumpWrapped"""
    return idf.newidfobject('COIL:WATERHEATING:AIRTOWATERHEATPUMP:WRAPPED', **kwargs)
class CoilWaterheatingAirtowaterheatpumpWrappedMeta:
    idf_name = 'COIL:WATERHEATING:AIRTOWATERHEATPUMP:WRAPPED'

def CoilWaterheatingDesuperheater(idf, **kwargs: Unpack[CoilWaterheatingDesuperheaterType]):
    """"helper for CoilWaterheatingDesuperheater"""
    return idf.newidfobject('COIL:WATERHEATING:DESUPERHEATER', **kwargs)
class CoilWaterheatingDesuperheaterMeta:
    idf_name = 'COIL:WATERHEATING:DESUPERHEATER'

def CoilperformanceDxCooling(idf, **kwargs: Unpack[CoilperformanceDxCoolingType]):
    """"helper for CoilperformanceDxCooling"""
    return idf.newidfobject('COILPERFORMANCE:DX:COOLING', **kwargs)
class CoilperformanceDxCoolingMeta:
    idf_name = 'COILPERFORMANCE:DX:COOLING'

def CoilsystemCoolingDx(idf, **kwargs: Unpack[CoilsystemCoolingDxType]):
    """"helper for CoilsystemCoolingDx"""
    return idf.newidfobject('COILSYSTEM:COOLING:DX', **kwargs)
class CoilsystemCoolingDxMeta:
    idf_name = 'COILSYSTEM:COOLING:DX'

def CoilsystemCoolingDxHeatexchangerassisted(idf, **kwargs: Unpack[CoilsystemCoolingDxHeatexchangerassistedType]):
    """"helper for CoilsystemCoolingDxHeatexchangerassisted"""
    return idf.newidfobject('COILSYSTEM:COOLING:DX:HEATEXCHANGERASSISTED', **kwargs)
class CoilsystemCoolingDxHeatexchangerassistedMeta:
    idf_name = 'COILSYSTEM:COOLING:DX:HEATEXCHANGERASSISTED'

def CoilsystemCoolingWater(idf, **kwargs: Unpack[CoilsystemCoolingWaterType]):
    """"helper for CoilsystemCoolingWater"""
    return idf.newidfobject('COILSYSTEM:COOLING:WATER', **kwargs)
class CoilsystemCoolingWaterMeta:
    idf_name = 'COILSYSTEM:COOLING:WATER'

def CoilsystemCoolingWaterHeatexchangerassisted(idf, **kwargs: Unpack[CoilsystemCoolingWaterHeatexchangerassistedType]):
    """"helper for CoilsystemCoolingWaterHeatexchangerassisted"""
    return idf.newidfobject('COILSYSTEM:COOLING:WATER:HEATEXCHANGERASSISTED', **kwargs)
class CoilsystemCoolingWaterHeatexchangerassistedMeta:
    idf_name = 'COILSYSTEM:COOLING:WATER:HEATEXCHANGERASSISTED'

def CoilsystemHeatingDx(idf, **kwargs: Unpack[CoilsystemHeatingDxType]):
    """"helper for CoilsystemHeatingDx"""
    return idf.newidfobject('COILSYSTEM:HEATING:DX', **kwargs)
class CoilsystemHeatingDxMeta:
    idf_name = 'COILSYSTEM:HEATING:DX'

def CoilsystemIntegratedheatpumpAirsource(idf, **kwargs: Unpack[CoilsystemIntegratedheatpumpAirsourceType]):
    """"helper for CoilsystemIntegratedheatpumpAirsource"""
    return idf.newidfobject('COILSYSTEM:INTEGRATEDHEATPUMP:AIRSOURCE', **kwargs)
class CoilsystemIntegratedheatpumpAirsourceMeta:
    idf_name = 'COILSYSTEM:INTEGRATEDHEATPUMP:AIRSOURCE'

def Comfortviewfactorangles(idf, **kwargs: Unpack[ComfortviewfactoranglesType]):
    """"helper for Comfortviewfactorangles"""
    return idf.newidfobject('COMFORTVIEWFACTORANGLES', **kwargs)
class ComfortviewfactoranglesMeta:
    idf_name = 'COMFORTVIEWFACTORANGLES'

def ComplexfenestrationpropertySolarabsorbedlayers(idf, **kwargs: Unpack[ComplexfenestrationpropertySolarabsorbedlayersType]):
    """"helper for ComplexfenestrationpropertySolarabsorbedlayers"""
    return idf.newidfobject('COMPLEXFENESTRATIONPROPERTY:SOLARABSORBEDLAYERS', **kwargs)
class ComplexfenestrationpropertySolarabsorbedlayersMeta:
    idf_name = 'COMPLEXFENESTRATIONPROPERTY:SOLARABSORBEDLAYERS'

def ComplianceBuilding(idf, **kwargs: Unpack[ComplianceBuildingType]):
    """"helper for ComplianceBuilding"""
    return idf.newidfobject('COMPLIANCE:BUILDING', **kwargs)
class ComplianceBuildingMeta:
    idf_name = 'COMPLIANCE:BUILDING'

def ComponentcostAdjustments(idf, **kwargs: Unpack[ComponentcostAdjustmentsType]):
    """"helper for ComponentcostAdjustments"""
    return idf.newidfobject('COMPONENTCOST:ADJUSTMENTS', **kwargs)
class ComponentcostAdjustmentsMeta:
    idf_name = 'COMPONENTCOST:ADJUSTMENTS'

def ComponentcostLineitem(idf, **kwargs: Unpack[ComponentcostLineitemType]):
    """"helper for ComponentcostLineitem"""
    return idf.newidfobject('COMPONENTCOST:LINEITEM', **kwargs)
class ComponentcostLineitemMeta:
    idf_name = 'COMPONENTCOST:LINEITEM'

def ComponentcostReference(idf, **kwargs: Unpack[ComponentcostReferenceType]):
    """"helper for ComponentcostReference"""
    return idf.newidfobject('COMPONENTCOST:REFERENCE', **kwargs)
class ComponentcostReferenceMeta:
    idf_name = 'COMPONENTCOST:REFERENCE'

def Condenserequipmentlist(idf, **kwargs: Unpack[CondenserequipmentlistType]):
    """"helper for Condenserequipmentlist"""
    return idf.newidfobject('CONDENSEREQUIPMENTLIST', **kwargs)
class CondenserequipmentlistMeta:
    idf_name = 'CONDENSEREQUIPMENTLIST'

def Condenserequipmentoperationschemes(idf, **kwargs: Unpack[CondenserequipmentoperationschemesType]):
    """"helper for Condenserequipmentoperationschemes"""
    return idf.newidfobject('CONDENSEREQUIPMENTOPERATIONSCHEMES', **kwargs)
class CondenserequipmentoperationschemesMeta:
    idf_name = 'CONDENSEREQUIPMENTOPERATIONSCHEMES'

def Condenserloop(idf, **kwargs: Unpack[CondenserloopType]):
    """"helper for Condenserloop"""
    return idf.newidfobject('CONDENSERLOOP', **kwargs)
class CondenserloopMeta:
    idf_name = 'CONDENSERLOOP'

def ConnectorMixer(idf, **kwargs: Unpack[ConnectorMixerType]):
    """"helper for ConnectorMixer"""
    return idf.newidfobject('CONNECTOR:MIXER', **kwargs)
class ConnectorMixerMeta:
    idf_name = 'CONNECTOR:MIXER'

def ConnectorSplitter(idf, **kwargs: Unpack[ConnectorSplitterType]):
    """"helper for ConnectorSplitter"""
    return idf.newidfobject('CONNECTOR:SPLITTER', **kwargs)
class ConnectorSplitterMeta:
    idf_name = 'CONNECTOR:SPLITTER'

def Connectorlist(idf, **kwargs: Unpack[ConnectorlistType]):
    """"helper for Connectorlist"""
    return idf.newidfobject('CONNECTORLIST', **kwargs)
class ConnectorlistMeta:
    idf_name = 'CONNECTORLIST'

def Construction(idf, **kwargs: Unpack[ConstructionType]):
    """"helper for Construction"""
    return idf.newidfobject('CONSTRUCTION', **kwargs)
class ConstructionMeta:
    idf_name = 'CONSTRUCTION'

def ConstructionAirboundary(idf, **kwargs: Unpack[ConstructionAirboundaryType]):
    """"helper for ConstructionAirboundary"""
    return idf.newidfobject('CONSTRUCTION:AIRBOUNDARY', **kwargs)
class ConstructionAirboundaryMeta:
    idf_name = 'CONSTRUCTION:AIRBOUNDARY'

def ConstructionCfactorundergroundwall(idf, **kwargs: Unpack[ConstructionCfactorundergroundwallType]):
    """"helper for ConstructionCfactorundergroundwall"""
    return idf.newidfobject('CONSTRUCTION:CFACTORUNDERGROUNDWALL', **kwargs)
class ConstructionCfactorundergroundwallMeta:
    idf_name = 'CONSTRUCTION:CFACTORUNDERGROUNDWALL'

def ConstructionComplexfenestrationstate(idf, **kwargs: Unpack[ConstructionComplexfenestrationstateType]):
    """"helper for ConstructionComplexfenestrationstate"""
    return idf.newidfobject('CONSTRUCTION:COMPLEXFENESTRATIONSTATE', **kwargs)
class ConstructionComplexfenestrationstateMeta:
    idf_name = 'CONSTRUCTION:COMPLEXFENESTRATIONSTATE'

def ConstructionFfactorgroundfloor(idf, **kwargs: Unpack[ConstructionFfactorgroundfloorType]):
    """"helper for ConstructionFfactorgroundfloor"""
    return idf.newidfobject('CONSTRUCTION:FFACTORGROUNDFLOOR', **kwargs)
class ConstructionFfactorgroundfloorMeta:
    idf_name = 'CONSTRUCTION:FFACTORGROUNDFLOOR'

def ConstructionWindowdatafile(idf, **kwargs: Unpack[ConstructionWindowdatafileType]):
    """"helper for ConstructionWindowdatafile"""
    return idf.newidfobject('CONSTRUCTION:WINDOWDATAFILE', **kwargs)
class ConstructionWindowdatafileMeta:
    idf_name = 'CONSTRUCTION:WINDOWDATAFILE'

def ConstructionWindowequivalentlayer(idf, **kwargs: Unpack[ConstructionWindowequivalentlayerType]):
    """"helper for ConstructionWindowequivalentlayer"""
    return idf.newidfobject('CONSTRUCTION:WINDOWEQUIVALENTLAYER', **kwargs)
class ConstructionWindowequivalentlayerMeta:
    idf_name = 'CONSTRUCTION:WINDOWEQUIVALENTLAYER'

def ConstructionpropertyInternalheatsource(idf, **kwargs: Unpack[ConstructionpropertyInternalheatsourceType]):
    """"helper for ConstructionpropertyInternalheatsource"""
    return idf.newidfobject('CONSTRUCTIONPROPERTY:INTERNALHEATSOURCE', **kwargs)
class ConstructionpropertyInternalheatsourceMeta:
    idf_name = 'CONSTRUCTIONPROPERTY:INTERNALHEATSOURCE'

def ControllerMechanicalventilation(idf, **kwargs: Unpack[ControllerMechanicalventilationType]):
    """"helper for ControllerMechanicalventilation"""
    return idf.newidfobject('CONTROLLER:MECHANICALVENTILATION', **kwargs)
class ControllerMechanicalventilationMeta:
    idf_name = 'CONTROLLER:MECHANICALVENTILATION'

def ControllerOutdoorair(idf, **kwargs: Unpack[ControllerOutdoorairType]):
    """"helper for ControllerOutdoorair"""
    return idf.newidfobject('CONTROLLER:OUTDOORAIR', **kwargs)
class ControllerOutdoorairMeta:
    idf_name = 'CONTROLLER:OUTDOORAIR'

def ControllerWatercoil(idf, **kwargs: Unpack[ControllerWatercoilType]):
    """"helper for ControllerWatercoil"""
    return idf.newidfobject('CONTROLLER:WATERCOIL', **kwargs)
class ControllerWatercoilMeta:
    idf_name = 'CONTROLLER:WATERCOIL'

def Convergencelimits(idf, **kwargs: Unpack[ConvergencelimitsType]):
    """"helper for Convergencelimits"""
    return idf.newidfobject('CONVERGENCELIMITS', **kwargs)
class ConvergencelimitsMeta:
    idf_name = 'CONVERGENCELIMITS'

def CoolingtowerSinglespeed(idf, **kwargs: Unpack[CoolingtowerSinglespeedType]):
    """"helper for CoolingtowerSinglespeed"""
    return idf.newidfobject('COOLINGTOWER:SINGLESPEED', **kwargs)
class CoolingtowerSinglespeedMeta:
    idf_name = 'COOLINGTOWER:SINGLESPEED'

def CoolingtowerTwospeed(idf, **kwargs: Unpack[CoolingtowerTwospeedType]):
    """"helper for CoolingtowerTwospeed"""
    return idf.newidfobject('COOLINGTOWER:TWOSPEED', **kwargs)
class CoolingtowerTwospeedMeta:
    idf_name = 'COOLINGTOWER:TWOSPEED'

def CoolingtowerVariablespeed(idf, **kwargs: Unpack[CoolingtowerVariablespeedType]):
    """"helper for CoolingtowerVariablespeed"""
    return idf.newidfobject('COOLINGTOWER:VARIABLESPEED', **kwargs)
class CoolingtowerVariablespeedMeta:
    idf_name = 'COOLINGTOWER:VARIABLESPEED'

def CoolingtowerVariablespeedMerkel(idf, **kwargs: Unpack[CoolingtowerVariablespeedMerkelType]):
    """"helper for CoolingtowerVariablespeedMerkel"""
    return idf.newidfobject('COOLINGTOWER:VARIABLESPEED:MERKEL', **kwargs)
class CoolingtowerVariablespeedMerkelMeta:
    idf_name = 'COOLINGTOWER:VARIABLESPEED:MERKEL'

def CoolingtowerperformanceCooltools(idf, **kwargs: Unpack[CoolingtowerperformanceCooltoolsType]):
    """"helper for CoolingtowerperformanceCooltools"""
    return idf.newidfobject('COOLINGTOWERPERFORMANCE:COOLTOOLS', **kwargs)
class CoolingtowerperformanceCooltoolsMeta:
    idf_name = 'COOLINGTOWERPERFORMANCE:COOLTOOLS'

def CoolingtowerperformanceYorkcalc(idf, **kwargs: Unpack[CoolingtowerperformanceYorkcalcType]):
    """"helper for CoolingtowerperformanceYorkcalc"""
    return idf.newidfobject('COOLINGTOWERPERFORMANCE:YORKCALC', **kwargs)
class CoolingtowerperformanceYorkcalcMeta:
    idf_name = 'COOLINGTOWERPERFORMANCE:YORKCALC'

def Currencytype(idf, **kwargs: Unpack[CurrencytypeType]):
    """"helper for Currencytype"""
    return idf.newidfobject('CURRENCYTYPE', **kwargs)
class CurrencytypeMeta:
    idf_name = 'CURRENCYTYPE'

def CurveBicubic(idf, **kwargs: Unpack[CurveBicubicType]):
    """"helper for CurveBicubic"""
    return idf.newidfobject('CURVE:BICUBIC', **kwargs)
class CurveBicubicMeta:
    idf_name = 'CURVE:BICUBIC'

def CurveBiquadratic(idf, **kwargs: Unpack[CurveBiquadraticType]):
    """"helper for CurveBiquadratic"""
    return idf.newidfobject('CURVE:BIQUADRATIC', **kwargs)
class CurveBiquadraticMeta:
    idf_name = 'CURVE:BIQUADRATIC'

def CurveChillerpartloadwithlift(idf, **kwargs: Unpack[CurveChillerpartloadwithliftType]):
    """"helper for CurveChillerpartloadwithlift"""
    return idf.newidfobject('CURVE:CHILLERPARTLOADWITHLIFT', **kwargs)
class CurveChillerpartloadwithliftMeta:
    idf_name = 'CURVE:CHILLERPARTLOADWITHLIFT'

def CurveCubic(idf, **kwargs: Unpack[CurveCubicType]):
    """"helper for CurveCubic"""
    return idf.newidfobject('CURVE:CUBIC', **kwargs)
class CurveCubicMeta:
    idf_name = 'CURVE:CUBIC'

def CurveCubiclinear(idf, **kwargs: Unpack[CurveCubiclinearType]):
    """"helper for CurveCubiclinear"""
    return idf.newidfobject('CURVE:CUBICLINEAR', **kwargs)
class CurveCubiclinearMeta:
    idf_name = 'CURVE:CUBICLINEAR'

def CurveDoubleexponentialdecay(idf, **kwargs: Unpack[CurveDoubleexponentialdecayType]):
    """"helper for CurveDoubleexponentialdecay"""
    return idf.newidfobject('CURVE:DOUBLEEXPONENTIALDECAY', **kwargs)
class CurveDoubleexponentialdecayMeta:
    idf_name = 'CURVE:DOUBLEEXPONENTIALDECAY'

def CurveExponent(idf, **kwargs: Unpack[CurveExponentType]):
    """"helper for CurveExponent"""
    return idf.newidfobject('CURVE:EXPONENT', **kwargs)
class CurveExponentMeta:
    idf_name = 'CURVE:EXPONENT'

def CurveExponentialdecay(idf, **kwargs: Unpack[CurveExponentialdecayType]):
    """"helper for CurveExponentialdecay"""
    return idf.newidfobject('CURVE:EXPONENTIALDECAY', **kwargs)
class CurveExponentialdecayMeta:
    idf_name = 'CURVE:EXPONENTIALDECAY'

def CurveExponentialskewnormal(idf, **kwargs: Unpack[CurveExponentialskewnormalType]):
    """"helper for CurveExponentialskewnormal"""
    return idf.newidfobject('CURVE:EXPONENTIALSKEWNORMAL', **kwargs)
class CurveExponentialskewnormalMeta:
    idf_name = 'CURVE:EXPONENTIALSKEWNORMAL'

def CurveFanpressurerise(idf, **kwargs: Unpack[CurveFanpressureriseType]):
    """"helper for CurveFanpressurerise"""
    return idf.newidfobject('CURVE:FANPRESSURERISE', **kwargs)
class CurveFanpressureriseMeta:
    idf_name = 'CURVE:FANPRESSURERISE'

def CurveFunctionalPressuredrop(idf, **kwargs: Unpack[CurveFunctionalPressuredropType]):
    """"helper for CurveFunctionalPressuredrop"""
    return idf.newidfobject('CURVE:FUNCTIONAL:PRESSUREDROP', **kwargs)
class CurveFunctionalPressuredropMeta:
    idf_name = 'CURVE:FUNCTIONAL:PRESSUREDROP'

def CurveLinear(idf, **kwargs: Unpack[CurveLinearType]):
    """"helper for CurveLinear"""
    return idf.newidfobject('CURVE:LINEAR', **kwargs)
class CurveLinearMeta:
    idf_name = 'CURVE:LINEAR'

def CurveQuadlinear(idf, **kwargs: Unpack[CurveQuadlinearType]):
    """"helper for CurveQuadlinear"""
    return idf.newidfobject('CURVE:QUADLINEAR', **kwargs)
class CurveQuadlinearMeta:
    idf_name = 'CURVE:QUADLINEAR'

def CurveQuadratic(idf, **kwargs: Unpack[CurveQuadraticType]):
    """"helper for CurveQuadratic"""
    return idf.newidfobject('CURVE:QUADRATIC', **kwargs)
class CurveQuadraticMeta:
    idf_name = 'CURVE:QUADRATIC'

def CurveQuadraticlinear(idf, **kwargs: Unpack[CurveQuadraticlinearType]):
    """"helper for CurveQuadraticlinear"""
    return idf.newidfobject('CURVE:QUADRATICLINEAR', **kwargs)
class CurveQuadraticlinearMeta:
    idf_name = 'CURVE:QUADRATICLINEAR'

def CurveQuartic(idf, **kwargs: Unpack[CurveQuarticType]):
    """"helper for CurveQuartic"""
    return idf.newidfobject('CURVE:QUARTIC', **kwargs)
class CurveQuarticMeta:
    idf_name = 'CURVE:QUARTIC'

def CurveQuintlinear(idf, **kwargs: Unpack[CurveQuintlinearType]):
    """"helper for CurveQuintlinear"""
    return idf.newidfobject('CURVE:QUINTLINEAR', **kwargs)
class CurveQuintlinearMeta:
    idf_name = 'CURVE:QUINTLINEAR'

def CurveRectangularhyperbola1(idf, **kwargs: Unpack[CurveRectangularhyperbola1Type]):
    """"helper for CurveRectangularhyperbola1"""
    return idf.newidfobject('CURVE:RECTANGULARHYPERBOLA1', **kwargs)
class CurveRectangularhyperbola1Meta:
    idf_name = 'CURVE:RECTANGULARHYPERBOLA1'

def CurveRectangularhyperbola2(idf, **kwargs: Unpack[CurveRectangularhyperbola2Type]):
    """"helper for CurveRectangularhyperbola2"""
    return idf.newidfobject('CURVE:RECTANGULARHYPERBOLA2', **kwargs)
class CurveRectangularhyperbola2Meta:
    idf_name = 'CURVE:RECTANGULARHYPERBOLA2'

def CurveSigmoid(idf, **kwargs: Unpack[CurveSigmoidType]):
    """"helper for CurveSigmoid"""
    return idf.newidfobject('CURVE:SIGMOID', **kwargs)
class CurveSigmoidMeta:
    idf_name = 'CURVE:SIGMOID'

def CurveTriquadratic(idf, **kwargs: Unpack[CurveTriquadraticType]):
    """"helper for CurveTriquadratic"""
    return idf.newidfobject('CURVE:TRIQUADRATIC', **kwargs)
class CurveTriquadraticMeta:
    idf_name = 'CURVE:TRIQUADRATIC'

def DaylightingControls(idf, **kwargs: Unpack[DaylightingControlsType]):
    """"helper for DaylightingControls"""
    return idf.newidfobject('DAYLIGHTING:CONTROLS', **kwargs)
class DaylightingControlsMeta:
    idf_name = 'DAYLIGHTING:CONTROLS'

def DaylightingDelightComplexfenestration(idf, **kwargs: Unpack[DaylightingDelightComplexfenestrationType]):
    """"helper for DaylightingDelightComplexfenestration"""
    return idf.newidfobject('DAYLIGHTING:DELIGHT:COMPLEXFENESTRATION', **kwargs)
class DaylightingDelightComplexfenestrationMeta:
    idf_name = 'DAYLIGHTING:DELIGHT:COMPLEXFENESTRATION'

def DaylightingReferencepoint(idf, **kwargs: Unpack[DaylightingReferencepointType]):
    """"helper for DaylightingReferencepoint"""
    return idf.newidfobject('DAYLIGHTING:REFERENCEPOINT', **kwargs)
class DaylightingReferencepointMeta:
    idf_name = 'DAYLIGHTING:REFERENCEPOINT'

def DaylightingdeviceLightwell(idf, **kwargs: Unpack[DaylightingdeviceLightwellType]):
    """"helper for DaylightingdeviceLightwell"""
    return idf.newidfobject('DAYLIGHTINGDEVICE:LIGHTWELL', **kwargs)
class DaylightingdeviceLightwellMeta:
    idf_name = 'DAYLIGHTINGDEVICE:LIGHTWELL'

def DaylightingdeviceShelf(idf, **kwargs: Unpack[DaylightingdeviceShelfType]):
    """"helper for DaylightingdeviceShelf"""
    return idf.newidfobject('DAYLIGHTINGDEVICE:SHELF', **kwargs)
class DaylightingdeviceShelfMeta:
    idf_name = 'DAYLIGHTINGDEVICE:SHELF'

def DaylightingdeviceTubular(idf, **kwargs: Unpack[DaylightingdeviceTubularType]):
    """"helper for DaylightingdeviceTubular"""
    return idf.newidfobject('DAYLIGHTINGDEVICE:TUBULAR', **kwargs)
class DaylightingdeviceTubularMeta:
    idf_name = 'DAYLIGHTINGDEVICE:TUBULAR'

def DehumidifierDesiccantNofans(idf, **kwargs: Unpack[DehumidifierDesiccantNofansType]):
    """"helper for DehumidifierDesiccantNofans"""
    return idf.newidfobject('DEHUMIDIFIER:DESICCANT:NOFANS', **kwargs)
class DehumidifierDesiccantNofansMeta:
    idf_name = 'DEHUMIDIFIER:DESICCANT:NOFANS'

def DehumidifierDesiccantSystem(idf, **kwargs: Unpack[DehumidifierDesiccantSystemType]):
    """"helper for DehumidifierDesiccantSystem"""
    return idf.newidfobject('DEHUMIDIFIER:DESICCANT:SYSTEM', **kwargs)
class DehumidifierDesiccantSystemMeta:
    idf_name = 'DEHUMIDIFIER:DESICCANT:SYSTEM'

def DemandmanagerElectricequipment(idf, **kwargs: Unpack[DemandmanagerElectricequipmentType]):
    """"helper for DemandmanagerElectricequipment"""
    return idf.newidfobject('DEMANDMANAGER:ELECTRICEQUIPMENT', **kwargs)
class DemandmanagerElectricequipmentMeta:
    idf_name = 'DEMANDMANAGER:ELECTRICEQUIPMENT'

def DemandmanagerExteriorlights(idf, **kwargs: Unpack[DemandmanagerExteriorlightsType]):
    """"helper for DemandmanagerExteriorlights"""
    return idf.newidfobject('DEMANDMANAGER:EXTERIORLIGHTS', **kwargs)
class DemandmanagerExteriorlightsMeta:
    idf_name = 'DEMANDMANAGER:EXTERIORLIGHTS'

def DemandmanagerLights(idf, **kwargs: Unpack[DemandmanagerLightsType]):
    """"helper for DemandmanagerLights"""
    return idf.newidfobject('DEMANDMANAGER:LIGHTS', **kwargs)
class DemandmanagerLightsMeta:
    idf_name = 'DEMANDMANAGER:LIGHTS'

def DemandmanagerThermostats(idf, **kwargs: Unpack[DemandmanagerThermostatsType]):
    """"helper for DemandmanagerThermostats"""
    return idf.newidfobject('DEMANDMANAGER:THERMOSTATS', **kwargs)
class DemandmanagerThermostatsMeta:
    idf_name = 'DEMANDMANAGER:THERMOSTATS'

def DemandmanagerVentilation(idf, **kwargs: Unpack[DemandmanagerVentilationType]):
    """"helper for DemandmanagerVentilation"""
    return idf.newidfobject('DEMANDMANAGER:VENTILATION', **kwargs)
class DemandmanagerVentilationMeta:
    idf_name = 'DEMANDMANAGER:VENTILATION'

def Demandmanagerassignmentlist(idf, **kwargs: Unpack[DemandmanagerassignmentlistType]):
    """"helper for Demandmanagerassignmentlist"""
    return idf.newidfobject('DEMANDMANAGERASSIGNMENTLIST', **kwargs)
class DemandmanagerassignmentlistMeta:
    idf_name = 'DEMANDMANAGERASSIGNMENTLIST'

def DesignspecificationAirterminalSizing(idf, **kwargs: Unpack[DesignspecificationAirterminalSizingType]):
    """"helper for DesignspecificationAirterminalSizing"""
    return idf.newidfobject('DESIGNSPECIFICATION:AIRTERMINAL:SIZING', **kwargs)
class DesignspecificationAirterminalSizingMeta:
    idf_name = 'DESIGNSPECIFICATION:AIRTERMINAL:SIZING'

def DesignspecificationOutdoorair(idf, **kwargs: Unpack[DesignspecificationOutdoorairType]):
    """"helper for DesignspecificationOutdoorair"""
    return idf.newidfobject('DESIGNSPECIFICATION:OUTDOORAIR', **kwargs)
class DesignspecificationOutdoorairMeta:
    idf_name = 'DESIGNSPECIFICATION:OUTDOORAIR'

def DesignspecificationOutdoorairSpacelist(idf, **kwargs: Unpack[DesignspecificationOutdoorairSpacelistType]):
    """"helper for DesignspecificationOutdoorairSpacelist"""
    return idf.newidfobject('DESIGNSPECIFICATION:OUTDOORAIR:SPACELIST', **kwargs)
class DesignspecificationOutdoorairSpacelistMeta:
    idf_name = 'DESIGNSPECIFICATION:OUTDOORAIR:SPACELIST'

def DesignspecificationZoneairdistribution(idf, **kwargs: Unpack[DesignspecificationZoneairdistributionType]):
    """"helper for DesignspecificationZoneairdistribution"""
    return idf.newidfobject('DESIGNSPECIFICATION:ZONEAIRDISTRIBUTION', **kwargs)
class DesignspecificationZoneairdistributionMeta:
    idf_name = 'DESIGNSPECIFICATION:ZONEAIRDISTRIBUTION'

def DesignspecificationZonehvacSizing(idf, **kwargs: Unpack[DesignspecificationZonehvacSizingType]):
    """"helper for DesignspecificationZonehvacSizing"""
    return idf.newidfobject('DESIGNSPECIFICATION:ZONEHVAC:SIZING', **kwargs)
class DesignspecificationZonehvacSizingMeta:
    idf_name = 'DESIGNSPECIFICATION:ZONEHVAC:SIZING'

def Districtcooling(idf, **kwargs: Unpack[DistrictcoolingType]):
    """"helper for Districtcooling"""
    return idf.newidfobject('DISTRICTCOOLING', **kwargs)
class DistrictcoolingMeta:
    idf_name = 'DISTRICTCOOLING'

def DistrictheatingSteam(idf, **kwargs: Unpack[DistrictheatingSteamType]):
    """"helper for DistrictheatingSteam"""
    return idf.newidfobject('DISTRICTHEATING:STEAM', **kwargs)
class DistrictheatingSteamMeta:
    idf_name = 'DISTRICTHEATING:STEAM'

def DistrictheatingWater(idf, **kwargs: Unpack[DistrictheatingWaterType]):
    """"helper for DistrictheatingWater"""
    return idf.newidfobject('DISTRICTHEATING:WATER', **kwargs)
class DistrictheatingWaterMeta:
    idf_name = 'DISTRICTHEATING:WATER'

def Door(idf, **kwargs: Unpack[DoorType]):
    """"helper for Door"""
    return idf.newidfobject('DOOR', **kwargs)
class DoorMeta:
    idf_name = 'DOOR'

def DoorInterzone(idf, **kwargs: Unpack[DoorInterzoneType]):
    """"helper for DoorInterzone"""
    return idf.newidfobject('DOOR:INTERZONE', **kwargs)
class DoorInterzoneMeta:
    idf_name = 'DOOR:INTERZONE'

def Duct(idf, **kwargs: Unpack[DuctType]):
    """"helper for Duct"""
    return idf.newidfobject('DUCT', **kwargs)
class DuctMeta:
    idf_name = 'DUCT'

def Electricequipment(idf, **kwargs: Unpack[ElectricequipmentType]):
    """"helper for Electricequipment"""
    return idf.newidfobject('ELECTRICEQUIPMENT', **kwargs)
class ElectricequipmentMeta:
    idf_name = 'ELECTRICEQUIPMENT'

def ElectricequipmentIteAircooled(idf, **kwargs: Unpack[ElectricequipmentIteAircooledType]):
    """"helper for ElectricequipmentIteAircooled"""
    return idf.newidfobject('ELECTRICEQUIPMENT:ITE:AIRCOOLED', **kwargs)
class ElectricequipmentIteAircooledMeta:
    idf_name = 'ELECTRICEQUIPMENT:ITE:AIRCOOLED'

def ElectricloadcenterDistribution(idf, **kwargs: Unpack[ElectricloadcenterDistributionType]):
    """"helper for ElectricloadcenterDistribution"""
    return idf.newidfobject('ELECTRICLOADCENTER:DISTRIBUTION', **kwargs)
class ElectricloadcenterDistributionMeta:
    idf_name = 'ELECTRICLOADCENTER:DISTRIBUTION'

def ElectricloadcenterGenerators(idf, **kwargs: Unpack[ElectricloadcenterGeneratorsType]):
    """"helper for ElectricloadcenterGenerators"""
    return idf.newidfobject('ELECTRICLOADCENTER:GENERATORS', **kwargs)
class ElectricloadcenterGeneratorsMeta:
    idf_name = 'ELECTRICLOADCENTER:GENERATORS'

def ElectricloadcenterInverterFunctionofpower(idf, **kwargs: Unpack[ElectricloadcenterInverterFunctionofpowerType]):
    """"helper for ElectricloadcenterInverterFunctionofpower"""
    return idf.newidfobject('ELECTRICLOADCENTER:INVERTER:FUNCTIONOFPOWER', **kwargs)
class ElectricloadcenterInverterFunctionofpowerMeta:
    idf_name = 'ELECTRICLOADCENTER:INVERTER:FUNCTIONOFPOWER'

def ElectricloadcenterInverterLookuptable(idf, **kwargs: Unpack[ElectricloadcenterInverterLookuptableType]):
    """"helper for ElectricloadcenterInverterLookuptable"""
    return idf.newidfobject('ELECTRICLOADCENTER:INVERTER:LOOKUPTABLE', **kwargs)
class ElectricloadcenterInverterLookuptableMeta:
    idf_name = 'ELECTRICLOADCENTER:INVERTER:LOOKUPTABLE'

def ElectricloadcenterInverterPvwatts(idf, **kwargs: Unpack[ElectricloadcenterInverterPvwattsType]):
    """"helper for ElectricloadcenterInverterPvwatts"""
    return idf.newidfobject('ELECTRICLOADCENTER:INVERTER:PVWATTS', **kwargs)
class ElectricloadcenterInverterPvwattsMeta:
    idf_name = 'ELECTRICLOADCENTER:INVERTER:PVWATTS'

def ElectricloadcenterInverterSimple(idf, **kwargs: Unpack[ElectricloadcenterInverterSimpleType]):
    """"helper for ElectricloadcenterInverterSimple"""
    return idf.newidfobject('ELECTRICLOADCENTER:INVERTER:SIMPLE', **kwargs)
class ElectricloadcenterInverterSimpleMeta:
    idf_name = 'ELECTRICLOADCENTER:INVERTER:SIMPLE'

def ElectricloadcenterStorageBattery(idf, **kwargs: Unpack[ElectricloadcenterStorageBatteryType]):
    """"helper for ElectricloadcenterStorageBattery"""
    return idf.newidfobject('ELECTRICLOADCENTER:STORAGE:BATTERY', **kwargs)
class ElectricloadcenterStorageBatteryMeta:
    idf_name = 'ELECTRICLOADCENTER:STORAGE:BATTERY'

def ElectricloadcenterStorageConverter(idf, **kwargs: Unpack[ElectricloadcenterStorageConverterType]):
    """"helper for ElectricloadcenterStorageConverter"""
    return idf.newidfobject('ELECTRICLOADCENTER:STORAGE:CONVERTER', **kwargs)
class ElectricloadcenterStorageConverterMeta:
    idf_name = 'ELECTRICLOADCENTER:STORAGE:CONVERTER'

def ElectricloadcenterStorageLiionnmcbattery(idf, **kwargs: Unpack[ElectricloadcenterStorageLiionnmcbatteryType]):
    """"helper for ElectricloadcenterStorageLiionnmcbattery"""
    return idf.newidfobject('ELECTRICLOADCENTER:STORAGE:LIIONNMCBATTERY', **kwargs)
class ElectricloadcenterStorageLiionnmcbatteryMeta:
    idf_name = 'ELECTRICLOADCENTER:STORAGE:LIIONNMCBATTERY'

def ElectricloadcenterStorageSimple(idf, **kwargs: Unpack[ElectricloadcenterStorageSimpleType]):
    """"helper for ElectricloadcenterStorageSimple"""
    return idf.newidfobject('ELECTRICLOADCENTER:STORAGE:SIMPLE', **kwargs)
class ElectricloadcenterStorageSimpleMeta:
    idf_name = 'ELECTRICLOADCENTER:STORAGE:SIMPLE'

def ElectricloadcenterTransformer(idf, **kwargs: Unpack[ElectricloadcenterTransformerType]):
    """"helper for ElectricloadcenterTransformer"""
    return idf.newidfobject('ELECTRICLOADCENTER:TRANSFORMER', **kwargs)
class ElectricloadcenterTransformerMeta:
    idf_name = 'ELECTRICLOADCENTER:TRANSFORMER'

def EnergymanagementsystemActuator(idf, **kwargs: Unpack[EnergymanagementsystemActuatorType]):
    """"helper for EnergymanagementsystemActuator"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:ACTUATOR', **kwargs)
class EnergymanagementsystemActuatorMeta:
    idf_name = 'ENERGYMANAGEMENTSYSTEM:ACTUATOR'

def EnergymanagementsystemConstructionindexvariable(idf, **kwargs: Unpack[EnergymanagementsystemConstructionindexvariableType]):
    """"helper for EnergymanagementsystemConstructionindexvariable"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:CONSTRUCTIONINDEXVARIABLE', **kwargs)
class EnergymanagementsystemConstructionindexvariableMeta:
    idf_name = 'ENERGYMANAGEMENTSYSTEM:CONSTRUCTIONINDEXVARIABLE'

def EnergymanagementsystemCurveortableindexvariable(idf, **kwargs: Unpack[EnergymanagementsystemCurveortableindexvariableType]):
    """"helper for EnergymanagementsystemCurveortableindexvariable"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:CURVEORTABLEINDEXVARIABLE', **kwargs)
class EnergymanagementsystemCurveortableindexvariableMeta:
    idf_name = 'ENERGYMANAGEMENTSYSTEM:CURVEORTABLEINDEXVARIABLE'

def EnergymanagementsystemGlobalvariable(idf, **kwargs: Unpack[EnergymanagementsystemGlobalvariableType]):
    """"helper for EnergymanagementsystemGlobalvariable"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:GLOBALVARIABLE', **kwargs)
class EnergymanagementsystemGlobalvariableMeta:
    idf_name = 'ENERGYMANAGEMENTSYSTEM:GLOBALVARIABLE'

def EnergymanagementsystemInternalvariable(idf, **kwargs: Unpack[EnergymanagementsystemInternalvariableType]):
    """"helper for EnergymanagementsystemInternalvariable"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:INTERNALVARIABLE', **kwargs)
class EnergymanagementsystemInternalvariableMeta:
    idf_name = 'ENERGYMANAGEMENTSYSTEM:INTERNALVARIABLE'

def EnergymanagementsystemMeteredoutputvariable(idf, **kwargs: Unpack[EnergymanagementsystemMeteredoutputvariableType]):
    """"helper for EnergymanagementsystemMeteredoutputvariable"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:METEREDOUTPUTVARIABLE', **kwargs)
class EnergymanagementsystemMeteredoutputvariableMeta:
    idf_name = 'ENERGYMANAGEMENTSYSTEM:METEREDOUTPUTVARIABLE'

def EnergymanagementsystemOutputvariable(idf, **kwargs: Unpack[EnergymanagementsystemOutputvariableType]):
    """"helper for EnergymanagementsystemOutputvariable"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:OUTPUTVARIABLE', **kwargs)
class EnergymanagementsystemOutputvariableMeta:
    idf_name = 'ENERGYMANAGEMENTSYSTEM:OUTPUTVARIABLE'

def EnergymanagementsystemProgram(idf, **kwargs: Unpack[EnergymanagementsystemProgramType]):
    """"helper for EnergymanagementsystemProgram"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:PROGRAM', **kwargs)
class EnergymanagementsystemProgramMeta:
    idf_name = 'ENERGYMANAGEMENTSYSTEM:PROGRAM'

def EnergymanagementsystemProgramcallingmanager(idf, **kwargs: Unpack[EnergymanagementsystemProgramcallingmanagerType]):
    """"helper for EnergymanagementsystemProgramcallingmanager"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:PROGRAMCALLINGMANAGER', **kwargs)
class EnergymanagementsystemProgramcallingmanagerMeta:
    idf_name = 'ENERGYMANAGEMENTSYSTEM:PROGRAMCALLINGMANAGER'

def EnergymanagementsystemSensor(idf, **kwargs: Unpack[EnergymanagementsystemSensorType]):
    """"helper for EnergymanagementsystemSensor"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:SENSOR', **kwargs)
class EnergymanagementsystemSensorMeta:
    idf_name = 'ENERGYMANAGEMENTSYSTEM:SENSOR'

def EnergymanagementsystemSubroutine(idf, **kwargs: Unpack[EnergymanagementsystemSubroutineType]):
    """"helper for EnergymanagementsystemSubroutine"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:SUBROUTINE', **kwargs)
class EnergymanagementsystemSubroutineMeta:
    idf_name = 'ENERGYMANAGEMENTSYSTEM:SUBROUTINE'

def EnergymanagementsystemTrendvariable(idf, **kwargs: Unpack[EnergymanagementsystemTrendvariableType]):
    """"helper for EnergymanagementsystemTrendvariable"""
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:TRENDVARIABLE', **kwargs)
class EnergymanagementsystemTrendvariableMeta:
    idf_name = 'ENERGYMANAGEMENTSYSTEM:TRENDVARIABLE'

def Environmentalimpactfactors(idf, **kwargs: Unpack[EnvironmentalimpactfactorsType]):
    """"helper for Environmentalimpactfactors"""
    return idf.newidfobject('ENVIRONMENTALIMPACTFACTORS', **kwargs)
class EnvironmentalimpactfactorsMeta:
    idf_name = 'ENVIRONMENTALIMPACTFACTORS'

def EvaporativecoolerDirectCeldekpad(idf, **kwargs: Unpack[EvaporativecoolerDirectCeldekpadType]):
    """"helper for EvaporativecoolerDirectCeldekpad"""
    return idf.newidfobject('EVAPORATIVECOOLER:DIRECT:CELDEKPAD', **kwargs)
class EvaporativecoolerDirectCeldekpadMeta:
    idf_name = 'EVAPORATIVECOOLER:DIRECT:CELDEKPAD'

def EvaporativecoolerDirectResearchspecial(idf, **kwargs: Unpack[EvaporativecoolerDirectResearchspecialType]):
    """"helper for EvaporativecoolerDirectResearchspecial"""
    return idf.newidfobject('EVAPORATIVECOOLER:DIRECT:RESEARCHSPECIAL', **kwargs)
class EvaporativecoolerDirectResearchspecialMeta:
    idf_name = 'EVAPORATIVECOOLER:DIRECT:RESEARCHSPECIAL'

def EvaporativecoolerIndirectCeldekpad(idf, **kwargs: Unpack[EvaporativecoolerIndirectCeldekpadType]):
    """"helper for EvaporativecoolerIndirectCeldekpad"""
    return idf.newidfobject('EVAPORATIVECOOLER:INDIRECT:CELDEKPAD', **kwargs)
class EvaporativecoolerIndirectCeldekpadMeta:
    idf_name = 'EVAPORATIVECOOLER:INDIRECT:CELDEKPAD'

def EvaporativecoolerIndirectResearchspecial(idf, **kwargs: Unpack[EvaporativecoolerIndirectResearchspecialType]):
    """"helper for EvaporativecoolerIndirectResearchspecial"""
    return idf.newidfobject('EVAPORATIVECOOLER:INDIRECT:RESEARCHSPECIAL', **kwargs)
class EvaporativecoolerIndirectResearchspecialMeta:
    idf_name = 'EVAPORATIVECOOLER:INDIRECT:RESEARCHSPECIAL'

def EvaporativecoolerIndirectWetcoil(idf, **kwargs: Unpack[EvaporativecoolerIndirectWetcoilType]):
    """"helper for EvaporativecoolerIndirectWetcoil"""
    return idf.newidfobject('EVAPORATIVECOOLER:INDIRECT:WETCOIL', **kwargs)
class EvaporativecoolerIndirectWetcoilMeta:
    idf_name = 'EVAPORATIVECOOLER:INDIRECT:WETCOIL'

def EvaporativefluidcoolerSinglespeed(idf, **kwargs: Unpack[EvaporativefluidcoolerSinglespeedType]):
    """"helper for EvaporativefluidcoolerSinglespeed"""
    return idf.newidfobject('EVAPORATIVEFLUIDCOOLER:SINGLESPEED', **kwargs)
class EvaporativefluidcoolerSinglespeedMeta:
    idf_name = 'EVAPORATIVEFLUIDCOOLER:SINGLESPEED'

def EvaporativefluidcoolerTwospeed(idf, **kwargs: Unpack[EvaporativefluidcoolerTwospeedType]):
    """"helper for EvaporativefluidcoolerTwospeed"""
    return idf.newidfobject('EVAPORATIVEFLUIDCOOLER:TWOSPEED', **kwargs)
class EvaporativefluidcoolerTwospeedMeta:
    idf_name = 'EVAPORATIVEFLUIDCOOLER:TWOSPEED'

def ExteriorFuelequipment(idf, **kwargs: Unpack[ExteriorFuelequipmentType]):
    """"helper for ExteriorFuelequipment"""
    return idf.newidfobject('EXTERIOR:FUELEQUIPMENT', **kwargs)
class ExteriorFuelequipmentMeta:
    idf_name = 'EXTERIOR:FUELEQUIPMENT'

def ExteriorLights(idf, **kwargs: Unpack[ExteriorLightsType]):
    """"helper for ExteriorLights"""
    return idf.newidfobject('EXTERIOR:LIGHTS', **kwargs)
class ExteriorLightsMeta:
    idf_name = 'EXTERIOR:LIGHTS'

def ExteriorWaterequipment(idf, **kwargs: Unpack[ExteriorWaterequipmentType]):
    """"helper for ExteriorWaterequipment"""
    return idf.newidfobject('EXTERIOR:WATEREQUIPMENT', **kwargs)
class ExteriorWaterequipmentMeta:
    idf_name = 'EXTERIOR:WATEREQUIPMENT'

def Externalinterface(idf, **kwargs: Unpack[ExternalinterfaceType]):
    """"helper for Externalinterface"""
    return idf.newidfobject('EXTERNALINTERFACE', **kwargs)
class ExternalinterfaceMeta:
    idf_name = 'EXTERNALINTERFACE'

def ExternalinterfaceActuator(idf, **kwargs: Unpack[ExternalinterfaceActuatorType]):
    """"helper for ExternalinterfaceActuator"""
    return idf.newidfobject('EXTERNALINTERFACE:ACTUATOR', **kwargs)
class ExternalinterfaceActuatorMeta:
    idf_name = 'EXTERNALINTERFACE:ACTUATOR'

def ExternalinterfaceFunctionalmockupunitexportFromVariable(idf, **kwargs: Unpack[ExternalinterfaceFunctionalmockupunitexportFromVariableType]):
    """"helper for ExternalinterfaceFunctionalmockupunitexportFromVariable"""
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITEXPORT:FROM:VARIABLE', **kwargs)
class ExternalinterfaceFunctionalmockupunitexportFromVariableMeta:
    idf_name = 'EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITEXPORT:FROM:VARIABLE'

def ExternalinterfaceFunctionalmockupunitexportToActuator(idf, **kwargs: Unpack[ExternalinterfaceFunctionalmockupunitexportToActuatorType]):
    """"helper for ExternalinterfaceFunctionalmockupunitexportToActuator"""
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITEXPORT:TO:ACTUATOR', **kwargs)
class ExternalinterfaceFunctionalmockupunitexportToActuatorMeta:
    idf_name = 'EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITEXPORT:TO:ACTUATOR'

def ExternalinterfaceFunctionalmockupunitexportToSchedule(idf, **kwargs: Unpack[ExternalinterfaceFunctionalmockupunitexportToScheduleType]):
    """"helper for ExternalinterfaceFunctionalmockupunitexportToSchedule"""
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITEXPORT:TO:SCHEDULE', **kwargs)
class ExternalinterfaceFunctionalmockupunitexportToScheduleMeta:
    idf_name = 'EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITEXPORT:TO:SCHEDULE'

def ExternalinterfaceFunctionalmockupunitexportToVariable(idf, **kwargs: Unpack[ExternalinterfaceFunctionalmockupunitexportToVariableType]):
    """"helper for ExternalinterfaceFunctionalmockupunitexportToVariable"""
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITEXPORT:TO:VARIABLE', **kwargs)
class ExternalinterfaceFunctionalmockupunitexportToVariableMeta:
    idf_name = 'EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITEXPORT:TO:VARIABLE'

def ExternalinterfaceFunctionalmockupunitimport(idf, **kwargs: Unpack[ExternalinterfaceFunctionalmockupunitimportType]):
    """"helper for ExternalinterfaceFunctionalmockupunitimport"""
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT', **kwargs)
class ExternalinterfaceFunctionalmockupunitimportMeta:
    idf_name = 'EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT'

def ExternalinterfaceFunctionalmockupunitimportFromVariable(idf, **kwargs: Unpack[ExternalinterfaceFunctionalmockupunitimportFromVariableType]):
    """"helper for ExternalinterfaceFunctionalmockupunitimportFromVariable"""
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT:FROM:VARIABLE', **kwargs)
class ExternalinterfaceFunctionalmockupunitimportFromVariableMeta:
    idf_name = 'EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT:FROM:VARIABLE'

def ExternalinterfaceFunctionalmockupunitimportToActuator(idf, **kwargs: Unpack[ExternalinterfaceFunctionalmockupunitimportToActuatorType]):
    """"helper for ExternalinterfaceFunctionalmockupunitimportToActuator"""
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT:TO:ACTUATOR', **kwargs)
class ExternalinterfaceFunctionalmockupunitimportToActuatorMeta:
    idf_name = 'EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT:TO:ACTUATOR'

def ExternalinterfaceFunctionalmockupunitimportToSchedule(idf, **kwargs: Unpack[ExternalinterfaceFunctionalmockupunitimportToScheduleType]):
    """"helper for ExternalinterfaceFunctionalmockupunitimportToSchedule"""
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT:TO:SCHEDULE', **kwargs)
class ExternalinterfaceFunctionalmockupunitimportToScheduleMeta:
    idf_name = 'EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT:TO:SCHEDULE'

def ExternalinterfaceFunctionalmockupunitimportToVariable(idf, **kwargs: Unpack[ExternalinterfaceFunctionalmockupunitimportToVariableType]):
    """"helper for ExternalinterfaceFunctionalmockupunitimportToVariable"""
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT:TO:VARIABLE', **kwargs)
class ExternalinterfaceFunctionalmockupunitimportToVariableMeta:
    idf_name = 'EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT:TO:VARIABLE'

def ExternalinterfaceSchedule(idf, **kwargs: Unpack[ExternalinterfaceScheduleType]):
    """"helper for ExternalinterfaceSchedule"""
    return idf.newidfobject('EXTERNALINTERFACE:SCHEDULE', **kwargs)
class ExternalinterfaceScheduleMeta:
    idf_name = 'EXTERNALINTERFACE:SCHEDULE'

def ExternalinterfaceVariable(idf, **kwargs: Unpack[ExternalinterfaceVariableType]):
    """"helper for ExternalinterfaceVariable"""
    return idf.newidfobject('EXTERNALINTERFACE:VARIABLE', **kwargs)
class ExternalinterfaceVariableMeta:
    idf_name = 'EXTERNALINTERFACE:VARIABLE'

def FanComponentmodel(idf, **kwargs: Unpack[FanComponentmodelType]):
    """"helper for FanComponentmodel"""
    return idf.newidfobject('FAN:COMPONENTMODEL', **kwargs)
class FanComponentmodelMeta:
    idf_name = 'FAN:COMPONENTMODEL'

def FanConstantvolume(idf, **kwargs: Unpack[FanConstantvolumeType]):
    """"helper for FanConstantvolume"""
    return idf.newidfobject('FAN:CONSTANTVOLUME', **kwargs)
class FanConstantvolumeMeta:
    idf_name = 'FAN:CONSTANTVOLUME'

def FanOnoff(idf, **kwargs: Unpack[FanOnoffType]):
    """"helper for FanOnoff"""
    return idf.newidfobject('FAN:ONOFF', **kwargs)
class FanOnoffMeta:
    idf_name = 'FAN:ONOFF'

def FanSystemmodel(idf, **kwargs: Unpack[FanSystemmodelType]):
    """"helper for FanSystemmodel"""
    return idf.newidfobject('FAN:SYSTEMMODEL', **kwargs)
class FanSystemmodelMeta:
    idf_name = 'FAN:SYSTEMMODEL'

def FanVariablevolume(idf, **kwargs: Unpack[FanVariablevolumeType]):
    """"helper for FanVariablevolume"""
    return idf.newidfobject('FAN:VARIABLEVOLUME', **kwargs)
class FanVariablevolumeMeta:
    idf_name = 'FAN:VARIABLEVOLUME'

def FanZoneexhaust(idf, **kwargs: Unpack[FanZoneexhaustType]):
    """"helper for FanZoneexhaust"""
    return idf.newidfobject('FAN:ZONEEXHAUST', **kwargs)
class FanZoneexhaustMeta:
    idf_name = 'FAN:ZONEEXHAUST'

def FanperformanceNightventilation(idf, **kwargs: Unpack[FanperformanceNightventilationType]):
    """"helper for FanperformanceNightventilation"""
    return idf.newidfobject('FANPERFORMANCE:NIGHTVENTILATION', **kwargs)
class FanperformanceNightventilationMeta:
    idf_name = 'FANPERFORMANCE:NIGHTVENTILATION'

def FaultmodelEnthalpysensoroffsetOutdoorair(idf, **kwargs: Unpack[FaultmodelEnthalpysensoroffsetOutdoorairType]):
    """"helper for FaultmodelEnthalpysensoroffsetOutdoorair"""
    return idf.newidfobject('FAULTMODEL:ENTHALPYSENSOROFFSET:OUTDOORAIR', **kwargs)
class FaultmodelEnthalpysensoroffsetOutdoorairMeta:
    idf_name = 'FAULTMODEL:ENTHALPYSENSOROFFSET:OUTDOORAIR'

def FaultmodelEnthalpysensoroffsetReturnair(idf, **kwargs: Unpack[FaultmodelEnthalpysensoroffsetReturnairType]):
    """"helper for FaultmodelEnthalpysensoroffsetReturnair"""
    return idf.newidfobject('FAULTMODEL:ENTHALPYSENSOROFFSET:RETURNAIR', **kwargs)
class FaultmodelEnthalpysensoroffsetReturnairMeta:
    idf_name = 'FAULTMODEL:ENTHALPYSENSOROFFSET:RETURNAIR'

def FaultmodelFoulingAirfilter(idf, **kwargs: Unpack[FaultmodelFoulingAirfilterType]):
    """"helper for FaultmodelFoulingAirfilter"""
    return idf.newidfobject('FAULTMODEL:FOULING:AIRFILTER', **kwargs)
class FaultmodelFoulingAirfilterMeta:
    idf_name = 'FAULTMODEL:FOULING:AIRFILTER'

def FaultmodelFoulingBoiler(idf, **kwargs: Unpack[FaultmodelFoulingBoilerType]):
    """"helper for FaultmodelFoulingBoiler"""
    return idf.newidfobject('FAULTMODEL:FOULING:BOILER', **kwargs)
class FaultmodelFoulingBoilerMeta:
    idf_name = 'FAULTMODEL:FOULING:BOILER'

def FaultmodelFoulingChiller(idf, **kwargs: Unpack[FaultmodelFoulingChillerType]):
    """"helper for FaultmodelFoulingChiller"""
    return idf.newidfobject('FAULTMODEL:FOULING:CHILLER', **kwargs)
class FaultmodelFoulingChillerMeta:
    idf_name = 'FAULTMODEL:FOULING:CHILLER'

def FaultmodelFoulingCoil(idf, **kwargs: Unpack[FaultmodelFoulingCoilType]):
    """"helper for FaultmodelFoulingCoil"""
    return idf.newidfobject('FAULTMODEL:FOULING:COIL', **kwargs)
class FaultmodelFoulingCoilMeta:
    idf_name = 'FAULTMODEL:FOULING:COIL'

def FaultmodelFoulingCoolingtower(idf, **kwargs: Unpack[FaultmodelFoulingCoolingtowerType]):
    """"helper for FaultmodelFoulingCoolingtower"""
    return idf.newidfobject('FAULTMODEL:FOULING:COOLINGTOWER', **kwargs)
class FaultmodelFoulingCoolingtowerMeta:
    idf_name = 'FAULTMODEL:FOULING:COOLINGTOWER'

def FaultmodelFoulingEvaporativecooler(idf, **kwargs: Unpack[FaultmodelFoulingEvaporativecoolerType]):
    """"helper for FaultmodelFoulingEvaporativecooler"""
    return idf.newidfobject('FAULTMODEL:FOULING:EVAPORATIVECOOLER', **kwargs)
class FaultmodelFoulingEvaporativecoolerMeta:
    idf_name = 'FAULTMODEL:FOULING:EVAPORATIVECOOLER'

def FaultmodelHumidistatoffset(idf, **kwargs: Unpack[FaultmodelHumidistatoffsetType]):
    """"helper for FaultmodelHumidistatoffset"""
    return idf.newidfobject('FAULTMODEL:HUMIDISTATOFFSET', **kwargs)
class FaultmodelHumidistatoffsetMeta:
    idf_name = 'FAULTMODEL:HUMIDISTATOFFSET'

def FaultmodelHumiditysensoroffsetOutdoorair(idf, **kwargs: Unpack[FaultmodelHumiditysensoroffsetOutdoorairType]):
    """"helper for FaultmodelHumiditysensoroffsetOutdoorair"""
    return idf.newidfobject('FAULTMODEL:HUMIDITYSENSOROFFSET:OUTDOORAIR', **kwargs)
class FaultmodelHumiditysensoroffsetOutdoorairMeta:
    idf_name = 'FAULTMODEL:HUMIDITYSENSOROFFSET:OUTDOORAIR'

def FaultmodelTemperaturesensoroffsetChillersupplywater(idf, **kwargs: Unpack[FaultmodelTemperaturesensoroffsetChillersupplywaterType]):
    """"helper for FaultmodelTemperaturesensoroffsetChillersupplywater"""
    return idf.newidfobject('FAULTMODEL:TEMPERATURESENSOROFFSET:CHILLERSUPPLYWATER', **kwargs)
class FaultmodelTemperaturesensoroffsetChillersupplywaterMeta:
    idf_name = 'FAULTMODEL:TEMPERATURESENSOROFFSET:CHILLERSUPPLYWATER'

def FaultmodelTemperaturesensoroffsetCoilsupplyair(idf, **kwargs: Unpack[FaultmodelTemperaturesensoroffsetCoilsupplyairType]):
    """"helper for FaultmodelTemperaturesensoroffsetCoilsupplyair"""
    return idf.newidfobject('FAULTMODEL:TEMPERATURESENSOROFFSET:COILSUPPLYAIR', **kwargs)
class FaultmodelTemperaturesensoroffsetCoilsupplyairMeta:
    idf_name = 'FAULTMODEL:TEMPERATURESENSOROFFSET:COILSUPPLYAIR'

def FaultmodelTemperaturesensoroffsetCondensersupplywater(idf, **kwargs: Unpack[FaultmodelTemperaturesensoroffsetCondensersupplywaterType]):
    """"helper for FaultmodelTemperaturesensoroffsetCondensersupplywater"""
    return idf.newidfobject('FAULTMODEL:TEMPERATURESENSOROFFSET:CONDENSERSUPPLYWATER', **kwargs)
class FaultmodelTemperaturesensoroffsetCondensersupplywaterMeta:
    idf_name = 'FAULTMODEL:TEMPERATURESENSOROFFSET:CONDENSERSUPPLYWATER'

def FaultmodelTemperaturesensoroffsetOutdoorair(idf, **kwargs: Unpack[FaultmodelTemperaturesensoroffsetOutdoorairType]):
    """"helper for FaultmodelTemperaturesensoroffsetOutdoorair"""
    return idf.newidfobject('FAULTMODEL:TEMPERATURESENSOROFFSET:OUTDOORAIR', **kwargs)
class FaultmodelTemperaturesensoroffsetOutdoorairMeta:
    idf_name = 'FAULTMODEL:TEMPERATURESENSOROFFSET:OUTDOORAIR'

def FaultmodelTemperaturesensoroffsetReturnair(idf, **kwargs: Unpack[FaultmodelTemperaturesensoroffsetReturnairType]):
    """"helper for FaultmodelTemperaturesensoroffsetReturnair"""
    return idf.newidfobject('FAULTMODEL:TEMPERATURESENSOROFFSET:RETURNAIR', **kwargs)
class FaultmodelTemperaturesensoroffsetReturnairMeta:
    idf_name = 'FAULTMODEL:TEMPERATURESENSOROFFSET:RETURNAIR'

def FaultmodelThermostatoffset(idf, **kwargs: Unpack[FaultmodelThermostatoffsetType]):
    """"helper for FaultmodelThermostatoffset"""
    return idf.newidfobject('FAULTMODEL:THERMOSTATOFFSET', **kwargs)
class FaultmodelThermostatoffsetMeta:
    idf_name = 'FAULTMODEL:THERMOSTATOFFSET'

def FenestrationsurfaceDetailed(idf, **kwargs: Unpack[FenestrationsurfaceDetailedType]):
    """"helper for FenestrationsurfaceDetailed"""
    return idf.newidfobject('FENESTRATIONSURFACE:DETAILED', **kwargs)
class FenestrationsurfaceDetailedMeta:
    idf_name = 'FENESTRATIONSURFACE:DETAILED'

def FloorAdiabatic(idf, **kwargs: Unpack[FloorAdiabaticType]):
    """"helper for FloorAdiabatic"""
    return idf.newidfobject('FLOOR:ADIABATIC', **kwargs)
class FloorAdiabaticMeta:
    idf_name = 'FLOOR:ADIABATIC'

def FloorDetailed(idf, **kwargs: Unpack[FloorDetailedType]):
    """"helper for FloorDetailed"""
    return idf.newidfobject('FLOOR:DETAILED', **kwargs)
class FloorDetailedMeta:
    idf_name = 'FLOOR:DETAILED'

def FloorGroundcontact(idf, **kwargs: Unpack[FloorGroundcontactType]):
    """"helper for FloorGroundcontact"""
    return idf.newidfobject('FLOOR:GROUNDCONTACT', **kwargs)
class FloorGroundcontactMeta:
    idf_name = 'FLOOR:GROUNDCONTACT'

def FloorInterzone(idf, **kwargs: Unpack[FloorInterzoneType]):
    """"helper for FloorInterzone"""
    return idf.newidfobject('FLOOR:INTERZONE', **kwargs)
class FloorInterzoneMeta:
    idf_name = 'FLOOR:INTERZONE'

def FluidcoolerSinglespeed(idf, **kwargs: Unpack[FluidcoolerSinglespeedType]):
    """"helper for FluidcoolerSinglespeed"""
    return idf.newidfobject('FLUIDCOOLER:SINGLESPEED', **kwargs)
class FluidcoolerSinglespeedMeta:
    idf_name = 'FLUIDCOOLER:SINGLESPEED'

def FluidcoolerTwospeed(idf, **kwargs: Unpack[FluidcoolerTwospeedType]):
    """"helper for FluidcoolerTwospeed"""
    return idf.newidfobject('FLUIDCOOLER:TWOSPEED', **kwargs)
class FluidcoolerTwospeedMeta:
    idf_name = 'FLUIDCOOLER:TWOSPEED'

def FluidpropertiesConcentration(idf, **kwargs: Unpack[FluidpropertiesConcentrationType]):
    """"helper for FluidpropertiesConcentration"""
    return idf.newidfobject('FLUIDPROPERTIES:CONCENTRATION', **kwargs)
class FluidpropertiesConcentrationMeta:
    idf_name = 'FLUIDPROPERTIES:CONCENTRATION'

def FluidpropertiesGlycolconcentration(idf, **kwargs: Unpack[FluidpropertiesGlycolconcentrationType]):
    """"helper for FluidpropertiesGlycolconcentration"""
    return idf.newidfobject('FLUIDPROPERTIES:GLYCOLCONCENTRATION', **kwargs)
class FluidpropertiesGlycolconcentrationMeta:
    idf_name = 'FLUIDPROPERTIES:GLYCOLCONCENTRATION'

def FluidpropertiesName(idf, **kwargs: Unpack[FluidpropertiesNameType]):
    """"helper for FluidpropertiesName"""
    return idf.newidfobject('FLUIDPROPERTIES:NAME', **kwargs)
class FluidpropertiesNameMeta:
    idf_name = 'FLUIDPROPERTIES:NAME'

def FluidpropertiesSaturated(idf, **kwargs: Unpack[FluidpropertiesSaturatedType]):
    """"helper for FluidpropertiesSaturated"""
    return idf.newidfobject('FLUIDPROPERTIES:SATURATED', **kwargs)
class FluidpropertiesSaturatedMeta:
    idf_name = 'FLUIDPROPERTIES:SATURATED'

def FluidpropertiesSuperheated(idf, **kwargs: Unpack[FluidpropertiesSuperheatedType]):
    """"helper for FluidpropertiesSuperheated"""
    return idf.newidfobject('FLUIDPROPERTIES:SUPERHEATED', **kwargs)
class FluidpropertiesSuperheatedMeta:
    idf_name = 'FLUIDPROPERTIES:SUPERHEATED'

def FluidpropertiesTemperatures(idf, **kwargs: Unpack[FluidpropertiesTemperaturesType]):
    """"helper for FluidpropertiesTemperatures"""
    return idf.newidfobject('FLUIDPROPERTIES:TEMPERATURES', **kwargs)
class FluidpropertiesTemperaturesMeta:
    idf_name = 'FLUIDPROPERTIES:TEMPERATURES'

def FoundationKiva(idf, **kwargs: Unpack[FoundationKivaType]):
    """"helper for FoundationKiva"""
    return idf.newidfobject('FOUNDATION:KIVA', **kwargs)
class FoundationKivaMeta:
    idf_name = 'FOUNDATION:KIVA'

def FoundationKivaSettings(idf, **kwargs: Unpack[FoundationKivaSettingsType]):
    """"helper for FoundationKivaSettings"""
    return idf.newidfobject('FOUNDATION:KIVA:SETTINGS', **kwargs)
class FoundationKivaSettingsMeta:
    idf_name = 'FOUNDATION:KIVA:SETTINGS'

def Fuelfactors(idf, **kwargs: Unpack[FuelfactorsType]):
    """"helper for Fuelfactors"""
    return idf.newidfobject('FUELFACTORS', **kwargs)
class FuelfactorsMeta:
    idf_name = 'FUELFACTORS'

def Gasequipment(idf, **kwargs: Unpack[GasequipmentType]):
    """"helper for Gasequipment"""
    return idf.newidfobject('GASEQUIPMENT', **kwargs)
class GasequipmentMeta:
    idf_name = 'GASEQUIPMENT'

def GeneratorCombustionturbine(idf, **kwargs: Unpack[GeneratorCombustionturbineType]):
    """"helper for GeneratorCombustionturbine"""
    return idf.newidfobject('GENERATOR:COMBUSTIONTURBINE', **kwargs)
class GeneratorCombustionturbineMeta:
    idf_name = 'GENERATOR:COMBUSTIONTURBINE'

def GeneratorFuelcell(idf, **kwargs: Unpack[GeneratorFuelcellType]):
    """"helper for GeneratorFuelcell"""
    return idf.newidfobject('GENERATOR:FUELCELL', **kwargs)
class GeneratorFuelcellMeta:
    idf_name = 'GENERATOR:FUELCELL'

def GeneratorFuelcellAirsupply(idf, **kwargs: Unpack[GeneratorFuelcellAirsupplyType]):
    """"helper for GeneratorFuelcellAirsupply"""
    return idf.newidfobject('GENERATOR:FUELCELL:AIRSUPPLY', **kwargs)
class GeneratorFuelcellAirsupplyMeta:
    idf_name = 'GENERATOR:FUELCELL:AIRSUPPLY'

def GeneratorFuelcellAuxiliaryheater(idf, **kwargs: Unpack[GeneratorFuelcellAuxiliaryheaterType]):
    """"helper for GeneratorFuelcellAuxiliaryheater"""
    return idf.newidfobject('GENERATOR:FUELCELL:AUXILIARYHEATER', **kwargs)
class GeneratorFuelcellAuxiliaryheaterMeta:
    idf_name = 'GENERATOR:FUELCELL:AUXILIARYHEATER'

def GeneratorFuelcellElectricalstorage(idf, **kwargs: Unpack[GeneratorFuelcellElectricalstorageType]):
    """"helper for GeneratorFuelcellElectricalstorage"""
    return idf.newidfobject('GENERATOR:FUELCELL:ELECTRICALSTORAGE', **kwargs)
class GeneratorFuelcellElectricalstorageMeta:
    idf_name = 'GENERATOR:FUELCELL:ELECTRICALSTORAGE'

def GeneratorFuelcellExhaustgastowaterheatexchanger(idf, **kwargs: Unpack[GeneratorFuelcellExhaustgastowaterheatexchangerType]):
    """"helper for GeneratorFuelcellExhaustgastowaterheatexchanger"""
    return idf.newidfobject('GENERATOR:FUELCELL:EXHAUSTGASTOWATERHEATEXCHANGER', **kwargs)
class GeneratorFuelcellExhaustgastowaterheatexchangerMeta:
    idf_name = 'GENERATOR:FUELCELL:EXHAUSTGASTOWATERHEATEXCHANGER'

def GeneratorFuelcellInverter(idf, **kwargs: Unpack[GeneratorFuelcellInverterType]):
    """"helper for GeneratorFuelcellInverter"""
    return idf.newidfobject('GENERATOR:FUELCELL:INVERTER', **kwargs)
class GeneratorFuelcellInverterMeta:
    idf_name = 'GENERATOR:FUELCELL:INVERTER'

def GeneratorFuelcellPowermodule(idf, **kwargs: Unpack[GeneratorFuelcellPowermoduleType]):
    """"helper for GeneratorFuelcellPowermodule"""
    return idf.newidfobject('GENERATOR:FUELCELL:POWERMODULE', **kwargs)
class GeneratorFuelcellPowermoduleMeta:
    idf_name = 'GENERATOR:FUELCELL:POWERMODULE'

def GeneratorFuelcellStackcooler(idf, **kwargs: Unpack[GeneratorFuelcellStackcoolerType]):
    """"helper for GeneratorFuelcellStackcooler"""
    return idf.newidfobject('GENERATOR:FUELCELL:STACKCOOLER', **kwargs)
class GeneratorFuelcellStackcoolerMeta:
    idf_name = 'GENERATOR:FUELCELL:STACKCOOLER'

def GeneratorFuelcellWatersupply(idf, **kwargs: Unpack[GeneratorFuelcellWatersupplyType]):
    """"helper for GeneratorFuelcellWatersupply"""
    return idf.newidfobject('GENERATOR:FUELCELL:WATERSUPPLY', **kwargs)
class GeneratorFuelcellWatersupplyMeta:
    idf_name = 'GENERATOR:FUELCELL:WATERSUPPLY'

def GeneratorFuelsupply(idf, **kwargs: Unpack[GeneratorFuelsupplyType]):
    """"helper for GeneratorFuelsupply"""
    return idf.newidfobject('GENERATOR:FUELSUPPLY', **kwargs)
class GeneratorFuelsupplyMeta:
    idf_name = 'GENERATOR:FUELSUPPLY'

def GeneratorInternalcombustionengine(idf, **kwargs: Unpack[GeneratorInternalcombustionengineType]):
    """"helper for GeneratorInternalcombustionengine"""
    return idf.newidfobject('GENERATOR:INTERNALCOMBUSTIONENGINE', **kwargs)
class GeneratorInternalcombustionengineMeta:
    idf_name = 'GENERATOR:INTERNALCOMBUSTIONENGINE'

def GeneratorMicrochp(idf, **kwargs: Unpack[GeneratorMicrochpType]):
    """"helper for GeneratorMicrochp"""
    return idf.newidfobject('GENERATOR:MICROCHP', **kwargs)
class GeneratorMicrochpMeta:
    idf_name = 'GENERATOR:MICROCHP'

def GeneratorMicrochpNonnormalizedparameters(idf, **kwargs: Unpack[GeneratorMicrochpNonnormalizedparametersType]):
    """"helper for GeneratorMicrochpNonnormalizedparameters"""
    return idf.newidfobject('GENERATOR:MICROCHP:NONNORMALIZEDPARAMETERS', **kwargs)
class GeneratorMicrochpNonnormalizedparametersMeta:
    idf_name = 'GENERATOR:MICROCHP:NONNORMALIZEDPARAMETERS'

def GeneratorMicroturbine(idf, **kwargs: Unpack[GeneratorMicroturbineType]):
    """"helper for GeneratorMicroturbine"""
    return idf.newidfobject('GENERATOR:MICROTURBINE', **kwargs)
class GeneratorMicroturbineMeta:
    idf_name = 'GENERATOR:MICROTURBINE'

def GeneratorPhotovoltaic(idf, **kwargs: Unpack[GeneratorPhotovoltaicType]):
    """"helper for GeneratorPhotovoltaic"""
    return idf.newidfobject('GENERATOR:PHOTOVOLTAIC', **kwargs)
class GeneratorPhotovoltaicMeta:
    idf_name = 'GENERATOR:PHOTOVOLTAIC'

def GeneratorPvwatts(idf, **kwargs: Unpack[GeneratorPvwattsType]):
    """"helper for GeneratorPvwatts"""
    return idf.newidfobject('GENERATOR:PVWATTS', **kwargs)
class GeneratorPvwattsMeta:
    idf_name = 'GENERATOR:PVWATTS'

def GeneratorWindturbine(idf, **kwargs: Unpack[GeneratorWindturbineType]):
    """"helper for GeneratorWindturbine"""
    return idf.newidfobject('GENERATOR:WINDTURBINE', **kwargs)
class GeneratorWindturbineMeta:
    idf_name = 'GENERATOR:WINDTURBINE'

def Geometrytransform(idf, **kwargs: Unpack[GeometrytransformType]):
    """"helper for Geometrytransform"""
    return idf.newidfobject('GEOMETRYTRANSFORM', **kwargs)
class GeometrytransformMeta:
    idf_name = 'GEOMETRYTRANSFORM'

def Glazeddoor(idf, **kwargs: Unpack[GlazeddoorType]):
    """"helper for Glazeddoor"""
    return idf.newidfobject('GLAZEDDOOR', **kwargs)
class GlazeddoorMeta:
    idf_name = 'GLAZEDDOOR'

def GlazeddoorInterzone(idf, **kwargs: Unpack[GlazeddoorInterzoneType]):
    """"helper for GlazeddoorInterzone"""
    return idf.newidfobject('GLAZEDDOOR:INTERZONE', **kwargs)
class GlazeddoorInterzoneMeta:
    idf_name = 'GLAZEDDOOR:INTERZONE'

def Globalgeometryrules(idf, **kwargs: Unpack[GlobalgeometryrulesType]):
    """"helper for Globalgeometryrules"""
    return idf.newidfobject('GLOBALGEOMETRYRULES', **kwargs)
class GlobalgeometryrulesMeta:
    idf_name = 'GLOBALGEOMETRYRULES'

def GroundheatexchangerHorizontaltrench(idf, **kwargs: Unpack[GroundheatexchangerHorizontaltrenchType]):
    """"helper for GroundheatexchangerHorizontaltrench"""
    return idf.newidfobject('GROUNDHEATEXCHANGER:HORIZONTALTRENCH', **kwargs)
class GroundheatexchangerHorizontaltrenchMeta:
    idf_name = 'GROUNDHEATEXCHANGER:HORIZONTALTRENCH'

def GroundheatexchangerPond(idf, **kwargs: Unpack[GroundheatexchangerPondType]):
    """"helper for GroundheatexchangerPond"""
    return idf.newidfobject('GROUNDHEATEXCHANGER:POND', **kwargs)
class GroundheatexchangerPondMeta:
    idf_name = 'GROUNDHEATEXCHANGER:POND'

def GroundheatexchangerResponsefactors(idf, **kwargs: Unpack[GroundheatexchangerResponsefactorsType]):
    """"helper for GroundheatexchangerResponsefactors"""
    return idf.newidfobject('GROUNDHEATEXCHANGER:RESPONSEFACTORS', **kwargs)
class GroundheatexchangerResponsefactorsMeta:
    idf_name = 'GROUNDHEATEXCHANGER:RESPONSEFACTORS'

def GroundheatexchangerSlinky(idf, **kwargs: Unpack[GroundheatexchangerSlinkyType]):
    """"helper for GroundheatexchangerSlinky"""
    return idf.newidfobject('GROUNDHEATEXCHANGER:SLINKY', **kwargs)
class GroundheatexchangerSlinkyMeta:
    idf_name = 'GROUNDHEATEXCHANGER:SLINKY'

def GroundheatexchangerSurface(idf, **kwargs: Unpack[GroundheatexchangerSurfaceType]):
    """"helper for GroundheatexchangerSurface"""
    return idf.newidfobject('GROUNDHEATEXCHANGER:SURFACE', **kwargs)
class GroundheatexchangerSurfaceMeta:
    idf_name = 'GROUNDHEATEXCHANGER:SURFACE'

def GroundheatexchangerSystem(idf, **kwargs: Unpack[GroundheatexchangerSystemType]):
    """"helper for GroundheatexchangerSystem"""
    return idf.newidfobject('GROUNDHEATEXCHANGER:SYSTEM', **kwargs)
class GroundheatexchangerSystemMeta:
    idf_name = 'GROUNDHEATEXCHANGER:SYSTEM'

def GroundheatexchangerVerticalArray(idf, **kwargs: Unpack[GroundheatexchangerVerticalArrayType]):
    """"helper for GroundheatexchangerVerticalArray"""
    return idf.newidfobject('GROUNDHEATEXCHANGER:VERTICAL:ARRAY', **kwargs)
class GroundheatexchangerVerticalArrayMeta:
    idf_name = 'GROUNDHEATEXCHANGER:VERTICAL:ARRAY'

def GroundheatexchangerVerticalProperties(idf, **kwargs: Unpack[GroundheatexchangerVerticalPropertiesType]):
    """"helper for GroundheatexchangerVerticalProperties"""
    return idf.newidfobject('GROUNDHEATEXCHANGER:VERTICAL:PROPERTIES', **kwargs)
class GroundheatexchangerVerticalPropertiesMeta:
    idf_name = 'GROUNDHEATEXCHANGER:VERTICAL:PROPERTIES'

def GroundheatexchangerVerticalSingle(idf, **kwargs: Unpack[GroundheatexchangerVerticalSingleType]):
    """"helper for GroundheatexchangerVerticalSingle"""
    return idf.newidfobject('GROUNDHEATEXCHANGER:VERTICAL:SINGLE', **kwargs)
class GroundheatexchangerVerticalSingleMeta:
    idf_name = 'GROUNDHEATEXCHANGER:VERTICAL:SINGLE'

def GroundheattransferBasementAutogrid(idf, **kwargs: Unpack[GroundheattransferBasementAutogridType]):
    """"helper for GroundheattransferBasementAutogrid"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:AUTOGRID', **kwargs)
class GroundheattransferBasementAutogridMeta:
    idf_name = 'GROUNDHEATTRANSFER:BASEMENT:AUTOGRID'

def GroundheattransferBasementBldgdata(idf, **kwargs: Unpack[GroundheattransferBasementBldgdataType]):
    """"helper for GroundheattransferBasementBldgdata"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:BLDGDATA', **kwargs)
class GroundheattransferBasementBldgdataMeta:
    idf_name = 'GROUNDHEATTRANSFER:BASEMENT:BLDGDATA'

def GroundheattransferBasementCombldg(idf, **kwargs: Unpack[GroundheattransferBasementCombldgType]):
    """"helper for GroundheattransferBasementCombldg"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:COMBLDG', **kwargs)
class GroundheattransferBasementCombldgMeta:
    idf_name = 'GROUNDHEATTRANSFER:BASEMENT:COMBLDG'

def GroundheattransferBasementEquivautogrid(idf, **kwargs: Unpack[GroundheattransferBasementEquivautogridType]):
    """"helper for GroundheattransferBasementEquivautogrid"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:EQUIVAUTOGRID', **kwargs)
class GroundheattransferBasementEquivautogridMeta:
    idf_name = 'GROUNDHEATTRANSFER:BASEMENT:EQUIVAUTOGRID'

def GroundheattransferBasementEquivslab(idf, **kwargs: Unpack[GroundheattransferBasementEquivslabType]):
    """"helper for GroundheattransferBasementEquivslab"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:EQUIVSLAB', **kwargs)
class GroundheattransferBasementEquivslabMeta:
    idf_name = 'GROUNDHEATTRANSFER:BASEMENT:EQUIVSLAB'

def GroundheattransferBasementInsulation(idf, **kwargs: Unpack[GroundheattransferBasementInsulationType]):
    """"helper for GroundheattransferBasementInsulation"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:INSULATION', **kwargs)
class GroundheattransferBasementInsulationMeta:
    idf_name = 'GROUNDHEATTRANSFER:BASEMENT:INSULATION'

def GroundheattransferBasementInterior(idf, **kwargs: Unpack[GroundheattransferBasementInteriorType]):
    """"helper for GroundheattransferBasementInterior"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:INTERIOR', **kwargs)
class GroundheattransferBasementInteriorMeta:
    idf_name = 'GROUNDHEATTRANSFER:BASEMENT:INTERIOR'

def GroundheattransferBasementManualgrid(idf, **kwargs: Unpack[GroundheattransferBasementManualgridType]):
    """"helper for GroundheattransferBasementManualgrid"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:MANUALGRID', **kwargs)
class GroundheattransferBasementManualgridMeta:
    idf_name = 'GROUNDHEATTRANSFER:BASEMENT:MANUALGRID'

def GroundheattransferBasementMatlprops(idf, **kwargs: Unpack[GroundheattransferBasementMatlpropsType]):
    """"helper for GroundheattransferBasementMatlprops"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:MATLPROPS', **kwargs)
class GroundheattransferBasementMatlpropsMeta:
    idf_name = 'GROUNDHEATTRANSFER:BASEMENT:MATLPROPS'

def GroundheattransferBasementSimparameters(idf, **kwargs: Unpack[GroundheattransferBasementSimparametersType]):
    """"helper for GroundheattransferBasementSimparameters"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:SIMPARAMETERS', **kwargs)
class GroundheattransferBasementSimparametersMeta:
    idf_name = 'GROUNDHEATTRANSFER:BASEMENT:SIMPARAMETERS'

def GroundheattransferBasementSurfaceprops(idf, **kwargs: Unpack[GroundheattransferBasementSurfacepropsType]):
    """"helper for GroundheattransferBasementSurfaceprops"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:SURFACEPROPS', **kwargs)
class GroundheattransferBasementSurfacepropsMeta:
    idf_name = 'GROUNDHEATTRANSFER:BASEMENT:SURFACEPROPS'

def GroundheattransferBasementXface(idf, **kwargs: Unpack[GroundheattransferBasementXfaceType]):
    """"helper for GroundheattransferBasementXface"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:XFACE', **kwargs)
class GroundheattransferBasementXfaceMeta:
    idf_name = 'GROUNDHEATTRANSFER:BASEMENT:XFACE'

def GroundheattransferBasementYface(idf, **kwargs: Unpack[GroundheattransferBasementYfaceType]):
    """"helper for GroundheattransferBasementYface"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:YFACE', **kwargs)
class GroundheattransferBasementYfaceMeta:
    idf_name = 'GROUNDHEATTRANSFER:BASEMENT:YFACE'

def GroundheattransferBasementZface(idf, **kwargs: Unpack[GroundheattransferBasementZfaceType]):
    """"helper for GroundheattransferBasementZface"""
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:ZFACE', **kwargs)
class GroundheattransferBasementZfaceMeta:
    idf_name = 'GROUNDHEATTRANSFER:BASEMENT:ZFACE'

def GroundheattransferControl(idf, **kwargs: Unpack[GroundheattransferControlType]):
    """"helper for GroundheattransferControl"""
    return idf.newidfobject('GROUNDHEATTRANSFER:CONTROL', **kwargs)
class GroundheattransferControlMeta:
    idf_name = 'GROUNDHEATTRANSFER:CONTROL'

def GroundheattransferSlabAutogrid(idf, **kwargs: Unpack[GroundheattransferSlabAutogridType]):
    """"helper for GroundheattransferSlabAutogrid"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:AUTOGRID', **kwargs)
class GroundheattransferSlabAutogridMeta:
    idf_name = 'GROUNDHEATTRANSFER:SLAB:AUTOGRID'

def GroundheattransferSlabBldgprops(idf, **kwargs: Unpack[GroundheattransferSlabBldgpropsType]):
    """"helper for GroundheattransferSlabBldgprops"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:BLDGPROPS', **kwargs)
class GroundheattransferSlabBldgpropsMeta:
    idf_name = 'GROUNDHEATTRANSFER:SLAB:BLDGPROPS'

def GroundheattransferSlabBoundconds(idf, **kwargs: Unpack[GroundheattransferSlabBoundcondsType]):
    """"helper for GroundheattransferSlabBoundconds"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:BOUNDCONDS', **kwargs)
class GroundheattransferSlabBoundcondsMeta:
    idf_name = 'GROUNDHEATTRANSFER:SLAB:BOUNDCONDS'

def GroundheattransferSlabEquivalentslab(idf, **kwargs: Unpack[GroundheattransferSlabEquivalentslabType]):
    """"helper for GroundheattransferSlabEquivalentslab"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:EQUIVALENTSLAB', **kwargs)
class GroundheattransferSlabEquivalentslabMeta:
    idf_name = 'GROUNDHEATTRANSFER:SLAB:EQUIVALENTSLAB'

def GroundheattransferSlabInsulation(idf, **kwargs: Unpack[GroundheattransferSlabInsulationType]):
    """"helper for GroundheattransferSlabInsulation"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:INSULATION', **kwargs)
class GroundheattransferSlabInsulationMeta:
    idf_name = 'GROUNDHEATTRANSFER:SLAB:INSULATION'

def GroundheattransferSlabManualgrid(idf, **kwargs: Unpack[GroundheattransferSlabManualgridType]):
    """"helper for GroundheattransferSlabManualgrid"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:MANUALGRID', **kwargs)
class GroundheattransferSlabManualgridMeta:
    idf_name = 'GROUNDHEATTRANSFER:SLAB:MANUALGRID'

def GroundheattransferSlabMaterials(idf, **kwargs: Unpack[GroundheattransferSlabMaterialsType]):
    """"helper for GroundheattransferSlabMaterials"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:MATERIALS', **kwargs)
class GroundheattransferSlabMaterialsMeta:
    idf_name = 'GROUNDHEATTRANSFER:SLAB:MATERIALS'

def GroundheattransferSlabMatlprops(idf, **kwargs: Unpack[GroundheattransferSlabMatlpropsType]):
    """"helper for GroundheattransferSlabMatlprops"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:MATLPROPS', **kwargs)
class GroundheattransferSlabMatlpropsMeta:
    idf_name = 'GROUNDHEATTRANSFER:SLAB:MATLPROPS'

def GroundheattransferSlabXface(idf, **kwargs: Unpack[GroundheattransferSlabXfaceType]):
    """"helper for GroundheattransferSlabXface"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:XFACE', **kwargs)
class GroundheattransferSlabXfaceMeta:
    idf_name = 'GROUNDHEATTRANSFER:SLAB:XFACE'

def GroundheattransferSlabYface(idf, **kwargs: Unpack[GroundheattransferSlabYfaceType]):
    """"helper for GroundheattransferSlabYface"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:YFACE', **kwargs)
class GroundheattransferSlabYfaceMeta:
    idf_name = 'GROUNDHEATTRANSFER:SLAB:YFACE'

def GroundheattransferSlabZface(idf, **kwargs: Unpack[GroundheattransferSlabZfaceType]):
    """"helper for GroundheattransferSlabZface"""
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:ZFACE', **kwargs)
class GroundheattransferSlabZfaceMeta:
    idf_name = 'GROUNDHEATTRANSFER:SLAB:ZFACE'

def HeaderedpumpsConstantspeed(idf, **kwargs: Unpack[HeaderedpumpsConstantspeedType]):
    """"helper for HeaderedpumpsConstantspeed"""
    return idf.newidfobject('HEADEREDPUMPS:CONSTANTSPEED', **kwargs)
class HeaderedpumpsConstantspeedMeta:
    idf_name = 'HEADEREDPUMPS:CONSTANTSPEED'

def HeaderedpumpsVariablespeed(idf, **kwargs: Unpack[HeaderedpumpsVariablespeedType]):
    """"helper for HeaderedpumpsVariablespeed"""
    return idf.newidfobject('HEADEREDPUMPS:VARIABLESPEED', **kwargs)
class HeaderedpumpsVariablespeedMeta:
    idf_name = 'HEADEREDPUMPS:VARIABLESPEED'

def Heatbalancealgorithm(idf, **kwargs: Unpack[HeatbalancealgorithmType]):
    """"helper for Heatbalancealgorithm"""
    return idf.newidfobject('HEATBALANCEALGORITHM', **kwargs)
class HeatbalancealgorithmMeta:
    idf_name = 'HEATBALANCEALGORITHM'

def HeatbalancesettingsConductionfinitedifference(idf, **kwargs: Unpack[HeatbalancesettingsConductionfinitedifferenceType]):
    """"helper for HeatbalancesettingsConductionfinitedifference"""
    return idf.newidfobject('HEATBALANCESETTINGS:CONDUCTIONFINITEDIFFERENCE', **kwargs)
class HeatbalancesettingsConductionfinitedifferenceMeta:
    idf_name = 'HEATBALANCESETTINGS:CONDUCTIONFINITEDIFFERENCE'

def HeatexchangerAirtoairFlatplate(idf, **kwargs: Unpack[HeatexchangerAirtoairFlatplateType]):
    """"helper for HeatexchangerAirtoairFlatplate"""
    return idf.newidfobject('HEATEXCHANGER:AIRTOAIR:FLATPLATE', **kwargs)
class HeatexchangerAirtoairFlatplateMeta:
    idf_name = 'HEATEXCHANGER:AIRTOAIR:FLATPLATE'

def HeatexchangerAirtoairSensibleandlatent(idf, **kwargs: Unpack[HeatexchangerAirtoairSensibleandlatentType]):
    """"helper for HeatexchangerAirtoairSensibleandlatent"""
    return idf.newidfobject('HEATEXCHANGER:AIRTOAIR:SENSIBLEANDLATENT', **kwargs)
class HeatexchangerAirtoairSensibleandlatentMeta:
    idf_name = 'HEATEXCHANGER:AIRTOAIR:SENSIBLEANDLATENT'

def HeatexchangerDesiccantBalancedflow(idf, **kwargs: Unpack[HeatexchangerDesiccantBalancedflowType]):
    """"helper for HeatexchangerDesiccantBalancedflow"""
    return idf.newidfobject('HEATEXCHANGER:DESICCANT:BALANCEDFLOW', **kwargs)
class HeatexchangerDesiccantBalancedflowMeta:
    idf_name = 'HEATEXCHANGER:DESICCANT:BALANCEDFLOW'

def HeatexchangerDesiccantBalancedflowPerformancedatatype1(idf, **kwargs: Unpack[HeatexchangerDesiccantBalancedflowPerformancedatatype1Type]):
    """"helper for HeatexchangerDesiccantBalancedflowPerformancedatatype1"""
    return idf.newidfobject('HEATEXCHANGER:DESICCANT:BALANCEDFLOW:PERFORMANCEDATATYPE1', **kwargs)
class HeatexchangerDesiccantBalancedflowPerformancedatatype1Meta:
    idf_name = 'HEATEXCHANGER:DESICCANT:BALANCEDFLOW:PERFORMANCEDATATYPE1'

def HeatexchangerFluidtofluid(idf, **kwargs: Unpack[HeatexchangerFluidtofluidType]):
    """"helper for HeatexchangerFluidtofluid"""
    return idf.newidfobject('HEATEXCHANGER:FLUIDTOFLUID', **kwargs)
class HeatexchangerFluidtofluidMeta:
    idf_name = 'HEATEXCHANGER:FLUIDTOFLUID'

def HeatpumpAirtowaterFuelfiredCooling(idf, **kwargs: Unpack[HeatpumpAirtowaterFuelfiredCoolingType]):
    """"helper for HeatpumpAirtowaterFuelfiredCooling"""
    return idf.newidfobject('HEATPUMP:AIRTOWATER:FUELFIRED:COOLING', **kwargs)
class HeatpumpAirtowaterFuelfiredCoolingMeta:
    idf_name = 'HEATPUMP:AIRTOWATER:FUELFIRED:COOLING'

def HeatpumpAirtowaterFuelfiredHeating(idf, **kwargs: Unpack[HeatpumpAirtowaterFuelfiredHeatingType]):
    """"helper for HeatpumpAirtowaterFuelfiredHeating"""
    return idf.newidfobject('HEATPUMP:AIRTOWATER:FUELFIRED:HEATING', **kwargs)
class HeatpumpAirtowaterFuelfiredHeatingMeta:
    idf_name = 'HEATPUMP:AIRTOWATER:FUELFIRED:HEATING'

def HeatpumpPlantloopEirCooling(idf, **kwargs: Unpack[HeatpumpPlantloopEirCoolingType]):
    """"helper for HeatpumpPlantloopEirCooling"""
    return idf.newidfobject('HEATPUMP:PLANTLOOP:EIR:COOLING', **kwargs)
class HeatpumpPlantloopEirCoolingMeta:
    idf_name = 'HEATPUMP:PLANTLOOP:EIR:COOLING'

def HeatpumpPlantloopEirHeating(idf, **kwargs: Unpack[HeatpumpPlantloopEirHeatingType]):
    """"helper for HeatpumpPlantloopEirHeating"""
    return idf.newidfobject('HEATPUMP:PLANTLOOP:EIR:HEATING', **kwargs)
class HeatpumpPlantloopEirHeatingMeta:
    idf_name = 'HEATPUMP:PLANTLOOP:EIR:HEATING'

def HeatpumpWatertowaterEquationfitCooling(idf, **kwargs: Unpack[HeatpumpWatertowaterEquationfitCoolingType]):
    """"helper for HeatpumpWatertowaterEquationfitCooling"""
    return idf.newidfobject('HEATPUMP:WATERTOWATER:EQUATIONFIT:COOLING', **kwargs)
class HeatpumpWatertowaterEquationfitCoolingMeta:
    idf_name = 'HEATPUMP:WATERTOWATER:EQUATIONFIT:COOLING'

def HeatpumpWatertowaterEquationfitHeating(idf, **kwargs: Unpack[HeatpumpWatertowaterEquationfitHeatingType]):
    """"helper for HeatpumpWatertowaterEquationfitHeating"""
    return idf.newidfobject('HEATPUMP:WATERTOWATER:EQUATIONFIT:HEATING', **kwargs)
class HeatpumpWatertowaterEquationfitHeatingMeta:
    idf_name = 'HEATPUMP:WATERTOWATER:EQUATIONFIT:HEATING'

def HeatpumpWatertowaterParameterestimationCooling(idf, **kwargs: Unpack[HeatpumpWatertowaterParameterestimationCoolingType]):
    """"helper for HeatpumpWatertowaterParameterestimationCooling"""
    return idf.newidfobject('HEATPUMP:WATERTOWATER:PARAMETERESTIMATION:COOLING', **kwargs)
class HeatpumpWatertowaterParameterestimationCoolingMeta:
    idf_name = 'HEATPUMP:WATERTOWATER:PARAMETERESTIMATION:COOLING'

def HeatpumpWatertowaterParameterestimationHeating(idf, **kwargs: Unpack[HeatpumpWatertowaterParameterestimationHeatingType]):
    """"helper for HeatpumpWatertowaterParameterestimationHeating"""
    return idf.newidfobject('HEATPUMP:WATERTOWATER:PARAMETERESTIMATION:HEATING', **kwargs)
class HeatpumpWatertowaterParameterestimationHeatingMeta:
    idf_name = 'HEATPUMP:WATERTOWATER:PARAMETERESTIMATION:HEATING'

def Hotwaterequipment(idf, **kwargs: Unpack[HotwaterequipmentType]):
    """"helper for Hotwaterequipment"""
    return idf.newidfobject('HOTWATEREQUIPMENT', **kwargs)
class HotwaterequipmentMeta:
    idf_name = 'HOTWATEREQUIPMENT'

def HumidifierSteamElectric(idf, **kwargs: Unpack[HumidifierSteamElectricType]):
    """"helper for HumidifierSteamElectric"""
    return idf.newidfobject('HUMIDIFIER:STEAM:ELECTRIC', **kwargs)
class HumidifierSteamElectricMeta:
    idf_name = 'HUMIDIFIER:STEAM:ELECTRIC'

def HumidifierSteamGas(idf, **kwargs: Unpack[HumidifierSteamGasType]):
    """"helper for HumidifierSteamGas"""
    return idf.newidfobject('HUMIDIFIER:STEAM:GAS', **kwargs)
class HumidifierSteamGasMeta:
    idf_name = 'HUMIDIFIER:STEAM:GAS'

def Hvacsystemrootfindingalgorithm(idf, **kwargs: Unpack[HvacsystemrootfindingalgorithmType]):
    """"helper for Hvacsystemrootfindingalgorithm"""
    return idf.newidfobject('HVACSYSTEMROOTFINDINGALGORITHM', **kwargs)
class HvacsystemrootfindingalgorithmMeta:
    idf_name = 'HVACSYSTEMROOTFINDINGALGORITHM'

def HvactemplatePlantBoiler(idf, **kwargs: Unpack[HvactemplatePlantBoilerType]):
    """"helper for HvactemplatePlantBoiler"""
    return idf.newidfobject('HVACTEMPLATE:PLANT:BOILER', **kwargs)
class HvactemplatePlantBoilerMeta:
    idf_name = 'HVACTEMPLATE:PLANT:BOILER'

def HvactemplatePlantBoilerObjectreference(idf, **kwargs: Unpack[HvactemplatePlantBoilerObjectreferenceType]):
    """"helper for HvactemplatePlantBoilerObjectreference"""
    return idf.newidfobject('HVACTEMPLATE:PLANT:BOILER:OBJECTREFERENCE', **kwargs)
class HvactemplatePlantBoilerObjectreferenceMeta:
    idf_name = 'HVACTEMPLATE:PLANT:BOILER:OBJECTREFERENCE'

def HvactemplatePlantChilledwaterloop(idf, **kwargs: Unpack[HvactemplatePlantChilledwaterloopType]):
    """"helper for HvactemplatePlantChilledwaterloop"""
    return idf.newidfobject('HVACTEMPLATE:PLANT:CHILLEDWATERLOOP', **kwargs)
class HvactemplatePlantChilledwaterloopMeta:
    idf_name = 'HVACTEMPLATE:PLANT:CHILLEDWATERLOOP'

def HvactemplatePlantChiller(idf, **kwargs: Unpack[HvactemplatePlantChillerType]):
    """"helper for HvactemplatePlantChiller"""
    return idf.newidfobject('HVACTEMPLATE:PLANT:CHILLER', **kwargs)
class HvactemplatePlantChillerMeta:
    idf_name = 'HVACTEMPLATE:PLANT:CHILLER'

def HvactemplatePlantChillerObjectreference(idf, **kwargs: Unpack[HvactemplatePlantChillerObjectreferenceType]):
    """"helper for HvactemplatePlantChillerObjectreference"""
    return idf.newidfobject('HVACTEMPLATE:PLANT:CHILLER:OBJECTREFERENCE', **kwargs)
class HvactemplatePlantChillerObjectreferenceMeta:
    idf_name = 'HVACTEMPLATE:PLANT:CHILLER:OBJECTREFERENCE'

def HvactemplatePlantHotwaterloop(idf, **kwargs: Unpack[HvactemplatePlantHotwaterloopType]):
    """"helper for HvactemplatePlantHotwaterloop"""
    return idf.newidfobject('HVACTEMPLATE:PLANT:HOTWATERLOOP', **kwargs)
class HvactemplatePlantHotwaterloopMeta:
    idf_name = 'HVACTEMPLATE:PLANT:HOTWATERLOOP'

def HvactemplatePlantMixedwaterloop(idf, **kwargs: Unpack[HvactemplatePlantMixedwaterloopType]):
    """"helper for HvactemplatePlantMixedwaterloop"""
    return idf.newidfobject('HVACTEMPLATE:PLANT:MIXEDWATERLOOP', **kwargs)
class HvactemplatePlantMixedwaterloopMeta:
    idf_name = 'HVACTEMPLATE:PLANT:MIXEDWATERLOOP'

def HvactemplatePlantTower(idf, **kwargs: Unpack[HvactemplatePlantTowerType]):
    """"helper for HvactemplatePlantTower"""
    return idf.newidfobject('HVACTEMPLATE:PLANT:TOWER', **kwargs)
class HvactemplatePlantTowerMeta:
    idf_name = 'HVACTEMPLATE:PLANT:TOWER'

def HvactemplatePlantTowerObjectreference(idf, **kwargs: Unpack[HvactemplatePlantTowerObjectreferenceType]):
    """"helper for HvactemplatePlantTowerObjectreference"""
    return idf.newidfobject('HVACTEMPLATE:PLANT:TOWER:OBJECTREFERENCE', **kwargs)
class HvactemplatePlantTowerObjectreferenceMeta:
    idf_name = 'HVACTEMPLATE:PLANT:TOWER:OBJECTREFERENCE'

def HvactemplateSystemConstantvolume(idf, **kwargs: Unpack[HvactemplateSystemConstantvolumeType]):
    """"helper for HvactemplateSystemConstantvolume"""
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:CONSTANTVOLUME', **kwargs)
class HvactemplateSystemConstantvolumeMeta:
    idf_name = 'HVACTEMPLATE:SYSTEM:CONSTANTVOLUME'

def HvactemplateSystemDedicatedoutdoorair(idf, **kwargs: Unpack[HvactemplateSystemDedicatedoutdoorairType]):
    """"helper for HvactemplateSystemDedicatedoutdoorair"""
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:DEDICATEDOUTDOORAIR', **kwargs)
class HvactemplateSystemDedicatedoutdoorairMeta:
    idf_name = 'HVACTEMPLATE:SYSTEM:DEDICATEDOUTDOORAIR'

def HvactemplateSystemDualduct(idf, **kwargs: Unpack[HvactemplateSystemDualductType]):
    """"helper for HvactemplateSystemDualduct"""
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:DUALDUCT', **kwargs)
class HvactemplateSystemDualductMeta:
    idf_name = 'HVACTEMPLATE:SYSTEM:DUALDUCT'

def HvactemplateSystemPackagedvav(idf, **kwargs: Unpack[HvactemplateSystemPackagedvavType]):
    """"helper for HvactemplateSystemPackagedvav"""
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:PACKAGEDVAV', **kwargs)
class HvactemplateSystemPackagedvavMeta:
    idf_name = 'HVACTEMPLATE:SYSTEM:PACKAGEDVAV'

def HvactemplateSystemUnitary(idf, **kwargs: Unpack[HvactemplateSystemUnitaryType]):
    """"helper for HvactemplateSystemUnitary"""
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:UNITARY', **kwargs)
class HvactemplateSystemUnitaryMeta:
    idf_name = 'HVACTEMPLATE:SYSTEM:UNITARY'

def HvactemplateSystemUnitaryheatpumpAirtoair(idf, **kwargs: Unpack[HvactemplateSystemUnitaryheatpumpAirtoairType]):
    """"helper for HvactemplateSystemUnitaryheatpumpAirtoair"""
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:UNITARYHEATPUMP:AIRTOAIR', **kwargs)
class HvactemplateSystemUnitaryheatpumpAirtoairMeta:
    idf_name = 'HVACTEMPLATE:SYSTEM:UNITARYHEATPUMP:AIRTOAIR'

def HvactemplateSystemUnitarysystem(idf, **kwargs: Unpack[HvactemplateSystemUnitarysystemType]):
    """"helper for HvactemplateSystemUnitarysystem"""
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:UNITARYSYSTEM', **kwargs)
class HvactemplateSystemUnitarysystemMeta:
    idf_name = 'HVACTEMPLATE:SYSTEM:UNITARYSYSTEM'

def HvactemplateSystemVav(idf, **kwargs: Unpack[HvactemplateSystemVavType]):
    """"helper for HvactemplateSystemVav"""
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:VAV', **kwargs)
class HvactemplateSystemVavMeta:
    idf_name = 'HVACTEMPLATE:SYSTEM:VAV'

def HvactemplateSystemVrf(idf, **kwargs: Unpack[HvactemplateSystemVrfType]):
    """"helper for HvactemplateSystemVrf"""
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:VRF', **kwargs)
class HvactemplateSystemVrfMeta:
    idf_name = 'HVACTEMPLATE:SYSTEM:VRF'

def HvactemplateThermostat(idf, **kwargs: Unpack[HvactemplateThermostatType]):
    """"helper for HvactemplateThermostat"""
    return idf.newidfobject('HVACTEMPLATE:THERMOSTAT', **kwargs)
class HvactemplateThermostatMeta:
    idf_name = 'HVACTEMPLATE:THERMOSTAT'

def HvactemplateZoneBaseboardheat(idf, **kwargs: Unpack[HvactemplateZoneBaseboardheatType]):
    """"helper for HvactemplateZoneBaseboardheat"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:BASEBOARDHEAT', **kwargs)
class HvactemplateZoneBaseboardheatMeta:
    idf_name = 'HVACTEMPLATE:ZONE:BASEBOARDHEAT'

def HvactemplateZoneConstantvolume(idf, **kwargs: Unpack[HvactemplateZoneConstantvolumeType]):
    """"helper for HvactemplateZoneConstantvolume"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:CONSTANTVOLUME', **kwargs)
class HvactemplateZoneConstantvolumeMeta:
    idf_name = 'HVACTEMPLATE:ZONE:CONSTANTVOLUME'

def HvactemplateZoneDualduct(idf, **kwargs: Unpack[HvactemplateZoneDualductType]):
    """"helper for HvactemplateZoneDualduct"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:DUALDUCT', **kwargs)
class HvactemplateZoneDualductMeta:
    idf_name = 'HVACTEMPLATE:ZONE:DUALDUCT'

def HvactemplateZoneFancoil(idf, **kwargs: Unpack[HvactemplateZoneFancoilType]):
    """"helper for HvactemplateZoneFancoil"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:FANCOIL', **kwargs)
class HvactemplateZoneFancoilMeta:
    idf_name = 'HVACTEMPLATE:ZONE:FANCOIL'

def HvactemplateZoneIdealloadsairsystem(idf, **kwargs: Unpack[HvactemplateZoneIdealloadsairsystemType]):
    """"helper for HvactemplateZoneIdealloadsairsystem"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:IDEALLOADSAIRSYSTEM', **kwargs)
class HvactemplateZoneIdealloadsairsystemMeta:
    idf_name = 'HVACTEMPLATE:ZONE:IDEALLOADSAIRSYSTEM'

def HvactemplateZonePtac(idf, **kwargs: Unpack[HvactemplateZonePtacType]):
    """"helper for HvactemplateZonePtac"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:PTAC', **kwargs)
class HvactemplateZonePtacMeta:
    idf_name = 'HVACTEMPLATE:ZONE:PTAC'

def HvactemplateZonePthp(idf, **kwargs: Unpack[HvactemplateZonePthpType]):
    """"helper for HvactemplateZonePthp"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:PTHP', **kwargs)
class HvactemplateZonePthpMeta:
    idf_name = 'HVACTEMPLATE:ZONE:PTHP'

def HvactemplateZoneUnitary(idf, **kwargs: Unpack[HvactemplateZoneUnitaryType]):
    """"helper for HvactemplateZoneUnitary"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:UNITARY', **kwargs)
class HvactemplateZoneUnitaryMeta:
    idf_name = 'HVACTEMPLATE:ZONE:UNITARY'

def HvactemplateZoneVav(idf, **kwargs: Unpack[HvactemplateZoneVavType]):
    """"helper for HvactemplateZoneVav"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:VAV', **kwargs)
class HvactemplateZoneVavMeta:
    idf_name = 'HVACTEMPLATE:ZONE:VAV'

def HvactemplateZoneVavFanpowered(idf, **kwargs: Unpack[HvactemplateZoneVavFanpoweredType]):
    """"helper for HvactemplateZoneVavFanpowered"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:VAV:FANPOWERED', **kwargs)
class HvactemplateZoneVavFanpoweredMeta:
    idf_name = 'HVACTEMPLATE:ZONE:VAV:FANPOWERED'

def HvactemplateZoneVavHeatandcool(idf, **kwargs: Unpack[HvactemplateZoneVavHeatandcoolType]):
    """"helper for HvactemplateZoneVavHeatandcool"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:VAV:HEATANDCOOL', **kwargs)
class HvactemplateZoneVavHeatandcoolMeta:
    idf_name = 'HVACTEMPLATE:ZONE:VAV:HEATANDCOOL'

def HvactemplateZoneVrf(idf, **kwargs: Unpack[HvactemplateZoneVrfType]):
    """"helper for HvactemplateZoneVrf"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:VRF', **kwargs)
class HvactemplateZoneVrfMeta:
    idf_name = 'HVACTEMPLATE:ZONE:VRF'

def HvactemplateZoneWatertoairheatpump(idf, **kwargs: Unpack[HvactemplateZoneWatertoairheatpumpType]):
    """"helper for HvactemplateZoneWatertoairheatpump"""
    return idf.newidfobject('HVACTEMPLATE:ZONE:WATERTOAIRHEATPUMP', **kwargs)
class HvactemplateZoneWatertoairheatpumpMeta:
    idf_name = 'HVACTEMPLATE:ZONE:WATERTOAIRHEATPUMP'

def HybridmodelZone(idf, **kwargs: Unpack[HybridmodelZoneType]):
    """"helper for HybridmodelZone"""
    return idf.newidfobject('HYBRIDMODEL:ZONE', **kwargs)
class HybridmodelZoneMeta:
    idf_name = 'HYBRIDMODEL:ZONE'

def Indoorlivingwall(idf, **kwargs: Unpack[IndoorlivingwallType]):
    """"helper for Indoorlivingwall"""
    return idf.newidfobject('INDOORLIVINGWALL', **kwargs)
class IndoorlivingwallMeta:
    idf_name = 'INDOORLIVINGWALL'

def Internalmass(idf, **kwargs: Unpack[InternalmassType]):
    """"helper for Internalmass"""
    return idf.newidfobject('INTERNALMASS', **kwargs)
class InternalmassMeta:
    idf_name = 'INTERNALMASS'

def LifecyclecostNonrecurringcost(idf, **kwargs: Unpack[LifecyclecostNonrecurringcostType]):
    """"helper for LifecyclecostNonrecurringcost"""
    return idf.newidfobject('LIFECYCLECOST:NONRECURRINGCOST', **kwargs)
class LifecyclecostNonrecurringcostMeta:
    idf_name = 'LIFECYCLECOST:NONRECURRINGCOST'

def LifecyclecostParameters(idf, **kwargs: Unpack[LifecyclecostParametersType]):
    """"helper for LifecyclecostParameters"""
    return idf.newidfobject('LIFECYCLECOST:PARAMETERS', **kwargs)
class LifecyclecostParametersMeta:
    idf_name = 'LIFECYCLECOST:PARAMETERS'

def LifecyclecostRecurringcosts(idf, **kwargs: Unpack[LifecyclecostRecurringcostsType]):
    """"helper for LifecyclecostRecurringcosts"""
    return idf.newidfobject('LIFECYCLECOST:RECURRINGCOSTS', **kwargs)
class LifecyclecostRecurringcostsMeta:
    idf_name = 'LIFECYCLECOST:RECURRINGCOSTS'

def LifecyclecostUseadjustment(idf, **kwargs: Unpack[LifecyclecostUseadjustmentType]):
    """"helper for LifecyclecostUseadjustment"""
    return idf.newidfobject('LIFECYCLECOST:USEADJUSTMENT', **kwargs)
class LifecyclecostUseadjustmentMeta:
    idf_name = 'LIFECYCLECOST:USEADJUSTMENT'

def LifecyclecostUsepriceescalation(idf, **kwargs: Unpack[LifecyclecostUsepriceescalationType]):
    """"helper for LifecyclecostUsepriceescalation"""
    return idf.newidfobject('LIFECYCLECOST:USEPRICEESCALATION', **kwargs)
class LifecyclecostUsepriceescalationMeta:
    idf_name = 'LIFECYCLECOST:USEPRICEESCALATION'

def Lights(idf, **kwargs: Unpack[LightsType]):
    """"helper for Lights"""
    return idf.newidfobject('LIGHTS', **kwargs)
class LightsMeta:
    idf_name = 'LIGHTS'

def LoadprofilePlant(idf, **kwargs: Unpack[LoadprofilePlantType]):
    """"helper for LoadprofilePlant"""
    return idf.newidfobject('LOADPROFILE:PLANT', **kwargs)
class LoadprofilePlantMeta:
    idf_name = 'LOADPROFILE:PLANT'

def Material(idf, **kwargs: Unpack[MaterialType]):
    """"helper for Material"""
    return idf.newidfobject('MATERIAL', **kwargs)
class MaterialMeta:
    idf_name = 'MATERIAL'

def MaterialAirgap(idf, **kwargs: Unpack[MaterialAirgapType]):
    """"helper for MaterialAirgap"""
    return idf.newidfobject('MATERIAL:AIRGAP', **kwargs)
class MaterialAirgapMeta:
    idf_name = 'MATERIAL:AIRGAP'

def MaterialInfraredtransparent(idf, **kwargs: Unpack[MaterialInfraredtransparentType]):
    """"helper for MaterialInfraredtransparent"""
    return idf.newidfobject('MATERIAL:INFRAREDTRANSPARENT', **kwargs)
class MaterialInfraredtransparentMeta:
    idf_name = 'MATERIAL:INFRAREDTRANSPARENT'

def MaterialNomass(idf, **kwargs: Unpack[MaterialNomassType]):
    """"helper for MaterialNomass"""
    return idf.newidfobject('MATERIAL:NOMASS', **kwargs)
class MaterialNomassMeta:
    idf_name = 'MATERIAL:NOMASS'

def MaterialRoofvegetation(idf, **kwargs: Unpack[MaterialRoofvegetationType]):
    """"helper for MaterialRoofvegetation"""
    return idf.newidfobject('MATERIAL:ROOFVEGETATION', **kwargs)
class MaterialRoofvegetationMeta:
    idf_name = 'MATERIAL:ROOFVEGETATION'

def MaterialpropertyGlazingspectraldata(idf, **kwargs: Unpack[MaterialpropertyGlazingspectraldataType]):
    """"helper for MaterialpropertyGlazingspectraldata"""
    return idf.newidfobject('MATERIALPROPERTY:GLAZINGSPECTRALDATA', **kwargs)
class MaterialpropertyGlazingspectraldataMeta:
    idf_name = 'MATERIALPROPERTY:GLAZINGSPECTRALDATA'

def MaterialpropertyHeatandmoisturetransferDiffusion(idf, **kwargs: Unpack[MaterialpropertyHeatandmoisturetransferDiffusionType]):
    """"helper for MaterialpropertyHeatandmoisturetransferDiffusion"""
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:DIFFUSION', **kwargs)
class MaterialpropertyHeatandmoisturetransferDiffusionMeta:
    idf_name = 'MATERIALPROPERTY:HEATANDMOISTURETRANSFER:DIFFUSION'

def MaterialpropertyHeatandmoisturetransferRedistribution(idf, **kwargs: Unpack[MaterialpropertyHeatandmoisturetransferRedistributionType]):
    """"helper for MaterialpropertyHeatandmoisturetransferRedistribution"""
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:REDISTRIBUTION', **kwargs)
class MaterialpropertyHeatandmoisturetransferRedistributionMeta:
    idf_name = 'MATERIALPROPERTY:HEATANDMOISTURETRANSFER:REDISTRIBUTION'

def MaterialpropertyHeatandmoisturetransferSettings(idf, **kwargs: Unpack[MaterialpropertyHeatandmoisturetransferSettingsType]):
    """"helper for MaterialpropertyHeatandmoisturetransferSettings"""
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:SETTINGS', **kwargs)
class MaterialpropertyHeatandmoisturetransferSettingsMeta:
    idf_name = 'MATERIALPROPERTY:HEATANDMOISTURETRANSFER:SETTINGS'

def MaterialpropertyHeatandmoisturetransferSorptionisotherm(idf, **kwargs: Unpack[MaterialpropertyHeatandmoisturetransferSorptionisothermType]):
    """"helper for MaterialpropertyHeatandmoisturetransferSorptionisotherm"""
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:SORPTIONISOTHERM', **kwargs)
class MaterialpropertyHeatandmoisturetransferSorptionisothermMeta:
    idf_name = 'MATERIALPROPERTY:HEATANDMOISTURETRANSFER:SORPTIONISOTHERM'

def MaterialpropertyHeatandmoisturetransferSuction(idf, **kwargs: Unpack[MaterialpropertyHeatandmoisturetransferSuctionType]):
    """"helper for MaterialpropertyHeatandmoisturetransferSuction"""
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:SUCTION', **kwargs)
class MaterialpropertyHeatandmoisturetransferSuctionMeta:
    idf_name = 'MATERIALPROPERTY:HEATANDMOISTURETRANSFER:SUCTION'

def MaterialpropertyHeatandmoisturetransferThermalconductivity(idf, **kwargs: Unpack[MaterialpropertyHeatandmoisturetransferThermalconductivityType]):
    """"helper for MaterialpropertyHeatandmoisturetransferThermalconductivity"""
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:THERMALCONDUCTIVITY', **kwargs)
class MaterialpropertyHeatandmoisturetransferThermalconductivityMeta:
    idf_name = 'MATERIALPROPERTY:HEATANDMOISTURETRANSFER:THERMALCONDUCTIVITY'

def MaterialpropertyMoisturepenetrationdepthSettings(idf, **kwargs: Unpack[MaterialpropertyMoisturepenetrationdepthSettingsType]):
    """"helper for MaterialpropertyMoisturepenetrationdepthSettings"""
    return idf.newidfobject('MATERIALPROPERTY:MOISTUREPENETRATIONDEPTH:SETTINGS', **kwargs)
class MaterialpropertyMoisturepenetrationdepthSettingsMeta:
    idf_name = 'MATERIALPROPERTY:MOISTUREPENETRATIONDEPTH:SETTINGS'

def MaterialpropertyPhasechange(idf, **kwargs: Unpack[MaterialpropertyPhasechangeType]):
    """"helper for MaterialpropertyPhasechange"""
    return idf.newidfobject('MATERIALPROPERTY:PHASECHANGE', **kwargs)
class MaterialpropertyPhasechangeMeta:
    idf_name = 'MATERIALPROPERTY:PHASECHANGE'

def MaterialpropertyPhasechangehysteresis(idf, **kwargs: Unpack[MaterialpropertyPhasechangehysteresisType]):
    """"helper for MaterialpropertyPhasechangehysteresis"""
    return idf.newidfobject('MATERIALPROPERTY:PHASECHANGEHYSTERESIS', **kwargs)
class MaterialpropertyPhasechangehysteresisMeta:
    idf_name = 'MATERIALPROPERTY:PHASECHANGEHYSTERESIS'

def MaterialpropertyVariableabsorptance(idf, **kwargs: Unpack[MaterialpropertyVariableabsorptanceType]):
    """"helper for MaterialpropertyVariableabsorptance"""
    return idf.newidfobject('MATERIALPROPERTY:VARIABLEABSORPTANCE', **kwargs)
class MaterialpropertyVariableabsorptanceMeta:
    idf_name = 'MATERIALPROPERTY:VARIABLEABSORPTANCE'

def MaterialpropertyVariablethermalconductivity(idf, **kwargs: Unpack[MaterialpropertyVariablethermalconductivityType]):
    """"helper for MaterialpropertyVariablethermalconductivity"""
    return idf.newidfobject('MATERIALPROPERTY:VARIABLETHERMALCONDUCTIVITY', **kwargs)
class MaterialpropertyVariablethermalconductivityMeta:
    idf_name = 'MATERIALPROPERTY:VARIABLETHERMALCONDUCTIVITY'

def MatrixTwodimension(idf, **kwargs: Unpack[MatrixTwodimensionType]):
    """"helper for MatrixTwodimension"""
    return idf.newidfobject('MATRIX:TWODIMENSION', **kwargs)
class MatrixTwodimensionMeta:
    idf_name = 'MATRIX:TWODIMENSION'

def MeterCustom(idf, **kwargs: Unpack[MeterCustomType]):
    """"helper for MeterCustom"""
    return idf.newidfobject('METER:CUSTOM', **kwargs)
class MeterCustomMeta:
    idf_name = 'METER:CUSTOM'

def MeterCustomdecrement(idf, **kwargs: Unpack[MeterCustomdecrementType]):
    """"helper for MeterCustomdecrement"""
    return idf.newidfobject('METER:CUSTOMDECREMENT', **kwargs)
class MeterCustomdecrementMeta:
    idf_name = 'METER:CUSTOMDECREMENT'

def Nodelist(idf, **kwargs: Unpack[NodelistType]):
    """"helper for Nodelist"""
    return idf.newidfobject('NODELIST', **kwargs)
class NodelistMeta:
    idf_name = 'NODELIST'

def Otherequipment(idf, **kwargs: Unpack[OtherequipmentType]):
    """"helper for Otherequipment"""
    return idf.newidfobject('OTHEREQUIPMENT', **kwargs)
class OtherequipmentMeta:
    idf_name = 'OTHEREQUIPMENT'

def OutdoorairMixer(idf, **kwargs: Unpack[OutdoorairMixerType]):
    """"helper for OutdoorairMixer"""
    return idf.newidfobject('OUTDOORAIR:MIXER', **kwargs)
class OutdoorairMixerMeta:
    idf_name = 'OUTDOORAIR:MIXER'

def OutdoorairNode(idf, **kwargs: Unpack[OutdoorairNodeType]):
    """"helper for OutdoorairNode"""
    return idf.newidfobject('OUTDOORAIR:NODE', **kwargs)
class OutdoorairNodeMeta:
    idf_name = 'OUTDOORAIR:NODE'

def OutdoorairNodelist(idf, **kwargs: Unpack[OutdoorairNodelistType]):
    """"helper for OutdoorairNodelist"""
    return idf.newidfobject('OUTDOORAIR:NODELIST', **kwargs)
class OutdoorairNodelistMeta:
    idf_name = 'OUTDOORAIR:NODELIST'

def OutputConstructions(idf, **kwargs: Unpack[OutputConstructionsType]):
    """"helper for OutputConstructions"""
    return idf.newidfobject('OUTPUT:CONSTRUCTIONS', **kwargs)
class OutputConstructionsMeta:
    idf_name = 'OUTPUT:CONSTRUCTIONS'

def OutputDaylightfactors(idf, **kwargs: Unpack[OutputDaylightfactorsType]):
    """"helper for OutputDaylightfactors"""
    return idf.newidfobject('OUTPUT:DAYLIGHTFACTORS', **kwargs)
class OutputDaylightfactorsMeta:
    idf_name = 'OUTPUT:DAYLIGHTFACTORS'

def OutputDebuggingdata(idf, **kwargs: Unpack[OutputDebuggingdataType]):
    """"helper for OutputDebuggingdata"""
    return idf.newidfobject('OUTPUT:DEBUGGINGDATA', **kwargs)
class OutputDebuggingdataMeta:
    idf_name = 'OUTPUT:DEBUGGINGDATA'

def OutputDiagnostics(idf, **kwargs: Unpack[OutputDiagnosticsType]):
    """"helper for OutputDiagnostics"""
    return idf.newidfobject('OUTPUT:DIAGNOSTICS', **kwargs)
class OutputDiagnosticsMeta:
    idf_name = 'OUTPUT:DIAGNOSTICS'

def OutputEnergymanagementsystem(idf, **kwargs: Unpack[OutputEnergymanagementsystemType]):
    """"helper for OutputEnergymanagementsystem"""
    return idf.newidfobject('OUTPUT:ENERGYMANAGEMENTSYSTEM', **kwargs)
class OutputEnergymanagementsystemMeta:
    idf_name = 'OUTPUT:ENERGYMANAGEMENTSYSTEM'

def OutputEnvironmentalimpactfactors(idf, **kwargs: Unpack[OutputEnvironmentalimpactfactorsType]):
    """"helper for OutputEnvironmentalimpactfactors"""
    return idf.newidfobject('OUTPUT:ENVIRONMENTALIMPACTFACTORS', **kwargs)
class OutputEnvironmentalimpactfactorsMeta:
    idf_name = 'OUTPUT:ENVIRONMENTALIMPACTFACTORS'

def OutputIlluminancemap(idf, **kwargs: Unpack[OutputIlluminancemapType]):
    """"helper for OutputIlluminancemap"""
    return idf.newidfobject('OUTPUT:ILLUMINANCEMAP', **kwargs)
class OutputIlluminancemapMeta:
    idf_name = 'OUTPUT:ILLUMINANCEMAP'

def OutputJson(idf, **kwargs: Unpack[OutputJsonType]):
    """"helper for OutputJson"""
    return idf.newidfobject('OUTPUT:JSON', **kwargs)
class OutputJsonMeta:
    idf_name = 'OUTPUT:JSON'

def OutputMeter(idf, **kwargs: Unpack[OutputMeterType]):
    """"helper for OutputMeter"""
    return idf.newidfobject('OUTPUT:METER', **kwargs)
class OutputMeterMeta:
    idf_name = 'OUTPUT:METER'

def OutputMeterCumulative(idf, **kwargs: Unpack[OutputMeterCumulativeType]):
    """"helper for OutputMeterCumulative"""
    return idf.newidfobject('OUTPUT:METER:CUMULATIVE', **kwargs)
class OutputMeterCumulativeMeta:
    idf_name = 'OUTPUT:METER:CUMULATIVE'

def OutputMeterCumulativeMeterfileonly(idf, **kwargs: Unpack[OutputMeterCumulativeMeterfileonlyType]):
    """"helper for OutputMeterCumulativeMeterfileonly"""
    return idf.newidfobject('OUTPUT:METER:CUMULATIVE:METERFILEONLY', **kwargs)
class OutputMeterCumulativeMeterfileonlyMeta:
    idf_name = 'OUTPUT:METER:CUMULATIVE:METERFILEONLY'

def OutputMeterMeterfileonly(idf, **kwargs: Unpack[OutputMeterMeterfileonlyType]):
    """"helper for OutputMeterMeterfileonly"""
    return idf.newidfobject('OUTPUT:METER:METERFILEONLY', **kwargs)
class OutputMeterMeterfileonlyMeta:
    idf_name = 'OUTPUT:METER:METERFILEONLY'

def OutputPreprocessormessage(idf, **kwargs: Unpack[OutputPreprocessormessageType]):
    """"helper for OutputPreprocessormessage"""
    return idf.newidfobject('OUTPUT:PREPROCESSORMESSAGE', **kwargs)
class OutputPreprocessormessageMeta:
    idf_name = 'OUTPUT:PREPROCESSORMESSAGE'

def OutputSchedules(idf, **kwargs: Unpack[OutputSchedulesType]):
    """"helper for OutputSchedules"""
    return idf.newidfobject('OUTPUT:SCHEDULES', **kwargs)
class OutputSchedulesMeta:
    idf_name = 'OUTPUT:SCHEDULES'

def OutputSqlite(idf, **kwargs: Unpack[OutputSqliteType]):
    """"helper for OutputSqlite"""
    return idf.newidfobject('OUTPUT:SQLITE', **kwargs)
class OutputSqliteMeta:
    idf_name = 'OUTPUT:SQLITE'

def OutputSurfacesDrawing(idf, **kwargs: Unpack[OutputSurfacesDrawingType]):
    """"helper for OutputSurfacesDrawing"""
    return idf.newidfobject('OUTPUT:SURFACES:DRAWING', **kwargs)
class OutputSurfacesDrawingMeta:
    idf_name = 'OUTPUT:SURFACES:DRAWING'

def OutputSurfacesList(idf, **kwargs: Unpack[OutputSurfacesListType]):
    """"helper for OutputSurfacesList"""
    return idf.newidfobject('OUTPUT:SURFACES:LIST', **kwargs)
class OutputSurfacesListMeta:
    idf_name = 'OUTPUT:SURFACES:LIST'

def OutputTableAnnual(idf, **kwargs: Unpack[OutputTableAnnualType]):
    """"helper for OutputTableAnnual"""
    return idf.newidfobject('OUTPUT:TABLE:ANNUAL', **kwargs)
class OutputTableAnnualMeta:
    idf_name = 'OUTPUT:TABLE:ANNUAL'

def OutputTableMonthly(idf, **kwargs: Unpack[OutputTableMonthlyType]):
    """"helper for OutputTableMonthly"""
    return idf.newidfobject('OUTPUT:TABLE:MONTHLY', **kwargs)
class OutputTableMonthlyMeta:
    idf_name = 'OUTPUT:TABLE:MONTHLY'

def OutputTableReportperiod(idf, **kwargs: Unpack[OutputTableReportperiodType]):
    """"helper for OutputTableReportperiod"""
    return idf.newidfobject('OUTPUT:TABLE:REPORTPERIOD', **kwargs)
class OutputTableReportperiodMeta:
    idf_name = 'OUTPUT:TABLE:REPORTPERIOD'

def OutputTableSummaryreports(idf, **kwargs: Unpack[OutputTableSummaryreportsType]):
    """"helper for OutputTableSummaryreports"""
    return idf.newidfobject('OUTPUT:TABLE:SUMMARYREPORTS', **kwargs)
class OutputTableSummaryreportsMeta:
    idf_name = 'OUTPUT:TABLE:SUMMARYREPORTS'

def OutputTableTimebins(idf, **kwargs: Unpack[OutputTableTimebinsType]):
    """"helper for OutputTableTimebins"""
    return idf.newidfobject('OUTPUT:TABLE:TIMEBINS', **kwargs)
class OutputTableTimebinsMeta:
    idf_name = 'OUTPUT:TABLE:TIMEBINS'

def OutputVariable(idf, **kwargs: Unpack[OutputVariableType]):
    """"helper for OutputVariable"""
    return idf.newidfobject('OUTPUT:VARIABLE', **kwargs)
class OutputVariableMeta:
    idf_name = 'OUTPUT:VARIABLE'

def OutputVariabledictionary(idf, **kwargs: Unpack[OutputVariabledictionaryType]):
    """"helper for OutputVariabledictionary"""
    return idf.newidfobject('OUTPUT:VARIABLEDICTIONARY', **kwargs)
class OutputVariabledictionaryMeta:
    idf_name = 'OUTPUT:VARIABLEDICTIONARY'

def OutputcontrolFiles(idf, **kwargs: Unpack[OutputcontrolFilesType]):
    """"helper for OutputcontrolFiles"""
    return idf.newidfobject('OUTPUTCONTROL:FILES', **kwargs)
class OutputcontrolFilesMeta:
    idf_name = 'OUTPUTCONTROL:FILES'

def OutputcontrolIlluminancemapStyle(idf, **kwargs: Unpack[OutputcontrolIlluminancemapStyleType]):
    """"helper for OutputcontrolIlluminancemapStyle"""
    return idf.newidfobject('OUTPUTCONTROL:ILLUMINANCEMAP:STYLE', **kwargs)
class OutputcontrolIlluminancemapStyleMeta:
    idf_name = 'OUTPUTCONTROL:ILLUMINANCEMAP:STYLE'

def OutputcontrolReportingtolerances(idf, **kwargs: Unpack[OutputcontrolReportingtolerancesType]):
    """"helper for OutputcontrolReportingtolerances"""
    return idf.newidfobject('OUTPUTCONTROL:REPORTINGTOLERANCES', **kwargs)
class OutputcontrolReportingtolerancesMeta:
    idf_name = 'OUTPUTCONTROL:REPORTINGTOLERANCES'

def OutputcontrolSizingStyle(idf, **kwargs: Unpack[OutputcontrolSizingStyleType]):
    """"helper for OutputcontrolSizingStyle"""
    return idf.newidfobject('OUTPUTCONTROL:SIZING:STYLE', **kwargs)
class OutputcontrolSizingStyleMeta:
    idf_name = 'OUTPUTCONTROL:SIZING:STYLE'

def OutputcontrolSurfacecolorscheme(idf, **kwargs: Unpack[OutputcontrolSurfacecolorschemeType]):
    """"helper for OutputcontrolSurfacecolorscheme"""
    return idf.newidfobject('OUTPUTCONTROL:SURFACECOLORSCHEME', **kwargs)
class OutputcontrolSurfacecolorschemeMeta:
    idf_name = 'OUTPUTCONTROL:SURFACECOLORSCHEME'

def OutputcontrolTableStyle(idf, **kwargs: Unpack[OutputcontrolTableStyleType]):
    """"helper for OutputcontrolTableStyle"""
    return idf.newidfobject('OUTPUTCONTROL:TABLE:STYLE', **kwargs)
class OutputcontrolTableStyleMeta:
    idf_name = 'OUTPUTCONTROL:TABLE:STYLE'

def OutputcontrolTimestamp(idf, **kwargs: Unpack[OutputcontrolTimestampType]):
    """"helper for OutputcontrolTimestamp"""
    return idf.newidfobject('OUTPUTCONTROL:TIMESTAMP', **kwargs)
class OutputcontrolTimestampMeta:
    idf_name = 'OUTPUTCONTROL:TIMESTAMP'

def ParametricFilenamesuffix(idf, **kwargs: Unpack[ParametricFilenamesuffixType]):
    """"helper for ParametricFilenamesuffix"""
    return idf.newidfobject('PARAMETRIC:FILENAMESUFFIX', **kwargs)
class ParametricFilenamesuffixMeta:
    idf_name = 'PARAMETRIC:FILENAMESUFFIX'

def ParametricLogic(idf, **kwargs: Unpack[ParametricLogicType]):
    """"helper for ParametricLogic"""
    return idf.newidfobject('PARAMETRIC:LOGIC', **kwargs)
class ParametricLogicMeta:
    idf_name = 'PARAMETRIC:LOGIC'

def ParametricRuncontrol(idf, **kwargs: Unpack[ParametricRuncontrolType]):
    """"helper for ParametricRuncontrol"""
    return idf.newidfobject('PARAMETRIC:RUNCONTROL', **kwargs)
class ParametricRuncontrolMeta:
    idf_name = 'PARAMETRIC:RUNCONTROL'

def ParametricSetvalueforrun(idf, **kwargs: Unpack[ParametricSetvalueforrunType]):
    """"helper for ParametricSetvalueforrun"""
    return idf.newidfobject('PARAMETRIC:SETVALUEFORRUN', **kwargs)
class ParametricSetvalueforrunMeta:
    idf_name = 'PARAMETRIC:SETVALUEFORRUN'

def People(idf, **kwargs: Unpack[PeopleType]):
    """"helper for People"""
    return idf.newidfobject('PEOPLE', **kwargs)
class PeopleMeta:
    idf_name = 'PEOPLE'

def Performanceprecisiontradeoffs(idf, **kwargs: Unpack[PerformanceprecisiontradeoffsType]):
    """"helper for Performanceprecisiontradeoffs"""
    return idf.newidfobject('PERFORMANCEPRECISIONTRADEOFFS', **kwargs)
class PerformanceprecisiontradeoffsMeta:
    idf_name = 'PERFORMANCEPRECISIONTRADEOFFS'

def PhotovoltaicperformanceEquivalentonediode(idf, **kwargs: Unpack[PhotovoltaicperformanceEquivalentonediodeType]):
    """"helper for PhotovoltaicperformanceEquivalentonediode"""
    return idf.newidfobject('PHOTOVOLTAICPERFORMANCE:EQUIVALENTONE-DIODE', **kwargs)
class PhotovoltaicperformanceEquivalentonediodeMeta:
    idf_name = 'PHOTOVOLTAICPERFORMANCE:EQUIVALENTONE-DIODE'

def PhotovoltaicperformanceSandia(idf, **kwargs: Unpack[PhotovoltaicperformanceSandiaType]):
    """"helper for PhotovoltaicperformanceSandia"""
    return idf.newidfobject('PHOTOVOLTAICPERFORMANCE:SANDIA', **kwargs)
class PhotovoltaicperformanceSandiaMeta:
    idf_name = 'PHOTOVOLTAICPERFORMANCE:SANDIA'

def PhotovoltaicperformanceSimple(idf, **kwargs: Unpack[PhotovoltaicperformanceSimpleType]):
    """"helper for PhotovoltaicperformanceSimple"""
    return idf.newidfobject('PHOTOVOLTAICPERFORMANCE:SIMPLE', **kwargs)
class PhotovoltaicperformanceSimpleMeta:
    idf_name = 'PHOTOVOLTAICPERFORMANCE:SIMPLE'

def PipeAdiabatic(idf, **kwargs: Unpack[PipeAdiabaticType]):
    """"helper for PipeAdiabatic"""
    return idf.newidfobject('PIPE:ADIABATIC', **kwargs)
class PipeAdiabaticMeta:
    idf_name = 'PIPE:ADIABATIC'

def PipeAdiabaticSteam(idf, **kwargs: Unpack[PipeAdiabaticSteamType]):
    """"helper for PipeAdiabaticSteam"""
    return idf.newidfobject('PIPE:ADIABATIC:STEAM', **kwargs)
class PipeAdiabaticSteamMeta:
    idf_name = 'PIPE:ADIABATIC:STEAM'

def PipeIndoor(idf, **kwargs: Unpack[PipeIndoorType]):
    """"helper for PipeIndoor"""
    return idf.newidfobject('PIPE:INDOOR', **kwargs)
class PipeIndoorMeta:
    idf_name = 'PIPE:INDOOR'

def PipeOutdoor(idf, **kwargs: Unpack[PipeOutdoorType]):
    """"helper for PipeOutdoor"""
    return idf.newidfobject('PIPE:OUTDOOR', **kwargs)
class PipeOutdoorMeta:
    idf_name = 'PIPE:OUTDOOR'

def PipeUnderground(idf, **kwargs: Unpack[PipeUndergroundType]):
    """"helper for PipeUnderground"""
    return idf.newidfobject('PIPE:UNDERGROUND', **kwargs)
class PipeUndergroundMeta:
    idf_name = 'PIPE:UNDERGROUND'

def PipingsystemUndergroundDomain(idf, **kwargs: Unpack[PipingsystemUndergroundDomainType]):
    """"helper for PipingsystemUndergroundDomain"""
    return idf.newidfobject('PIPINGSYSTEM:UNDERGROUND:DOMAIN', **kwargs)
class PipingsystemUndergroundDomainMeta:
    idf_name = 'PIPINGSYSTEM:UNDERGROUND:DOMAIN'

def PipingsystemUndergroundPipecircuit(idf, **kwargs: Unpack[PipingsystemUndergroundPipecircuitType]):
    """"helper for PipingsystemUndergroundPipecircuit"""
    return idf.newidfobject('PIPINGSYSTEM:UNDERGROUND:PIPECIRCUIT', **kwargs)
class PipingsystemUndergroundPipecircuitMeta:
    idf_name = 'PIPINGSYSTEM:UNDERGROUND:PIPECIRCUIT'

def PipingsystemUndergroundPipesegment(idf, **kwargs: Unpack[PipingsystemUndergroundPipesegmentType]):
    """"helper for PipingsystemUndergroundPipesegment"""
    return idf.newidfobject('PIPINGSYSTEM:UNDERGROUND:PIPESEGMENT', **kwargs)
class PipingsystemUndergroundPipesegmentMeta:
    idf_name = 'PIPINGSYSTEM:UNDERGROUND:PIPESEGMENT'

def PlantcomponentTemperaturesource(idf, **kwargs: Unpack[PlantcomponentTemperaturesourceType]):
    """"helper for PlantcomponentTemperaturesource"""
    return idf.newidfobject('PLANTCOMPONENT:TEMPERATURESOURCE', **kwargs)
class PlantcomponentTemperaturesourceMeta:
    idf_name = 'PLANTCOMPONENT:TEMPERATURESOURCE'

def PlantcomponentUserdefined(idf, **kwargs: Unpack[PlantcomponentUserdefinedType]):
    """"helper for PlantcomponentUserdefined"""
    return idf.newidfobject('PLANTCOMPONENT:USERDEFINED', **kwargs)
class PlantcomponentUserdefinedMeta:
    idf_name = 'PLANTCOMPONENT:USERDEFINED'

def Plantequipmentlist(idf, **kwargs: Unpack[PlantequipmentlistType]):
    """"helper for Plantequipmentlist"""
    return idf.newidfobject('PLANTEQUIPMENTLIST', **kwargs)
class PlantequipmentlistMeta:
    idf_name = 'PLANTEQUIPMENTLIST'

def PlantequipmentoperationChillerheaterchangeover(idf, **kwargs: Unpack[PlantequipmentoperationChillerheaterchangeoverType]):
    """"helper for PlantequipmentoperationChillerheaterchangeover"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:CHILLERHEATERCHANGEOVER', **kwargs)
class PlantequipmentoperationChillerheaterchangeoverMeta:
    idf_name = 'PLANTEQUIPMENTOPERATION:CHILLERHEATERCHANGEOVER'

def PlantequipmentoperationComponentsetpoint(idf, **kwargs: Unpack[PlantequipmentoperationComponentsetpointType]):
    """"helper for PlantequipmentoperationComponentsetpoint"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:COMPONENTSETPOINT', **kwargs)
class PlantequipmentoperationComponentsetpointMeta:
    idf_name = 'PLANTEQUIPMENTOPERATION:COMPONENTSETPOINT'

def PlantequipmentoperationCoolingload(idf, **kwargs: Unpack[PlantequipmentoperationCoolingloadType]):
    """"helper for PlantequipmentoperationCoolingload"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:COOLINGLOAD', **kwargs)
class PlantequipmentoperationCoolingloadMeta:
    idf_name = 'PLANTEQUIPMENTOPERATION:COOLINGLOAD'

def PlantequipmentoperationHeatingload(idf, **kwargs: Unpack[PlantequipmentoperationHeatingloadType]):
    """"helper for PlantequipmentoperationHeatingload"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:HEATINGLOAD', **kwargs)
class PlantequipmentoperationHeatingloadMeta:
    idf_name = 'PLANTEQUIPMENTOPERATION:HEATINGLOAD'

def PlantequipmentoperationOutdoordewpoint(idf, **kwargs: Unpack[PlantequipmentoperationOutdoordewpointType]):
    """"helper for PlantequipmentoperationOutdoordewpoint"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORDEWPOINT', **kwargs)
class PlantequipmentoperationOutdoordewpointMeta:
    idf_name = 'PLANTEQUIPMENTOPERATION:OUTDOORDEWPOINT'

def PlantequipmentoperationOutdoordewpointdifference(idf, **kwargs: Unpack[PlantequipmentoperationOutdoordewpointdifferenceType]):
    """"helper for PlantequipmentoperationOutdoordewpointdifference"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORDEWPOINTDIFFERENCE', **kwargs)
class PlantequipmentoperationOutdoordewpointdifferenceMeta:
    idf_name = 'PLANTEQUIPMENTOPERATION:OUTDOORDEWPOINTDIFFERENCE'

def PlantequipmentoperationOutdoordrybulb(idf, **kwargs: Unpack[PlantequipmentoperationOutdoordrybulbType]):
    """"helper for PlantequipmentoperationOutdoordrybulb"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORDRYBULB', **kwargs)
class PlantequipmentoperationOutdoordrybulbMeta:
    idf_name = 'PLANTEQUIPMENTOPERATION:OUTDOORDRYBULB'

def PlantequipmentoperationOutdoordrybulbdifference(idf, **kwargs: Unpack[PlantequipmentoperationOutdoordrybulbdifferenceType]):
    """"helper for PlantequipmentoperationOutdoordrybulbdifference"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORDRYBULBDIFFERENCE', **kwargs)
class PlantequipmentoperationOutdoordrybulbdifferenceMeta:
    idf_name = 'PLANTEQUIPMENTOPERATION:OUTDOORDRYBULBDIFFERENCE'

def PlantequipmentoperationOutdoorrelativehumidity(idf, **kwargs: Unpack[PlantequipmentoperationOutdoorrelativehumidityType]):
    """"helper for PlantequipmentoperationOutdoorrelativehumidity"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORRELATIVEHUMIDITY', **kwargs)
class PlantequipmentoperationOutdoorrelativehumidityMeta:
    idf_name = 'PLANTEQUIPMENTOPERATION:OUTDOORRELATIVEHUMIDITY'

def PlantequipmentoperationOutdoorwetbulb(idf, **kwargs: Unpack[PlantequipmentoperationOutdoorwetbulbType]):
    """"helper for PlantequipmentoperationOutdoorwetbulb"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORWETBULB', **kwargs)
class PlantequipmentoperationOutdoorwetbulbMeta:
    idf_name = 'PLANTEQUIPMENTOPERATION:OUTDOORWETBULB'

def PlantequipmentoperationOutdoorwetbulbdifference(idf, **kwargs: Unpack[PlantequipmentoperationOutdoorwetbulbdifferenceType]):
    """"helper for PlantequipmentoperationOutdoorwetbulbdifference"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORWETBULBDIFFERENCE', **kwargs)
class PlantequipmentoperationOutdoorwetbulbdifferenceMeta:
    idf_name = 'PLANTEQUIPMENTOPERATION:OUTDOORWETBULBDIFFERENCE'

def PlantequipmentoperationThermalenergystorage(idf, **kwargs: Unpack[PlantequipmentoperationThermalenergystorageType]):
    """"helper for PlantequipmentoperationThermalenergystorage"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:THERMALENERGYSTORAGE', **kwargs)
class PlantequipmentoperationThermalenergystorageMeta:
    idf_name = 'PLANTEQUIPMENTOPERATION:THERMALENERGYSTORAGE'

def PlantequipmentoperationUncontrolled(idf, **kwargs: Unpack[PlantequipmentoperationUncontrolledType]):
    """"helper for PlantequipmentoperationUncontrolled"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:UNCONTROLLED', **kwargs)
class PlantequipmentoperationUncontrolledMeta:
    idf_name = 'PLANTEQUIPMENTOPERATION:UNCONTROLLED'

def PlantequipmentoperationUserdefined(idf, **kwargs: Unpack[PlantequipmentoperationUserdefinedType]):
    """"helper for PlantequipmentoperationUserdefined"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:USERDEFINED', **kwargs)
class PlantequipmentoperationUserdefinedMeta:
    idf_name = 'PLANTEQUIPMENTOPERATION:USERDEFINED'

def Plantequipmentoperationschemes(idf, **kwargs: Unpack[PlantequipmentoperationschemesType]):
    """"helper for Plantequipmentoperationschemes"""
    return idf.newidfobject('PLANTEQUIPMENTOPERATIONSCHEMES', **kwargs)
class PlantequipmentoperationschemesMeta:
    idf_name = 'PLANTEQUIPMENTOPERATIONSCHEMES'

def Plantloop(idf, **kwargs: Unpack[PlantloopType]):
    """"helper for Plantloop"""
    return idf.newidfobject('PLANTLOOP', **kwargs)
class PlantloopMeta:
    idf_name = 'PLANTLOOP'

def PumpConstantspeed(idf, **kwargs: Unpack[PumpConstantspeedType]):
    """"helper for PumpConstantspeed"""
    return idf.newidfobject('PUMP:CONSTANTSPEED', **kwargs)
class PumpConstantspeedMeta:
    idf_name = 'PUMP:CONSTANTSPEED'

def PumpVariablespeed(idf, **kwargs: Unpack[PumpVariablespeedType]):
    """"helper for PumpVariablespeed"""
    return idf.newidfobject('PUMP:VARIABLESPEED', **kwargs)
class PumpVariablespeedMeta:
    idf_name = 'PUMP:VARIABLESPEED'

def PumpVariablespeedCondensate(idf, **kwargs: Unpack[PumpVariablespeedCondensateType]):
    """"helper for PumpVariablespeedCondensate"""
    return idf.newidfobject('PUMP:VARIABLESPEED:CONDENSATE', **kwargs)
class PumpVariablespeedCondensateMeta:
    idf_name = 'PUMP:VARIABLESPEED:CONDENSATE'

def PythonpluginInstance(idf, **kwargs: Unpack[PythonpluginInstanceType]):
    """"helper for PythonpluginInstance"""
    return idf.newidfobject('PYTHONPLUGIN:INSTANCE', **kwargs)
class PythonpluginInstanceMeta:
    idf_name = 'PYTHONPLUGIN:INSTANCE'

def PythonpluginOutputvariable(idf, **kwargs: Unpack[PythonpluginOutputvariableType]):
    """"helper for PythonpluginOutputvariable"""
    return idf.newidfobject('PYTHONPLUGIN:OUTPUTVARIABLE', **kwargs)
class PythonpluginOutputvariableMeta:
    idf_name = 'PYTHONPLUGIN:OUTPUTVARIABLE'

def PythonpluginSearchpaths(idf, **kwargs: Unpack[PythonpluginSearchpathsType]):
    """"helper for PythonpluginSearchpaths"""
    return idf.newidfobject('PYTHONPLUGIN:SEARCHPATHS', **kwargs)
class PythonpluginSearchpathsMeta:
    idf_name = 'PYTHONPLUGIN:SEARCHPATHS'

def PythonpluginTrendvariable(idf, **kwargs: Unpack[PythonpluginTrendvariableType]):
    """"helper for PythonpluginTrendvariable"""
    return idf.newidfobject('PYTHONPLUGIN:TRENDVARIABLE', **kwargs)
class PythonpluginTrendvariableMeta:
    idf_name = 'PYTHONPLUGIN:TRENDVARIABLE'

def PythonpluginVariables(idf, **kwargs: Unpack[PythonpluginVariablesType]):
    """"helper for PythonpluginVariables"""
    return idf.newidfobject('PYTHONPLUGIN:VARIABLES', **kwargs)
class PythonpluginVariablesMeta:
    idf_name = 'PYTHONPLUGIN:VARIABLES'

def RefrigerationAirchiller(idf, **kwargs: Unpack[RefrigerationAirchillerType]):
    """"helper for RefrigerationAirchiller"""
    return idf.newidfobject('REFRIGERATION:AIRCHILLER', **kwargs)
class RefrigerationAirchillerMeta:
    idf_name = 'REFRIGERATION:AIRCHILLER'

def RefrigerationCase(idf, **kwargs: Unpack[RefrigerationCaseType]):
    """"helper for RefrigerationCase"""
    return idf.newidfobject('REFRIGERATION:CASE', **kwargs)
class RefrigerationCaseMeta:
    idf_name = 'REFRIGERATION:CASE'

def RefrigerationCaseandwalkinlist(idf, **kwargs: Unpack[RefrigerationCaseandwalkinlistType]):
    """"helper for RefrigerationCaseandwalkinlist"""
    return idf.newidfobject('REFRIGERATION:CASEANDWALKINLIST', **kwargs)
class RefrigerationCaseandwalkinlistMeta:
    idf_name = 'REFRIGERATION:CASEANDWALKINLIST'

def RefrigerationCompressor(idf, **kwargs: Unpack[RefrigerationCompressorType]):
    """"helper for RefrigerationCompressor"""
    return idf.newidfobject('REFRIGERATION:COMPRESSOR', **kwargs)
class RefrigerationCompressorMeta:
    idf_name = 'REFRIGERATION:COMPRESSOR'

def RefrigerationCompressorlist(idf, **kwargs: Unpack[RefrigerationCompressorlistType]):
    """"helper for RefrigerationCompressorlist"""
    return idf.newidfobject('REFRIGERATION:COMPRESSORLIST', **kwargs)
class RefrigerationCompressorlistMeta:
    idf_name = 'REFRIGERATION:COMPRESSORLIST'

def RefrigerationCompressorrack(idf, **kwargs: Unpack[RefrigerationCompressorrackType]):
    """"helper for RefrigerationCompressorrack"""
    return idf.newidfobject('REFRIGERATION:COMPRESSORRACK', **kwargs)
class RefrigerationCompressorrackMeta:
    idf_name = 'REFRIGERATION:COMPRESSORRACK'

def RefrigerationCondenserAircooled(idf, **kwargs: Unpack[RefrigerationCondenserAircooledType]):
    """"helper for RefrigerationCondenserAircooled"""
    return idf.newidfobject('REFRIGERATION:CONDENSER:AIRCOOLED', **kwargs)
class RefrigerationCondenserAircooledMeta:
    idf_name = 'REFRIGERATION:CONDENSER:AIRCOOLED'

def RefrigerationCondenserCascade(idf, **kwargs: Unpack[RefrigerationCondenserCascadeType]):
    """"helper for RefrigerationCondenserCascade"""
    return idf.newidfobject('REFRIGERATION:CONDENSER:CASCADE', **kwargs)
class RefrigerationCondenserCascadeMeta:
    idf_name = 'REFRIGERATION:CONDENSER:CASCADE'

def RefrigerationCondenserEvaporativecooled(idf, **kwargs: Unpack[RefrigerationCondenserEvaporativecooledType]):
    """"helper for RefrigerationCondenserEvaporativecooled"""
    return idf.newidfobject('REFRIGERATION:CONDENSER:EVAPORATIVECOOLED', **kwargs)
class RefrigerationCondenserEvaporativecooledMeta:
    idf_name = 'REFRIGERATION:CONDENSER:EVAPORATIVECOOLED'

def RefrigerationCondenserWatercooled(idf, **kwargs: Unpack[RefrigerationCondenserWatercooledType]):
    """"helper for RefrigerationCondenserWatercooled"""
    return idf.newidfobject('REFRIGERATION:CONDENSER:WATERCOOLED', **kwargs)
class RefrigerationCondenserWatercooledMeta:
    idf_name = 'REFRIGERATION:CONDENSER:WATERCOOLED'

def RefrigerationGascoolerAircooled(idf, **kwargs: Unpack[RefrigerationGascoolerAircooledType]):
    """"helper for RefrigerationGascoolerAircooled"""
    return idf.newidfobject('REFRIGERATION:GASCOOLER:AIRCOOLED', **kwargs)
class RefrigerationGascoolerAircooledMeta:
    idf_name = 'REFRIGERATION:GASCOOLER:AIRCOOLED'

def RefrigerationSecondarysystem(idf, **kwargs: Unpack[RefrigerationSecondarysystemType]):
    """"helper for RefrigerationSecondarysystem"""
    return idf.newidfobject('REFRIGERATION:SECONDARYSYSTEM', **kwargs)
class RefrigerationSecondarysystemMeta:
    idf_name = 'REFRIGERATION:SECONDARYSYSTEM'

def RefrigerationSubcooler(idf, **kwargs: Unpack[RefrigerationSubcoolerType]):
    """"helper for RefrigerationSubcooler"""
    return idf.newidfobject('REFRIGERATION:SUBCOOLER', **kwargs)
class RefrigerationSubcoolerMeta:
    idf_name = 'REFRIGERATION:SUBCOOLER'

def RefrigerationSystem(idf, **kwargs: Unpack[RefrigerationSystemType]):
    """"helper for RefrigerationSystem"""
    return idf.newidfobject('REFRIGERATION:SYSTEM', **kwargs)
class RefrigerationSystemMeta:
    idf_name = 'REFRIGERATION:SYSTEM'

def RefrigerationTranscriticalsystem(idf, **kwargs: Unpack[RefrigerationTranscriticalsystemType]):
    """"helper for RefrigerationTranscriticalsystem"""
    return idf.newidfobject('REFRIGERATION:TRANSCRITICALSYSTEM', **kwargs)
class RefrigerationTranscriticalsystemMeta:
    idf_name = 'REFRIGERATION:TRANSCRITICALSYSTEM'

def RefrigerationTransferloadlist(idf, **kwargs: Unpack[RefrigerationTransferloadlistType]):
    """"helper for RefrigerationTransferloadlist"""
    return idf.newidfobject('REFRIGERATION:TRANSFERLOADLIST', **kwargs)
class RefrigerationTransferloadlistMeta:
    idf_name = 'REFRIGERATION:TRANSFERLOADLIST'

def RefrigerationWalkin(idf, **kwargs: Unpack[RefrigerationWalkinType]):
    """"helper for RefrigerationWalkin"""
    return idf.newidfobject('REFRIGERATION:WALKIN', **kwargs)
class RefrigerationWalkinMeta:
    idf_name = 'REFRIGERATION:WALKIN'

def Roof(idf, **kwargs: Unpack[RoofType]):
    """"helper for Roof"""
    return idf.newidfobject('ROOF', **kwargs)
class RoofMeta:
    idf_name = 'ROOF'

def RoofceilingDetailed(idf, **kwargs: Unpack[RoofceilingDetailedType]):
    """"helper for RoofceilingDetailed"""
    return idf.newidfobject('ROOFCEILING:DETAILED', **kwargs)
class RoofceilingDetailedMeta:
    idf_name = 'ROOFCEILING:DETAILED'

def Roofirrigation(idf, **kwargs: Unpack[RoofirrigationType]):
    """"helper for Roofirrigation"""
    return idf.newidfobject('ROOFIRRIGATION', **kwargs)
class RoofirrigationMeta:
    idf_name = 'ROOFIRRIGATION'

def RoomairNode(idf, **kwargs: Unpack[RoomairNodeType]):
    """"helper for RoomairNode"""
    return idf.newidfobject('ROOMAIR:NODE', **kwargs)
class RoomairNodeMeta:
    idf_name = 'ROOMAIR:NODE'

def RoomairNodeAirflownetwork(idf, **kwargs: Unpack[RoomairNodeAirflownetworkType]):
    """"helper for RoomairNodeAirflownetwork"""
    return idf.newidfobject('ROOMAIR:NODE:AIRFLOWNETWORK', **kwargs)
class RoomairNodeAirflownetworkMeta:
    idf_name = 'ROOMAIR:NODE:AIRFLOWNETWORK'

def RoomairNodeAirflownetworkAdjacentsurfacelist(idf, **kwargs: Unpack[RoomairNodeAirflownetworkAdjacentsurfacelistType]):
    """"helper for RoomairNodeAirflownetworkAdjacentsurfacelist"""
    return idf.newidfobject('ROOMAIR:NODE:AIRFLOWNETWORK:ADJACENTSURFACELIST', **kwargs)
class RoomairNodeAirflownetworkAdjacentsurfacelistMeta:
    idf_name = 'ROOMAIR:NODE:AIRFLOWNETWORK:ADJACENTSURFACELIST'

def RoomairNodeAirflownetworkHvacequipment(idf, **kwargs: Unpack[RoomairNodeAirflownetworkHvacequipmentType]):
    """"helper for RoomairNodeAirflownetworkHvacequipment"""
    return idf.newidfobject('ROOMAIR:NODE:AIRFLOWNETWORK:HVACEQUIPMENT', **kwargs)
class RoomairNodeAirflownetworkHvacequipmentMeta:
    idf_name = 'ROOMAIR:NODE:AIRFLOWNETWORK:HVACEQUIPMENT'

def RoomairNodeAirflownetworkInternalgains(idf, **kwargs: Unpack[RoomairNodeAirflownetworkInternalgainsType]):
    """"helper for RoomairNodeAirflownetworkInternalgains"""
    return idf.newidfobject('ROOMAIR:NODE:AIRFLOWNETWORK:INTERNALGAINS', **kwargs)
class RoomairNodeAirflownetworkInternalgainsMeta:
    idf_name = 'ROOMAIR:NODE:AIRFLOWNETWORK:INTERNALGAINS'

def RoomairTemperaturepatternConstantgradient(idf, **kwargs: Unpack[RoomairTemperaturepatternConstantgradientType]):
    """"helper for RoomairTemperaturepatternConstantgradient"""
    return idf.newidfobject('ROOMAIR:TEMPERATUREPATTERN:CONSTANTGRADIENT', **kwargs)
class RoomairTemperaturepatternConstantgradientMeta:
    idf_name = 'ROOMAIR:TEMPERATUREPATTERN:CONSTANTGRADIENT'

def RoomairTemperaturepatternNondimensionalheight(idf, **kwargs: Unpack[RoomairTemperaturepatternNondimensionalheightType]):
    """"helper for RoomairTemperaturepatternNondimensionalheight"""
    return idf.newidfobject('ROOMAIR:TEMPERATUREPATTERN:NONDIMENSIONALHEIGHT', **kwargs)
class RoomairTemperaturepatternNondimensionalheightMeta:
    idf_name = 'ROOMAIR:TEMPERATUREPATTERN:NONDIMENSIONALHEIGHT'

def RoomairTemperaturepatternSurfacemapping(idf, **kwargs: Unpack[RoomairTemperaturepatternSurfacemappingType]):
    """"helper for RoomairTemperaturepatternSurfacemapping"""
    return idf.newidfobject('ROOMAIR:TEMPERATUREPATTERN:SURFACEMAPPING', **kwargs)
class RoomairTemperaturepatternSurfacemappingMeta:
    idf_name = 'ROOMAIR:TEMPERATUREPATTERN:SURFACEMAPPING'

def RoomairTemperaturepatternTwogradient(idf, **kwargs: Unpack[RoomairTemperaturepatternTwogradientType]):
    """"helper for RoomairTemperaturepatternTwogradient"""
    return idf.newidfobject('ROOMAIR:TEMPERATUREPATTERN:TWOGRADIENT', **kwargs)
class RoomairTemperaturepatternTwogradientMeta:
    idf_name = 'ROOMAIR:TEMPERATUREPATTERN:TWOGRADIENT'

def RoomairTemperaturepatternUserdefined(idf, **kwargs: Unpack[RoomairTemperaturepatternUserdefinedType]):
    """"helper for RoomairTemperaturepatternUserdefined"""
    return idf.newidfobject('ROOMAIR:TEMPERATUREPATTERN:USERDEFINED', **kwargs)
class RoomairTemperaturepatternUserdefinedMeta:
    idf_name = 'ROOMAIR:TEMPERATUREPATTERN:USERDEFINED'

def Roomairmodeltype(idf, **kwargs: Unpack[RoomairmodeltypeType]):
    """"helper for Roomairmodeltype"""
    return idf.newidfobject('ROOMAIRMODELTYPE', **kwargs)
class RoomairmodeltypeMeta:
    idf_name = 'ROOMAIRMODELTYPE'

def RoomairsettingsAirflownetwork(idf, **kwargs: Unpack[RoomairsettingsAirflownetworkType]):
    """"helper for RoomairsettingsAirflownetwork"""
    return idf.newidfobject('ROOMAIRSETTINGS:AIRFLOWNETWORK', **kwargs)
class RoomairsettingsAirflownetworkMeta:
    idf_name = 'ROOMAIRSETTINGS:AIRFLOWNETWORK'

def RoomairsettingsCrossventilation(idf, **kwargs: Unpack[RoomairsettingsCrossventilationType]):
    """"helper for RoomairsettingsCrossventilation"""
    return idf.newidfobject('ROOMAIRSETTINGS:CROSSVENTILATION', **kwargs)
class RoomairsettingsCrossventilationMeta:
    idf_name = 'ROOMAIRSETTINGS:CROSSVENTILATION'

def RoomairsettingsOnenodedisplacementventilation(idf, **kwargs: Unpack[RoomairsettingsOnenodedisplacementventilationType]):
    """"helper for RoomairsettingsOnenodedisplacementventilation"""
    return idf.newidfobject('ROOMAIRSETTINGS:ONENODEDISPLACEMENTVENTILATION', **kwargs)
class RoomairsettingsOnenodedisplacementventilationMeta:
    idf_name = 'ROOMAIRSETTINGS:ONENODEDISPLACEMENTVENTILATION'

def RoomairsettingsThreenodedisplacementventilation(idf, **kwargs: Unpack[RoomairsettingsThreenodedisplacementventilationType]):
    """"helper for RoomairsettingsThreenodedisplacementventilation"""
    return idf.newidfobject('ROOMAIRSETTINGS:THREENODEDISPLACEMENTVENTILATION', **kwargs)
class RoomairsettingsThreenodedisplacementventilationMeta:
    idf_name = 'ROOMAIRSETTINGS:THREENODEDISPLACEMENTVENTILATION'

def RoomairsettingsUnderfloorairdistributionexterior(idf, **kwargs: Unpack[RoomairsettingsUnderfloorairdistributionexteriorType]):
    """"helper for RoomairsettingsUnderfloorairdistributionexterior"""
    return idf.newidfobject('ROOMAIRSETTINGS:UNDERFLOORAIRDISTRIBUTIONEXTERIOR', **kwargs)
class RoomairsettingsUnderfloorairdistributionexteriorMeta:
    idf_name = 'ROOMAIRSETTINGS:UNDERFLOORAIRDISTRIBUTIONEXTERIOR'

def RoomairsettingsUnderfloorairdistributioninterior(idf, **kwargs: Unpack[RoomairsettingsUnderfloorairdistributioninteriorType]):
    """"helper for RoomairsettingsUnderfloorairdistributioninterior"""
    return idf.newidfobject('ROOMAIRSETTINGS:UNDERFLOORAIRDISTRIBUTIONINTERIOR', **kwargs)
class RoomairsettingsUnderfloorairdistributioninteriorMeta:
    idf_name = 'ROOMAIRSETTINGS:UNDERFLOORAIRDISTRIBUTIONINTERIOR'

def Runperiod(idf, **kwargs: Unpack[RunperiodType]):
    """"helper for Runperiod"""
    return idf.newidfobject('RUNPERIOD', **kwargs)
class RunperiodMeta:
    idf_name = 'RUNPERIOD'

def RunperiodcontrolDaylightsavingtime(idf, **kwargs: Unpack[RunperiodcontrolDaylightsavingtimeType]):
    """"helper for RunperiodcontrolDaylightsavingtime"""
    return idf.newidfobject('RUNPERIODCONTROL:DAYLIGHTSAVINGTIME', **kwargs)
class RunperiodcontrolDaylightsavingtimeMeta:
    idf_name = 'RUNPERIODCONTROL:DAYLIGHTSAVINGTIME'

def RunperiodcontrolSpecialdays(idf, **kwargs: Unpack[RunperiodcontrolSpecialdaysType]):
    """"helper for RunperiodcontrolSpecialdays"""
    return idf.newidfobject('RUNPERIODCONTROL:SPECIALDAYS', **kwargs)
class RunperiodcontrolSpecialdaysMeta:
    idf_name = 'RUNPERIODCONTROL:SPECIALDAYS'

def ScheduleCompact(idf, **kwargs: Unpack[ScheduleCompactType]):
    """"helper for ScheduleCompact"""
    return idf.newidfobject('SCHEDULE:COMPACT', **kwargs)
class ScheduleCompactMeta:
    idf_name = 'SCHEDULE:COMPACT'

def ScheduleConstant(idf, **kwargs: Unpack[ScheduleConstantType]):
    """"helper for ScheduleConstant"""
    return idf.newidfobject('SCHEDULE:CONSTANT', **kwargs)
class ScheduleConstantMeta:
    idf_name = 'SCHEDULE:CONSTANT'

def ScheduleDayHourly(idf, **kwargs: Unpack[ScheduleDayHourlyType]):
    """"helper for ScheduleDayHourly"""
    return idf.newidfobject('SCHEDULE:DAY:HOURLY', **kwargs)
class ScheduleDayHourlyMeta:
    idf_name = 'SCHEDULE:DAY:HOURLY'

def ScheduleDayInterval(idf, **kwargs: Unpack[ScheduleDayIntervalType]):
    """"helper for ScheduleDayInterval"""
    return idf.newidfobject('SCHEDULE:DAY:INTERVAL', **kwargs)
class ScheduleDayIntervalMeta:
    idf_name = 'SCHEDULE:DAY:INTERVAL'

def ScheduleDayList(idf, **kwargs: Unpack[ScheduleDayListType]):
    """"helper for ScheduleDayList"""
    return idf.newidfobject('SCHEDULE:DAY:LIST', **kwargs)
class ScheduleDayListMeta:
    idf_name = 'SCHEDULE:DAY:LIST'

def ScheduleFile(idf, **kwargs: Unpack[ScheduleFileType]):
    """"helper for ScheduleFile"""
    return idf.newidfobject('SCHEDULE:FILE', **kwargs)
class ScheduleFileMeta:
    idf_name = 'SCHEDULE:FILE'

def ScheduleFileShading(idf, **kwargs: Unpack[ScheduleFileShadingType]):
    """"helper for ScheduleFileShading"""
    return idf.newidfobject('SCHEDULE:FILE:SHADING', **kwargs)
class ScheduleFileShadingMeta:
    idf_name = 'SCHEDULE:FILE:SHADING'

def ScheduleWeekCompact(idf, **kwargs: Unpack[ScheduleWeekCompactType]):
    """"helper for ScheduleWeekCompact"""
    return idf.newidfobject('SCHEDULE:WEEK:COMPACT', **kwargs)
class ScheduleWeekCompactMeta:
    idf_name = 'SCHEDULE:WEEK:COMPACT'

def ScheduleWeekDaily(idf, **kwargs: Unpack[ScheduleWeekDailyType]):
    """"helper for ScheduleWeekDaily"""
    return idf.newidfobject('SCHEDULE:WEEK:DAILY', **kwargs)
class ScheduleWeekDailyMeta:
    idf_name = 'SCHEDULE:WEEK:DAILY'

def ScheduleYear(idf, **kwargs: Unpack[ScheduleYearType]):
    """"helper for ScheduleYear"""
    return idf.newidfobject('SCHEDULE:YEAR', **kwargs)
class ScheduleYearMeta:
    idf_name = 'SCHEDULE:YEAR'

def Scheduletypelimits(idf, **kwargs: Unpack[ScheduletypelimitsType]):
    """"helper for Scheduletypelimits"""
    return idf.newidfobject('SCHEDULETYPELIMITS', **kwargs)
class ScheduletypelimitsMeta:
    idf_name = 'SCHEDULETYPELIMITS'

def SetpointmanagerColdest(idf, **kwargs: Unpack[SetpointmanagerColdestType]):
    """"helper for SetpointmanagerColdest"""
    return idf.newidfobject('SETPOINTMANAGER:COLDEST', **kwargs)
class SetpointmanagerColdestMeta:
    idf_name = 'SETPOINTMANAGER:COLDEST'

def SetpointmanagerCondenserenteringreset(idf, **kwargs: Unpack[SetpointmanagerCondenserenteringresetType]):
    """"helper for SetpointmanagerCondenserenteringreset"""
    return idf.newidfobject('SETPOINTMANAGER:CONDENSERENTERINGRESET', **kwargs)
class SetpointmanagerCondenserenteringresetMeta:
    idf_name = 'SETPOINTMANAGER:CONDENSERENTERINGRESET'

def SetpointmanagerCondenserenteringresetIdeal(idf, **kwargs: Unpack[SetpointmanagerCondenserenteringresetIdealType]):
    """"helper for SetpointmanagerCondenserenteringresetIdeal"""
    return idf.newidfobject('SETPOINTMANAGER:CONDENSERENTERINGRESET:IDEAL', **kwargs)
class SetpointmanagerCondenserenteringresetIdealMeta:
    idf_name = 'SETPOINTMANAGER:CONDENSERENTERINGRESET:IDEAL'

def SetpointmanagerFollowgroundtemperature(idf, **kwargs: Unpack[SetpointmanagerFollowgroundtemperatureType]):
    """"helper for SetpointmanagerFollowgroundtemperature"""
    return idf.newidfobject('SETPOINTMANAGER:FOLLOWGROUNDTEMPERATURE', **kwargs)
class SetpointmanagerFollowgroundtemperatureMeta:
    idf_name = 'SETPOINTMANAGER:FOLLOWGROUNDTEMPERATURE'

def SetpointmanagerFollowoutdoorairtemperature(idf, **kwargs: Unpack[SetpointmanagerFollowoutdoorairtemperatureType]):
    """"helper for SetpointmanagerFollowoutdoorairtemperature"""
    return idf.newidfobject('SETPOINTMANAGER:FOLLOWOUTDOORAIRTEMPERATURE', **kwargs)
class SetpointmanagerFollowoutdoorairtemperatureMeta:
    idf_name = 'SETPOINTMANAGER:FOLLOWOUTDOORAIRTEMPERATURE'

def SetpointmanagerFollowsystemnodetemperature(idf, **kwargs: Unpack[SetpointmanagerFollowsystemnodetemperatureType]):
    """"helper for SetpointmanagerFollowsystemnodetemperature"""
    return idf.newidfobject('SETPOINTMANAGER:FOLLOWSYSTEMNODETEMPERATURE', **kwargs)
class SetpointmanagerFollowsystemnodetemperatureMeta:
    idf_name = 'SETPOINTMANAGER:FOLLOWSYSTEMNODETEMPERATURE'

def SetpointmanagerMixedair(idf, **kwargs: Unpack[SetpointmanagerMixedairType]):
    """"helper for SetpointmanagerMixedair"""
    return idf.newidfobject('SETPOINTMANAGER:MIXEDAIR', **kwargs)
class SetpointmanagerMixedairMeta:
    idf_name = 'SETPOINTMANAGER:MIXEDAIR'

def SetpointmanagerMultizoneCoolingAverage(idf, **kwargs: Unpack[SetpointmanagerMultizoneCoolingAverageType]):
    """"helper for SetpointmanagerMultizoneCoolingAverage"""
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:COOLING:AVERAGE', **kwargs)
class SetpointmanagerMultizoneCoolingAverageMeta:
    idf_name = 'SETPOINTMANAGER:MULTIZONE:COOLING:AVERAGE'

def SetpointmanagerMultizoneHeatingAverage(idf, **kwargs: Unpack[SetpointmanagerMultizoneHeatingAverageType]):
    """"helper for SetpointmanagerMultizoneHeatingAverage"""
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:HEATING:AVERAGE', **kwargs)
class SetpointmanagerMultizoneHeatingAverageMeta:
    idf_name = 'SETPOINTMANAGER:MULTIZONE:HEATING:AVERAGE'

def SetpointmanagerMultizoneHumidityMaximum(idf, **kwargs: Unpack[SetpointmanagerMultizoneHumidityMaximumType]):
    """"helper for SetpointmanagerMultizoneHumidityMaximum"""
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:HUMIDITY:MAXIMUM', **kwargs)
class SetpointmanagerMultizoneHumidityMaximumMeta:
    idf_name = 'SETPOINTMANAGER:MULTIZONE:HUMIDITY:MAXIMUM'

def SetpointmanagerMultizoneHumidityMinimum(idf, **kwargs: Unpack[SetpointmanagerMultizoneHumidityMinimumType]):
    """"helper for SetpointmanagerMultizoneHumidityMinimum"""
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:HUMIDITY:MINIMUM', **kwargs)
class SetpointmanagerMultizoneHumidityMinimumMeta:
    idf_name = 'SETPOINTMANAGER:MULTIZONE:HUMIDITY:MINIMUM'

def SetpointmanagerMultizoneMaximumhumidityAverage(idf, **kwargs: Unpack[SetpointmanagerMultizoneMaximumhumidityAverageType]):
    """"helper for SetpointmanagerMultizoneMaximumhumidityAverage"""
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:MAXIMUMHUMIDITY:AVERAGE', **kwargs)
class SetpointmanagerMultizoneMaximumhumidityAverageMeta:
    idf_name = 'SETPOINTMANAGER:MULTIZONE:MAXIMUMHUMIDITY:AVERAGE'

def SetpointmanagerMultizoneMinimumhumidityAverage(idf, **kwargs: Unpack[SetpointmanagerMultizoneMinimumhumidityAverageType]):
    """"helper for SetpointmanagerMultizoneMinimumhumidityAverage"""
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:MINIMUMHUMIDITY:AVERAGE', **kwargs)
class SetpointmanagerMultizoneMinimumhumidityAverageMeta:
    idf_name = 'SETPOINTMANAGER:MULTIZONE:MINIMUMHUMIDITY:AVERAGE'

def SetpointmanagerOutdoorairpretreat(idf, **kwargs: Unpack[SetpointmanagerOutdoorairpretreatType]):
    """"helper for SetpointmanagerOutdoorairpretreat"""
    return idf.newidfobject('SETPOINTMANAGER:OUTDOORAIRPRETREAT', **kwargs)
class SetpointmanagerOutdoorairpretreatMeta:
    idf_name = 'SETPOINTMANAGER:OUTDOORAIRPRETREAT'

def SetpointmanagerOutdoorairreset(idf, **kwargs: Unpack[SetpointmanagerOutdoorairresetType]):
    """"helper for SetpointmanagerOutdoorairreset"""
    return idf.newidfobject('SETPOINTMANAGER:OUTDOORAIRRESET', **kwargs)
class SetpointmanagerOutdoorairresetMeta:
    idf_name = 'SETPOINTMANAGER:OUTDOORAIRRESET'

def SetpointmanagerReturnairbypassflow(idf, **kwargs: Unpack[SetpointmanagerReturnairbypassflowType]):
    """"helper for SetpointmanagerReturnairbypassflow"""
    return idf.newidfobject('SETPOINTMANAGER:RETURNAIRBYPASSFLOW', **kwargs)
class SetpointmanagerReturnairbypassflowMeta:
    idf_name = 'SETPOINTMANAGER:RETURNAIRBYPASSFLOW'

def SetpointmanagerReturntemperatureChilledwater(idf, **kwargs: Unpack[SetpointmanagerReturntemperatureChilledwaterType]):
    """"helper for SetpointmanagerReturntemperatureChilledwater"""
    return idf.newidfobject('SETPOINTMANAGER:RETURNTEMPERATURE:CHILLEDWATER', **kwargs)
class SetpointmanagerReturntemperatureChilledwaterMeta:
    idf_name = 'SETPOINTMANAGER:RETURNTEMPERATURE:CHILLEDWATER'

def SetpointmanagerReturntemperatureHotwater(idf, **kwargs: Unpack[SetpointmanagerReturntemperatureHotwaterType]):
    """"helper for SetpointmanagerReturntemperatureHotwater"""
    return idf.newidfobject('SETPOINTMANAGER:RETURNTEMPERATURE:HOTWATER', **kwargs)
class SetpointmanagerReturntemperatureHotwaterMeta:
    idf_name = 'SETPOINTMANAGER:RETURNTEMPERATURE:HOTWATER'

def SetpointmanagerScheduled(idf, **kwargs: Unpack[SetpointmanagerScheduledType]):
    """"helper for SetpointmanagerScheduled"""
    return idf.newidfobject('SETPOINTMANAGER:SCHEDULED', **kwargs)
class SetpointmanagerScheduledMeta:
    idf_name = 'SETPOINTMANAGER:SCHEDULED'

def SetpointmanagerScheduledDualsetpoint(idf, **kwargs: Unpack[SetpointmanagerScheduledDualsetpointType]):
    """"helper for SetpointmanagerScheduledDualsetpoint"""
    return idf.newidfobject('SETPOINTMANAGER:SCHEDULED:DUALSETPOINT', **kwargs)
class SetpointmanagerScheduledDualsetpointMeta:
    idf_name = 'SETPOINTMANAGER:SCHEDULED:DUALSETPOINT'

def SetpointmanagerSinglezoneCooling(idf, **kwargs: Unpack[SetpointmanagerSinglezoneCoolingType]):
    """"helper for SetpointmanagerSinglezoneCooling"""
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:COOLING', **kwargs)
class SetpointmanagerSinglezoneCoolingMeta:
    idf_name = 'SETPOINTMANAGER:SINGLEZONE:COOLING'

def SetpointmanagerSinglezoneHeating(idf, **kwargs: Unpack[SetpointmanagerSinglezoneHeatingType]):
    """"helper for SetpointmanagerSinglezoneHeating"""
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:HEATING', **kwargs)
class SetpointmanagerSinglezoneHeatingMeta:
    idf_name = 'SETPOINTMANAGER:SINGLEZONE:HEATING'

def SetpointmanagerSinglezoneHumidityMaximum(idf, **kwargs: Unpack[SetpointmanagerSinglezoneHumidityMaximumType]):
    """"helper for SetpointmanagerSinglezoneHumidityMaximum"""
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:HUMIDITY:MAXIMUM', **kwargs)
class SetpointmanagerSinglezoneHumidityMaximumMeta:
    idf_name = 'SETPOINTMANAGER:SINGLEZONE:HUMIDITY:MAXIMUM'

def SetpointmanagerSinglezoneHumidityMinimum(idf, **kwargs: Unpack[SetpointmanagerSinglezoneHumidityMinimumType]):
    """"helper for SetpointmanagerSinglezoneHumidityMinimum"""
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:HUMIDITY:MINIMUM', **kwargs)
class SetpointmanagerSinglezoneHumidityMinimumMeta:
    idf_name = 'SETPOINTMANAGER:SINGLEZONE:HUMIDITY:MINIMUM'

def SetpointmanagerSinglezoneOnestagecooling(idf, **kwargs: Unpack[SetpointmanagerSinglezoneOnestagecoolingType]):
    """"helper for SetpointmanagerSinglezoneOnestagecooling"""
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:ONESTAGECOOLING', **kwargs)
class SetpointmanagerSinglezoneOnestagecoolingMeta:
    idf_name = 'SETPOINTMANAGER:SINGLEZONE:ONESTAGECOOLING'

def SetpointmanagerSinglezoneOnestageheating(idf, **kwargs: Unpack[SetpointmanagerSinglezoneOnestageheatingType]):
    """"helper for SetpointmanagerSinglezoneOnestageheating"""
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:ONESTAGEHEATING', **kwargs)
class SetpointmanagerSinglezoneOnestageheatingMeta:
    idf_name = 'SETPOINTMANAGER:SINGLEZONE:ONESTAGEHEATING'

def SetpointmanagerSinglezoneReheat(idf, **kwargs: Unpack[SetpointmanagerSinglezoneReheatType]):
    """"helper for SetpointmanagerSinglezoneReheat"""
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:REHEAT', **kwargs)
class SetpointmanagerSinglezoneReheatMeta:
    idf_name = 'SETPOINTMANAGER:SINGLEZONE:REHEAT'

def SetpointmanagerSystemnoderesetHumidity(idf, **kwargs: Unpack[SetpointmanagerSystemnoderesetHumidityType]):
    """"helper for SetpointmanagerSystemnoderesetHumidity"""
    return idf.newidfobject('SETPOINTMANAGER:SYSTEMNODERESET:HUMIDITY', **kwargs)
class SetpointmanagerSystemnoderesetHumidityMeta:
    idf_name = 'SETPOINTMANAGER:SYSTEMNODERESET:HUMIDITY'

def SetpointmanagerSystemnoderesetTemperature(idf, **kwargs: Unpack[SetpointmanagerSystemnoderesetTemperatureType]):
    """"helper for SetpointmanagerSystemnoderesetTemperature"""
    return idf.newidfobject('SETPOINTMANAGER:SYSTEMNODERESET:TEMPERATURE', **kwargs)
class SetpointmanagerSystemnoderesetTemperatureMeta:
    idf_name = 'SETPOINTMANAGER:SYSTEMNODERESET:TEMPERATURE'

def SetpointmanagerWarmest(idf, **kwargs: Unpack[SetpointmanagerWarmestType]):
    """"helper for SetpointmanagerWarmest"""
    return idf.newidfobject('SETPOINTMANAGER:WARMEST', **kwargs)
class SetpointmanagerWarmestMeta:
    idf_name = 'SETPOINTMANAGER:WARMEST'

def SetpointmanagerWarmesttemperatureflow(idf, **kwargs: Unpack[SetpointmanagerWarmesttemperatureflowType]):
    """"helper for SetpointmanagerWarmesttemperatureflow"""
    return idf.newidfobject('SETPOINTMANAGER:WARMESTTEMPERATUREFLOW', **kwargs)
class SetpointmanagerWarmesttemperatureflowMeta:
    idf_name = 'SETPOINTMANAGER:WARMESTTEMPERATUREFLOW'

def ShadingBuilding(idf, **kwargs: Unpack[ShadingBuildingType]):
    """"helper for ShadingBuilding"""
    return idf.newidfobject('SHADING:BUILDING', **kwargs)
class ShadingBuildingMeta:
    idf_name = 'SHADING:BUILDING'

def ShadingBuildingDetailed(idf, **kwargs: Unpack[ShadingBuildingDetailedType]):
    """"helper for ShadingBuildingDetailed"""
    return idf.newidfobject('SHADING:BUILDING:DETAILED', **kwargs)
class ShadingBuildingDetailedMeta:
    idf_name = 'SHADING:BUILDING:DETAILED'

def ShadingFin(idf, **kwargs: Unpack[ShadingFinType]):
    """"helper for ShadingFin"""
    return idf.newidfobject('SHADING:FIN', **kwargs)
class ShadingFinMeta:
    idf_name = 'SHADING:FIN'

def ShadingFinProjection(idf, **kwargs: Unpack[ShadingFinProjectionType]):
    """"helper for ShadingFinProjection"""
    return idf.newidfobject('SHADING:FIN:PROJECTION', **kwargs)
class ShadingFinProjectionMeta:
    idf_name = 'SHADING:FIN:PROJECTION'

def ShadingOverhang(idf, **kwargs: Unpack[ShadingOverhangType]):
    """"helper for ShadingOverhang"""
    return idf.newidfobject('SHADING:OVERHANG', **kwargs)
class ShadingOverhangMeta:
    idf_name = 'SHADING:OVERHANG'

def ShadingOverhangProjection(idf, **kwargs: Unpack[ShadingOverhangProjectionType]):
    """"helper for ShadingOverhangProjection"""
    return idf.newidfobject('SHADING:OVERHANG:PROJECTION', **kwargs)
class ShadingOverhangProjectionMeta:
    idf_name = 'SHADING:OVERHANG:PROJECTION'

def ShadingSite(idf, **kwargs: Unpack[ShadingSiteType]):
    """"helper for ShadingSite"""
    return idf.newidfobject('SHADING:SITE', **kwargs)
class ShadingSiteMeta:
    idf_name = 'SHADING:SITE'

def ShadingSiteDetailed(idf, **kwargs: Unpack[ShadingSiteDetailedType]):
    """"helper for ShadingSiteDetailed"""
    return idf.newidfobject('SHADING:SITE:DETAILED', **kwargs)
class ShadingSiteDetailedMeta:
    idf_name = 'SHADING:SITE:DETAILED'

def ShadingZoneDetailed(idf, **kwargs: Unpack[ShadingZoneDetailedType]):
    """"helper for ShadingZoneDetailed"""
    return idf.newidfobject('SHADING:ZONE:DETAILED', **kwargs)
class ShadingZoneDetailedMeta:
    idf_name = 'SHADING:ZONE:DETAILED'

def ShadingpropertyReflectance(idf, **kwargs: Unpack[ShadingpropertyReflectanceType]):
    """"helper for ShadingpropertyReflectance"""
    return idf.newidfobject('SHADINGPROPERTY:REFLECTANCE', **kwargs)
class ShadingpropertyReflectanceMeta:
    idf_name = 'SHADINGPROPERTY:REFLECTANCE'

def Shadowcalculation(idf, **kwargs: Unpack[ShadowcalculationType]):
    """"helper for Shadowcalculation"""
    return idf.newidfobject('SHADOWCALCULATION', **kwargs)
class ShadowcalculationMeta:
    idf_name = 'SHADOWCALCULATION'

def Simulationcontrol(idf, **kwargs: Unpack[SimulationcontrolType]):
    """"helper for Simulationcontrol"""
    return idf.newidfobject('SIMULATIONCONTROL', **kwargs)
class SimulationcontrolMeta:
    idf_name = 'SIMULATIONCONTROL'

def SiteGrounddomainBasement(idf, **kwargs: Unpack[SiteGrounddomainBasementType]):
    """"helper for SiteGrounddomainBasement"""
    return idf.newidfobject('SITE:GROUNDDOMAIN:BASEMENT', **kwargs)
class SiteGrounddomainBasementMeta:
    idf_name = 'SITE:GROUNDDOMAIN:BASEMENT'

def SiteGrounddomainSlab(idf, **kwargs: Unpack[SiteGrounddomainSlabType]):
    """"helper for SiteGrounddomainSlab"""
    return idf.newidfobject('SITE:GROUNDDOMAIN:SLAB', **kwargs)
class SiteGrounddomainSlabMeta:
    idf_name = 'SITE:GROUNDDOMAIN:SLAB'

def SiteGroundreflectance(idf, **kwargs: Unpack[SiteGroundreflectanceType]):
    """"helper for SiteGroundreflectance"""
    return idf.newidfobject('SITE:GROUNDREFLECTANCE', **kwargs)
class SiteGroundreflectanceMeta:
    idf_name = 'SITE:GROUNDREFLECTANCE'

def SiteGroundreflectanceSnowmodifier(idf, **kwargs: Unpack[SiteGroundreflectanceSnowmodifierType]):
    """"helper for SiteGroundreflectanceSnowmodifier"""
    return idf.newidfobject('SITE:GROUNDREFLECTANCE:SNOWMODIFIER', **kwargs)
class SiteGroundreflectanceSnowmodifierMeta:
    idf_name = 'SITE:GROUNDREFLECTANCE:SNOWMODIFIER'

def SiteGroundtemperatureBuildingsurface(idf, **kwargs: Unpack[SiteGroundtemperatureBuildingsurfaceType]):
    """"helper for SiteGroundtemperatureBuildingsurface"""
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:BUILDINGSURFACE', **kwargs)
class SiteGroundtemperatureBuildingsurfaceMeta:
    idf_name = 'SITE:GROUNDTEMPERATURE:BUILDINGSURFACE'

def SiteGroundtemperatureDeep(idf, **kwargs: Unpack[SiteGroundtemperatureDeepType]):
    """"helper for SiteGroundtemperatureDeep"""
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:DEEP', **kwargs)
class SiteGroundtemperatureDeepMeta:
    idf_name = 'SITE:GROUNDTEMPERATURE:DEEP'

def SiteGroundtemperatureFcfactormethod(idf, **kwargs: Unpack[SiteGroundtemperatureFcfactormethodType]):
    """"helper for SiteGroundtemperatureFcfactormethod"""
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:FCFACTORMETHOD', **kwargs)
class SiteGroundtemperatureFcfactormethodMeta:
    idf_name = 'SITE:GROUNDTEMPERATURE:FCFACTORMETHOD'

def SiteGroundtemperatureShallow(idf, **kwargs: Unpack[SiteGroundtemperatureShallowType]):
    """"helper for SiteGroundtemperatureShallow"""
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:SHALLOW', **kwargs)
class SiteGroundtemperatureShallowMeta:
    idf_name = 'SITE:GROUNDTEMPERATURE:SHALLOW'

def SiteGroundtemperatureUndisturbedFinitedifference(idf, **kwargs: Unpack[SiteGroundtemperatureUndisturbedFinitedifferenceType]):
    """"helper for SiteGroundtemperatureUndisturbedFinitedifference"""
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:UNDISTURBED:FINITEDIFFERENCE', **kwargs)
class SiteGroundtemperatureUndisturbedFinitedifferenceMeta:
    idf_name = 'SITE:GROUNDTEMPERATURE:UNDISTURBED:FINITEDIFFERENCE'

def SiteGroundtemperatureUndisturbedKusudaachenbach(idf, **kwargs: Unpack[SiteGroundtemperatureUndisturbedKusudaachenbachType]):
    """"helper for SiteGroundtemperatureUndisturbedKusudaachenbach"""
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:UNDISTURBED:KUSUDAACHENBACH', **kwargs)
class SiteGroundtemperatureUndisturbedKusudaachenbachMeta:
    idf_name = 'SITE:GROUNDTEMPERATURE:UNDISTURBED:KUSUDAACHENBACH'

def SiteGroundtemperatureUndisturbedXing(idf, **kwargs: Unpack[SiteGroundtemperatureUndisturbedXingType]):
    """"helper for SiteGroundtemperatureUndisturbedXing"""
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:UNDISTURBED:XING', **kwargs)
class SiteGroundtemperatureUndisturbedXingMeta:
    idf_name = 'SITE:GROUNDTEMPERATURE:UNDISTURBED:XING'

def SiteHeightvariation(idf, **kwargs: Unpack[SiteHeightvariationType]):
    """"helper for SiteHeightvariation"""
    return idf.newidfobject('SITE:HEIGHTVARIATION', **kwargs)
class SiteHeightvariationMeta:
    idf_name = 'SITE:HEIGHTVARIATION'

def SiteLocation(idf, **kwargs: Unpack[SiteLocationType]):
    """"helper for SiteLocation"""
    return idf.newidfobject('SITE:LOCATION', **kwargs)
class SiteLocationMeta:
    idf_name = 'SITE:LOCATION'

def SitePrecipitation(idf, **kwargs: Unpack[SitePrecipitationType]):
    """"helper for SitePrecipitation"""
    return idf.newidfobject('SITE:PRECIPITATION', **kwargs)
class SitePrecipitationMeta:
    idf_name = 'SITE:PRECIPITATION'

def SiteSolarandvisiblespectrum(idf, **kwargs: Unpack[SiteSolarandvisiblespectrumType]):
    """"helper for SiteSolarandvisiblespectrum"""
    return idf.newidfobject('SITE:SOLARANDVISIBLESPECTRUM', **kwargs)
class SiteSolarandvisiblespectrumMeta:
    idf_name = 'SITE:SOLARANDVISIBLESPECTRUM'

def SiteSpectrumdata(idf, **kwargs: Unpack[SiteSpectrumdataType]):
    """"helper for SiteSpectrumdata"""
    return idf.newidfobject('SITE:SPECTRUMDATA', **kwargs)
class SiteSpectrumdataMeta:
    idf_name = 'SITE:SPECTRUMDATA'

def SiteVariablelocation(idf, **kwargs: Unpack[SiteVariablelocationType]):
    """"helper for SiteVariablelocation"""
    return idf.newidfobject('SITE:VARIABLELOCATION', **kwargs)
class SiteVariablelocationMeta:
    idf_name = 'SITE:VARIABLELOCATION'

def SiteWatermainstemperature(idf, **kwargs: Unpack[SiteWatermainstemperatureType]):
    """"helper for SiteWatermainstemperature"""
    return idf.newidfobject('SITE:WATERMAINSTEMPERATURE', **kwargs)
class SiteWatermainstemperatureMeta:
    idf_name = 'SITE:WATERMAINSTEMPERATURE'

def SiteWeatherstation(idf, **kwargs: Unpack[SiteWeatherstationType]):
    """"helper for SiteWeatherstation"""
    return idf.newidfobject('SITE:WEATHERSTATION', **kwargs)
class SiteWeatherstationMeta:
    idf_name = 'SITE:WEATHERSTATION'

def SizingParameters(idf, **kwargs: Unpack[SizingParametersType]):
    """"helper for SizingParameters"""
    return idf.newidfobject('SIZING:PARAMETERS', **kwargs)
class SizingParametersMeta:
    idf_name = 'SIZING:PARAMETERS'

def SizingPlant(idf, **kwargs: Unpack[SizingPlantType]):
    """"helper for SizingPlant"""
    return idf.newidfobject('SIZING:PLANT', **kwargs)
class SizingPlantMeta:
    idf_name = 'SIZING:PLANT'

def SizingSystem(idf, **kwargs: Unpack[SizingSystemType]):
    """"helper for SizingSystem"""
    return idf.newidfobject('SIZING:SYSTEM', **kwargs)
class SizingSystemMeta:
    idf_name = 'SIZING:SYSTEM'

def SizingZone(idf, **kwargs: Unpack[SizingZoneType]):
    """"helper for SizingZone"""
    return idf.newidfobject('SIZING:ZONE', **kwargs)
class SizingZoneMeta:
    idf_name = 'SIZING:ZONE'

def SizingperiodDesignday(idf, **kwargs: Unpack[SizingperiodDesigndayType]):
    """"helper for SizingperiodDesignday"""
    return idf.newidfobject('SIZINGPERIOD:DESIGNDAY', **kwargs)
class SizingperiodDesigndayMeta:
    idf_name = 'SIZINGPERIOD:DESIGNDAY'

def SizingperiodWeatherfileconditiontype(idf, **kwargs: Unpack[SizingperiodWeatherfileconditiontypeType]):
    """"helper for SizingperiodWeatherfileconditiontype"""
    return idf.newidfobject('SIZINGPERIOD:WEATHERFILECONDITIONTYPE', **kwargs)
class SizingperiodWeatherfileconditiontypeMeta:
    idf_name = 'SIZINGPERIOD:WEATHERFILECONDITIONTYPE'

def SizingperiodWeatherfiledays(idf, **kwargs: Unpack[SizingperiodWeatherfiledaysType]):
    """"helper for SizingperiodWeatherfiledays"""
    return idf.newidfobject('SIZINGPERIOD:WEATHERFILEDAYS', **kwargs)
class SizingperiodWeatherfiledaysMeta:
    idf_name = 'SIZINGPERIOD:WEATHERFILEDAYS'

def SolarcollectorFlatplatePhotovoltaicthermal(idf, **kwargs: Unpack[SolarcollectorFlatplatePhotovoltaicthermalType]):
    """"helper for SolarcollectorFlatplatePhotovoltaicthermal"""
    return idf.newidfobject('SOLARCOLLECTOR:FLATPLATE:PHOTOVOLTAICTHERMAL', **kwargs)
class SolarcollectorFlatplatePhotovoltaicthermalMeta:
    idf_name = 'SOLARCOLLECTOR:FLATPLATE:PHOTOVOLTAICTHERMAL'

def SolarcollectorFlatplateWater(idf, **kwargs: Unpack[SolarcollectorFlatplateWaterType]):
    """"helper for SolarcollectorFlatplateWater"""
    return idf.newidfobject('SOLARCOLLECTOR:FLATPLATE:WATER', **kwargs)
class SolarcollectorFlatplateWaterMeta:
    idf_name = 'SOLARCOLLECTOR:FLATPLATE:WATER'

def SolarcollectorIntegralcollectorstorage(idf, **kwargs: Unpack[SolarcollectorIntegralcollectorstorageType]):
    """"helper for SolarcollectorIntegralcollectorstorage"""
    return idf.newidfobject('SOLARCOLLECTOR:INTEGRALCOLLECTORSTORAGE', **kwargs)
class SolarcollectorIntegralcollectorstorageMeta:
    idf_name = 'SOLARCOLLECTOR:INTEGRALCOLLECTORSTORAGE'

def SolarcollectorUnglazedtranspired(idf, **kwargs: Unpack[SolarcollectorUnglazedtranspiredType]):
    """"helper for SolarcollectorUnglazedtranspired"""
    return idf.newidfobject('SOLARCOLLECTOR:UNGLAZEDTRANSPIRED', **kwargs)
class SolarcollectorUnglazedtranspiredMeta:
    idf_name = 'SOLARCOLLECTOR:UNGLAZEDTRANSPIRED'

def SolarcollectorUnglazedtranspiredMultisystem(idf, **kwargs: Unpack[SolarcollectorUnglazedtranspiredMultisystemType]):
    """"helper for SolarcollectorUnglazedtranspiredMultisystem"""
    return idf.newidfobject('SOLARCOLLECTOR:UNGLAZEDTRANSPIRED:MULTISYSTEM', **kwargs)
class SolarcollectorUnglazedtranspiredMultisystemMeta:
    idf_name = 'SOLARCOLLECTOR:UNGLAZEDTRANSPIRED:MULTISYSTEM'

def SolarcollectorperformanceFlatplate(idf, **kwargs: Unpack[SolarcollectorperformanceFlatplateType]):
    """"helper for SolarcollectorperformanceFlatplate"""
    return idf.newidfobject('SOLARCOLLECTORPERFORMANCE:FLATPLATE', **kwargs)
class SolarcollectorperformanceFlatplateMeta:
    idf_name = 'SOLARCOLLECTORPERFORMANCE:FLATPLATE'

def SolarcollectorperformanceIntegralcollectorstorage(idf, **kwargs: Unpack[SolarcollectorperformanceIntegralcollectorstorageType]):
    """"helper for SolarcollectorperformanceIntegralcollectorstorage"""
    return idf.newidfobject('SOLARCOLLECTORPERFORMANCE:INTEGRALCOLLECTORSTORAGE', **kwargs)
class SolarcollectorperformanceIntegralcollectorstorageMeta:
    idf_name = 'SOLARCOLLECTORPERFORMANCE:INTEGRALCOLLECTORSTORAGE'

def SolarcollectorperformancePhotovoltaicthermalBipvt(idf, **kwargs: Unpack[SolarcollectorperformancePhotovoltaicthermalBipvtType]):
    """"helper for SolarcollectorperformancePhotovoltaicthermalBipvt"""
    return idf.newidfobject('SOLARCOLLECTORPERFORMANCE:PHOTOVOLTAICTHERMAL:BIPVT', **kwargs)
class SolarcollectorperformancePhotovoltaicthermalBipvtMeta:
    idf_name = 'SOLARCOLLECTORPERFORMANCE:PHOTOVOLTAICTHERMAL:BIPVT'

def SolarcollectorperformancePhotovoltaicthermalSimple(idf, **kwargs: Unpack[SolarcollectorperformancePhotovoltaicthermalSimpleType]):
    """"helper for SolarcollectorperformancePhotovoltaicthermalSimple"""
    return idf.newidfobject('SOLARCOLLECTORPERFORMANCE:PHOTOVOLTAICTHERMAL:SIMPLE', **kwargs)
class SolarcollectorperformancePhotovoltaicthermalSimpleMeta:
    idf_name = 'SOLARCOLLECTORPERFORMANCE:PHOTOVOLTAICTHERMAL:SIMPLE'

def Space(idf, **kwargs: Unpack[SpaceType]):
    """"helper for Space"""
    return idf.newidfobject('SPACE', **kwargs)
class SpaceMeta:
    idf_name = 'SPACE'

def SpacehvacEquipmentconnections(idf, **kwargs: Unpack[SpacehvacEquipmentconnectionsType]):
    """"helper for SpacehvacEquipmentconnections"""
    return idf.newidfobject('SPACEHVAC:EQUIPMENTCONNECTIONS', **kwargs)
class SpacehvacEquipmentconnectionsMeta:
    idf_name = 'SPACEHVAC:EQUIPMENTCONNECTIONS'

def SpacehvacZoneequipmentmixer(idf, **kwargs: Unpack[SpacehvacZoneequipmentmixerType]):
    """"helper for SpacehvacZoneequipmentmixer"""
    return idf.newidfobject('SPACEHVAC:ZONEEQUIPMENTMIXER', **kwargs)
class SpacehvacZoneequipmentmixerMeta:
    idf_name = 'SPACEHVAC:ZONEEQUIPMENTMIXER'

def SpacehvacZoneequipmentsplitter(idf, **kwargs: Unpack[SpacehvacZoneequipmentsplitterType]):
    """"helper for SpacehvacZoneequipmentsplitter"""
    return idf.newidfobject('SPACEHVAC:ZONEEQUIPMENTSPLITTER', **kwargs)
class SpacehvacZoneequipmentsplitterMeta:
    idf_name = 'SPACEHVAC:ZONEEQUIPMENTSPLITTER'

def Spacelist(idf, **kwargs: Unpack[SpacelistType]):
    """"helper for Spacelist"""
    return idf.newidfobject('SPACELIST', **kwargs)
class SpacelistMeta:
    idf_name = 'SPACELIST'

def Steamequipment(idf, **kwargs: Unpack[SteamequipmentType]):
    """"helper for Steamequipment"""
    return idf.newidfobject('STEAMEQUIPMENT', **kwargs)
class SteamequipmentMeta:
    idf_name = 'STEAMEQUIPMENT'

def SurfacecontaminantsourceandsinkGenericBoundarylayerdiffusion(idf, **kwargs: Unpack[SurfacecontaminantsourceandsinkGenericBoundarylayerdiffusionType]):
    """"helper for SurfacecontaminantsourceandsinkGenericBoundarylayerdiffusion"""
    return idf.newidfobject('SURFACECONTAMINANTSOURCEANDSINK:GENERIC:BOUNDARYLAYERDIFFUSION', **kwargs)
class SurfacecontaminantsourceandsinkGenericBoundarylayerdiffusionMeta:
    idf_name = 'SURFACECONTAMINANTSOURCEANDSINK:GENERIC:BOUNDARYLAYERDIFFUSION'

def SurfacecontaminantsourceandsinkGenericDepositionvelocitysink(idf, **kwargs: Unpack[SurfacecontaminantsourceandsinkGenericDepositionvelocitysinkType]):
    """"helper for SurfacecontaminantsourceandsinkGenericDepositionvelocitysink"""
    return idf.newidfobject('SURFACECONTAMINANTSOURCEANDSINK:GENERIC:DEPOSITIONVELOCITYSINK', **kwargs)
class SurfacecontaminantsourceandsinkGenericDepositionvelocitysinkMeta:
    idf_name = 'SURFACECONTAMINANTSOURCEANDSINK:GENERIC:DEPOSITIONVELOCITYSINK'

def SurfacecontaminantsourceandsinkGenericPressuredriven(idf, **kwargs: Unpack[SurfacecontaminantsourceandsinkGenericPressuredrivenType]):
    """"helper for SurfacecontaminantsourceandsinkGenericPressuredriven"""
    return idf.newidfobject('SURFACECONTAMINANTSOURCEANDSINK:GENERIC:PRESSUREDRIVEN', **kwargs)
class SurfacecontaminantsourceandsinkGenericPressuredrivenMeta:
    idf_name = 'SURFACECONTAMINANTSOURCEANDSINK:GENERIC:PRESSUREDRIVEN'

def SurfacecontrolMovableinsulation(idf, **kwargs: Unpack[SurfacecontrolMovableinsulationType]):
    """"helper for SurfacecontrolMovableinsulation"""
    return idf.newidfobject('SURFACECONTROL:MOVABLEINSULATION', **kwargs)
class SurfacecontrolMovableinsulationMeta:
    idf_name = 'SURFACECONTROL:MOVABLEINSULATION'

def SurfaceconvectionalgorithmInside(idf, **kwargs: Unpack[SurfaceconvectionalgorithmInsideType]):
    """"helper for SurfaceconvectionalgorithmInside"""
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:INSIDE', **kwargs)
class SurfaceconvectionalgorithmInsideMeta:
    idf_name = 'SURFACECONVECTIONALGORITHM:INSIDE'

def SurfaceconvectionalgorithmInsideAdaptivemodelselections(idf, **kwargs: Unpack[SurfaceconvectionalgorithmInsideAdaptivemodelselectionsType]):
    """"helper for SurfaceconvectionalgorithmInsideAdaptivemodelselections"""
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:INSIDE:ADAPTIVEMODELSELECTIONS', **kwargs)
class SurfaceconvectionalgorithmInsideAdaptivemodelselectionsMeta:
    idf_name = 'SURFACECONVECTIONALGORITHM:INSIDE:ADAPTIVEMODELSELECTIONS'

def SurfaceconvectionalgorithmInsideUsercurve(idf, **kwargs: Unpack[SurfaceconvectionalgorithmInsideUsercurveType]):
    """"helper for SurfaceconvectionalgorithmInsideUsercurve"""
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:INSIDE:USERCURVE', **kwargs)
class SurfaceconvectionalgorithmInsideUsercurveMeta:
    idf_name = 'SURFACECONVECTIONALGORITHM:INSIDE:USERCURVE'

def SurfaceconvectionalgorithmOutside(idf, **kwargs: Unpack[SurfaceconvectionalgorithmOutsideType]):
    """"helper for SurfaceconvectionalgorithmOutside"""
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:OUTSIDE', **kwargs)
class SurfaceconvectionalgorithmOutsideMeta:
    idf_name = 'SURFACECONVECTIONALGORITHM:OUTSIDE'

def SurfaceconvectionalgorithmOutsideAdaptivemodelselections(idf, **kwargs: Unpack[SurfaceconvectionalgorithmOutsideAdaptivemodelselectionsType]):
    """"helper for SurfaceconvectionalgorithmOutsideAdaptivemodelselections"""
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:OUTSIDE:ADAPTIVEMODELSELECTIONS', **kwargs)
class SurfaceconvectionalgorithmOutsideAdaptivemodelselectionsMeta:
    idf_name = 'SURFACECONVECTIONALGORITHM:OUTSIDE:ADAPTIVEMODELSELECTIONS'

def SurfaceconvectionalgorithmOutsideUsercurve(idf, **kwargs: Unpack[SurfaceconvectionalgorithmOutsideUsercurveType]):
    """"helper for SurfaceconvectionalgorithmOutsideUsercurve"""
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:OUTSIDE:USERCURVE', **kwargs)
class SurfaceconvectionalgorithmOutsideUsercurveMeta:
    idf_name = 'SURFACECONVECTIONALGORITHM:OUTSIDE:USERCURVE'

def SurfacepropertiesVaporcoefficients(idf, **kwargs: Unpack[SurfacepropertiesVaporcoefficientsType]):
    """"helper for SurfacepropertiesVaporcoefficients"""
    return idf.newidfobject('SURFACEPROPERTIES:VAPORCOEFFICIENTS', **kwargs)
class SurfacepropertiesVaporcoefficientsMeta:
    idf_name = 'SURFACEPROPERTIES:VAPORCOEFFICIENTS'

def SurfacepropertyConvectioncoefficients(idf, **kwargs: Unpack[SurfacepropertyConvectioncoefficientsType]):
    """"helper for SurfacepropertyConvectioncoefficients"""
    return idf.newidfobject('SURFACEPROPERTY:CONVECTIONCOEFFICIENTS', **kwargs)
class SurfacepropertyConvectioncoefficientsMeta:
    idf_name = 'SURFACEPROPERTY:CONVECTIONCOEFFICIENTS'

def SurfacepropertyConvectioncoefficientsMultiplesurface(idf, **kwargs: Unpack[SurfacepropertyConvectioncoefficientsMultiplesurfaceType]):
    """"helper for SurfacepropertyConvectioncoefficientsMultiplesurface"""
    return idf.newidfobject('SURFACEPROPERTY:CONVECTIONCOEFFICIENTS:MULTIPLESURFACE', **kwargs)
class SurfacepropertyConvectioncoefficientsMultiplesurfaceMeta:
    idf_name = 'SURFACEPROPERTY:CONVECTIONCOEFFICIENTS:MULTIPLESURFACE'

def SurfacepropertyExposedfoundationperimeter(idf, **kwargs: Unpack[SurfacepropertyExposedfoundationperimeterType]):
    """"helper for SurfacepropertyExposedfoundationperimeter"""
    return idf.newidfobject('SURFACEPROPERTY:EXPOSEDFOUNDATIONPERIMETER', **kwargs)
class SurfacepropertyExposedfoundationperimeterMeta:
    idf_name = 'SURFACEPROPERTY:EXPOSEDFOUNDATIONPERIMETER'

def SurfacepropertyExteriornaturalventedcavity(idf, **kwargs: Unpack[SurfacepropertyExteriornaturalventedcavityType]):
    """"helper for SurfacepropertyExteriornaturalventedcavity"""
    return idf.newidfobject('SURFACEPROPERTY:EXTERIORNATURALVENTEDCAVITY', **kwargs)
class SurfacepropertyExteriornaturalventedcavityMeta:
    idf_name = 'SURFACEPROPERTY:EXTERIORNATURALVENTEDCAVITY'

def SurfacepropertyGroundsurfaces(idf, **kwargs: Unpack[SurfacepropertyGroundsurfacesType]):
    """"helper for SurfacepropertyGroundsurfaces"""
    return idf.newidfobject('SURFACEPROPERTY:GROUNDSURFACES', **kwargs)
class SurfacepropertyGroundsurfacesMeta:
    idf_name = 'SURFACEPROPERTY:GROUNDSURFACES'

def SurfacepropertyHeatbalancesourceterm(idf, **kwargs: Unpack[SurfacepropertyHeatbalancesourcetermType]):
    """"helper for SurfacepropertyHeatbalancesourceterm"""
    return idf.newidfobject('SURFACEPROPERTY:HEATBALANCESOURCETERM', **kwargs)
class SurfacepropertyHeatbalancesourcetermMeta:
    idf_name = 'SURFACEPROPERTY:HEATBALANCESOURCETERM'

def SurfacepropertyHeattransferalgorithm(idf, **kwargs: Unpack[SurfacepropertyHeattransferalgorithmType]):
    """"helper for SurfacepropertyHeattransferalgorithm"""
    return idf.newidfobject('SURFACEPROPERTY:HEATTRANSFERALGORITHM', **kwargs)
class SurfacepropertyHeattransferalgorithmMeta:
    idf_name = 'SURFACEPROPERTY:HEATTRANSFERALGORITHM'

def SurfacepropertyHeattransferalgorithmConstruction(idf, **kwargs: Unpack[SurfacepropertyHeattransferalgorithmConstructionType]):
    """"helper for SurfacepropertyHeattransferalgorithmConstruction"""
    return idf.newidfobject('SURFACEPROPERTY:HEATTRANSFERALGORITHM:CONSTRUCTION', **kwargs)
class SurfacepropertyHeattransferalgorithmConstructionMeta:
    idf_name = 'SURFACEPROPERTY:HEATTRANSFERALGORITHM:CONSTRUCTION'

def SurfacepropertyHeattransferalgorithmMultiplesurface(idf, **kwargs: Unpack[SurfacepropertyHeattransferalgorithmMultiplesurfaceType]):
    """"helper for SurfacepropertyHeattransferalgorithmMultiplesurface"""
    return idf.newidfobject('SURFACEPROPERTY:HEATTRANSFERALGORITHM:MULTIPLESURFACE', **kwargs)
class SurfacepropertyHeattransferalgorithmMultiplesurfaceMeta:
    idf_name = 'SURFACEPROPERTY:HEATTRANSFERALGORITHM:MULTIPLESURFACE'

def SurfacepropertyHeattransferalgorithmSurfacelist(idf, **kwargs: Unpack[SurfacepropertyHeattransferalgorithmSurfacelistType]):
    """"helper for SurfacepropertyHeattransferalgorithmSurfacelist"""
    return idf.newidfobject('SURFACEPROPERTY:HEATTRANSFERALGORITHM:SURFACELIST', **kwargs)
class SurfacepropertyHeattransferalgorithmSurfacelistMeta:
    idf_name = 'SURFACEPROPERTY:HEATTRANSFERALGORITHM:SURFACELIST'

def SurfacepropertyIncidentsolarmultiplier(idf, **kwargs: Unpack[SurfacepropertyIncidentsolarmultiplierType]):
    """"helper for SurfacepropertyIncidentsolarmultiplier"""
    return idf.newidfobject('SURFACEPROPERTY:INCIDENTSOLARMULTIPLIER', **kwargs)
class SurfacepropertyIncidentsolarmultiplierMeta:
    idf_name = 'SURFACEPROPERTY:INCIDENTSOLARMULTIPLIER'

def SurfacepropertyLocalenvironment(idf, **kwargs: Unpack[SurfacepropertyLocalenvironmentType]):
    """"helper for SurfacepropertyLocalenvironment"""
    return idf.newidfobject('SURFACEPROPERTY:LOCALENVIRONMENT', **kwargs)
class SurfacepropertyLocalenvironmentMeta:
    idf_name = 'SURFACEPROPERTY:LOCALENVIRONMENT'

def SurfacepropertyOthersidecoefficients(idf, **kwargs: Unpack[SurfacepropertyOthersidecoefficientsType]):
    """"helper for SurfacepropertyOthersidecoefficients"""
    return idf.newidfobject('SURFACEPROPERTY:OTHERSIDECOEFFICIENTS', **kwargs)
class SurfacepropertyOthersidecoefficientsMeta:
    idf_name = 'SURFACEPROPERTY:OTHERSIDECOEFFICIENTS'

def SurfacepropertyOthersideconditionsmodel(idf, **kwargs: Unpack[SurfacepropertyOthersideconditionsmodelType]):
    """"helper for SurfacepropertyOthersideconditionsmodel"""
    return idf.newidfobject('SURFACEPROPERTY:OTHERSIDECONDITIONSMODEL', **kwargs)
class SurfacepropertyOthersideconditionsmodelMeta:
    idf_name = 'SURFACEPROPERTY:OTHERSIDECONDITIONSMODEL'

def SurfacepropertySolarincidentinside(idf, **kwargs: Unpack[SurfacepropertySolarincidentinsideType]):
    """"helper for SurfacepropertySolarincidentinside"""
    return idf.newidfobject('SURFACEPROPERTY:SOLARINCIDENTINSIDE', **kwargs)
class SurfacepropertySolarincidentinsideMeta:
    idf_name = 'SURFACEPROPERTY:SOLARINCIDENTINSIDE'

def SurfacepropertySurroundingsurfaces(idf, **kwargs: Unpack[SurfacepropertySurroundingsurfacesType]):
    """"helper for SurfacepropertySurroundingsurfaces"""
    return idf.newidfobject('SURFACEPROPERTY:SURROUNDINGSURFACES', **kwargs)
class SurfacepropertySurroundingsurfacesMeta:
    idf_name = 'SURFACEPROPERTY:SURROUNDINGSURFACES'

def SurfacepropertyUnderwater(idf, **kwargs: Unpack[SurfacepropertyUnderwaterType]):
    """"helper for SurfacepropertyUnderwater"""
    return idf.newidfobject('SURFACEPROPERTY:UNDERWATER', **kwargs)
class SurfacepropertyUnderwaterMeta:
    idf_name = 'SURFACEPROPERTY:UNDERWATER'

def SwimmingpoolIndoor(idf, **kwargs: Unpack[SwimmingpoolIndoorType]):
    """"helper for SwimmingpoolIndoor"""
    return idf.newidfobject('SWIMMINGPOOL:INDOOR', **kwargs)
class SwimmingpoolIndoorMeta:
    idf_name = 'SWIMMINGPOOL:INDOOR'

def TableIndependentvariable(idf, **kwargs: Unpack[TableIndependentvariableType]):
    """"helper for TableIndependentvariable"""
    return idf.newidfobject('TABLE:INDEPENDENTVARIABLE', **kwargs)
class TableIndependentvariableMeta:
    idf_name = 'TABLE:INDEPENDENTVARIABLE'

def TableIndependentvariablelist(idf, **kwargs: Unpack[TableIndependentvariablelistType]):
    """"helper for TableIndependentvariablelist"""
    return idf.newidfobject('TABLE:INDEPENDENTVARIABLELIST', **kwargs)
class TableIndependentvariablelistMeta:
    idf_name = 'TABLE:INDEPENDENTVARIABLELIST'

def TableLookup(idf, **kwargs: Unpack[TableLookupType]):
    """"helper for TableLookup"""
    return idf.newidfobject('TABLE:LOOKUP', **kwargs)
class TableLookupMeta:
    idf_name = 'TABLE:LOOKUP'

def Temperingvalve(idf, **kwargs: Unpack[TemperingvalveType]):
    """"helper for Temperingvalve"""
    return idf.newidfobject('TEMPERINGVALVE', **kwargs)
class TemperingvalveMeta:
    idf_name = 'TEMPERINGVALVE'

def ThermalstorageChilledwaterMixed(idf, **kwargs: Unpack[ThermalstorageChilledwaterMixedType]):
    """"helper for ThermalstorageChilledwaterMixed"""
    return idf.newidfobject('THERMALSTORAGE:CHILLEDWATER:MIXED', **kwargs)
class ThermalstorageChilledwaterMixedMeta:
    idf_name = 'THERMALSTORAGE:CHILLEDWATER:MIXED'

def ThermalstorageChilledwaterStratified(idf, **kwargs: Unpack[ThermalstorageChilledwaterStratifiedType]):
    """"helper for ThermalstorageChilledwaterStratified"""
    return idf.newidfobject('THERMALSTORAGE:CHILLEDWATER:STRATIFIED', **kwargs)
class ThermalstorageChilledwaterStratifiedMeta:
    idf_name = 'THERMALSTORAGE:CHILLEDWATER:STRATIFIED'

def ThermalstorageIceDetailed(idf, **kwargs: Unpack[ThermalstorageIceDetailedType]):
    """"helper for ThermalstorageIceDetailed"""
    return idf.newidfobject('THERMALSTORAGE:ICE:DETAILED', **kwargs)
class ThermalstorageIceDetailedMeta:
    idf_name = 'THERMALSTORAGE:ICE:DETAILED'

def ThermalstorageIceSimple(idf, **kwargs: Unpack[ThermalstorageIceSimpleType]):
    """"helper for ThermalstorageIceSimple"""
    return idf.newidfobject('THERMALSTORAGE:ICE:SIMPLE', **kwargs)
class ThermalstorageIceSimpleMeta:
    idf_name = 'THERMALSTORAGE:ICE:SIMPLE'

def ThermostatsetpointDualsetpoint(idf, **kwargs: Unpack[ThermostatsetpointDualsetpointType]):
    """"helper for ThermostatsetpointDualsetpoint"""
    return idf.newidfobject('THERMOSTATSETPOINT:DUALSETPOINT', **kwargs)
class ThermostatsetpointDualsetpointMeta:
    idf_name = 'THERMOSTATSETPOINT:DUALSETPOINT'

def ThermostatsetpointSinglecooling(idf, **kwargs: Unpack[ThermostatsetpointSinglecoolingType]):
    """"helper for ThermostatsetpointSinglecooling"""
    return idf.newidfobject('THERMOSTATSETPOINT:SINGLECOOLING', **kwargs)
class ThermostatsetpointSinglecoolingMeta:
    idf_name = 'THERMOSTATSETPOINT:SINGLECOOLING'

def ThermostatsetpointSingleheating(idf, **kwargs: Unpack[ThermostatsetpointSingleheatingType]):
    """"helper for ThermostatsetpointSingleheating"""
    return idf.newidfobject('THERMOSTATSETPOINT:SINGLEHEATING', **kwargs)
class ThermostatsetpointSingleheatingMeta:
    idf_name = 'THERMOSTATSETPOINT:SINGLEHEATING'

def ThermostatsetpointSingleheatingorcooling(idf, **kwargs: Unpack[ThermostatsetpointSingleheatingorcoolingType]):
    """"helper for ThermostatsetpointSingleheatingorcooling"""
    return idf.newidfobject('THERMOSTATSETPOINT:SINGLEHEATINGORCOOLING', **kwargs)
class ThermostatsetpointSingleheatingorcoolingMeta:
    idf_name = 'THERMOSTATSETPOINT:SINGLEHEATINGORCOOLING'

def ThermostatsetpointThermalcomfortFangerDualsetpoint(idf, **kwargs: Unpack[ThermostatsetpointThermalcomfortFangerDualsetpointType]):
    """"helper for ThermostatsetpointThermalcomfortFangerDualsetpoint"""
    return idf.newidfobject('THERMOSTATSETPOINT:THERMALCOMFORT:FANGER:DUALSETPOINT', **kwargs)
class ThermostatsetpointThermalcomfortFangerDualsetpointMeta:
    idf_name = 'THERMOSTATSETPOINT:THERMALCOMFORT:FANGER:DUALSETPOINT'

def ThermostatsetpointThermalcomfortFangerSinglecooling(idf, **kwargs: Unpack[ThermostatsetpointThermalcomfortFangerSinglecoolingType]):
    """"helper for ThermostatsetpointThermalcomfortFangerSinglecooling"""
    return idf.newidfobject('THERMOSTATSETPOINT:THERMALCOMFORT:FANGER:SINGLECOOLING', **kwargs)
class ThermostatsetpointThermalcomfortFangerSinglecoolingMeta:
    idf_name = 'THERMOSTATSETPOINT:THERMALCOMFORT:FANGER:SINGLECOOLING'

def ThermostatsetpointThermalcomfortFangerSingleheating(idf, **kwargs: Unpack[ThermostatsetpointThermalcomfortFangerSingleheatingType]):
    """"helper for ThermostatsetpointThermalcomfortFangerSingleheating"""
    return idf.newidfobject('THERMOSTATSETPOINT:THERMALCOMFORT:FANGER:SINGLEHEATING', **kwargs)
class ThermostatsetpointThermalcomfortFangerSingleheatingMeta:
    idf_name = 'THERMOSTATSETPOINT:THERMALCOMFORT:FANGER:SINGLEHEATING'

def ThermostatsetpointThermalcomfortFangerSingleheatingorcooling(idf, **kwargs: Unpack[ThermostatsetpointThermalcomfortFangerSingleheatingorcoolingType]):
    """"helper for ThermostatsetpointThermalcomfortFangerSingleheatingorcooling"""
    return idf.newidfobject('THERMOSTATSETPOINT:THERMALCOMFORT:FANGER:SINGLEHEATINGORCOOLING', **kwargs)
class ThermostatsetpointThermalcomfortFangerSingleheatingorcoolingMeta:
    idf_name = 'THERMOSTATSETPOINT:THERMALCOMFORT:FANGER:SINGLEHEATINGORCOOLING'

def Timestep(idf, **kwargs: Unpack[TimestepType]):
    """"helper for Timestep"""
    return idf.newidfobject('TIMESTEP', **kwargs)
class TimestepMeta:
    idf_name = 'TIMESTEP'

def UnitarysystemperformanceMultispeed(idf, **kwargs: Unpack[UnitarysystemperformanceMultispeedType]):
    """"helper for UnitarysystemperformanceMultispeed"""
    return idf.newidfobject('UNITARYSYSTEMPERFORMANCE:MULTISPEED', **kwargs)
class UnitarysystemperformanceMultispeedMeta:
    idf_name = 'UNITARYSYSTEMPERFORMANCE:MULTISPEED'

def UtilitycostChargeBlock(idf, **kwargs: Unpack[UtilitycostChargeBlockType]):
    """"helper for UtilitycostChargeBlock"""
    return idf.newidfobject('UTILITYCOST:CHARGE:BLOCK', **kwargs)
class UtilitycostChargeBlockMeta:
    idf_name = 'UTILITYCOST:CHARGE:BLOCK'

def UtilitycostChargeSimple(idf, **kwargs: Unpack[UtilitycostChargeSimpleType]):
    """"helper for UtilitycostChargeSimple"""
    return idf.newidfobject('UTILITYCOST:CHARGE:SIMPLE', **kwargs)
class UtilitycostChargeSimpleMeta:
    idf_name = 'UTILITYCOST:CHARGE:SIMPLE'

def UtilitycostComputation(idf, **kwargs: Unpack[UtilitycostComputationType]):
    """"helper for UtilitycostComputation"""
    return idf.newidfobject('UTILITYCOST:COMPUTATION', **kwargs)
class UtilitycostComputationMeta:
    idf_name = 'UTILITYCOST:COMPUTATION'

def UtilitycostQualify(idf, **kwargs: Unpack[UtilitycostQualifyType]):
    """"helper for UtilitycostQualify"""
    return idf.newidfobject('UTILITYCOST:QUALIFY', **kwargs)
class UtilitycostQualifyMeta:
    idf_name = 'UTILITYCOST:QUALIFY'

def UtilitycostRatchet(idf, **kwargs: Unpack[UtilitycostRatchetType]):
    """"helper for UtilitycostRatchet"""
    return idf.newidfobject('UTILITYCOST:RATCHET', **kwargs)
class UtilitycostRatchetMeta:
    idf_name = 'UTILITYCOST:RATCHET'

def UtilitycostTariff(idf, **kwargs: Unpack[UtilitycostTariffType]):
    """"helper for UtilitycostTariff"""
    return idf.newidfobject('UTILITYCOST:TARIFF', **kwargs)
class UtilitycostTariffMeta:
    idf_name = 'UTILITYCOST:TARIFF'

def UtilitycostVariable(idf, **kwargs: Unpack[UtilitycostVariableType]):
    """"helper for UtilitycostVariable"""
    return idf.newidfobject('UTILITYCOST:VARIABLE', **kwargs)
class UtilitycostVariableMeta:
    idf_name = 'UTILITYCOST:VARIABLE'

def Version(idf, **kwargs: Unpack[VersionType]):
    """"helper for Version"""
    return idf.newidfobject('VERSION', **kwargs)
class VersionMeta:
    idf_name = 'VERSION'

def WallAdiabatic(idf, **kwargs: Unpack[WallAdiabaticType]):
    """"helper for WallAdiabatic"""
    return idf.newidfobject('WALL:ADIABATIC', **kwargs)
class WallAdiabaticMeta:
    idf_name = 'WALL:ADIABATIC'

def WallDetailed(idf, **kwargs: Unpack[WallDetailedType]):
    """"helper for WallDetailed"""
    return idf.newidfobject('WALL:DETAILED', **kwargs)
class WallDetailedMeta:
    idf_name = 'WALL:DETAILED'

def WallExterior(idf, **kwargs: Unpack[WallExteriorType]):
    """"helper for WallExterior"""
    return idf.newidfobject('WALL:EXTERIOR', **kwargs)
class WallExteriorMeta:
    idf_name = 'WALL:EXTERIOR'

def WallInterzone(idf, **kwargs: Unpack[WallInterzoneType]):
    """"helper for WallInterzone"""
    return idf.newidfobject('WALL:INTERZONE', **kwargs)
class WallInterzoneMeta:
    idf_name = 'WALL:INTERZONE'

def WallUnderground(idf, **kwargs: Unpack[WallUndergroundType]):
    """"helper for WallUnderground"""
    return idf.newidfobject('WALL:UNDERGROUND', **kwargs)
class WallUndergroundMeta:
    idf_name = 'WALL:UNDERGROUND'

def WaterheaterHeatpumpPumpedcondenser(idf, **kwargs: Unpack[WaterheaterHeatpumpPumpedcondenserType]):
    """"helper for WaterheaterHeatpumpPumpedcondenser"""
    return idf.newidfobject('WATERHEATER:HEATPUMP:PUMPEDCONDENSER', **kwargs)
class WaterheaterHeatpumpPumpedcondenserMeta:
    idf_name = 'WATERHEATER:HEATPUMP:PUMPEDCONDENSER'

def WaterheaterHeatpumpWrappedcondenser(idf, **kwargs: Unpack[WaterheaterHeatpumpWrappedcondenserType]):
    """"helper for WaterheaterHeatpumpWrappedcondenser"""
    return idf.newidfobject('WATERHEATER:HEATPUMP:WRAPPEDCONDENSER', **kwargs)
class WaterheaterHeatpumpWrappedcondenserMeta:
    idf_name = 'WATERHEATER:HEATPUMP:WRAPPEDCONDENSER'

def WaterheaterMixed(idf, **kwargs: Unpack[WaterheaterMixedType]):
    """"helper for WaterheaterMixed"""
    return idf.newidfobject('WATERHEATER:MIXED', **kwargs)
class WaterheaterMixedMeta:
    idf_name = 'WATERHEATER:MIXED'

def WaterheaterSizing(idf, **kwargs: Unpack[WaterheaterSizingType]):
    """"helper for WaterheaterSizing"""
    return idf.newidfobject('WATERHEATER:SIZING', **kwargs)
class WaterheaterSizingMeta:
    idf_name = 'WATERHEATER:SIZING'

def WaterheaterStratified(idf, **kwargs: Unpack[WaterheaterStratifiedType]):
    """"helper for WaterheaterStratified"""
    return idf.newidfobject('WATERHEATER:STRATIFIED', **kwargs)
class WaterheaterStratifiedMeta:
    idf_name = 'WATERHEATER:STRATIFIED'

def WateruseConnections(idf, **kwargs: Unpack[WateruseConnectionsType]):
    """"helper for WateruseConnections"""
    return idf.newidfobject('WATERUSE:CONNECTIONS', **kwargs)
class WateruseConnectionsMeta:
    idf_name = 'WATERUSE:CONNECTIONS'

def WateruseEquipment(idf, **kwargs: Unpack[WateruseEquipmentType]):
    """"helper for WateruseEquipment"""
    return idf.newidfobject('WATERUSE:EQUIPMENT', **kwargs)
class WateruseEquipmentMeta:
    idf_name = 'WATERUSE:EQUIPMENT'

def WateruseRaincollector(idf, **kwargs: Unpack[WateruseRaincollectorType]):
    """"helper for WateruseRaincollector"""
    return idf.newidfobject('WATERUSE:RAINCOLLECTOR', **kwargs)
class WateruseRaincollectorMeta:
    idf_name = 'WATERUSE:RAINCOLLECTOR'

def WateruseStorage(idf, **kwargs: Unpack[WateruseStorageType]):
    """"helper for WateruseStorage"""
    return idf.newidfobject('WATERUSE:STORAGE', **kwargs)
class WateruseStorageMeta:
    idf_name = 'WATERUSE:STORAGE'

def WateruseWell(idf, **kwargs: Unpack[WateruseWellType]):
    """"helper for WateruseWell"""
    return idf.newidfobject('WATERUSE:WELL', **kwargs)
class WateruseWellMeta:
    idf_name = 'WATERUSE:WELL'

def WeatherpropertySkytemperature(idf, **kwargs: Unpack[WeatherpropertySkytemperatureType]):
    """"helper for WeatherpropertySkytemperature"""
    return idf.newidfobject('WEATHERPROPERTY:SKYTEMPERATURE', **kwargs)
class WeatherpropertySkytemperatureMeta:
    idf_name = 'WEATHERPROPERTY:SKYTEMPERATURE'

def Window(idf, **kwargs: Unpack[WindowType]):
    """"helper for Window"""
    return idf.newidfobject('WINDOW', **kwargs)
class WindowMeta:
    idf_name = 'WINDOW'

def WindowInterzone(idf, **kwargs: Unpack[WindowInterzoneType]):
    """"helper for WindowInterzone"""
    return idf.newidfobject('WINDOW:INTERZONE', **kwargs)
class WindowInterzoneMeta:
    idf_name = 'WINDOW:INTERZONE'

def WindowgapDeflectionstate(idf, **kwargs: Unpack[WindowgapDeflectionstateType]):
    """"helper for WindowgapDeflectionstate"""
    return idf.newidfobject('WINDOWGAP:DEFLECTIONSTATE', **kwargs)
class WindowgapDeflectionstateMeta:
    idf_name = 'WINDOWGAP:DEFLECTIONSTATE'

def WindowgapSupportpillar(idf, **kwargs: Unpack[WindowgapSupportpillarType]):
    """"helper for WindowgapSupportpillar"""
    return idf.newidfobject('WINDOWGAP:SUPPORTPILLAR', **kwargs)
class WindowgapSupportpillarMeta:
    idf_name = 'WINDOWGAP:SUPPORTPILLAR'

def WindowmaterialBlind(idf, **kwargs: Unpack[WindowmaterialBlindType]):
    """"helper for WindowmaterialBlind"""
    return idf.newidfobject('WINDOWMATERIAL:BLIND', **kwargs)
class WindowmaterialBlindMeta:
    idf_name = 'WINDOWMATERIAL:BLIND'

def WindowmaterialBlindEquivalentlayer(idf, **kwargs: Unpack[WindowmaterialBlindEquivalentlayerType]):
    """"helper for WindowmaterialBlindEquivalentlayer"""
    return idf.newidfobject('WINDOWMATERIAL:BLIND:EQUIVALENTLAYER', **kwargs)
class WindowmaterialBlindEquivalentlayerMeta:
    idf_name = 'WINDOWMATERIAL:BLIND:EQUIVALENTLAYER'

def WindowmaterialComplexshade(idf, **kwargs: Unpack[WindowmaterialComplexshadeType]):
    """"helper for WindowmaterialComplexshade"""
    return idf.newidfobject('WINDOWMATERIAL:COMPLEXSHADE', **kwargs)
class WindowmaterialComplexshadeMeta:
    idf_name = 'WINDOWMATERIAL:COMPLEXSHADE'

def WindowmaterialDrapeEquivalentlayer(idf, **kwargs: Unpack[WindowmaterialDrapeEquivalentlayerType]):
    """"helper for WindowmaterialDrapeEquivalentlayer"""
    return idf.newidfobject('WINDOWMATERIAL:DRAPE:EQUIVALENTLAYER', **kwargs)
class WindowmaterialDrapeEquivalentlayerMeta:
    idf_name = 'WINDOWMATERIAL:DRAPE:EQUIVALENTLAYER'

def WindowmaterialGap(idf, **kwargs: Unpack[WindowmaterialGapType]):
    """"helper for WindowmaterialGap"""
    return idf.newidfobject('WINDOWMATERIAL:GAP', **kwargs)
class WindowmaterialGapMeta:
    idf_name = 'WINDOWMATERIAL:GAP'

def WindowmaterialGapEquivalentlayer(idf, **kwargs: Unpack[WindowmaterialGapEquivalentlayerType]):
    """"helper for WindowmaterialGapEquivalentlayer"""
    return idf.newidfobject('WINDOWMATERIAL:GAP:EQUIVALENTLAYER', **kwargs)
class WindowmaterialGapEquivalentlayerMeta:
    idf_name = 'WINDOWMATERIAL:GAP:EQUIVALENTLAYER'

def WindowmaterialGas(idf, **kwargs: Unpack[WindowmaterialGasType]):
    """"helper for WindowmaterialGas"""
    return idf.newidfobject('WINDOWMATERIAL:GAS', **kwargs)
class WindowmaterialGasMeta:
    idf_name = 'WINDOWMATERIAL:GAS'

def WindowmaterialGasmixture(idf, **kwargs: Unpack[WindowmaterialGasmixtureType]):
    """"helper for WindowmaterialGasmixture"""
    return idf.newidfobject('WINDOWMATERIAL:GASMIXTURE', **kwargs)
class WindowmaterialGasmixtureMeta:
    idf_name = 'WINDOWMATERIAL:GASMIXTURE'

def WindowmaterialGlazing(idf, **kwargs: Unpack[WindowmaterialGlazingType]):
    """"helper for WindowmaterialGlazing"""
    return idf.newidfobject('WINDOWMATERIAL:GLAZING', **kwargs)
class WindowmaterialGlazingMeta:
    idf_name = 'WINDOWMATERIAL:GLAZING'

def WindowmaterialGlazingEquivalentlayer(idf, **kwargs: Unpack[WindowmaterialGlazingEquivalentlayerType]):
    """"helper for WindowmaterialGlazingEquivalentlayer"""
    return idf.newidfobject('WINDOWMATERIAL:GLAZING:EQUIVALENTLAYER', **kwargs)
class WindowmaterialGlazingEquivalentlayerMeta:
    idf_name = 'WINDOWMATERIAL:GLAZING:EQUIVALENTLAYER'

def WindowmaterialGlazingRefractionextinctionmethod(idf, **kwargs: Unpack[WindowmaterialGlazingRefractionextinctionmethodType]):
    """"helper for WindowmaterialGlazingRefractionextinctionmethod"""
    return idf.newidfobject('WINDOWMATERIAL:GLAZING:REFRACTIONEXTINCTIONMETHOD', **kwargs)
class WindowmaterialGlazingRefractionextinctionmethodMeta:
    idf_name = 'WINDOWMATERIAL:GLAZING:REFRACTIONEXTINCTIONMETHOD'

def WindowmaterialGlazinggroupThermochromic(idf, **kwargs: Unpack[WindowmaterialGlazinggroupThermochromicType]):
    """"helper for WindowmaterialGlazinggroupThermochromic"""
    return idf.newidfobject('WINDOWMATERIAL:GLAZINGGROUP:THERMOCHROMIC', **kwargs)
class WindowmaterialGlazinggroupThermochromicMeta:
    idf_name = 'WINDOWMATERIAL:GLAZINGGROUP:THERMOCHROMIC'

def WindowmaterialScreen(idf, **kwargs: Unpack[WindowmaterialScreenType]):
    """"helper for WindowmaterialScreen"""
    return idf.newidfobject('WINDOWMATERIAL:SCREEN', **kwargs)
class WindowmaterialScreenMeta:
    idf_name = 'WINDOWMATERIAL:SCREEN'

def WindowmaterialScreenEquivalentlayer(idf, **kwargs: Unpack[WindowmaterialScreenEquivalentlayerType]):
    """"helper for WindowmaterialScreenEquivalentlayer"""
    return idf.newidfobject('WINDOWMATERIAL:SCREEN:EQUIVALENTLAYER', **kwargs)
class WindowmaterialScreenEquivalentlayerMeta:
    idf_name = 'WINDOWMATERIAL:SCREEN:EQUIVALENTLAYER'

def WindowmaterialShade(idf, **kwargs: Unpack[WindowmaterialShadeType]):
    """"helper for WindowmaterialShade"""
    return idf.newidfobject('WINDOWMATERIAL:SHADE', **kwargs)
class WindowmaterialShadeMeta:
    idf_name = 'WINDOWMATERIAL:SHADE'

def WindowmaterialShadeEquivalentlayer(idf, **kwargs: Unpack[WindowmaterialShadeEquivalentlayerType]):
    """"helper for WindowmaterialShadeEquivalentlayer"""
    return idf.newidfobject('WINDOWMATERIAL:SHADE:EQUIVALENTLAYER', **kwargs)
class WindowmaterialShadeEquivalentlayerMeta:
    idf_name = 'WINDOWMATERIAL:SHADE:EQUIVALENTLAYER'

def WindowmaterialSimpleglazingsystem(idf, **kwargs: Unpack[WindowmaterialSimpleglazingsystemType]):
    """"helper for WindowmaterialSimpleglazingsystem"""
    return idf.newidfobject('WINDOWMATERIAL:SIMPLEGLAZINGSYSTEM', **kwargs)
class WindowmaterialSimpleglazingsystemMeta:
    idf_name = 'WINDOWMATERIAL:SIMPLEGLAZINGSYSTEM'

def WindowpropertyAirflowcontrol(idf, **kwargs: Unpack[WindowpropertyAirflowcontrolType]):
    """"helper for WindowpropertyAirflowcontrol"""
    return idf.newidfobject('WINDOWPROPERTY:AIRFLOWCONTROL', **kwargs)
class WindowpropertyAirflowcontrolMeta:
    idf_name = 'WINDOWPROPERTY:AIRFLOWCONTROL'

def WindowpropertyFrameanddivider(idf, **kwargs: Unpack[WindowpropertyFrameanddividerType]):
    """"helper for WindowpropertyFrameanddivider"""
    return idf.newidfobject('WINDOWPROPERTY:FRAMEANDDIVIDER', **kwargs)
class WindowpropertyFrameanddividerMeta:
    idf_name = 'WINDOWPROPERTY:FRAMEANDDIVIDER'

def WindowpropertyStormwindow(idf, **kwargs: Unpack[WindowpropertyStormwindowType]):
    """"helper for WindowpropertyStormwindow"""
    return idf.newidfobject('WINDOWPROPERTY:STORMWINDOW', **kwargs)
class WindowpropertyStormwindowMeta:
    idf_name = 'WINDOWPROPERTY:STORMWINDOW'

def Windowscalculationengine(idf, **kwargs: Unpack[WindowscalculationengineType]):
    """"helper for Windowscalculationengine"""
    return idf.newidfobject('WINDOWSCALCULATIONENGINE', **kwargs)
class WindowscalculationengineMeta:
    idf_name = 'WINDOWSCALCULATIONENGINE'

def Windowshadingcontrol(idf, **kwargs: Unpack[WindowshadingcontrolType]):
    """"helper for Windowshadingcontrol"""
    return idf.newidfobject('WINDOWSHADINGCONTROL', **kwargs)
class WindowshadingcontrolMeta:
    idf_name = 'WINDOWSHADINGCONTROL'

def WindowthermalmodelParams(idf, **kwargs: Unpack[WindowthermalmodelParamsType]):
    """"helper for WindowthermalmodelParams"""
    return idf.newidfobject('WINDOWTHERMALMODEL:PARAMS', **kwargs)
class WindowthermalmodelParamsMeta:
    idf_name = 'WINDOWTHERMALMODEL:PARAMS'

def Zone(idf, **kwargs: Unpack[ZoneType]):
    """"helper for Zone"""
    return idf.newidfobject('ZONE', **kwargs)
class ZoneMeta:
    idf_name = 'ZONE'

def ZoneairbalanceOutdoorair(idf, **kwargs: Unpack[ZoneairbalanceOutdoorairType]):
    """"helper for ZoneairbalanceOutdoorair"""
    return idf.newidfobject('ZONEAIRBALANCE:OUTDOORAIR', **kwargs)
class ZoneairbalanceOutdoorairMeta:
    idf_name = 'ZONEAIRBALANCE:OUTDOORAIR'

def Zoneaircontaminantbalance(idf, **kwargs: Unpack[ZoneaircontaminantbalanceType]):
    """"helper for Zoneaircontaminantbalance"""
    return idf.newidfobject('ZONEAIRCONTAMINANTBALANCE', **kwargs)
class ZoneaircontaminantbalanceMeta:
    idf_name = 'ZONEAIRCONTAMINANTBALANCE'

def Zoneairheatbalancealgorithm(idf, **kwargs: Unpack[ZoneairheatbalancealgorithmType]):
    """"helper for Zoneairheatbalancealgorithm"""
    return idf.newidfobject('ZONEAIRHEATBALANCEALGORITHM', **kwargs)
class ZoneairheatbalancealgorithmMeta:
    idf_name = 'ZONEAIRHEATBALANCEALGORITHM'

def Zoneairmassflowconservation(idf, **kwargs: Unpack[ZoneairmassflowconservationType]):
    """"helper for Zoneairmassflowconservation"""
    return idf.newidfobject('ZONEAIRMASSFLOWCONSERVATION', **kwargs)
class ZoneairmassflowconservationMeta:
    idf_name = 'ZONEAIRMASSFLOWCONSERVATION'

def ZonebaseboardOutdoortemperaturecontrolled(idf, **kwargs: Unpack[ZonebaseboardOutdoortemperaturecontrolledType]):
    """"helper for ZonebaseboardOutdoortemperaturecontrolled"""
    return idf.newidfobject('ZONEBASEBOARD:OUTDOORTEMPERATURECONTROLLED', **kwargs)
class ZonebaseboardOutdoortemperaturecontrolledMeta:
    idf_name = 'ZONEBASEBOARD:OUTDOORTEMPERATURECONTROLLED'

def ZonecapacitancemultiplierResearchspecial(idf, **kwargs: Unpack[ZonecapacitancemultiplierResearchspecialType]):
    """"helper for ZonecapacitancemultiplierResearchspecial"""
    return idf.newidfobject('ZONECAPACITANCEMULTIPLIER:RESEARCHSPECIAL', **kwargs)
class ZonecapacitancemultiplierResearchspecialMeta:
    idf_name = 'ZONECAPACITANCEMULTIPLIER:RESEARCHSPECIAL'

def ZonecontaminantsourceandsinkCarbondioxide(idf, **kwargs: Unpack[ZonecontaminantsourceandsinkCarbondioxideType]):
    """"helper for ZonecontaminantsourceandsinkCarbondioxide"""
    return idf.newidfobject('ZONECONTAMINANTSOURCEANDSINK:CARBONDIOXIDE', **kwargs)
class ZonecontaminantsourceandsinkCarbondioxideMeta:
    idf_name = 'ZONECONTAMINANTSOURCEANDSINK:CARBONDIOXIDE'

def ZonecontaminantsourceandsinkGenericConstant(idf, **kwargs: Unpack[ZonecontaminantsourceandsinkGenericConstantType]):
    """"helper for ZonecontaminantsourceandsinkGenericConstant"""
    return idf.newidfobject('ZONECONTAMINANTSOURCEANDSINK:GENERIC:CONSTANT', **kwargs)
class ZonecontaminantsourceandsinkGenericConstantMeta:
    idf_name = 'ZONECONTAMINANTSOURCEANDSINK:GENERIC:CONSTANT'

def ZonecontaminantsourceandsinkGenericCutoffmodel(idf, **kwargs: Unpack[ZonecontaminantsourceandsinkGenericCutoffmodelType]):
    """"helper for ZonecontaminantsourceandsinkGenericCutoffmodel"""
    return idf.newidfobject('ZONECONTAMINANTSOURCEANDSINK:GENERIC:CUTOFFMODEL', **kwargs)
class ZonecontaminantsourceandsinkGenericCutoffmodelMeta:
    idf_name = 'ZONECONTAMINANTSOURCEANDSINK:GENERIC:CUTOFFMODEL'

def ZonecontaminantsourceandsinkGenericDecaysource(idf, **kwargs: Unpack[ZonecontaminantsourceandsinkGenericDecaysourceType]):
    """"helper for ZonecontaminantsourceandsinkGenericDecaysource"""
    return idf.newidfobject('ZONECONTAMINANTSOURCEANDSINK:GENERIC:DECAYSOURCE', **kwargs)
class ZonecontaminantsourceandsinkGenericDecaysourceMeta:
    idf_name = 'ZONECONTAMINANTSOURCEANDSINK:GENERIC:DECAYSOURCE'

def ZonecontaminantsourceandsinkGenericDepositionratesink(idf, **kwargs: Unpack[ZonecontaminantsourceandsinkGenericDepositionratesinkType]):
    """"helper for ZonecontaminantsourceandsinkGenericDepositionratesink"""
    return idf.newidfobject('ZONECONTAMINANTSOURCEANDSINK:GENERIC:DEPOSITIONRATESINK', **kwargs)
class ZonecontaminantsourceandsinkGenericDepositionratesinkMeta:
    idf_name = 'ZONECONTAMINANTSOURCEANDSINK:GENERIC:DEPOSITIONRATESINK'

def ZonecontrolContaminantcontroller(idf, **kwargs: Unpack[ZonecontrolContaminantcontrollerType]):
    """"helper for ZonecontrolContaminantcontroller"""
    return idf.newidfobject('ZONECONTROL:CONTAMINANTCONTROLLER', **kwargs)
class ZonecontrolContaminantcontrollerMeta:
    idf_name = 'ZONECONTROL:CONTAMINANTCONTROLLER'

def ZonecontrolHumidistat(idf, **kwargs: Unpack[ZonecontrolHumidistatType]):
    """"helper for ZonecontrolHumidistat"""
    return idf.newidfobject('ZONECONTROL:HUMIDISTAT', **kwargs)
class ZonecontrolHumidistatMeta:
    idf_name = 'ZONECONTROL:HUMIDISTAT'

def ZonecontrolThermostat(idf, **kwargs: Unpack[ZonecontrolThermostatType]):
    """"helper for ZonecontrolThermostat"""
    return idf.newidfobject('ZONECONTROL:THERMOSTAT', **kwargs)
class ZonecontrolThermostatMeta:
    idf_name = 'ZONECONTROL:THERMOSTAT'

def ZonecontrolThermostatOperativetemperature(idf, **kwargs: Unpack[ZonecontrolThermostatOperativetemperatureType]):
    """"helper for ZonecontrolThermostatOperativetemperature"""
    return idf.newidfobject('ZONECONTROL:THERMOSTAT:OPERATIVETEMPERATURE', **kwargs)
class ZonecontrolThermostatOperativetemperatureMeta:
    idf_name = 'ZONECONTROL:THERMOSTAT:OPERATIVETEMPERATURE'

def ZonecontrolThermostatStageddualsetpoint(idf, **kwargs: Unpack[ZonecontrolThermostatStageddualsetpointType]):
    """"helper for ZonecontrolThermostatStageddualsetpoint"""
    return idf.newidfobject('ZONECONTROL:THERMOSTAT:STAGEDDUALSETPOINT', **kwargs)
class ZonecontrolThermostatStageddualsetpointMeta:
    idf_name = 'ZONECONTROL:THERMOSTAT:STAGEDDUALSETPOINT'

def ZonecontrolThermostatTemperatureandhumidity(idf, **kwargs: Unpack[ZonecontrolThermostatTemperatureandhumidityType]):
    """"helper for ZonecontrolThermostatTemperatureandhumidity"""
    return idf.newidfobject('ZONECONTROL:THERMOSTAT:TEMPERATUREANDHUMIDITY', **kwargs)
class ZonecontrolThermostatTemperatureandhumidityMeta:
    idf_name = 'ZONECONTROL:THERMOSTAT:TEMPERATUREANDHUMIDITY'

def ZonecontrolThermostatThermalcomfort(idf, **kwargs: Unpack[ZonecontrolThermostatThermalcomfortType]):
    """"helper for ZonecontrolThermostatThermalcomfort"""
    return idf.newidfobject('ZONECONTROL:THERMOSTAT:THERMALCOMFORT', **kwargs)
class ZonecontrolThermostatThermalcomfortMeta:
    idf_name = 'ZONECONTROL:THERMOSTAT:THERMALCOMFORT'

def ZonecooltowerShower(idf, **kwargs: Unpack[ZonecooltowerShowerType]):
    """"helper for ZonecooltowerShower"""
    return idf.newidfobject('ZONECOOLTOWER:SHOWER', **kwargs)
class ZonecooltowerShowerMeta:
    idf_name = 'ZONECOOLTOWER:SHOWER'

def Zonecrossmixing(idf, **kwargs: Unpack[ZonecrossmixingType]):
    """"helper for Zonecrossmixing"""
    return idf.newidfobject('ZONECROSSMIXING', **kwargs)
class ZonecrossmixingMeta:
    idf_name = 'ZONECROSSMIXING'

def Zoneearthtube(idf, **kwargs: Unpack[ZoneearthtubeType]):
    """"helper for Zoneearthtube"""
    return idf.newidfobject('ZONEEARTHTUBE', **kwargs)
class ZoneearthtubeMeta:
    idf_name = 'ZONEEARTHTUBE'

def ZoneearthtubeParameters(idf, **kwargs: Unpack[ZoneearthtubeParametersType]):
    """"helper for ZoneearthtubeParameters"""
    return idf.newidfobject('ZONEEARTHTUBE:PARAMETERS', **kwargs)
class ZoneearthtubeParametersMeta:
    idf_name = 'ZONEEARTHTUBE:PARAMETERS'

def Zonegroup(idf, **kwargs: Unpack[ZonegroupType]):
    """"helper for Zonegroup"""
    return idf.newidfobject('ZONEGROUP', **kwargs)
class ZonegroupMeta:
    idf_name = 'ZONEGROUP'

def ZonehvacAirdistributionunit(idf, **kwargs: Unpack[ZonehvacAirdistributionunitType]):
    """"helper for ZonehvacAirdistributionunit"""
    return idf.newidfobject('ZONEHVAC:AIRDISTRIBUTIONUNIT', **kwargs)
class ZonehvacAirdistributionunitMeta:
    idf_name = 'ZONEHVAC:AIRDISTRIBUTIONUNIT'

def ZonehvacBaseboardConvectiveElectric(idf, **kwargs: Unpack[ZonehvacBaseboardConvectiveElectricType]):
    """"helper for ZonehvacBaseboardConvectiveElectric"""
    return idf.newidfobject('ZONEHVAC:BASEBOARD:CONVECTIVE:ELECTRIC', **kwargs)
class ZonehvacBaseboardConvectiveElectricMeta:
    idf_name = 'ZONEHVAC:BASEBOARD:CONVECTIVE:ELECTRIC'

def ZonehvacBaseboardConvectiveWater(idf, **kwargs: Unpack[ZonehvacBaseboardConvectiveWaterType]):
    """"helper for ZonehvacBaseboardConvectiveWater"""
    return idf.newidfobject('ZONEHVAC:BASEBOARD:CONVECTIVE:WATER', **kwargs)
class ZonehvacBaseboardConvectiveWaterMeta:
    idf_name = 'ZONEHVAC:BASEBOARD:CONVECTIVE:WATER'

def ZonehvacBaseboardRadiantconvectiveElectric(idf, **kwargs: Unpack[ZonehvacBaseboardRadiantconvectiveElectricType]):
    """"helper for ZonehvacBaseboardRadiantconvectiveElectric"""
    return idf.newidfobject('ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:ELECTRIC', **kwargs)
class ZonehvacBaseboardRadiantconvectiveElectricMeta:
    idf_name = 'ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:ELECTRIC'

def ZonehvacBaseboardRadiantconvectiveSteam(idf, **kwargs: Unpack[ZonehvacBaseboardRadiantconvectiveSteamType]):
    """"helper for ZonehvacBaseboardRadiantconvectiveSteam"""
    return idf.newidfobject('ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:STEAM', **kwargs)
class ZonehvacBaseboardRadiantconvectiveSteamMeta:
    idf_name = 'ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:STEAM'

def ZonehvacBaseboardRadiantconvectiveSteamDesign(idf, **kwargs: Unpack[ZonehvacBaseboardRadiantconvectiveSteamDesignType]):
    """"helper for ZonehvacBaseboardRadiantconvectiveSteamDesign"""
    return idf.newidfobject('ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:STEAM:DESIGN', **kwargs)
class ZonehvacBaseboardRadiantconvectiveSteamDesignMeta:
    idf_name = 'ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:STEAM:DESIGN'

def ZonehvacBaseboardRadiantconvectiveWater(idf, **kwargs: Unpack[ZonehvacBaseboardRadiantconvectiveWaterType]):
    """"helper for ZonehvacBaseboardRadiantconvectiveWater"""
    return idf.newidfobject('ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:WATER', **kwargs)
class ZonehvacBaseboardRadiantconvectiveWaterMeta:
    idf_name = 'ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:WATER'

def ZonehvacBaseboardRadiantconvectiveWaterDesign(idf, **kwargs: Unpack[ZonehvacBaseboardRadiantconvectiveWaterDesignType]):
    """"helper for ZonehvacBaseboardRadiantconvectiveWaterDesign"""
    return idf.newidfobject('ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:WATER:DESIGN', **kwargs)
class ZonehvacBaseboardRadiantconvectiveWaterDesignMeta:
    idf_name = 'ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:WATER:DESIGN'

def ZonehvacCoolingpanelRadiantconvectiveWater(idf, **kwargs: Unpack[ZonehvacCoolingpanelRadiantconvectiveWaterType]):
    """"helper for ZonehvacCoolingpanelRadiantconvectiveWater"""
    return idf.newidfobject('ZONEHVAC:COOLINGPANEL:RADIANTCONVECTIVE:WATER', **kwargs)
class ZonehvacCoolingpanelRadiantconvectiveWaterMeta:
    idf_name = 'ZONEHVAC:COOLINGPANEL:RADIANTCONVECTIVE:WATER'

def ZonehvacDehumidifierDx(idf, **kwargs: Unpack[ZonehvacDehumidifierDxType]):
    """"helper for ZonehvacDehumidifierDx"""
    return idf.newidfobject('ZONEHVAC:DEHUMIDIFIER:DX', **kwargs)
class ZonehvacDehumidifierDxMeta:
    idf_name = 'ZONEHVAC:DEHUMIDIFIER:DX'

def ZonehvacEnergyrecoveryventilator(idf, **kwargs: Unpack[ZonehvacEnergyrecoveryventilatorType]):
    """"helper for ZonehvacEnergyrecoveryventilator"""
    return idf.newidfobject('ZONEHVAC:ENERGYRECOVERYVENTILATOR', **kwargs)
class ZonehvacEnergyrecoveryventilatorMeta:
    idf_name = 'ZONEHVAC:ENERGYRECOVERYVENTILATOR'

def ZonehvacEnergyrecoveryventilatorController(idf, **kwargs: Unpack[ZonehvacEnergyrecoveryventilatorControllerType]):
    """"helper for ZonehvacEnergyrecoveryventilatorController"""
    return idf.newidfobject('ZONEHVAC:ENERGYRECOVERYVENTILATOR:CONTROLLER', **kwargs)
class ZonehvacEnergyrecoveryventilatorControllerMeta:
    idf_name = 'ZONEHVAC:ENERGYRECOVERYVENTILATOR:CONTROLLER'

def ZonehvacEquipmentconnections(idf, **kwargs: Unpack[ZonehvacEquipmentconnectionsType]):
    """"helper for ZonehvacEquipmentconnections"""
    return idf.newidfobject('ZONEHVAC:EQUIPMENTCONNECTIONS', **kwargs)
class ZonehvacEquipmentconnectionsMeta:
    idf_name = 'ZONEHVAC:EQUIPMENTCONNECTIONS'

def ZonehvacEquipmentlist(idf, **kwargs: Unpack[ZonehvacEquipmentlistType]):
    """"helper for ZonehvacEquipmentlist"""
    return idf.newidfobject('ZONEHVAC:EQUIPMENTLIST', **kwargs)
class ZonehvacEquipmentlistMeta:
    idf_name = 'ZONEHVAC:EQUIPMENTLIST'

def ZonehvacEvaporativecoolerunit(idf, **kwargs: Unpack[ZonehvacEvaporativecoolerunitType]):
    """"helper for ZonehvacEvaporativecoolerunit"""
    return idf.newidfobject('ZONEHVAC:EVAPORATIVECOOLERUNIT', **kwargs)
class ZonehvacEvaporativecoolerunitMeta:
    idf_name = 'ZONEHVAC:EVAPORATIVECOOLERUNIT'

def ZonehvacExhaustcontrol(idf, **kwargs: Unpack[ZonehvacExhaustcontrolType]):
    """"helper for ZonehvacExhaustcontrol"""
    return idf.newidfobject('ZONEHVAC:EXHAUSTCONTROL', **kwargs)
class ZonehvacExhaustcontrolMeta:
    idf_name = 'ZONEHVAC:EXHAUSTCONTROL'

def ZonehvacForcedairUserdefined(idf, **kwargs: Unpack[ZonehvacForcedairUserdefinedType]):
    """"helper for ZonehvacForcedairUserdefined"""
    return idf.newidfobject('ZONEHVAC:FORCEDAIR:USERDEFINED', **kwargs)
class ZonehvacForcedairUserdefinedMeta:
    idf_name = 'ZONEHVAC:FORCEDAIR:USERDEFINED'

def ZonehvacFourpipefancoil(idf, **kwargs: Unpack[ZonehvacFourpipefancoilType]):
    """"helper for ZonehvacFourpipefancoil"""
    return idf.newidfobject('ZONEHVAC:FOURPIPEFANCOIL', **kwargs)
class ZonehvacFourpipefancoilMeta:
    idf_name = 'ZONEHVAC:FOURPIPEFANCOIL'

def ZonehvacHightemperatureradiant(idf, **kwargs: Unpack[ZonehvacHightemperatureradiantType]):
    """"helper for ZonehvacHightemperatureradiant"""
    return idf.newidfobject('ZONEHVAC:HIGHTEMPERATURERADIANT', **kwargs)
class ZonehvacHightemperatureradiantMeta:
    idf_name = 'ZONEHVAC:HIGHTEMPERATURERADIANT'

def ZonehvacHybridunitaryhvac(idf, **kwargs: Unpack[ZonehvacHybridunitaryhvacType]):
    """"helper for ZonehvacHybridunitaryhvac"""
    return idf.newidfobject('ZONEHVAC:HYBRIDUNITARYHVAC', **kwargs)
class ZonehvacHybridunitaryhvacMeta:
    idf_name = 'ZONEHVAC:HYBRIDUNITARYHVAC'

def ZonehvacIdealloadsairsystem(idf, **kwargs: Unpack[ZonehvacIdealloadsairsystemType]):
    """"helper for ZonehvacIdealloadsairsystem"""
    return idf.newidfobject('ZONEHVAC:IDEALLOADSAIRSYSTEM', **kwargs)
class ZonehvacIdealloadsairsystemMeta:
    idf_name = 'ZONEHVAC:IDEALLOADSAIRSYSTEM'

def ZonehvacLowtemperatureradiantConstantflow(idf, **kwargs: Unpack[ZonehvacLowtemperatureradiantConstantflowType]):
    """"helper for ZonehvacLowtemperatureradiantConstantflow"""
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:CONSTANTFLOW', **kwargs)
class ZonehvacLowtemperatureradiantConstantflowMeta:
    idf_name = 'ZONEHVAC:LOWTEMPERATURERADIANT:CONSTANTFLOW'

def ZonehvacLowtemperatureradiantConstantflowDesign(idf, **kwargs: Unpack[ZonehvacLowtemperatureradiantConstantflowDesignType]):
    """"helper for ZonehvacLowtemperatureradiantConstantflowDesign"""
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:CONSTANTFLOW:DESIGN', **kwargs)
class ZonehvacLowtemperatureradiantConstantflowDesignMeta:
    idf_name = 'ZONEHVAC:LOWTEMPERATURERADIANT:CONSTANTFLOW:DESIGN'

def ZonehvacLowtemperatureradiantElectric(idf, **kwargs: Unpack[ZonehvacLowtemperatureradiantElectricType]):
    """"helper for ZonehvacLowtemperatureradiantElectric"""
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:ELECTRIC', **kwargs)
class ZonehvacLowtemperatureradiantElectricMeta:
    idf_name = 'ZONEHVAC:LOWTEMPERATURERADIANT:ELECTRIC'

def ZonehvacLowtemperatureradiantSurfacegroup(idf, **kwargs: Unpack[ZonehvacLowtemperatureradiantSurfacegroupType]):
    """"helper for ZonehvacLowtemperatureradiantSurfacegroup"""
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:SURFACEGROUP', **kwargs)
class ZonehvacLowtemperatureradiantSurfacegroupMeta:
    idf_name = 'ZONEHVAC:LOWTEMPERATURERADIANT:SURFACEGROUP'

def ZonehvacLowtemperatureradiantVariableflow(idf, **kwargs: Unpack[ZonehvacLowtemperatureradiantVariableflowType]):
    """"helper for ZonehvacLowtemperatureradiantVariableflow"""
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:VARIABLEFLOW', **kwargs)
class ZonehvacLowtemperatureradiantVariableflowMeta:
    idf_name = 'ZONEHVAC:LOWTEMPERATURERADIANT:VARIABLEFLOW'

def ZonehvacLowtemperatureradiantVariableflowDesign(idf, **kwargs: Unpack[ZonehvacLowtemperatureradiantVariableflowDesignType]):
    """"helper for ZonehvacLowtemperatureradiantVariableflowDesign"""
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:VARIABLEFLOW:DESIGN', **kwargs)
class ZonehvacLowtemperatureradiantVariableflowDesignMeta:
    idf_name = 'ZONEHVAC:LOWTEMPERATURERADIANT:VARIABLEFLOW:DESIGN'

def ZonehvacOutdoorairunit(idf, **kwargs: Unpack[ZonehvacOutdoorairunitType]):
    """"helper for ZonehvacOutdoorairunit"""
    return idf.newidfobject('ZONEHVAC:OUTDOORAIRUNIT', **kwargs)
class ZonehvacOutdoorairunitMeta:
    idf_name = 'ZONEHVAC:OUTDOORAIRUNIT'

def ZonehvacOutdoorairunitEquipmentlist(idf, **kwargs: Unpack[ZonehvacOutdoorairunitEquipmentlistType]):
    """"helper for ZonehvacOutdoorairunitEquipmentlist"""
    return idf.newidfobject('ZONEHVAC:OUTDOORAIRUNIT:EQUIPMENTLIST', **kwargs)
class ZonehvacOutdoorairunitEquipmentlistMeta:
    idf_name = 'ZONEHVAC:OUTDOORAIRUNIT:EQUIPMENTLIST'

def ZonehvacPackagedterminalairconditioner(idf, **kwargs: Unpack[ZonehvacPackagedterminalairconditionerType]):
    """"helper for ZonehvacPackagedterminalairconditioner"""
    return idf.newidfobject('ZONEHVAC:PACKAGEDTERMINALAIRCONDITIONER', **kwargs)
class ZonehvacPackagedterminalairconditionerMeta:
    idf_name = 'ZONEHVAC:PACKAGEDTERMINALAIRCONDITIONER'

def ZonehvacPackagedterminalheatpump(idf, **kwargs: Unpack[ZonehvacPackagedterminalheatpumpType]):
    """"helper for ZonehvacPackagedterminalheatpump"""
    return idf.newidfobject('ZONEHVAC:PACKAGEDTERMINALHEATPUMP', **kwargs)
class ZonehvacPackagedterminalheatpumpMeta:
    idf_name = 'ZONEHVAC:PACKAGEDTERMINALHEATPUMP'

def ZonehvacRefrigerationchillerset(idf, **kwargs: Unpack[ZonehvacRefrigerationchillersetType]):
    """"helper for ZonehvacRefrigerationchillerset"""
    return idf.newidfobject('ZONEHVAC:REFRIGERATIONCHILLERSET', **kwargs)
class ZonehvacRefrigerationchillersetMeta:
    idf_name = 'ZONEHVAC:REFRIGERATIONCHILLERSET'

def ZonehvacTerminalunitVariablerefrigerantflow(idf, **kwargs: Unpack[ZonehvacTerminalunitVariablerefrigerantflowType]):
    """"helper for ZonehvacTerminalunitVariablerefrigerantflow"""
    return idf.newidfobject('ZONEHVAC:TERMINALUNIT:VARIABLEREFRIGERANTFLOW', **kwargs)
class ZonehvacTerminalunitVariablerefrigerantflowMeta:
    idf_name = 'ZONEHVAC:TERMINALUNIT:VARIABLEREFRIGERANTFLOW'

def ZonehvacUnitheater(idf, **kwargs: Unpack[ZonehvacUnitheaterType]):
    """"helper for ZonehvacUnitheater"""
    return idf.newidfobject('ZONEHVAC:UNITHEATER', **kwargs)
class ZonehvacUnitheaterMeta:
    idf_name = 'ZONEHVAC:UNITHEATER'

def ZonehvacUnitventilator(idf, **kwargs: Unpack[ZonehvacUnitventilatorType]):
    """"helper for ZonehvacUnitventilator"""
    return idf.newidfobject('ZONEHVAC:UNITVENTILATOR', **kwargs)
class ZonehvacUnitventilatorMeta:
    idf_name = 'ZONEHVAC:UNITVENTILATOR'

def ZonehvacVentilatedslab(idf, **kwargs: Unpack[ZonehvacVentilatedslabType]):
    """"helper for ZonehvacVentilatedslab"""
    return idf.newidfobject('ZONEHVAC:VENTILATEDSLAB', **kwargs)
class ZonehvacVentilatedslabMeta:
    idf_name = 'ZONEHVAC:VENTILATEDSLAB'

def ZonehvacVentilatedslabSlabgroup(idf, **kwargs: Unpack[ZonehvacVentilatedslabSlabgroupType]):
    """"helper for ZonehvacVentilatedslabSlabgroup"""
    return idf.newidfobject('ZONEHVAC:VENTILATEDSLAB:SLABGROUP', **kwargs)
class ZonehvacVentilatedslabSlabgroupMeta:
    idf_name = 'ZONEHVAC:VENTILATEDSLAB:SLABGROUP'

def ZonehvacWatertoairheatpump(idf, **kwargs: Unpack[ZonehvacWatertoairheatpumpType]):
    """"helper for ZonehvacWatertoairheatpump"""
    return idf.newidfobject('ZONEHVAC:WATERTOAIRHEATPUMP', **kwargs)
class ZonehvacWatertoairheatpumpMeta:
    idf_name = 'ZONEHVAC:WATERTOAIRHEATPUMP'

def ZonehvacWindowairconditioner(idf, **kwargs: Unpack[ZonehvacWindowairconditionerType]):
    """"helper for ZonehvacWindowairconditioner"""
    return idf.newidfobject('ZONEHVAC:WINDOWAIRCONDITIONER', **kwargs)
class ZonehvacWindowairconditionerMeta:
    idf_name = 'ZONEHVAC:WINDOWAIRCONDITIONER'

def ZoneinfiltrationDesignflowrate(idf, **kwargs: Unpack[ZoneinfiltrationDesignflowrateType]):
    """"helper for ZoneinfiltrationDesignflowrate"""
    return idf.newidfobject('ZONEINFILTRATION:DESIGNFLOWRATE', **kwargs)
class ZoneinfiltrationDesignflowrateMeta:
    idf_name = 'ZONEINFILTRATION:DESIGNFLOWRATE'

def ZoneinfiltrationEffectiveleakagearea(idf, **kwargs: Unpack[ZoneinfiltrationEffectiveleakageareaType]):
    """"helper for ZoneinfiltrationEffectiveleakagearea"""
    return idf.newidfobject('ZONEINFILTRATION:EFFECTIVELEAKAGEAREA', **kwargs)
class ZoneinfiltrationEffectiveleakageareaMeta:
    idf_name = 'ZONEINFILTRATION:EFFECTIVELEAKAGEAREA'

def ZoneinfiltrationFlowcoefficient(idf, **kwargs: Unpack[ZoneinfiltrationFlowcoefficientType]):
    """"helper for ZoneinfiltrationFlowcoefficient"""
    return idf.newidfobject('ZONEINFILTRATION:FLOWCOEFFICIENT', **kwargs)
class ZoneinfiltrationFlowcoefficientMeta:
    idf_name = 'ZONEINFILTRATION:FLOWCOEFFICIENT'

def Zonelist(idf, **kwargs: Unpack[ZonelistType]):
    """"helper for Zonelist"""
    return idf.newidfobject('ZONELIST', **kwargs)
class ZonelistMeta:
    idf_name = 'ZONELIST'

def Zonemixing(idf, **kwargs: Unpack[ZonemixingType]):
    """"helper for Zonemixing"""
    return idf.newidfobject('ZONEMIXING', **kwargs)
class ZonemixingMeta:
    idf_name = 'ZONEMIXING'

def ZonepropertyLocalenvironment(idf, **kwargs: Unpack[ZonepropertyLocalenvironmentType]):
    """"helper for ZonepropertyLocalenvironment"""
    return idf.newidfobject('ZONEPROPERTY:LOCALENVIRONMENT', **kwargs)
class ZonepropertyLocalenvironmentMeta:
    idf_name = 'ZONEPROPERTY:LOCALENVIRONMENT'

def ZonepropertyUserviewfactorsBysurfacename(idf, **kwargs: Unpack[ZonepropertyUserviewfactorsBysurfacenameType]):
    """"helper for ZonepropertyUserviewfactorsBysurfacename"""
    return idf.newidfobject('ZONEPROPERTY:USERVIEWFACTORS:BYSURFACENAME', **kwargs)
class ZonepropertyUserviewfactorsBysurfacenameMeta:
    idf_name = 'ZONEPROPERTY:USERVIEWFACTORS:BYSURFACENAME'

def Zonerefrigerationdoormixing(idf, **kwargs: Unpack[ZonerefrigerationdoormixingType]):
    """"helper for Zonerefrigerationdoormixing"""
    return idf.newidfobject('ZONEREFRIGERATIONDOORMIXING', **kwargs)
class ZonerefrigerationdoormixingMeta:
    idf_name = 'ZONEREFRIGERATIONDOORMIXING'

def Zoneterminalunitlist(idf, **kwargs: Unpack[ZoneterminalunitlistType]):
    """"helper for Zoneterminalunitlist"""
    return idf.newidfobject('ZONETERMINALUNITLIST', **kwargs)
class ZoneterminalunitlistMeta:
    idf_name = 'ZONETERMINALUNITLIST'

def Zonethermalchimney(idf, **kwargs: Unpack[ZonethermalchimneyType]):
    """"helper for Zonethermalchimney"""
    return idf.newidfobject('ZONETHERMALCHIMNEY', **kwargs)
class ZonethermalchimneyMeta:
    idf_name = 'ZONETHERMALCHIMNEY'

def ZoneventilationDesignflowrate(idf, **kwargs: Unpack[ZoneventilationDesignflowrateType]):
    """"helper for ZoneventilationDesignflowrate"""
    return idf.newidfobject('ZONEVENTILATION:DESIGNFLOWRATE', **kwargs)
class ZoneventilationDesignflowrateMeta:
    idf_name = 'ZONEVENTILATION:DESIGNFLOWRATE'

def ZoneventilationWindandstackopenarea(idf, **kwargs: Unpack[ZoneventilationWindandstackopenareaType]):
    """"helper for ZoneventilationWindandstackopenarea"""
    return idf.newidfobject('ZONEVENTILATION:WINDANDSTACKOPENAREA', **kwargs)
class ZoneventilationWindandstackopenareaMeta:
    idf_name = 'ZONEVENTILATION:WINDANDSTACKOPENAREA'
