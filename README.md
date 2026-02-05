caution : current work in progress !

# idfhub

> how to generate idf files for energyplus ?

[honeybee](https://github.com/ladybug-tools/honeybee) is really convenient for geometry and materials.

The idfhub lib provides some helpers to go even faster.

To install :

```
git clone https://github.com/Open-Building-Management/ladybug_codes
cd ladybug_codes
py -m pip install -e .
pip install -e
```

The hvac API of energyplus is really complex. [openstudio](https://openstudiocoalition.org/) is excellent for standard systems (PackagedRoofHeatPump for exemple) 

To customize things, you have to acquire some knowledge of how an idf file is structured.

IDFEditor is great for visualisation, but fastidious for data entry.

On the contrary, the [eppy](https://github.com/santoshphilip/eppy) library is a good starting point to complete an idf through python code, but lack of autocompletion facilities.

So a toolkit for autocompletion has been produced :-) 

# Geometry

```
py .\generate_geometry.py
```

The idf produced in openstudio :

![](https://github.com/user-attachments/assets/e67ee291-8ce6-4776-8e4f-35654355ca41)

# IDF editor

![](https://github.com/user-attachments/assets/1d899391-1820-4541-933c-3667d51e8685)

# basic autocompletion in vscode

![](https://github.com/user-attachments/assets/2f84fcaf-1d63-4512-90f6-ea1fb404a3c0)

# HVAC

install openstudio first !

for openstudio 1.8.0 :
- https://github.com/openstudiocoalition/OpenStudioApplication/releases/tag/v1.8.0
- https://github.com/openstudiocoalition/OpenStudioApplication/releases/download/v1.8.0/OpenStudioApplication-1.8.0+2722e3e751-Windows.exe

the 1.8.0 version will install energyplus 24.1.0 but not a complete version : IDFEditor will not be available

the full version can be installed from https://energyplus.net/downloads

- https://github.com/NatLabRockies/EnergyPlus/releases/tag/v24.1.0
- https://github.com/NatLabRockies/EnergyPlus/releases/download/v24.1.0/EnergyPlus-24.1.0-9d7789a3ac-Windows-x86_64.exe


```
py .\generate_hvac.py
```

# DVIEW

Dview is the viewer to use to analyse an energyplus simulation 

https://github.com/NatLabRockies/wex/releases/tag/v1.2.0
