# Sources

The OpenStudio Application 1.8.0
OpenStudio 3.8.0, EnergyPlus 24.1.0

# notations et sigles

VAV – Variable Air Volume

PTAC signifie Packaged Terminal Air Conditioner.
On le trouve sous cette forme "ZoneHVAC:PackagedTerminalAirConditioner"
PTAC = unité air-air autonome par zone

# simulation settings

Do Zone Sizing → calcule la charge thermique de la zone

Do System Sizing → calcule la distribution air (AirLoops / Coils / Terminals)

Do Plant Sizing → calcule les besoins des boucles eau chaude / froide → essentiel si tu utilises des Baseboards ou un PlantLoop avec chaudière

Do HVAC sizing simulation for sizing periods

Pour un système à eau chaude, les 4 doivent être cochés, sinon le plant est mal informé de la demande réelle


# chaleur radiante et convection

Physiquement, un radiateur à eau ≈
- ~30–40 % rayonnement
- ~60–70 % convection naturelle

Un convecteur ≈
- très majoritairement convection
- peu de rayonnement

Le modèle HighTempRadiant repose sur :
- une fraction radiative majoritaire (70%)
- une fraction convective vers l’air
- une distribution radiative vers les surfaces

Cet objet ne représente PAS un radiateur à eau classique.

Exemples de radiants haute température :
- tubes gaz
- plaques infrarouges
- surfaces très chaudes (> 300 °C)

Cas d'usage typiques :
- halls industriels
- gymnases
- entrepôts

chauffage direct des personnes et surfaces par rayonnement, très peu de convection d'air

L'objet à utiliser pour représenter des radiateurs muraux est Zone HVAC Baseboard Rad Conv Water
ce sont des radiateurs très bas, le long de la plinthe, d'où le nom de baseboard


# Modéliser une chaufferie avec des radiateurs muraux à eau chaude

La loi d’eau se met sur la boucle eau chaude via un SetpointManager:OutdoorAirReset, on la trouve sous le nom de OA Temp Reset

L’émetteur :
- reçoit une eau à température pilotée
- module son débit (si VariableFlow)
Dans EnergyPlus, la loi d’eau n’est PAS portée par l’émetteur, mais par la boucle hydraulique.

Depuis l'onglet HVAC
- Créer un plant loop avec un HW Boiler et une Const Spd Pump
- Mettre un OA temp reset sur la production (-5°C ext = 70°C hot water, 15°C ext = 40°C hot water)
- Sur le boiler, mettre leavingSetPointModulated comme choix de modulation

Les objets baseboards ne sont pas visibles dans l’onglet HVAC, mais on les y injecte via l'onglet Thermal Zones

Depuis l'onglet Thermal Zones
- Mettre des Zone HVAC Baseboard Rad Conv Water comme équipement de zones sur les thermal zones à chauffer
- Rattacher ces équipements au plant loop via la case à cocher du second onglet de configuration des HVAC baseboard rad conv water.
- Mettre Always On comme availability schedule pour ces radiateurs
- Affecter le heating schedule aux thermal zones à chauffer


# PRHP

DX = direct expansion

type de batterie frigorifique ou chauffage où le fluide frigorigène est directement utilisé dans l’échangeur

Pas de boucle secondaire d’eau

Typiquement pour les unités :
- rooftop air-air
- split units

ADU = Air Distribution Unit

Dans EnergyPlus / OpenStudio, cela correspond à :
- Air Terminal Single Duct Constant Volume No Reheat
- ADU RPLUS1-AIR TERMINAL SINGLE DUCT CONSTANT VOLUME NO REHEAT 2:Zone Air Terminal Sensible Heating Rate [W](Hourly)

Ce n’est PAS une unité de chauffage active, mais l’interface entre le réseau d’air et la zone ou encore le flux thermique sensible transmis par l’air à la zone


Les PRHP sont modélisés par des courbes représentant :
- la dégradation avec la température extérieure
- l’influence du débit d’air

EIR = Energy Input Ratio.

## Heating Capacity Function of Temperature

Modifie la puissance maximale de la PAC

Capaciteˊ= Capaciteˊrated × f(Text, Tair)

- quand il fait froid → capacité diminue
- limite la puissance disponible
- impacte les unmet hours

## Heating EIR Function of Temperature

Modifie la consommation électrique : EIR = 1 / COP

quand il fait froid → EIR augmente, donc COP diminue

## Heating EIR Function of Flow Fraction

Corrige la conso si le débit d’air ≠ nominal

- débit partiel → rendement diminue
- plein débit → rendement optimal

## Part Load Fraction Correlation

Représente les cycles ON/OFF et les pertes à charge partielle

L'effet est un COP dégradé à faible charge, important en mi-saison

## Capacity Function of Flow Fraction

Corrige la capacité si débit ≠ nominal

Souvent peu impactant et proche de 1