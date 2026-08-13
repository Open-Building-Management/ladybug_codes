A site can be composed of as many buildings as required

Each building is composed of different levels

mandatory level key | description
--|--
`height` or `heights` | height of walls, for example `height: 7`. You may create walls with different heights using the `heights` key and a list of heights. When defining heights, you also have to define roofs, otherwise the roof will be a horizontal plane. Using the list blocks defined in the blocks section, it is easy to define a ceiling/roof which is not a simple translation of the floor
`walls` | list of points defining the level floor. The first wall bottom line is between the first and second point, and so on... 

optional level key | description
--|--
`altitude` | altitude of the floor, for example `altitude: &lab_alt -3` which defines a `lab_alt` yml anchor

A point is a list of 3 coordinates : [X, Y, Z]

To define a coordinate, you can use :
- number/float
- yml anchor, for example `*lab_alt`
- simple formula, for example `"37+45"` or `"altitude+height"`

# reusable blocks

At the yaml root, a `blocks` key permits :
- to define reusable lists of points
- to address numeric variables (`d0` to `d8`, `z0`, `h0` to `h4`) in the blocks section, that can be used in zone subsections (`floors`, `roofs`, `walls`, `elements`) without the need of adding an anchor

```
blocks:
  ss1_alt: &ss1_alt -4
  rdc_alt: &rdc_alt 0
  d0: 19
  d1: 3
  d2: 5
  d3: 4
  d4: 4
  d5: 3
  d6: 7 # début cage
  d7: 1 # largeur cage
  d8: 2 # profondeur cage
  ss1_floor:
    - ["d0", 0, *ss1_alt]
    - ["d0", "d3+d4+d5", *ss1_alt]
    - ["-d1-d2",  "d3+d4+d5", *ss1_alt]
    - ["-d1-d2",  0, *ss1_alt]
  rdc_cage:
    - ["d6", 0, *rdc_alt]
    - ["d6", "d8", *rdc_alt]
    - ["d6+d7", "d8", *rdc_alt]
    - ["d6+d7", 0, *rdc_alt]
  caves:
    - [0, 0, *rdc_alt]
    - rdc_cage
    - ["d0", 0, *rdc_alt]
    - ["d0", "d3+d4", *rdc_alt]
    - [0, "d3+d4", *rdc_alt]
```

In zone subsections, you have to specify `use_blocks_vars: 1` when using reusable blocks or vars

```
use_blocks_vars: 1
walls:
  - ["d0", 0, *ss2_alt]
  - ["d0", "d3+d4+d5", *ss2_alt]
  - ["-d1-d2",  "d3+d4+d5", *ss2_alt]
  - ["-d1-d2",  0, *ss2_alt]
```

for list blocks :
```
use_blocks_vars: 1
floors: [ss1_floor]
roofs: [annexe, cour_drouet, car_path, caves, rdc_cage]
walls: [ss1_floor]
```

# constructions

A `constructions` key may be added to define a dictionnary with construction for `walls`, `roofs` and/or `floors`.

You may specify a default construction for a zone and customize only some walls
```
constructions:
  default: townhouse_basement
  roofs:
    4: air_boundary
```

# dispatch apertures

2 methods :

1) use a `apertures`, `doors` and/or`vasistas` key

The value is a dict : 
- key = wall number, 
- value = list `[nb_apertures, width, height, sill_height]`

You may also add a construction type as the last (string) element of the list
```
doors:
  1: [1, 2, 2.5, 0, window_pvc]
  2: [1, 1, 2.5, 0, window_pvc]
apertures:
  4: [1, 1.3, 1.5, 1]
  5: [1, 1.3, 1.5, 1]
  9: [1, 1.3, 1.5, 1]
```

2) use a `numbers` key
value = list `[number of apertures for each wall - 0 if no aperture]`.

Other non mandatory keys : `widths`, `heights`, `sill_heights`, `constructions` (none if no custom construction), `types` (aperture, door or none).

You may also use singular if all elements are the same, for example `width: 4` or `construction: townhouse_basement`

aperture key | description
--|--
`numbers` | list of the numbers of windows on each wall. For a wall without any window, use `0`
`width` or `widths` | float or list of floats
`height` or `heights` | float or list of floats
`sill_height` or `sill_heights` | float or list of floats
`construction` or `constructions` | string or list of strings.
`type` or `types` | string or list of strings. For a window, use `aperture`, for a door, use `door`.

When using `constructions` or `types`, if you have a wall without any window, use none, dont skip !

The generator relies on honeybee default constructions when nothing or none is mentionned.

All lists lengths should be the same. If not, the generator will consider they all start at the same index, ie 0.

The same configuration expressed with the second method is far more verbose :
```
apertures:
  numbers: [0, 1, 1, 0, 1, 1, 0, 0, 0, 1]
  widths: [0, 2, 1, 0, 1.3, 1.3, 0, 0, 0, 1.3]
  heights: [0, 2.5, 2.5, 0, 1.5, 1.5, 0, 0, 0, 1.5]
  sill_heights: [0, 0, 0, 0, 1, 1, 0, 0, 0, 1]
  constructions:
    - none
    - window_pvc
    - window_pvc
  types:
    - none
    - door
    - door
    - none
    - aperture
    - aperture
    - none
    - aperture
    - none
    - aperture
``` 

# single vasistas & triangular surface
You may add a single vasistas on a triangular surface (portion of a roof) using vertices numbers
```
vasistas:
  1: [3, 1.2, 1.3, 2]
  4:
    base_start: 0
    base_end: 2
    apex: 1
    width: 1.2
    height: 1
    sill_height: 1
```

# extras

You may also : 

- define specific elements, such as an isolated door, with an `elements` key.
- delete a wall between two adjacent zones (`remove_wall` key)
- introduce air_boundary to start using ZoneCrossMixing

