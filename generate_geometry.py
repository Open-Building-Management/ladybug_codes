"""Building generator
Honeybee utilise un repère standard :
X+ = Est
Y+ = Nord
Z+ = Haut
Si on ne fait aucune rotation :
front = ouest
back  = est
left  = nord
right = sud
"""
import logging

from ladybug_geometry.geometry3d import Point3D, Face3D

from honeybee.boundarycondition import Ground, Outdoors
from honeybee.door import Door
from honeybee.face import Face, Wall, RoofCeiling
from honeybee.facetype import Floor
from honeybee.model import Model

from honeybee_energy.writer import model_to_idf

from idfhub.helpers.common import get_logger, view_boundaries

from idfhub.helpers.material import (
    wall_osb, wall_parpaing,
    floor_internal,
    window_pvc, simple_glass_wall
)
from idfhub.helpers.geometry import (
    box_room, complex_room,
    get, get_from_pattern,
    ApertureManager, add_aperture,
    join_surface
)

get_logger("idfhub", level=logging.INFO)

BUILDING_NAME = "batiment_600m2"

# Building global params
ADMIN_WIDTH = 37.0
ADMIN_DEPTH = 11.0
LEVEL_HEIGHT = 3.0

print("-> Creating Honeybee Rooms.....")

ss = box_room("SS", origin=Point3D(0,0,- LEVEL_HEIGHT))
rplus1 = box_room("RPLUS1", origin=Point3D(0,0, LEVEL_HEIGHT))

# salle de réunion
meeting_pts = [
    Point3D(-4, -4, 0),
    Point3D(-4, 11, 0),
    Point3D(-4, 12, 0),
    Point3D(-12, 4, 0)
]

meeting = complex_room(
    meeting_pts,
    height=LEVEL_HEIGHT,
    identifier="MEETING"
)

# jonction
jonction_pts:list[Point3D] = [
    Point3D(4, 0, 0),
    Point3D(0, 0, 0),
    Point3D(0, ADMIN_DEPTH, 0),
    Point3D(-4,ADMIN_DEPTH, 0),
    Point3D(-4,-4,0),
    Point3D(-4,-8,0),
    Point3D(0,-8, 0),
    Point3D(0,-4, 0),
    Point3D(4,-4, 0)
]

rdc_admin_pts = [
    Point3D(ADMIN_WIDTH, 0, 0),
    Point3D(ADMIN_WIDTH, ADMIN_DEPTH, 0),
    Point3D(0, ADMIN_DEPTH, 0),
    Point3D(0, 0, 0)
]

rdc_pts = [
    rdc_admin_pts[0],
    rdc_admin_pts[1],
    rdc_admin_pts[2],
    jonction_pts[3],
    jonction_pts[4],
    jonction_pts[5],
    jonction_pts[6],
    jonction_pts[7],
    jonction_pts[8],
    jonction_pts[0]
]

rdc = complex_room(
    rdc_pts,
    height=LEVEL_HEIGHT,
    identifier="RDC",
    floors=[rdc_admin_pts, jonction_pts],
    use_polyface=False
)

# matériaux
face: Face
for face in ss.faces:
    if isinstance(face.type, Floor):
        face.boundary_condition = Ground()
    if isinstance(face.type, Wall):
        face.properties.energy.construction = wall_parpaing
    if isinstance(face.type, RoofCeiling):
        face.properties.energy.construction = floor_internal
for niveau in [rplus1]:
    for face in niveau.faces:
        if isinstance(face.type, Floor):
            face.properties.energy.construction = floor_internal
        if isinstance(face.type, Wall):
            face.properties.energy.construction = wall_osb
        if isinstance(face.type, RoofCeiling):
            if face.identifier.startswith("RDC"):
                face.properties.energy.construction = floor_internal

for room in meeting, rdc:
    for face in room.faces:
        if isinstance(face.type, Wall):
            face.properties.energy.construction = wall_osb

get_from_pattern(rdc, "floor0").properties.energy.construction = floor_internal
get_from_pattern(rdc, "roof0").properties.energy.construction = floor_internal

# boundary conditions
for face in ss.faces:
    if isinstance(face.type, Wall):
        # sous-sol semi-enterré
        if face.identifier.endswith('Front'):
            face.boundary_condition = Outdoors()
        else:
            face.boundary_condition = Ground()

join_surface(rdc, "wall3", meeting, "Face1")
join_surface(ss, "Top", rdc, "floor0")
join_surface(rdc, "roof0", rplus1, "Bottom")

# ouvertures
apm = ApertureManager(rplus1)
for pattern in "front", "back":
    apm.fix_face(pattern)
    apm.add_from_border(window_pvc, count=24)
for pattern in "left", "right":
    apm.fix_face(pattern)
    apm.add_from_border(window_pvc, count=6)

apm.fix_dim(3.8,2.9,0)
for pattern in ["wall8", "wall6", "wall4"]:
    apm.set(rdc, pattern, use_orientation=False)
    apm.add_from_center(simple_glass_wall, count=1)
apm.fix_face("wall7", use_orientation=False)
apm.add_from_center(simple_glass_wall, aperture_type=Door, count=1)
apm.fix_dim(1.2,1.3,1)
apm.fix_face("wall9", use_orientation=False)
apm.add_from_border(window_pvc, count=22)
apm.fix_face("wall0", use_orientation=False)
apm.add_from_border(window_pvc, count=6)
apm.fix_face("wall1", use_orientation=False)
apm.add_from_border(window_pvc, count=24)
apm.fix_dim(2,2,0)
apm.fix_face("wall2", use_orientation=False)
apm.add_from_center(simple_glass_wall, aperture_type=Door, count=1)

apm.fix_dim(4,2,0)
for pattern in ["Face3", "Face4"]:
    apm.set(meeting, pattern, use_orientation=False)
    apm.add_from_center(simple_glass_wall, aperture_type=Door, count=1)


geom = Face3D([
    Point3D(10+1, ADMIN_DEPTH, -LEVEL_HEIGHT),
    Point3D(10, ADMIN_DEPTH, -LEVEL_HEIGHT),
    Point3D(10, ADMIN_DEPTH, 2-LEVEL_HEIGHT),
    Point3D(10+1, ADMIN_DEPTH, 2-LEVEL_HEIGHT)
])
add_aperture(
    get(ss, "front"),
    geometry=geom,
    construction=simple_glass_wall,
    label="porte_sous_sol",
    aperture_type=Door,
)

bat = [ss, rdc, rplus1, meeting]
model = Model(BUILDING_NAME, bat)

view_boundaries(bat)

with open(f"{BUILDING_NAME}.idf", "w", encoding="utf-8") as f:
    f.write(model_to_idf(model))
