"""yml geometry generator"""
import logging

from honeybee.boundarycondition import Ground, Outdoors
from honeybee.facetype import Floor, Wall, RoofCeiling
from honeybee.model import Model
from honeybee.room import Room
from honeybee_energy.writer import model_to_idf

from ladybug_geometry.geometry3d import Face3D, Point3D

from src.idfhub.common import get_logger, eval_expr, GEOMETRY, BLOCKS

from src.idfhub.helpers.geometry import complex_room, ApertureManager, add_aperture
from src.idfhub.helpers.matlib import CONSTLIB

LOGGER = get_logger(log_level=logging.INFO)

site = {}
buildings: list[list[Room]] = []

common_height = GEOMETRY.get("height", 3)

def prepare(
    coordinates: list[list[float]],
    variables: dict|None = None
) -> list[Point3D]:
    """prepare for complex_room method"""
    if variables is None:
        return [
            Point3D(*row)
            for row in coordinates
        ]
    return [
        Point3D(*[
            eval_expr(el, variables) if isinstance(el, str) else el
            for el in row
        ])
        for row in coordinates
    ]

def get_variables(metadata: dict) -> dict:
    """return dict of variables"""
    variables = {}
    variables["height"] = metadata.get("height", common_height)
    variables["altitude"] = metadata.get("altitude", 0)
    return variables

for building_name, building_metadata in GEOMETRY.items():
    if not isinstance(building_metadata, dict):
        continue
    building: list[Room] = []
    building_dict: dict[str, Room] = {}
    if "blocks" not in building_name:
        for level_name, level_metadata in building_metadata.items():
            if not isinstance(level_metadata, dict):
                continue
            if "walls" not in level_metadata:
                LOGGER.error("no floors key for %s, skipping the level", level_name)
                continue
            LOGGER.info("Generating %s", level_name)
            level_variables = get_variables(level_metadata)
            wall_points: list[list[float]] = []
            for x in level_metadata["walls"]:
                if isinstance(x, str):
                    if x in BLOCKS:
                        wall_points = [*wall_points, *BLOCKS[x]]
                if isinstance(x, list):
                    wall_points = [*wall_points, x]

            walls = prepare(wall_points, variables=level_variables)
            floors = []
            if "floors" in level_metadata:
                LOGGER.info("custom floors for %s", level_name)
                for x in level_metadata["floors"]:
                    if isinstance(x, str):
                        if x in BLOCKS:
                            floors.append(prepare(BLOCKS[x]))
            level = complex_room(
                walls,
                height=level_variables["height"],
                identifier=level_name,
                floors = floors if floors else None,
                use_polyface = not floors
            )
            building.append(level)
            building_dict[level_name] = level

    if building:
        site[building_name] = building_dict
        buildings= [*buildings, *building]

name = GEOMETRY.get("name", "test")
model = Model(name, buildings)
Room.solve_adjacency(model.rooms)

LOGGER.info(site)

# now we can customize the construction settings
for building_name, building_metadata in GEOMETRY.items():
    if not isinstance(building_metadata, dict):
        continue
    if "blocks" in building_name:
        continue
    for level_name, level_metadata in building_metadata.items():
        if not isinstance(level_metadata, dict):
            continue
        if "walls" not in level_metadata:
            LOGGER.error("no walls key for %s, skipping the level", level_name)
            continue
        constructions = level_metadata.get("constructions", {})
        level_walls: list[Wall] = []
        for face in site[building_name][level_name].faces:
            if isinstance(face.type, Wall):
                construction_name = constructions.get("walls")
                construction = CONSTLIB.get(construction_name)
                if construction is not None:
                    face.properties.energy.construction = construction
                level_walls.append(face)
            if isinstance(face.type, Floor):
                construction_name = constructions.get("floors")
                construction = CONSTLIB.get(construction_name)
                if construction is None:
                    continue
                if face.boundary_condition != Ground():
                    LOGGER.info("Setting floor construction %s on %s", construction_name, face)
                    face.properties.energy.construction = construction
            if isinstance(face.type, RoofCeiling):
                construction_name = constructions.get("roofs")
                construction = CONSTLIB.get(construction_name)
                if construction is None:
                    continue
                if face.boundary_condition != Outdoors():
                    LOGGER.info("Setting roof construction %s on %s", construction_name, face)
                    face.properties.energy.construction = construction
        # now we can add apertures
        apertures = level_metadata.get("apertures", {})
        if "numbers" not in apertures:
            LOGGER.warning("NO APERTURE ON LEVEL %s", level_name)
        else:
            numbers = apertures["numbers"]
            try:
                widths = apertures["widths"]
            except KeyError:
                widths = []
            try:
                heights = apertures["heights"]
            except KeyError:
                heights = []
            try:
                sill_heights = apertures["sill_heights"]
            except KeyError:
                sill_heights = []
            try:
                constructions = apertures["constructions"]
            except KeyError:
                constructions = []
            try:
                aperture_types = apertures["types"]
            except KeyError:
                aperture_types = []
            for i, face in enumerate(level_walls):
                try:
                    count = numbers[i]
                except IndexError:
                    LOGGER.warning("aperture index error")
                    continue
                if not count:
                    LOGGER.warning("skipping aperture on %s", face)
                    continue
                apm = ApertureManager(site[building_name][level_name])
                try:
                    width = widths[i]
                except IndexError:
                    width = apertures.get("width", 1.2)
                try:
                    height = heights[i]
                except IndexError:
                    height = apertures.get("height", 1.3)
                try:
                    sill_height = sill_heights[i]
                except IndexError:
                    sill_height = apertures.get("sill_height", 1)
                try:
                    aperture_type = aperture_types[i]
                except IndexError:
                    aperture_type = apertures.get("type", "aperture")
                apm.fix_dim(
                    width = width,
                    height = height,
                    sill_height = sill_height
                )
                try:
                    construction_name = constructions[i]
                except IndexError:
                    construction_name = apertures.get("construction")
                construction=CONSTLIB.get(construction_name)
                apm.face = face
                apm.set_u_v_bounds()
                apm.add_from_border(
                    construction=construction,
                    count=count,
                    aperture_type=aperture_type
                )
        # now we can add single elements if any
        elements = level_metadata.get("elements", {})
        level_variables = get_variables(level_metadata)
        for element_name, element_metadata in elements.items():
            if "geometry" not in element_metadata:
                continue
            face = level_walls[element_metadata.get("index", 0)]
            # we add an aperture so boundary conditions need to be outdoors
            # design choice, maybe not perfect, we could have an indoor aperture
            face.boundary_condition = Outdoors()
            points = prepare(element_metadata["geometry"], variables=level_variables)
            construction_name = element_metadata.get("construction")
            construction = CONSTLIB.get(construction_name)
            LOGGER.warning("GOT ELEMENT %s on %s", element_name, face)
            add_aperture(
                face,
                Face3D(points),
                construction=construction,
                label=element_name,
                aperture_type=element_metadata.get("type", "door")
            )

with open(f"{name}.idf", "w", encoding="utf-8") as f:
    f.write(model_to_idf(model))
