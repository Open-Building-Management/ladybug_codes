from __future__ import annotations
from .idf_types import *

def AirconditionerVariablerefrigerantflow(idf, **kwargs: AirconditionerVariablerefrigerantflow):
    return idf.newidfobject('AIRCONDITIONER:VARIABLEREFRIGERANTFLOW', **kwargs)

def AirconditionerVariablerefrigerantflowFluidtemperaturecontrol(idf, **kwargs: AirconditionerVariablerefrigerantflowFluidtemperaturecontrol):
    return idf.newidfobject('AIRCONDITIONER:VARIABLEREFRIGERANTFLOW:FLUIDTEMPERATURECONTROL', **kwargs)

def AirconditionerVariablerefrigerantflowFluidtemperaturecontrolHr(idf, **kwargs: AirconditionerVariablerefrigerantflowFluidtemperaturecontrolHr):
    return idf.newidfobject('AIRCONDITIONER:VARIABLEREFRIGERANTFLOW:FLUIDTEMPERATURECONTROL:HR', **kwargs)

def AirflownetworkDistributionComponentCoil(idf, **kwargs: AirflownetworkDistributionComponentCoil):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:COIL', **kwargs)

def AirflownetworkDistributionComponentConstantpressuredrop(idf, **kwargs: AirflownetworkDistributionComponentConstantpressuredrop):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:CONSTANTPRESSUREDROP', **kwargs)

def AirflownetworkDistributionComponentDuct(idf, **kwargs: AirflownetworkDistributionComponentDuct):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:DUCT', **kwargs)

def AirflownetworkDistributionComponentFan(idf, **kwargs: AirflownetworkDistributionComponentFan):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:FAN', **kwargs)

def AirflownetworkDistributionComponentHeatexchanger(idf, **kwargs: AirflownetworkDistributionComponentHeatexchanger):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:HEATEXCHANGER', **kwargs)

def AirflownetworkDistributionComponentLeak(idf, **kwargs: AirflownetworkDistributionComponentLeak):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:LEAK', **kwargs)

def AirflownetworkDistributionComponentLeakageratio(idf, **kwargs: AirflownetworkDistributionComponentLeakageratio):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:LEAKAGERATIO', **kwargs)

def AirflownetworkDistributionComponentOutdoorairflow(idf, **kwargs: AirflownetworkDistributionComponentOutdoorairflow):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:OUTDOORAIRFLOW', **kwargs)

def AirflownetworkDistributionComponentReliefairflow(idf, **kwargs: AirflownetworkDistributionComponentReliefairflow):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:RELIEFAIRFLOW', **kwargs)

def AirflownetworkDistributionComponentTerminalunit(idf, **kwargs: AirflownetworkDistributionComponentTerminalunit):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:COMPONENT:TERMINALUNIT', **kwargs)

def AirflownetworkDistributionDuctsizing(idf, **kwargs: AirflownetworkDistributionDuctsizing):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:DUCTSIZING', **kwargs)

def AirflownetworkDistributionDuctviewfactors(idf, **kwargs: AirflownetworkDistributionDuctviewfactors):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:DUCTVIEWFACTORS', **kwargs)

def AirflownetworkDistributionLinkage(idf, **kwargs: AirflownetworkDistributionLinkage):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:LINKAGE', **kwargs)

def AirflownetworkDistributionNode(idf, **kwargs: AirflownetworkDistributionNode):
    return idf.newidfobject('AIRFLOWNETWORK:DISTRIBUTION:NODE', **kwargs)

def AirflownetworkIntrazoneLinkage(idf, **kwargs: AirflownetworkIntrazoneLinkage):
    return idf.newidfobject('AIRFLOWNETWORK:INTRAZONE:LINKAGE', **kwargs)

def AirflownetworkIntrazoneNode(idf, **kwargs: AirflownetworkIntrazoneNode):
    return idf.newidfobject('AIRFLOWNETWORK:INTRAZONE:NODE', **kwargs)

def AirflownetworkMultizoneComponentDetailedopening(idf, **kwargs: AirflownetworkMultizoneComponentDetailedopening):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:COMPONENT:DETAILEDOPENING', **kwargs)

def AirflownetworkMultizoneComponentHorizontalopening(idf, **kwargs: AirflownetworkMultizoneComponentHorizontalopening):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:COMPONENT:HORIZONTALOPENING', **kwargs)

def AirflownetworkMultizoneComponentSimpleopening(idf, **kwargs: AirflownetworkMultizoneComponentSimpleopening):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:COMPONENT:SIMPLEOPENING', **kwargs)

def AirflownetworkMultizoneComponentZoneexhaustfan(idf, **kwargs: AirflownetworkMultizoneComponentZoneexhaustfan):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:COMPONENT:ZONEEXHAUSTFAN', **kwargs)

def AirflownetworkMultizoneExternalnode(idf, **kwargs: AirflownetworkMultizoneExternalnode):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:EXTERNALNODE', **kwargs)

def AirflownetworkMultizoneReferencecrackconditions(idf, **kwargs: AirflownetworkMultizoneReferencecrackconditions):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:REFERENCECRACKCONDITIONS', **kwargs)

def AirflownetworkMultizoneSpecifiedflowrate(idf, **kwargs: AirflownetworkMultizoneSpecifiedflowrate):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:SPECIFIEDFLOWRATE', **kwargs)

def AirflownetworkMultizoneSurface(idf, **kwargs: AirflownetworkMultizoneSurface):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:SURFACE', **kwargs)

def AirflownetworkMultizoneSurfaceCrack(idf, **kwargs: AirflownetworkMultizoneSurfaceCrack):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:SURFACE:CRACK', **kwargs)

def AirflownetworkMultizoneSurfaceEffectiveleakagearea(idf, **kwargs: AirflownetworkMultizoneSurfaceEffectiveleakagearea):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:SURFACE:EFFECTIVELEAKAGEAREA', **kwargs)

def AirflownetworkMultizoneWindpressurecoefficientarray(idf, **kwargs: AirflownetworkMultizoneWindpressurecoefficientarray):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:WINDPRESSURECOEFFICIENTARRAY', **kwargs)

def AirflownetworkMultizoneWindpressurecoefficientvalues(idf, **kwargs: AirflownetworkMultizoneWindpressurecoefficientvalues):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:WINDPRESSURECOEFFICIENTVALUES', **kwargs)

def AirflownetworkMultizoneZone(idf, **kwargs: AirflownetworkMultizoneZone):
    return idf.newidfobject('AIRFLOWNETWORK:MULTIZONE:ZONE', **kwargs)

def AirflownetworkOccupantventilationcontrol(idf, **kwargs: AirflownetworkOccupantventilationcontrol):
    return idf.newidfobject('AIRFLOWNETWORK:OCCUPANTVENTILATIONCONTROL', **kwargs)

def AirflownetworkSimulationcontrol(idf, **kwargs: AirflownetworkSimulationcontrol):
    return idf.newidfobject('AIRFLOWNETWORK:SIMULATIONCONTROL', **kwargs)

def AirflownetworkZonecontrolPressurecontroller(idf, **kwargs: AirflownetworkZonecontrolPressurecontroller):
    return idf.newidfobject('AIRFLOWNETWORK:ZONECONTROL:PRESSURECONTROLLER', **kwargs)

def Airloophvac(idf, **kwargs: Airloophvac):
    return idf.newidfobject('AIRLOOPHVAC', **kwargs)

def AirloophvacControllerlist(idf, **kwargs: AirloophvacControllerlist):
    return idf.newidfobject('AIRLOOPHVAC:CONTROLLERLIST', **kwargs)

def AirloophvacDedicatedoutdoorairsystem(idf, **kwargs: AirloophvacDedicatedoutdoorairsystem):
    return idf.newidfobject('AIRLOOPHVAC:DEDICATEDOUTDOORAIRSYSTEM', **kwargs)

def AirloophvacExhaustsystem(idf, **kwargs: AirloophvacExhaustsystem):
    return idf.newidfobject('AIRLOOPHVAC:EXHAUSTSYSTEM', **kwargs)

def AirloophvacMixer(idf, **kwargs: AirloophvacMixer):
    return idf.newidfobject('AIRLOOPHVAC:MIXER', **kwargs)

def AirloophvacOutdoorairsystem(idf, **kwargs: AirloophvacOutdoorairsystem):
    return idf.newidfobject('AIRLOOPHVAC:OUTDOORAIRSYSTEM', **kwargs)

def AirloophvacOutdoorairsystemEquipmentlist(idf, **kwargs: AirloophvacOutdoorairsystemEquipmentlist):
    return idf.newidfobject('AIRLOOPHVAC:OUTDOORAIRSYSTEM:EQUIPMENTLIST', **kwargs)

def AirloophvacReturnpath(idf, **kwargs: AirloophvacReturnpath):
    return idf.newidfobject('AIRLOOPHVAC:RETURNPATH', **kwargs)

def AirloophvacReturnplenum(idf, **kwargs: AirloophvacReturnplenum):
    return idf.newidfobject('AIRLOOPHVAC:RETURNPLENUM', **kwargs)

def AirloophvacSplitter(idf, **kwargs: AirloophvacSplitter):
    return idf.newidfobject('AIRLOOPHVAC:SPLITTER', **kwargs)

def AirloophvacSupplypath(idf, **kwargs: AirloophvacSupplypath):
    return idf.newidfobject('AIRLOOPHVAC:SUPPLYPATH', **kwargs)

def AirloophvacSupplyplenum(idf, **kwargs: AirloophvacSupplyplenum):
    return idf.newidfobject('AIRLOOPHVAC:SUPPLYPLENUM', **kwargs)

def AirloophvacUnitaryFurnaceHeatcool(idf, **kwargs: AirloophvacUnitaryFurnaceHeatcool):
    return idf.newidfobject('AIRLOOPHVAC:UNITARY:FURNACE:HEATCOOL', **kwargs)

def AirloophvacUnitaryFurnaceHeatonly(idf, **kwargs: AirloophvacUnitaryFurnaceHeatonly):
    return idf.newidfobject('AIRLOOPHVAC:UNITARY:FURNACE:HEATONLY', **kwargs)

def AirloophvacUnitaryheatcool(idf, **kwargs: AirloophvacUnitaryheatcool):
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATCOOL', **kwargs)

def AirloophvacUnitaryheatcoolVavchangeoverbypass(idf, **kwargs: AirloophvacUnitaryheatcoolVavchangeoverbypass):
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATCOOL:VAVCHANGEOVERBYPASS', **kwargs)

def AirloophvacUnitaryheatonly(idf, **kwargs: AirloophvacUnitaryheatonly):
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATONLY', **kwargs)

def AirloophvacUnitaryheatpumpAirtoair(idf, **kwargs: AirloophvacUnitaryheatpumpAirtoair):
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATPUMP:AIRTOAIR', **kwargs)

def AirloophvacUnitaryheatpumpAirtoairMultispeed(idf, **kwargs: AirloophvacUnitaryheatpumpAirtoairMultispeed):
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATPUMP:AIRTOAIR:MULTISPEED', **kwargs)

def AirloophvacUnitaryheatpumpWatertoair(idf, **kwargs: AirloophvacUnitaryheatpumpWatertoair):
    return idf.newidfobject('AIRLOOPHVAC:UNITARYHEATPUMP:WATERTOAIR', **kwargs)

def AirloophvacUnitarysystem(idf, **kwargs: AirloophvacUnitarysystem):
    return idf.newidfobject('AIRLOOPHVAC:UNITARYSYSTEM', **kwargs)

def AirloophvacZonemixer(idf, **kwargs: AirloophvacZonemixer):
    return idf.newidfobject('AIRLOOPHVAC:ZONEMIXER', **kwargs)

def AirloophvacZonesplitter(idf, **kwargs: AirloophvacZonesplitter):
    return idf.newidfobject('AIRLOOPHVAC:ZONESPLITTER', **kwargs)

def AirterminalDualductConstantvolume(idf, **kwargs: AirterminalDualductConstantvolume):
    return idf.newidfobject('AIRTERMINAL:DUALDUCT:CONSTANTVOLUME', **kwargs)

def AirterminalDualductVav(idf, **kwargs: AirterminalDualductVav):
    return idf.newidfobject('AIRTERMINAL:DUALDUCT:VAV', **kwargs)

def AirterminalDualductVavOutdoorair(idf, **kwargs: AirterminalDualductVavOutdoorair):
    return idf.newidfobject('AIRTERMINAL:DUALDUCT:VAV:OUTDOORAIR', **kwargs)

def AirterminalSingleductConstantvolumeCooledbeam(idf, **kwargs: AirterminalSingleductConstantvolumeCooledbeam):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:COOLEDBEAM', **kwargs)

def AirterminalSingleductConstantvolumeFourpipebeam(idf, **kwargs: AirterminalSingleductConstantvolumeFourpipebeam):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:FOURPIPEBEAM', **kwargs)

def AirterminalSingleductConstantvolumeFourpipeinduction(idf, **kwargs: AirterminalSingleductConstantvolumeFourpipeinduction):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:FOURPIPEINDUCTION', **kwargs)

def AirterminalSingleductConstantvolumeNoreheat(idf, **kwargs: AirterminalSingleductConstantvolumeNoreheat):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:NOREHEAT', **kwargs)

def AirterminalSingleductConstantvolumeReheat(idf, **kwargs: AirterminalSingleductConstantvolumeReheat):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:REHEAT', **kwargs)

def AirterminalSingleductMixer(idf, **kwargs: AirterminalSingleductMixer):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:MIXER', **kwargs)

def AirterminalSingleductParallelpiuReheat(idf, **kwargs: AirterminalSingleductParallelpiuReheat):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:PARALLELPIU:REHEAT', **kwargs)

def AirterminalSingleductSeriespiuReheat(idf, **kwargs: AirterminalSingleductSeriespiuReheat):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:SERIESPIU:REHEAT', **kwargs)

def AirterminalSingleductUserdefined(idf, **kwargs: AirterminalSingleductUserdefined):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:USERDEFINED', **kwargs)

def AirterminalSingleductVavHeatandcoolNoreheat(idf, **kwargs: AirterminalSingleductVavHeatandcoolNoreheat):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:VAV:HEATANDCOOL:NOREHEAT', **kwargs)

def AirterminalSingleductVavHeatandcoolReheat(idf, **kwargs: AirterminalSingleductVavHeatandcoolReheat):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:VAV:HEATANDCOOL:REHEAT', **kwargs)

def AirterminalSingleductVavNoreheat(idf, **kwargs: AirterminalSingleductVavNoreheat):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:VAV:NOREHEAT', **kwargs)

def AirterminalSingleductVavReheat(idf, **kwargs: AirterminalSingleductVavReheat):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:VAV:REHEAT', **kwargs)

def AirterminalSingleductVavReheatVariablespeedfan(idf, **kwargs: AirterminalSingleductVavReheatVariablespeedfan):
    return idf.newidfobject('AIRTERMINAL:SINGLEDUCT:VAV:REHEAT:VARIABLESPEEDFAN', **kwargs)

def AvailabilitymanagerDifferentialthermostat(idf, **kwargs: AvailabilitymanagerDifferentialthermostat):
    return idf.newidfobject('AVAILABILITYMANAGER:DIFFERENTIALTHERMOSTAT', **kwargs)

def AvailabilitymanagerHightemperatureturnoff(idf, **kwargs: AvailabilitymanagerHightemperatureturnoff):
    return idf.newidfobject('AVAILABILITYMANAGER:HIGHTEMPERATURETURNOFF', **kwargs)

def AvailabilitymanagerHightemperatureturnon(idf, **kwargs: AvailabilitymanagerHightemperatureturnon):
    return idf.newidfobject('AVAILABILITYMANAGER:HIGHTEMPERATURETURNON', **kwargs)

def AvailabilitymanagerHybridventilation(idf, **kwargs: AvailabilitymanagerHybridventilation):
    return idf.newidfobject('AVAILABILITYMANAGER:HYBRIDVENTILATION', **kwargs)

def AvailabilitymanagerLowtemperatureturnoff(idf, **kwargs: AvailabilitymanagerLowtemperatureturnoff):
    return idf.newidfobject('AVAILABILITYMANAGER:LOWTEMPERATURETURNOFF', **kwargs)

def AvailabilitymanagerLowtemperatureturnon(idf, **kwargs: AvailabilitymanagerLowtemperatureturnon):
    return idf.newidfobject('AVAILABILITYMANAGER:LOWTEMPERATURETURNON', **kwargs)

def AvailabilitymanagerNightcycle(idf, **kwargs: AvailabilitymanagerNightcycle):
    return idf.newidfobject('AVAILABILITYMANAGER:NIGHTCYCLE', **kwargs)

def AvailabilitymanagerNightventilation(idf, **kwargs: AvailabilitymanagerNightventilation):
    return idf.newidfobject('AVAILABILITYMANAGER:NIGHTVENTILATION', **kwargs)

def AvailabilitymanagerOptimumstart(idf, **kwargs: AvailabilitymanagerOptimumstart):
    return idf.newidfobject('AVAILABILITYMANAGER:OPTIMUMSTART', **kwargs)

def AvailabilitymanagerScheduled(idf, **kwargs: AvailabilitymanagerScheduled):
    return idf.newidfobject('AVAILABILITYMANAGER:SCHEDULED', **kwargs)

def AvailabilitymanagerScheduledoff(idf, **kwargs: AvailabilitymanagerScheduledoff):
    return idf.newidfobject('AVAILABILITYMANAGER:SCHEDULEDOFF', **kwargs)

def AvailabilitymanagerScheduledon(idf, **kwargs: AvailabilitymanagerScheduledon):
    return idf.newidfobject('AVAILABILITYMANAGER:SCHEDULEDON', **kwargs)

def Availabilitymanagerassignmentlist(idf, **kwargs: Availabilitymanagerassignmentlist):
    return idf.newidfobject('AVAILABILITYMANAGERASSIGNMENTLIST', **kwargs)

def BoilerHotwater(idf, **kwargs: BoilerHotwater):
    return idf.newidfobject('BOILER:HOTWATER', **kwargs)

def BoilerSteam(idf, **kwargs: BoilerSteam):
    return idf.newidfobject('BOILER:STEAM', **kwargs)

def Branch(idf, **kwargs: Branch):
    return idf.newidfobject('BRANCH', **kwargs)

def Branchlist(idf, **kwargs: Branchlist):
    return idf.newidfobject('BRANCHLIST', **kwargs)

def Building(idf, **kwargs: Building):
    return idf.newidfobject('BUILDING', **kwargs)

def BuildingsurfaceDetailed(idf, **kwargs: BuildingsurfaceDetailed):
    return idf.newidfobject('BUILDINGSURFACE:DETAILED', **kwargs)

def CeilingAdiabatic(idf, **kwargs: CeilingAdiabatic):
    return idf.newidfobject('CEILING:ADIABATIC', **kwargs)

def CeilingInterzone(idf, **kwargs: CeilingInterzone):
    return idf.newidfobject('CEILING:INTERZONE', **kwargs)

def Centralheatpumpsystem(idf, **kwargs: Centralheatpumpsystem):
    return idf.newidfobject('CENTRALHEATPUMPSYSTEM', **kwargs)

def ChillerAbsorption(idf, **kwargs: ChillerAbsorption):
    return idf.newidfobject('CHILLER:ABSORPTION', **kwargs)

def ChillerAbsorptionIndirect(idf, **kwargs: ChillerAbsorptionIndirect):
    return idf.newidfobject('CHILLER:ABSORPTION:INDIRECT', **kwargs)

def ChillerCombustionturbine(idf, **kwargs: ChillerCombustionturbine):
    return idf.newidfobject('CHILLER:COMBUSTIONTURBINE', **kwargs)

def ChillerConstantcop(idf, **kwargs: ChillerConstantcop):
    return idf.newidfobject('CHILLER:CONSTANTCOP', **kwargs)

def ChillerElectric(idf, **kwargs: ChillerElectric):
    return idf.newidfobject('CHILLER:ELECTRIC', **kwargs)

def ChillerElectricAshrae205(idf, **kwargs: ChillerElectricAshrae205):
    return idf.newidfobject('CHILLER:ELECTRIC:ASHRAE205', **kwargs)

def ChillerElectricEir(idf, **kwargs: ChillerElectricEir):
    return idf.newidfobject('CHILLER:ELECTRIC:EIR', **kwargs)

def ChillerElectricReformulatedeir(idf, **kwargs: ChillerElectricReformulatedeir):
    return idf.newidfobject('CHILLER:ELECTRIC:REFORMULATEDEIR', **kwargs)

def ChillerEnginedriven(idf, **kwargs: ChillerEnginedriven):
    return idf.newidfobject('CHILLER:ENGINEDRIVEN', **kwargs)

def ChillerheaterAbsorptionDirectfired(idf, **kwargs: ChillerheaterAbsorptionDirectfired):
    return idf.newidfobject('CHILLERHEATER:ABSORPTION:DIRECTFIRED', **kwargs)

def ChillerheaterAbsorptionDoubleeffect(idf, **kwargs: ChillerheaterAbsorptionDoubleeffect):
    return idf.newidfobject('CHILLERHEATER:ABSORPTION:DOUBLEEFFECT', **kwargs)

def ChillerheaterperformanceElectricEir(idf, **kwargs: ChillerheaterperformanceElectricEir):
    return idf.newidfobject('CHILLERHEATERPERFORMANCE:ELECTRIC:EIR', **kwargs)

def CoilCoolingDx(idf, **kwargs: CoilCoolingDx):
    return idf.newidfobject('COIL:COOLING:DX', **kwargs)

def CoilCoolingDxCurvefitOperatingmode(idf, **kwargs: CoilCoolingDxCurvefitOperatingmode):
    return idf.newidfobject('COIL:COOLING:DX:CURVEFIT:OPERATINGMODE', **kwargs)

def CoilCoolingDxCurvefitPerformance(idf, **kwargs: CoilCoolingDxCurvefitPerformance):
    return idf.newidfobject('COIL:COOLING:DX:CURVEFIT:PERFORMANCE', **kwargs)

def CoilCoolingDxCurvefitSpeed(idf, **kwargs: CoilCoolingDxCurvefitSpeed):
    return idf.newidfobject('COIL:COOLING:DX:CURVEFIT:SPEED', **kwargs)

def CoilCoolingDxMultispeed(idf, **kwargs: CoilCoolingDxMultispeed):
    return idf.newidfobject('COIL:COOLING:DX:MULTISPEED', **kwargs)

def CoilCoolingDxSinglespeed(idf, **kwargs: CoilCoolingDxSinglespeed):
    return idf.newidfobject('COIL:COOLING:DX:SINGLESPEED', **kwargs)

def CoilCoolingDxSinglespeedThermalstorage(idf, **kwargs: CoilCoolingDxSinglespeedThermalstorage):
    return idf.newidfobject('COIL:COOLING:DX:SINGLESPEED:THERMALSTORAGE', **kwargs)

def CoilCoolingDxTwospeed(idf, **kwargs: CoilCoolingDxTwospeed):
    return idf.newidfobject('COIL:COOLING:DX:TWOSPEED', **kwargs)

def CoilCoolingDxTwostagewithhumiditycontrolmode(idf, **kwargs: CoilCoolingDxTwostagewithhumiditycontrolmode):
    return idf.newidfobject('COIL:COOLING:DX:TWOSTAGEWITHHUMIDITYCONTROLMODE', **kwargs)

def CoilCoolingDxVariablerefrigerantflow(idf, **kwargs: CoilCoolingDxVariablerefrigerantflow):
    return idf.newidfobject('COIL:COOLING:DX:VARIABLEREFRIGERANTFLOW', **kwargs)

def CoilCoolingDxVariablerefrigerantflowFluidtemperaturecontrol(idf, **kwargs: CoilCoolingDxVariablerefrigerantflowFluidtemperaturecontrol):
    return idf.newidfobject('COIL:COOLING:DX:VARIABLEREFRIGERANTFLOW:FLUIDTEMPERATURECONTROL', **kwargs)

def CoilCoolingDxVariablespeed(idf, **kwargs: CoilCoolingDxVariablespeed):
    return idf.newidfobject('COIL:COOLING:DX:VARIABLESPEED', **kwargs)

def CoilCoolingWater(idf, **kwargs: CoilCoolingWater):
    return idf.newidfobject('COIL:COOLING:WATER', **kwargs)

def CoilCoolingWaterDetailedgeometry(idf, **kwargs: CoilCoolingWaterDetailedgeometry):
    return idf.newidfobject('COIL:COOLING:WATER:DETAILEDGEOMETRY', **kwargs)

def CoilCoolingWatertoairheatpumpEquationfit(idf, **kwargs: CoilCoolingWatertoairheatpumpEquationfit):
    return idf.newidfobject('COIL:COOLING:WATERTOAIRHEATPUMP:EQUATIONFIT', **kwargs)

def CoilCoolingWatertoairheatpumpParameterestimation(idf, **kwargs: CoilCoolingWatertoairheatpumpParameterestimation):
    return idf.newidfobject('COIL:COOLING:WATERTOAIRHEATPUMP:PARAMETERESTIMATION', **kwargs)

def CoilCoolingWatertoairheatpumpVariablespeedequationfit(idf, **kwargs: CoilCoolingWatertoairheatpumpVariablespeedequationfit):
    return idf.newidfobject('COIL:COOLING:WATERTOAIRHEATPUMP:VARIABLESPEEDEQUATIONFIT', **kwargs)

def CoilHeatingDesuperheater(idf, **kwargs: CoilHeatingDesuperheater):
    return idf.newidfobject('COIL:HEATING:DESUPERHEATER', **kwargs)

def CoilHeatingDxMultispeed(idf, **kwargs: CoilHeatingDxMultispeed):
    return idf.newidfobject('COIL:HEATING:DX:MULTISPEED', **kwargs)

def CoilHeatingDxSinglespeed(idf, **kwargs: CoilHeatingDxSinglespeed):
    return idf.newidfobject('COIL:HEATING:DX:SINGLESPEED', **kwargs)

def CoilHeatingDxVariablerefrigerantflow(idf, **kwargs: CoilHeatingDxVariablerefrigerantflow):
    return idf.newidfobject('COIL:HEATING:DX:VARIABLEREFRIGERANTFLOW', **kwargs)

def CoilHeatingDxVariablerefrigerantflowFluidtemperaturecontrol(idf, **kwargs: CoilHeatingDxVariablerefrigerantflowFluidtemperaturecontrol):
    return idf.newidfobject('COIL:HEATING:DX:VARIABLEREFRIGERANTFLOW:FLUIDTEMPERATURECONTROL', **kwargs)

def CoilHeatingDxVariablespeed(idf, **kwargs: CoilHeatingDxVariablespeed):
    return idf.newidfobject('COIL:HEATING:DX:VARIABLESPEED', **kwargs)

def CoilHeatingElectric(idf, **kwargs: CoilHeatingElectric):
    return idf.newidfobject('COIL:HEATING:ELECTRIC', **kwargs)

def CoilHeatingElectricMultistage(idf, **kwargs: CoilHeatingElectricMultistage):
    return idf.newidfobject('COIL:HEATING:ELECTRIC:MULTISTAGE', **kwargs)

def CoilHeatingFuel(idf, **kwargs: CoilHeatingFuel):
    return idf.newidfobject('COIL:HEATING:FUEL', **kwargs)

def CoilHeatingGasMultistage(idf, **kwargs: CoilHeatingGasMultistage):
    return idf.newidfobject('COIL:HEATING:GAS:MULTISTAGE', **kwargs)

def CoilHeatingSteam(idf, **kwargs: CoilHeatingSteam):
    return idf.newidfobject('COIL:HEATING:STEAM', **kwargs)

def CoilHeatingWater(idf, **kwargs: CoilHeatingWater):
    return idf.newidfobject('COIL:HEATING:WATER', **kwargs)

def CoilHeatingWatertoairheatpumpEquationfit(idf, **kwargs: CoilHeatingWatertoairheatpumpEquationfit):
    return idf.newidfobject('COIL:HEATING:WATERTOAIRHEATPUMP:EQUATIONFIT', **kwargs)

def CoilHeatingWatertoairheatpumpParameterestimation(idf, **kwargs: CoilHeatingWatertoairheatpumpParameterestimation):
    return idf.newidfobject('COIL:HEATING:WATERTOAIRHEATPUMP:PARAMETERESTIMATION', **kwargs)

def CoilHeatingWatertoairheatpumpVariablespeedequationfit(idf, **kwargs: CoilHeatingWatertoairheatpumpVariablespeedequationfit):
    return idf.newidfobject('COIL:HEATING:WATERTOAIRHEATPUMP:VARIABLESPEEDEQUATIONFIT', **kwargs)

def CoilUserdefined(idf, **kwargs: CoilUserdefined):
    return idf.newidfobject('COIL:USERDEFINED', **kwargs)

def CoilWaterheatingAirtowaterheatpumpPumped(idf, **kwargs: CoilWaterheatingAirtowaterheatpumpPumped):
    return idf.newidfobject('COIL:WATERHEATING:AIRTOWATERHEATPUMP:PUMPED', **kwargs)

def CoilWaterheatingAirtowaterheatpumpVariablespeed(idf, **kwargs: CoilWaterheatingAirtowaterheatpumpVariablespeed):
    return idf.newidfobject('COIL:WATERHEATING:AIRTOWATERHEATPUMP:VARIABLESPEED', **kwargs)

def CoilWaterheatingAirtowaterheatpumpWrapped(idf, **kwargs: CoilWaterheatingAirtowaterheatpumpWrapped):
    return idf.newidfobject('COIL:WATERHEATING:AIRTOWATERHEATPUMP:WRAPPED', **kwargs)

def CoilWaterheatingDesuperheater(idf, **kwargs: CoilWaterheatingDesuperheater):
    return idf.newidfobject('COIL:WATERHEATING:DESUPERHEATER', **kwargs)

def CoilperformanceDxCooling(idf, **kwargs: CoilperformanceDxCooling):
    return idf.newidfobject('COILPERFORMANCE:DX:COOLING', **kwargs)

def CoilsystemCoolingDx(idf, **kwargs: CoilsystemCoolingDx):
    return idf.newidfobject('COILSYSTEM:COOLING:DX', **kwargs)

def CoilsystemCoolingDxHeatexchangerassisted(idf, **kwargs: CoilsystemCoolingDxHeatexchangerassisted):
    return idf.newidfobject('COILSYSTEM:COOLING:DX:HEATEXCHANGERASSISTED', **kwargs)

def CoilsystemCoolingWater(idf, **kwargs: CoilsystemCoolingWater):
    return idf.newidfobject('COILSYSTEM:COOLING:WATER', **kwargs)

def CoilsystemCoolingWaterHeatexchangerassisted(idf, **kwargs: CoilsystemCoolingWaterHeatexchangerassisted):
    return idf.newidfobject('COILSYSTEM:COOLING:WATER:HEATEXCHANGERASSISTED', **kwargs)

def CoilsystemHeatingDx(idf, **kwargs: CoilsystemHeatingDx):
    return idf.newidfobject('COILSYSTEM:HEATING:DX', **kwargs)

def CoilsystemIntegratedheatpumpAirsource(idf, **kwargs: CoilsystemIntegratedheatpumpAirsource):
    return idf.newidfobject('COILSYSTEM:INTEGRATEDHEATPUMP:AIRSOURCE', **kwargs)

def Comfortviewfactorangles(idf, **kwargs: Comfortviewfactorangles):
    return idf.newidfobject('COMFORTVIEWFACTORANGLES', **kwargs)

def ComplexfenestrationpropertySolarabsorbedlayers(idf, **kwargs: ComplexfenestrationpropertySolarabsorbedlayers):
    return idf.newidfobject('COMPLEXFENESTRATIONPROPERTY:SOLARABSORBEDLAYERS', **kwargs)

def ComplianceBuilding(idf, **kwargs: ComplianceBuilding):
    return idf.newidfobject('COMPLIANCE:BUILDING', **kwargs)

def ComponentcostAdjustments(idf, **kwargs: ComponentcostAdjustments):
    return idf.newidfobject('COMPONENTCOST:ADJUSTMENTS', **kwargs)

def ComponentcostLineitem(idf, **kwargs: ComponentcostLineitem):
    return idf.newidfobject('COMPONENTCOST:LINEITEM', **kwargs)

def ComponentcostReference(idf, **kwargs: ComponentcostReference):
    return idf.newidfobject('COMPONENTCOST:REFERENCE', **kwargs)

def Condenserequipmentlist(idf, **kwargs: Condenserequipmentlist):
    return idf.newidfobject('CONDENSEREQUIPMENTLIST', **kwargs)

def Condenserequipmentoperationschemes(idf, **kwargs: Condenserequipmentoperationschemes):
    return idf.newidfobject('CONDENSEREQUIPMENTOPERATIONSCHEMES', **kwargs)

def Condenserloop(idf, **kwargs: Condenserloop):
    return idf.newidfobject('CONDENSERLOOP', **kwargs)

def ConnectorMixer(idf, **kwargs: ConnectorMixer):
    return idf.newidfobject('CONNECTOR:MIXER', **kwargs)

def ConnectorSplitter(idf, **kwargs: ConnectorSplitter):
    return idf.newidfobject('CONNECTOR:SPLITTER', **kwargs)

def Connectorlist(idf, **kwargs: Connectorlist):
    return idf.newidfobject('CONNECTORLIST', **kwargs)

def Construction(idf, **kwargs: Construction):
    return idf.newidfobject('CONSTRUCTION', **kwargs)

def ConstructionAirboundary(idf, **kwargs: ConstructionAirboundary):
    return idf.newidfobject('CONSTRUCTION:AIRBOUNDARY', **kwargs)

def ConstructionCfactorundergroundwall(idf, **kwargs: ConstructionCfactorundergroundwall):
    return idf.newidfobject('CONSTRUCTION:CFACTORUNDERGROUNDWALL', **kwargs)

def ConstructionComplexfenestrationstate(idf, **kwargs: ConstructionComplexfenestrationstate):
    return idf.newidfobject('CONSTRUCTION:COMPLEXFENESTRATIONSTATE', **kwargs)

def ConstructionFfactorgroundfloor(idf, **kwargs: ConstructionFfactorgroundfloor):
    return idf.newidfobject('CONSTRUCTION:FFACTORGROUNDFLOOR', **kwargs)

def ConstructionWindowdatafile(idf, **kwargs: ConstructionWindowdatafile):
    return idf.newidfobject('CONSTRUCTION:WINDOWDATAFILE', **kwargs)

def ConstructionWindowequivalentlayer(idf, **kwargs: ConstructionWindowequivalentlayer):
    return idf.newidfobject('CONSTRUCTION:WINDOWEQUIVALENTLAYER', **kwargs)

def ConstructionpropertyInternalheatsource(idf, **kwargs: ConstructionpropertyInternalheatsource):
    return idf.newidfobject('CONSTRUCTIONPROPERTY:INTERNALHEATSOURCE', **kwargs)

def ControllerMechanicalventilation(idf, **kwargs: ControllerMechanicalventilation):
    return idf.newidfobject('CONTROLLER:MECHANICALVENTILATION', **kwargs)

def ControllerOutdoorair(idf, **kwargs: ControllerOutdoorair):
    return idf.newidfobject('CONTROLLER:OUTDOORAIR', **kwargs)

def ControllerWatercoil(idf, **kwargs: ControllerWatercoil):
    return idf.newidfobject('CONTROLLER:WATERCOIL', **kwargs)

def Convergencelimits(idf, **kwargs: Convergencelimits):
    return idf.newidfobject('CONVERGENCELIMITS', **kwargs)

def CoolingtowerSinglespeed(idf, **kwargs: CoolingtowerSinglespeed):
    return idf.newidfobject('COOLINGTOWER:SINGLESPEED', **kwargs)

def CoolingtowerTwospeed(idf, **kwargs: CoolingtowerTwospeed):
    return idf.newidfobject('COOLINGTOWER:TWOSPEED', **kwargs)

def CoolingtowerVariablespeed(idf, **kwargs: CoolingtowerVariablespeed):
    return idf.newidfobject('COOLINGTOWER:VARIABLESPEED', **kwargs)

def CoolingtowerVariablespeedMerkel(idf, **kwargs: CoolingtowerVariablespeedMerkel):
    return idf.newidfobject('COOLINGTOWER:VARIABLESPEED:MERKEL', **kwargs)

def CoolingtowerperformanceCooltools(idf, **kwargs: CoolingtowerperformanceCooltools):
    return idf.newidfobject('COOLINGTOWERPERFORMANCE:COOLTOOLS', **kwargs)

def CoolingtowerperformanceYorkcalc(idf, **kwargs: CoolingtowerperformanceYorkcalc):
    return idf.newidfobject('COOLINGTOWERPERFORMANCE:YORKCALC', **kwargs)

def Currencytype(idf, **kwargs: Currencytype):
    return idf.newidfobject('CURRENCYTYPE', **kwargs)

def CurveBicubic(idf, **kwargs: CurveBicubic):
    return idf.newidfobject('CURVE:BICUBIC', **kwargs)

def CurveBiquadratic(idf, **kwargs: CurveBiquadratic):
    return idf.newidfobject('CURVE:BIQUADRATIC', **kwargs)

def CurveChillerpartloadwithlift(idf, **kwargs: CurveChillerpartloadwithlift):
    return idf.newidfobject('CURVE:CHILLERPARTLOADWITHLIFT', **kwargs)

def CurveCubic(idf, **kwargs: CurveCubic):
    return idf.newidfobject('CURVE:CUBIC', **kwargs)

def CurveCubiclinear(idf, **kwargs: CurveCubiclinear):
    return idf.newidfobject('CURVE:CUBICLINEAR', **kwargs)

def CurveDoubleexponentialdecay(idf, **kwargs: CurveDoubleexponentialdecay):
    return idf.newidfobject('CURVE:DOUBLEEXPONENTIALDECAY', **kwargs)

def CurveExponent(idf, **kwargs: CurveExponent):
    return idf.newidfobject('CURVE:EXPONENT', **kwargs)

def CurveExponentialdecay(idf, **kwargs: CurveExponentialdecay):
    return idf.newidfobject('CURVE:EXPONENTIALDECAY', **kwargs)

def CurveExponentialskewnormal(idf, **kwargs: CurveExponentialskewnormal):
    return idf.newidfobject('CURVE:EXPONENTIALSKEWNORMAL', **kwargs)

def CurveFanpressurerise(idf, **kwargs: CurveFanpressurerise):
    return idf.newidfobject('CURVE:FANPRESSURERISE', **kwargs)

def CurveFunctionalPressuredrop(idf, **kwargs: CurveFunctionalPressuredrop):
    return idf.newidfobject('CURVE:FUNCTIONAL:PRESSUREDROP', **kwargs)

def CurveLinear(idf, **kwargs: CurveLinear):
    return idf.newidfobject('CURVE:LINEAR', **kwargs)

def CurveQuadlinear(idf, **kwargs: CurveQuadlinear):
    return idf.newidfobject('CURVE:QUADLINEAR', **kwargs)

def CurveQuadratic(idf, **kwargs: CurveQuadratic):
    return idf.newidfobject('CURVE:QUADRATIC', **kwargs)

def CurveQuadraticlinear(idf, **kwargs: CurveQuadraticlinear):
    return idf.newidfobject('CURVE:QUADRATICLINEAR', **kwargs)

def CurveQuartic(idf, **kwargs: CurveQuartic):
    return idf.newidfobject('CURVE:QUARTIC', **kwargs)

def CurveQuintlinear(idf, **kwargs: CurveQuintlinear):
    return idf.newidfobject('CURVE:QUINTLINEAR', **kwargs)

def CurveRectangularhyperbola1(idf, **kwargs: CurveRectangularhyperbola1):
    return idf.newidfobject('CURVE:RECTANGULARHYPERBOLA1', **kwargs)

def CurveRectangularhyperbola2(idf, **kwargs: CurveRectangularhyperbola2):
    return idf.newidfobject('CURVE:RECTANGULARHYPERBOLA2', **kwargs)

def CurveSigmoid(idf, **kwargs: CurveSigmoid):
    return idf.newidfobject('CURVE:SIGMOID', **kwargs)

def CurveTriquadratic(idf, **kwargs: CurveTriquadratic):
    return idf.newidfobject('CURVE:TRIQUADRATIC', **kwargs)

def DaylightingControls(idf, **kwargs: DaylightingControls):
    return idf.newidfobject('DAYLIGHTING:CONTROLS', **kwargs)

def DaylightingDelightComplexfenestration(idf, **kwargs: DaylightingDelightComplexfenestration):
    return idf.newidfobject('DAYLIGHTING:DELIGHT:COMPLEXFENESTRATION', **kwargs)

def DaylightingReferencepoint(idf, **kwargs: DaylightingReferencepoint):
    return idf.newidfobject('DAYLIGHTING:REFERENCEPOINT', **kwargs)

def DaylightingdeviceLightwell(idf, **kwargs: DaylightingdeviceLightwell):
    return idf.newidfobject('DAYLIGHTINGDEVICE:LIGHTWELL', **kwargs)

def DaylightingdeviceShelf(idf, **kwargs: DaylightingdeviceShelf):
    return idf.newidfobject('DAYLIGHTINGDEVICE:SHELF', **kwargs)

def DaylightingdeviceTubular(idf, **kwargs: DaylightingdeviceTubular):
    return idf.newidfobject('DAYLIGHTINGDEVICE:TUBULAR', **kwargs)

def DehumidifierDesiccantNofans(idf, **kwargs: DehumidifierDesiccantNofans):
    return idf.newidfobject('DEHUMIDIFIER:DESICCANT:NOFANS', **kwargs)

def DehumidifierDesiccantSystem(idf, **kwargs: DehumidifierDesiccantSystem):
    return idf.newidfobject('DEHUMIDIFIER:DESICCANT:SYSTEM', **kwargs)

def DemandmanagerElectricequipment(idf, **kwargs: DemandmanagerElectricequipment):
    return idf.newidfobject('DEMANDMANAGER:ELECTRICEQUIPMENT', **kwargs)

def DemandmanagerExteriorlights(idf, **kwargs: DemandmanagerExteriorlights):
    return idf.newidfobject('DEMANDMANAGER:EXTERIORLIGHTS', **kwargs)

def DemandmanagerLights(idf, **kwargs: DemandmanagerLights):
    return idf.newidfobject('DEMANDMANAGER:LIGHTS', **kwargs)

def DemandmanagerThermostats(idf, **kwargs: DemandmanagerThermostats):
    return idf.newidfobject('DEMANDMANAGER:THERMOSTATS', **kwargs)

def DemandmanagerVentilation(idf, **kwargs: DemandmanagerVentilation):
    return idf.newidfobject('DEMANDMANAGER:VENTILATION', **kwargs)

def Demandmanagerassignmentlist(idf, **kwargs: Demandmanagerassignmentlist):
    return idf.newidfobject('DEMANDMANAGERASSIGNMENTLIST', **kwargs)

def DesignspecificationAirterminalSizing(idf, **kwargs: DesignspecificationAirterminalSizing):
    return idf.newidfobject('DESIGNSPECIFICATION:AIRTERMINAL:SIZING', **kwargs)

def DesignspecificationOutdoorair(idf, **kwargs: DesignspecificationOutdoorair):
    return idf.newidfobject('DESIGNSPECIFICATION:OUTDOORAIR', **kwargs)

def DesignspecificationOutdoorairSpacelist(idf, **kwargs: DesignspecificationOutdoorairSpacelist):
    return idf.newidfobject('DESIGNSPECIFICATION:OUTDOORAIR:SPACELIST', **kwargs)

def DesignspecificationZoneairdistribution(idf, **kwargs: DesignspecificationZoneairdistribution):
    return idf.newidfobject('DESIGNSPECIFICATION:ZONEAIRDISTRIBUTION', **kwargs)

def DesignspecificationZonehvacSizing(idf, **kwargs: DesignspecificationZonehvacSizing):
    return idf.newidfobject('DESIGNSPECIFICATION:ZONEHVAC:SIZING', **kwargs)

def Districtcooling(idf, **kwargs: Districtcooling):
    return idf.newidfobject('DISTRICTCOOLING', **kwargs)

def DistrictheatingSteam(idf, **kwargs: DistrictheatingSteam):
    return idf.newidfobject('DISTRICTHEATING:STEAM', **kwargs)

def DistrictheatingWater(idf, **kwargs: DistrictheatingWater):
    return idf.newidfobject('DISTRICTHEATING:WATER', **kwargs)

def Door(idf, **kwargs: Door):
    return idf.newidfobject('DOOR', **kwargs)

def DoorInterzone(idf, **kwargs: DoorInterzone):
    return idf.newidfobject('DOOR:INTERZONE', **kwargs)

def Duct(idf, **kwargs: Duct):
    return idf.newidfobject('DUCT', **kwargs)

def Electricequipment(idf, **kwargs: Electricequipment):
    return idf.newidfobject('ELECTRICEQUIPMENT', **kwargs)

def ElectricequipmentIteAircooled(idf, **kwargs: ElectricequipmentIteAircooled):
    return idf.newidfobject('ELECTRICEQUIPMENT:ITE:AIRCOOLED', **kwargs)

def ElectricloadcenterDistribution(idf, **kwargs: ElectricloadcenterDistribution):
    return idf.newidfobject('ELECTRICLOADCENTER:DISTRIBUTION', **kwargs)

def ElectricloadcenterGenerators(idf, **kwargs: ElectricloadcenterGenerators):
    return idf.newidfobject('ELECTRICLOADCENTER:GENERATORS', **kwargs)

def ElectricloadcenterInverterFunctionofpower(idf, **kwargs: ElectricloadcenterInverterFunctionofpower):
    return idf.newidfobject('ELECTRICLOADCENTER:INVERTER:FUNCTIONOFPOWER', **kwargs)

def ElectricloadcenterInverterLookuptable(idf, **kwargs: ElectricloadcenterInverterLookuptable):
    return idf.newidfobject('ELECTRICLOADCENTER:INVERTER:LOOKUPTABLE', **kwargs)

def ElectricloadcenterInverterPvwatts(idf, **kwargs: ElectricloadcenterInverterPvwatts):
    return idf.newidfobject('ELECTRICLOADCENTER:INVERTER:PVWATTS', **kwargs)

def ElectricloadcenterInverterSimple(idf, **kwargs: ElectricloadcenterInverterSimple):
    return idf.newidfobject('ELECTRICLOADCENTER:INVERTER:SIMPLE', **kwargs)

def ElectricloadcenterStorageBattery(idf, **kwargs: ElectricloadcenterStorageBattery):
    return idf.newidfobject('ELECTRICLOADCENTER:STORAGE:BATTERY', **kwargs)

def ElectricloadcenterStorageConverter(idf, **kwargs: ElectricloadcenterStorageConverter):
    return idf.newidfobject('ELECTRICLOADCENTER:STORAGE:CONVERTER', **kwargs)

def ElectricloadcenterStorageLiionnmcbattery(idf, **kwargs: ElectricloadcenterStorageLiionnmcbattery):
    return idf.newidfobject('ELECTRICLOADCENTER:STORAGE:LIIONNMCBATTERY', **kwargs)

def ElectricloadcenterStorageSimple(idf, **kwargs: ElectricloadcenterStorageSimple):
    return idf.newidfobject('ELECTRICLOADCENTER:STORAGE:SIMPLE', **kwargs)

def ElectricloadcenterTransformer(idf, **kwargs: ElectricloadcenterTransformer):
    return idf.newidfobject('ELECTRICLOADCENTER:TRANSFORMER', **kwargs)

def EnergymanagementsystemActuator(idf, **kwargs: EnergymanagementsystemActuator):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:ACTUATOR', **kwargs)

def EnergymanagementsystemConstructionindexvariable(idf, **kwargs: EnergymanagementsystemConstructionindexvariable):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:CONSTRUCTIONINDEXVARIABLE', **kwargs)

def EnergymanagementsystemCurveortableindexvariable(idf, **kwargs: EnergymanagementsystemCurveortableindexvariable):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:CURVEORTABLEINDEXVARIABLE', **kwargs)

def EnergymanagementsystemGlobalvariable(idf, **kwargs: EnergymanagementsystemGlobalvariable):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:GLOBALVARIABLE', **kwargs)

def EnergymanagementsystemInternalvariable(idf, **kwargs: EnergymanagementsystemInternalvariable):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:INTERNALVARIABLE', **kwargs)

def EnergymanagementsystemMeteredoutputvariable(idf, **kwargs: EnergymanagementsystemMeteredoutputvariable):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:METEREDOUTPUTVARIABLE', **kwargs)

def EnergymanagementsystemOutputvariable(idf, **kwargs: EnergymanagementsystemOutputvariable):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:OUTPUTVARIABLE', **kwargs)

def EnergymanagementsystemProgram(idf, **kwargs: EnergymanagementsystemProgram):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:PROGRAM', **kwargs)

def EnergymanagementsystemProgramcallingmanager(idf, **kwargs: EnergymanagementsystemProgramcallingmanager):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:PROGRAMCALLINGMANAGER', **kwargs)

def EnergymanagementsystemSensor(idf, **kwargs: EnergymanagementsystemSensor):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:SENSOR', **kwargs)

def EnergymanagementsystemSubroutine(idf, **kwargs: EnergymanagementsystemSubroutine):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:SUBROUTINE', **kwargs)

def EnergymanagementsystemTrendvariable(idf, **kwargs: EnergymanagementsystemTrendvariable):
    return idf.newidfobject('ENERGYMANAGEMENTSYSTEM:TRENDVARIABLE', **kwargs)

def Environmentalimpactfactors(idf, **kwargs: Environmentalimpactfactors):
    return idf.newidfobject('ENVIRONMENTALIMPACTFACTORS', **kwargs)

def EvaporativecoolerDirectCeldekpad(idf, **kwargs: EvaporativecoolerDirectCeldekpad):
    return idf.newidfobject('EVAPORATIVECOOLER:DIRECT:CELDEKPAD', **kwargs)

def EvaporativecoolerDirectResearchspecial(idf, **kwargs: EvaporativecoolerDirectResearchspecial):
    return idf.newidfobject('EVAPORATIVECOOLER:DIRECT:RESEARCHSPECIAL', **kwargs)

def EvaporativecoolerIndirectCeldekpad(idf, **kwargs: EvaporativecoolerIndirectCeldekpad):
    return idf.newidfobject('EVAPORATIVECOOLER:INDIRECT:CELDEKPAD', **kwargs)

def EvaporativecoolerIndirectResearchspecial(idf, **kwargs: EvaporativecoolerIndirectResearchspecial):
    return idf.newidfobject('EVAPORATIVECOOLER:INDIRECT:RESEARCHSPECIAL', **kwargs)

def EvaporativecoolerIndirectWetcoil(idf, **kwargs: EvaporativecoolerIndirectWetcoil):
    return idf.newidfobject('EVAPORATIVECOOLER:INDIRECT:WETCOIL', **kwargs)

def EvaporativefluidcoolerSinglespeed(idf, **kwargs: EvaporativefluidcoolerSinglespeed):
    return idf.newidfobject('EVAPORATIVEFLUIDCOOLER:SINGLESPEED', **kwargs)

def EvaporativefluidcoolerTwospeed(idf, **kwargs: EvaporativefluidcoolerTwospeed):
    return idf.newidfobject('EVAPORATIVEFLUIDCOOLER:TWOSPEED', **kwargs)

def ExteriorFuelequipment(idf, **kwargs: ExteriorFuelequipment):
    return idf.newidfobject('EXTERIOR:FUELEQUIPMENT', **kwargs)

def ExteriorLights(idf, **kwargs: ExteriorLights):
    return idf.newidfobject('EXTERIOR:LIGHTS', **kwargs)

def ExteriorWaterequipment(idf, **kwargs: ExteriorWaterequipment):
    return idf.newidfobject('EXTERIOR:WATEREQUIPMENT', **kwargs)

def Externalinterface(idf, **kwargs: Externalinterface):
    return idf.newidfobject('EXTERNALINTERFACE', **kwargs)

def ExternalinterfaceActuator(idf, **kwargs: ExternalinterfaceActuator):
    return idf.newidfobject('EXTERNALINTERFACE:ACTUATOR', **kwargs)

def ExternalinterfaceFunctionalmockupunitexportFromVariable(idf, **kwargs: ExternalinterfaceFunctionalmockupunitexportFromVariable):
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITEXPORT:FROM:VARIABLE', **kwargs)

def ExternalinterfaceFunctionalmockupunitexportToActuator(idf, **kwargs: ExternalinterfaceFunctionalmockupunitexportToActuator):
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITEXPORT:TO:ACTUATOR', **kwargs)

def ExternalinterfaceFunctionalmockupunitexportToSchedule(idf, **kwargs: ExternalinterfaceFunctionalmockupunitexportToSchedule):
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITEXPORT:TO:SCHEDULE', **kwargs)

def ExternalinterfaceFunctionalmockupunitexportToVariable(idf, **kwargs: ExternalinterfaceFunctionalmockupunitexportToVariable):
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITEXPORT:TO:VARIABLE', **kwargs)

def ExternalinterfaceFunctionalmockupunitimport(idf, **kwargs: ExternalinterfaceFunctionalmockupunitimport):
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT', **kwargs)

def ExternalinterfaceFunctionalmockupunitimportFromVariable(idf, **kwargs: ExternalinterfaceFunctionalmockupunitimportFromVariable):
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT:FROM:VARIABLE', **kwargs)

def ExternalinterfaceFunctionalmockupunitimportToActuator(idf, **kwargs: ExternalinterfaceFunctionalmockupunitimportToActuator):
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT:TO:ACTUATOR', **kwargs)

def ExternalinterfaceFunctionalmockupunitimportToSchedule(idf, **kwargs: ExternalinterfaceFunctionalmockupunitimportToSchedule):
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT:TO:SCHEDULE', **kwargs)

def ExternalinterfaceFunctionalmockupunitimportToVariable(idf, **kwargs: ExternalinterfaceFunctionalmockupunitimportToVariable):
    return idf.newidfobject('EXTERNALINTERFACE:FUNCTIONALMOCKUPUNITIMPORT:TO:VARIABLE', **kwargs)

def ExternalinterfaceSchedule(idf, **kwargs: ExternalinterfaceSchedule):
    return idf.newidfobject('EXTERNALINTERFACE:SCHEDULE', **kwargs)

def ExternalinterfaceVariable(idf, **kwargs: ExternalinterfaceVariable):
    return idf.newidfobject('EXTERNALINTERFACE:VARIABLE', **kwargs)

def FanComponentmodel(idf, **kwargs: FanComponentmodel):
    return idf.newidfobject('FAN:COMPONENTMODEL', **kwargs)

def FanConstantvolume(idf, **kwargs: FanConstantvolume):
    return idf.newidfobject('FAN:CONSTANTVOLUME', **kwargs)

def FanOnoff(idf, **kwargs: FanOnoff):
    return idf.newidfobject('FAN:ONOFF', **kwargs)

def FanSystemmodel(idf, **kwargs: FanSystemmodel):
    return idf.newidfobject('FAN:SYSTEMMODEL', **kwargs)

def FanVariablevolume(idf, **kwargs: FanVariablevolume):
    return idf.newidfobject('FAN:VARIABLEVOLUME', **kwargs)

def FanZoneexhaust(idf, **kwargs: FanZoneexhaust):
    return idf.newidfobject('FAN:ZONEEXHAUST', **kwargs)

def FanperformanceNightventilation(idf, **kwargs: FanperformanceNightventilation):
    return idf.newidfobject('FANPERFORMANCE:NIGHTVENTILATION', **kwargs)

def FaultmodelEnthalpysensoroffsetOutdoorair(idf, **kwargs: FaultmodelEnthalpysensoroffsetOutdoorair):
    return idf.newidfobject('FAULTMODEL:ENTHALPYSENSOROFFSET:OUTDOORAIR', **kwargs)

def FaultmodelEnthalpysensoroffsetReturnair(idf, **kwargs: FaultmodelEnthalpysensoroffsetReturnair):
    return idf.newidfobject('FAULTMODEL:ENTHALPYSENSOROFFSET:RETURNAIR', **kwargs)

def FaultmodelFoulingAirfilter(idf, **kwargs: FaultmodelFoulingAirfilter):
    return idf.newidfobject('FAULTMODEL:FOULING:AIRFILTER', **kwargs)

def FaultmodelFoulingBoiler(idf, **kwargs: FaultmodelFoulingBoiler):
    return idf.newidfobject('FAULTMODEL:FOULING:BOILER', **kwargs)

def FaultmodelFoulingChiller(idf, **kwargs: FaultmodelFoulingChiller):
    return idf.newidfobject('FAULTMODEL:FOULING:CHILLER', **kwargs)

def FaultmodelFoulingCoil(idf, **kwargs: FaultmodelFoulingCoil):
    return idf.newidfobject('FAULTMODEL:FOULING:COIL', **kwargs)

def FaultmodelFoulingCoolingtower(idf, **kwargs: FaultmodelFoulingCoolingtower):
    return idf.newidfobject('FAULTMODEL:FOULING:COOLINGTOWER', **kwargs)

def FaultmodelFoulingEvaporativecooler(idf, **kwargs: FaultmodelFoulingEvaporativecooler):
    return idf.newidfobject('FAULTMODEL:FOULING:EVAPORATIVECOOLER', **kwargs)

def FaultmodelHumidistatoffset(idf, **kwargs: FaultmodelHumidistatoffset):
    return idf.newidfobject('FAULTMODEL:HUMIDISTATOFFSET', **kwargs)

def FaultmodelHumiditysensoroffsetOutdoorair(idf, **kwargs: FaultmodelHumiditysensoroffsetOutdoorair):
    return idf.newidfobject('FAULTMODEL:HUMIDITYSENSOROFFSET:OUTDOORAIR', **kwargs)

def FaultmodelTemperaturesensoroffsetChillersupplywater(idf, **kwargs: FaultmodelTemperaturesensoroffsetChillersupplywater):
    return idf.newidfobject('FAULTMODEL:TEMPERATURESENSOROFFSET:CHILLERSUPPLYWATER', **kwargs)

def FaultmodelTemperaturesensoroffsetCoilsupplyair(idf, **kwargs: FaultmodelTemperaturesensoroffsetCoilsupplyair):
    return idf.newidfobject('FAULTMODEL:TEMPERATURESENSOROFFSET:COILSUPPLYAIR', **kwargs)

def FaultmodelTemperaturesensoroffsetCondensersupplywater(idf, **kwargs: FaultmodelTemperaturesensoroffsetCondensersupplywater):
    return idf.newidfobject('FAULTMODEL:TEMPERATURESENSOROFFSET:CONDENSERSUPPLYWATER', **kwargs)

def FaultmodelTemperaturesensoroffsetOutdoorair(idf, **kwargs: FaultmodelTemperaturesensoroffsetOutdoorair):
    return idf.newidfobject('FAULTMODEL:TEMPERATURESENSOROFFSET:OUTDOORAIR', **kwargs)

def FaultmodelTemperaturesensoroffsetReturnair(idf, **kwargs: FaultmodelTemperaturesensoroffsetReturnair):
    return idf.newidfobject('FAULTMODEL:TEMPERATURESENSOROFFSET:RETURNAIR', **kwargs)

def FaultmodelThermostatoffset(idf, **kwargs: FaultmodelThermostatoffset):
    return idf.newidfobject('FAULTMODEL:THERMOSTATOFFSET', **kwargs)

def FenestrationsurfaceDetailed(idf, **kwargs: FenestrationsurfaceDetailed):
    return idf.newidfobject('FENESTRATIONSURFACE:DETAILED', **kwargs)

def FloorAdiabatic(idf, **kwargs: FloorAdiabatic):
    return idf.newidfobject('FLOOR:ADIABATIC', **kwargs)

def FloorDetailed(idf, **kwargs: FloorDetailed):
    return idf.newidfobject('FLOOR:DETAILED', **kwargs)

def FloorGroundcontact(idf, **kwargs: FloorGroundcontact):
    return idf.newidfobject('FLOOR:GROUNDCONTACT', **kwargs)

def FloorInterzone(idf, **kwargs: FloorInterzone):
    return idf.newidfobject('FLOOR:INTERZONE', **kwargs)

def FluidcoolerSinglespeed(idf, **kwargs: FluidcoolerSinglespeed):
    return idf.newidfobject('FLUIDCOOLER:SINGLESPEED', **kwargs)

def FluidcoolerTwospeed(idf, **kwargs: FluidcoolerTwospeed):
    return idf.newidfobject('FLUIDCOOLER:TWOSPEED', **kwargs)

def FluidpropertiesConcentration(idf, **kwargs: FluidpropertiesConcentration):
    return idf.newidfobject('FLUIDPROPERTIES:CONCENTRATION', **kwargs)

def FluidpropertiesGlycolconcentration(idf, **kwargs: FluidpropertiesGlycolconcentration):
    return idf.newidfobject('FLUIDPROPERTIES:GLYCOLCONCENTRATION', **kwargs)

def FluidpropertiesName(idf, **kwargs: FluidpropertiesName):
    return idf.newidfobject('FLUIDPROPERTIES:NAME', **kwargs)

def FluidpropertiesSaturated(idf, **kwargs: FluidpropertiesSaturated):
    return idf.newidfobject('FLUIDPROPERTIES:SATURATED', **kwargs)

def FluidpropertiesSuperheated(idf, **kwargs: FluidpropertiesSuperheated):
    return idf.newidfobject('FLUIDPROPERTIES:SUPERHEATED', **kwargs)

def FluidpropertiesTemperatures(idf, **kwargs: FluidpropertiesTemperatures):
    return idf.newidfobject('FLUIDPROPERTIES:TEMPERATURES', **kwargs)

def FoundationKiva(idf, **kwargs: FoundationKiva):
    return idf.newidfobject('FOUNDATION:KIVA', **kwargs)

def FoundationKivaSettings(idf, **kwargs: FoundationKivaSettings):
    return idf.newidfobject('FOUNDATION:KIVA:SETTINGS', **kwargs)

def Fuelfactors(idf, **kwargs: Fuelfactors):
    return idf.newidfobject('FUELFACTORS', **kwargs)

def Gasequipment(idf, **kwargs: Gasequipment):
    return idf.newidfobject('GASEQUIPMENT', **kwargs)

def GeneratorCombustionturbine(idf, **kwargs: GeneratorCombustionturbine):
    return idf.newidfobject('GENERATOR:COMBUSTIONTURBINE', **kwargs)

def GeneratorFuelcell(idf, **kwargs: GeneratorFuelcell):
    return idf.newidfobject('GENERATOR:FUELCELL', **kwargs)

def GeneratorFuelcellAirsupply(idf, **kwargs: GeneratorFuelcellAirsupply):
    return idf.newidfobject('GENERATOR:FUELCELL:AIRSUPPLY', **kwargs)

def GeneratorFuelcellAuxiliaryheater(idf, **kwargs: GeneratorFuelcellAuxiliaryheater):
    return idf.newidfobject('GENERATOR:FUELCELL:AUXILIARYHEATER', **kwargs)

def GeneratorFuelcellElectricalstorage(idf, **kwargs: GeneratorFuelcellElectricalstorage):
    return idf.newidfobject('GENERATOR:FUELCELL:ELECTRICALSTORAGE', **kwargs)

def GeneratorFuelcellExhaustgastowaterheatexchanger(idf, **kwargs: GeneratorFuelcellExhaustgastowaterheatexchanger):
    return idf.newidfobject('GENERATOR:FUELCELL:EXHAUSTGASTOWATERHEATEXCHANGER', **kwargs)

def GeneratorFuelcellInverter(idf, **kwargs: GeneratorFuelcellInverter):
    return idf.newidfobject('GENERATOR:FUELCELL:INVERTER', **kwargs)

def GeneratorFuelcellPowermodule(idf, **kwargs: GeneratorFuelcellPowermodule):
    return idf.newidfobject('GENERATOR:FUELCELL:POWERMODULE', **kwargs)

def GeneratorFuelcellStackcooler(idf, **kwargs: GeneratorFuelcellStackcooler):
    return idf.newidfobject('GENERATOR:FUELCELL:STACKCOOLER', **kwargs)

def GeneratorFuelcellWatersupply(idf, **kwargs: GeneratorFuelcellWatersupply):
    return idf.newidfobject('GENERATOR:FUELCELL:WATERSUPPLY', **kwargs)

def GeneratorFuelsupply(idf, **kwargs: GeneratorFuelsupply):
    return idf.newidfobject('GENERATOR:FUELSUPPLY', **kwargs)

def GeneratorInternalcombustionengine(idf, **kwargs: GeneratorInternalcombustionengine):
    return idf.newidfobject('GENERATOR:INTERNALCOMBUSTIONENGINE', **kwargs)

def GeneratorMicrochp(idf, **kwargs: GeneratorMicrochp):
    return idf.newidfobject('GENERATOR:MICROCHP', **kwargs)

def GeneratorMicrochpNonnormalizedparameters(idf, **kwargs: GeneratorMicrochpNonnormalizedparameters):
    return idf.newidfobject('GENERATOR:MICROCHP:NONNORMALIZEDPARAMETERS', **kwargs)

def GeneratorMicroturbine(idf, **kwargs: GeneratorMicroturbine):
    return idf.newidfobject('GENERATOR:MICROTURBINE', **kwargs)

def GeneratorPhotovoltaic(idf, **kwargs: GeneratorPhotovoltaic):
    return idf.newidfobject('GENERATOR:PHOTOVOLTAIC', **kwargs)

def GeneratorPvwatts(idf, **kwargs: GeneratorPvwatts):
    return idf.newidfobject('GENERATOR:PVWATTS', **kwargs)

def GeneratorWindturbine(idf, **kwargs: GeneratorWindturbine):
    return idf.newidfobject('GENERATOR:WINDTURBINE', **kwargs)

def Geometrytransform(idf, **kwargs: Geometrytransform):
    return idf.newidfobject('GEOMETRYTRANSFORM', **kwargs)

def Glazeddoor(idf, **kwargs: Glazeddoor):
    return idf.newidfobject('GLAZEDDOOR', **kwargs)

def GlazeddoorInterzone(idf, **kwargs: GlazeddoorInterzone):
    return idf.newidfobject('GLAZEDDOOR:INTERZONE', **kwargs)

def Globalgeometryrules(idf, **kwargs: Globalgeometryrules):
    return idf.newidfobject('GLOBALGEOMETRYRULES', **kwargs)

def GroundheatexchangerHorizontaltrench(idf, **kwargs: GroundheatexchangerHorizontaltrench):
    return idf.newidfobject('GROUNDHEATEXCHANGER:HORIZONTALTRENCH', **kwargs)

def GroundheatexchangerPond(idf, **kwargs: GroundheatexchangerPond):
    return idf.newidfobject('GROUNDHEATEXCHANGER:POND', **kwargs)

def GroundheatexchangerResponsefactors(idf, **kwargs: GroundheatexchangerResponsefactors):
    return idf.newidfobject('GROUNDHEATEXCHANGER:RESPONSEFACTORS', **kwargs)

def GroundheatexchangerSlinky(idf, **kwargs: GroundheatexchangerSlinky):
    return idf.newidfobject('GROUNDHEATEXCHANGER:SLINKY', **kwargs)

def GroundheatexchangerSurface(idf, **kwargs: GroundheatexchangerSurface):
    return idf.newidfobject('GROUNDHEATEXCHANGER:SURFACE', **kwargs)

def GroundheatexchangerSystem(idf, **kwargs: GroundheatexchangerSystem):
    return idf.newidfobject('GROUNDHEATEXCHANGER:SYSTEM', **kwargs)

def GroundheatexchangerVerticalArray(idf, **kwargs: GroundheatexchangerVerticalArray):
    return idf.newidfobject('GROUNDHEATEXCHANGER:VERTICAL:ARRAY', **kwargs)

def GroundheatexchangerVerticalProperties(idf, **kwargs: GroundheatexchangerVerticalProperties):
    return idf.newidfobject('GROUNDHEATEXCHANGER:VERTICAL:PROPERTIES', **kwargs)

def GroundheatexchangerVerticalSingle(idf, **kwargs: GroundheatexchangerVerticalSingle):
    return idf.newidfobject('GROUNDHEATEXCHANGER:VERTICAL:SINGLE', **kwargs)

def GroundheattransferBasementAutogrid(idf, **kwargs: GroundheattransferBasementAutogrid):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:AUTOGRID', **kwargs)

def GroundheattransferBasementBldgdata(idf, **kwargs: GroundheattransferBasementBldgdata):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:BLDGDATA', **kwargs)

def GroundheattransferBasementCombldg(idf, **kwargs: GroundheattransferBasementCombldg):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:COMBLDG', **kwargs)

def GroundheattransferBasementEquivautogrid(idf, **kwargs: GroundheattransferBasementEquivautogrid):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:EQUIVAUTOGRID', **kwargs)

def GroundheattransferBasementEquivslab(idf, **kwargs: GroundheattransferBasementEquivslab):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:EQUIVSLAB', **kwargs)

def GroundheattransferBasementInsulation(idf, **kwargs: GroundheattransferBasementInsulation):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:INSULATION', **kwargs)

def GroundheattransferBasementInterior(idf, **kwargs: GroundheattransferBasementInterior):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:INTERIOR', **kwargs)

def GroundheattransferBasementManualgrid(idf, **kwargs: GroundheattransferBasementManualgrid):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:MANUALGRID', **kwargs)

def GroundheattransferBasementMatlprops(idf, **kwargs: GroundheattransferBasementMatlprops):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:MATLPROPS', **kwargs)

def GroundheattransferBasementSimparameters(idf, **kwargs: GroundheattransferBasementSimparameters):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:SIMPARAMETERS', **kwargs)

def GroundheattransferBasementSurfaceprops(idf, **kwargs: GroundheattransferBasementSurfaceprops):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:SURFACEPROPS', **kwargs)

def GroundheattransferBasementXface(idf, **kwargs: GroundheattransferBasementXface):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:XFACE', **kwargs)

def GroundheattransferBasementYface(idf, **kwargs: GroundheattransferBasementYface):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:YFACE', **kwargs)

def GroundheattransferBasementZface(idf, **kwargs: GroundheattransferBasementZface):
    return idf.newidfobject('GROUNDHEATTRANSFER:BASEMENT:ZFACE', **kwargs)

def GroundheattransferControl(idf, **kwargs: GroundheattransferControl):
    return idf.newidfobject('GROUNDHEATTRANSFER:CONTROL', **kwargs)

def GroundheattransferSlabAutogrid(idf, **kwargs: GroundheattransferSlabAutogrid):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:AUTOGRID', **kwargs)

def GroundheattransferSlabBldgprops(idf, **kwargs: GroundheattransferSlabBldgprops):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:BLDGPROPS', **kwargs)

def GroundheattransferSlabBoundconds(idf, **kwargs: GroundheattransferSlabBoundconds):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:BOUNDCONDS', **kwargs)

def GroundheattransferSlabEquivalentslab(idf, **kwargs: GroundheattransferSlabEquivalentslab):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:EQUIVALENTSLAB', **kwargs)

def GroundheattransferSlabInsulation(idf, **kwargs: GroundheattransferSlabInsulation):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:INSULATION', **kwargs)

def GroundheattransferSlabManualgrid(idf, **kwargs: GroundheattransferSlabManualgrid):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:MANUALGRID', **kwargs)

def GroundheattransferSlabMaterials(idf, **kwargs: GroundheattransferSlabMaterials):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:MATERIALS', **kwargs)

def GroundheattransferSlabMatlprops(idf, **kwargs: GroundheattransferSlabMatlprops):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:MATLPROPS', **kwargs)

def GroundheattransferSlabXface(idf, **kwargs: GroundheattransferSlabXface):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:XFACE', **kwargs)

def GroundheattransferSlabYface(idf, **kwargs: GroundheattransferSlabYface):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:YFACE', **kwargs)

def GroundheattransferSlabZface(idf, **kwargs: GroundheattransferSlabZface):
    return idf.newidfobject('GROUNDHEATTRANSFER:SLAB:ZFACE', **kwargs)

def HeaderedpumpsConstantspeed(idf, **kwargs: HeaderedpumpsConstantspeed):
    return idf.newidfobject('HEADEREDPUMPS:CONSTANTSPEED', **kwargs)

def HeaderedpumpsVariablespeed(idf, **kwargs: HeaderedpumpsVariablespeed):
    return idf.newidfobject('HEADEREDPUMPS:VARIABLESPEED', **kwargs)

def Heatbalancealgorithm(idf, **kwargs: Heatbalancealgorithm):
    return idf.newidfobject('HEATBALANCEALGORITHM', **kwargs)

def HeatbalancesettingsConductionfinitedifference(idf, **kwargs: HeatbalancesettingsConductionfinitedifference):
    return idf.newidfobject('HEATBALANCESETTINGS:CONDUCTIONFINITEDIFFERENCE', **kwargs)

def HeatexchangerAirtoairFlatplate(idf, **kwargs: HeatexchangerAirtoairFlatplate):
    return idf.newidfobject('HEATEXCHANGER:AIRTOAIR:FLATPLATE', **kwargs)

def HeatexchangerAirtoairSensibleandlatent(idf, **kwargs: HeatexchangerAirtoairSensibleandlatent):
    return idf.newidfobject('HEATEXCHANGER:AIRTOAIR:SENSIBLEANDLATENT', **kwargs)

def HeatexchangerDesiccantBalancedflow(idf, **kwargs: HeatexchangerDesiccantBalancedflow):
    return idf.newidfobject('HEATEXCHANGER:DESICCANT:BALANCEDFLOW', **kwargs)

def HeatexchangerDesiccantBalancedflowPerformancedatatype1(idf, **kwargs: HeatexchangerDesiccantBalancedflowPerformancedatatype1):
    return idf.newidfobject('HEATEXCHANGER:DESICCANT:BALANCEDFLOW:PERFORMANCEDATATYPE1', **kwargs)

def HeatexchangerFluidtofluid(idf, **kwargs: HeatexchangerFluidtofluid):
    return idf.newidfobject('HEATEXCHANGER:FLUIDTOFLUID', **kwargs)

def HeatpumpAirtowaterFuelfiredCooling(idf, **kwargs: HeatpumpAirtowaterFuelfiredCooling):
    return idf.newidfobject('HEATPUMP:AIRTOWATER:FUELFIRED:COOLING', **kwargs)

def HeatpumpAirtowaterFuelfiredHeating(idf, **kwargs: HeatpumpAirtowaterFuelfiredHeating):
    return idf.newidfobject('HEATPUMP:AIRTOWATER:FUELFIRED:HEATING', **kwargs)

def HeatpumpPlantloopEirCooling(idf, **kwargs: HeatpumpPlantloopEirCooling):
    return idf.newidfobject('HEATPUMP:PLANTLOOP:EIR:COOLING', **kwargs)

def HeatpumpPlantloopEirHeating(idf, **kwargs: HeatpumpPlantloopEirHeating):
    return idf.newidfobject('HEATPUMP:PLANTLOOP:EIR:HEATING', **kwargs)

def HeatpumpWatertowaterEquationfitCooling(idf, **kwargs: HeatpumpWatertowaterEquationfitCooling):
    return idf.newidfobject('HEATPUMP:WATERTOWATER:EQUATIONFIT:COOLING', **kwargs)

def HeatpumpWatertowaterEquationfitHeating(idf, **kwargs: HeatpumpWatertowaterEquationfitHeating):
    return idf.newidfobject('HEATPUMP:WATERTOWATER:EQUATIONFIT:HEATING', **kwargs)

def HeatpumpWatertowaterParameterestimationCooling(idf, **kwargs: HeatpumpWatertowaterParameterestimationCooling):
    return idf.newidfobject('HEATPUMP:WATERTOWATER:PARAMETERESTIMATION:COOLING', **kwargs)

def HeatpumpWatertowaterParameterestimationHeating(idf, **kwargs: HeatpumpWatertowaterParameterestimationHeating):
    return idf.newidfobject('HEATPUMP:WATERTOWATER:PARAMETERESTIMATION:HEATING', **kwargs)

def Hotwaterequipment(idf, **kwargs: Hotwaterequipment):
    return idf.newidfobject('HOTWATEREQUIPMENT', **kwargs)

def HumidifierSteamElectric(idf, **kwargs: HumidifierSteamElectric):
    return idf.newidfobject('HUMIDIFIER:STEAM:ELECTRIC', **kwargs)

def HumidifierSteamGas(idf, **kwargs: HumidifierSteamGas):
    return idf.newidfobject('HUMIDIFIER:STEAM:GAS', **kwargs)

def Hvacsystemrootfindingalgorithm(idf, **kwargs: Hvacsystemrootfindingalgorithm):
    return idf.newidfobject('HVACSYSTEMROOTFINDINGALGORITHM', **kwargs)

def HvactemplatePlantBoiler(idf, **kwargs: HvactemplatePlantBoiler):
    return idf.newidfobject('HVACTEMPLATE:PLANT:BOILER', **kwargs)

def HvactemplatePlantBoilerObjectreference(idf, **kwargs: HvactemplatePlantBoilerObjectreference):
    return idf.newidfobject('HVACTEMPLATE:PLANT:BOILER:OBJECTREFERENCE', **kwargs)

def HvactemplatePlantChilledwaterloop(idf, **kwargs: HvactemplatePlantChilledwaterloop):
    return idf.newidfobject('HVACTEMPLATE:PLANT:CHILLEDWATERLOOP', **kwargs)

def HvactemplatePlantChiller(idf, **kwargs: HvactemplatePlantChiller):
    return idf.newidfobject('HVACTEMPLATE:PLANT:CHILLER', **kwargs)

def HvactemplatePlantChillerObjectreference(idf, **kwargs: HvactemplatePlantChillerObjectreference):
    return idf.newidfobject('HVACTEMPLATE:PLANT:CHILLER:OBJECTREFERENCE', **kwargs)

def HvactemplatePlantHotwaterloop(idf, **kwargs: HvactemplatePlantHotwaterloop):
    return idf.newidfobject('HVACTEMPLATE:PLANT:HOTWATERLOOP', **kwargs)

def HvactemplatePlantMixedwaterloop(idf, **kwargs: HvactemplatePlantMixedwaterloop):
    return idf.newidfobject('HVACTEMPLATE:PLANT:MIXEDWATERLOOP', **kwargs)

def HvactemplatePlantTower(idf, **kwargs: HvactemplatePlantTower):
    return idf.newidfobject('HVACTEMPLATE:PLANT:TOWER', **kwargs)

def HvactemplatePlantTowerObjectreference(idf, **kwargs: HvactemplatePlantTowerObjectreference):
    return idf.newidfobject('HVACTEMPLATE:PLANT:TOWER:OBJECTREFERENCE', **kwargs)

def HvactemplateSystemConstantvolume(idf, **kwargs: HvactemplateSystemConstantvolume):
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:CONSTANTVOLUME', **kwargs)

def HvactemplateSystemDedicatedoutdoorair(idf, **kwargs: HvactemplateSystemDedicatedoutdoorair):
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:DEDICATEDOUTDOORAIR', **kwargs)

def HvactemplateSystemDualduct(idf, **kwargs: HvactemplateSystemDualduct):
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:DUALDUCT', **kwargs)

def HvactemplateSystemPackagedvav(idf, **kwargs: HvactemplateSystemPackagedvav):
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:PACKAGEDVAV', **kwargs)

def HvactemplateSystemUnitary(idf, **kwargs: HvactemplateSystemUnitary):
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:UNITARY', **kwargs)

def HvactemplateSystemUnitaryheatpumpAirtoair(idf, **kwargs: HvactemplateSystemUnitaryheatpumpAirtoair):
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:UNITARYHEATPUMP:AIRTOAIR', **kwargs)

def HvactemplateSystemUnitarysystem(idf, **kwargs: HvactemplateSystemUnitarysystem):
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:UNITARYSYSTEM', **kwargs)

def HvactemplateSystemVav(idf, **kwargs: HvactemplateSystemVav):
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:VAV', **kwargs)

def HvactemplateSystemVrf(idf, **kwargs: HvactemplateSystemVrf):
    return idf.newidfobject('HVACTEMPLATE:SYSTEM:VRF', **kwargs)

def HvactemplateThermostat(idf, **kwargs: HvactemplateThermostat):
    return idf.newidfobject('HVACTEMPLATE:THERMOSTAT', **kwargs)

def HvactemplateZoneBaseboardheat(idf, **kwargs: HvactemplateZoneBaseboardheat):
    return idf.newidfobject('HVACTEMPLATE:ZONE:BASEBOARDHEAT', **kwargs)

def HvactemplateZoneConstantvolume(idf, **kwargs: HvactemplateZoneConstantvolume):
    return idf.newidfobject('HVACTEMPLATE:ZONE:CONSTANTVOLUME', **kwargs)

def HvactemplateZoneDualduct(idf, **kwargs: HvactemplateZoneDualduct):
    return idf.newidfobject('HVACTEMPLATE:ZONE:DUALDUCT', **kwargs)

def HvactemplateZoneFancoil(idf, **kwargs: HvactemplateZoneFancoil):
    return idf.newidfobject('HVACTEMPLATE:ZONE:FANCOIL', **kwargs)

def HvactemplateZoneIdealloadsairsystem(idf, **kwargs: HvactemplateZoneIdealloadsairsystem):
    return idf.newidfobject('HVACTEMPLATE:ZONE:IDEALLOADSAIRSYSTEM', **kwargs)

def HvactemplateZonePtac(idf, **kwargs: HvactemplateZonePtac):
    return idf.newidfobject('HVACTEMPLATE:ZONE:PTAC', **kwargs)

def HvactemplateZonePthp(idf, **kwargs: HvactemplateZonePthp):
    return idf.newidfobject('HVACTEMPLATE:ZONE:PTHP', **kwargs)

def HvactemplateZoneUnitary(idf, **kwargs: HvactemplateZoneUnitary):
    return idf.newidfobject('HVACTEMPLATE:ZONE:UNITARY', **kwargs)

def HvactemplateZoneVav(idf, **kwargs: HvactemplateZoneVav):
    return idf.newidfobject('HVACTEMPLATE:ZONE:VAV', **kwargs)

def HvactemplateZoneVavFanpowered(idf, **kwargs: HvactemplateZoneVavFanpowered):
    return idf.newidfobject('HVACTEMPLATE:ZONE:VAV:FANPOWERED', **kwargs)

def HvactemplateZoneVavHeatandcool(idf, **kwargs: HvactemplateZoneVavHeatandcool):
    return idf.newidfobject('HVACTEMPLATE:ZONE:VAV:HEATANDCOOL', **kwargs)

def HvactemplateZoneVrf(idf, **kwargs: HvactemplateZoneVrf):
    return idf.newidfobject('HVACTEMPLATE:ZONE:VRF', **kwargs)

def HvactemplateZoneWatertoairheatpump(idf, **kwargs: HvactemplateZoneWatertoairheatpump):
    return idf.newidfobject('HVACTEMPLATE:ZONE:WATERTOAIRHEATPUMP', **kwargs)

def HybridmodelZone(idf, **kwargs: HybridmodelZone):
    return idf.newidfobject('HYBRIDMODEL:ZONE', **kwargs)

def Indoorlivingwall(idf, **kwargs: Indoorlivingwall):
    return idf.newidfobject('INDOORLIVINGWALL', **kwargs)

def Internalmass(idf, **kwargs: Internalmass):
    return idf.newidfobject('INTERNALMASS', **kwargs)

def LifecyclecostNonrecurringcost(idf, **kwargs: LifecyclecostNonrecurringcost):
    return idf.newidfobject('LIFECYCLECOST:NONRECURRINGCOST', **kwargs)

def LifecyclecostParameters(idf, **kwargs: LifecyclecostParameters):
    return idf.newidfobject('LIFECYCLECOST:PARAMETERS', **kwargs)

def LifecyclecostRecurringcosts(idf, **kwargs: LifecyclecostRecurringcosts):
    return idf.newidfobject('LIFECYCLECOST:RECURRINGCOSTS', **kwargs)

def LifecyclecostUseadjustment(idf, **kwargs: LifecyclecostUseadjustment):
    return idf.newidfobject('LIFECYCLECOST:USEADJUSTMENT', **kwargs)

def LifecyclecostUsepriceescalation(idf, **kwargs: LifecyclecostUsepriceescalation):
    return idf.newidfobject('LIFECYCLECOST:USEPRICEESCALATION', **kwargs)

def Lights(idf, **kwargs: Lights):
    return idf.newidfobject('LIGHTS', **kwargs)

def LoadprofilePlant(idf, **kwargs: LoadprofilePlant):
    return idf.newidfobject('LOADPROFILE:PLANT', **kwargs)

def Material(idf, **kwargs: Material):
    return idf.newidfobject('MATERIAL', **kwargs)

def MaterialAirgap(idf, **kwargs: MaterialAirgap):
    return idf.newidfobject('MATERIAL:AIRGAP', **kwargs)

def MaterialInfraredtransparent(idf, **kwargs: MaterialInfraredtransparent):
    return idf.newidfobject('MATERIAL:INFRAREDTRANSPARENT', **kwargs)

def MaterialNomass(idf, **kwargs: MaterialNomass):
    return idf.newidfobject('MATERIAL:NOMASS', **kwargs)

def MaterialRoofvegetation(idf, **kwargs: MaterialRoofvegetation):
    return idf.newidfobject('MATERIAL:ROOFVEGETATION', **kwargs)

def MaterialpropertyGlazingspectraldata(idf, **kwargs: MaterialpropertyGlazingspectraldata):
    return idf.newidfobject('MATERIALPROPERTY:GLAZINGSPECTRALDATA', **kwargs)

def MaterialpropertyHeatandmoisturetransferDiffusion(idf, **kwargs: MaterialpropertyHeatandmoisturetransferDiffusion):
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:DIFFUSION', **kwargs)

def MaterialpropertyHeatandmoisturetransferRedistribution(idf, **kwargs: MaterialpropertyHeatandmoisturetransferRedistribution):
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:REDISTRIBUTION', **kwargs)

def MaterialpropertyHeatandmoisturetransferSettings(idf, **kwargs: MaterialpropertyHeatandmoisturetransferSettings):
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:SETTINGS', **kwargs)

def MaterialpropertyHeatandmoisturetransferSorptionisotherm(idf, **kwargs: MaterialpropertyHeatandmoisturetransferSorptionisotherm):
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:SORPTIONISOTHERM', **kwargs)

def MaterialpropertyHeatandmoisturetransferSuction(idf, **kwargs: MaterialpropertyHeatandmoisturetransferSuction):
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:SUCTION', **kwargs)

def MaterialpropertyHeatandmoisturetransferThermalconductivity(idf, **kwargs: MaterialpropertyHeatandmoisturetransferThermalconductivity):
    return idf.newidfobject('MATERIALPROPERTY:HEATANDMOISTURETRANSFER:THERMALCONDUCTIVITY', **kwargs)

def MaterialpropertyMoisturepenetrationdepthSettings(idf, **kwargs: MaterialpropertyMoisturepenetrationdepthSettings):
    return idf.newidfobject('MATERIALPROPERTY:MOISTUREPENETRATIONDEPTH:SETTINGS', **kwargs)

def MaterialpropertyPhasechange(idf, **kwargs: MaterialpropertyPhasechange):
    return idf.newidfobject('MATERIALPROPERTY:PHASECHANGE', **kwargs)

def MaterialpropertyPhasechangehysteresis(idf, **kwargs: MaterialpropertyPhasechangehysteresis):
    return idf.newidfobject('MATERIALPROPERTY:PHASECHANGEHYSTERESIS', **kwargs)

def MaterialpropertyVariableabsorptance(idf, **kwargs: MaterialpropertyVariableabsorptance):
    return idf.newidfobject('MATERIALPROPERTY:VARIABLEABSORPTANCE', **kwargs)

def MaterialpropertyVariablethermalconductivity(idf, **kwargs: MaterialpropertyVariablethermalconductivity):
    return idf.newidfobject('MATERIALPROPERTY:VARIABLETHERMALCONDUCTIVITY', **kwargs)

def MatrixTwodimension(idf, **kwargs: MatrixTwodimension):
    return idf.newidfobject('MATRIX:TWODIMENSION', **kwargs)

def MeterCustom(idf, **kwargs: MeterCustom):
    return idf.newidfobject('METER:CUSTOM', **kwargs)

def MeterCustomdecrement(idf, **kwargs: MeterCustomdecrement):
    return idf.newidfobject('METER:CUSTOMDECREMENT', **kwargs)

def Nodelist(idf, **kwargs: Nodelist):
    return idf.newidfobject('NODELIST', **kwargs)

def Otherequipment(idf, **kwargs: Otherequipment):
    return idf.newidfobject('OTHEREQUIPMENT', **kwargs)

def OutdoorairMixer(idf, **kwargs: OutdoorairMixer):
    return idf.newidfobject('OUTDOORAIR:MIXER', **kwargs)

def OutdoorairNode(idf, **kwargs: OutdoorairNode):
    return idf.newidfobject('OUTDOORAIR:NODE', **kwargs)

def OutdoorairNodelist(idf, **kwargs: OutdoorairNodelist):
    return idf.newidfobject('OUTDOORAIR:NODELIST', **kwargs)

def OutputConstructions(idf, **kwargs: OutputConstructions):
    return idf.newidfobject('OUTPUT:CONSTRUCTIONS', **kwargs)

def OutputDaylightfactors(idf, **kwargs: OutputDaylightfactors):
    return idf.newidfobject('OUTPUT:DAYLIGHTFACTORS', **kwargs)

def OutputDebuggingdata(idf, **kwargs: OutputDebuggingdata):
    return idf.newidfobject('OUTPUT:DEBUGGINGDATA', **kwargs)

def OutputDiagnostics(idf, **kwargs: OutputDiagnostics):
    return idf.newidfobject('OUTPUT:DIAGNOSTICS', **kwargs)

def OutputEnergymanagementsystem(idf, **kwargs: OutputEnergymanagementsystem):
    return idf.newidfobject('OUTPUT:ENERGYMANAGEMENTSYSTEM', **kwargs)

def OutputEnvironmentalimpactfactors(idf, **kwargs: OutputEnvironmentalimpactfactors):
    return idf.newidfobject('OUTPUT:ENVIRONMENTALIMPACTFACTORS', **kwargs)

def OutputIlluminancemap(idf, **kwargs: OutputIlluminancemap):
    return idf.newidfobject('OUTPUT:ILLUMINANCEMAP', **kwargs)

def OutputJson(idf, **kwargs: OutputJson):
    return idf.newidfobject('OUTPUT:JSON', **kwargs)

def OutputMeter(idf, **kwargs: OutputMeter):
    return idf.newidfobject('OUTPUT:METER', **kwargs)

def OutputMeterCumulative(idf, **kwargs: OutputMeterCumulative):
    return idf.newidfobject('OUTPUT:METER:CUMULATIVE', **kwargs)

def OutputMeterCumulativeMeterfileonly(idf, **kwargs: OutputMeterCumulativeMeterfileonly):
    return idf.newidfobject('OUTPUT:METER:CUMULATIVE:METERFILEONLY', **kwargs)

def OutputMeterMeterfileonly(idf, **kwargs: OutputMeterMeterfileonly):
    return idf.newidfobject('OUTPUT:METER:METERFILEONLY', **kwargs)

def OutputPreprocessormessage(idf, **kwargs: OutputPreprocessormessage):
    return idf.newidfobject('OUTPUT:PREPROCESSORMESSAGE', **kwargs)

def OutputSchedules(idf, **kwargs: OutputSchedules):
    return idf.newidfobject('OUTPUT:SCHEDULES', **kwargs)

def OutputSqlite(idf, **kwargs: OutputSqlite):
    return idf.newidfobject('OUTPUT:SQLITE', **kwargs)

def OutputSurfacesDrawing(idf, **kwargs: OutputSurfacesDrawing):
    return idf.newidfobject('OUTPUT:SURFACES:DRAWING', **kwargs)

def OutputSurfacesList(idf, **kwargs: OutputSurfacesList):
    return idf.newidfobject('OUTPUT:SURFACES:LIST', **kwargs)

def OutputTableAnnual(idf, **kwargs: OutputTableAnnual):
    return idf.newidfobject('OUTPUT:TABLE:ANNUAL', **kwargs)

def OutputTableMonthly(idf, **kwargs: OutputTableMonthly):
    return idf.newidfobject('OUTPUT:TABLE:MONTHLY', **kwargs)

def OutputTableReportperiod(idf, **kwargs: OutputTableReportperiod):
    return idf.newidfobject('OUTPUT:TABLE:REPORTPERIOD', **kwargs)

def OutputTableSummaryreports(idf, **kwargs: OutputTableSummaryreports):
    return idf.newidfobject('OUTPUT:TABLE:SUMMARYREPORTS', **kwargs)

def OutputTableTimebins(idf, **kwargs: OutputTableTimebins):
    return idf.newidfobject('OUTPUT:TABLE:TIMEBINS', **kwargs)

def OutputVariable(idf, **kwargs: OutputVariable):
    return idf.newidfobject('OUTPUT:VARIABLE', **kwargs)

def OutputVariabledictionary(idf, **kwargs: OutputVariabledictionary):
    return idf.newidfobject('OUTPUT:VARIABLEDICTIONARY', **kwargs)

def OutputcontrolFiles(idf, **kwargs: OutputcontrolFiles):
    return idf.newidfobject('OUTPUTCONTROL:FILES', **kwargs)

def OutputcontrolIlluminancemapStyle(idf, **kwargs: OutputcontrolIlluminancemapStyle):
    return idf.newidfobject('OUTPUTCONTROL:ILLUMINANCEMAP:STYLE', **kwargs)

def OutputcontrolReportingtolerances(idf, **kwargs: OutputcontrolReportingtolerances):
    return idf.newidfobject('OUTPUTCONTROL:REPORTINGTOLERANCES', **kwargs)

def OutputcontrolSizingStyle(idf, **kwargs: OutputcontrolSizingStyle):
    return idf.newidfobject('OUTPUTCONTROL:SIZING:STYLE', **kwargs)

def OutputcontrolSurfacecolorscheme(idf, **kwargs: OutputcontrolSurfacecolorscheme):
    return idf.newidfobject('OUTPUTCONTROL:SURFACECOLORSCHEME', **kwargs)

def OutputcontrolTableStyle(idf, **kwargs: OutputcontrolTableStyle):
    return idf.newidfobject('OUTPUTCONTROL:TABLE:STYLE', **kwargs)

def OutputcontrolTimestamp(idf, **kwargs: OutputcontrolTimestamp):
    return idf.newidfobject('OUTPUTCONTROL:TIMESTAMP', **kwargs)

def ParametricFilenamesuffix(idf, **kwargs: ParametricFilenamesuffix):
    return idf.newidfobject('PARAMETRIC:FILENAMESUFFIX', **kwargs)

def ParametricLogic(idf, **kwargs: ParametricLogic):
    return idf.newidfobject('PARAMETRIC:LOGIC', **kwargs)

def ParametricRuncontrol(idf, **kwargs: ParametricRuncontrol):
    return idf.newidfobject('PARAMETRIC:RUNCONTROL', **kwargs)

def ParametricSetvalueforrun(idf, **kwargs: ParametricSetvalueforrun):
    return idf.newidfobject('PARAMETRIC:SETVALUEFORRUN', **kwargs)

def People(idf, **kwargs: People):
    return idf.newidfobject('PEOPLE', **kwargs)

def Performanceprecisiontradeoffs(idf, **kwargs: Performanceprecisiontradeoffs):
    return idf.newidfobject('PERFORMANCEPRECISIONTRADEOFFS', **kwargs)

def PhotovoltaicperformanceEquivalentonediode(idf, **kwargs: PhotovoltaicperformanceEquivalentonediode):
    return idf.newidfobject('PHOTOVOLTAICPERFORMANCE:EQUIVALENTONE-DIODE', **kwargs)

def PhotovoltaicperformanceSandia(idf, **kwargs: PhotovoltaicperformanceSandia):
    return idf.newidfobject('PHOTOVOLTAICPERFORMANCE:SANDIA', **kwargs)

def PhotovoltaicperformanceSimple(idf, **kwargs: PhotovoltaicperformanceSimple):
    return idf.newidfobject('PHOTOVOLTAICPERFORMANCE:SIMPLE', **kwargs)

def PipeAdiabatic(idf, **kwargs: PipeAdiabatic):
    return idf.newidfobject('PIPE:ADIABATIC', **kwargs)

def PipeAdiabaticSteam(idf, **kwargs: PipeAdiabaticSteam):
    return idf.newidfobject('PIPE:ADIABATIC:STEAM', **kwargs)

def PipeIndoor(idf, **kwargs: PipeIndoor):
    return idf.newidfobject('PIPE:INDOOR', **kwargs)

def PipeOutdoor(idf, **kwargs: PipeOutdoor):
    return idf.newidfobject('PIPE:OUTDOOR', **kwargs)

def PipeUnderground(idf, **kwargs: PipeUnderground):
    return idf.newidfobject('PIPE:UNDERGROUND', **kwargs)

def PipingsystemUndergroundDomain(idf, **kwargs: PipingsystemUndergroundDomain):
    return idf.newidfobject('PIPINGSYSTEM:UNDERGROUND:DOMAIN', **kwargs)

def PipingsystemUndergroundPipecircuit(idf, **kwargs: PipingsystemUndergroundPipecircuit):
    return idf.newidfobject('PIPINGSYSTEM:UNDERGROUND:PIPECIRCUIT', **kwargs)

def PipingsystemUndergroundPipesegment(idf, **kwargs: PipingsystemUndergroundPipesegment):
    return idf.newidfobject('PIPINGSYSTEM:UNDERGROUND:PIPESEGMENT', **kwargs)

def PlantcomponentTemperaturesource(idf, **kwargs: PlantcomponentTemperaturesource):
    return idf.newidfobject('PLANTCOMPONENT:TEMPERATURESOURCE', **kwargs)

def PlantcomponentUserdefined(idf, **kwargs: PlantcomponentUserdefined):
    return idf.newidfobject('PLANTCOMPONENT:USERDEFINED', **kwargs)

def Plantequipmentlist(idf, **kwargs: Plantequipmentlist):
    return idf.newidfobject('PLANTEQUIPMENTLIST', **kwargs)

def PlantequipmentoperationChillerheaterchangeover(idf, **kwargs: PlantequipmentoperationChillerheaterchangeover):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:CHILLERHEATERCHANGEOVER', **kwargs)

def PlantequipmentoperationComponentsetpoint(idf, **kwargs: PlantequipmentoperationComponentsetpoint):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:COMPONENTSETPOINT', **kwargs)

def PlantequipmentoperationCoolingload(idf, **kwargs: PlantequipmentoperationCoolingload):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:COOLINGLOAD', **kwargs)

def PlantequipmentoperationHeatingload(idf, **kwargs: PlantequipmentoperationHeatingload):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:HEATINGLOAD', **kwargs)

def PlantequipmentoperationOutdoordewpoint(idf, **kwargs: PlantequipmentoperationOutdoordewpoint):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORDEWPOINT', **kwargs)

def PlantequipmentoperationOutdoordewpointdifference(idf, **kwargs: PlantequipmentoperationOutdoordewpointdifference):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORDEWPOINTDIFFERENCE', **kwargs)

def PlantequipmentoperationOutdoordrybulb(idf, **kwargs: PlantequipmentoperationOutdoordrybulb):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORDRYBULB', **kwargs)

def PlantequipmentoperationOutdoordrybulbdifference(idf, **kwargs: PlantequipmentoperationOutdoordrybulbdifference):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORDRYBULBDIFFERENCE', **kwargs)

def PlantequipmentoperationOutdoorrelativehumidity(idf, **kwargs: PlantequipmentoperationOutdoorrelativehumidity):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORRELATIVEHUMIDITY', **kwargs)

def PlantequipmentoperationOutdoorwetbulb(idf, **kwargs: PlantequipmentoperationOutdoorwetbulb):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORWETBULB', **kwargs)

def PlantequipmentoperationOutdoorwetbulbdifference(idf, **kwargs: PlantequipmentoperationOutdoorwetbulbdifference):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:OUTDOORWETBULBDIFFERENCE', **kwargs)

def PlantequipmentoperationThermalenergystorage(idf, **kwargs: PlantequipmentoperationThermalenergystorage):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:THERMALENERGYSTORAGE', **kwargs)

def PlantequipmentoperationUncontrolled(idf, **kwargs: PlantequipmentoperationUncontrolled):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:UNCONTROLLED', **kwargs)

def PlantequipmentoperationUserdefined(idf, **kwargs: PlantequipmentoperationUserdefined):
    return idf.newidfobject('PLANTEQUIPMENTOPERATION:USERDEFINED', **kwargs)

def Plantequipmentoperationschemes(idf, **kwargs: Plantequipmentoperationschemes):
    return idf.newidfobject('PLANTEQUIPMENTOPERATIONSCHEMES', **kwargs)

def Plantloop(idf, **kwargs: Plantloop):
    return idf.newidfobject('PLANTLOOP', **kwargs)

def PumpConstantspeed(idf, **kwargs: PumpConstantspeed):
    return idf.newidfobject('PUMP:CONSTANTSPEED', **kwargs)

def PumpVariablespeed(idf, **kwargs: PumpVariablespeed):
    return idf.newidfobject('PUMP:VARIABLESPEED', **kwargs)

def PumpVariablespeedCondensate(idf, **kwargs: PumpVariablespeedCondensate):
    return idf.newidfobject('PUMP:VARIABLESPEED:CONDENSATE', **kwargs)

def PythonpluginInstance(idf, **kwargs: PythonpluginInstance):
    return idf.newidfobject('PYTHONPLUGIN:INSTANCE', **kwargs)

def PythonpluginOutputvariable(idf, **kwargs: PythonpluginOutputvariable):
    return idf.newidfobject('PYTHONPLUGIN:OUTPUTVARIABLE', **kwargs)

def PythonpluginSearchpaths(idf, **kwargs: PythonpluginSearchpaths):
    return idf.newidfobject('PYTHONPLUGIN:SEARCHPATHS', **kwargs)

def PythonpluginTrendvariable(idf, **kwargs: PythonpluginTrendvariable):
    return idf.newidfobject('PYTHONPLUGIN:TRENDVARIABLE', **kwargs)

def PythonpluginVariables(idf, **kwargs: PythonpluginVariables):
    return idf.newidfobject('PYTHONPLUGIN:VARIABLES', **kwargs)

def RefrigerationAirchiller(idf, **kwargs: RefrigerationAirchiller):
    return idf.newidfobject('REFRIGERATION:AIRCHILLER', **kwargs)

def RefrigerationCase(idf, **kwargs: RefrigerationCase):
    return idf.newidfobject('REFRIGERATION:CASE', **kwargs)

def RefrigerationCaseandwalkinlist(idf, **kwargs: RefrigerationCaseandwalkinlist):
    return idf.newidfobject('REFRIGERATION:CASEANDWALKINLIST', **kwargs)

def RefrigerationCompressor(idf, **kwargs: RefrigerationCompressor):
    return idf.newidfobject('REFRIGERATION:COMPRESSOR', **kwargs)

def RefrigerationCompressorlist(idf, **kwargs: RefrigerationCompressorlist):
    return idf.newidfobject('REFRIGERATION:COMPRESSORLIST', **kwargs)

def RefrigerationCompressorrack(idf, **kwargs: RefrigerationCompressorrack):
    return idf.newidfobject('REFRIGERATION:COMPRESSORRACK', **kwargs)

def RefrigerationCondenserAircooled(idf, **kwargs: RefrigerationCondenserAircooled):
    return idf.newidfobject('REFRIGERATION:CONDENSER:AIRCOOLED', **kwargs)

def RefrigerationCondenserCascade(idf, **kwargs: RefrigerationCondenserCascade):
    return idf.newidfobject('REFRIGERATION:CONDENSER:CASCADE', **kwargs)

def RefrigerationCondenserEvaporativecooled(idf, **kwargs: RefrigerationCondenserEvaporativecooled):
    return idf.newidfobject('REFRIGERATION:CONDENSER:EVAPORATIVECOOLED', **kwargs)

def RefrigerationCondenserWatercooled(idf, **kwargs: RefrigerationCondenserWatercooled):
    return idf.newidfobject('REFRIGERATION:CONDENSER:WATERCOOLED', **kwargs)

def RefrigerationGascoolerAircooled(idf, **kwargs: RefrigerationGascoolerAircooled):
    return idf.newidfobject('REFRIGERATION:GASCOOLER:AIRCOOLED', **kwargs)

def RefrigerationSecondarysystem(idf, **kwargs: RefrigerationSecondarysystem):
    return idf.newidfobject('REFRIGERATION:SECONDARYSYSTEM', **kwargs)

def RefrigerationSubcooler(idf, **kwargs: RefrigerationSubcooler):
    return idf.newidfobject('REFRIGERATION:SUBCOOLER', **kwargs)

def RefrigerationSystem(idf, **kwargs: RefrigerationSystem):
    return idf.newidfobject('REFRIGERATION:SYSTEM', **kwargs)

def RefrigerationTranscriticalsystem(idf, **kwargs: RefrigerationTranscriticalsystem):
    return idf.newidfobject('REFRIGERATION:TRANSCRITICALSYSTEM', **kwargs)

def RefrigerationTransferloadlist(idf, **kwargs: RefrigerationTransferloadlist):
    return idf.newidfobject('REFRIGERATION:TRANSFERLOADLIST', **kwargs)

def RefrigerationWalkin(idf, **kwargs: RefrigerationWalkin):
    return idf.newidfobject('REFRIGERATION:WALKIN', **kwargs)

def Roof(idf, **kwargs: Roof):
    return idf.newidfobject('ROOF', **kwargs)

def RoofceilingDetailed(idf, **kwargs: RoofceilingDetailed):
    return idf.newidfobject('ROOFCEILING:DETAILED', **kwargs)

def Roofirrigation(idf, **kwargs: Roofirrigation):
    return idf.newidfobject('ROOFIRRIGATION', **kwargs)

def RoomairNode(idf, **kwargs: RoomairNode):
    return idf.newidfobject('ROOMAIR:NODE', **kwargs)

def RoomairNodeAirflownetwork(idf, **kwargs: RoomairNodeAirflownetwork):
    return idf.newidfobject('ROOMAIR:NODE:AIRFLOWNETWORK', **kwargs)

def RoomairNodeAirflownetworkAdjacentsurfacelist(idf, **kwargs: RoomairNodeAirflownetworkAdjacentsurfacelist):
    return idf.newidfobject('ROOMAIR:NODE:AIRFLOWNETWORK:ADJACENTSURFACELIST', **kwargs)

def RoomairNodeAirflownetworkHvacequipment(idf, **kwargs: RoomairNodeAirflownetworkHvacequipment):
    return idf.newidfobject('ROOMAIR:NODE:AIRFLOWNETWORK:HVACEQUIPMENT', **kwargs)

def RoomairNodeAirflownetworkInternalgains(idf, **kwargs: RoomairNodeAirflownetworkInternalgains):
    return idf.newidfobject('ROOMAIR:NODE:AIRFLOWNETWORK:INTERNALGAINS', **kwargs)

def RoomairTemperaturepatternConstantgradient(idf, **kwargs: RoomairTemperaturepatternConstantgradient):
    return idf.newidfobject('ROOMAIR:TEMPERATUREPATTERN:CONSTANTGRADIENT', **kwargs)

def RoomairTemperaturepatternNondimensionalheight(idf, **kwargs: RoomairTemperaturepatternNondimensionalheight):
    return idf.newidfobject('ROOMAIR:TEMPERATUREPATTERN:NONDIMENSIONALHEIGHT', **kwargs)

def RoomairTemperaturepatternSurfacemapping(idf, **kwargs: RoomairTemperaturepatternSurfacemapping):
    return idf.newidfobject('ROOMAIR:TEMPERATUREPATTERN:SURFACEMAPPING', **kwargs)

def RoomairTemperaturepatternTwogradient(idf, **kwargs: RoomairTemperaturepatternTwogradient):
    return idf.newidfobject('ROOMAIR:TEMPERATUREPATTERN:TWOGRADIENT', **kwargs)

def RoomairTemperaturepatternUserdefined(idf, **kwargs: RoomairTemperaturepatternUserdefined):
    return idf.newidfobject('ROOMAIR:TEMPERATUREPATTERN:USERDEFINED', **kwargs)

def Roomairmodeltype(idf, **kwargs: Roomairmodeltype):
    return idf.newidfobject('ROOMAIRMODELTYPE', **kwargs)

def RoomairsettingsAirflownetwork(idf, **kwargs: RoomairsettingsAirflownetwork):
    return idf.newidfobject('ROOMAIRSETTINGS:AIRFLOWNETWORK', **kwargs)

def RoomairsettingsCrossventilation(idf, **kwargs: RoomairsettingsCrossventilation):
    return idf.newidfobject('ROOMAIRSETTINGS:CROSSVENTILATION', **kwargs)

def RoomairsettingsOnenodedisplacementventilation(idf, **kwargs: RoomairsettingsOnenodedisplacementventilation):
    return idf.newidfobject('ROOMAIRSETTINGS:ONENODEDISPLACEMENTVENTILATION', **kwargs)

def RoomairsettingsThreenodedisplacementventilation(idf, **kwargs: RoomairsettingsThreenodedisplacementventilation):
    return idf.newidfobject('ROOMAIRSETTINGS:THREENODEDISPLACEMENTVENTILATION', **kwargs)

def RoomairsettingsUnderfloorairdistributionexterior(idf, **kwargs: RoomairsettingsUnderfloorairdistributionexterior):
    return idf.newidfobject('ROOMAIRSETTINGS:UNDERFLOORAIRDISTRIBUTIONEXTERIOR', **kwargs)

def RoomairsettingsUnderfloorairdistributioninterior(idf, **kwargs: RoomairsettingsUnderfloorairdistributioninterior):
    return idf.newidfobject('ROOMAIRSETTINGS:UNDERFLOORAIRDISTRIBUTIONINTERIOR', **kwargs)

def Runperiod(idf, **kwargs: Runperiod):
    return idf.newidfobject('RUNPERIOD', **kwargs)

def RunperiodcontrolDaylightsavingtime(idf, **kwargs: RunperiodcontrolDaylightsavingtime):
    return idf.newidfobject('RUNPERIODCONTROL:DAYLIGHTSAVINGTIME', **kwargs)

def RunperiodcontrolSpecialdays(idf, **kwargs: RunperiodcontrolSpecialdays):
    return idf.newidfobject('RUNPERIODCONTROL:SPECIALDAYS', **kwargs)

def ScheduleCompact(idf, **kwargs: ScheduleCompact):
    return idf.newidfobject('SCHEDULE:COMPACT', **kwargs)

def ScheduleConstant(idf, **kwargs: ScheduleConstant):
    return idf.newidfobject('SCHEDULE:CONSTANT', **kwargs)

def ScheduleDayHourly(idf, **kwargs: ScheduleDayHourly):
    return idf.newidfobject('SCHEDULE:DAY:HOURLY', **kwargs)

def ScheduleDayInterval(idf, **kwargs: ScheduleDayInterval):
    return idf.newidfobject('SCHEDULE:DAY:INTERVAL', **kwargs)

def ScheduleDayList(idf, **kwargs: ScheduleDayList):
    return idf.newidfobject('SCHEDULE:DAY:LIST', **kwargs)

def ScheduleFile(idf, **kwargs: ScheduleFile):
    return idf.newidfobject('SCHEDULE:FILE', **kwargs)

def ScheduleFileShading(idf, **kwargs: ScheduleFileShading):
    return idf.newidfobject('SCHEDULE:FILE:SHADING', **kwargs)

def ScheduleWeekCompact(idf, **kwargs: ScheduleWeekCompact):
    return idf.newidfobject('SCHEDULE:WEEK:COMPACT', **kwargs)

def ScheduleWeekDaily(idf, **kwargs: ScheduleWeekDaily):
    return idf.newidfobject('SCHEDULE:WEEK:DAILY', **kwargs)

def ScheduleYear(idf, **kwargs: ScheduleYear):
    return idf.newidfobject('SCHEDULE:YEAR', **kwargs)

def Scheduletypelimits(idf, **kwargs: Scheduletypelimits):
    return idf.newidfobject('SCHEDULETYPELIMITS', **kwargs)

def SetpointmanagerColdest(idf, **kwargs: SetpointmanagerColdest):
    return idf.newidfobject('SETPOINTMANAGER:COLDEST', **kwargs)

def SetpointmanagerCondenserenteringreset(idf, **kwargs: SetpointmanagerCondenserenteringreset):
    return idf.newidfobject('SETPOINTMANAGER:CONDENSERENTERINGRESET', **kwargs)

def SetpointmanagerCondenserenteringresetIdeal(idf, **kwargs: SetpointmanagerCondenserenteringresetIdeal):
    return idf.newidfobject('SETPOINTMANAGER:CONDENSERENTERINGRESET:IDEAL', **kwargs)

def SetpointmanagerFollowgroundtemperature(idf, **kwargs: SetpointmanagerFollowgroundtemperature):
    return idf.newidfobject('SETPOINTMANAGER:FOLLOWGROUNDTEMPERATURE', **kwargs)

def SetpointmanagerFollowoutdoorairtemperature(idf, **kwargs: SetpointmanagerFollowoutdoorairtemperature):
    return idf.newidfobject('SETPOINTMANAGER:FOLLOWOUTDOORAIRTEMPERATURE', **kwargs)

def SetpointmanagerFollowsystemnodetemperature(idf, **kwargs: SetpointmanagerFollowsystemnodetemperature):
    return idf.newidfobject('SETPOINTMANAGER:FOLLOWSYSTEMNODETEMPERATURE', **kwargs)

def SetpointmanagerMixedair(idf, **kwargs: SetpointmanagerMixedair):
    return idf.newidfobject('SETPOINTMANAGER:MIXEDAIR', **kwargs)

def SetpointmanagerMultizoneCoolingAverage(idf, **kwargs: SetpointmanagerMultizoneCoolingAverage):
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:COOLING:AVERAGE', **kwargs)

def SetpointmanagerMultizoneHeatingAverage(idf, **kwargs: SetpointmanagerMultizoneHeatingAverage):
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:HEATING:AVERAGE', **kwargs)

def SetpointmanagerMultizoneHumidityMaximum(idf, **kwargs: SetpointmanagerMultizoneHumidityMaximum):
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:HUMIDITY:MAXIMUM', **kwargs)

def SetpointmanagerMultizoneHumidityMinimum(idf, **kwargs: SetpointmanagerMultizoneHumidityMinimum):
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:HUMIDITY:MINIMUM', **kwargs)

def SetpointmanagerMultizoneMaximumhumidityAverage(idf, **kwargs: SetpointmanagerMultizoneMaximumhumidityAverage):
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:MAXIMUMHUMIDITY:AVERAGE', **kwargs)

def SetpointmanagerMultizoneMinimumhumidityAverage(idf, **kwargs: SetpointmanagerMultizoneMinimumhumidityAverage):
    return idf.newidfobject('SETPOINTMANAGER:MULTIZONE:MINIMUMHUMIDITY:AVERAGE', **kwargs)

def SetpointmanagerOutdoorairpretreat(idf, **kwargs: SetpointmanagerOutdoorairpretreat):
    return idf.newidfobject('SETPOINTMANAGER:OUTDOORAIRPRETREAT', **kwargs)

def SetpointmanagerOutdoorairreset(idf, **kwargs: SetpointmanagerOutdoorairreset):
    return idf.newidfobject('SETPOINTMANAGER:OUTDOORAIRRESET', **kwargs)

def SetpointmanagerReturnairbypassflow(idf, **kwargs: SetpointmanagerReturnairbypassflow):
    return idf.newidfobject('SETPOINTMANAGER:RETURNAIRBYPASSFLOW', **kwargs)

def SetpointmanagerReturntemperatureChilledwater(idf, **kwargs: SetpointmanagerReturntemperatureChilledwater):
    return idf.newidfobject('SETPOINTMANAGER:RETURNTEMPERATURE:CHILLEDWATER', **kwargs)

def SetpointmanagerReturntemperatureHotwater(idf, **kwargs: SetpointmanagerReturntemperatureHotwater):
    return idf.newidfobject('SETPOINTMANAGER:RETURNTEMPERATURE:HOTWATER', **kwargs)

def SetpointmanagerScheduled(idf, **kwargs: SetpointmanagerScheduled):
    return idf.newidfobject('SETPOINTMANAGER:SCHEDULED', **kwargs)

def SetpointmanagerScheduledDualsetpoint(idf, **kwargs: SetpointmanagerScheduledDualsetpoint):
    return idf.newidfobject('SETPOINTMANAGER:SCHEDULED:DUALSETPOINT', **kwargs)

def SetpointmanagerSinglezoneCooling(idf, **kwargs: SetpointmanagerSinglezoneCooling):
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:COOLING', **kwargs)

def SetpointmanagerSinglezoneHeating(idf, **kwargs: SetpointmanagerSinglezoneHeating):
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:HEATING', **kwargs)

def SetpointmanagerSinglezoneHumidityMaximum(idf, **kwargs: SetpointmanagerSinglezoneHumidityMaximum):
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:HUMIDITY:MAXIMUM', **kwargs)

def SetpointmanagerSinglezoneHumidityMinimum(idf, **kwargs: SetpointmanagerSinglezoneHumidityMinimum):
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:HUMIDITY:MINIMUM', **kwargs)

def SetpointmanagerSinglezoneOnestagecooling(idf, **kwargs: SetpointmanagerSinglezoneOnestagecooling):
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:ONESTAGECOOLING', **kwargs)

def SetpointmanagerSinglezoneOnestageheating(idf, **kwargs: SetpointmanagerSinglezoneOnestageheating):
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:ONESTAGEHEATING', **kwargs)

def SetpointmanagerSinglezoneReheat(idf, **kwargs: SetpointmanagerSinglezoneReheat):
    return idf.newidfobject('SETPOINTMANAGER:SINGLEZONE:REHEAT', **kwargs)

def SetpointmanagerSystemnoderesetHumidity(idf, **kwargs: SetpointmanagerSystemnoderesetHumidity):
    return idf.newidfobject('SETPOINTMANAGER:SYSTEMNODERESET:HUMIDITY', **kwargs)

def SetpointmanagerSystemnoderesetTemperature(idf, **kwargs: SetpointmanagerSystemnoderesetTemperature):
    return idf.newidfobject('SETPOINTMANAGER:SYSTEMNODERESET:TEMPERATURE', **kwargs)

def SetpointmanagerWarmest(idf, **kwargs: SetpointmanagerWarmest):
    return idf.newidfobject('SETPOINTMANAGER:WARMEST', **kwargs)

def SetpointmanagerWarmesttemperatureflow(idf, **kwargs: SetpointmanagerWarmesttemperatureflow):
    return idf.newidfobject('SETPOINTMANAGER:WARMESTTEMPERATUREFLOW', **kwargs)

def ShadingBuilding(idf, **kwargs: ShadingBuilding):
    return idf.newidfobject('SHADING:BUILDING', **kwargs)

def ShadingBuildingDetailed(idf, **kwargs: ShadingBuildingDetailed):
    return idf.newidfobject('SHADING:BUILDING:DETAILED', **kwargs)

def ShadingFin(idf, **kwargs: ShadingFin):
    return idf.newidfobject('SHADING:FIN', **kwargs)

def ShadingFinProjection(idf, **kwargs: ShadingFinProjection):
    return idf.newidfobject('SHADING:FIN:PROJECTION', **kwargs)

def ShadingOverhang(idf, **kwargs: ShadingOverhang):
    return idf.newidfobject('SHADING:OVERHANG', **kwargs)

def ShadingOverhangProjection(idf, **kwargs: ShadingOverhangProjection):
    return idf.newidfobject('SHADING:OVERHANG:PROJECTION', **kwargs)

def ShadingSite(idf, **kwargs: ShadingSite):
    return idf.newidfobject('SHADING:SITE', **kwargs)

def ShadingSiteDetailed(idf, **kwargs: ShadingSiteDetailed):
    return idf.newidfobject('SHADING:SITE:DETAILED', **kwargs)

def ShadingZoneDetailed(idf, **kwargs: ShadingZoneDetailed):
    return idf.newidfobject('SHADING:ZONE:DETAILED', **kwargs)

def ShadingpropertyReflectance(idf, **kwargs: ShadingpropertyReflectance):
    return idf.newidfobject('SHADINGPROPERTY:REFLECTANCE', **kwargs)

def Shadowcalculation(idf, **kwargs: Shadowcalculation):
    return idf.newidfobject('SHADOWCALCULATION', **kwargs)

def Simulationcontrol(idf, **kwargs: Simulationcontrol):
    return idf.newidfobject('SIMULATIONCONTROL', **kwargs)

def SiteGrounddomainBasement(idf, **kwargs: SiteGrounddomainBasement):
    return idf.newidfobject('SITE:GROUNDDOMAIN:BASEMENT', **kwargs)

def SiteGrounddomainSlab(idf, **kwargs: SiteGrounddomainSlab):
    return idf.newidfobject('SITE:GROUNDDOMAIN:SLAB', **kwargs)

def SiteGroundreflectance(idf, **kwargs: SiteGroundreflectance):
    return idf.newidfobject('SITE:GROUNDREFLECTANCE', **kwargs)

def SiteGroundreflectanceSnowmodifier(idf, **kwargs: SiteGroundreflectanceSnowmodifier):
    return idf.newidfobject('SITE:GROUNDREFLECTANCE:SNOWMODIFIER', **kwargs)

def SiteGroundtemperatureBuildingsurface(idf, **kwargs: SiteGroundtemperatureBuildingsurface):
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:BUILDINGSURFACE', **kwargs)

def SiteGroundtemperatureDeep(idf, **kwargs: SiteGroundtemperatureDeep):
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:DEEP', **kwargs)

def SiteGroundtemperatureFcfactormethod(idf, **kwargs: SiteGroundtemperatureFcfactormethod):
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:FCFACTORMETHOD', **kwargs)

def SiteGroundtemperatureShallow(idf, **kwargs: SiteGroundtemperatureShallow):
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:SHALLOW', **kwargs)

def SiteGroundtemperatureUndisturbedFinitedifference(idf, **kwargs: SiteGroundtemperatureUndisturbedFinitedifference):
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:UNDISTURBED:FINITEDIFFERENCE', **kwargs)

def SiteGroundtemperatureUndisturbedKusudaachenbach(idf, **kwargs: SiteGroundtemperatureUndisturbedKusudaachenbach):
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:UNDISTURBED:KUSUDAACHENBACH', **kwargs)

def SiteGroundtemperatureUndisturbedXing(idf, **kwargs: SiteGroundtemperatureUndisturbedXing):
    return idf.newidfobject('SITE:GROUNDTEMPERATURE:UNDISTURBED:XING', **kwargs)

def SiteHeightvariation(idf, **kwargs: SiteHeightvariation):
    return idf.newidfobject('SITE:HEIGHTVARIATION', **kwargs)

def SiteLocation(idf, **kwargs: SiteLocation):
    return idf.newidfobject('SITE:LOCATION', **kwargs)

def SitePrecipitation(idf, **kwargs: SitePrecipitation):
    return idf.newidfobject('SITE:PRECIPITATION', **kwargs)

def SiteSolarandvisiblespectrum(idf, **kwargs: SiteSolarandvisiblespectrum):
    return idf.newidfobject('SITE:SOLARANDVISIBLESPECTRUM', **kwargs)

def SiteSpectrumdata(idf, **kwargs: SiteSpectrumdata):
    return idf.newidfobject('SITE:SPECTRUMDATA', **kwargs)

def SiteVariablelocation(idf, **kwargs: SiteVariablelocation):
    return idf.newidfobject('SITE:VARIABLELOCATION', **kwargs)

def SiteWatermainstemperature(idf, **kwargs: SiteWatermainstemperature):
    return idf.newidfobject('SITE:WATERMAINSTEMPERATURE', **kwargs)

def SiteWeatherstation(idf, **kwargs: SiteWeatherstation):
    return idf.newidfobject('SITE:WEATHERSTATION', **kwargs)

def SizingParameters(idf, **kwargs: SizingParameters):
    return idf.newidfobject('SIZING:PARAMETERS', **kwargs)

def SizingPlant(idf, **kwargs: SizingPlant):
    return idf.newidfobject('SIZING:PLANT', **kwargs)

def SizingSystem(idf, **kwargs: SizingSystem):
    return idf.newidfobject('SIZING:SYSTEM', **kwargs)

def SizingZone(idf, **kwargs: SizingZone):
    return idf.newidfobject('SIZING:ZONE', **kwargs)

def SizingperiodDesignday(idf, **kwargs: SizingperiodDesignday):
    return idf.newidfobject('SIZINGPERIOD:DESIGNDAY', **kwargs)

def SizingperiodWeatherfileconditiontype(idf, **kwargs: SizingperiodWeatherfileconditiontype):
    return idf.newidfobject('SIZINGPERIOD:WEATHERFILECONDITIONTYPE', **kwargs)

def SizingperiodWeatherfiledays(idf, **kwargs: SizingperiodWeatherfiledays):
    return idf.newidfobject('SIZINGPERIOD:WEATHERFILEDAYS', **kwargs)

def SolarcollectorFlatplatePhotovoltaicthermal(idf, **kwargs: SolarcollectorFlatplatePhotovoltaicthermal):
    return idf.newidfobject('SOLARCOLLECTOR:FLATPLATE:PHOTOVOLTAICTHERMAL', **kwargs)

def SolarcollectorFlatplateWater(idf, **kwargs: SolarcollectorFlatplateWater):
    return idf.newidfobject('SOLARCOLLECTOR:FLATPLATE:WATER', **kwargs)

def SolarcollectorIntegralcollectorstorage(idf, **kwargs: SolarcollectorIntegralcollectorstorage):
    return idf.newidfobject('SOLARCOLLECTOR:INTEGRALCOLLECTORSTORAGE', **kwargs)

def SolarcollectorUnglazedtranspired(idf, **kwargs: SolarcollectorUnglazedtranspired):
    return idf.newidfobject('SOLARCOLLECTOR:UNGLAZEDTRANSPIRED', **kwargs)

def SolarcollectorUnglazedtranspiredMultisystem(idf, **kwargs: SolarcollectorUnglazedtranspiredMultisystem):
    return idf.newidfobject('SOLARCOLLECTOR:UNGLAZEDTRANSPIRED:MULTISYSTEM', **kwargs)

def SolarcollectorperformanceFlatplate(idf, **kwargs: SolarcollectorperformanceFlatplate):
    return idf.newidfobject('SOLARCOLLECTORPERFORMANCE:FLATPLATE', **kwargs)

def SolarcollectorperformanceIntegralcollectorstorage(idf, **kwargs: SolarcollectorperformanceIntegralcollectorstorage):
    return idf.newidfobject('SOLARCOLLECTORPERFORMANCE:INTEGRALCOLLECTORSTORAGE', **kwargs)

def SolarcollectorperformancePhotovoltaicthermalBipvt(idf, **kwargs: SolarcollectorperformancePhotovoltaicthermalBipvt):
    return idf.newidfobject('SOLARCOLLECTORPERFORMANCE:PHOTOVOLTAICTHERMAL:BIPVT', **kwargs)

def SolarcollectorperformancePhotovoltaicthermalSimple(idf, **kwargs: SolarcollectorperformancePhotovoltaicthermalSimple):
    return idf.newidfobject('SOLARCOLLECTORPERFORMANCE:PHOTOVOLTAICTHERMAL:SIMPLE', **kwargs)

def Space(idf, **kwargs: Space):
    return idf.newidfobject('SPACE', **kwargs)

def SpacehvacEquipmentconnections(idf, **kwargs: SpacehvacEquipmentconnections):
    return idf.newidfobject('SPACEHVAC:EQUIPMENTCONNECTIONS', **kwargs)

def SpacehvacZoneequipmentmixer(idf, **kwargs: SpacehvacZoneequipmentmixer):
    return idf.newidfobject('SPACEHVAC:ZONEEQUIPMENTMIXER', **kwargs)

def SpacehvacZoneequipmentsplitter(idf, **kwargs: SpacehvacZoneequipmentsplitter):
    return idf.newidfobject('SPACEHVAC:ZONEEQUIPMENTSPLITTER', **kwargs)

def Spacelist(idf, **kwargs: Spacelist):
    return idf.newidfobject('SPACELIST', **kwargs)

def Steamequipment(idf, **kwargs: Steamequipment):
    return idf.newidfobject('STEAMEQUIPMENT', **kwargs)

def SurfacecontaminantsourceandsinkGenericBoundarylayerdiffusion(idf, **kwargs: SurfacecontaminantsourceandsinkGenericBoundarylayerdiffusion):
    return idf.newidfobject('SURFACECONTAMINANTSOURCEANDSINK:GENERIC:BOUNDARYLAYERDIFFUSION', **kwargs)

def SurfacecontaminantsourceandsinkGenericDepositionvelocitysink(idf, **kwargs: SurfacecontaminantsourceandsinkGenericDepositionvelocitysink):
    return idf.newidfobject('SURFACECONTAMINANTSOURCEANDSINK:GENERIC:DEPOSITIONVELOCITYSINK', **kwargs)

def SurfacecontaminantsourceandsinkGenericPressuredriven(idf, **kwargs: SurfacecontaminantsourceandsinkGenericPressuredriven):
    return idf.newidfobject('SURFACECONTAMINANTSOURCEANDSINK:GENERIC:PRESSUREDRIVEN', **kwargs)

def SurfacecontrolMovableinsulation(idf, **kwargs: SurfacecontrolMovableinsulation):
    return idf.newidfobject('SURFACECONTROL:MOVABLEINSULATION', **kwargs)

def SurfaceconvectionalgorithmInside(idf, **kwargs: SurfaceconvectionalgorithmInside):
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:INSIDE', **kwargs)

def SurfaceconvectionalgorithmInsideAdaptivemodelselections(idf, **kwargs: SurfaceconvectionalgorithmInsideAdaptivemodelselections):
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:INSIDE:ADAPTIVEMODELSELECTIONS', **kwargs)

def SurfaceconvectionalgorithmInsideUsercurve(idf, **kwargs: SurfaceconvectionalgorithmInsideUsercurve):
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:INSIDE:USERCURVE', **kwargs)

def SurfaceconvectionalgorithmOutside(idf, **kwargs: SurfaceconvectionalgorithmOutside):
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:OUTSIDE', **kwargs)

def SurfaceconvectionalgorithmOutsideAdaptivemodelselections(idf, **kwargs: SurfaceconvectionalgorithmOutsideAdaptivemodelselections):
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:OUTSIDE:ADAPTIVEMODELSELECTIONS', **kwargs)

def SurfaceconvectionalgorithmOutsideUsercurve(idf, **kwargs: SurfaceconvectionalgorithmOutsideUsercurve):
    return idf.newidfobject('SURFACECONVECTIONALGORITHM:OUTSIDE:USERCURVE', **kwargs)

def SurfacepropertiesVaporcoefficients(idf, **kwargs: SurfacepropertiesVaporcoefficients):
    return idf.newidfobject('SURFACEPROPERTIES:VAPORCOEFFICIENTS', **kwargs)

def SurfacepropertyConvectioncoefficients(idf, **kwargs: SurfacepropertyConvectioncoefficients):
    return idf.newidfobject('SURFACEPROPERTY:CONVECTIONCOEFFICIENTS', **kwargs)

def SurfacepropertyConvectioncoefficientsMultiplesurface(idf, **kwargs: SurfacepropertyConvectioncoefficientsMultiplesurface):
    return idf.newidfobject('SURFACEPROPERTY:CONVECTIONCOEFFICIENTS:MULTIPLESURFACE', **kwargs)

def SurfacepropertyExposedfoundationperimeter(idf, **kwargs: SurfacepropertyExposedfoundationperimeter):
    return idf.newidfobject('SURFACEPROPERTY:EXPOSEDFOUNDATIONPERIMETER', **kwargs)

def SurfacepropertyExteriornaturalventedcavity(idf, **kwargs: SurfacepropertyExteriornaturalventedcavity):
    return idf.newidfobject('SURFACEPROPERTY:EXTERIORNATURALVENTEDCAVITY', **kwargs)

def SurfacepropertyGroundsurfaces(idf, **kwargs: SurfacepropertyGroundsurfaces):
    return idf.newidfobject('SURFACEPROPERTY:GROUNDSURFACES', **kwargs)

def SurfacepropertyHeatbalancesourceterm(idf, **kwargs: SurfacepropertyHeatbalancesourceterm):
    return idf.newidfobject('SURFACEPROPERTY:HEATBALANCESOURCETERM', **kwargs)

def SurfacepropertyHeattransferalgorithm(idf, **kwargs: SurfacepropertyHeattransferalgorithm):
    return idf.newidfobject('SURFACEPROPERTY:HEATTRANSFERALGORITHM', **kwargs)

def SurfacepropertyHeattransferalgorithmConstruction(idf, **kwargs: SurfacepropertyHeattransferalgorithmConstruction):
    return idf.newidfobject('SURFACEPROPERTY:HEATTRANSFERALGORITHM:CONSTRUCTION', **kwargs)

def SurfacepropertyHeattransferalgorithmMultiplesurface(idf, **kwargs: SurfacepropertyHeattransferalgorithmMultiplesurface):
    return idf.newidfobject('SURFACEPROPERTY:HEATTRANSFERALGORITHM:MULTIPLESURFACE', **kwargs)

def SurfacepropertyHeattransferalgorithmSurfacelist(idf, **kwargs: SurfacepropertyHeattransferalgorithmSurfacelist):
    return idf.newidfobject('SURFACEPROPERTY:HEATTRANSFERALGORITHM:SURFACELIST', **kwargs)

def SurfacepropertyIncidentsolarmultiplier(idf, **kwargs: SurfacepropertyIncidentsolarmultiplier):
    return idf.newidfobject('SURFACEPROPERTY:INCIDENTSOLARMULTIPLIER', **kwargs)

def SurfacepropertyLocalenvironment(idf, **kwargs: SurfacepropertyLocalenvironment):
    return idf.newidfobject('SURFACEPROPERTY:LOCALENVIRONMENT', **kwargs)

def SurfacepropertyOthersidecoefficients(idf, **kwargs: SurfacepropertyOthersidecoefficients):
    return idf.newidfobject('SURFACEPROPERTY:OTHERSIDECOEFFICIENTS', **kwargs)

def SurfacepropertyOthersideconditionsmodel(idf, **kwargs: SurfacepropertyOthersideconditionsmodel):
    return idf.newidfobject('SURFACEPROPERTY:OTHERSIDECONDITIONSMODEL', **kwargs)

def SurfacepropertySolarincidentinside(idf, **kwargs: SurfacepropertySolarincidentinside):
    return idf.newidfobject('SURFACEPROPERTY:SOLARINCIDENTINSIDE', **kwargs)

def SurfacepropertySurroundingsurfaces(idf, **kwargs: SurfacepropertySurroundingsurfaces):
    return idf.newidfobject('SURFACEPROPERTY:SURROUNDINGSURFACES', **kwargs)

def SurfacepropertyUnderwater(idf, **kwargs: SurfacepropertyUnderwater):
    return idf.newidfobject('SURFACEPROPERTY:UNDERWATER', **kwargs)

def SwimmingpoolIndoor(idf, **kwargs: SwimmingpoolIndoor):
    return idf.newidfobject('SWIMMINGPOOL:INDOOR', **kwargs)

def TableIndependentvariable(idf, **kwargs: TableIndependentvariable):
    return idf.newidfobject('TABLE:INDEPENDENTVARIABLE', **kwargs)

def TableIndependentvariablelist(idf, **kwargs: TableIndependentvariablelist):
    return idf.newidfobject('TABLE:INDEPENDENTVARIABLELIST', **kwargs)

def TableLookup(idf, **kwargs: TableLookup):
    return idf.newidfobject('TABLE:LOOKUP', **kwargs)

def Temperingvalve(idf, **kwargs: Temperingvalve):
    return idf.newidfobject('TEMPERINGVALVE', **kwargs)

def ThermalstorageChilledwaterMixed(idf, **kwargs: ThermalstorageChilledwaterMixed):
    return idf.newidfobject('THERMALSTORAGE:CHILLEDWATER:MIXED', **kwargs)

def ThermalstorageChilledwaterStratified(idf, **kwargs: ThermalstorageChilledwaterStratified):
    return idf.newidfobject('THERMALSTORAGE:CHILLEDWATER:STRATIFIED', **kwargs)

def ThermalstorageIceDetailed(idf, **kwargs: ThermalstorageIceDetailed):
    return idf.newidfobject('THERMALSTORAGE:ICE:DETAILED', **kwargs)

def ThermalstorageIceSimple(idf, **kwargs: ThermalstorageIceSimple):
    return idf.newidfobject('THERMALSTORAGE:ICE:SIMPLE', **kwargs)

def ThermostatsetpointDualsetpoint(idf, **kwargs: ThermostatsetpointDualsetpoint):
    return idf.newidfobject('THERMOSTATSETPOINT:DUALSETPOINT', **kwargs)

def ThermostatsetpointSinglecooling(idf, **kwargs: ThermostatsetpointSinglecooling):
    return idf.newidfobject('THERMOSTATSETPOINT:SINGLECOOLING', **kwargs)

def ThermostatsetpointSingleheating(idf, **kwargs: ThermostatsetpointSingleheating):
    return idf.newidfobject('THERMOSTATSETPOINT:SINGLEHEATING', **kwargs)

def ThermostatsetpointSingleheatingorcooling(idf, **kwargs: ThermostatsetpointSingleheatingorcooling):
    return idf.newidfobject('THERMOSTATSETPOINT:SINGLEHEATINGORCOOLING', **kwargs)

def ThermostatsetpointThermalcomfortFangerDualsetpoint(idf, **kwargs: ThermostatsetpointThermalcomfortFangerDualsetpoint):
    return idf.newidfobject('THERMOSTATSETPOINT:THERMALCOMFORT:FANGER:DUALSETPOINT', **kwargs)

def ThermostatsetpointThermalcomfortFangerSinglecooling(idf, **kwargs: ThermostatsetpointThermalcomfortFangerSinglecooling):
    return idf.newidfobject('THERMOSTATSETPOINT:THERMALCOMFORT:FANGER:SINGLECOOLING', **kwargs)

def ThermostatsetpointThermalcomfortFangerSingleheating(idf, **kwargs: ThermostatsetpointThermalcomfortFangerSingleheating):
    return idf.newidfobject('THERMOSTATSETPOINT:THERMALCOMFORT:FANGER:SINGLEHEATING', **kwargs)

def ThermostatsetpointThermalcomfortFangerSingleheatingorcooling(idf, **kwargs: ThermostatsetpointThermalcomfortFangerSingleheatingorcooling):
    return idf.newidfobject('THERMOSTATSETPOINT:THERMALCOMFORT:FANGER:SINGLEHEATINGORCOOLING', **kwargs)

def Timestep(idf, **kwargs: Timestep):
    return idf.newidfobject('TIMESTEP', **kwargs)

def UnitarysystemperformanceMultispeed(idf, **kwargs: UnitarysystemperformanceMultispeed):
    return idf.newidfobject('UNITARYSYSTEMPERFORMANCE:MULTISPEED', **kwargs)

def UtilitycostChargeBlock(idf, **kwargs: UtilitycostChargeBlock):
    return idf.newidfobject('UTILITYCOST:CHARGE:BLOCK', **kwargs)

def UtilitycostChargeSimple(idf, **kwargs: UtilitycostChargeSimple):
    return idf.newidfobject('UTILITYCOST:CHARGE:SIMPLE', **kwargs)

def UtilitycostComputation(idf, **kwargs: UtilitycostComputation):
    return idf.newidfobject('UTILITYCOST:COMPUTATION', **kwargs)

def UtilitycostQualify(idf, **kwargs: UtilitycostQualify):
    return idf.newidfobject('UTILITYCOST:QUALIFY', **kwargs)

def UtilitycostRatchet(idf, **kwargs: UtilitycostRatchet):
    return idf.newidfobject('UTILITYCOST:RATCHET', **kwargs)

def UtilitycostTariff(idf, **kwargs: UtilitycostTariff):
    return idf.newidfobject('UTILITYCOST:TARIFF', **kwargs)

def UtilitycostVariable(idf, **kwargs: UtilitycostVariable):
    return idf.newidfobject('UTILITYCOST:VARIABLE', **kwargs)

def Version(idf, **kwargs: Version):
    return idf.newidfobject('VERSION', **kwargs)

def WallAdiabatic(idf, **kwargs: WallAdiabatic):
    return idf.newidfobject('WALL:ADIABATIC', **kwargs)

def WallDetailed(idf, **kwargs: WallDetailed):
    return idf.newidfobject('WALL:DETAILED', **kwargs)

def WallExterior(idf, **kwargs: WallExterior):
    return idf.newidfobject('WALL:EXTERIOR', **kwargs)

def WallInterzone(idf, **kwargs: WallInterzone):
    return idf.newidfobject('WALL:INTERZONE', **kwargs)

def WallUnderground(idf, **kwargs: WallUnderground):
    return idf.newidfobject('WALL:UNDERGROUND', **kwargs)

def WaterheaterHeatpumpPumpedcondenser(idf, **kwargs: WaterheaterHeatpumpPumpedcondenser):
    return idf.newidfobject('WATERHEATER:HEATPUMP:PUMPEDCONDENSER', **kwargs)

def WaterheaterHeatpumpWrappedcondenser(idf, **kwargs: WaterheaterHeatpumpWrappedcondenser):
    return idf.newidfobject('WATERHEATER:HEATPUMP:WRAPPEDCONDENSER', **kwargs)

def WaterheaterMixed(idf, **kwargs: WaterheaterMixed):
    return idf.newidfobject('WATERHEATER:MIXED', **kwargs)

def WaterheaterSizing(idf, **kwargs: WaterheaterSizing):
    return idf.newidfobject('WATERHEATER:SIZING', **kwargs)

def WaterheaterStratified(idf, **kwargs: WaterheaterStratified):
    return idf.newidfobject('WATERHEATER:STRATIFIED', **kwargs)

def WateruseConnections(idf, **kwargs: WateruseConnections):
    return idf.newidfobject('WATERUSE:CONNECTIONS', **kwargs)

def WateruseEquipment(idf, **kwargs: WateruseEquipment):
    return idf.newidfobject('WATERUSE:EQUIPMENT', **kwargs)

def WateruseRaincollector(idf, **kwargs: WateruseRaincollector):
    return idf.newidfobject('WATERUSE:RAINCOLLECTOR', **kwargs)

def WateruseStorage(idf, **kwargs: WateruseStorage):
    return idf.newidfobject('WATERUSE:STORAGE', **kwargs)

def WateruseWell(idf, **kwargs: WateruseWell):
    return idf.newidfobject('WATERUSE:WELL', **kwargs)

def WeatherpropertySkytemperature(idf, **kwargs: WeatherpropertySkytemperature):
    return idf.newidfobject('WEATHERPROPERTY:SKYTEMPERATURE', **kwargs)

def Window(idf, **kwargs: Window):
    return idf.newidfobject('WINDOW', **kwargs)

def WindowInterzone(idf, **kwargs: WindowInterzone):
    return idf.newidfobject('WINDOW:INTERZONE', **kwargs)

def WindowgapDeflectionstate(idf, **kwargs: WindowgapDeflectionstate):
    return idf.newidfobject('WINDOWGAP:DEFLECTIONSTATE', **kwargs)

def WindowgapSupportpillar(idf, **kwargs: WindowgapSupportpillar):
    return idf.newidfobject('WINDOWGAP:SUPPORTPILLAR', **kwargs)

def WindowmaterialBlind(idf, **kwargs: WindowmaterialBlind):
    return idf.newidfobject('WINDOWMATERIAL:BLIND', **kwargs)

def WindowmaterialBlindEquivalentlayer(idf, **kwargs: WindowmaterialBlindEquivalentlayer):
    return idf.newidfobject('WINDOWMATERIAL:BLIND:EQUIVALENTLAYER', **kwargs)

def WindowmaterialComplexshade(idf, **kwargs: WindowmaterialComplexshade):
    return idf.newidfobject('WINDOWMATERIAL:COMPLEXSHADE', **kwargs)

def WindowmaterialDrapeEquivalentlayer(idf, **kwargs: WindowmaterialDrapeEquivalentlayer):
    return idf.newidfobject('WINDOWMATERIAL:DRAPE:EQUIVALENTLAYER', **kwargs)

def WindowmaterialGap(idf, **kwargs: WindowmaterialGap):
    return idf.newidfobject('WINDOWMATERIAL:GAP', **kwargs)

def WindowmaterialGapEquivalentlayer(idf, **kwargs: WindowmaterialGapEquivalentlayer):
    return idf.newidfobject('WINDOWMATERIAL:GAP:EQUIVALENTLAYER', **kwargs)

def WindowmaterialGas(idf, **kwargs: WindowmaterialGas):
    return idf.newidfobject('WINDOWMATERIAL:GAS', **kwargs)

def WindowmaterialGasmixture(idf, **kwargs: WindowmaterialGasmixture):
    return idf.newidfobject('WINDOWMATERIAL:GASMIXTURE', **kwargs)

def WindowmaterialGlazing(idf, **kwargs: WindowmaterialGlazing):
    return idf.newidfobject('WINDOWMATERIAL:GLAZING', **kwargs)

def WindowmaterialGlazingEquivalentlayer(idf, **kwargs: WindowmaterialGlazingEquivalentlayer):
    return idf.newidfobject('WINDOWMATERIAL:GLAZING:EQUIVALENTLAYER', **kwargs)

def WindowmaterialGlazingRefractionextinctionmethod(idf, **kwargs: WindowmaterialGlazingRefractionextinctionmethod):
    return idf.newidfobject('WINDOWMATERIAL:GLAZING:REFRACTIONEXTINCTIONMETHOD', **kwargs)

def WindowmaterialGlazinggroupThermochromic(idf, **kwargs: WindowmaterialGlazinggroupThermochromic):
    return idf.newidfobject('WINDOWMATERIAL:GLAZINGGROUP:THERMOCHROMIC', **kwargs)

def WindowmaterialScreen(idf, **kwargs: WindowmaterialScreen):
    return idf.newidfobject('WINDOWMATERIAL:SCREEN', **kwargs)

def WindowmaterialScreenEquivalentlayer(idf, **kwargs: WindowmaterialScreenEquivalentlayer):
    return idf.newidfobject('WINDOWMATERIAL:SCREEN:EQUIVALENTLAYER', **kwargs)

def WindowmaterialShade(idf, **kwargs: WindowmaterialShade):
    return idf.newidfobject('WINDOWMATERIAL:SHADE', **kwargs)

def WindowmaterialShadeEquivalentlayer(idf, **kwargs: WindowmaterialShadeEquivalentlayer):
    return idf.newidfobject('WINDOWMATERIAL:SHADE:EQUIVALENTLAYER', **kwargs)

def WindowmaterialSimpleglazingsystem(idf, **kwargs: WindowmaterialSimpleglazingsystem):
    return idf.newidfobject('WINDOWMATERIAL:SIMPLEGLAZINGSYSTEM', **kwargs)

def WindowpropertyAirflowcontrol(idf, **kwargs: WindowpropertyAirflowcontrol):
    return idf.newidfobject('WINDOWPROPERTY:AIRFLOWCONTROL', **kwargs)

def WindowpropertyFrameanddivider(idf, **kwargs: WindowpropertyFrameanddivider):
    return idf.newidfobject('WINDOWPROPERTY:FRAMEANDDIVIDER', **kwargs)

def WindowpropertyStormwindow(idf, **kwargs: WindowpropertyStormwindow):
    return idf.newidfobject('WINDOWPROPERTY:STORMWINDOW', **kwargs)

def Windowscalculationengine(idf, **kwargs: Windowscalculationengine):
    return idf.newidfobject('WINDOWSCALCULATIONENGINE', **kwargs)

def Windowshadingcontrol(idf, **kwargs: Windowshadingcontrol):
    return idf.newidfobject('WINDOWSHADINGCONTROL', **kwargs)

def WindowthermalmodelParams(idf, **kwargs: WindowthermalmodelParams):
    return idf.newidfobject('WINDOWTHERMALMODEL:PARAMS', **kwargs)

def Zone(idf, **kwargs: Zone):
    return idf.newidfobject('ZONE', **kwargs)

def ZoneairbalanceOutdoorair(idf, **kwargs: ZoneairbalanceOutdoorair):
    return idf.newidfobject('ZONEAIRBALANCE:OUTDOORAIR', **kwargs)

def Zoneaircontaminantbalance(idf, **kwargs: Zoneaircontaminantbalance):
    return idf.newidfobject('ZONEAIRCONTAMINANTBALANCE', **kwargs)

def Zoneairheatbalancealgorithm(idf, **kwargs: Zoneairheatbalancealgorithm):
    return idf.newidfobject('ZONEAIRHEATBALANCEALGORITHM', **kwargs)

def Zoneairmassflowconservation(idf, **kwargs: Zoneairmassflowconservation):
    return idf.newidfobject('ZONEAIRMASSFLOWCONSERVATION', **kwargs)

def ZonebaseboardOutdoortemperaturecontrolled(idf, **kwargs: ZonebaseboardOutdoortemperaturecontrolled):
    return idf.newidfobject('ZONEBASEBOARD:OUTDOORTEMPERATURECONTROLLED', **kwargs)

def ZonecapacitancemultiplierResearchspecial(idf, **kwargs: ZonecapacitancemultiplierResearchspecial):
    return idf.newidfobject('ZONECAPACITANCEMULTIPLIER:RESEARCHSPECIAL', **kwargs)

def ZonecontaminantsourceandsinkCarbondioxide(idf, **kwargs: ZonecontaminantsourceandsinkCarbondioxide):
    return idf.newidfobject('ZONECONTAMINANTSOURCEANDSINK:CARBONDIOXIDE', **kwargs)

def ZonecontaminantsourceandsinkGenericConstant(idf, **kwargs: ZonecontaminantsourceandsinkGenericConstant):
    return idf.newidfobject('ZONECONTAMINANTSOURCEANDSINK:GENERIC:CONSTANT', **kwargs)

def ZonecontaminantsourceandsinkGenericCutoffmodel(idf, **kwargs: ZonecontaminantsourceandsinkGenericCutoffmodel):
    return idf.newidfobject('ZONECONTAMINANTSOURCEANDSINK:GENERIC:CUTOFFMODEL', **kwargs)

def ZonecontaminantsourceandsinkGenericDecaysource(idf, **kwargs: ZonecontaminantsourceandsinkGenericDecaysource):
    return idf.newidfobject('ZONECONTAMINANTSOURCEANDSINK:GENERIC:DECAYSOURCE', **kwargs)

def ZonecontaminantsourceandsinkGenericDepositionratesink(idf, **kwargs: ZonecontaminantsourceandsinkGenericDepositionratesink):
    return idf.newidfobject('ZONECONTAMINANTSOURCEANDSINK:GENERIC:DEPOSITIONRATESINK', **kwargs)

def ZonecontrolContaminantcontroller(idf, **kwargs: ZonecontrolContaminantcontroller):
    return idf.newidfobject('ZONECONTROL:CONTAMINANTCONTROLLER', **kwargs)

def ZonecontrolHumidistat(idf, **kwargs: ZonecontrolHumidistat):
    return idf.newidfobject('ZONECONTROL:HUMIDISTAT', **kwargs)

def ZonecontrolThermostat(idf, **kwargs: ZonecontrolThermostat):
    return idf.newidfobject('ZONECONTROL:THERMOSTAT', **kwargs)

def ZonecontrolThermostatOperativetemperature(idf, **kwargs: ZonecontrolThermostatOperativetemperature):
    return idf.newidfobject('ZONECONTROL:THERMOSTAT:OPERATIVETEMPERATURE', **kwargs)

def ZonecontrolThermostatStageddualsetpoint(idf, **kwargs: ZonecontrolThermostatStageddualsetpoint):
    return idf.newidfobject('ZONECONTROL:THERMOSTAT:STAGEDDUALSETPOINT', **kwargs)

def ZonecontrolThermostatTemperatureandhumidity(idf, **kwargs: ZonecontrolThermostatTemperatureandhumidity):
    return idf.newidfobject('ZONECONTROL:THERMOSTAT:TEMPERATUREANDHUMIDITY', **kwargs)

def ZonecontrolThermostatThermalcomfort(idf, **kwargs: ZonecontrolThermostatThermalcomfort):
    return idf.newidfobject('ZONECONTROL:THERMOSTAT:THERMALCOMFORT', **kwargs)

def ZonecooltowerShower(idf, **kwargs: ZonecooltowerShower):
    return idf.newidfobject('ZONECOOLTOWER:SHOWER', **kwargs)

def Zonecrossmixing(idf, **kwargs: Zonecrossmixing):
    return idf.newidfobject('ZONECROSSMIXING', **kwargs)

def Zoneearthtube(idf, **kwargs: Zoneearthtube):
    return idf.newidfobject('ZONEEARTHTUBE', **kwargs)

def ZoneearthtubeParameters(idf, **kwargs: ZoneearthtubeParameters):
    return idf.newidfobject('ZONEEARTHTUBE:PARAMETERS', **kwargs)

def Zonegroup(idf, **kwargs: Zonegroup):
    return idf.newidfobject('ZONEGROUP', **kwargs)

def ZonehvacAirdistributionunit(idf, **kwargs: ZonehvacAirdistributionunit):
    return idf.newidfobject('ZONEHVAC:AIRDISTRIBUTIONUNIT', **kwargs)

def ZonehvacBaseboardConvectiveElectric(idf, **kwargs: ZonehvacBaseboardConvectiveElectric):
    return idf.newidfobject('ZONEHVAC:BASEBOARD:CONVECTIVE:ELECTRIC', **kwargs)

def ZonehvacBaseboardConvectiveWater(idf, **kwargs: ZonehvacBaseboardConvectiveWater):
    return idf.newidfobject('ZONEHVAC:BASEBOARD:CONVECTIVE:WATER', **kwargs)

def ZonehvacBaseboardRadiantconvectiveElectric(idf, **kwargs: ZonehvacBaseboardRadiantconvectiveElectric):
    return idf.newidfobject('ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:ELECTRIC', **kwargs)

def ZonehvacBaseboardRadiantconvectiveSteam(idf, **kwargs: ZonehvacBaseboardRadiantconvectiveSteam):
    return idf.newidfobject('ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:STEAM', **kwargs)

def ZonehvacBaseboardRadiantconvectiveSteamDesign(idf, **kwargs: ZonehvacBaseboardRadiantconvectiveSteamDesign):
    return idf.newidfobject('ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:STEAM:DESIGN', **kwargs)

def ZonehvacBaseboardRadiantconvectiveWater(idf, **kwargs: ZonehvacBaseboardRadiantconvectiveWater):
    return idf.newidfobject('ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:WATER', **kwargs)

def ZonehvacBaseboardRadiantconvectiveWaterDesign(idf, **kwargs: ZonehvacBaseboardRadiantconvectiveWaterDesign):
    return idf.newidfobject('ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:WATER:DESIGN', **kwargs)

def ZonehvacCoolingpanelRadiantconvectiveWater(idf, **kwargs: ZonehvacCoolingpanelRadiantconvectiveWater):
    return idf.newidfobject('ZONEHVAC:COOLINGPANEL:RADIANTCONVECTIVE:WATER', **kwargs)

def ZonehvacDehumidifierDx(idf, **kwargs: ZonehvacDehumidifierDx):
    return idf.newidfobject('ZONEHVAC:DEHUMIDIFIER:DX', **kwargs)

def ZonehvacEnergyrecoveryventilator(idf, **kwargs: ZonehvacEnergyrecoveryventilator):
    return idf.newidfobject('ZONEHVAC:ENERGYRECOVERYVENTILATOR', **kwargs)

def ZonehvacEnergyrecoveryventilatorController(idf, **kwargs: ZonehvacEnergyrecoveryventilatorController):
    return idf.newidfobject('ZONEHVAC:ENERGYRECOVERYVENTILATOR:CONTROLLER', **kwargs)

def ZonehvacEquipmentconnections(idf, **kwargs: ZonehvacEquipmentconnections):
    return idf.newidfobject('ZONEHVAC:EQUIPMENTCONNECTIONS', **kwargs)

def ZonehvacEquipmentlist(idf, **kwargs: ZonehvacEquipmentlist):
    return idf.newidfobject('ZONEHVAC:EQUIPMENTLIST', **kwargs)

def ZonehvacEvaporativecoolerunit(idf, **kwargs: ZonehvacEvaporativecoolerunit):
    return idf.newidfobject('ZONEHVAC:EVAPORATIVECOOLERUNIT', **kwargs)

def ZonehvacExhaustcontrol(idf, **kwargs: ZonehvacExhaustcontrol):
    return idf.newidfobject('ZONEHVAC:EXHAUSTCONTROL', **kwargs)

def ZonehvacForcedairUserdefined(idf, **kwargs: ZonehvacForcedairUserdefined):
    return idf.newidfobject('ZONEHVAC:FORCEDAIR:USERDEFINED', **kwargs)

def ZonehvacFourpipefancoil(idf, **kwargs: ZonehvacFourpipefancoil):
    return idf.newidfobject('ZONEHVAC:FOURPIPEFANCOIL', **kwargs)

def ZonehvacHightemperatureradiant(idf, **kwargs: ZonehvacHightemperatureradiant):
    return idf.newidfobject('ZONEHVAC:HIGHTEMPERATURERADIANT', **kwargs)

def ZonehvacHybridunitaryhvac(idf, **kwargs: ZonehvacHybridunitaryhvac):
    return idf.newidfobject('ZONEHVAC:HYBRIDUNITARYHVAC', **kwargs)

def ZonehvacIdealloadsairsystem(idf, **kwargs: ZonehvacIdealloadsairsystem):
    return idf.newidfobject('ZONEHVAC:IDEALLOADSAIRSYSTEM', **kwargs)

def ZonehvacLowtemperatureradiantConstantflow(idf, **kwargs: ZonehvacLowtemperatureradiantConstantflow):
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:CONSTANTFLOW', **kwargs)

def ZonehvacLowtemperatureradiantConstantflowDesign(idf, **kwargs: ZonehvacLowtemperatureradiantConstantflowDesign):
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:CONSTANTFLOW:DESIGN', **kwargs)

def ZonehvacLowtemperatureradiantElectric(idf, **kwargs: ZonehvacLowtemperatureradiantElectric):
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:ELECTRIC', **kwargs)

def ZonehvacLowtemperatureradiantSurfacegroup(idf, **kwargs: ZonehvacLowtemperatureradiantSurfacegroup):
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:SURFACEGROUP', **kwargs)

def ZonehvacLowtemperatureradiantVariableflow(idf, **kwargs: ZonehvacLowtemperatureradiantVariableflow):
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:VARIABLEFLOW', **kwargs)

def ZonehvacLowtemperatureradiantVariableflowDesign(idf, **kwargs: ZonehvacLowtemperatureradiantVariableflowDesign):
    return idf.newidfobject('ZONEHVAC:LOWTEMPERATURERADIANT:VARIABLEFLOW:DESIGN', **kwargs)

def ZonehvacOutdoorairunit(idf, **kwargs: ZonehvacOutdoorairunit):
    return idf.newidfobject('ZONEHVAC:OUTDOORAIRUNIT', **kwargs)

def ZonehvacOutdoorairunitEquipmentlist(idf, **kwargs: ZonehvacOutdoorairunitEquipmentlist):
    return idf.newidfobject('ZONEHVAC:OUTDOORAIRUNIT:EQUIPMENTLIST', **kwargs)

def ZonehvacPackagedterminalairconditioner(idf, **kwargs: ZonehvacPackagedterminalairconditioner):
    return idf.newidfobject('ZONEHVAC:PACKAGEDTERMINALAIRCONDITIONER', **kwargs)

def ZonehvacPackagedterminalheatpump(idf, **kwargs: ZonehvacPackagedterminalheatpump):
    return idf.newidfobject('ZONEHVAC:PACKAGEDTERMINALHEATPUMP', **kwargs)

def ZonehvacRefrigerationchillerset(idf, **kwargs: ZonehvacRefrigerationchillerset):
    return idf.newidfobject('ZONEHVAC:REFRIGERATIONCHILLERSET', **kwargs)

def ZonehvacTerminalunitVariablerefrigerantflow(idf, **kwargs: ZonehvacTerminalunitVariablerefrigerantflow):
    return idf.newidfobject('ZONEHVAC:TERMINALUNIT:VARIABLEREFRIGERANTFLOW', **kwargs)

def ZonehvacUnitheater(idf, **kwargs: ZonehvacUnitheater):
    return idf.newidfobject('ZONEHVAC:UNITHEATER', **kwargs)

def ZonehvacUnitventilator(idf, **kwargs: ZonehvacUnitventilator):
    return idf.newidfobject('ZONEHVAC:UNITVENTILATOR', **kwargs)

def ZonehvacVentilatedslab(idf, **kwargs: ZonehvacVentilatedslab):
    return idf.newidfobject('ZONEHVAC:VENTILATEDSLAB', **kwargs)

def ZonehvacVentilatedslabSlabgroup(idf, **kwargs: ZonehvacVentilatedslabSlabgroup):
    return idf.newidfobject('ZONEHVAC:VENTILATEDSLAB:SLABGROUP', **kwargs)

def ZonehvacWatertoairheatpump(idf, **kwargs: ZonehvacWatertoairheatpump):
    return idf.newidfobject('ZONEHVAC:WATERTOAIRHEATPUMP', **kwargs)

def ZonehvacWindowairconditioner(idf, **kwargs: ZonehvacWindowairconditioner):
    return idf.newidfobject('ZONEHVAC:WINDOWAIRCONDITIONER', **kwargs)

def ZoneinfiltrationDesignflowrate(idf, **kwargs: ZoneinfiltrationDesignflowrate):
    return idf.newidfobject('ZONEINFILTRATION:DESIGNFLOWRATE', **kwargs)

def ZoneinfiltrationEffectiveleakagearea(idf, **kwargs: ZoneinfiltrationEffectiveleakagearea):
    return idf.newidfobject('ZONEINFILTRATION:EFFECTIVELEAKAGEAREA', **kwargs)

def ZoneinfiltrationFlowcoefficient(idf, **kwargs: ZoneinfiltrationFlowcoefficient):
    return idf.newidfobject('ZONEINFILTRATION:FLOWCOEFFICIENT', **kwargs)

def Zonelist(idf, **kwargs: Zonelist):
    return idf.newidfobject('ZONELIST', **kwargs)

def Zonemixing(idf, **kwargs: Zonemixing):
    return idf.newidfobject('ZONEMIXING', **kwargs)

def ZonepropertyLocalenvironment(idf, **kwargs: ZonepropertyLocalenvironment):
    return idf.newidfobject('ZONEPROPERTY:LOCALENVIRONMENT', **kwargs)

def ZonepropertyUserviewfactorsBysurfacename(idf, **kwargs: ZonepropertyUserviewfactorsBysurfacename):
    return idf.newidfobject('ZONEPROPERTY:USERVIEWFACTORS:BYSURFACENAME', **kwargs)

def Zonerefrigerationdoormixing(idf, **kwargs: Zonerefrigerationdoormixing):
    return idf.newidfobject('ZONEREFRIGERATIONDOORMIXING', **kwargs)

def Zoneterminalunitlist(idf, **kwargs: Zoneterminalunitlist):
    return idf.newidfobject('ZONETERMINALUNITLIST', **kwargs)

def Zonethermalchimney(idf, **kwargs: Zonethermalchimney):
    return idf.newidfobject('ZONETHERMALCHIMNEY', **kwargs)

def ZoneventilationDesignflowrate(idf, **kwargs: ZoneventilationDesignflowrate):
    return idf.newidfobject('ZONEVENTILATION:DESIGNFLOWRATE', **kwargs)

def ZoneventilationWindandstackopenarea(idf, **kwargs: ZoneventilationWindandstackopenarea):
    return idf.newidfobject('ZONEVENTILATION:WINDANDSTACKOPENAREA', **kwargs)
