"""yml geometry generator"""
import logging

from eppy.modeleditor import IDF

from honeybee.boundarycondition import Ground, Outdoors
from honeybee.facetype import Floor, Wall, RoofCeiling
from honeybee.model import Model
from honeybee.room import Room
from honeybee_energy.writer import model_to_idf

from ladybug_geometry.geometry3d import Face3D, Point3D

from idfhub.common import get_logger, eval_expr, GEOMETRY, BLOCKS, get_variables, OS_EP_PATH

from idfhub.helpers.geometry import complex_room, ApertureManager, add_aperture, dispatch_apertures
from idfhub.helpers.matlib import CONSTLIB

from idfhub.idf_autocomplete.v24_1_0.idf_helpers_short import BuildingsurfaceDetailedMeta

LOGGER = get_logger(log_level=logging.INFO)

site: dict[str, dict[str, Room]] = {}
buildings: list[list[Room]] = []

common_height = GEOMETRY.get("height", 3)

def prepare(
    coordinates: list[list[float|str]],
    *,
    variables: dict
) -> list[Point3D]:
    """evaluate user formulas and prepare for complex_room method"""
    if len(variables) == 0:
        return [
            Point3D(*row[0:3])
            for row in coordinates
        ]
    return [
        Point3D(*[
            eval_expr(el, variables) if isinstance(el, str) else el
            for el in row[0:3]
        ])
        for row in coordinates
    ]


def resolve(
    block: list[list|int|str],
    resolving: set[int|str] | None = None,
) -> list[list]:
    """auto resolve a reusable block
    Recursively resolve block names into block contents.
    """
    if resolving is None:
        resolving = set()
    result: list[list] = []
    for item in block:
        if isinstance(item, list):
            result.append(item)
        elif item in BLOCKS:
            if item in resolving:
                raise ValueError(
                    f"Circular block reference: {item}"
                )
            resolving.add(item)
            result.extend(resolve(BLOCKS[item], resolving))
            resolving.remove(item)
    return result

def get_construction_name(face3d: Face3D, yml_data: str | dict, default: str|None = None):
    """return the construction name from the yml data
    for roof and floor only"""
    if isinstance(yml_data, str):
        return yml_data
    if isinstance(yml_data, dict):
        nb = int(face3d.identifier.split("_")[-1])
        if nb in yml_data:
            return yml_data[nb]
    return default

level_metadatas = {}
air_boundaries = []
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
                LOGGER.error("no walls key for %s, skipping the level", level_name)
                continue
            level_metadatas[level_name] = level_metadata
            LOGGER.info("Generating %s", level_name)
            level_variables = get_variables(level_metadata)
            if level_metadata.get("use_blocks_vars", 0) == 1:
                level_variables = {**level_variables, **get_variables(BLOCKS)}
            wall_points: list[list[float | str]] = []
            for x in level_metadata["walls"]:
                if isinstance(x, str):
                    if x in BLOCKS:
                        wall_points.extend(resolve(BLOCKS[x]))
                if isinstance(x, list):
                    wall_points.append(x[0:3])

            walls = prepare(wall_points, variables=level_variables)
            surfaces: dict[str, list[list[Point3D]]] = {"floors": [], "roofs": []}
            for key, surface in surfaces.items():
                if key in level_metadata:
                    pts: list[list[float | str]] = []
                    LOGGER.info("custom %s for %s", key, level_name)
                    for x in level_metadata[key]:
                        if isinstance(x, str):
                            if x in BLOCKS:
                                surface.append(
                                    prepare(
                                        resolve(BLOCKS[x]),
                                        variables=get_variables(BLOCKS)
                                    )
                                )
                        if isinstance(x, list):
                            pts.append(x)
                    if len(pts) > 0:
                        surface.append(
                            prepare(
                                pts,
                                variables=level_variables
                            )
                        )
            height=level_metadata.get("height", common_height)
            if "heights" in level_metadata:
                height = [
                    eval_expr(el, level_variables)if isinstance(el, str) else el
                    for el in level_metadata["heights"]
                ]
            level = complex_room(
                walls,
                height=height,
                identifier=level_name,
                floors = surfaces["floors"],
                roofs = surfaces["roofs"],
                use_polyface = False,
                remove=level_metadata.get("remove")
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
for building_name, building_dict in site.items():
    for level_name, level in building_dict.items():
        level_metadata = level_metadatas[level_name]
        constructions = level_metadata.get("constructions", {})
        level_walls: list[Wall] = []
        level_roofs: list[RoofCeiling] = []
        walls_metadata = resolve(level_metadata["walls"])
        excluded = constructions.get("exclude", {})
        for face in level.faces:
            if isinstance(face.type, Wall):
                number = int(face.identifier.split("_")[-1])
                if number in excluded.get("walls", []):
                    continue
                generic = constructions.get("walls", constructions.get("default"))
                try:
                    construction_name = walls_metadata[number][3]
                except IndexError:
                    construction_name = generic
                if construction_name == "air_boundary":
                    air_boundaries.append(face.identifier)
                    continue
                construction = CONSTLIB.get(construction_name)
                if construction is not None:
                    face.properties.energy.construction = construction
                level_walls.append(face)
            if isinstance(face.type, Floor):
                number = int(face.identifier.split("_")[-1])
                if number in excluded.get("floors", []):
                    continue
                construction_name = get_construction_name(
                    face3d=face,
                    yml_data=constructions.get("floors"),
                    default=constructions.get("default")
                )
                if construction_name == "air_boundary":
                    air_boundaries.append(face.identifier)
                    continue
                construction = CONSTLIB.get(construction_name)
                if construction is None:
                    continue
                if face.boundary_condition != Ground():
                    LOGGER.info("Setting floor construction %s on %s", construction_name, face)
                    face.properties.energy.construction = construction
            if isinstance(face.type, RoofCeiling):
                number = int(face.identifier.split("_")[-1])
                if number in excluded.get("roofs", []):
                    continue
                construction_name = get_construction_name(
                    face3d=face,
                    yml_data=constructions.get("roofs"),
                    default=constructions.get("default")
                )
                if construction_name == "air_boundary":
                    air_boundaries.append(face.identifier)
                    continue
                construction = CONSTLIB.get(construction_name)
                if face.boundary_condition == Outdoors():
                    level_roofs.append(face)
                if construction is None:
                    continue
                if face.boundary_condition != Outdoors():
                    LOGGER.info("Setting roof construction %s on %s", construction_name, face)
                    face.properties.energy.construction = construction
        # now we can add apertures, doors and vasistas using an aperture manager
        aperture_keys = ["apertures", "doors", "vasistas"]
        apm = ApertureManager(level)
        for key in aperture_keys:
            apertures = level_metadata.get(key, {})
            dispatch_apertures(
                apertures=apertures,
                manager=apm,
                destination_faces=level_walls if key != "vasistas" else level_roofs,
                level_name=level_name,
                ap_type="aperture" if key != "doors" else "door"
            )
        # now we can add single elements if any
        elements = level_metadata.get("elements", {})
        level_variables = get_variables(level_metadata)
        if level_metadata.get("use_blocks_vars", 0) == 1:
            level_variables = {**level_variables, **get_variables(BLOCKS)}
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

# now we should set surfaces to air boundary if any in yaml
if air_boundaries:
    LOGGER.info("setting air boundaries...")
    IDF.setiddname(f"{OS_EP_PATH}/Energy+.idd")
    idf = IDF(f"{name}.idf")
    for surface_name in air_boundaries:
        surface = idf.getobject(
            BuildingsurfaceDetailedMeta.idf_name,
            surface_name
        )
        surface["Construction_Name"] = "Generic Air Boundary"
    idf.save(f"{name}.idf")
