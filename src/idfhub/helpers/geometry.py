"""geometric fonctions"""
from dataclasses import dataclass
import logging

from honeybee.aperture import Aperture
from honeybee.boundarycondition import Surface
from honeybee.door import Door
from honeybee.face import Face
from honeybee.model import Model
from honeybee.room import Room

from honeybee_energy.construction.window import WindowConstruction
from honeybee_energy.construction.opaque import OpaqueConstruction

from ladybug_geometry.geometry3d.polyface import Polyface3D
from ladybug_geometry.geometry3d import Vector3D, Point3D
from ladybug_geometry.geometry3d.plane import Plane
from ladybug_geometry.geometry3d.face import Face3D

from idfhub.helpers.matlib import CONSTLIB

LOGGER = logging.getLogger(__name__)

WIDTH = 37.0
DEPTH = 11.0
LEVEL_HEIGHT = 3.0
TOLERANCE = 1e-7
ROOF = "roof"
FLOOR = "floor"
WALL = "wall"
DOOR = "door"
WIN = "win"

def view_boundaries(building: Model):
    """check boundary conditions"""
    for element in building:
        for _face in element.faces:
            message = f"id: {_face.identifier} type: {type(_face.type)}"
            LOGGER.info(message)
            message = f"bc: {_face.boundary_condition}"
            LOGGER.info(message)
            message = f"material: {_face.properties.energy.construction.identifier}"
            LOGGER.info(message)

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
    *,
    pts: list[Point3D],
    height: float|list[float] = 3,
    remove_wall: list[int] | None = None
) -> dict[str|int, Face3D]:
    """create walls from lower and upper points"""
    if remove_wall is None:
        remove_wall = []
    if isinstance(height, list):
        LOGGER.debug("having a list of heights %s", height)
        if len(height) != len(pts):
            pts_u = [pt.move(Vector3D(0,0,height[0])) for pt in pts]
        else:
            pts_u = [pt.move(Vector3D(0,0,height[i])) for i,pt in enumerate(pts)]
    else:
        up = Vector3D(0, 0, height)
        pts_u = [pt.move(up) for pt in pts]
    i_inds = list(range(len(pts)))
    j_inds = i_inds[1:] + [0]
    if remove_wall:
        LOGGER.info("removing wall %s", remove_wall)
    return {
        i: Face3D([
            pts[i],
            pts[j_inds[i]],
            pts_u[j_inds[i]],
            pts_u[i]
        ])
        for i in i_inds if i not in remove_wall
    }

def create_floors_roofs(
    *,
    floors:list[list[Point3D]],
    height: float = 3,
    roofs:list[list[Point3D]]|None = None,
    remove_floor: list[int]|None = None,
    remove_roof: list[int]|None = None
) -> tuple[dict[str|int, Face3D], dict[str|int, Face3D]]:
    """create floors and roofs"""
    if roofs is None:
        roofs = []
    if remove_floor is None:
        remove_floor = []
    if remove_roof is None:
        remove_roof = []
    all_floors: dict[str|int, Face3D] = {
        i: Face3D(pts).flip() if Face3D(pts).normal.z > 0 else Face3D(pts)
        for i, pts in enumerate(floors)
        if i not in remove_floor
    }
    # initialise the all_up_pts variable for the roofs
    if len(roofs) == 0:
        up = Vector3D(0, 0, height)
        all_up_pts = [[pt.move(up) for pt in pts] for pts in floors]
    else:
        all_up_pts = roofs
    all_roofs: dict[str|int, Face3D] = {
        i: Face3D(pts).flip() if Face3D(pts).normal.z < 0 else Face3D(pts)
        for i, pts in enumerate(all_up_pts)
        if i not in remove_roof
    }
    for key, f3d in all_floors.items():
        message = f"floor {key} -> {f3d.normal}"
        LOGGER.debug(message)
    for key, f3d in all_roofs.items():
        message = f"roof {key} -> {f3d.normal}"
        LOGGER.debug(message)
    return all_floors, all_roofs

REMOVE: dict[str, list[int]] = {
    "walls": [],
    "floors": [],
    "roofs": []
}

def complex_room(
    pts:list[Point3D],
    height:float|list[float],
    identifier:str,
    floors:list[list[Point3D]]|None = None,
    roofs:list[list[Point3D]]|None = None,
    use_polyface:bool = True,
    remove:dict[str, list[int]]|None = None
) -> Room:
    """create a complex room"""
    if floors is None:
        floors = []
    if roofs is None:
        roofs = []
    if remove is None:
        remove = REMOVE
    # on crée les murs d'après les glacis de points
    walls = create_walls(pts=pts, height=height, remove_wall=remove.get("walls"))
    # on crée sol(s) et plafond(s)
    # si l'utilisateur fournit une liste de hauteurs, il doit définir le plafond dans le yaml
    # s'il ne l'a pas fait, on produit un plafond plat
    room_height = max(height) if isinstance(height, list) else height
    all_floors, all_roofs = create_floors_roofs(
        floors=[Face3D(pts)] if len(floors)==0 else floors,
        height=room_height,
        roofs=roofs,
        remove_floor=remove.get("floors"),
        remove_roof=remove.get("roofs")
    )

    if use_polyface:
        polyface = Polyface3D.from_faces(
            [*all_floors.values(), *walls.values(), *all_roofs.values()],
            tolerance = TOLERANCE
        )
        output_room = Room.from_polyface3d(
            identifier=identifier,
            polyface=polyface
        )
    else:
        hb_faces = []
        for key, f3d in all_floors.items():
            hb = Face(
                identifier=f'{identifier}_{FLOOR}_{key}',
                geometry=f3d
            )
            hb_faces.append(hb)
        for key, f3d in all_roofs.items():
            hb = Face(
                identifier=f'{identifier}_{ROOF}_{key}',
                geometry=f3d
            )
            hb_faces.append(hb)
        for key, f3d in walls.items():
            hb = Face(
                identifier=f'{identifier}_{WALL}_{key}',
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
    face_type: str
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
    LOGGER.debug("wall_plane.o is %s", wall_plane.o)
    LOGGER.debug("wall_plane.x is %s", wall_plane.x)
    LOGGER.debug("wall_plane.y is %s", wall_plane.y)


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
    construction: WindowConstruction | OpaqueConstruction | None,
    label: str,
    aperture_type: str
):
    """create the aperture given its geometry"""
    identifier = f"{face.identifier}_{label}"
    if aperture_type == "door" :
        aperture = Door(
            identifier=identifier,
            geometry=geometry,
            is_glass=isinstance(construction, WindowConstruction)
        )
    else:
        aperture = Aperture(
            identifier=identifier,
            geometry=geometry
        )
    if construction is not None:
        aperture.properties.energy.construction = construction
    if aperture_type == "door":
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
        self.set_u_v_bounds()

    def set_u_v_bounds(self):
        """set u and v bounds presuming face is fixed"""
        self.u_min, self.u_max, v_min, v_max = get_face_u_v_bounds(self.face)
        if self.face.geometry.plane.y.z < 0:
            self.v = v_max - self.dims.height - self.dims.sill_height
        else:
            self.v = v_min + self.dims.sill_height

    def _add(
        self,
        origin: Point3D,
        construction: WindowConstruction | None,
        label: str,
        aperture_type: str = "aperture",
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
        construction: WindowConstruction | None,
        aperture_type: str = "aperture",
        ecart: float | None = None,
        count: int = 1
    ):
        """ajoute les ouvertures symétriquement par rapport au centre"""
        translate = self.dims.width if not ecart else self.dims.width + ecart
        start_u = ( self.u_max + self.u_min - count * translate ) / 2
        for i in range(count):
            u = start_u + i * translate
            origin = local_to_world(self.face, u, self.v)
            LOGGER.debug("i %s > plane origin: %s", i, origin)
            self._add(
                origin=origin,
                construction=construction,
                label=f"{DOOR}_{i}" if aperture_type=="door" else f"{WIN}_{i}",
                aperture_type=aperture_type
            )

    def add_from_border(
        self,
        construction: WindowConstruction | None,
        aperture_type: str = "aperture",
        ecart: float | None = None,
        count: int = 1
    ):
        """ajoute les ouvertures depuis un bord"""
        if not ecart:
            spacing = (self.u_max - self.u_min - count * self.dims.width) / (count + 1)
        else:
            spacing = ecart
        LOGGER.info("%s >>>> aperture spacing is %.2f m", self.face.identifier, spacing)
        for i in range(count):
            u = self.u_min + i * (self.dims.width + spacing) + spacing
            origin = local_to_world(self.face, u, self.v)
            LOGGER.debug("i %s > plane origin: %s", i, origin)
            self._add(
                origin=origin,
                construction=construction,
                label=f"{DOOR}_{i}" if aperture_type=="door" else f"{WIN}_{i}",
                aperture_type=aperture_type
            )

def join_surface(room1: Room, pattern1: str, room2: Room, pattern2: str):
    """Add boundary condition between two adjacent faces."""
    face1 = get_from_pattern(room1, pattern1)
    face2 = get_from_pattern(room2, pattern2)
    bdo = (face1.identifier, face2.identifier)
    face2.boundary_condition = Surface(boundary_condition_objects=bdo)
    bdo = (face2.identifier, face1.identifier)
    face1.boundary_condition = Surface(boundary_condition_objects=bdo)


def dispatch_apertures(
    *,
    apertures: dict[str, list],
    manager: ApertureManager,
    destination_faces: list[Face3D]
):
    """dispatch apertures on destination faces
    numbers is a mandatory key in the apertures dict
    """
    ap_numbers = apertures["numbers"]
    ap_widths = apertures["widths"] if "widths" in apertures else []
    ap_heights = apertures["heights"] if "heights" in apertures else []
    ap_sill_heights = apertures["sill_heights"] if "sill_heights" in apertures else []
    ap_constructions = apertures["constructions"] if "constructions" in apertures else []
    ap_types = apertures["types"] if "types" in apertures else []
    for destination_face in destination_faces:
        j = int(destination_face.identifier.split("_")[-1])
        try:
            ap_count = ap_numbers[j]
        except IndexError:
            continue
        if ap_count == 0:
            LOGGER.warning("skipping aperture on %s", destination_face)
            continue
        try:
            ap_width = ap_widths[j]
        except IndexError:
            ap_width = apertures.get("width", 1.2)
        try:
            ap_height = ap_heights[j]
        except IndexError:
            ap_height = apertures.get("height", 1.3)
        try:
            ap_sill_height = ap_sill_heights[j]
        except IndexError:
            ap_sill_height = apertures.get("sill_height", 1)
        try:
            ap_type = ap_types[j]
        except IndexError:
            ap_type = apertures.get("type", "aperture")
        manager.fix_dim(
            width = ap_width,
            height = ap_height,
            sill_height = ap_sill_height
        )
        try:
            ap_construction_name = ap_constructions[j]
        except IndexError:
            ap_construction_name = apertures.get("construction")
        ap_construction=CONSTLIB.get(ap_construction_name)
        manager.face = destination_face
        manager.set_u_v_bounds()
        manager.add_from_border(
            construction=ap_construction,
            count=ap_count,
            aperture_type=ap_type
        )
