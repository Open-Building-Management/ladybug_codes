"""list of materials"""

from honeybee_energy.material.opaque import EnergyMaterial
from honeybee_energy.material.glazing import EnergyWindowMaterialGlazing
from honeybee_energy.material.gas import EnergyWindowMaterialGas
from honeybee_energy.construction.opaque import OpaqueConstruction
from honeybee_energy.construction.window import WindowConstruction

from idfhub.common import GEOMETRY

# constantes qui peuvent être utilisées dans le yml
# pour définir des épaisseurs custom
OSB = "osb"
GLASSWOOL_OLD = "glasswool_old"
GLASSWOOL_NEW = "glasswool_new"
GLASSWOOL_2000 = "glasswool_2000"
PAREMENT = "amiante_ciment"
CONCRETE = "concrete"
PLASTER = "plaster"
AIR_CAVITY = "air_cavity"
PARPAING = "parpaing"
CUT_STONE = "cut_stone"
OLD_MASONRY = "old_masonry"
LIME_PLASTER = "lime_plaster"
GYPSUM_BOARD = "gypsum_board"

# épaisseurs par défaut
THICKNESS = {
    OSB: 0.02, # 2 cm
    GLASSWOOL_OLD: 0.1,
    GLASSWOOL_NEW: 0.12,
    GLASSWOOL_2000: 0.1,
    PAREMENT: 0.02,
    CONCRETE: 0.2,
    PLASTER: 0.02,
    AIR_CAVITY: 0.05,
    PARPAING: 0.1,
    CUT_STONE: 0.6,
    OLD_MASONRY: 0.4,
    LIME_PLASTER: 0.02,
    GYPSUM_BOARD: 0.0127,
}

def thickness(name):
    """fetch the thickness from the yml conf"""
    return GEOMETRY.get(name, THICKNESS[name])

osb = EnergyMaterial(
    identifier=OSB,
    roughness='MediumRough',
    thickness=thickness(OSB),
    conductivity=0.13,       # W/m·K
    density=600,             # kg/m3
    specific_heat=1600       # J/kg·K
)

# Laine de verre ancienne (années 70–90)
glasswool_old = EnergyMaterial(
    identifier=GLASSWOOL_OLD,
    roughness='Rough',
    thickness=thickness(GLASSWOOL_OLD),
    conductivity=0.050,
    density=18,
    specific_heat=840
)
# laine de verre récente
glasswool_new = EnergyMaterial(
    identifier=GLASSWOOL_NEW,
    roughness='MediumRough',
    thickness=thickness(GLASSWOOL_NEW),
    conductivity=0.032,
    density=12,
    specific_heat=840
)
# laine de verre des années 2000
glasswool_2000 = EnergyMaterial(
    identifier=GLASSWOOL_2000,
    roughness='MediumRough',
    thickness=thickness(GLASSWOOL_2000),
    conductivity=0.040,
    density=15,
    specific_heat=840
)
# parement extérieur en amiante
parement = EnergyMaterial(
    identifier=PAREMENT,
    roughness='Rough',
    thickness=thickness(PAREMENT),
    conductivity=0.35,
    density=1600,
    specific_heat=900
)

# plancher en béton
concrete = EnergyMaterial(
    identifier=CONCRETE,
    roughness='MediumRough',
    thickness=thickness(CONCRETE),
    conductivity=1.75,
    density=2300,
    specific_heat=900
)

# éléments pour un mur en parpaing creux
plaster = EnergyMaterial(
    identifier=PLASTER,
    thickness=thickness(PLASTER),
    conductivity=0.7,
    density=900,
    specific_heat=1000
)

air_cavity = EnergyMaterial(
    identifier=AIR_CAVITY,
    thickness=thickness(AIR_CAVITY),
    conductivity=0.025,  # conductivité de l’air
    density=1.2,
    specific_heat=1005
)

parpaing = EnergyMaterial(
    identifier=PARPAING,
    thickness=thickness(PARPAING),
    conductivity=0.72,
    density=800,
    specific_heat=840
)

# pierre de taille
cut_stone = EnergyMaterial(
    identifier=CUT_STONE,
    roughness="Rough",
    thickness=thickness(CUT_STONE),
    conductivity=1.5,
    density=2100,
    specific_heat=900,
    thermal_absorptance=0.9,
    solar_absorptance=0.6,
    visible_absorptance=0.6
)

# maçonnerie ancienne
old_masonry = EnergyMaterial(
    identifier=OLD_MASONRY,
    roughness="Rough",
    thickness=thickness(OLD_MASONRY),
    conductivity=1,
    density=1700,
    specific_heat=900,
    thermal_absorptance=0.9,
    solar_absorptance=0.7,
    visible_absorptance=0.7
)

# enduit à la chaux
lime_plaster = EnergyMaterial(
    identifier=LIME_PLASTER,
    roughness="Smooth",
    thickness=thickness(LIME_PLASTER),
    conductivity=0.80,
    density=1700,
    specific_heat=1000,
    thermal_absorptance=0.90,
    solar_absorptance=0.30,
    visible_absorptance=0.30
)

# plaque au platre
gypsum_board = EnergyMaterial(
    identifier="gypsum_board",
    thickness=0.0127,
    conductivity=0.16,
    density=800,
    specific_heat=1090,
    thermal_absorptance=0.9,
    solar_absorptance=0.5,
    visible_absorptance=0.5
)

# tuile
roman_tile = EnergyMaterial(
    identifier="roman_tile",
    roughness="MediumRough",
    thickness=0.02,
    conductivity=0.85,
    density=1900,
    specific_heat=840,
    thermal_absorptance=0.90,
    solar_absorptance=0.75,
    visible_absorptance=0.75
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

thick_glass_for_wall = EnergyWindowMaterialGlazing(
    identifier="thick_glass_for_wall",
    thickness=0.02,          # 2 cm
    conductivity=1.0,         # verre
    solar_transmittance=0.75,
    visible_transmittance=0.80,
    emissivity=0.84,
    emissivity_back=0.84
)

gap = EnergyWindowMaterialGas(
    identifier="air_gap",
    gas_type="Air",
    thickness=0.016
)

# compositions
# outside layer always first
townhouse_basement = OpaqueConstruction(
    identifier="townhouse_basement",
    materials=[
        cut_stone
    ]
)

recent_light_renovation = OpaqueConstruction(
    identifier="recent_light_renovation",
    materials=[
        osb,
        glasswool_new,
        gypsum_board
    ]
)


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
    identifier='wall_osb',
    materials=[
        parement,
        glasswool_old,
        osb
    ]
)

floor_internal = OpaqueConstruction(
    identifier='floor_internal',
    materials=[
        concrete
    ]
)


window_pvc = WindowConstruction(
    identifier="fenetre_pvc_double",
    materials=[glass, gap, glass]
)

simple_glass_wall = WindowConstruction(
    identifier="mur_simple_vitrage",
    materials=[thick_glass_for_wall]
)
