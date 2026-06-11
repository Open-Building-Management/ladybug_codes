A site can be composed of as many buildings as required

Each building is composed of different levels

mandatory level key | description
--|--
`height` | height of walls, for example `height: 7`
`altitude` | altitude of the floor, for example `altitude: &lab_alt -3` which defines a `lab_alt` yml anchor
`walls` | list of points defining the level floor. The first wall bottom line is between the first and second point, and so on... 

A point is a list of 3 coordinates : [X, Y, Z]

To define a coordinate, you can use :
- number/float
- yml anchor, for example `*lab_alt`
- simple formula, for example `"37+45"` or `"altitude+height"`

A `constructions` key may be added to define a dictionnary with construction for `walls`, `roofs` and/or `floors`.

Apertures can be added as an option

aperture key | description
--|--
`numbers` | list of the numbers of windows on each wall. For a wall without any window, use `0`
`width` or `widths` | float or list of floats
`height` or `heights` | float or list of floats
`sill_height` or `sill_heights` | float or list of floats
`construction` or `constructions` | string or list of strings.
`type` or `types` | string or list of strings. For a window, use `aperture`, for a door, use `door`.

The generator relies on honeybee default constructions when nothing is mentionned.

When using `constructions` or `types`, if you have a wall without any window, use none, dont skip !

All lists lengths must be the same.

You may define specific elements, such as an isolated door, with an `elements` key.

At the yaml root, a `blocks` key permit to define reusable lists of points as strings.

