"""geometric fonctions"""
from typing import Literal
from dataclasses import dataclass

from honeybee.room import Room
from honeybee.aperture import Aperture
from honeybee.door import Door
from honeybee.face import Face

from honeybee_energy.construction.window import WindowConstruction
from honeybee_energy.construction.opaque import OpaqueConstruction

from ladybug_geometry.geometry3d.polyface import Polyface3D
from ladybug_geometry.geometry3d import Vector3D, Point3D
from ladybug_geometry.geometry3d.plane import Plane
from ladybug_geometry.geometry3d.face import Face3D

from helpers.consts import LOGGER

WIDTH = 37.0
DEPTH = 11.0
LEVEL_HEIGHT = 3.0
TOLERANCE = 1e-7
ROOF = "roof"
FLOOR = "floor"
WALL = "wall"
DOOR = "door"
WIN = "win"

def box_room(
    name,
    width=WIDTH,
    depth=DEPTH,
    height=LEVEL_HEIGHT,
    origin=Point3D(0,0,0)
) -> Room:
    """create room"""
    return Room.from_box(
        identifier=name,
        width=width,
        depth=depth,
        height=height,
        origin=origin
    )

def create_walls(
    pts:list[Point3D],
    height: float,
) -> list[Face3D]:
    """create walls from lower and upper points"""
    up = Vector3D(0, 0, height)
    pts_u = [pt.move(up) for pt in pts]
    i_inds = list(range(len(pts)))
    j_inds = i_inds[1:] + [0]
    return [
        Face3D([
            pts[i],
            pts[j_inds[i]],
            pts_u[j_inds[i]],
            pts_u[i]
        ])
        for i in i_inds
    ]

def create_floors_roofs(
    floors:list[list[Point3D]],
    height: float
) -> tuple[list[Point3D], list[Point3D]]:
    """create floors and roofs"""
    up = Vector3D(0, 0, height)
    all_floors: list[Face3D] = []
    for floor in [Face3D(pts) for pts in floors]:
        if floor.normal.z > 0:
            LOGGER.debug("flipping to have a floor")
            all_floors.append(floor.flip())
        else:
            all_floors.append(floor.flip())
    all_up_pts = [[pt.move(up) for pt in pts] for pts in floors]
    all_roofs: list[Face3D] = []
    for roof in [Face3D(pts) for pts in all_up_pts]:
        if roof.normal.z < 0:
            LOGGER.debug("flipping to have a roof")
            all_roofs.append(roof.flip())
        else:
            all_roofs.append(roof)
    for i, f3d in enumerate(all_floors):
        message = f"floor {i} -> {f3d.normal}"
        LOGGER.debug(message)
    for i, f3d in enumerate(all_roofs):
        message = f"roof {i} -> {f3d.normal}"
        LOGGER.debug(message)
    return all_floors, all_roofs

def complex_room(
    pts:list[Point3D],
    height:float,
    identifier:str,
    floors:list[list[Point3D]]|None = None,
    use_polyface:bool = True
) -> Room:
    """create a complex room"""
    # on crée les murs d'après les glacis de points
    walls = create_walls(pts, height)
    # on crée sol(s) et plafond(s)
    if not floors:
        all_floors, all_roofs = create_floors_roofs([Face3D(pts)], height)
    else:
        all_floors, all_roofs = create_floors_roofs(floors, height)

    if use_polyface:
        polyface = Polyface3D.from_faces(
            [*all_floors, *walls, *all_roofs],
            tolerance = TOLERANCE
        )
        output_room = Room.from_polyface3d(
            identifier=identifier,
            polyface=polyface
        )
    else:
        hb_faces = []
        for i, f3d in enumerate(all_floors):
            hb = Face(
                identifier=f'{identifier}_{FLOOR}{i}',
                geometry=f3d
            )
            hb_faces.append(hb)
        for i, f3d in enumerate(all_roofs):
            hb = Face(
                identifier=f'{identifier}_{ROOF}{i}',
                geometry=f3d
            )
            hb_faces.append(hb)
        for i, f3d in enumerate(walls):
            hb = Face(
                identifier=f'{identifier}_{WALL}{i}',
                geometry=f3d
            )
            hb_faces.append(hb)
        output_room = Room(identifier, hb_faces)
    return output_room

def get_from_pattern(
    niveau :Room,
    pattern_identifier: str,
) -> Face:
    """get face from pattern identifier"""
    face: Face
    for face in niveau.faces:
        if pattern_identifier in face.identifier:
            return face
    return face

def get(
    niveau :Room,
    face_type: Literal[
        "floor",
        "roof",
        "front",
        "back",
        "left",
        "right"
    ]
) -> Face:
    """get a face checking its normal"""
    if face_type == "floor":
        normale = Vector3D(0, 0,-1)
    if face_type == "roof":
        normale = Vector3D(0, 0, 1)
    if face_type == "front":
        normale = Vector3D(0, 1, 0)
    if face_type == "back":
        normale = Vector3D(0,-1, 0)
    if face_type == "left":
        normale = Vector3D(-1,0, 0)
    if face_type == "right":
        normale = Vector3D(1, 0, 0)
    return next(
        face for face in niveau.faces
        if face.geometry.normal == normale
    )


def log_face_o_x_y(
    face: Face
) -> None:
    """affiche le repère du mur"""
    wall_plane = face.geometry.plane
    #message = dir(wall_plane)
    #LOGGER.debug(message)
    LOGGER.debug(f"wall_plane.o is {wall_plane.o}")
    LOGGER.debug(f"wall_plane.x is {wall_plane.x}")
    LOGGER.debug(f"wall_plane.y is {wall_plane.y}")


def world_to_local(
    face: Face,
    p_world: Point3D
) -> tuple[float, float]:
    """convertit un point monde en point local"""
    plane = face.geometry.plane
    vec = p_world - plane.o
    u = vec.dot(plane.x)
    v = vec.dot(plane.y)
    return u, v


def local_to_world(
    face: Face,
    u: float,
    v: float
) -> Point3D:
    """convertit un point local (u, v) en point monde"""
    plane = face.geometry.plane
    return plane.o + plane.x * u + plane.y * v


def get_face_u_v_bounds(face: Face) -> tuple[float, float, float, float]:
    """min et max selon le repère local u / v"""
    log_face_o_x_y(face)
    plane = face.geometry.plane
    us = []
    vs = []

    for i, pt in enumerate(face.geometry.vertices):
        message = f"point numéro {i} - {pt}"
        LOGGER.debug(message)
        LOGGER.debug(world_to_local(face, pt))
        vec = pt - plane.o
        us.append(vec.dot(plane.x))
        vs.append(vec.dot(plane.y))

    return min(us), max(us), min(vs), max(vs)


def aperture_geometry(
    face:Face,
    origin:Point3D,
    width:float,
    height:float,
) -> Face3D:
    """form geometry from face and origin"""
    plane = Plane(n=face.geometry.normal, o=origin)
    return Face3D.from_rectangle(
        base=width,
        height=height,
        base_plane=plane
    )


def add_aperture(
    face: Face,
    geometry: Face3D,
    construction: WindowConstruction|OpaqueConstruction,
    label: str,
    aperture_type: Aperture|Door
):
    """create the aperture given its geometry"""
    kwargs = {}
    if aperture_type == Door and isinstance(construction, WindowConstruction):
        kwargs={"is_glass":True}
    aperture = aperture_type(
        identifier=f"{face.identifier}_{label}",
        geometry=geometry,
        **kwargs
    )
    aperture.properties.energy.construction = construction
    if aperture_type==Door:
        face.add_door(aperture)
    else:
        face.add_aperture(aperture)


@dataclass
class Dims:
    """paramètre dimensionnels des ouvertures"""
    width: float = 1.2
    height: float = 1.3
    sill_height: float = 1


class ApertureManager:
    """helper pour positionner les ouvertures"""
    def __init__(
        self,
        room: Room,
        width: float = 1.2,
        height: float = 1.3,
        sill_height: float = 1
    ):
        """initialisation"""
        self.face: Face
        self.room: Room
        self.dims: Dims
        self.u_min: float
        self.u_max: float
        self.v: float
        self.fix_dim(width, height, sill_height)
        self.room = room

    def fix_dim(
        self,
        width: float,
        height: float,
        sill_height: float
    ):
        """fix aperture dimensions"""
        self.dims = Dims(
            width=width,
            height=height,
            sill_height=sill_height
        )

    def set(
        self,
        room: Room,
        pattern: str,
        use_orientation: bool = True
    ):
        """set the working room (and face)"""
        self.room = room
        self.fix_face(pattern, use_orientation)

    def fix_face(
        self,
        pattern: str,
        use_orientation: bool = True
    ):
        """fix working face"""
        if use_orientation:
            self.face = get(self.room, pattern)
        else:
            self.face = get_from_pattern(self.room, pattern)
        self.u_min, self.u_max, v_min, v_max = get_face_u_v_bounds(self.face)
        if self.face.geometry.plane.y.z < 0:
            self.v = v_max - self.dims.height - self.dims.sill_height
        else:
            self.v = v_min + self.dims.sill_height

    def _add(
        self,
        origin: Point3D,
        construction: WindowConstruction,
        label: str,
        aperture_type: Aperture|Door = Aperture,
    ):
        """add a single aperture"""
        geometry = aperture_geometry(
            self.face,
            origin=origin,
            width=self.dims.width,
            height=self.dims.height
        )
        add_aperture(
            self.face,
            geometry,
            construction=construction,
            label=label,
            aperture_type=aperture_type
        )

    def add_from_center(
        self,
        construction: WindowConstruction,
        aperture_type: Aperture|Door = Aperture,
        ecart:float|None = None,
        count:int = 1
    ):
        """ajoute les ouvertures symétriquement par rapport au centre"""
        translate = self.dims.width if not ecart else self.dims.width + ecart
        start_u = ( self.u_max + self.u_min - count * translate ) / 2
        for i in range(count):
            u = start_u + i * translate
            origin = local_to_world(self.face, u, self.v)
            LOGGER.debug(f"i {i} > plane origin: {origin}")
            self._add(
                origin=origin,
                construction=construction,
                label=f"{DOOR}_{i}" if aperture_type==Door else f"{WIN}_{i}",
                aperture_type=aperture_type
            )

    def add_from_border(
        self,
        construction: WindowConstruction,
        aperture_type: Aperture|Door = Aperture,
        ecart:float|None = None,
        count:int = 1
    ):
        """ajoute les ouvertures depuis un bord"""
        if not ecart:
            spacing = (self.u_max - self.u_min - count * self.dims.width) / (count + 1)
        else:
            spacing = ecart
        LOGGER.info(f"{self.face.identifier} >>>> spacing is {spacing}")
        for i in range(count):
            u = self.u_min + i * (self.dims.width + spacing) + spacing
            origin = local_to_world(self.face, u, self.v)
            LOGGER.debug(f"i {i} > plane origin: {origin}")
            self._add(
                origin=origin,
                construction=construction,
                label=f"{DOOR}_{i}" if aperture_type==Door else f"{WIN}_{i}",
                aperture_type=aperture_type
            )
