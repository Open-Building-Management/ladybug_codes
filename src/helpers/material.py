"""list of materials"""

from honeybee_energy.material.opaque import EnergyMaterial
from honeybee_energy.material.glazing import EnergyWindowMaterialGlazing
from honeybee_energy.material.gas import EnergyWindowMaterialGas
from honeybee_energy.construction.opaque import OpaqueConstruction
from honeybee_energy.construction.window import WindowConstruction

osb_20mm = EnergyMaterial(
    identifier='OSB_20mm',
    roughness='MediumRough',
    thickness=0.020,         # 2 cm
    conductivity=0.13,       # W/m·K
    density=600,             # kg/m3
    specific_heat=1600       # J/kg·K
)

# Laine de verre ancienne (années 70–90)
glasswool_old = EnergyMaterial(
    identifier='GlassWool_Old',
    roughness='Rough',
    thickness=0.100,
    conductivity=0.050,
    density=18,
    specific_heat=840
)
# laine de verre récente
glasswool_new = EnergyMaterial(
    identifier='GlassWool_New',
    roughness='MediumRough',
    thickness=0.120,
    conductivity=0.032,
    density=12,
    specific_heat=840
)
# laine de verre des années 2000
glasswool_2000 = EnergyMaterial(
    identifier='GlassWool_2000',
    roughness='MediumRough',
    thickness=0.100,
    conductivity=0.040,
    density=15,
    specific_heat=840
)
# parement extérieur en amiante
parement = EnergyMaterial(
    identifier='AmianteCiment_20mm',
    roughness='Rough',
    thickness=0.020,
    conductivity=0.35,
    density=1600,
    specific_heat=900
)

# plancher en béton
concrete_200mm = EnergyMaterial(
    identifier='Concrete_200mm',
    roughness='MediumRough',
    thickness=0.20,
    conductivity=1.75,
    density=2300,
    specific_heat=900
)

# éléments pour un mur en parpaing creux
plaster = EnergyMaterial(
    identifier='Plaster_2cm',
    thickness=0.02,
    conductivity=0.7,
    density=900,
    specific_heat=1000
)

air_cavity = EnergyMaterial(
    identifier='AirCavity_5cm',
    thickness=0.05,
    conductivity=0.025,  # conductivité de l’air
    density=1.2,
    specific_heat=1005
)

parpaing = EnergyMaterial(
    identifier='Parpaing_10cm',
    thickness=0.10,
    conductivity=0.72,
    density=800,
    specific_heat=840
)


# verre
glass = EnergyWindowMaterialGlazing(
    identifier="clear_glass",
    thickness=0.004,          # 4 mm
    conductivity=1.0,         # verre
    solar_transmittance=0.75,
    visible_transmittance=0.80,
    emissivity=0.84,
    emissivity_back=0.84
)

glass_2cm = EnergyWindowMaterialGlazing(
    identifier="thick_glass_for_wall",
    thickness=0.02,          # 2 cm
    conductivity=1.0,         # verre
    solar_transmittance=0.75,
    visible_transmittance=0.80,
    emissivity=0.84,
    emissivity_back=0.84
)

gap = EnergyWindowMaterialGas(
    identifier="air_gap_16mm",
    gas_type="Air",
    thickness=0.016
)

# compositions
wall_parpaing = OpaqueConstruction(
    identifier='wall_parpaing',
    materials=[
        plaster,
        parpaing,
        air_cavity,
        plaster
    ]
)

wall_osb = OpaqueConstruction(
    identifier='Wall_osb',
    materials=[
        osb_20mm,
        glasswool_old,
        parement
    ]
)

floor_internal = OpaqueConstruction(
    identifier='Floor_Internal',
    materials=[
        concrete_200mm
    ]
)


window_pvc = WindowConstruction(
    identifier="Fenetre_PVC_Double",
    materials=[glass, gap, glass]
)

simple_glass_wall = WindowConstruction(
    identifier="paroi murale simple vitrage",
    materials=[glass_2cm]
)
