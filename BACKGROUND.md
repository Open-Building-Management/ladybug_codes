The HVAC API of energyplus is really complex.
[openstudio](https://openstudiocoalition.org/) is excellent for standard systems (PackagedRoofHeatPump for exemple) 

To customize things, you have to acquire some knowledge of how an idf file is structured.

IDFEditor is great for visualisation, but fastidious for data entry.

On the contrary, the [eppy](https://github.com/santoshphilip/eppy) library is a good starting point to complete an idf through python code, but lack of autocompletion facilities.

So a toolkit for autocompletion has been produced :-) 

# IDF editor

![](https://github.com/user-attachments/assets/1d899391-1820-4541-933c-3667d51e8685)

# basic autocompletion in vscode

https://code.visualstudio.com/download

![](https://github.com/user-attachments/assets/2f84fcaf-1d63-4512-90f6-ea1fb404a3c0)

# openstudio and energyplus

install openstudio first !

for openstudio 1.8.0 :
- https://github.com/openstudiocoalition/OpenStudioApplication/releases/tag/v1.8.0
- https://github.com/openstudiocoalition/OpenStudioApplication/releases/download/v1.8.0/OpenStudioApplication-1.8.0+2722e3e751-Windows.exe

the 1.8.0 version will install energyplus 24.1.0 but not a complete version : IDFEditor will not be available

the full version can be installed from https://energyplus.net/downloads

- https://github.com/NatLabRockies/EnergyPlus/releases/tag/v24.1.0
- https://github.com/NatLabRockies/EnergyPlus/releases/download/v24.1.0/EnergyPlus-24.1.0-9d7789a3ac-Windows-x86_64.exe
