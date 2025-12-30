# simulations avec energyplus

Il existe un convertisseur pour passer d'une version à une autre d'openstudio/energy plus

Ce convertisseur est nécessaire si on télécharge des idf depuis https://www.energycodes.gov/prototype-building-models

```
C:\EnergyPlusV24-1-0\PreProcess\IDFVersionUpdater
```
C'est un utilitaire GUI qui est inclus dans toute version d'energyplus autonome. 

Les outils de preprocess/postprocess ne sont pas installés lorsqu'on installe Openstudio.

L'installation d'Openstudio GUI comporte un ensemble de fichiers osm de tests.

Openstudio migre automatiquement les fichiers vers la version en cours, si besoin.

Il y a notamment :
- un exemple small office avec un toit en tuiles
- un fichier MidriseApartment qui montre comment modéliser des corridors

```
C:\openstudioapplication-1.8.0\Resources\ShoeboxModel\ShoeboxExample\measures\create_typical_building_from_model\tests
```

Pour activer l'enregistrement de timeseries lors des simulations :
Aller dans `Output Variables` puis `select output variables`
type | filtre | noms de variable 
--|--|--
températures extérieures | `Outdoor Air` | `Air Drybulb Temperature, *` et `Air Wetbulb Temperature, *`
températures de zones | `Zone Mean` ou `Zone Air` | `Zone Mean Air Temperature, *` et/ou `Zone Air Temperature, *`
puissances instantannées en W | `Rate` ou `Radiant` si on a des radiants | `Zone Radiant HVAC Heating Rate, *`
calendriers | `schedules` | `Schedule Value, *`

Energyplus fournit d'autres champs, mais qu'on retrouve facilement : 
type | filtre | noms de variable 
--|--|--
puissances instantannées en W | `Rate` ou `Radiant` si on a des radiants | `Zone Radiant HVAC Heating Rate, *` = 0.9 × `Zone Radiant HVAC NaturalGas Rate, *` si combustion efficiency = 0.9
énergie en joules | `energy` | `Zone Radiant HVAC Heating Energy, *` = 3600 × `Zone Radiant HVAC Heating Rate, *`

A quoi correspond `Zone Gas Equipement Radiant Heating Energy, *` ? normalement, c'est la fraction radiative. Mais lorsqu'on met des radiants et qu'on active ce champ, il n'y a pas de valeurs....

Il est intéressant d'observer la consommation totale du site, qui tient compte des pertes modelisées...

Pour convertir un eso, on utilise le ReadVarsESO.exe
```
C:\EnergyPlusV24-1-0\PostProcess
```
On colle l'eso dans ce répertoire et on double clique sur ReadVarsESO.exe

Normalement le csv doit apparaitre à coté de l'eso

Par défaut, Openstudio exporte 6 points par heures :

Simulation settings > Timestep > Number Of Timesteps Per Hour : 6 par défaut, mettre 1
