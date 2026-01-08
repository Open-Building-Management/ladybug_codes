from __future__ import annotations
from .idf_types import *

def AirconditionerVariablerefrigerantflow(idf, **kwargs: AirconditionerVariablerefrigerantflowType):
    return idf.newidfobject('AIRCONDITIONER:VARIABLEREFRIGERANTFLOW', **kwargs)

def AirconditionerVariablerefrigerantflowFluidtemperaturecontrol(idf, **kwargs: AirconditionerVariablerefrigerantflowFluidtemperaturecontrolType):
    return idf.newidfobject('AIRCONDITIONER:VARIABLEREFRIGERANTFLOW:FLUIDTEMPERATURECONTROL', **kwargs)

def AirconditionerVariablerefrigerantflowFluidtemperaturecontrolHr(idf, **kwargs: AirconditionerVariablerefrigerantflowFluidtemperaturecontrolHrType):
    return idf.newidfobject('AIRCONDITIONER:VARIABLEREFRIGERANTFLOW:FLUIDTEMPERATURECONTROL:HR', **kwargs)

def AirflownetworkDistributionComponentCoil(idf, **kwargs: AirflownetworkDistributionComponentCoilType):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:COIL', **kwargs)

def AirflownetworkDistributionComponentConstantpressuredrop(idf, **kwargs: AirflownetworkDistributionComponentConstantpressuredropType):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:CONSTANTPRESSUREDROP', **kwargs)

def AirflownetworkDistributionComponentDuct(idf, **kwargs: AirflownetworkDistributionComponentDuctType):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:DUCT', **kwargs)

def AirflownetworkDistributionComponentFan(idf, **kwargs: AirflownetworkDistributionComponentFanType):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:FAN', **kwargs)

def AirflownetworkDistributionComponentHeatexchanger(idf, **kwargs: AirflownetworkDistributionComponentHeatexchangerType):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:HEATEXCHANGER', **kwargs)

def AirflownetworkDistributionComponentLeak(idf, **kwargs: AirflownetworkDistributionComponentLeakType):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:LEAK', **kwargs)

def AirflownetworkDistributionComponentLeakageratio(idf, **kwargs: AirflownetworkDistributionComponentLeakageratioType):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:LEAKAGERATIO', **kwargs)

def AirflownetworkDistributionComponentOutdoorairflow(idf, **kwargs: AirflownetworkDistributionComponentOutdoorairflowType):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:OUTDOORAIRFLOW', **kwargs)

def AirflownetworkDistributionComponentReliefairflow(idf, **kwargs: AirflownetworkDistributionComponentReliefairflowType):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:RELIEFAIRFLOW', **kwargs)

def AirflownetworkDistributionComponentTerminalunit(idf, **kwargs: AirflownetworkDistributionComponentTerminalunitType):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:TERMINALUNIT', **kwargs)

def AirflownetworkDistributionDuctsizing(idf, **kwargs: AirflownetworkDistributionDuctsizingType):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:DUCTSIZING', **kwargs)

def AirflownetworkDistributionDuctviewfactors(idf, **kwargs: AirflownetworkDistributionDuctviewfactorsType):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:DUCTVIEWFACTORS', **kwargs)

def AirflownetworkDistributionLinkage(idf, **kwargs: AirflownetworkDistributionLinkageType):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:LINKAGE', **kwargs)

def AirflownetworkDistributionNode(idf, **kwargs: AirflownetworkDistributionNodeType):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:NODE', **kwargs)

def AirflownetworkIntrazoneLinkage(idf, **kwargs: AirflownetworkIntrazoneLinkageType):
    return idf.newidfobject('AIRFLOWNETWORK:INTRAZONE:LINKAGE', **kwargs)

def AirflownetworkIntrazoneNode(idf, **kwargs: AirflownetworkIntrazoneNodeType):
    return idf.newidfobject('AIRFLOWNETWORK:INTRAZONE:NODE', **kwargs)

def AirflownetworkMultizoneComponentDetailedopening(idf, **kwargs: AirflownetworkMultizoneComponentDetailedopeningType):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:COMPONENT:DETAILEDOPENING', **kwargs)

def AirflownetworkMultizoneComponentHorizontalopening(idf, **kwargs: AirflownetworkMultizoneComponentHorizontalopeningType):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:COMPONENT:HORIZONTALOPENING', **kwargs)

def AirflownetworkMultizoneComponentSimpleopening(idf, **kwargs: AirflownetworkMultizoneComponentSimpleopeningType):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:COMPONENT:SIMPLEOPENING', **kwargs)

def AirflownetworkMultizoneComponentZoneexhaustfan(idf, **kwargs: AirflownetworkMultizoneComponentZoneexhaustfanType):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:COMPONENT:ZONEEXHAUSTFAN', **kwargs)

def AirflownetworkMultizoneExternalnode(idf, **kwargs: AirflownetworkMultizoneExternalnodeType):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:EXTERNALNODE', **kwargs)

def AirflownetworkMultizoneReferencecrackconditions(idf, **kwargs: AirflownetworkMultizoneReferencecrackconditionsType):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:REFERENCECRACKCONDITIONS', **kwargs)

def AirflownetworkMultizoneSpecifiedflowrate(idf, **kwargs: AirflownetworkMultizoneSpecifiedflowrateType):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:SPECIFIEDFLOWRATE', **kwargs)

def AirflownetworkMultizoneSurface(idf, **kwargs: AirflownetworkMultizoneSurfaceType):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:SURFACE', **kwargs)

def AirflownetworkMultizoneSurfaceCrack(idf, **kwargs: AirflownetworkMultizoneSurfaceCrackType):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:SURFACE:CRACK', **kwargs)

def AirflownetworkMultizoneSurfaceEffectiveleakagearea(idf, **kwargs: AirflownetworkMultizoneSurfaceEffectiveleakageareaType):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:SURFACE:EFFECTIVELEAKAGEAREA', **kwargs)

def AirflownetworkMultizoneWindpressurecoefficientarray(idf, **kwargs: AirflownetworkMultizoneWindpressurecoefficientarrayType):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:WINDPRESSURECOEFFICIENTARRAY', **kwargs)

def AirflownetworkMultizoneWindpressurecoefficientvalues(idf, **kwargs: AirflownetworkMultizoneWindpressurecoefficientvaluesType):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:WINDPRESSURECOEFFICIENTVALUES', **kwargs)

def AirflownetworkMultizoneZone(idf, **kwargs: AirflownetworkMultizoneZoneType):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:ZONE', **kwargs)

def AirflownetworkOccupantventilationcontrol(idf, **kwargs: AirflownetworkOccupantventilationcontrolType):
    return idf.newidfobject('AIRFLOWNETWORK:OCCUPANTVENTILATIONCONTROL', **kwargs)

def AirflownetworkSimulationcontrol(idf, **kwargs: AirflownetworkSimulationcontrolType):
    return idf.newidfobject('AIRFLOWNETWORK:SIMULATIONCONTROL', **kwargs)

def AirflownetworkZonecontrolPressurecontroller(idf, **kwargs: AirflownetworkZonecontrolPressurecontrollerType):
    return idf.newidfobject('AIRFLOWNETWORK:ZONECONTROL:PRESSURECONTROLLER', **kwargs)

def Airloophvac(idf, **kwargs: AirloophvacType):
    return idf.newidfobject('AIRLOOPHVAC', **kwargs)

def AirloophvacControllerlist(idf, **kwargs: AirloophvacControllerlistType):
    return idf.newidfobject('AIRLOOPHVAC:CONTROLLERLIST', **kwargs)

def AirloophvacDedicatedoutdoorairsystem(idf, **kwargs: AirloophvacDedicatedoutdoorairsystemType):
    return idf.newidfobject('AIRLOOPHVAC:DEDICATEDOUTDOORAIRSYSTEM', **kwargs)

def AirloophvacExhaustsystem(idf, **kwargs: AirloophvacExhaustsystemType):
    return idf.newidfobject('AIRLOOPHVAC:EXHAUSTSYSTEM', **kwargs)

def AirloophvacMixer(idf, **kwargs: AirloophvacMixerType):
    return idf.newidfobject('AIRLOOPHVAC:MIXER', **kwargs)

def AirloophvacOutdoorairsystem(idf, **kwargs: AirloophvacOutdoorairsystemType):
    return idf.newidfobject('AIRLOOPHVAC:OUTDOORAIRSYSTEM', **kwargs)

def AirloophvacOutdoorairsystemEquipmentlist(idf, **kwargs: AirloophvacOutdoorairsystemEquipmentlistType):
    return idf.newidfobject('AIRLOOPHVAC:OUTDOORAIRSYSTEM:EQUIPMENTLIST', **kwargs)

def AirloophvacReturnpath(idf, **kwargs: AirloophvacReturnpathType):
    return idf.newidfobject('AIRLOOPHVAC:RETURNPATH', **kwargs)

def AirloophvacReturnplenum(idf, **kwargs: AirloophvacReturnplenumType):
    return idf.newidfobject('AIRLOOPHVAC:RETURNPLENUM', **kwargs)

def AirloophvacSplitter(idf, **kwargs: AirloophvacSplitterType):
    return idf.newidfobject('AIRLOOPHVAC:SPLITTER', **kwargs)

def AirloophvacSupplypath(idf, **kwargs: AirloophvacSupplypathType):
    return idf.newidfobject('AIRLOOPHVAC:SUPPLYPATH', **kwargs)

def AirloophvacSupplyplenum(idf, **kwargs: AirloophvacSupplyplenumType):
    return idf.newidfobject('AIRLOOPHVAC:SUPPLYPLENUM', **kwargs)

def AirloophvacUnitaryFurnaceHeatcool(idf, **kwargs: AirloophvacUnitaryFurnaceHeatcoolType):
    return idf.newidfobject('AIRLOOPHVAC:UNITARY:FURNACE:HEATCOOL', **kwargs)

def AirloophvacUnitaryFurnaceHeatonly(idf, **kwargs: AirloophvacUnitaryFurnaceHeatonlyType):
    return idf.newidfobject('AIRLOOPHVAC:UNITARY:FURNACE:HEATONLY', **kwargs)

def AirloophvacUnitaryheatcool(idf, **kwargs: AirloophvacUnitaryheatcoolType):
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATCOOL', **kwargs)

def AirloophvacUnitaryheatcoolVavchangeoverbypass(idf, **kwargs: AirloophvacUnitaryheatcoolVavchangeoverbypassType):
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATCOOL:VAVCHANGEOVERBYPASS', **kwargs)

def AirloophvacUnitaryheatonly(idf, **kwargs: AirloophvacUnitaryheatonlyType):
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATONLY', **kwargs)

def AirloophvacUnitaryheatpumpAirtoair(idf, **kwargs: AirloophvacUnitaryheatpumpAirtoairType):
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATPUMP:AIRTOAIR', **kwargs)

def AirloophvacUnitaryheatpumpAirtoairMultispeed(idf, **kwargs: AirloophvacUnitaryheatpumpAirtoairMultispeedType):
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATPUMP:AIRTOAIR:MULTISPEED', **kwargs)

def AirloophvacUnitaryheatpumpWatertoair(idf, **kwargs: AirloophvacUnitaryheatpumpWatertoairType):
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATPUMP:WATERTOAIR', **kwargs)

def AirloophvacUnitarysystem(idf, **kwargs: AirloophvacUnitarysystemType):
    return idf.newidfobject('AIRLOOPHVAC:UNITARYSYSTEM', **kwargs)

def AirloophvacZonemixer(idf, **kwargs: AirloophvacZonemixerType):
    return idf.newidfobject('AIRLOOPHVAC:ZONEMIXER', **kwargs)

def AirloophvacZonesplitter(idf, **kwargs: AirloophvacZonesplitterType):
    return idf.newidfobject('AIRLOOPHVAC:ZONESPLITTER', **kwargs)

def AirterminalDualductConstantvolume(idf, **kwargs: AirterminalDualductConstantvolumeType):
    return idf.newidfobject('AIRTERMINAL:DUALDUCT:CONSTANTVOLUME', **kwargs)

def AirterminalDualductVav(idf, **kwargs: AirterminalDualductVavType):
    return idf.newidfobject('AIRTERMINAL:DUALDUCT:VAV', **kwargs)

def AirterminalDualductVavOutdoorair(idf, **kwargs: AirterminalDualductVavOutdoorairType):
    return idf.newidfobject('AIRTERMINAL:DUALDUCT:VAV:OUTDOORAIR', **kwargs)

def AirterminalSingleductConstantvolumeCooledbeam(idf, **kwargs: AirterminalSingleductConstantvolumeCooledbeamType):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:COOLEDBEAM', **kwargs)

def AirterminalSingleductConstantvolumeFourpipebeam(idf, **kwargs: AirterminalSingleductConstantvolumeFourpipebeamType):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:FOURPIPEBEAM', **kwargs)

def AirterminalSingleductConstantvolumeFourpipeinduction(idf, **kwargs: AirterminalSingleductConstantvolumeFourpipeinductionType):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:FOURPIPEINDUCTION', **kwargs)

def AirterminalSingleductConstantvolumeNoreheat(idf, **kwargs: AirterminalSingleductConstantvolumeNoreheatType):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:NOREHEAT', **kwargs)

def AirterminalSingleductConstantvolumeReheat(idf, **kwargs: AirterminalSingleductConstantvolumeReheatType):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:REHEAT', **kwargs)

def AirterminalSingleductMixer(idf, **kwargs: AirterminalSingleductMixerType):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:MIXER', **kwargs)

def AirterminalSingleductParallelpiuReheat(idf, **kwargs: AirterminalSingleductParallelpiuReheatType):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:PARALLELPIU:REHEAT', **kwargs)

def AirterminalSingleductSeriespiuReheat(idf, **kwargs: AirterminalSingleductSeriespiuReheatType):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:SERIESPIU:REHEAT', **kwargs)

def AirterminalSingleductUserdefined(idf, **kwargs: AirterminalSingleductUserdefinedType):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:USERDEFINED', **kwargs)

def AirterminalSingleductVavHeatandcoolNoreheat(idf, **kwargs: AirterminalSingleductVavHeatandcoolNoreheatType):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:VAV:HEATANDCOOL:NOREHEAT', **kwargs)

def AirterminalSingleductVavHeatandcoolReheat(idf, **kwargs: AirterminalSingleductVavHeatandcoolReheatType):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:VAV:HEATANDCOOL:REHEAT', **kwargs)

def AirterminalSingleductVavNoreheat(idf, **kwargs: AirterminalSingleductVavNoreheatType):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:VAV:NOREHEAT', **kwargs)

def AirterminalSingleductVavReheat(idf, **kwargs: AirterminalSingleductVavReheatType):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:VAV:REHEAT', **kwargs)

def AirterminalSingleductVavReheatVariablespeedfan(idf, **kwargs: AirterminalSingleductVavReheatVariablespeedfanType):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:VAV:REHEAT:VARIABLESPEEDFAN', **kwargs)

def AvailabilitymanagerDifferentialthermostat(idf, **kwargs: AvailabilitymanagerDifferentialthermostatType):
    return idf.newidfobject('AVAILABILITYMANAGER:DIFFERENTIALTHERMOSTAT', **kwargs)

def AvailabilitymanagerHightemperatureturnoff(idf, **kwargs: AvailabilitymanagerHightemperatureturnoffType):
    return idf.newidfobject('AVAILABILITYMANAGER:HIGHTEMPERATURETURNOFF', **kwargs)

def AvailabilitymanagerHightemperatureturnon(idf, **kwargs: AvailabilitymanagerHightemperatureturnonType):
    return idf.newidfobject('AVAILABILITYMANAGER:HIGHTEMPERATURETURNON', **kwargs)

def AvailabilitymanagerHybridventilation(idf, **kwargs: AvailabilitymanagerHybridventilationType):
    return idf.newidfobject('AVAILABILITYMANAGER:HYBRIDVENTILATION', **kwargs)

def AvailabilitymanagerLowtemperatureturnoff(idf, **kwargs: AvailabilitymanagerLowtemperatureturnoffType):
    return idf.newidfobject('AVAILABILITYMANAGER:LOWTEMPERATURETURNOFF', **kwargs)

def AvailabilitymanagerLowtemperatureturnon(idf, **kwargs: AvailabilitymanagerLowtemperatureturnonType):
    return idf.newidfobject('AVAILABILITYMANAGER:LOWTEMPERATURETURNON', **kwargs)

def AvailabilitymanagerNightcycle(idf, **kwargs: AvailabilitymanagerNightcycleType):
    return idf.newidfobject('AVAILABILITYMANAGER:NIGHTCYCLE', **kwargs)

def AvailabilitymanagerNightventilation(idf, **kwargs: AvailabilitymanagerNightventilationType):
    return idf.newidfobject('AVAILABILITYMANAGER:NIGHTVENTILATION', **kwargs)

def AvailabilitymanagerOptimumstart(idf, **kwargs: AvailabilitymanagerOptimumstartType):
    return idf.newidfobject('AVAILABILITYMANAGER:OPTIMUMSTART', **kwargs)

def AvailabilitymanagerScheduled(idf, **kwargs: AvailabilitymanagerScheduledType):
    return idf.newidfobject('AVAILABILITYMANAGER:SCHEDULED', **kwargs)

def AvailabilitymanagerScheduledoff(idf, **kwargs: AvailabilitymanagerScheduledoffType):
    return idf.newidfobject('AVAILABILITYMANAGER:SCHEDULEDOFF', **kwargs)

def AvailabilitymanagerScheduledon(idf, **kwargs: AvailabilitymanagerScheduledonType):
    return idf.newidfobject('AVAILABILITYMANAGER:SCHEDULEDON', **kwargs)

def Availabilitymanagerassignmentlist(idf, **kwargs: AvailabilitymanagerassignmentlistType):
    return idf.newidfobject('AVAILABILITYMANAGERASSIGNMENTLIST', **kwargs)

def BoilerHotwater(idf, **kwargs: BoilerHotwaterType):
    return idf.newidfobject('BOILER:HOTWATER', **kwargs)

def BoilerSteam(idf, **kwargs: BoilerSteamType):
    return idf.newidfobject('BOILER:STEAM', **kwargs)

def Branch(idf, **kwargs: BranchType):
    return idf.newidfobject('BRANCH', **kwargs)

def Branchlist(idf, **kwargs: BranchlistType):
    return idf.newidfobject('BRANCHLIST', **kwargs)

def Building(idf, **kwargs: BuildingType):
    return idf.newidfobject('BUILDING', **kwargs)

def BuildingsurfaceDetailed(idf, **kwargs: BuildingsurfaceDetailedType):
    return idf.newidfobject('BUILDINGSURFACE:DETAILED', **kwargs)

def CeilingAdiabatic(idf, **kwargs: CeilingAdiabaticType):
    return idf.newidfobject('CEILING:ADIABATIC', **kwargs)

def CeilingInterzone(idf, **kwargs: CeilingInterzoneType):
    return idf.newidfobject('CEILING:INTERZONE', **kwargs)

def Centralheatpumpsystem(idf, **kwargs: CentralheatpumpsystemType):
    return idf.newidfobject('CENTRALHEATPUMPSYSTEM', **kwargs)

def ChillerAbsorption(idf, **kwargs: ChillerAbsorptionType):
    return idf.newidfobject('CHILLER:ABSORPTION', **kwargs)

def ChillerAbsorptionIndirect(idf, **kwargs: ChillerAbsorptionIndirectType):
    return idf.newidfobject('CHILLER:ABSORPTION:INDIRECT', **kwargs)

def ChillerCombustionturbine(idf, **kwargs: ChillerCombustionturbineType):
    return idf.newidfobject('CHILLER:COMBUSTIONTURBINE', **kwargs)

def ChillerConstantcop(idf, **kwargs: ChillerConstantcopType):
    return idf.newidfobject('CHILLER:CONSTANTCOP', **kwargs)

def ChillerElectric(idf, **kwargs: ChillerElectricType):
    return idf.newidfobject('CHILLER:ELECTRIC', **kwargs)

def ChillerElectricAshrae205(idf, **kwargs: ChillerElectricAshrae205Type):
    return idf.newidfobject('CHILLER:ELECTRIC:ASHRAE205', **kwargs)

def ChillerElectricEir(idf, **kwargs: ChillerElectricEirType):
    return idf.newidfobject('CHILLER:ELECTRIC:EIR', **kwargs)

def ChillerElectricReformulatedeir(idf, **kwargs: ChillerElectricReformulatedeirType):
    return idf.newidfobject('CHILLER:ELECTRIC:REFORMULATEDEIR', **kwargs)

def ChillerEnginedriven(idf, **kwargs: ChillerEnginedrivenType):
    return idf.newidfobject('CHILLER:ENGINEDRIVEN', **kwargs)

def ChillerheaterAbsorptionDirectfired(idf, **kwargs: ChillerheaterAbsorptionDirectfiredType):
    return idf.newidfobject('CHILLERHEATER:ABSORPTION:DIRECTFIRED', **kwargs)

def ChillerheaterAbsorptionDoubleeffect(idf, **kwargs: ChillerheaterAbsorptionDoubleeffectType):
    return idf.newidfobject('CHILLERHEATER:ABSORPTION:DOUBLEEFFECT', **kwargs)

def ChillerheaterperformanceElectricEir(idf, **kwargs: ChillerheaterperformanceElectricEirType):
    return idf.newidfobject('CHILLERHEATERPERFORMANCE:ELECTRIC:EIR', **kwargs)

def CoilCoolingDx(idf, **kwargs: CoilCoolingDxType):
    return idf.newidfobject('COIL:COOLING:DX', **kwargs)

def CoilCoolingDxCurvefitOperatingmode(idf, **kwargs: CoilCoolingDxCurvefitOperatingmodeType):
    return idf.newidfobject('COIL:COOLING:DX:CURVEFIT:OPERATINGMODE', **kwargs)

def CoilCoolingDxCurvefitPerformance(idf, **kwargs: CoilCoolingDxCurvefitPerformanceType):
    return idf.newidfobject('COIL:COOLING:DX:CURVEFIT:PERFORMANCE', **kwargs)

def CoilCoolingDxCurvefitSpeed(idf, **kwargs: CoilCoolingDxCurvefitSpeedType):
    return idf.newidfobject('COIL:COOLING:DX:CURVEFIT:SPEED', **kwargs)

def CoilCoolingDxMultispeed(idf, **kwargs: CoilCoolingDxMultispeedType):
    return idf.newidfobject('COIL:COOLING:DX:MULTISPEED', **kwargs)

def CoilCoolingDxSinglespeed(idf, **kwargs: CoilCoolingDxSinglespeedType):
    return idf.newidfobject('COIL:COOLING:DX:SINGLESPEED', **kwargs)

def CoilCoolingDxSinglespeedThermalstorage(idf, **kwargs: CoilCoolingDxSinglespeedThermalstorageType):
    return idf.newidfobject('COIL:COOLING:DX:SINGLESPEED:THERMALSTORAGE', **kwargs)

def CoilCoolingDxTwospeed(idf, **kwargs: CoilCoolingDxTwospeedType):
    return idf.newidfobject('COIL:COOLING:DX:TWOSPEED', **kwargs)

def CoilCoolingDxTwostagewithhumiditycontrolmode(idf, **kwargs: CoilCoolingDxTwostagewithhumiditycontrolmodeType):
    return idf.newidfobject('COIL:COOLING:DX:TWOSTAGEWITHHUMIDITYCONTROLMODE', **kwargs)

def CoilCoolingDxVariablerefrigerantflow(idf, **kwargs: CoilCoolingDxVariablerefrigerantflowType):
    return idf.newidfobject('COIL:COOLING:DX:VARIABLEREFRIGERANTFLOW', **kwargs)

def CoilCoolingDxVariablerefrigerantflowFluidtemperaturecontrol(idf, **kwargs: CoilCoolingDxVariablerefrigerantflowFluidtemperaturecontrolType):
    return idf.newidfobject('COIL:COOLING:DX:VARIABLEREFRIGERANTFLOW:FLUIDTEMPERATURECONTROL', **kwargs)

def CoilCoolingDxVariablespeed(idf, **kwargs: CoilCoolingDxVariablespeedType):
    return idf.newidfobject('COIL:COOLING:DX:VARIABLESPEED', **kwargs)

def CoilCoolingWater(idf, **kwargs: CoilCoolingWaterType):
    return idf.newidfobject('COIL:COOLING:WATER', **kwargs)

def CoilCoolingWaterDetailedgeometry(idf, **kwargs: CoilCoolingWaterDetailedgeometryType):
    return idf.newidfobject('COIL:COOLING:WATER:DETAILEDGEOMETRY', **kwargs)

def CoilCoolingWatertoairheatpumpEquationfit(idf, **kwargs: CoilCoolingWatertoairheatpumpEquationfitType):
    return idf.newidfobject('COIL:COOLING:WATERTOAIRHEATPUMP:EQUATIONFIT', **kwargs)

def CoilCoolingWatertoairheatpumpParameterestimation(idf, **kwargs: CoilCoolingWatertoairheatpumpParameterestimationType):
    return idf.newidfobject('COIL:COOLING:WATERTOAIRHEATPUMP:PARAMETERESTIMATION', **kwargs)

def CoilCoolingWatertoairheatpumpVariablespeedequationfit(idf, **kwargs: CoilCoolingWatertoairheatpumpVariablespeedequationfitType):
    return idf.newidfobject('COIL:COOLING:WATERTOAIRHEATPUMP:VARIABLESPEEDEQUATIONFIT', **kwargs)

def CoilHeatingDesuperheater(idf, **kwargs: CoilHeatingDesuperheaterType):
    return idf.newidfobject('COIL:HEATING:DESUPERHEATER', **kwargs)

def CoilHeatingDxMultispeed(idf, **kwargs: CoilHeatingDxMultispeedType):
    return idf.newidfobject('COIL:HEATING:DX:MULTISPEED', **kwargs)

def CoilHeatingDxSinglespeed(idf, **kwargs: CoilHeatingDxSinglespeedType):
    return idf.newidfobject('COIL:HEATING:DX:SINGLESPEED', **kwargs)

def CoilHeatingDxVariablerefrigerantflow(idf, **kwargs: CoilHeatingDxVariablerefrigerantflowType):
    return idf.newidfobject('COIL:HEATING:DX:VARIABLEREFRIGERANTFLOW', **kwargs)

def CoilHeatingDxVariablerefrigerantflowFluidtemperaturecontrol(idf, **kwargs: CoilHeatingDxVariablerefrigerantflowFluidtemperaturecontrolType):
    return idf.newidfobject('COIL:HEATING:DX:VARIABLEREFRIGERANTFLOW:FLUIDTEMPERATURECONTROL', **kwargs)

def CoilHeatingDxVariablespeed(idf, **kwargs: CoilHeatingDxVariablespeedType):
    return idf.newidfobject('COIL:HEATING:DX:VARIABLESPEED', **kwargs)

def CoilHeatingElectric(idf, **kwargs: CoilHeatingElectricType):
    return idf.newidfobject('COIL:HEATING:ELECTRIC', **kwargs)

def CoilHeatingElectricMultistage(idf, **kwargs: CoilHeatingElectricMultistageType):
    return idf.newidfobject('COIL:HEATING:ELECTRIC:MULTISTAGE', **kwargs)

def CoilHeatingFuel(idf, **kwargs: CoilHeatingFuelType):
    return idf.newidfobject('COIL:HEATING:FUEL', **kwargs)

def CoilHeatingGasMultistage(idf, **kwargs: CoilHeatingGasMultistageType):
    return idf.newidfobject('COIL:HEATING:GAS:MULTISTAGE', **kwargs)

def CoilHeatingSteam(idf, **kwargs: CoilHeatingSteamType):
    return idf.newidfobject('COIL:HEATING:STEAM', **kwargs)

def CoilHeatingWater(idf, **kwargs: CoilHeatingWaterType):
    return idf.newidfobject('COIL:HEATING:WATER', **kwargs)

def CoilHeatingWatertoairheatpumpEquationfit(idf, **kwargs: CoilHeatingWatertoairheatpumpEquationfitType):
    return idf.newidfobject('COIL:HEATING:WATERTOAIRHEATPUMP:EQUATIONFIT', **kwargs)

def CoilHeatingWatertoairheatpumpParameterestimation(idf, **kwargs: CoilHeatingWatertoairheatpumpParameterestimationType):
    return idf.newidfobject('COIL:HEATING:WATERTOAIRHEATPUMP:PARAMETERESTIMATION', **kwargs)

def CoilHeatingWatertoairheatpumpVariablespeedequationfit(idf, **kwargs: CoilHeatingWatertoairheatpumpVariablespeedequationfitType):
    return idf.newidfobject('COIL:HEATING:WATERTOAIRHEATPUMP:VARIABLESPEEDEQUATIONFIT', **kwargs)

def CoilUserdefined(idf, **kwargs: CoilUserdefinedType):
    return idf.newidfobject('COIL:USERDEFINED', **kwargs)

def CoilWaterheatingAirtowaterheatpumpPumped(idf, **kwargs: CoilWaterheatingAirtowaterheatpumpPumpedType):
    return idf.newidfobject('COIL:WATERHEATING:AIRTOWATERHEATPUMP:PUMPED', **kwargs)

def CoilWaterheatingAirtowaterheatpumpVariablespeed(idf, **kwargs: CoilWaterheatingAirtowaterheatpumpVariablespeedType):
    return idf.newidfobject('COIL:WATERHEATING:AIRTOWATERHEATPUMP:VARIABLESPEED', **kwargs)

def CoilWaterheatingAirtowaterheatpumpWrapped(idf, **kwargs: CoilWaterheatingAirtowaterheatpumpWrappedType):
    return idf.newidfobject('COIL:WATERHEATING:AIRTOWATERHEATPUMP:WRAPPED', **kwargs)

def CoilWaterheatingDesuperheater(idf, **kwargs: CoilWaterheatingDesuperheaterType):
    return idf.newidfobject('COIL:WATERHEATING:DESUPERHEATER', **kwargs)

def CoilperformanceDxCooling(idf, **kwargs: CoilperformanceDxCoolingType):
    return idf.newidfobject('COILPERFORMANCE:DX:COOLING', **kwargs)

def CoilsystemCoolingDx(idf, **kwargs: CoilsystemCoolingDxType):
    return idf.newidfobject('COILSYSTEM:COOLING:DX', **kwargs)

def CoilsystemCoolingDxHeatexchangerassisted(idf, **kwargs: CoilsystemCoolingDxHeatexchangerassistedType):
    return idf.newidfobject('COILSYSTEM:COOLING:DX:HEATEXCHANGERASSISTED', **kwargs)

def CoilsystemCoolingWater(idf, **kwargs: CoilsystemCoolingWaterType):
    return idf.newidfobject('COILSYSTEM:COOLING:WATER', **kwargs)

def CoilsystemCoolingWaterHeatexchangerassisted(idf, **kwargs: CoilsystemCoolingWaterHeatexchangerassistedType):
    return idf.newidfobject('COILSYSTEM:COOLING:WATER:HEATEXCHANGERASSISTED', **kwargs)

def CoilsystemHeatingDx(idf, **kwargs: CoilsystemHeatingDxType):
    return idf.newidfobject('COILSYSTEM:HEATING:DX', **kwargs)

def CoilsystemIntegratedheatpumpAirsource(idf, **kwargs: CoilsystemIntegratedheatpumpAirsourceType):
    return idf.newidfobject('COILSYSTEM:INTEGRATEDHEATPUMP:AIRSOURCE', **kwargs)

def Comfortviewfactorangles(idf, **kwargs: ComfortviewfactoranglesType):
    return idf.newidfobject('COMFORTVIEWFACTORANGLES', **kwargs)

def ComplexfenestrationpropertySolarabsorbedlayers(idf, **kwargs: ComplexfenestrationpropertySolarabsorbedlayersType):
    return idf.newidfobject('COMPLEXFENESTRATIONPROPERTY:SOLARABSORBEDLAYERS', **kwargs)

def ComplianceBuilding(idf, **kwargs: ComplianceBuildingType):
    return idf.newidfobject('COMPLIANCE:BUILDING', **kwargs)

def ComponentcostAdjustments(idf, **kwargs: ComponentcostAdjustmentsType):
    return idf.newidfobject('COMPONENTCOST:ADJUSTMENTS', **kwargs)

def ComponentcostLineitem(idf, **kwargs: ComponentcostLineitemType):
    return idf.newidfobject('COMPONENTCOST:LINEITEM', **kwargs)

def ComponentcostReference(idf, **kwargs: ComponentcostReferenceType):
    return idf.newidfobject('COMPONENTCOST:REFERENCE', **kwargs)

def Condenserequipmentlist(idf, **kwargs: CondenserequipmentlistType):
    return idf.newidfobject('CONDENSEREQUIPMENTLIST', **kwargs)

def Condenserequipmentoperationschemes(idf, **kwargs: CondenserequipmentoperationschemesType):
    return idf.newidfobject('CONDENSEREQUIPMENTOPERATIONSCHEMES', **kwargs)

def Condenserloop(idf, **kwargs: CondenserloopType):
    return idf.newidfobject('CONDENSERLOOP', **kwargs)

def ConnectorMixer(idf, **kwargs: ConnectorMixerType):
    return idf.newidfobject('CONNECTOR:MIXER', **kwargs)

def ConnectorSplitter(idf, **kwargs: ConnectorSplitterType):
    return idf.newidfobject('CONNECTOR:SPLITTER', **kwargs)

def Connectorlist(idf, **kwargs: ConnectorlistType):
    return idf.newidfobject('CONNECTORLIST', **kwargs)

def Construction(idf, **kwargs: ConstructionType):
    return idf.newidfobject('CONSTRUCTION', **kwargs)

def ConstructionAirboundary(idf, **kwargs: ConstructionAirboundaryType):
    return idf.newidfobject('CONSTRUCTION:AIRBOUNDARY', **kwargs)

def ConstructionCfactorundergroundwall(idf, **kwargs: ConstructionCfactorundergroundwallType):
    return idf.newidfobject('CONSTRUCTION:CFACTORUNDERGROUNDWALL', **kwargs)

def ConstructionComplexfenestrationstate(idf, **kwargs: ConstructionComplexfenestrationstateType):
    return idf.newidfobject('CONSTRUCTION:COMPLEXFENESTRATIONSTATE', **kwargs)

def ConstructionFfactorgroundfloor(idf, **kwargs: ConstructionFfactorgroundfloorType):
    return idf.newidfobject('CONSTRUCTION:FFACTORGROUNDFLOOR', **kwargs)

def ConstructionWindowdatafile(idf, **kwargs: ConstructionWindowdatafileType):
    return idf.newidfobject('CONSTRUCTION:WINDOWDATAFILE', **kwargs)

def ConstructionWindowequivalentlayer(idf, **kwargs: ConstructionWindowequivalentlayerType):
    return idf.newidfobject('CONSTRUCTION:WINDOWEQUIVALENTLAYER', **kwargs)

def ConstructionpropertyInternalheatsource(idf, **kwargs: ConstructionpropertyInternalheatsourceType):
    return idf.newidfobject('CONSTRUCTIONPROPERTY:INTERNALHEATSOURCE', **kwargs)

def ControllerMechanicalventilation(idf, **kwargs: ControllerMechanicalventilationType):
    return idf.newidfobject('CONTROLLER:MECHANICALVENTILATION', **kwargs)

def ControllerOutdoorair(idf, **kwargs: ControllerOutdoorairType):
    return idf.newidfobject('CONTROLLER:OUTDOORAIR', **kwargs)

def ControllerWatercoil(idf, **kwargs: ControllerWatercoilType):
    return idf.newidfobject('CONTROLLER:WATERCOIL', **kwargs)

def Convergencelimits(idf, **kwargs: ConvergencelimitsType):
    return idf.newidfobject('CONVERGENCELIMITS', **kwargs)

def CoolingtowerSinglespeed(idf, **kwargs: CoolingtowerSinglespeedType):
    return idf.newidfobject('COOLINGTOWER:SINGLESPEED', **kwargs)

def CoolingtowerTwospeed(idf, **kwargs: CoolingtowerTwospeedType):
    return idf.newidfobject('COOLINGTOWER:TWOSPEED', **kwargs)

def CoolingtowerVariablespeed(idf, **kwargs: CoolingtowerVariablespeedType):
    return idf.newidfobject('COOLINGTOWER:VARIABLESPEED', **kwargs)

def CoolingtowerVariablespeedMerkel(idf, **kwargs: CoolingtowerVariablespeedMerkelType):
    return idf.newidfobject('COOLINGTOWER:VARIABLESPEED:MERKEL', **kwargs)

def CoolingtowerperformanceCooltools(idf, **kwargs: CoolingtowerperformanceCooltoolsType):
    return idf.newidfobject('COOLINGTOWERPERFORMANCE:COOLTOOLS', **kwargs)

def CoolingtowerperformanceYorkcalc(idf, **kwargs: CoolingtowerperformanceYorkcalcType):
    return idf.newidfobject('COOLINGTOWERPERFORMANCE:YORKCALC', **kwargs)

def Currencytype(idf, **kwargs: CurrencytypeType):
    return idf.newidfobject('CURRENCYTYPE', **kwargs)

def CurveBicubic(idf, **kwargs: CurveBicubicType):
    return idf.newidfobject('CURVE:BICUBIC', **kwargs)

def CurveBiquadratic(idf, **kwargs: CurveBiquadraticType):
    return idf.newidfobject('CURVE:BIQUADRATIC', **kwargs)

def CurveChillerpartloadwithlift(idf, **kwargs: CurveChillerpartloadwithliftType):
    return idf.newidfobject('CURVE:CHILLERPARTLOADWITHLIFT', **kwargs)

def CurveCubic(idf, **kwargs: CurveCubicType):
    return idf.newidfobject('CURVE:CUBIC', **kwargs)

def CurveCubiclinear(idf, **kwargs: CurveCubiclinearType):
    return idf.newidfobject('CURVE:CUBICLINEAR', **kwargs)

def CurveDoubleexponentialdecay(idf, **kwargs: CurveDoubleexponentialdecayType):
    return idf.newidfobject('CURVE:DOUBLEEXPONENTIALDECAY', **kwargs)

def CurveExponent(idf, **kwargs: CurveExponentType):
    return idf.newidfobject('CURVE:EXPONENT', **kwargs)

def CurveExponentialdecay(idf, **kwargs: CurveExponentialdecayType):
    return idf.newidfobject('CURVE:EXPONENTIALDECAY', **kwargs)

def CurveExponentialskewnormal(idf, **kwargs: CurveExponentialskewnormalType):
    return idf.newidfobject('CURVE:EXPONENTIALSKEWNORMAL', **kwargs)

def CurveFanpressurerise(idf, **kwargs: CurveFanpressureriseType):
    return idf.newidfobject('CURVE:FANPRESSURERISE', **kwargs)

def CurveFunctionalPressuredrop(idf, **kwargs: CurveFunctionalPressuredropType):
    return idf.newidfobject('CURVE:FUNCTIONAL:PRESSUREDROP', **kwargs)

def CurveLinear(idf, **kwargs: CurveLinearType):
    return idf.newidfobject('CURVE:LINEAR', **kwargs)

def CurveQuadlinear(idf, **kwargs: CurveQuadlinearType):
    return idf.newidfobject('CURVE:QUADLINEAR', **kwargs)

def CurveQuadratic(idf, **kwargs: CurveQuadraticType):
    return idf.newidfobject('CURVE:QUADRATIC', **kwargs)

def CurveQuadraticlinear(idf, **kwargs: CurveQuadraticlinearType):
    return idf.newidfobject('CURVE:QUADRATICLINEAR', **kwargs)

def CurveQuartic(idf, **kwargs: CurveQuarticType):
    return idf.newidfobject('CURVE:QUARTIC', **kwargs)

def CurveQuintlinear(idf, **kwargs: CurveQuintlinearType):
    return idf.newidfobject('CURVE:QUINTLINEAR', **kwargs)

def CurveRectangularhyperbola1(idf, **kwargs: CurveRectangularhyperbola1Type):
    return idf.newidfobject('CURVE:RECTANGULARHYPERBOLA1', **kwargs)

def CurveRectangularhyperbola2(idf, **kwargs: CurveRectangularhyperbola2Type):
    return idf.newidfobject('CURVE:RECTANGULARHYPERBOLA2', **kwargs)

def CurveSigmoid(idf, **kwargs: CurveSigmoidType):
    return idf.newidfobject('CURVE:SIGMOID', **kwargs)

def CurveTriquadratic(idf, **kwargs: CurveTriquadraticType):
    return idf.newidfobject('CURVE:TRIQUADRATIC', **kwargs)

def DaylightingControls(idf, **kwargs: DaylightingControlsType):
    return idf.newidfobject('DAYLIGHTING:CONTROLS', **kwargs)

def DaylightingDelightComplexfenestration(idf, **kwargs: DaylightingDelightComplexfenestrationType):
    return idf.newidfobject('DAYLIGHTING:DELIGHT:COMPLEXFENESTRATION', **kwargs)

def DaylightingReferencepoint(idf, **kwargs: DaylightingReferencepointType):
    return idf.newidfobject('DAYLIGHTING:REFERENCEPOINT', **kwargs)

def DaylightingdeviceLightwell(idf, **kwargs: DaylightingdeviceLightwellType):
    return idf.newidfobject('DAYLIGHTINGDEVICE:LIGHTWELL', **kwargs)

def DaylightingdeviceShelf(idf, **kwargs: DaylightingdeviceShelfType):
    return idf.newidfobject('DAYLIGHTINGDEVICE:SHELF', **kwargs)

def DaylightingdeviceTubular(idf, **kwargs: DaylightingdeviceTubularType):
    return idf.newidfobject('DAYLIGHTINGDEVICE:TUBULAR', **kwargs)

def DehumidifierDesiccantNofans(idf, **kwargs: DehumidifierDesiccantNofansType):
    return idf.newidfobject('DEHUMIDIFIER:DESICCANT:NOFANS', **kwargs)

def DehumidifierDesiccantSystem(idf, **kwargs: DehumidifierDesiccantSystemType):
    return idf.newidfobject('DEHUMIDIFIER:DESICCANT:SYSTEM', **kwargs)

def DemandmanagerElectricequipment(idf, **kwargs: DemandmanagerElectricequipmentType):
    return idf.newidfobject('DEMANDMANAGER:ELECTRICEQUIPMENT', **kwargs)

def DemandmanagerExteriorlights(idf, **kwargs: DemandmanagerExteriorlightsType):
    return idf.newidfobject('DEMANDMANAGER:EXTERIORLIGHTS', **kwargs)

def DemandmanagerLights(idf, **kwargs: DemandmanagerLightsType):
    return idf.newidfobject('DEMANDMANAGER:LIGHTS', **kwargs)

def DemandmanagerThermostats(idf, **kwargs: DemandmanagerThermostatsType):
    return idf.newidfobject('DEMANDMANAGER:THERMOSTATS', **kwargs)

def DemandmanagerVentilation(idf, **kwargs: DemandmanagerVentilationType):
    return idf.newidfobject('DEMANDMANAGER:VENTILATION', **kwargs)

def Demandmanagerassignmentlist(idf, **kwargs: DemandmanagerassignmentlistType):
    return idf.newidfobject('DEMANDMANAGERASSIGNMENTLIST', **kwargs)

def DesignspecificationAirterminalSizing(idf, **kwargs: DesignspecificationAirterminalSizingType):
    return idf.newidfobject('DESIGNSPECIFICATION:AIRTERMINAL:SIZING', **kwargs)

def DesignspecificationOutdoorair(idf, **kwargs: DesignspecificationOutdoorairType):
    return idf.newidfobject('DESIGNSPECIFICATION:OUTDOORAIR', **kwargs)

def DesignspecificationOutdoorairSpacelist(idf, **kwargs: DesignspecificationOutdoorairSpacelistType):
    return idf.newidfobject('DESIGNSPECIFICATION:OUTDOORAIR:SPACELIST', **kwargs)

def DesignspecificationZoneairdistribution(idf, **kwargs: DesignspecificationZoneairdistributionType):
    return idf.newidfobject('DESIGNSPECIFICATION:ZONEAIRDISTRIBUTION', **kwargs)

def DesignspecificationZonehvacSizing(idf, **kwargs: DesignspecificationZonehvacSizingType):
    return idf.newidfobject('DESIGNSPECIFICATION:ZONEHVAC:SIZING', **kwargs)

def Districtcooling(idf, **kwargs: DistrictcoolingType):
    return idf.newidfobject('DISTRICTCOOLING', **kwargs)

def DistrictheatingSteam(idf, **kwargs: DistrictheatingSteamType):
    return idf.newidfobject('DISTRICTHEATING:STEAM', **kwargs)

def DistrictheatingWater(idf, **kwargs: DistrictheatingWaterType):
    return idf.newidfobject('DISTRICTHEATING:WATER', **kwargs)

def Door(idf, **kwargs: DoorType):
    return idf.newidfobject('DOOR', **kwargs)

def DoorInterzone(idf, **kwargs: DoorInterzoneType):
    return idf.newidfobject('DOOR:INTERZONE', **kwargs)

def Duct(idf, **kwargs: DuctType):
    return idf.newidfobject('DUCT', **kwargs)

def Electricequipment(idf, **kwargs: ElectricequipmentType):
    return idf.newidfobject('ELECTRICEQUIPMENT', **kwargs)

def ElectricequipmentIteAircooled(idf, **kwargs: ElectricequipmentIteAircooledType):
    return idf.newidfobject('ELECTRICEQUIPMENT:ITE:AIRCOOLED', **kwargs)

def ElectricloadcenterDistribution(idf, **kwargs: ElectricloadcenterDistributionType):
    return idf.newidfobject('ELECTRICLOADCENTER:DISTRIBUTION', **kwargs)

def ElectricloadcenterGenerators(idf, **kwargs: ElectricloadcenterGeneratorsType):
    return idf.newidfobject('ELECTRICLOADCENTER:GENERATORS', **kwargs)

def ElectricloadcenterInverterFunctionofpower(idf, **kwargs: ElectricloadcenterInverterFunctionofpowerType):
    return idf.newidfobject('ELECTRICLOADCENTER:INVERTER:FUNCTIONOFPOWER', **kwargs)

def ElectricloadcenterInverterLookuptable(idf, **kwargs: ElectricloadcenterInverterLookuptableType):
    return idf.newidfobject('ELECTRICLOADCENTER:INVERTER:LOOKUPTABLE', **kwargs)

def ElectricloadcenterInverterPvwatts(idf, **kwargs: ElectricloadcenterInverterPvwattsType):
    return idf.newidfobject('ELECTRICLOADCENTER:INVERTER:PVWATTS', **kwargs)

def ElectricloadcenterInverterSimple(idf, **kwargs: ElectricloadcenterInverterSimpleType):
    return idf.newidfobject('ELECTRICLOADCENTER:INVERTER:SIMPLE', **kwargs)

def ElectricloadcenterStorageBattery(idf, **kwargs: ElectricloadcenterStorageBatteryType):
    return idf.newidfobject('ELECTRICLOADCENTER:STORAGE:BATTERY', **kwargs)

def ElectricloadcenterStorageConverter(idf, **kwargs: ElectricloadcenterStorageConverterType):
    return idf.newidfobject('ELECTRICLOADCENTER:STORAGE:CONVERTER', **kwargs)

def ElectricloadcenterStorageLiionnmcbattery(idf, **kwargs: ElectricloadcenterStorageLiionnmcbatteryType):
    return idf.newidfobject('ELECTRICLOADCENTER:STORAGE:LIIONNMCBATTERY', **kwargs)

def ElectricloadcenterStorageSimple(idf, **kwargs: ElectricloadcenterStorageSimpleType):
    return idf.newidfobject('ELECTRICLOADCENTER:STORAGE:SIMPLE', **kwargs)

def ElectricloadcenterTransformer(idf, **kwargs: ElectricloadcenterTransformerType):
    return idf.newidfobject('ELECTRICLOADCENTER:TRANSFORMER', **kwargs)

def EnergymanagementsystemActuator(idf, **kwargs: EnergymanagementsystemActuatorType):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:ACTUATOR', **kwargs)

def EnergymanagementsystemConstructionindexvariable(idf, **kwargs: EnergymanagementsystemConstructionindexvariableType):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:CONSTRUCTIONINDEXVARIABLE', **kwargs)

def EnergymanagementsystemCurveortableindexvariable(idf, **kwargs: EnergymanagementsystemCurveortableindexvariableType):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:CURVEORTABLEINDEXVARIABLE', **kwargs)

def EnergymanagementsystemGlobalvariable(idf, **kwargs: EnergymanagementsystemGlobalvariableType):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:GLOBALVARIABLE', **kwargs)

def EnergymanagementsystemInternalvariable(idf, **kwargs: EnergymanagementsystemInternalvariableType):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:INTERNALVARIABLE', **kwargs)

def EnergymanagementsystemMeteredoutputvariable(idf, **kwargs: EnergymanagementsystemMeteredoutputvariableType):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:METEREDOUTPUTVARIABLE', **kwargs)

def EnergymanagementsystemOutputvariable(idf, **kwargs: EnergymanagementsystemOutputvariableType):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:OUTPUTVARIABLE', **kwargs)

def EnergymanagementsystemProgram(idf, **kwargs: EnergymanagementsystemProgramType):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:PROGRAM', **kwargs)

def EnergymanagementsystemProgramcallingmanager(idf, **kwargs: EnergymanagementsystemProgramcallingmanagerType):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:PROGRAMCALLINGMANAGER', **kwargs)

def EnergymanagementsystemSensor(idf, **kwargs: EnergymanagementsystemSensorType):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:SENSOR', **kwargs)

def EnergymanagementsystemSubroutine(idf, **kwargs: EnergymanagementsystemSubroutineType):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:SUBROUTINE', **kwargs)

def EnergymanagementsystemTrendvariable(idf, **kwargs: EnergymanagementsystemTrendvariableType):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:TRENDVARIABLE', **kwargs)

def Environmentalimpactfactors(idf, **kwargs: EnvironmentalimpactfactorsType):
    return idf.newidfobject('ENVIRONMENTALIMPACTFACTORS', **kwargs)

def EvaporativecoolerDirectCeldekpad(idf, **kwargs: EvaporativecoolerDirectCeldekpadType):
    return idf.newidfobject('EVAPORATIVECOOLER:DIRECT:CELDEKPAD', **kwargs)

def EvaporativecoolerDirectResearchspecial(idf, **kwargs: EvaporativecoolerDirectResearchspecialType):
    return idf.newidfobject('EVAPORATIVECOOLER:DIRECT:RESEARCHSPECIAL', **kwargs)

def EvaporativecoolerIndirectCeldekpad(idf, **kwargs: EvaporativecoolerIndirectCeldekpadType):
    return idf.newidfobject('EVAPORATIVECOOLER:INDIRECT:CELDEKPAD', **kwargs)

def EvaporativecoolerIndirectResearchspecial(idf, **kwargs: EvaporativecoolerIndirectResearchspecialType):
    return idf.newidfobject('EVAPORATIVECOOLER:INDIRECT:RESEARCHSPECIAL', **kwargs)

def EvaporativecoolerIndirectWetcoil(idf, **kwargs: EvaporativecoolerIndirectWetcoilType):
    return idf.newidfobject('EVAPORATIVECOOLER:INDIRECT:WETCOIL', **kwargs)

def EvaporativefluidcoolerSinglespeed(idf, **kwargs: EvaporativefluidcoolerSinglespeedType):
    return idf.newidfobject('EVAPORATIVEFLUIDCOOLER:SINGLESPEED', **kwargs)

def EvaporativefluidcoolerTwospeed(idf, **kwargs: EvaporativefluidcoolerTwospeedType):
    return idf.newidfobject('EVAPORATIVEFLUIDCOOLER:TWOSPEED', **kwargs)

def ExteriorFuelequipment(idf, **kwargs: ExteriorFuelequipmentType):
    return idf.newidfobject('EXTERIOR:FUELEQUIPMENT', **kwargs)

def ExteriorLights(idf, **kwargs: ExteriorLightsType):
    return idf.newidfobject('EXTERIOR:LIGHTS', **kwargs)

def ExteriorWaterequipment(idf, **kwargs: ExteriorWaterequipmentType):
    return idf.newidfobject('EXTERIOR:WATEREQUIPMENT', **kwargs)

def Externalinterface(idf, **kwargs: ExternalinterfaceType):
    return idf.newidfobject('EXTERNALINTERFACE', **kwargs)

def ExternalinterfaceActuator(idf, **kwargs: ExternalinterfaceActuatorType):
    return idf.newidfobject('EXTERNALINTERFACE:ACTUATOR', **kwargs)

def ExternalinterfaceFunctionalmockupunitexportFromVariable(idf, **kwargs: ExternalinterfaceFunctionalmockupunitexportFromVariableType):
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITEXPORT:FROM:VARIABLE', **kwargs)

def ExternalinterfaceFunctionalmockupunitexportToActuator(idf, **kwargs: ExternalinterfaceFunctionalmockupunitexportToActuatorType):
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITEXPORT:TO:ACTUATOR', **kwargs)

def ExternalinterfaceFunctionalmockupunitexportToSchedule(idf, **kwargs: ExternalinterfaceFunctionalmockupunitexportToScheduleType):
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITEXPORT:TO:SCHEDULE', **kwargs)

def ExternalinterfaceFunctionalmockupunitexportToVariable(idf, **kwargs: ExternalinterfaceFunctionalmockupunitexportToVariableType):
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITEXPORT:TO:VARIABLE', **kwargs)

def ExternalinterfaceFunctionalmockupunitimport(idf, **kwargs: ExternalinterfaceFunctionalmockupunitimportType):
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT', **kwargs)

def ExternalinterfaceFunctionalmockupunitimportFromVariable(idf, **kwargs: ExternalinterfaceFunctionalmockupunitimportFromVariableType):
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT:FROM:VARIABLE', **kwargs)

def ExternalinterfaceFunctionalmockupunitimportToActuator(idf, **kwargs: ExternalinterfaceFunctionalmockupunitimportToActuatorType):
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT:TO:ACTUATOR', **kwargs)

def ExternalinterfaceFunctionalmockupunitimportToSchedule(idf, **kwargs: ExternalinterfaceFunctionalmockupunitimportToScheduleType):
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT:TO:SCHEDULE', **kwargs)

def ExternalinterfaceFunctionalmockupunitimportToVariable(idf, **kwargs: ExternalinterfaceFunctionalmockupunitimportToVariableType):
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT:TO:VARIABLE', **kwargs)

def ExternalinterfaceSchedule(idf, **kwargs: ExternalinterfaceScheduleType):
    return idf.newidfobject('EXTERNALINTERFACE:SCHEDULE', **kwargs)

def ExternalinterfaceVariable(idf, **kwargs: ExternalinterfaceVariableType):
    return idf.newidfobject('EXTERNALINTERFACE:VARIABLE', **kwargs)

def FanComponentmodel(idf, **kwargs: FanComponentmodelType):
    return idf.newidfobject('FAN:COMPONENTMODEL', **kwargs)

def FanConstantvolume(idf, **kwargs: FanConstantvolumeType):
    return idf.newidfobject('FAN:CONSTANTVOLUME', **kwargs)

def FanOnoff(idf, **kwargs: FanOnoffType):
    return idf.newidfobject('FAN:ONOFF', **kwargs)

def FanSystemmodel(idf, **kwargs: FanSystemmodelType):
    return idf.newidfobject('FAN:SYSTEMMODEL', **kwargs)

def FanVariablevolume(idf, **kwargs: FanVariablevolumeType):
    return idf.newidfobject('FAN:VARIABLEVOLUME', **kwargs)

def FanZoneexhaust(idf, **kwargs: FanZoneexhaustType):
    return idf.newidfobject('FAN:ZONEEXHAUST', **kwargs)

def FanperformanceNightventilation(idf, **kwargs: FanperformanceNightventilationType):
    return idf.newidfobject('FANPERFORMANCE:NIGHTVENTILATION', **kwargs)

def FaultmodelEnthalpysensoroffsetOutdoorair(idf, **kwargs: FaultmodelEnthalpysensoroffsetOutdoorairType):
    return idf.newidfobject('FAULTMODEL:ENTHALPYSENSOROFFSET:OUTDOORAIR', **kwargs)

def FaultmodelEnthalpysensoroffsetReturnair(idf, **kwargs: FaultmodelEnthalpysensoroffsetReturnairType):
    return idf.newidfobject('FAULTMODEL:ENTHALPYSENSOROFFSET:RETURNAIR', **kwargs)

def FaultmodelFoulingAirfilter(idf, **kwargs: FaultmodelFoulingAirfilterType):
    return idf.newidfobject('FAULTMODEL:FOULING:AIRFILTER', **kwargs)

def FaultmodelFoulingBoiler(idf, **kwargs: FaultmodelFoulingBoilerType):
    return idf.newidfobject('FAULTMODEL:FOULING:BOILER', **kwargs)

def FaultmodelFoulingChiller(idf, **kwargs: FaultmodelFoulingChillerType):
    return idf.newidfobject('FAULTMODEL:FOULING:CHILLER', **kwargs)

def FaultmodelFoulingCoil(idf, **kwargs: FaultmodelFoulingCoilType):
    return idf.newidfobject('FAULTMODEL:FOULING:COIL', **kwargs)

def FaultmodelFoulingCoolingtower(idf, **kwargs: FaultmodelFoulingCoolingtowerType):
    return idf.newidfobject('FAULTMODEL:FOULING:COOLINGTOWER', **kwargs)

def FaultmodelFoulingEvaporativecooler(idf, **kwargs: FaultmodelFoulingEvaporativecoolerType):
    return idf.newidfobject('FAULTMODEL:FOULING:EVAPORATIVECOOLER', **kwargs)

def FaultmodelHumidistatoffset(idf, **kwargs: FaultmodelHumidistatoffsetType):
    return idf.newidfobject('FAULTMODEL:HUMIDISTATOFFSET', **kwargs)

def FaultmodelHumiditysensoroffsetOutdoorair(idf, **kwargs: FaultmodelHumiditysensoroffsetOutdoorairType):
    return idf.newidfobject('FAULTMODEL:HUMIDITYSENSOROFFSET:OUTDOORAIR', **kwargs)

def FaultmodelTemperaturesensoroffsetChillersupplywater(idf, **kwargs: FaultmodelTemperaturesensoroffsetChillersupplywaterType):
    return idf.newidfobject('FAULTMODEL:TEMPERATURESENSOROFFSET:CHILLERSUPPLYWATER', **kwargs)

def FaultmodelTemperaturesensoroffsetCoilsupplyair(idf, **kwargs: FaultmodelTemperaturesensoroffsetCoilsupplyairType):
    return idf.newidfobject('FAULTMODEL:TEMPERATURESENSOROFFSET:COILSUPPLYAIR', **kwargs)

def FaultmodelTemperaturesensoroffsetCondensersupplywater(idf, **kwargs: FaultmodelTemperaturesensoroffsetCondensersupplywaterType):
    return idf.newidfobject('FAULTMODEL:TEMPERATURESENSOROFFSET:CONDENSERSUPPLYWATER', **kwargs)

def FaultmodelTemperaturesensoroffsetOutdoorair(idf, **kwargs: FaultmodelTemperaturesensoroffsetOutdoorairType):
    return idf.newidfobject('FAULTMODEL:TEMPERATURESENSOROFFSET:OUTDOORAIR', **kwargs)

def FaultmodelTemperaturesensoroffsetReturnair(idf, **kwargs: FaultmodelTemperaturesensoroffsetReturnairType):
    return idf.newidfobject('FAULTMODEL:TEMPERATURESENSOROFFSET:RETURNAIR', **kwargs)

def FaultmodelThermostatoffset(idf, **kwargs: FaultmodelThermostatoffsetType):
    return idf.newidfobject('FAULTMODEL:THERMOSTATOFFSET', **kwargs)

def FenestrationsurfaceDetailed(idf, **kwargs: FenestrationsurfaceDetailedType):
    return idf.newidfobject('FENESTRATIONSURFACE:DETAILED', **kwargs)

def FloorAdiabatic(idf, **kwargs: FloorAdiabaticType):
    return idf.newidfobject('FLOOR:ADIABATIC', **kwargs)

def FloorDetailed(idf, **kwargs: FloorDetailedType):
    return idf.newidfobject('FLOOR:DETAILED', **kwargs)

def FloorGroundcontact(idf, **kwargs: FloorGroundcontactType):
    return idf.newidfobject('FLOOR:GROUNDCONTACT', **kwargs)

def FloorInterzone(idf, **kwargs: FloorInterzoneType):
    return idf.newidfobject('FLOOR:INTERZONE', **kwargs)

def FluidcoolerSinglespeed(idf, **kwargs: FluidcoolerSinglespeedType):
    return idf.newidfobject('FLUIDCOOLER:SINGLESPEED', **kwargs)

def FluidcoolerTwospeed(idf, **kwargs: FluidcoolerTwospeedType):
    return idf.newidfobject('FLUIDCOOLER:TWOSPEED', **kwargs)

def FluidpropertiesConcentration(idf, **kwargs: FluidpropertiesConcentrationType):
    return idf.newidfobject('FLUIDPROPERTIES:CONCENTRATION', **kwargs)

def FluidpropertiesGlycolconcentration(idf, **kwargs: FluidpropertiesGlycolconcentrationType):
    return idf.newidfobject('FLUIDPROPERTIES:GLYCOLCONCENTRATION', **kwargs)

def FluidpropertiesName(idf, **kwargs: FluidpropertiesNameType):
    return idf.newidfobject('FLUIDPROPERTIES:NAME', **kwargs)

def FluidpropertiesSaturated(idf, **kwargs: FluidpropertiesSaturatedType):
    return idf.newidfobject('FLUIDPROPERTIES:SATURATED', **kwargs)

def FluidpropertiesSuperheated(idf, **kwargs: FluidpropertiesSuperheatedType):
    return idf.newidfobject('FLUIDPROPERTIES:SUPERHEATED', **kwargs)

def FluidpropertiesTemperatures(idf, **kwargs: FluidpropertiesTemperaturesType):
    return idf.newidfobject('FLUIDPROPERTIES:TEMPERATURES', **kwargs)

def FoundationKiva(idf, **kwargs: FoundationKivaType):
    return idf.newidfobject('FOUNDATION:KIVA', **kwargs)

def FoundationKivaSettings(idf, **kwargs: FoundationKivaSettingsType):
    return idf.newidfobject('FOUNDATION:KIVA:SETTINGS', **kwargs)

def Fuelfactors(idf, **kwargs: FuelfactorsType):
    return idf.newidfobject('FUELFACTORS', **kwargs)

def Gasequipment(idf, **kwargs: GasequipmentType):
    return idf.newidfobject('GASEQUIPMENT', **kwargs)

def GeneratorCombustionturbine(idf, **kwargs: GeneratorCombustionturbineType):
    return idf.newidfobject('GENERATOR:COMBUSTIONTURBINE', **kwargs)

def GeneratorFuelcell(idf, **kwargs: GeneratorFuelcellType):
    return idf.newidfobject('GENERATOR:FUELCELL', **kwargs)

def GeneratorFuelcellAirsupply(idf, **kwargs: GeneratorFuelcellAirsupplyType):
    return idf.newidfobject('GENERATOR:FUELCELL:AIRSUPPLY', **kwargs)

def GeneratorFuelcellAuxiliaryheater(idf, **kwargs: GeneratorFuelcellAuxiliaryheaterType):
    return idf.newidfobject('GENERATOR:FUELCELL:AUXILIARYHEATER', **kwargs)

def GeneratorFuelcellElectricalstorage(idf, **kwargs: GeneratorFuelcellElectricalstorageType):
    return idf.newidfobject('GENERATOR:FUELCELL:ELECTRICALSTORAGE', **kwargs)

def GeneratorFuelcellExhaustgastowaterheatexchanger(idf, **kwargs: GeneratorFuelcellExhaustgastowaterheatexchangerType):
    return idf.newidfobject('GENERATOR:FUELCELL:EXHAUSTGASTOWATERHEATEXCHANGER', **kwargs)

def GeneratorFuelcellInverter(idf, **kwargs: GeneratorFuelcellInverterType):
    return idf.newidfobject('GENERATOR:FUELCELL:INVERTER', **kwargs)

def GeneratorFuelcellPowermodule(idf, **kwargs: GeneratorFuelcellPowermoduleType):
    return idf.newidfobject('GENERATOR:FUELCELL:POWERMODULE', **kwargs)

def GeneratorFuelcellStackcooler(idf, **kwargs: GeneratorFuelcellStackcoolerType):
    return idf.newidfobject('GENERATOR:FUELCELL:STACKCOOLER', **kwargs)

def GeneratorFuelcellWatersupply(idf, **kwargs: GeneratorFuelcellWatersupplyType):
    return idf.newidfobject('GENERATOR:FUELCELL:WATERSUPPLY', **kwargs)

def GeneratorFuelsupply(idf, **kwargs: GeneratorFuelsupplyType):
    return idf.newidfobject('GENERATOR:FUELSUPPLY', **kwargs)

def GeneratorInternalcombustionengine(idf, **kwargs: GeneratorInternalcombustionengineType):
    return idf.newidfobject('GENERATOR:INTERNALCOMBUSTIONENGINE', **kwargs)

def GeneratorMicrochp(idf, **kwargs: GeneratorMicrochpType):
    return idf.newidfobject('GENERATOR:MICROCHP', **kwargs)

def GeneratorMicrochpNonnormalizedparameters(idf, **kwargs: GeneratorMicrochpNonnormalizedparametersType):
    return idf.newidfobject('GENERATOR:MICROCHP:NONNORMALIZEDPARAMETERS', **kwargs)

def GeneratorMicroturbine(idf, **kwargs: GeneratorMicroturbineType):
    return idf.newidfobject('GENERATOR:MICROTURBINE', **kwargs)

def GeneratorPhotovoltaic(idf, **kwargs: GeneratorPhotovoltaicType):
    return idf.newidfobject('GENERATOR:PHOTOVOLTAIC', **kwargs)

def GeneratorPvwatts(idf, **kwargs: GeneratorPvwattsType):
    return idf.newidfobject('GENERATOR:PVWATTS', **kwargs)

def GeneratorWindturbine(idf, **kwargs: GeneratorWindturbineType):
    return idf.newidfobject('GENERATOR:WINDTURBINE', **kwargs)

def Geometrytransform(idf, **kwargs: GeometrytransformType):
    return idf.newidfobject('GEOMETRYTRANSFORM', **kwargs)

def Glazeddoor(idf, **kwargs: GlazeddoorType):
    return idf.newidfobject('GLAZEDDOOR', **kwargs)

def GlazeddoorInterzone(idf, **kwargs: GlazeddoorInterzoneType):
    return idf.newidfobject('GLAZEDDOOR:INTERZONE', **kwargs)

def Globalgeometryrules(idf, **kwargs: GlobalgeometryrulesType):
    return idf.newidfobject('GLOBALGEOMETRYRULES', **kwargs)

def GroundheatexchangerHorizontaltrench(idf, **kwargs: GroundheatexchangerHorizontaltrenchType):
    return idf.newidfobject('GROUNDHEATEXCHANGER:HORIZONTALTRENCH', **kwargs)

def GroundheatexchangerPond(idf, **kwargs: GroundheatexchangerPondType):
    return idf.newidfobject('GROUNDHEATEXCHANGER:POND', **kwargs)

def GroundheatexchangerResponsefactors(idf, **kwargs: GroundheatexchangerResponsefactorsType):
    return idf.newidfobject('GROUNDHEATEXCHANGER:RESPONSEFACTORS', **kwargs)

def GroundheatexchangerSlinky(idf, **kwargs: GroundheatexchangerSlinkyType):
    return idf.newidfobject('GROUNDHEATEXCHANGER:SLINKY', **kwargs)

def GroundheatexchangerSurface(idf, **kwargs: GroundheatexchangerSurfaceType):
    return idf.newidfobject('GROUNDHEATEXCHANGER:SURFACE', **kwargs)

def GroundheatexchangerSystem(idf, **kwargs: GroundheatexchangerSystemType):
    return idf.newidfobject('GROUNDHEATEXCHANGER:SYSTEM', **kwargs)

def GroundheatexchangerVerticalArray(idf, **kwargs: GroundheatexchangerVerticalArrayType):
    return idf.newidfobject('GROUNDHEATEXCHANGER:VERTICAL:ARRAY', **kwargs)

def GroundheatexchangerVerticalProperties(idf, **kwargs: GroundheatexchangerVerticalPropertiesType):
    return idf.newidfobject('GROUNDHEATEXCHANGER:VERTICAL:PROPERTIES', **kwargs)

def GroundheatexchangerVerticalSingle(idf, **kwargs: GroundheatexchangerVerticalSingleType):
    return idf.newidfobject('GROUNDHEATEXCHANGER:VERTICAL:SINGLE', **kwargs)

def GroundheattransferBasementAutogrid(idf, **kwargs: GroundheattransferBasementAutogridType):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:AUTOGRID', **kwargs)

def GroundheattransferBasementBldgdata(idf, **kwargs: GroundheattransferBasementBldgdataType):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:BLDGDATA', **kwargs)

def GroundheattransferBasementCombldg(idf, **kwargs: GroundheattransferBasementCombldgType):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:COMBLDG', **kwargs)

def GroundheattransferBasementEquivautogrid(idf, **kwargs: GroundheattransferBasementEquivautogridType):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:EQUIVAUTOGRID', **kwargs)

def GroundheattransferBasementEquivslab(idf, **kwargs: GroundheattransferBasementEquivslabType):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:EQUIVSLAB', **kwargs)

def GroundheattransferBasementInsulation(idf, **kwargs: GroundheattransferBasementInsulationType):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:INSULATION', **kwargs)

def GroundheattransferBasementInterior(idf, **kwargs: GroundheattransferBasementInteriorType):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:INTERIOR', **kwargs)

def GroundheattransferBasementManualgrid(idf, **kwargs: GroundheattransferBasementManualgridType):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:MANUALGRID', **kwargs)

def GroundheattransferBasementMatlprops(idf, **kwargs: GroundheattransferBasementMatlpropsType):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:MATLPROPS', **kwargs)

def GroundheattransferBasementSimparameters(idf, **kwargs: GroundheattransferBasementSimparametersType):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:SIMPARAMETERS', **kwargs)

def GroundheattransferBasementSurfaceprops(idf, **kwargs: GroundheattransferBasementSurfacepropsType):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:SURFACEPROPS', **kwargs)

def GroundheattransferBasementXface(idf, **kwargs: GroundheattransferBasementXfaceType):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:XFACE', **kwargs)

def GroundheattransferBasementYface(idf, **kwargs: GroundheattransferBasementYfaceType):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:YFACE', **kwargs)

def GroundheattransferBasementZface(idf, **kwargs: GroundheattransferBasementZfaceType):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:ZFACE', **kwargs)

def GroundheattransferControl(idf, **kwargs: GroundheattransferControlType):
    return idf.newidfobject('GROUNDHEATTRANSFER:CONTROL', **kwargs)

def GroundheattransferSlabAutogrid(idf, **kwargs: GroundheattransferSlabAutogridType):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:AUTOGRID', **kwargs)

def GroundheattransferSlabBldgprops(idf, **kwargs: GroundheattransferSlabBldgpropsType):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:BLDGPROPS', **kwargs)

def GroundheattransferSlabBoundconds(idf, **kwargs: GroundheattransferSlabBoundcondsType):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:BOUNDCONDS', **kwargs)

def GroundheattransferSlabEquivalentslab(idf, **kwargs: GroundheattransferSlabEquivalentslabType):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:EQUIVALENTSLAB', **kwargs)

def GroundheattransferSlabInsulation(idf, **kwargs: GroundheattransferSlabInsulationType):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:INSULATION', **kwargs)

def GroundheattransferSlabManualgrid(idf, **kwargs: GroundheattransferSlabManualgridType):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:MANUALGRID', **kwargs)

def GroundheattransferSlabMaterials(idf, **kwargs: GroundheattransferSlabMaterialsType):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:MATERIALS', **kwargs)

def GroundheattransferSlabMatlprops(idf, **kwargs: GroundheattransferSlabMatlpropsType):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:MATLPROPS', **kwargs)

def GroundheattransferSlabXface(idf, **kwargs: GroundheattransferSlabXfaceType):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:XFACE', **kwargs)

def GroundheattransferSlabYface(idf, **kwargs: GroundheattransferSlabYfaceType):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:YFACE', **kwargs)

def GroundheattransferSlabZface(idf, **kwargs: GroundheattransferSlabZfaceType):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:ZFACE', **kwargs)

def HeaderedpumpsConstantspeed(idf, **kwargs: HeaderedpumpsConstantspeedType):
    return idf.newidfobject('HEADEREDPUMPS:CONSTANTSPEED', **kwargs)

def HeaderedpumpsVariablespeed(idf, **kwargs: HeaderedpumpsVariablespeedType):
    return idf.newidfobject('HEADEREDPUMPS:VARIABLESPEED', **kwargs)

def Heatbalancealgorithm(idf, **kwargs: HeatbalancealgorithmType):
    return idf.newidfobject('HEATBALANCEALGORITHM', **kwargs)

def HeatbalancesettingsConductionfinitedifference(idf, **kwargs: HeatbalancesettingsConductionfinitedifferenceType):
    return idf.newidfobject('HEATBALANCESETTINGS:CONDUCTIONFINITEDIFFERENCE', **kwargs)

def HeatexchangerAirtoairFlatplate(idf, **kwargs: HeatexchangerAirtoairFlatplateType):
    return idf.newidfobject('HEATEXCHANGER:AIRTOAIR:FLATPLATE', **kwargs)

def HeatexchangerAirtoairSensibleandlatent(idf, **kwargs: HeatexchangerAirtoairSensibleandlatentType):
    return idf.newidfobject('HEATEXCHANGER:AIRTOAIR:SENSIBLEANDLATENT', **kwargs)

def HeatexchangerDesiccantBalancedflow(idf, **kwargs: HeatexchangerDesiccantBalancedflowType):
    return idf.newidfobject('HEATEXCHANGER:DESICCANT:BALANCEDFLOW', **kwargs)

def HeatexchangerDesiccantBalancedflowPerformancedatatype1(idf, **kwargs: HeatexchangerDesiccantBalancedflowPerformancedatatype1Type):
    return idf.newidfobject('HEATEXCHANGER:DESICCANT:BALANCEDFLOW:PERFORMANCEDATATYPE1', **kwargs)

def HeatexchangerFluidtofluid(idf, **kwargs: HeatexchangerFluidtofluidType):
    return idf.newidfobject('HEATEXCHANGER:FLUIDTOFLUID', **kwargs)

def HeatpumpAirtowaterFuelfiredCooling(idf, **kwargs: HeatpumpAirtowaterFuelfiredCoolingType):
    return idf.newidfobject('HEATPUMP:AIRTOWATER:FUELFIRED:COOLING', **kwargs)

def HeatpumpAirtowaterFuelfiredHeating(idf, **kwargs: HeatpumpAirtowaterFuelfiredHeatingType):
    return idf.newidfobject('HEATPUMP:AIRTOWATER:FUELFIRED:HEATING', **kwargs)

def HeatpumpPlantloopEirCooling(idf, **kwargs: HeatpumpPlantloopEirCoolingType):
    return idf.newidfobject('HEATPUMP:PLANTLOOP:EIR:COOLING', **kwargs)

def HeatpumpPlantloopEirHeating(idf, **kwargs: HeatpumpPlantloopEirHeatingType):
    return idf.newidfobject('HEATPUMP:PLANTLOOP:EIR:HEATING', **kwargs)

def HeatpumpWatertowaterEquationfitCooling(idf, **kwargs: HeatpumpWatertowaterEquationfitCoolingType):
    return idf.newidfobject('HEATPUMP:WATERTOWATER:EQUATIONFIT:COOLING', **kwargs)

def HeatpumpWatertowaterEquationfitHeating(idf, **kwargs: HeatpumpWatertowaterEquationfitHeatingType):
    return idf.newidfobject('HEATPUMP:WATERTOWATER:EQUATIONFIT:HEATING', **kwargs)

def HeatpumpWatertowaterParameterestimationCooling(idf, **kwargs: HeatpumpWatertowaterParameterestimationCoolingType):
    return idf.newidfobject('HEATPUMP:WATERTOWATER:PARAMETERESTIMATION:COOLING', **kwargs)

def HeatpumpWatertowaterParameterestimationHeating(idf, **kwargs: HeatpumpWatertowaterParameterestimationHeatingType):
    return idf.newidfobject('HEATPUMP:WATERTOWATER:PARAMETERESTIMATION:HEATING', **kwargs)

def Hotwaterequipment(idf, **kwargs: HotwaterequipmentType):
    return idf.newidfobject('HOTWATEREQUIPMENT', **kwargs)

def HumidifierSteamElectric(idf, **kwargs: HumidifierSteamElectricType):
    return idf.newidfobject('HUMIDIFIER:STEAM:ELECTRIC', **kwargs)

def HumidifierSteamGas(idf, **kwargs: HumidifierSteamGasType):
    return idf.newidfobject('HUMIDIFIER:STEAM:GAS', **kwargs)

def Hvacsystemrootfindingalgorithm(idf, **kwargs: HvacsystemrootfindingalgorithmType):
    return idf.newidfobject('HVACSYSTEMROOTFINDINGALGORITHM', **kwargs)

def HvactemplatePlantBoiler(idf, **kwargs: HvactemplatePlantBoilerType):
    return idf.newidfobject('HVACTEMPLATE:PLANT:BOILER', **kwargs)

def HvactemplatePlantBoilerObjectreference(idf, **kwargs: HvactemplatePlantBoilerObjectreferenceType):
    return idf.newidfobject('HVACTEMPLATE:PLANT:BOILER:OBJECTREFERENCE', **kwargs)

def HvactemplatePlantChilledwaterloop(idf, **kwargs: HvactemplatePlantChilledwaterloopType):
    return idf.newidfobject('HVACTEMPLATE:PLANT:CHILLEDWATERLOOP', **kwargs)

def HvactemplatePlantChiller(idf, **kwargs: HvactemplatePlantChillerType):
    return idf.newidfobject('HVACTEMPLATE:PLANT:CHILLER', **kwargs)

def HvactemplatePlantChillerObjectreference(idf, **kwargs: HvactemplatePlantChillerObjectreferenceType):
    return idf.newidfobject('HVACTEMPLATE:PLANT:CHILLER:OBJECTREFERENCE', **kwargs)

def HvactemplatePlantHotwaterloop(idf, **kwargs: HvactemplatePlantHotwaterloopType):
    return idf.newidfobject('HVACTEMPLATE:PLANT:HOTWATERLOOP', **kwargs)

def HvactemplatePlantMixedwaterloop(idf, **kwargs: HvactemplatePlantMixedwaterloopType):
    return idf.newidfobject('HVACTEMPLATE:PLANT:MIXEDWATERLOOP', **kwargs)

def HvactemplatePlantTower(idf, **kwargs: HvactemplatePlantTowerType):
    return idf.newidfobject('HVACTEMPLATE:PLANT:TOWER', **kwargs)

def HvactemplatePlantTowerObjectreference(idf, **kwargs: HvactemplatePlantTowerObjectreferenceType):
    return idf.newidfobject('HVACTEMPLATE:PLANT:TOWER:OBJECTREFERENCE', **kwargs)

def HvactemplateSystemConstantvolume(idf, **kwargs: HvactemplateSystemConstantvolumeType):
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:CONSTANTVOLUME', **kwargs)

def HvactemplateSystemDedicatedoutdoorair(idf, **kwargs: HvactemplateSystemDedicatedoutdoorairType):
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:DEDICATEDOUTDOORAIR', **kwargs)

def HvactemplateSystemDualduct(idf, **kwargs: HvactemplateSystemDualductType):
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:DUALDUCT', **kwargs)

def HvactemplateSystemPackagedvav(idf, **kwargs: HvactemplateSystemPackagedvavType):
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:PACKAGEDVAV', **kwargs)

def HvactemplateSystemUnitary(idf, **kwargs: HvactemplateSystemUnitaryType):
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:UNITARY', **kwargs)

def HvactemplateSystemUnitaryheatpumpAirtoair(idf, **kwargs: HvactemplateSystemUnitaryheatpumpAirtoairType):
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:UNITARYHEATPUMP:AIRTOAIR', **kwargs)

def HvactemplateSystemUnitarysystem(idf, **kwargs: HvactemplateSystemUnitarysystemType):
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:UNITARYSYSTEM', **kwargs)

def HvactemplateSystemVav(idf, **kwargs: HvactemplateSystemVavType):
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:VAV', **kwargs)

def HvactemplateSystemVrf(idf, **kwargs: HvactemplateSystemVrfType):
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:VRF', **kwargs)

def HvactemplateThermostat(idf, **kwargs: HvactemplateThermostatType):
    return idf.newidfobject('HVACTEMPLATE:THERMOSTAT', **kwargs)

def HvactemplateZoneBaseboardheat(idf, **kwargs: HvactemplateZoneBaseboardheatType):
    return idf.newidfobject('HVACTEMPLATE:ZONE:BASEBOARDHEAT', **kwargs)

def HvactemplateZoneConstantvolume(idf, **kwargs: HvactemplateZoneConstantvolumeType):
    return idf.newidfobject('HVACTEMPLATE:ZONE:CONSTANTVOLUME', **kwargs)

def HvactemplateZoneDualduct(idf, **kwargs: HvactemplateZoneDualductType):
    return idf.newidfobject('HVACTEMPLATE:ZONE:DUALDUCT', **kwargs)

def HvactemplateZoneFancoil(idf, **kwargs: HvactemplateZoneFancoilType):
    return idf.newidfobject('HVACTEMPLATE:ZONE:FANCOIL', **kwargs)

def HvactemplateZoneIdealloadsairsystem(idf, **kwargs: HvactemplateZoneIdealloadsairsystemType):
    return idf.newidfobject('HVACTEMPLATE:ZONE:IDEALLOADSAIRSYSTEM', **kwargs)

def HvactemplateZonePtac(idf, **kwargs: HvactemplateZonePtacType):
    return idf.newidfobject('HVACTEMPLATE:ZONE:PTAC', **kwargs)

def HvactemplateZonePthp(idf, **kwargs: HvactemplateZonePthpType):
    return idf.newidfobject('HVACTEMPLATE:ZONE:PTHP', **kwargs)

def HvactemplateZoneUnitary(idf, **kwargs: HvactemplateZoneUnitaryType):
    return idf.newidfobject('HVACTEMPLATE:ZONE:UNITARY', **kwargs)

def HvactemplateZoneVav(idf, **kwargs: HvactemplateZoneVavType):
    return idf.newidfobject('HVACTEMPLATE:ZONE:VAV', **kwargs)

def HvactemplateZoneVavFanpowered(idf, **kwargs: HvactemplateZoneVavFanpoweredType):
    return idf.newidfobject('HVACTEMPLATE:ZONE:VAV:FANPOWERED', **kwargs)

def HvactemplateZoneVavHeatandcool(idf, **kwargs: HvactemplateZoneVavHeatandcoolType):
    return idf.newidfobject('HVACTEMPLATE:ZONE:VAV:HEATANDCOOL', **kwargs)

def HvactemplateZoneVrf(idf, **kwargs: HvactemplateZoneVrfType):
    return idf.newidfobject('HVACTEMPLATE:ZONE:VRF', **kwargs)

def HvactemplateZoneWatertoairheatpump(idf, **kwargs: HvactemplateZoneWatertoairheatpumpType):
    return idf.newidfobject('HVACTEMPLATE:ZONE:WATERTOAIRHEATPUMP', **kwargs)

def HybridmodelZone(idf, **kwargs: HybridmodelZoneType):
    return idf.newidfobject('HYBRIDMODEL:ZONE', **kwargs)

def Indoorlivingwall(idf, **kwargs: IndoorlivingwallType):
    return idf.newidfobject('INDOORLIVINGWALL', **kwargs)

def Internalmass(idf, **kwargs: InternalmassType):
    return idf.newidfobject('INTERNALMASS', **kwargs)

def LifecyclecostNonrecurringcost(idf, **kwargs: LifecyclecostNonrecurringcostType):
    return idf.newidfobject('LIFECYCLECOST:NONRECURRINGCOST', **kwargs)

def LifecyclecostParameters(idf, **kwargs: LifecyclecostParametersType):
    return idf.newidfobject('LIFECYCLECOST:PARAMETERS', **kwargs)

def LifecyclecostRecurringcosts(idf, **kwargs: LifecyclecostRecurringcostsType):
    return idf.newidfobject('LIFECYCLECOST:RECURRINGCOSTS', **kwargs)

def LifecyclecostUseadjustment(idf, **kwargs: LifecyclecostUseadjustmentType):
    return idf.newidfobject('LIFECYCLECOST:USEADJUSTMENT', **kwargs)

def LifecyclecostUsepriceescalation(idf, **kwargs: LifecyclecostUsepriceescalationType):
    return idf.newidfobject('LIFECYCLECOST:USEPRICEESCALATION', **kwargs)

def Lights(idf, **kwargs: LightsType):
    return idf.newidfobject('LIGHTS', **kwargs)

def LoadprofilePlant(idf, **kwargs: LoadprofilePlantType):
    return idf.newidfobject('LOADPROFILE:PLANT', **kwargs)

def Material(idf, **kwargs: MaterialType):
    return idf.newidfobject('MATERIAL', **kwargs)

def MaterialAirgap(idf, **kwargs: MaterialAirgapType):
    return idf.newidfobject('MATERIAL:AIRGAP', **kwargs)

def MaterialInfraredtransparent(idf, **kwargs: MaterialInfraredtransparentType):
    return idf.newidfobject('MATERIAL:INFRAREDTRANSPARENT', **kwargs)

def MaterialNomass(idf, **kwargs: MaterialNomassType):
    return idf.newidfobject('MATERIAL:NOMASS', **kwargs)

def MaterialRoofvegetation(idf, **kwargs: MaterialRoofvegetationType):
    return idf.newidfobject('MATERIAL:ROOFVEGETATION', **kwargs)

def MaterialpropertyGlazingspectraldata(idf, **kwargs: MaterialpropertyGlazingspectraldataType):
    return idf.newidfobject('MATERIALPROPERTY:GLAZINGSPECTRALDATA', **kwargs)

def MaterialpropertyHeatandmoisturetransferDiffusion(idf, **kwargs: MaterialpropertyHeatandmoisturetransferDiffusionType):
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:DIFFUSION', **kwargs)

def MaterialpropertyHeatandmoisturetransferRedistribution(idf, **kwargs: MaterialpropertyHeatandmoisturetransferRedistributionType):
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:REDISTRIBUTION', **kwargs)

def MaterialpropertyHeatandmoisturetransferSettings(idf, **kwargs: MaterialpropertyHeatandmoisturetransferSettingsType):
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:SETTINGS', **kwargs)

def MaterialpropertyHeatandmoisturetransferSorptionisotherm(idf, **kwargs: MaterialpropertyHeatandmoisturetransferSorptionisothermType):
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:SORPTIONISOTHERM', **kwargs)

def MaterialpropertyHeatandmoisturetransferSuction(idf, **kwargs: MaterialpropertyHeatandmoisturetransferSuctionType):
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:SUCTION', **kwargs)

def MaterialpropertyHeatandmoisturetransferThermalconductivity(idf, **kwargs: MaterialpropertyHeatandmoisturetransferThermalconductivityType):
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:THERMALCONDUCTIVITY', **kwargs)

def MaterialpropertyMoisturepenetrationdepthSettings(idf, **kwargs: MaterialpropertyMoisturepenetrationdepthSettingsType):
    return idf.newidfobject('MATERIALPROPERTY:MOISTUREPENETRATIONDEPTH:SETTINGS', **kwargs)

def MaterialpropertyPhasechange(idf, **kwargs: MaterialpropertyPhasechangeType):
    return idf.newidfobject('MATERIALPROPERTY:PHASECHANGE', **kwargs)

def MaterialpropertyPhasechangehysteresis(idf, **kwargs: MaterialpropertyPhasechangehysteresisType):
    return idf.newidfobject('MATERIALPROPERTY:PHASECHANGEHYSTERESIS', **kwargs)

def MaterialpropertyVariableabsorptance(idf, **kwargs: MaterialpropertyVariableabsorptanceType):
    return idf.newidfobject('MATERIALPROPERTY:VARIABLEABSORPTANCE', **kwargs)

def MaterialpropertyVariablethermalconductivity(idf, **kwargs: MaterialpropertyVariablethermalconductivityType):
    return idf.newidfobject('MATERIALPROPERTY:VARIABLETHERMALCONDUCTIVITY', **kwargs)

def MatrixTwodimension(idf, **kwargs: MatrixTwodimensionType):
    return idf.newidfobject('MATRIX:TWODIMENSION', **kwargs)

def MeterCustom(idf, **kwargs: MeterCustomType):
    return idf.newidfobject('METER:CUSTOM', **kwargs)

def MeterCustomdecrement(idf, **kwargs: MeterCustomdecrementType):
    return idf.newidfobject('METER:CUSTOMDECREMENT', **kwargs)

def Nodelist(idf, **kwargs: NodelistType):
    return idf.newidfobject('NODELIST', **kwargs)

def Otherequipment(idf, **kwargs: OtherequipmentType):
    return idf.newidfobject('OTHEREQUIPMENT', **kwargs)

def OutdoorairMixer(idf, **kwargs: OutdoorairMixerType):
    return idf.newidfobject('OUTDOORAIR:MIXER', **kwargs)

def OutdoorairNode(idf, **kwargs: OutdoorairNodeType):
    return idf.newidfobject('OUTDOORAIR:NODE', **kwargs)

def OutdoorairNodelist(idf, **kwargs: OutdoorairNodelistType):
    return idf.newidfobject('OUTDOORAIR:NODELIST', **kwargs)

def OutputConstructions(idf, **kwargs: OutputConstructionsType):
    return idf.newidfobject('OUTPUT:CONSTRUCTIONS', **kwargs)

def OutputDaylightfactors(idf, **kwargs: OutputDaylightfactorsType):
    return idf.newidfobject('OUTPUT:DAYLIGHTFACTORS', **kwargs)

def OutputDebuggingdata(idf, **kwargs: OutputDebuggingdataType):
    return idf.newidfobject('OUTPUT:DEBUGGINGDATA', **kwargs)

def OutputDiagnostics(idf, **kwargs: OutputDiagnosticsType):
    return idf.newidfobject('OUTPUT:DIAGNOSTICS', **kwargs)

def OutputEnergymanagementsystem(idf, **kwargs: OutputEnergymanagementsystemType):
    return idf.newidfobject('OUTPUT:ENERGYMANAGEMENTSYSTEM', **kwargs)

def OutputEnvironmentalimpactfactors(idf, **kwargs: OutputEnvironmentalimpactfactorsType):
    return idf.newidfobject('OUTPUT:ENVIRONMENTALIMPACTFACTORS', **kwargs)

def OutputIlluminancemap(idf, **kwargs: OutputIlluminancemapType):
    return idf.newidfobject('OUTPUT:ILLUMINANCEMAP', **kwargs)

def OutputJson(idf, **kwargs: OutputJsonType):
    return idf.newidfobject('OUTPUT:JSON', **kwargs)

def OutputMeter(idf, **kwargs: OutputMeterType):
    return idf.newidfobject('OUTPUT:METER', **kwargs)

def OutputMeterCumulative(idf, **kwargs: OutputMeterCumulativeType):
    return idf.newidfobject('OUTPUT:METER:CUMULATIVE', **kwargs)

def OutputMeterCumulativeMeterfileonly(idf, **kwargs: OutputMeterCumulativeMeterfileonlyType):
    return idf.newidfobject('OUTPUT:METER:CUMULATIVE:METERFILEONLY', **kwargs)

def OutputMeterMeterfileonly(idf, **kwargs: OutputMeterMeterfileonlyType):
    return idf.newidfobject('OUTPUT:METER:METERFILEONLY', **kwargs)

def OutputPreprocessormessage(idf, **kwargs: OutputPreprocessormessageType):
    return idf.newidfobject('OUTPUT:PREPROCESSORMESSAGE', **kwargs)

def OutputSchedules(idf, **kwargs: OutputSchedulesType):
    return idf.newidfobject('OUTPUT:SCHEDULES', **kwargs)

def OutputSqlite(idf, **kwargs: OutputSqliteType):
    return idf.newidfobject('OUTPUT:SQLITE', **kwargs)

def OutputSurfacesDrawing(idf, **kwargs: OutputSurfacesDrawingType):
    return idf.newidfobject('OUTPUT:SURFACES:DRAWING', **kwargs)

def OutputSurfacesList(idf, **kwargs: OutputSurfacesListType):
    return idf.newidfobject('OUTPUT:SURFACES:LIST', **kwargs)

def OutputTableAnnual(idf, **kwargs: OutputTableAnnualType):
    return idf.newidfobject('OUTPUT:TABLE:ANNUAL', **kwargs)

def OutputTableMonthly(idf, **kwargs: OutputTableMonthlyType):
    return idf.newidfobject('OUTPUT:TABLE:MONTHLY', **kwargs)

def OutputTableReportperiod(idf, **kwargs: OutputTableReportperiodType):
    return idf.newidfobject('OUTPUT:TABLE:REPORTPERIOD', **kwargs)

def OutputTableSummaryreports(idf, **kwargs: OutputTableSummaryreportsType):
    return idf.newidfobject('OUTPUT:TABLE:SUMMARYREPORTS', **kwargs)

def OutputTableTimebins(idf, **kwargs: OutputTableTimebinsType):
    return idf.newidfobject('OUTPUT:TABLE:TIMEBINS', **kwargs)

def OutputVariable(idf, **kwargs: OutputVariableType):
    return idf.newidfobject('OUTPUT:VARIABLE', **kwargs)

def OutputVariabledictionary(idf, **kwargs: OutputVariabledictionaryType):
    return idf.newidfobject('OUTPUT:VARIABLEDICTIONARY', **kwargs)

def OutputcontrolFiles(idf, **kwargs: OutputcontrolFilesType):
    return idf.newidfobject('OUTPUTCONTROL:FILES', **kwargs)

def OutputcontrolIlluminancemapStyle(idf, **kwargs: OutputcontrolIlluminancemapStyleType):
    return idf.newidfobject('OUTPUTCONTROL:ILLUMINANCEMAP:STYLE', **kwargs)

def OutputcontrolReportingtolerances(idf, **kwargs: OutputcontrolReportingtolerancesType):
    return idf.newidfobject('OUTPUTCONTROL:REPORTINGTOLERANCES', **kwargs)

def OutputcontrolSizingStyle(idf, **kwargs: OutputcontrolSizingStyleType):
    return idf.newidfobject('OUTPUTCONTROL:SIZING:STYLE', **kwargs)

def OutputcontrolSurfacecolorscheme(idf, **kwargs: OutputcontrolSurfacecolorschemeType):
    return idf.newidfobject('OUTPUTCONTROL:SURFACECOLORSCHEME', **kwargs)

def OutputcontrolTableStyle(idf, **kwargs: OutputcontrolTableStyleType):
    return idf.newidfobject('OUTPUTCONTROL:TABLE:STYLE', **kwargs)

def OutputcontrolTimestamp(idf, **kwargs: OutputcontrolTimestampType):
    return idf.newidfobject('OUTPUTCONTROL:TIMESTAMP', **kwargs)

def ParametricFilenamesuffix(idf, **kwargs: ParametricFilenamesuffixType):
    return idf.newidfobject('PARAMETRIC:FILENAMESUFFIX', **kwargs)

def ParametricLogic(idf, **kwargs: ParametricLogicType):
    return idf.newidfobject('PARAMETRIC:LOGIC', **kwargs)

def ParametricRuncontrol(idf, **kwargs: ParametricRuncontrolType):
    return idf.newidfobject('PARAMETRIC:RUNCONTROL', **kwargs)

def ParametricSetvalueforrun(idf, **kwargs: ParametricSetvalueforrunType):
    return idf.newidfobject('PARAMETRIC:SETVALUEFORRUN', **kwargs)

def People(idf, **kwargs: PeopleType):
    return idf.newidfobject('PEOPLE', **kwargs)

def Performanceprecisiontradeoffs(idf, **kwargs: PerformanceprecisiontradeoffsType):
    return idf.newidfobject('PERFORMANCEPRECISIONTRADEOFFS', **kwargs)

def PhotovoltaicperformanceEquivalentonediode(idf, **kwargs: PhotovoltaicperformanceEquivalentonediodeType):
    return idf.newidfobject('PHOTOVOLTAICPERFORMANCE:EQUIVALENTONE-DIODE', **kwargs)

def PhotovoltaicperformanceSandia(idf, **kwargs: PhotovoltaicperformanceSandiaType):
    return idf.newidfobject('PHOTOVOLTAICPERFORMANCE:SANDIA', **kwargs)

def PhotovoltaicperformanceSimple(idf, **kwargs: PhotovoltaicperformanceSimpleType):
    return idf.newidfobject('PHOTOVOLTAICPERFORMANCE:SIMPLE', **kwargs)

def PipeAdiabatic(idf, **kwargs: PipeAdiabaticType):
    return idf.newidfobject('PIPE:ADIABATIC', **kwargs)

def PipeAdiabaticSteam(idf, **kwargs: PipeAdiabaticSteamType):
    return idf.newidfobject('PIPE:ADIABATIC:STEAM', **kwargs)

def PipeIndoor(idf, **kwargs: PipeIndoorType):
    return idf.newidfobject('PIPE:INDOOR', **kwargs)

def PipeOutdoor(idf, **kwargs: PipeOutdoorType):
    return idf.newidfobject('PIPE:OUTDOOR', **kwargs)

def PipeUnderground(idf, **kwargs: PipeUndergroundType):
    return idf.newidfobject('PIPE:UNDERGROUND', **kwargs)

def PipingsystemUndergroundDomain(idf, **kwargs: PipingsystemUndergroundDomainType):
    return idf.newidfobject('PIPINGSYSTEM:UNDERGROUND:DOMAIN', **kwargs)

def PipingsystemUndergroundPipecircuit(idf, **kwargs: PipingsystemUndergroundPipecircuitType):
    return idf.newidfobject('PIPINGSYSTEM:UNDERGROUND:PIPECIRCUIT', **kwargs)

def PipingsystemUndergroundPipesegment(idf, **kwargs: PipingsystemUndergroundPipesegmentType):
    return idf.newidfobject('PIPINGSYSTEM:UNDERGROUND:PIPESEGMENT', **kwargs)

def PlantcomponentTemperaturesource(idf, **kwargs: PlantcomponentTemperaturesourceType):
    return idf.newidfobject('PLANTCOMPONENT:TEMPERATURESOURCE', **kwargs)

def PlantcomponentUserdefined(idf, **kwargs: PlantcomponentUserdefinedType):
    return idf.newidfobject('PLANTCOMPONENT:USERDEFINED', **kwargs)

def Plantequipmentlist(idf, **kwargs: PlantequipmentlistType):
    return idf.newidfobject('PLANTEQUIPMENTLIST', **kwargs)

def PlantequipmentoperationChillerheaterchangeover(idf, **kwargs: PlantequipmentoperationChillerheaterchangeoverType):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:CHILLERHEATERCHANGEOVER', **kwargs)

def PlantequipmentoperationComponentsetpoint(idf, **kwargs: PlantequipmentoperationComponentsetpointType):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:COMPONENTSETPOINT', **kwargs)

def PlantequipmentoperationCoolingload(idf, **kwargs: PlantequipmentoperationCoolingloadType):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:COOLINGLOAD', **kwargs)

def PlantequipmentoperationHeatingload(idf, **kwargs: PlantequipmentoperationHeatingloadType):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:HEATINGLOAD', **kwargs)

def PlantequipmentoperationOutdoordewpoint(idf, **kwargs: PlantequipmentoperationOutdoordewpointType):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORDEWPOINT', **kwargs)

def PlantequipmentoperationOutdoordewpointdifference(idf, **kwargs: PlantequipmentoperationOutdoordewpointdifferenceType):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORDEWPOINTDIFFERENCE', **kwargs)

def PlantequipmentoperationOutdoordrybulb(idf, **kwargs: PlantequipmentoperationOutdoordrybulbType):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORDRYBULB', **kwargs)

def PlantequipmentoperationOutdoordrybulbdifference(idf, **kwargs: PlantequipmentoperationOutdoordrybulbdifferenceType):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORDRYBULBDIFFERENCE', **kwargs)

def PlantequipmentoperationOutdoorrelativehumidity(idf, **kwargs: PlantequipmentoperationOutdoorrelativehumidityType):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORRELATIVEHUMIDITY', **kwargs)

def PlantequipmentoperationOutdoorwetbulb(idf, **kwargs: PlantequipmentoperationOutdoorwetbulbType):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORWETBULB', **kwargs)

def PlantequipmentoperationOutdoorwetbulbdifference(idf, **kwargs: PlantequipmentoperationOutdoorwetbulbdifferenceType):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORWETBULBDIFFERENCE', **kwargs)

def PlantequipmentoperationThermalenergystorage(idf, **kwargs: PlantequipmentoperationThermalenergystorageType):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:THERMALENERGYSTORAGE', **kwargs)

def PlantequipmentoperationUncontrolled(idf, **kwargs: PlantequipmentoperationUncontrolledType):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:UNCONTROLLED', **kwargs)

def PlantequipmentoperationUserdefined(idf, **kwargs: PlantequipmentoperationUserdefinedType):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:USERDEFINED', **kwargs)

def Plantequipmentoperationschemes(idf, **kwargs: PlantequipmentoperationschemesType):
    return idf.newidfobject('PLANTEQUIPMENTOPERATIONSCHEMES', **kwargs)

def Plantloop(idf, **kwargs: PlantloopType):
    return idf.newidfobject('PLANTLOOP', **kwargs)

def PumpConstantspeed(idf, **kwargs: PumpConstantspeedType):
    return idf.newidfobject('PUMP:CONSTANTSPEED', **kwargs)

def PumpVariablespeed(idf, **kwargs: PumpVariablespeedType):
    return idf.newidfobject('PUMP:VARIABLESPEED', **kwargs)

def PumpVariablespeedCondensate(idf, **kwargs: PumpVariablespeedCondensateType):
    return idf.newidfobject('PUMP:VARIABLESPEED:CONDENSATE', **kwargs)

def PythonpluginInstance(idf, **kwargs: PythonpluginInstanceType):
    return idf.newidfobject('PYTHONPLUGIN:INSTANCE', **kwargs)

def PythonpluginOutputvariable(idf, **kwargs: PythonpluginOutputvariableType):
    return idf.newidfobject('PYTHONPLUGIN:OUTPUTVARIABLE', **kwargs)

def PythonpluginSearchpaths(idf, **kwargs: PythonpluginSearchpathsType):
    return idf.newidfobject('PYTHONPLUGIN:SEARCHPATHS', **kwargs)

def PythonpluginTrendvariable(idf, **kwargs: PythonpluginTrendvariableType):
    return idf.newidfobject('PYTHONPLUGIN:TRENDVARIABLE', **kwargs)

def PythonpluginVariables(idf, **kwargs: PythonpluginVariablesType):
    return idf.newidfobject('PYTHONPLUGIN:VARIABLES', **kwargs)

def RefrigerationAirchiller(idf, **kwargs: RefrigerationAirchillerType):
    return idf.newidfobject('REFRIGERATION:AIRCHILLER', **kwargs)

def RefrigerationCase(idf, **kwargs: RefrigerationCaseType):
    return idf.newidfobject('REFRIGERATION:CASE', **kwargs)

def RefrigerationCaseandwalkinlist(idf, **kwargs: RefrigerationCaseandwalkinlistType):
    return idf.newidfobject('REFRIGERATION:CASEANDWALKINLIST', **kwargs)

def RefrigerationCompressor(idf, **kwargs: RefrigerationCompressorType):
    return idf.newidfobject('REFRIGERATION:COMPRESSOR', **kwargs)

def RefrigerationCompressorlist(idf, **kwargs: RefrigerationCompressorlistType):
    return idf.newidfobject('REFRIGERATION:COMPRESSORLIST', **kwargs)

def RefrigerationCompressorrack(idf, **kwargs: RefrigerationCompressorrackType):
    return idf.newidfobject('REFRIGERATION:COMPRESSORRACK', **kwargs)

def RefrigerationCondenserAircooled(idf, **kwargs: RefrigerationCondenserAircooledType):
    return idf.newidfobject('REFRIGERATION:CONDENSER:AIRCOOLED', **kwargs)

def RefrigerationCondenserCascade(idf, **kwargs: RefrigerationCondenserCascadeType):
    return idf.newidfobject('REFRIGERATION:CONDENSER:CASCADE', **kwargs)

def RefrigerationCondenserEvaporativecooled(idf, **kwargs: RefrigerationCondenserEvaporativecooledType):
    return idf.newidfobject('REFRIGERATION:CONDENSER:EVAPORATIVECOOLED', **kwargs)

def RefrigerationCondenserWatercooled(idf, **kwargs: RefrigerationCondenserWatercooledType):
    return idf.newidfobject('REFRIGERATION:CONDENSER:WATERCOOLED', **kwargs)

def RefrigerationGascoolerAircooled(idf, **kwargs: RefrigerationGascoolerAircooledType):
    return idf.newidfobject('REFRIGERATION:GASCOOLER:AIRCOOLED', **kwargs)

def RefrigerationSecondarysystem(idf, **kwargs: RefrigerationSecondarysystemType):
    return idf.newidfobject('REFRIGERATION:SECONDARYSYSTEM', **kwargs)

def RefrigerationSubcooler(idf, **kwargs: RefrigerationSubcoolerType):
    return idf.newidfobject('REFRIGERATION:SUBCOOLER', **kwargs)

def RefrigerationSystem(idf, **kwargs: RefrigerationSystemType):
    return idf.newidfobject('REFRIGERATION:SYSTEM', **kwargs)

def RefrigerationTranscriticalsystem(idf, **kwargs: RefrigerationTranscriticalsystemType):
    return idf.newidfobject('REFRIGERATION:TRANSCRITICALSYSTEM', **kwargs)

def RefrigerationTransferloadlist(idf, **kwargs: RefrigerationTransferloadlistType):
    return idf.newidfobject('REFRIGERATION:TRANSFERLOADLIST', **kwargs)

def RefrigerationWalkin(idf, **kwargs: RefrigerationWalkinType):
    return idf.newidfobject('REFRIGERATION:WALKIN', **kwargs)

def Roof(idf, **kwargs: RoofType):
    return idf.newidfobject('ROOF', **kwargs)

def RoofceilingDetailed(idf, **kwargs: RoofceilingDetailedType):
    return idf.newidfobject('ROOFCEILING:DETAILED', **kwargs)

def Roofirrigation(idf, **kwargs: RoofirrigationType):
    return idf.newidfobject('ROOFIRRIGATION', **kwargs)

def RoomairNode(idf, **kwargs: RoomairNodeType):
    return idf.newidfobject('ROOMAIR:NODE', **kwargs)

def RoomairNodeAirflownetwork(idf, **kwargs: RoomairNodeAirflownetworkType):
    return idf.newidfobject('ROOMAIR:NODE:AIRFLOWNETWORK', **kwargs)

def RoomairNodeAirflownetworkAdjacentsurfacelist(idf, **kwargs: RoomairNodeAirflownetworkAdjacentsurfacelistType):
    return idf.newidfobject('ROOMAIR:NODE:AIRFLOWNETWORK:ADJACENTSURFACELIST', **kwargs)

def RoomairNodeAirflownetworkHvacequipment(idf, **kwargs: RoomairNodeAirflownetworkHvacequipmentType):
    return idf.newidfobject('ROOMAIR:NODE:AIRFLOWNETWORK:HVACEQUIPMENT', **kwargs)

def RoomairNodeAirflownetworkInternalgains(idf, **kwargs: RoomairNodeAirflownetworkInternalgainsType):
    return idf.newidfobject('ROOMAIR:NODE:AIRFLOWNETWORK:INTERNALGAINS', **kwargs)

def RoomairTemperaturepatternConstantgradient(idf, **kwargs: RoomairTemperaturepatternConstantgradientType):
    return idf.newidfobject('ROOMAIR:TEMPERATUREPATTERN:CONSTANTGRADIENT', **kwargs)

def RoomairTemperaturepatternNondimensionalheight(idf, **kwargs: RoomairTemperaturepatternNondimensionalheightType):
    return idf.newidfobject('ROOMAIR:TEMPERATUREPATTERN:NONDIMENSIONALHEIGHT', **kwargs)

def RoomairTemperaturepatternSurfacemapping(idf, **kwargs: RoomairTemperaturepatternSurfacemappingType):
    return idf.newidfobject('ROOMAIR:TEMPERATUREPATTERN:SURFACEMAPPING', **kwargs)

def RoomairTemperaturepatternTwogradient(idf, **kwargs: RoomairTemperaturepatternTwogradientType):
    return idf.newidfobject('ROOMAIR:TEMPERATUREPATTERN:TWOGRADIENT', **kwargs)

def RoomairTemperaturepatternUserdefined(idf, **kwargs: RoomairTemperaturepatternUserdefinedType):
    return idf.newidfobject('ROOMAIR:TEMPERATUREPATTERN:USERDEFINED', **kwargs)

def Roomairmodeltype(idf, **kwargs: RoomairmodeltypeType):
    return idf.newidfobject('ROOMAIRMODELTYPE', **kwargs)

def RoomairsettingsAirflownetwork(idf, **kwargs: RoomairsettingsAirflownetworkType):
    return idf.newidfobject('ROOMAIRSETTINGS:AIRFLOWNETWORK', **kwargs)

def RoomairsettingsCrossventilation(idf, **kwargs: RoomairsettingsCrossventilationType):
    return idf.newidfobject('ROOMAIRSETTINGS:CROSSVENTILATION', **kwargs)

def RoomairsettingsOnenodedisplacementventilation(idf, **kwargs: RoomairsettingsOnenodedisplacementventilationType):
    return idf.newidfobject('ROOMAIRSETTINGS:ONENODEDISPLACEMENTVENTILATION', **kwargs)

def RoomairsettingsThreenodedisplacementventilation(idf, **kwargs: RoomairsettingsThreenodedisplacementventilationType):
    return idf.newidfobject('ROOMAIRSETTINGS:THREENODEDISPLACEMENTVENTILATION', **kwargs)

def RoomairsettingsUnderfloorairdistributionexterior(idf, **kwargs: RoomairsettingsUnderfloorairdistributionexteriorType):
    return idf.newidfobject('ROOMAIRSETTINGS:UNDERFLOORAIRDISTRIBUTIONEXTERIOR', **kwargs)

def RoomairsettingsUnderfloorairdistributioninterior(idf, **kwargs: RoomairsettingsUnderfloorairdistributioninteriorType):
    return idf.newidfobject('ROOMAIRSETTINGS:UNDERFLOORAIRDISTRIBUTIONINTERIOR', **kwargs)

def Runperiod(idf, **kwargs: RunperiodType):
    return idf.newidfobject('RUNPERIOD', **kwargs)

def RunperiodcontrolDaylightsavingtime(idf, **kwargs: RunperiodcontrolDaylightsavingtimeType):
    return idf.newidfobject('RUNPERIODCONTROL:DAYLIGHTSAVINGTIME', **kwargs)

def RunperiodcontrolSpecialdays(idf, **kwargs: RunperiodcontrolSpecialdaysType):
    return idf.newidfobject('RUNPERIODCONTROL:SPECIALDAYS', **kwargs)

def ScheduleCompact(idf, **kwargs: ScheduleCompactType):
    return idf.newidfobject('SCHEDULE:COMPACT', **kwargs)

def ScheduleConstant(idf, **kwargs: ScheduleConstantType):
    return idf.newidfobject('SCHEDULE:CONSTANT', **kwargs)

def ScheduleDayHourly(idf, **kwargs: ScheduleDayHourlyType):
    return idf.newidfobject('SCHEDULE:DAY:HOURLY', **kwargs)

def ScheduleDayInterval(idf, **kwargs: ScheduleDayIntervalType):
    return idf.newidfobject('SCHEDULE:DAY:INTERVAL', **kwargs)

def ScheduleDayList(idf, **kwargs: ScheduleDayListType):
    return idf.newidfobject('SCHEDULE:DAY:LIST', **kwargs)

def ScheduleFile(idf, **kwargs: ScheduleFileType):
    return idf.newidfobject('SCHEDULE:FILE', **kwargs)

def ScheduleFileShading(idf, **kwargs: ScheduleFileShadingType):
    return idf.newidfobject('SCHEDULE:FILE:SHADING', **kwargs)

def ScheduleWeekCompact(idf, **kwargs: ScheduleWeekCompactType):
    return idf.newidfobject('SCHEDULE:WEEK:COMPACT', **kwargs)

def ScheduleWeekDaily(idf, **kwargs: ScheduleWeekDailyType):
    return idf.newidfobject('SCHEDULE:WEEK:DAILY', **kwargs)

def ScheduleYear(idf, **kwargs: ScheduleYearType):
    return idf.newidfobject('SCHEDULE:YEAR', **kwargs)

def Scheduletypelimits(idf, **kwargs: ScheduletypelimitsType):
    return idf.newidfobject('SCHEDULETYPELIMITS', **kwargs)

def SetpointmanagerColdest(idf, **kwargs: SetpointmanagerColdestType):
    return idf.newidfobject('SETPOINTMANAGER:COLDEST', **kwargs)

def SetpointmanagerCondenserenteringreset(idf, **kwargs: SetpointmanagerCondenserenteringresetType):
    return idf.newidfobject('SETPOINTMANAGER:CONDENSERENTERINGRESET', **kwargs)

def SetpointmanagerCondenserenteringresetIdeal(idf, **kwargs: SetpointmanagerCondenserenteringresetIdealType):
    return idf.newidfobject('SETPOINTMANAGER:CONDENSERENTERINGRESET:IDEAL', **kwargs)

def SetpointmanagerFollowgroundtemperature(idf, **kwargs: SetpointmanagerFollowgroundtemperatureType):
    return idf.newidfobject('SETPOINTMANAGER:FOLLOWGROUNDTEMPERATURE', **kwargs)

def SetpointmanagerFollowoutdoorairtemperature(idf, **kwargs: SetpointmanagerFollowoutdoorairtemperatureType):
    return idf.newidfobject('SETPOINTMANAGER:FOLLOWOUTDOORAIRTEMPERATURE', **kwargs)

def SetpointmanagerFollowsystemnodetemperature(idf, **kwargs: SetpointmanagerFollowsystemnodetemperatureType):
    return idf.newidfobject('SETPOINTMANAGER:FOLLOWSYSTEMNODETEMPERATURE', **kwargs)

def SetpointmanagerMixedair(idf, **kwargs: SetpointmanagerMixedairType):
    return idf.newidfobject('SETPOINTMANAGER:MIXEDAIR', **kwargs)

def SetpointmanagerMultizoneCoolingAverage(idf, **kwargs: SetpointmanagerMultizoneCoolingAverageType):
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:COOLING:AVERAGE', **kwargs)

def SetpointmanagerMultizoneHeatingAverage(idf, **kwargs: SetpointmanagerMultizoneHeatingAverageType):
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:HEATING:AVERAGE', **kwargs)

def SetpointmanagerMultizoneHumidityMaximum(idf, **kwargs: SetpointmanagerMultizoneHumidityMaximumType):
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:HUMIDITY:MAXIMUM', **kwargs)

def SetpointmanagerMultizoneHumidityMinimum(idf, **kwargs: SetpointmanagerMultizoneHumidityMinimumType):
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:HUMIDITY:MINIMUM', **kwargs)

def SetpointmanagerMultizoneMaximumhumidityAverage(idf, **kwargs: SetpointmanagerMultizoneMaximumhumidityAverageType):
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:MAXIMUMHUMIDITY:AVERAGE', **kwargs)

def SetpointmanagerMultizoneMinimumhumidityAverage(idf, **kwargs: SetpointmanagerMultizoneMinimumhumidityAverageType):
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:MINIMUMHUMIDITY:AVERAGE', **kwargs)

def SetpointmanagerOutdoorairpretreat(idf, **kwargs: SetpointmanagerOutdoorairpretreatType):
    return idf.newidfobject('SETPOINTMANAGER:OUTDOORAIRPRETREAT', **kwargs)

def SetpointmanagerOutdoorairreset(idf, **kwargs: SetpointmanagerOutdoorairresetType):
    return idf.newidfobject('SETPOINTMANAGER:OUTDOORAIRRESET', **kwargs)

def SetpointmanagerReturnairbypassflow(idf, **kwargs: SetpointmanagerReturnairbypassflowType):
    return idf.newidfobject('SETPOINTMANAGER:RETURNAIRBYPASSFLOW', **kwargs)

def SetpointmanagerReturntemperatureChilledwater(idf, **kwargs: SetpointmanagerReturntemperatureChilledwaterType):
    return idf.newidfobject('SETPOINTMANAGER:RETURNTEMPERATURE:CHILLEDWATER', **kwargs)

def SetpointmanagerReturntemperatureHotwater(idf, **kwargs: SetpointmanagerReturntemperatureHotwaterType):
    return idf.newidfobject('SETPOINTMANAGER:RETURNTEMPERATURE:HOTWATER', **kwargs)

def SetpointmanagerScheduled(idf, **kwargs: SetpointmanagerScheduledType):
    return idf.newidfobject('SETPOINTMANAGER:SCHEDULED', **kwargs)

def SetpointmanagerScheduledDualsetpoint(idf, **kwargs: SetpointmanagerScheduledDualsetpointType):
    return idf.newidfobject('SETPOINTMANAGER:SCHEDULED:DUALSETPOINT', **kwargs)

def SetpointmanagerSinglezoneCooling(idf, **kwargs: SetpointmanagerSinglezoneCoolingType):
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:COOLING', **kwargs)

def SetpointmanagerSinglezoneHeating(idf, **kwargs: SetpointmanagerSinglezoneHeatingType):
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:HEATING', **kwargs)

def SetpointmanagerSinglezoneHumidityMaximum(idf, **kwargs: SetpointmanagerSinglezoneHumidityMaximumType):
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:HUMIDITY:MAXIMUM', **kwargs)

def SetpointmanagerSinglezoneHumidityMinimum(idf, **kwargs: SetpointmanagerSinglezoneHumidityMinimumType):
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:HUMIDITY:MINIMUM', **kwargs)

def SetpointmanagerSinglezoneOnestagecooling(idf, **kwargs: SetpointmanagerSinglezoneOnestagecoolingType):
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:ONESTAGECOOLING', **kwargs)

def SetpointmanagerSinglezoneOnestageheating(idf, **kwargs: SetpointmanagerSinglezoneOnestageheatingType):
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:ONESTAGEHEATING', **kwargs)

def SetpointmanagerSinglezoneReheat(idf, **kwargs: SetpointmanagerSinglezoneReheatType):
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:REHEAT', **kwargs)

def SetpointmanagerSystemnoderesetHumidity(idf, **kwargs: SetpointmanagerSystemnoderesetHumidityType):
    return idf.newidfobject('SETPOINTMANAGER:SYSTEMNODERESET:HUMIDITY', **kwargs)

def SetpointmanagerSystemnoderesetTemperature(idf, **kwargs: SetpointmanagerSystemnoderesetTemperatureType):
    return idf.newidfobject('SETPOINTMANAGER:SYSTEMNODERESET:TEMPERATURE', **kwargs)

def SetpointmanagerWarmest(idf, **kwargs: SetpointmanagerWarmestType):
    return idf.newidfobject('SETPOINTMANAGER:WARMEST', **kwargs)

def SetpointmanagerWarmesttemperatureflow(idf, **kwargs: SetpointmanagerWarmesttemperatureflowType):
    return idf.newidfobject('SETPOINTMANAGER:WARMESTTEMPERATUREFLOW', **kwargs)

def ShadingBuilding(idf, **kwargs: ShadingBuildingType):
    return idf.newidfobject('SHADING:BUILDING', **kwargs)

def ShadingBuildingDetailed(idf, **kwargs: ShadingBuildingDetailedType):
    return idf.newidfobject('SHADING:BUILDING:DETAILED', **kwargs)

def ShadingFin(idf, **kwargs: ShadingFinType):
    return idf.newidfobject('SHADING:FIN', **kwargs)

def ShadingFinProjection(idf, **kwargs: ShadingFinProjectionType):
    return idf.newidfobject('SHADING:FIN:PROJECTION', **kwargs)

def ShadingOverhang(idf, **kwargs: ShadingOverhangType):
    return idf.newidfobject('SHADING:OVERHANG', **kwargs)

def ShadingOverhangProjection(idf, **kwargs: ShadingOverhangProjectionType):
    return idf.newidfobject('SHADING:OVERHANG:PROJECTION', **kwargs)

def ShadingSite(idf, **kwargs: ShadingSiteType):
    return idf.newidfobject('SHADING:SITE', **kwargs)

def ShadingSiteDetailed(idf, **kwargs: ShadingSiteDetailedType):
    return idf.newidfobject('SHADING:SITE:DETAILED', **kwargs)

def ShadingZoneDetailed(idf, **kwargs: ShadingZoneDetailedType):
    return idf.newidfobject('SHADING:ZONE:DETAILED', **kwargs)

def ShadingpropertyReflectance(idf, **kwargs: ShadingpropertyReflectanceType):
    return idf.newidfobject('SHADINGPROPERTY:REFLECTANCE', **kwargs)

def Shadowcalculation(idf, **kwargs: ShadowcalculationType):
    return idf.newidfobject('SHADOWCALCULATION', **kwargs)

def Simulationcontrol(idf, **kwargs: SimulationcontrolType):
    return idf.newidfobject('SIMULATIONCONTROL', **kwargs)

def SiteGrounddomainBasement(idf, **kwargs: SiteGrounddomainBasementType):
    return idf.newidfobject('SITE:GROUNDDOMAIN:BASEMENT', **kwargs)

def SiteGrounddomainSlab(idf, **kwargs: SiteGrounddomainSlabType):
    return idf.newidfobject('SITE:GROUNDDOMAIN:SLAB', **kwargs)

def SiteGroundreflectance(idf, **kwargs: SiteGroundreflectanceType):
    return idf.newidfobject('SITE:GROUNDREFLECTANCE', **kwargs)

def SiteGroundreflectanceSnowmodifier(idf, **kwargs: SiteGroundreflectanceSnowmodifierType):
    return idf.newidfobject('SITE:GROUNDREFLECTANCE:SNOWMODIFIER', **kwargs)

def SiteGroundtemperatureBuildingsurface(idf, **kwargs: SiteGroundtemperatureBuildingsurfaceType):
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:BUILDINGSURFACE', **kwargs)

def SiteGroundtemperatureDeep(idf, **kwargs: SiteGroundtemperatureDeepType):
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:DEEP', **kwargs)

def SiteGroundtemperatureFcfactormethod(idf, **kwargs: SiteGroundtemperatureFcfactormethodType):
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:FCFACTORMETHOD', **kwargs)

def SiteGroundtemperatureShallow(idf, **kwargs: SiteGroundtemperatureShallowType):
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:SHALLOW', **kwargs)

def SiteGroundtemperatureUndisturbedFinitedifference(idf, **kwargs: SiteGroundtemperatureUndisturbedFinitedifferenceType):
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:UNDISTURBED:FINITEDIFFERENCE', **kwargs)

def SiteGroundtemperatureUndisturbedKusudaachenbach(idf, **kwargs: SiteGroundtemperatureUndisturbedKusudaachenbachType):
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:UNDISTURBED:KUSUDAACHENBACH', **kwargs)

def SiteGroundtemperatureUndisturbedXing(idf, **kwargs: SiteGroundtemperatureUndisturbedXingType):
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:UNDISTURBED:XING', **kwargs)

def SiteHeightvariation(idf, **kwargs: SiteHeightvariationType):
    return idf.newidfobject('SITE:HEIGHTVARIATION', **kwargs)

def SiteLocation(idf, **kwargs: SiteLocationType):
    return idf.newidfobject('SITE:LOCATION', **kwargs)

def SitePrecipitation(idf, **kwargs: SitePrecipitationType):
    return idf.newidfobject('SITE:PRECIPITATION', **kwargs)

def SiteSolarandvisiblespectrum(idf, **kwargs: SiteSolarandvisiblespectrumType):
    return idf.newidfobject('SITE:SOLARANDVISIBLESPECTRUM', **kwargs)

def SiteSpectrumdata(idf, **kwargs: SiteSpectrumdataType):
    return idf.newidfobject('SITE:SPECTRUMDATA', **kwargs)

def SiteVariablelocation(idf, **kwargs: SiteVariablelocationType):
    return idf.newidfobject('SITE:VARIABLELOCATION', **kwargs)

def SiteWatermainstemperature(idf, **kwargs: SiteWatermainstemperatureType):
    return idf.newidfobject('SITE:WATERMAINSTEMPERATURE', **kwargs)

def SiteWeatherstation(idf, **kwargs: SiteWeatherstationType):
    return idf.newidfobject('SITE:WEATHERSTATION', **kwargs)

def SizingParameters(idf, **kwargs: SizingParametersType):
    return idf.newidfobject('SIZING:PARAMETERS', **kwargs)

def SizingPlant(idf, **kwargs: SizingPlantType):
    return idf.newidfobject('SIZING:PLANT', **kwargs)

def SizingSystem(idf, **kwargs: SizingSystemType):
    return idf.newidfobject('SIZING:SYSTEM', **kwargs)

def SizingZone(idf, **kwargs: SizingZoneType):
    return idf.newidfobject('SIZING:ZONE', **kwargs)

def SizingperiodDesignday(idf, **kwargs: SizingperiodDesigndayType):
    return idf.newidfobject('SIZINGPERIOD:DESIGNDAY', **kwargs)

def SizingperiodWeatherfileconditiontype(idf, **kwargs: SizingperiodWeatherfileconditiontypeType):
    return idf.newidfobject('SIZINGPERIOD:WEATHERFILECONDITIONTYPE', **kwargs)

def SizingperiodWeatherfiledays(idf, **kwargs: SizingperiodWeatherfiledaysType):
    return idf.newidfobject('SIZINGPERIOD:WEATHERFILEDAYS', **kwargs)

def SolarcollectorFlatplatePhotovoltaicthermal(idf, **kwargs: SolarcollectorFlatplatePhotovoltaicthermalType):
    return idf.newidfobject('SOLARCOLLECTOR:FLATPLATE:PHOTOVOLTAICTHERMAL', **kwargs)

def SolarcollectorFlatplateWater(idf, **kwargs: SolarcollectorFlatplateWaterType):
    return idf.newidfobject('SOLARCOLLECTOR:FLATPLATE:WATER', **kwargs)

def SolarcollectorIntegralcollectorstorage(idf, **kwargs: SolarcollectorIntegralcollectorstorageType):
    return idf.newidfobject('SOLARCOLLECTOR:INTEGRALCOLLECTORSTORAGE', **kwargs)

def SolarcollectorUnglazedtranspired(idf, **kwargs: SolarcollectorUnglazedtranspiredType):
    return idf.newidfobject('SOLARCOLLECTOR:UNGLAZEDTRANSPIRED', **kwargs)

def SolarcollectorUnglazedtranspiredMultisystem(idf, **kwargs: SolarcollectorUnglazedtranspiredMultisystemType):
    return idf.newidfobject('SOLARCOLLECTOR:UNGLAZEDTRANSPIRED:MULTISYSTEM', **kwargs)

def SolarcollectorperformanceFlatplate(idf, **kwargs: SolarcollectorperformanceFlatplateType):
    return idf.newidfobject('SOLARCOLLECTORPERFORMANCE:FLATPLATE', **kwargs)

def SolarcollectorperformanceIntegralcollectorstorage(idf, **kwargs: SolarcollectorperformanceIntegralcollectorstorageType):
    return idf.newidfobject('SOLARCOLLECTORPERFORMANCE:INTEGRALCOLLECTORSTORAGE', **kwargs)

def SolarcollectorperformancePhotovoltaicthermalBipvt(idf, **kwargs: SolarcollectorperformancePhotovoltaicthermalBipvtType):
    return idf.newidfobject('SOLARCOLLECTORPERFORMANCE:PHOTOVOLTAICTHERMAL:BIPVT', **kwargs)

def SolarcollectorperformancePhotovoltaicthermalSimple(idf, **kwargs: SolarcollectorperformancePhotovoltaicthermalSimpleType):
    return idf.newidfobject('SOLARCOLLECTORPERFORMANCE:PHOTOVOLTAICTHERMAL:SIMPLE', **kwargs)

def Space(idf, **kwargs: SpaceType):
    return idf.newidfobject('SPACE', **kwargs)

def SpacehvacEquipmentconnections(idf, **kwargs: SpacehvacEquipmentconnectionsType):
    return idf.newidfobject('SPACEHVAC:EQUIPMENTCONNECTIONS', **kwargs)

def SpacehvacZoneequipmentmixer(idf, **kwargs: SpacehvacZoneequipmentmixerType):
    return idf.newidfobject('SPACEHVAC:ZONEEQUIPMENTMIXER', **kwargs)

def SpacehvacZoneequipmentsplitter(idf, **kwargs: SpacehvacZoneequipmentsplitterType):
    return idf.newidfobject('SPACEHVAC:ZONEEQUIPMENTSPLITTER', **kwargs)

def Spacelist(idf, **kwargs: SpacelistType):
    return idf.newidfobject('SPACELIST', **kwargs)

def Steamequipment(idf, **kwargs: SteamequipmentType):
    return idf.newidfobject('STEAMEQUIPMENT', **kwargs)

def SurfacecontaminantsourceandsinkGenericBoundarylayerdiffusion(idf, **kwargs: SurfacecontaminantsourceandsinkGenericBoundarylayerdiffusionType):
    return idf.newidfobject('SURFACECONTAMINANTSOURCEANDSINK:GENERIC:BOUNDARYLAYERDIFFUSION', **kwargs)

def SurfacecontaminantsourceandsinkGenericDepositionvelocitysink(idf, **kwargs: SurfacecontaminantsourceandsinkGenericDepositionvelocitysinkType):
    return idf.newidfobject('SURFACECONTAMINANTSOURCEANDSINK:GENERIC:DEPOSITIONVELOCITYSINK', **kwargs)

def SurfacecontaminantsourceandsinkGenericPressuredriven(idf, **kwargs: SurfacecontaminantsourceandsinkGenericPressuredrivenType):
    return idf.newidfobject('SURFACECONTAMINANTSOURCEANDSINK:GENERIC:PRESSUREDRIVEN', **kwargs)

def SurfacecontrolMovableinsulation(idf, **kwargs: SurfacecontrolMovableinsulationType):
    return idf.newidfobject('SURFACECONTROL:MOVABLEINSULATION', **kwargs)

def SurfaceconvectionalgorithmInside(idf, **kwargs: SurfaceconvectionalgorithmInsideType):
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:INSIDE', **kwargs)

def SurfaceconvectionalgorithmInsideAdaptivemodelselections(idf, **kwargs: SurfaceconvectionalgorithmInsideAdaptivemodelselectionsType):
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:INSIDE:ADAPTIVEMODELSELECTIONS', **kwargs)

def SurfaceconvectionalgorithmInsideUsercurve(idf, **kwargs: SurfaceconvectionalgorithmInsideUsercurveType):
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:INSIDE:USERCURVE', **kwargs)

def SurfaceconvectionalgorithmOutside(idf, **kwargs: SurfaceconvectionalgorithmOutsideType):
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:OUTSIDE', **kwargs)

def SurfaceconvectionalgorithmOutsideAdaptivemodelselections(idf, **kwargs: SurfaceconvectionalgorithmOutsideAdaptivemodelselectionsType):
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:OUTSIDE:ADAPTIVEMODELSELECTIONS', **kwargs)

def SurfaceconvectionalgorithmOutsideUsercurve(idf, **kwargs: SurfaceconvectionalgorithmOutsideUsercurveType):
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:OUTSIDE:USERCURVE', **kwargs)

def SurfacepropertiesVaporcoefficients(idf, **kwargs: SurfacepropertiesVaporcoefficientsType):
    return idf.newidfobject('SURFACEPROPERTIES:VAPORCOEFFICIENTS', **kwargs)

def SurfacepropertyConvectioncoefficients(idf, **kwargs: SurfacepropertyConvectioncoefficientsType):
    return idf.newidfobject('SURFACEPROPERTY:CONVECTIONCOEFFICIENTS', **kwargs)

def SurfacepropertyConvectioncoefficientsMultiplesurface(idf, **kwargs: SurfacepropertyConvectioncoefficientsMultiplesurfaceType):
    return idf.newidfobject('SURFACEPROPERTY:CONVECTIONCOEFFICIENTS:MULTIPLESURFACE', **kwargs)

def SurfacepropertyExposedfoundationperimeter(idf, **kwargs: SurfacepropertyExposedfoundationperimeterType):
    return idf.newidfobject('SURFACEPROPERTY:EXPOSEDFOUNDATIONPERIMETER', **kwargs)

def SurfacepropertyExteriornaturalventedcavity(idf, **kwargs: SurfacepropertyExteriornaturalventedcavityType):
    return idf.newidfobject('SURFACEPROPERTY:EXTERIORNATURALVENTEDCAVITY', **kwargs)

def SurfacepropertyGroundsurfaces(idf, **kwargs: SurfacepropertyGroundsurfacesType):
    return idf.newidfobject('SURFACEPROPERTY:GROUNDSURFACES', **kwargs)

def SurfacepropertyHeatbalancesourceterm(idf, **kwargs: SurfacepropertyHeatbalancesourcetermType):
    return idf.newidfobject('SURFACEPROPERTY:HEATBALANCESOURCETERM', **kwargs)

def SurfacepropertyHeattransferalgorithm(idf, **kwargs: SurfacepropertyHeattransferalgorithmType):
    return idf.newidfobject('SURFACEPROPERTY:HEATTRANSFERALGORITHM', **kwargs)

def SurfacepropertyHeattransferalgorithmConstruction(idf, **kwargs: SurfacepropertyHeattransferalgorithmConstructionType):
    return idf.newidfobject('SURFACEPROPERTY:HEATTRANSFERALGORITHM:CONSTRUCTION', **kwargs)

def SurfacepropertyHeattransferalgorithmMultiplesurface(idf, **kwargs: SurfacepropertyHeattransferalgorithmMultiplesurfaceType):
    return idf.newidfobject('SURFACEPROPERTY:HEATTRANSFERALGORITHM:MULTIPLESURFACE', **kwargs)

def SurfacepropertyHeattransferalgorithmSurfacelist(idf, **kwargs: SurfacepropertyHeattransferalgorithmSurfacelistType):
    return idf.newidfobject('SURFACEPROPERTY:HEATTRANSFERALGORITHM:SURFACELIST', **kwargs)

def SurfacepropertyIncidentsolarmultiplier(idf, **kwargs: SurfacepropertyIncidentsolarmultiplierType):
    return idf.newidfobject('SURFACEPROPERTY:INCIDENTSOLARMULTIPLIER', **kwargs)

def SurfacepropertyLocalenvironment(idf, **kwargs: SurfacepropertyLocalenvironmentType):
    return idf.newidfobject('SURFACEPROPERTY:LOCALENVIRONMENT', **kwargs)

def SurfacepropertyOthersidecoefficients(idf, **kwargs: SurfacepropertyOthersidecoefficientsType):
    return idf.newidfobject('SURFACEPROPERTY:OTHERSIDECOEFFICIENTS', **kwargs)

def SurfacepropertyOthersideconditionsmodel(idf, **kwargs: SurfacepropertyOthersideconditionsmodelType):
    return idf.newidfobject('SURFACEPROPERTY:OTHERSIDECONDITIONSMODEL', **kwargs)

def SurfacepropertySolarincidentinside(idf, **kwargs: SurfacepropertySolarincidentinsideType):
    return idf.newidfobject('SURFACEPROPERTY:SOLARINCIDENTINSIDE', **kwargs)

def SurfacepropertySurroundingsurfaces(idf, **kwargs: SurfacepropertySurroundingsurfacesType):
    return idf.newidfobject('SURFACEPROPERTY:SURROUNDINGSURFACES', **kwargs)

def SurfacepropertyUnderwater(idf, **kwargs: SurfacepropertyUnderwaterType):
    return idf.newidfobject('SURFACEPROPERTY:UNDERWATER', **kwargs)

def SwimmingpoolIndoor(idf, **kwargs: SwimmingpoolIndoorType):
    return idf.newidfobject('SWIMMINGPOOL:INDOOR', **kwargs)

def TableIndependentvariable(idf, **kwargs: TableIndependentvariableType):
    return idf.newidfobject('TABLE:INDEPENDENTVARIABLE', **kwargs)

def TableIndependentvariablelist(idf, **kwargs: TableIndependentvariablelistType):
    return idf.newidfobject('TABLE:INDEPENDENTVARIABLELIST', **kwargs)

def TableLookup(idf, **kwargs: TableLookupType):
    return idf.newidfobject('TABLE:LOOKUP', **kwargs)

def Temperingvalve(idf, **kwargs: TemperingvalveType):
    return idf.newidfobject('TEMPERINGVALVE', **kwargs)

def ThermalstorageChilledwaterMixed(idf, **kwargs: ThermalstorageChilledwaterMixedType):
    return idf.newidfobject('THERMALSTORAGE:CHILLEDWATER:MIXED', **kwargs)

def ThermalstorageChilledwaterStratified(idf, **kwargs: ThermalstorageChilledwaterStratifiedType):
    return idf.newidfobject('THERMALSTORAGE:CHILLEDWATER:STRATIFIED', **kwargs)

def ThermalstorageIceDetailed(idf, **kwargs: ThermalstorageIceDetailedType):
    return idf.newidfobject('THERMALSTORAGE:ICE:DETAILED', **kwargs)

def ThermalstorageIceSimple(idf, **kwargs: ThermalstorageIceSimpleType):
    return idf.newidfobject('THERMALSTORAGE:ICE:SIMPLE', **kwargs)

def ThermostatsetpointDualsetpoint(idf, **kwargs: ThermostatsetpointDualsetpointType):
    return idf.newidfobject('THERMOSTATSETPOINT:DUALSETPOINT', **kwargs)

def ThermostatsetpointSinglecooling(idf, **kwargs: ThermostatsetpointSinglecoolingType):
    return idf.newidfobject('THERMOSTATSETPOINT:SINGLECOOLING', **kwargs)

def ThermostatsetpointSingleheating(idf, **kwargs: ThermostatsetpointSingleheatingType):
    return idf.newidfobject('THERMOSTATSETPOINT:SINGLEHEATING', **kwargs)

def ThermostatsetpointSingleheatingorcooling(idf, **kwargs: ThermostatsetpointSingleheatingorcoolingType):
    return idf.newidfobject('THERMOSTATSETPOINT:SINGLEHEATINGORCOOLING', **kwargs)

def ThermostatsetpointThermalcomfortFangerDualsetpoint(idf, **kwargs: ThermostatsetpointThermalcomfortFangerDualsetpointType):
    return idf.newidfobject('THERMOSTATSETPOINT:THERMALCOMFORT:FANGER:DUALSETPOINT', **kwargs)

def ThermostatsetpointThermalcomfortFangerSinglecooling(idf, **kwargs: ThermostatsetpointThermalcomfortFangerSinglecoolingType):
    return idf.newidfobject('THERMOSTATSETPOINT:THERMALCOMFORT:FANGER:SINGLECOOLING', **kwargs)

def ThermostatsetpointThermalcomfortFangerSingleheating(idf, **kwargs: ThermostatsetpointThermalcomfortFangerSingleheatingType):
    return idf.newidfobject('THERMOSTATSETPOINT:THERMALCOMFORT:FANGER:SINGLEHEATING', **kwargs)

def ThermostatsetpointThermalcomfortFangerSingleheatingorcooling(idf, **kwargs: ThermostatsetpointThermalcomfortFangerSingleheatingorcoolingType):
    return idf.newidfobject('THERMOSTATSETPOINT:THERMALCOMFORT:FANGER:SINGLEHEATINGORCOOLING', **kwargs)

def Timestep(idf, **kwargs: TimestepType):
    return idf.newidfobject('TIMESTEP', **kwargs)

def UnitarysystemperformanceMultispeed(idf, **kwargs: UnitarysystemperformanceMultispeedType):
    return idf.newidfobject('UNITARYSYSTEMPERFORMANCE:MULTISPEED', **kwargs)

def UtilitycostChargeBlock(idf, **kwargs: UtilitycostChargeBlockType):
    return idf.newidfobject('UTILITYCOST:CHARGE:BLOCK', **kwargs)

def UtilitycostChargeSimple(idf, **kwargs: UtilitycostChargeSimpleType):
    return idf.newidfobject('UTILITYCOST:CHARGE:SIMPLE', **kwargs)

def UtilitycostComputation(idf, **kwargs: UtilitycostComputationType):
    return idf.newidfobject('UTILITYCOST:COMPUTATION', **kwargs)

def UtilitycostQualify(idf, **kwargs: UtilitycostQualifyType):
    return idf.newidfobject('UTILITYCOST:QUALIFY', **kwargs)

def UtilitycostRatchet(idf, **kwargs: UtilitycostRatchetType):
    return idf.newidfobject('UTILITYCOST:RATCHET', **kwargs)

def UtilitycostTariff(idf, **kwargs: UtilitycostTariffType):
    return idf.newidfobject('UTILITYCOST:TARIFF', **kwargs)

def UtilitycostVariable(idf, **kwargs: UtilitycostVariableType):
    return idf.newidfobject('UTILITYCOST:VARIABLE', **kwargs)

def Version(idf, **kwargs: VersionType):
    return idf.newidfobject('VERSION', **kwargs)

def WallAdiabatic(idf, **kwargs: WallAdiabaticType):
    return idf.newidfobject('WALL:ADIABATIC', **kwargs)

def WallDetailed(idf, **kwargs: WallDetailedType):
    return idf.newidfobject('WALL:DETAILED', **kwargs)

def WallExterior(idf, **kwargs: WallExteriorType):
    return idf.newidfobject('WALL:EXTERIOR', **kwargs)

def WallInterzone(idf, **kwargs: WallInterzoneType):
    return idf.newidfobject('WALL:INTERZONE', **kwargs)

def WallUnderground(idf, **kwargs: WallUndergroundType):
    return idf.newidfobject('WALL:UNDERGROUND', **kwargs)

def WaterheaterHeatpumpPumpedcondenser(idf, **kwargs: WaterheaterHeatpumpPumpedcondenserType):
    return idf.newidfobject('WATERHEATER:HEATPUMP:PUMPEDCONDENSER', **kwargs)

def WaterheaterHeatpumpWrappedcondenser(idf, **kwargs: WaterheaterHeatpumpWrappedcondenserType):
    return idf.newidfobject('WATERHEATER:HEATPUMP:WRAPPEDCONDENSER', **kwargs)

def WaterheaterMixed(idf, **kwargs: WaterheaterMixedType):
    return idf.newidfobject('WATERHEATER:MIXED', **kwargs)

def WaterheaterSizing(idf, **kwargs: WaterheaterSizingType):
    return idf.newidfobject('WATERHEATER:SIZING', **kwargs)

def WaterheaterStratified(idf, **kwargs: WaterheaterStratifiedType):
    return idf.newidfobject('WATERHEATER:STRATIFIED', **kwargs)

def WateruseConnections(idf, **kwargs: WateruseConnectionsType):
    return idf.newidfobject('WATERUSE:CONNECTIONS', **kwargs)

def WateruseEquipment(idf, **kwargs: WateruseEquipmentType):
    return idf.newidfobject('WATERUSE:EQUIPMENT', **kwargs)

def WateruseRaincollector(idf, **kwargs: WateruseRaincollectorType):
    return idf.newidfobject('WATERUSE:RAINCOLLECTOR', **kwargs)

def WateruseStorage(idf, **kwargs: WateruseStorageType):
    return idf.newidfobject('WATERUSE:STORAGE', **kwargs)

def WateruseWell(idf, **kwargs: WateruseWellType):
    return idf.newidfobject('WATERUSE:WELL', **kwargs)

def WeatherpropertySkytemperature(idf, **kwargs: WeatherpropertySkytemperatureType):
    return idf.newidfobject('WEATHERPROPERTY:SKYTEMPERATURE', **kwargs)

def Window(idf, **kwargs: WindowType):
    return idf.newidfobject('WINDOW', **kwargs)

def WindowInterzone(idf, **kwargs: WindowInterzoneType):
    return idf.newidfobject('WINDOW:INTERZONE', **kwargs)

def WindowgapDeflectionstate(idf, **kwargs: WindowgapDeflectionstateType):
    return idf.newidfobject('WINDOWGAP:DEFLECTIONSTATE', **kwargs)

def WindowgapSupportpillar(idf, **kwargs: WindowgapSupportpillarType):
    return idf.newidfobject('WINDOWGAP:SUPPORTPILLAR', **kwargs)

def WindowmaterialBlind(idf, **kwargs: WindowmaterialBlindType):
    return idf.newidfobject('WINDOWMATERIAL:BLIND', **kwargs)

def WindowmaterialBlindEquivalentlayer(idf, **kwargs: WindowmaterialBlindEquivalentlayerType):
    return idf.newidfobject('WINDOWMATERIAL:BLIND:EQUIVALENTLAYER', **kwargs)

def WindowmaterialComplexshade(idf, **kwargs: WindowmaterialComplexshadeType):
    return idf.newidfobject('WINDOWMATERIAL:COMPLEXSHADE', **kwargs)

def WindowmaterialDrapeEquivalentlayer(idf, **kwargs: WindowmaterialDrapeEquivalentlayerType):
    return idf.newidfobject('WINDOWMATERIAL:DRAPE:EQUIVALENTLAYER', **kwargs)

def WindowmaterialGap(idf, **kwargs: WindowmaterialGapType):
    return idf.newidfobject('WINDOWMATERIAL:GAP', **kwargs)

def WindowmaterialGapEquivalentlayer(idf, **kwargs: WindowmaterialGapEquivalentlayerType):
    return idf.newidfobject('WINDOWMATERIAL:GAP:EQUIVALENTLAYER', **kwargs)

def WindowmaterialGas(idf, **kwargs: WindowmaterialGasType):
    return idf.newidfobject('WINDOWMATERIAL:GAS', **kwargs)

def WindowmaterialGasmixture(idf, **kwargs: WindowmaterialGasmixtureType):
    return idf.newidfobject('WINDOWMATERIAL:GASMIXTURE', **kwargs)

def WindowmaterialGlazing(idf, **kwargs: WindowmaterialGlazingType):
    return idf.newidfobject('WINDOWMATERIAL:GLAZING', **kwargs)

def WindowmaterialGlazingEquivalentlayer(idf, **kwargs: WindowmaterialGlazingEquivalentlayerType):
    return idf.newidfobject('WINDOWMATERIAL:GLAZING:EQUIVALENTLAYER', **kwargs)

def WindowmaterialGlazingRefractionextinctionmethod(idf, **kwargs: WindowmaterialGlazingRefractionextinctionmethodType):
    return idf.newidfobject('WINDOWMATERIAL:GLAZING:REFRACTIONEXTINCTIONMETHOD', **kwargs)

def WindowmaterialGlazinggroupThermochromic(idf, **kwargs: WindowmaterialGlazinggroupThermochromicType):
    return idf.newidfobject('WINDOWMATERIAL:GLAZINGGROUP:THERMOCHROMIC', **kwargs)

def WindowmaterialScreen(idf, **kwargs: WindowmaterialScreenType):
    return idf.newidfobject('WINDOWMATERIAL:SCREEN', **kwargs)

def WindowmaterialScreenEquivalentlayer(idf, **kwargs: WindowmaterialScreenEquivalentlayerType):
    return idf.newidfobject('WINDOWMATERIAL:SCREEN:EQUIVALENTLAYER', **kwargs)

def WindowmaterialShade(idf, **kwargs: WindowmaterialShadeType):
    return idf.newidfobject('WINDOWMATERIAL:SHADE', **kwargs)

def WindowmaterialShadeEquivalentlayer(idf, **kwargs: WindowmaterialShadeEquivalentlayerType):
    return idf.newidfobject('WINDOWMATERIAL:SHADE:EQUIVALENTLAYER', **kwargs)

def WindowmaterialSimpleglazingsystem(idf, **kwargs: WindowmaterialSimpleglazingsystemType):
    return idf.newidfobject('WINDOWMATERIAL:SIMPLEGLAZINGSYSTEM', **kwargs)

def WindowpropertyAirflowcontrol(idf, **kwargs: WindowpropertyAirflowcontrolType):
    return idf.newidfobject('WINDOWPROPERTY:AIRFLOWCONTROL', **kwargs)

def WindowpropertyFrameanddivider(idf, **kwargs: WindowpropertyFrameanddividerType):
    return idf.newidfobject('WINDOWPROPERTY:FRAMEANDDIVIDER', **kwargs)

def WindowpropertyStormwindow(idf, **kwargs: WindowpropertyStormwindowType):
    return idf.newidfobject('WINDOWPROPERTY:STORMWINDOW', **kwargs)

def Windowscalculationengine(idf, **kwargs: WindowscalculationengineType):
    return idf.newidfobject('WINDOWSCALCULATIONENGINE', **kwargs)

def Windowshadingcontrol(idf, **kwargs: WindowshadingcontrolType):
    return idf.newidfobject('WINDOWSHADINGCONTROL', **kwargs)

def WindowthermalmodelParams(idf, **kwargs: WindowthermalmodelParamsType):
    return idf.newidfobject('WINDOWTHERMALMODEL:PARAMS', **kwargs)

def Zone(idf, **kwargs: ZoneType):
    return idf.newidfobject('ZONE', **kwargs)

def ZoneairbalanceOutdoorair(idf, **kwargs: ZoneairbalanceOutdoorairType):
    return idf.newidfobject('ZONEAIRBALANCE:OUTDOORAIR', **kwargs)

def Zoneaircontaminantbalance(idf, **kwargs: ZoneaircontaminantbalanceType):
    return idf.newidfobject('ZONEAIRCONTAMINANTBALANCE', **kwargs)

def Zoneairheatbalancealgorithm(idf, **kwargs: ZoneairheatbalancealgorithmType):
    return idf.newidfobject('ZONEAIRHEATBALANCEALGORITHM', **kwargs)

def Zoneairmassflowconservation(idf, **kwargs: ZoneairmassflowconservationType):
    return idf.newidfobject('ZONEAIRMASSFLOWCONSERVATION', **kwargs)

def ZonebaseboardOutdoortemperaturecontrolled(idf, **kwargs: ZonebaseboardOutdoortemperaturecontrolledType):
    return idf.newidfobject('ZONEBASEBOARD:OUTDOORTEMPERATURECONTROLLED', **kwargs)

def ZonecapacitancemultiplierResearchspecial(idf, **kwargs: ZonecapacitancemultiplierResearchspecialType):
    return idf.newidfobject('ZONECAPACITANCEMULTIPLIER:RESEARCHSPECIAL', **kwargs)

def ZonecontaminantsourceandsinkCarbondioxide(idf, **kwargs: ZonecontaminantsourceandsinkCarbondioxideType):
    return idf.newidfobject('ZONECONTAMINANTSOURCEANDSINK:CARBONDIOXIDE', **kwargs)

def ZonecontaminantsourceandsinkGenericConstant(idf, **kwargs: ZonecontaminantsourceandsinkGenericConstantType):
    return idf.newidfobject('ZONECONTAMINANTSOURCEANDSINK:GENERIC:CONSTANT', **kwargs)

def ZonecontaminantsourceandsinkGenericCutoffmodel(idf, **kwargs: ZonecontaminantsourceandsinkGenericCutoffmodelType):
    return idf.newidfobject('ZONECONTAMINANTSOURCEANDSINK:GENERIC:CUTOFFMODEL', **kwargs)

def ZonecontaminantsourceandsinkGenericDecaysource(idf, **kwargs: ZonecontaminantsourceandsinkGenericDecaysourceType):
    return idf.newidfobject('ZONECONTAMINANTSOURCEANDSINK:GENERIC:DECAYSOURCE', **kwargs)

def ZonecontaminantsourceandsinkGenericDepositionratesink(idf, **kwargs: ZonecontaminantsourceandsinkGenericDepositionratesinkType):
    return idf.newidfobject('ZONECONTAMINANTSOURCEANDSINK:GENERIC:DEPOSITIONRATESINK', **kwargs)

def ZonecontrolContaminantcontroller(idf, **kwargs: ZonecontrolContaminantcontrollerType):
    return idf.newidfobject('ZONECONTROL:CONTAMINANTCONTROLLER', **kwargs)

def ZonecontrolHumidistat(idf, **kwargs: ZonecontrolHumidistatType):
    return idf.newidfobject('ZONECONTROL:HUMIDISTAT', **kwargs)

def ZonecontrolThermostat(idf, **kwargs: ZonecontrolThermostatType):
    return idf.newidfobject('ZONECONTROL:THERMOSTAT', **kwargs)

def ZonecontrolThermostatOperativetemperature(idf, **kwargs: ZonecontrolThermostatOperativetemperatureType):
    return idf.newidfobject('ZONECONTROL:THERMOSTAT:OPERATIVETEMPERATURE', **kwargs)

def ZonecontrolThermostatStageddualsetpoint(idf, **kwargs: ZonecontrolThermostatStageddualsetpointType):
    return idf.newidfobject('ZONECONTROL:THERMOSTAT:STAGEDDUALSETPOINT', **kwargs)

def ZonecontrolThermostatTemperatureandhumidity(idf, **kwargs: ZonecontrolThermostatTemperatureandhumidityType):
    return idf.newidfobject('ZONECONTROL:THERMOSTAT:TEMPERATUREANDHUMIDITY', **kwargs)

def ZonecontrolThermostatThermalcomfort(idf, **kwargs: ZonecontrolThermostatThermalcomfortType):
    return idf.newidfobject('ZONECONTROL:THERMOSTAT:THERMALCOMFORT', **kwargs)

def ZonecooltowerShower(idf, **kwargs: ZonecooltowerShowerType):
    return idf.newidfobject('ZONECOOLTOWER:SHOWER', **kwargs)

def Zonecrossmixing(idf, **kwargs: ZonecrossmixingType):
    return idf.newidfobject('ZONECROSSMIXING', **kwargs)

def Zoneearthtube(idf, **kwargs: ZoneearthtubeType):
    return idf.newidfobject('ZONEEARTHTUBE', **kwargs)

def ZoneearthtubeParameters(idf, **kwargs: ZoneearthtubeParametersType):
    return idf.newidfobject('ZONEEARTHTUBE:PARAMETERS', **kwargs)

def Zonegroup(idf, **kwargs: ZonegroupType):
    return idf.newidfobject('ZONEGROUP', **kwargs)

def ZonehvacAirdistributionunit(idf, **kwargs: ZonehvacAirdistributionunitType):
    return idf.newidfobject('ZONEHVAC:AIRDISTRIBUTIONUNIT', **kwargs)

def ZonehvacBaseboardConvectiveElectric(idf, **kwargs: ZonehvacBaseboardConvectiveElectricType):
    return idf.newidfobject('ZONEHVAC:BASEBOARD:CONVECTIVE:ELECTRIC', **kwargs)

def ZonehvacBaseboardConvectiveWater(idf, **kwargs: ZonehvacBaseboardConvectiveWaterType):
    return idf.newidfobject('ZONEHVAC:BASEBOARD:CONVECTIVE:WATER', **kwargs)

def ZonehvacBaseboardRadiantconvectiveElectric(idf, **kwargs: ZonehvacBaseboardRadiantconvectiveElectricType):
    return idf.newidfobject('ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:ELECTRIC', **kwargs)

def ZonehvacBaseboardRadiantconvectiveSteam(idf, **kwargs: ZonehvacBaseboardRadiantconvectiveSteamType):
    return idf.newidfobject('ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:STEAM', **kwargs)

def ZonehvacBaseboardRadiantconvectiveSteamDesign(idf, **kwargs: ZonehvacBaseboardRadiantconvectiveSteamDesignType):
    return idf.newidfobject('ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:STEAM:DESIGN', **kwargs)

def ZonehvacBaseboardRadiantconvectiveWater(idf, **kwargs: ZonehvacBaseboardRadiantconvectiveWaterType):
    return idf.newidfobject('ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:WATER', **kwargs)

def ZonehvacBaseboardRadiantconvectiveWaterDesign(idf, **kwargs: ZonehvacBaseboardRadiantconvectiveWaterDesignType):
    return idf.newidfobject('ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:WATER:DESIGN', **kwargs)

def ZonehvacCoolingpanelRadiantconvectiveWater(idf, **kwargs: ZonehvacCoolingpanelRadiantconvectiveWaterType):
    return idf.newidfobject('ZONEHVAC:COOLINGPANEL:RADIANTCONVECTIVE:WATER', **kwargs)

def ZonehvacDehumidifierDx(idf, **kwargs: ZonehvacDehumidifierDxType):
    return idf.newidfobject('ZONEHVAC:DEHUMIDIFIER:DX', **kwargs)

def ZonehvacEnergyrecoveryventilator(idf, **kwargs: ZonehvacEnergyrecoveryventilatorType):
    return idf.newidfobject('ZONEHVAC:ENERGYRECOVERYVENTILATOR', **kwargs)

def ZonehvacEnergyrecoveryventilatorController(idf, **kwargs: ZonehvacEnergyrecoveryventilatorControllerType):
    return idf.newidfobject('ZONEHVAC:ENERGYRECOVERYVENTILATOR:CONTROLLER', **kwargs)

def ZonehvacEquipmentconnections(idf, **kwargs: ZonehvacEquipmentconnectionsType):
    return idf.newidfobject('ZONEHVAC:EQUIPMENTCONNECTIONS', **kwargs)

def ZonehvacEquipmentlist(idf, **kwargs: ZonehvacEquipmentlistType):
    return idf.newidfobject('ZONEHVAC:EQUIPMENTLIST', **kwargs)

def ZonehvacEvaporativecoolerunit(idf, **kwargs: ZonehvacEvaporativecoolerunitType):
    return idf.newidfobject('ZONEHVAC:EVAPORATIVECOOLERUNIT', **kwargs)

def ZonehvacExhaustcontrol(idf, **kwargs: ZonehvacExhaustcontrolType):
    return idf.newidfobject('ZONEHVAC:EXHAUSTCONTROL', **kwargs)

def ZonehvacForcedairUserdefined(idf, **kwargs: ZonehvacForcedairUserdefinedType):
    return idf.newidfobject('ZONEHVAC:FORCEDAIR:USERDEFINED', **kwargs)

def ZonehvacFourpipefancoil(idf, **kwargs: ZonehvacFourpipefancoilType):
    return idf.newidfobject('ZONEHVAC:FOURPIPEFANCOIL', **kwargs)

def ZonehvacHightemperatureradiant(idf, **kwargs: ZonehvacHightemperatureradiantType):
    return idf.newidfobject('ZONEHVAC:HIGHTEMPERATURERADIANT', **kwargs)

def ZonehvacHybridunitaryhvac(idf, **kwargs: ZonehvacHybridunitaryhvacType):
    return idf.newidfobject('ZONEHVAC:HYBRIDUNITARYHVAC', **kwargs)

def ZonehvacIdealloadsairsystem(idf, **kwargs: ZonehvacIdealloadsairsystemType):
    return idf.newidfobject('ZONEHVAC:IDEALLOADSAIRSYSTEM', **kwargs)

def ZonehvacLowtemperatureradiantConstantflow(idf, **kwargs: ZonehvacLowtemperatureradiantConstantflowType):
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:CONSTANTFLOW', **kwargs)

def ZonehvacLowtemperatureradiantConstantflowDesign(idf, **kwargs: ZonehvacLowtemperatureradiantConstantflowDesignType):
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:CONSTANTFLOW:DESIGN', **kwargs)

def ZonehvacLowtemperatureradiantElectric(idf, **kwargs: ZonehvacLowtemperatureradiantElectricType):
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:ELECTRIC', **kwargs)

def ZonehvacLowtemperatureradiantSurfacegroup(idf, **kwargs: ZonehvacLowtemperatureradiantSurfacegroupType):
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:SURFACEGROUP', **kwargs)

def ZonehvacLowtemperatureradiantVariableflow(idf, **kwargs: ZonehvacLowtemperatureradiantVariableflowType):
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:VARIABLEFLOW', **kwargs)

def ZonehvacLowtemperatureradiantVariableflowDesign(idf, **kwargs: ZonehvacLowtemperatureradiantVariableflowDesignType):
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:VARIABLEFLOW:DESIGN', **kwargs)

def ZonehvacOutdoorairunit(idf, **kwargs: ZonehvacOutdoorairunitType):
    return idf.newidfobject('ZONEHVAC:OUTDOORAIRUNIT', **kwargs)

def ZonehvacOutdoorairunitEquipmentlist(idf, **kwargs: ZonehvacOutdoorairunitEquipmentlistType):
    return idf.newidfobject('ZONEHVAC:OUTDOORAIRUNIT:EQUIPMENTLIST', **kwargs)

def ZonehvacPackagedterminalairconditioner(idf, **kwargs: ZonehvacPackagedterminalairconditionerType):
    return idf.newidfobject('ZONEHVAC:PACKAGEDTERMINALAIRCONDITIONER', **kwargs)

def ZonehvacPackagedterminalheatpump(idf, **kwargs: ZonehvacPackagedterminalheatpumpType):
    return idf.newidfobject('ZONEHVAC:PACKAGEDTERMINALHEATPUMP', **kwargs)

def ZonehvacRefrigerationchillerset(idf, **kwargs: ZonehvacRefrigerationchillersetType):
    return idf.newidfobject('ZONEHVAC:REFRIGERATIONCHILLERSET', **kwargs)

def ZonehvacTerminalunitVariablerefrigerantflow(idf, **kwargs: ZonehvacTerminalunitVariablerefrigerantflowType):
    return idf.newidfobject('ZONEHVAC:TERMINALUNIT:VARIABLEREFRIGERANTFLOW', **kwargs)

def ZonehvacUnitheater(idf, **kwargs: ZonehvacUnitheaterType):
    return idf.newidfobject('ZONEHVAC:UNITHEATER', **kwargs)

def ZonehvacUnitventilator(idf, **kwargs: ZonehvacUnitventilatorType):
    return idf.newidfobject('ZONEHVAC:UNITVENTILATOR', **kwargs)

def ZonehvacVentilatedslab(idf, **kwargs: ZonehvacVentilatedslabType):
    return idf.newidfobject('ZONEHVAC:VENTILATEDSLAB', **kwargs)

def ZonehvacVentilatedslabSlabgroup(idf, **kwargs: ZonehvacVentilatedslabSlabgroupType):
    return idf.newidfobject('ZONEHVAC:VENTILATEDSLAB:SLABGROUP', **kwargs)

def ZonehvacWatertoairheatpump(idf, **kwargs: ZonehvacWatertoairheatpumpType):
    return idf.newidfobject('ZONEHVAC:WATERTOAIRHEATPUMP', **kwargs)

def ZonehvacWindowairconditioner(idf, **kwargs: ZonehvacWindowairconditionerType):
    return idf.newidfobject('ZONEHVAC:WINDOWAIRCONDITIONER', **kwargs)

def ZoneinfiltrationDesignflowrate(idf, **kwargs: ZoneinfiltrationDesignflowrateType):
    return idf.newidfobject('ZONEINFILTRATION:DESIGNFLOWRATE', **kwargs)

def ZoneinfiltrationEffectiveleakagearea(idf, **kwargs: ZoneinfiltrationEffectiveleakageareaType):
    return idf.newidfobject('ZONEINFILTRATION:EFFECTIVELEAKAGEAREA', **kwargs)

def ZoneinfiltrationFlowcoefficient(idf, **kwargs: ZoneinfiltrationFlowcoefficientType):
    return idf.newidfobject('ZONEINFILTRATION:FLOWCOEFFICIENT', **kwargs)

def Zonelist(idf, **kwargs: ZonelistType):
    return idf.newidfobject('ZONELIST', **kwargs)

def Zonemixing(idf, **kwargs: ZonemixingType):
    return idf.newidfobject('ZONEMIXING', **kwargs)

def ZonepropertyLocalenvironment(idf, **kwargs: ZonepropertyLocalenvironmentType):
    return idf.newidfobject('ZONEPROPERTY:LOCALENVIRONMENT', **kwargs)

def ZonepropertyUserviewfactorsBysurfacename(idf, **kwargs: ZonepropertyUserviewfactorsBysurfacenameType):
    return idf.newidfobject('ZONEPROPERTY:USERVIEWFACTORS:BYSURFACENAME', **kwargs)

def Zonerefrigerationdoormixing(idf, **kwargs: ZonerefrigerationdoormixingType):
    return idf.newidfobject('ZONEREFRIGERATIONDOORMIXING', **kwargs)

def Zoneterminalunitlist(idf, **kwargs: ZoneterminalunitlistType):
    return idf.newidfobject('ZONETERMINALUNITLIST', **kwargs)

def Zonethermalchimney(idf, **kwargs: ZonethermalchimneyType):
    return idf.newidfobject('ZONETHERMALCHIMNEY', **kwargs)

def ZoneventilationDesignflowrate(idf, **kwargs: ZoneventilationDesignflowrateType):
    return idf.newidfobject('ZONEVENTILATION:DESIGNFLOWRATE', **kwargs)

def ZoneventilationWindandstackopenarea(idf, **kwargs: ZoneventilationWindandstackopenareaType):
    return idf.newidfobject('ZONEVENTILATION:WINDANDSTACKOPENAREA', **kwargs)
