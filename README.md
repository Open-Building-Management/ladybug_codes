caution : current work in progress !

# idfhub

> how to generate idf files for energyplus ?

[more on the energyplus ecosystem](BACKGROUND.md)

[honeybee](https://github.com/ladybug-tools/honeybee) is very convenient for geometry and materials.

The idfhub lib provides some helpers to go even faster and to easily add custom hvac through simple yaml declaration

To install :

```
git clone https://github.com/Open-Building-Management/ladybug_codes
cd ladybug_codes
py -m pip install -e .
pip install -e
```

# Geometry

```
py .\generate_geometry.py
```

The idf produced in openstudio :

![](https://github.com/user-attachments/assets/e67ee291-8ce6-4776-8e4f-35654355ca41)
![](https://github.com/user-attachments/assets/7a4c0e1e-7308-45db-9393-114b42a19f35)

# HVAC

```
py .\generate_hvac.py
```

# DVIEW

Dview is the viewer to use to analyse an energyplus simulation 

https://github.com/NatLabRockies/wex/releases/tag/v1.2.0
