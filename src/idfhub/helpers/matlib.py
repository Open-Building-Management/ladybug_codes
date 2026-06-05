"""library of constructions"""

from .material import (
    wall_osb, wall_parpaing,
    floor_internal,
    window_pvc, simple_glass_wall
)

CONSTLIB = {
    "wall_osb": wall_osb,
    "wall_parpaing": wall_parpaing,
    "floor_internal": floor_internal,
    "window_pvc": window_pvc,
    "simple_glass_wall": simple_glass_wall
}
