###########################################################################
# License regarding the Viridis, Magma, Plasma and Inferno color maps:
# New matplotlib colormaps by Nathaniel J. Smith, Stefan van der Walt,
# and (in the case of viridis) Eric Firing.
#
# This file and the colormaps in it are released under the CC0 license /
# public domain dedication. We would appreciate credit if you use or
# redistribute these colormaps, but do not impose any legal restrictions.
#
# To the extent possible under law, the persons who associated CC0 with
# mpl-colormaps have waived all copyright and related or neighboring rights
# to mpl-colormaps.
#
# You should have received a copy of the CC0 legalcode along with this
# work.  If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.
###########################################################################
# This product includes color specifications and designs developed by
# Cynthia Brewer (http://colorbrewer2.org/).  The Brewer colormaps are
# licensed under the Apache v2 license. You may obtain a copy of the
# License at http://www.apache.org/licenses/LICENSE-2.0
###########################################################################
""" Provide a collection of palettes for color mapping.

Palettes are simple plain Python lists of (hex) RGB colors. This module
containts the following sets of palettes:

* All Brewer palettes
* Magma
* Inferno
* Plasma
* Viridis

Every pre-built palette is available as a module attributes, e.g.
``bokeh.palettes.YlGn3`` or ``bokeh.palettes.Viridis256``. The name of every
all pre-built palettes can be found in the ``__palettes__`` module attribute.

There are functions :func:`~bokeh.palettes.magma`,
:func:`~bokeh.palettes.inferno`, :func:`~bokeh.palettes.plasma`,
:func:`~bokeh.palettes.viridis` that can generate lists of colors of arbitrary
size from those palettes.

The Brewer palettes are also collected and grouped by name in a
``brewer`` dictionary, e.g.: ``brewer['Spectral'][6]``

Finally, all "small" palettes (i.e. excluding the 256 color ones) are
collected and grouped similarly in a ``small_palettes`` attribute.
The complete contents of ``small_palettes`` is show below.

----

.. bokeh-palette:: unused.for.now

"""
import math
import numpy as np

YlGn3       = ["#31a354", "#addd8e", "#f7fcb9"]
YlGn4       = ["#238443", "#78c679", "#c2e699", "#ffffcc"]
YlGn5       = ["#006837", "#31a354", "#78c679", "#c2e699", "#ffffcc"]
YlGn6       = ["#006837", "#31a354", "#78c679", "#addd8e", "#d9f0a3", "#ffffcc"]
YlGn7       = ["#005a32", "#238443", "#41ab5d", "#78c679", "#addd8e", "#d9f0a3", "#ffffcc"]
YlGn8       = ["#005a32", "#238443", "#41ab5d", "#78c679", "#addd8e", "#d9f0a3", "#f7fcb9", "#ffffe5"]
YlGn9       = ["#004529", "#006837", "#238443", "#41ab5d", "#78c679", "#addd8e", "#d9f0a3", "#f7fcb9", "#ffffe5"]

YlGnBu3     = ["#2c7fb8", "#7fcdbb", "#edf8b1"]
YlGnBu4     = ["#225ea8", "#41b6c4", "#a1dab4", "#ffffcc"]
YlGnBu5     = ["#253494", "#2c7fb8", "#41b6c4", "#a1dab4", "#ffffcc"]
YlGnBu6     = ["#253494", "#2c7fb8", "#41b6c4", "#7fcdbb", "#c7e9b4", "#ffffcc"]
YlGnBu7     = ["#0c2c84", "#225ea8", "#1d91c0", "#41b6c4", "#7fcdbb", "#c7e9b4", "#ffffcc"]
YlGnBu8     = ["#0c2c84", "#225ea8", "#1d91c0", "#41b6c4", "#7fcdbb", "#c7e9b4", "#edf8b1", "#ffffd9"]
YlGnBu9     = ["#081d58", "#253494", "#225ea8", "#1d91c0", "#41b6c4", "#7fcdbb", "#c7e9b4", "#edf8b1", "#ffffd9"]

GnBu3       = ["#43a2ca", "#a8ddb5", "#e0f3db"]
GnBu4       = ["#2b8cbe", "#7bccc4", "#bae4bc", "#f0f9e8"]
GnBu5       = ["#0868ac", "#43a2ca", "#7bccc4", "#bae4bc", "#f0f9e8"]
GnBu6       = ["#0868ac", "#43a2ca", "#7bccc4", "#a8ddb5", "#ccebc5", "#f0f9e8"]
GnBu7       = ["#08589e", "#2b8cbe", "#4eb3d3", "#7bccc4", "#a8ddb5", "#ccebc5", "#f0f9e8"]
GnBu8       = ["#08589e", "#2b8cbe", "#4eb3d3", "#7bccc4", "#a8ddb5", "#ccebc5", "#e0f3db", "#f7fcf0"]
GnBu9       = ["#084081", "#0868ac", "#2b8cbe", "#4eb3d3", "#7bccc4", "#a8ddb5", "#ccebc5", "#e0f3db", "#f7fcf0"]

BuGn3       = ["#2ca25f", "#99d8c9", "#e5f5f9"]
BuGn4       = ["#238b45", "#66c2a4", "#b2e2e2", "#edf8fb"]
BuGn5       = ["#006d2c", "#2ca25f", "#66c2a4", "#b2e2e2", "#edf8fb"]
BuGn6       = ["#006d2c", "#2ca25f", "#66c2a4", "#99d8c9", "#ccece6", "#edf8fb"]
BuGn7       = ["#005824", "#238b45", "#41ae76", "#66c2a4", "#99d8c9", "#ccece6", "#edf8fb"]
BuGn8       = ["#005824", "#238b45", "#41ae76", "#66c2a4", "#99d8c9", "#ccece6", "#e5f5f9", "#f7fcfd"]
BuGn9       = ["#00441b", "#006d2c", "#238b45", "#41ae76", "#66c2a4", "#99d8c9", "#ccece6", "#e5f5f9", "#f7fcfd"]

PuBuGn3     = ["#1c9099", "#a6bddb", "#ece2f0"]
PuBuGn4     = ["#02818a", "#67a9cf", "#bdc9e1", "#f6eff7"]
PuBuGn5     = ["#016c59", "#1c9099", "#67a9cf", "#bdc9e1", "#f6eff7"]
PuBuGn6     = ["#016c59", "#1c9099", "#67a9cf", "#a6bddb", "#d0d1e6", "#f6eff7"]
PuBuGn7     = ["#016450", "#02818a", "#3690c0", "#67a9cf", "#a6bddb", "#d0d1e6", "#f6eff7"]
PuBuGn8     = ["#016450", "#02818a", "#3690c0", "#67a9cf", "#a6bddb", "#d0d1e6", "#ece2f0", "#fff7fb"]
PuBuGn9     = ["#014636", "#016c59", "#02818a", "#3690c0", "#67a9cf", "#a6bddb", "#d0d1e6", "#ece2f0", "#fff7fb"]

PuBu3       = ["#2b8cbe", "#a6bddb", "#ece7f2"]
PuBu4       = ["#0570b0", "#74a9cf", "#bdc9e1", "#f1eef6"]
PuBu5       = ["#045a8d", "#2b8cbe", "#74a9cf", "#bdc9e1", "#f1eef6"]
PuBu6       = ["#045a8d", "#2b8cbe", "#74a9cf", "#a6bddb", "#d0d1e6", "#f1eef6"]
PuBu7       = ["#034e7b", "#0570b0", "#3690c0", "#74a9cf", "#a6bddb", "#d0d1e6", "#f1eef6"]
PuBu8       = ["#034e7b", "#0570b0", "#3690c0", "#74a9cf", "#a6bddb", "#d0d1e6", "#ece7f2", "#fff7fb"]
PuBu9       = ["#023858", "#045a8d", "#0570b0", "#3690c0", "#74a9cf", "#a6bddb", "#d0d1e6", "#ece7f2", "#fff7fb"]

BuPu3       = ["#8856a7", "#9ebcda", "#e0ecf4"]
BuPu4       = ["#88419d", "#8c96c6", "#b3cde3", "#edf8fb"]
BuPu5       = ["#810f7c", "#8856a7", "#8c96c6", "#b3cde3", "#edf8fb"]
BuPu6       = ["#810f7c", "#8856a7", "#8c96c6", "#9ebcda", "#bfd3e6", "#edf8fb"]
BuPu7       = ["#6e016b", "#88419d", "#8c6bb1", "#8c96c6", "#9ebcda", "#bfd3e6", "#edf8fb"]
BuPu8       = ["#6e016b", "#88419d", "#8c6bb1", "#8c96c6", "#9ebcda", "#bfd3e6", "#e0ecf4", "#f7fcfd"]
BuPu9       = ["#4d004b", "#810f7c", "#88419d", "#8c6bb1", "#8c96c6", "#9ebcda", "#bfd3e6", "#e0ecf4", "#f7fcfd"]

RdPu3       = ["#c51b8a", "#fa9fb5", "#fde0dd"]
RdPu4       = ["#ae017e", "#f768a1", "#fbb4b9", "#feebe2"]
RdPu5       = ["#7a0177", "#c51b8a", "#f768a1", "#fbb4b9", "#feebe2"]
RdPu6       = ["#7a0177", "#c51b8a", "#f768a1", "#fa9fb5", "#fcc5c0", "#feebe2"]
RdPu7       = ["#7a0177", "#ae017e", "#dd3497", "#f768a1", "#fa9fb5", "#fcc5c0", "#feebe2"]
RdPu8       = ["#7a0177", "#ae017e", "#dd3497", "#f768a1", "#fa9fb5", "#fcc5c0", "#fde0dd", "#fff7f3"]
RdPu9       = ["#49006a", "#7a0177", "#ae017e", "#dd3497", "#f768a1", "#fa9fb5", "#fcc5c0", "#fde0dd", "#fff7f3"]

PuRd3       = ["#dd1c77", "#c994c7", "#e7e1ef"]
PuRd4       = ["#ce1256", "#df65b0", "#d7b5d8", "#f1eef6"]
PuRd5       = ["#980043", "#dd1c77", "#df65b0", "#d7b5d8", "#f1eef6"]
PuRd6       = ["#980043", "#dd1c77", "#df65b0", "#c994c7", "#d4b9da", "#f1eef6"]
PuRd7       = ["#91003f", "#ce1256", "#e7298a", "#df65b0", "#c994c7", "#d4b9da", "#f1eef6"]
PuRd8       = ["#91003f", "#ce1256", "#e7298a", "#df65b0", "#c994c7", "#d4b9da", "#e7e1ef", "#f7f4f9"]
PuRd9       = ["#67001f", "#980043", "#ce1256", "#e7298a", "#df65b0", "#c994c7", "#d4b9da", "#e7e1ef", "#f7f4f9"]

OrRd3       = ["#e34a33", "#fdbb84", "#fee8c8"]
OrRd4       = ["#d7301f", "#fc8d59", "#fdcc8a", "#fef0d9"]
OrRd5       = ["#b30000", "#e34a33", "#fc8d59", "#fdcc8a", "#fef0d9"]
OrRd6       = ["#b30000", "#e34a33", "#fc8d59", "#fdbb84", "#fdd49e", "#fef0d9"]
OrRd7       = ["#990000", "#d7301f", "#ef6548", "#fc8d59", "#fdbb84", "#fdd49e", "#fef0d9"]
OrRd8       = ["#990000", "#d7301f", "#ef6548", "#fc8d59", "#fdbb84", "#fdd49e", "#fee8c8", "#fff7ec"]
OrRd9       = ["#7f0000", "#b30000", "#d7301f", "#ef6548", "#fc8d59", "#fdbb84", "#fdd49e", "#fee8c8", "#fff7ec"]

YlOrRd3     = ["#f03b20", "#feb24c", "#ffeda0"]
YlOrRd4     = ["#e31a1c", "#fd8d3c", "#fecc5c", "#ffffb2"]
YlOrRd5     = ["#bd0026", "#f03b20", "#fd8d3c", "#fecc5c", "#ffffb2"]
YlOrRd6     = ["#bd0026", "#f03b20", "#fd8d3c", "#feb24c", "#fed976", "#ffffb2"]
YlOrRd7     = ["#b10026", "#e31a1c", "#fc4e2a", "#fd8d3c", "#feb24c", "#fed976", "#ffffb2"]
YlOrRd8     = ["#b10026", "#e31a1c", "#fc4e2a", "#fd8d3c", "#feb24c", "#fed976", "#ffeda0", "#ffffcc"]
YlOrRd9     = ["#800026", "#bd0026", "#e31a1c", "#fc4e2a", "#fd8d3c", "#feb24c", "#fed976", "#ffeda0", "#ffffcc"]

YlOrBr3     = ["#d95f0e", "#fec44f", "#fff7bc"]
YlOrBr4     = ["#cc4c02", "#fe9929", "#fed98e", "#ffffd4"]
YlOrBr5     = ["#993404", "#d95f0e", "#fe9929", "#fed98e", "#ffffd4"]
YlOrBr6     = ["#993404", "#d95f0e", "#fe9929", "#fec44f", "#fee391", "#ffffd4"]
YlOrBr7     = ["#8c2d04", "#cc4c02", "#ec7014", "#fe9929", "#fec44f", "#fee391", "#ffffd4"]
YlOrBr8     = ["#8c2d04", "#cc4c02", "#ec7014", "#fe9929", "#fec44f", "#fee391", "#fff7bc", "#ffffe5"]
YlOrBr9     = ["#662506", "#993404", "#cc4c02", "#ec7014", "#fe9929", "#fec44f", "#fee391", "#fff7bc", "#ffffe5"]

Purples3    = ["#756bb1", "#bcbddc", "#efedf5"]
Purples4    = ["#6a51a3", "#9e9ac8", "#cbc9e2", "#f2f0f7"]
Purples5    = ["#54278f", "#756bb1", "#9e9ac8", "#cbc9e2", "#f2f0f7"]
Purples6    = ["#54278f", "#756bb1", "#9e9ac8", "#bcbddc", "#dadaeb", "#f2f0f7"]
Purples7    = ["#4a1486", "#6a51a3", "#807dba", "#9e9ac8", "#bcbddc", "#dadaeb", "#f2f0f7"]
Purples8    = ["#4a1486", "#6a51a3", "#807dba", "#9e9ac8", "#bcbddc", "#dadaeb", "#efedf5", "#fcfbfd"]
Purples9    = ["#3f007d", "#54278f", "#6a51a3", "#807dba", "#9e9ac8", "#bcbddc", "#dadaeb", "#efedf5", "#fcfbfd"]

Blues3      = ["#3182bd", "#9ecae1", "#deebf7"]
Blues4      = ["#2171b5", "#6baed6", "#bdd7e7", "#eff3ff"]
Blues5      = ["#08519c", "#3182bd", "#6baed6", "#bdd7e7", "#eff3ff"]
Blues6      = ["#08519c", "#3182bd", "#6baed6", "#9ecae1", "#c6dbef", "#eff3ff"]
Blues7      = ["#084594", "#2171b5", "#4292c6", "#6baed6", "#9ecae1", "#c6dbef", "#eff3ff"]
Blues8      = ["#084594", "#2171b5", "#4292c6", "#6baed6", "#9ecae1", "#c6dbef", "#deebf7", "#f7fbff"]
Blues9      = ["#08306b", "#08519c", "#2171b5", "#4292c6", "#6baed6", "#9ecae1", "#c6dbef", "#deebf7", "#f7fbff"]

Greens3     = ["#31a354", "#a1d99b", "#e5f5e0"]
Greens4     = ["#238b45", "#74c476", "#bae4b3", "#edf8e9"]
Greens5     = ["#006d2c", "#31a354", "#74c476", "#bae4b3", "#edf8e9"]
Greens6     = ["#006d2c", "#31a354", "#74c476", "#a1d99b", "#c7e9c0", "#edf8e9"]
Greens7     = ["#005a32", "#238b45", "#41ab5d", "#74c476", "#a1d99b", "#c7e9c0", "#edf8e9"]
Greens8     = ["#005a32", "#238b45", "#41ab5d", "#74c476", "#a1d99b", "#c7e9c0", "#e5f5e0", "#f7fcf5"]
Greens9     = ["#00441b", "#006d2c", "#238b45", "#41ab5d", "#74c476", "#a1d99b", "#c7e9c0", "#e5f5e0", "#f7fcf5"]

Oranges3    = ["#e6550d", "#fdae6b", "#fee6ce"]
Oranges4    = ["#d94701", "#fd8d3c", "#fdbe85", "#feedde"]
Oranges5    = ["#a63603", "#e6550d", "#fd8d3c", "#fdbe85", "#feedde"]
Oranges6    = ["#a63603", "#e6550d", "#fd8d3c", "#fdae6b", "#fdd0a2", "#feedde"]
Oranges7    = ["#8c2d04", "#d94801", "#f16913", "#fd8d3c", "#fdae6b", "#fdd0a2", "#feedde"]
Oranges8    = ["#8c2d04", "#d94801", "#f16913", "#fd8d3c", "#fdae6b", "#fdd0a2", "#fee6ce", "#fff5eb"]
Oranges9    = ["#7f2704", "#a63603", "#d94801", "#f16913", "#fd8d3c", "#fdae6b", "#fdd0a2", "#fee6ce", "#fff5eb"]

Reds3       = ["#de2d26", "#fc9272", "#fee0d2"]
Reds4       = ["#cb181d", "#fb6a4a", "#fcae91", "#fee5d9"]
Reds5       = ["#a50f15", "#de2d26", "#fb6a4a", "#fcae91", "#fee5d9"]
Reds6       = ["#a50f15", "#de2d26", "#fb6a4a", "#fc9272", "#fcbba1", "#fee5d9"]
Reds7       = ["#99000d", "#cb181d", "#ef3b2c", "#fb6a4a", "#fc9272", "#fcbba1", "#fee5d9"]
Reds8       = ["#99000d", "#cb181d", "#ef3b2c", "#fb6a4a", "#fc9272", "#fcbba1", "#fee0d2", "#fff5f0"]
Reds9       = ["#67000d", "#a50f15", "#cb181d", "#ef3b2c", "#fb6a4a", "#fc9272", "#fcbba1", "#fee0d2", "#fff5f0"]

Greys3      = ["#636363", "#bdbdbd", "#f0f0f0"]
Greys4      = ["#525252", "#969696", "#cccccc", "#f7f7f7"]
Greys5      = ["#252525", "#636363", "#969696", "#cccccc", "#f7f7f7"]
Greys6      = ["#252525", "#636363", "#969696", "#bdbdbd", "#d9d9d9", "#f7f7f7"]
Greys7      = ["#252525", "#525252", "#737373", "#969696", "#bdbdbd", "#d9d9d9", "#f7f7f7"]
Greys8      = ["#252525", "#525252", "#737373", "#969696", "#bdbdbd", "#d9d9d9", "#f0f0f0", "#ffffff"]
Greys9      = ["#000000", "#252525", "#525252", "#737373", "#969696", "#bdbdbd", "#d9d9d9", "#f0f0f0", "#ffffff"]
Greys10     = ['#000000', '#1c1c1c', '#383838', '#555555', '#717171', '#8d8d8d', '#aaaaaa', '#c6c6c6', '#e2e2e2', '#ffffff']
Greys11     = ['#000000', '#191919', '#333333', '#4c4c4c', '#666666', '#7f7f7f', '#999999', '#b2b2b2', '#cccccc', '#e5e5e5', '#ffffff']
Greys256    = [
    "#000000", "#010101", "#020202", "#030303", "#040404", "#050505", "#060606", "#070707", "#080808", "#090909", "#0a0a0a", "#0b0b0b",
    "#0c0c0c", "#0d0d0d", "#0e0e0e", "#0f0f0f", "#101010", "#111111", "#121212", "#131313", "#141414", "#151515", "#161616", "#171717",
    "#181818", "#191919", "#1a1a1a", "#1b1b1b", "#1c1c1c", "#1d1d1d", "#1e1e1e", "#1f1f1f", "#202020", "#212121", "#222222", "#232323",
    "#242424", "#252525", "#262626", "#272727", "#282828", "#292929", "#2a2a2a", "#2b2b2b", "#2c2c2c", "#2d2d2d", "#2e2e2e", "#2f2f2f",
    "#303030", "#313131", "#323232", "#333333", "#343434", "#353535", "#363636", "#373737", "#383838", "#393939", "#3a3a3a", "#3b3b3b",
    "#3c3c3c", "#3d3d3d", "#3e3e3e", "#3f3f3f", "#404040", "#414141", "#424242", "#434343", "#444444", "#454545", "#464646", "#474747",
    "#484848", "#494949", "#4a4a4a", "#4b4b4b", "#4c4c4c", "#4d4d4d", "#4e4e4e", "#4f4f4f", "#505050", "#515151", "#525252", "#535353",
    "#545454", "#555555", "#565656", "#575757", "#585858", "#595959", "#5a5a5a", "#5b5b5b", "#5c5c5c", "#5d5d5d", "#5e5e5e", "#5f5f5f",
    "#606060", "#616161", "#626262", "#636363", "#646464", "#656565", "#666666", "#676767", "#686868", "#696969", "#6a6a6a", "#6b6b6b",
    "#6c6c6c", "#6d6d6d", "#6e6e6e", "#6f6f6f", "#707070", "#717171", "#727272", "#737373", "#747474", "#757575", "#767676", "#777777",
    "#787878", "#797979", "#7a7a7a", "#7b7b7b", "#7c7c7c", "#7d7d7d", "#7e7e7e", "#7f7f7f", "#808080", "#818181", "#828282", "#838383",
    "#848484", "#858585", "#868686", "#878787", "#888888", "#898989", "#8a8a8a", "#8b8b8b", "#8c8c8c", "#8d8d8d", "#8e8e8e", "#8f8f8f",
    "#909090", "#919191", "#929292", "#939393", "#949494", "#959595", "#969696", "#979797", "#989898", "#999999", "#9a9a9a", "#9b9b9b",
    "#9c9c9c", "#9d9d9d", "#9e9e9e", "#9f9f9f", "#a0a0a0", "#a1a1a1", "#a2a2a2", "#a3a3a3", "#a4a4a4", "#a5a5a5", "#a6a6a6", "#a7a7a7",
    "#a8a8a8", "#a9a9a9", "#aaaaaa", "#ababab", "#acacac", "#adadad", "#aeaeae", "#afafaf", "#b0b0b0", "#b1b1b1", "#b2b2b2", "#b3b3b3",
    "#b4b4b4", "#b5b5b5", "#b6b6b6", "#b7b7b7", "#b8b8b8", "#b9b9b9", "#bababa", "#bbbbbb", "#bcbcbc", "#bdbdbd", "#bebebe", "#bfbfbf",
    "#c0c0c0", "#c1c1c1", "#c2c2c2", "#c3c3c3", "#c4c4c4", "#c5c5c5", "#c6c6c6", "#c7c7c7", "#c8c8c8", "#c9c9c9", "#cacaca", "#cbcbcb",
    "#cccccc", "#cdcdcd", "#cecece", "#cfcfcf", "#d0d0d0", "#d1d1d1", "#d2d2d2", "#d3d3d3", "#d4d4d4", "#d5d5d5", "#d6d6d6", "#d7d7d7",
    "#d8d8d8", "#d9d9d9", "#dadada", "#dbdbdb", "#dcdcdc", "#dddddd", "#dedede", "#dfdfdf", "#e0e0e0", "#e1e1e1", "#e2e2e2", "#e3e3e3",
    "#e4e4e4", "#e5e5e5", "#e6e6e6", "#e7e7e7", "#e8e8e8", "#e9e9e9", "#eaeaea", "#ebebeb", "#ececec", "#ededed", "#eeeeee", "#efefef",
    "#f0f0f0", "#f1f1f1", "#f2f2f2", "#f3f3f3", "#f4f4f4", "#f5f5f5", "#f6f6f6", "#f7f7f7", "#f8f8f8", "#f9f9f9", "#fafafa", "#fbfbfb",
    "#fcfcfc", "#fdfdfd", "#fefefe", "#ffffff"]

PuOr3       = ["#998ec3", "#f7f7f7", "#f1a340"]
PuOr4       = ["#5e3c99", "#b2abd2", "#fdb863", "#e66101"]
PuOr5       = ["#5e3c99", "#b2abd2", "#f7f7f7", "#fdb863", "#e66101"]
PuOr6       = ["#542788", "#998ec3", "#d8daeb", "#fee0b6", "#f1a340", "#b35806"]
PuOr7       = ["#542788", "#998ec3", "#d8daeb", "#f7f7f7", "#fee0b6", "#f1a340", "#b35806"]
PuOr8       = ["#542788", "#8073ac", "#b2abd2", "#d8daeb", "#fee0b6", "#fdb863", "#e08214", "#b35806"]
PuOr9       = ["#542788", "#8073ac", "#b2abd2", "#d8daeb", "#f7f7f7", "#fee0b6", "#fdb863", "#e08214", "#b35806"]
PuOr10      = ["#2d004b", "#542788", "#8073ac", "#b2abd2", "#d8daeb", "#fee0b6", "#fdb863", "#e08214", "#b35806", "#7f3b08"]
PuOr11      = ["#2d004b", "#542788", "#8073ac", "#b2abd2", "#d8daeb", "#f7f7f7", "#fee0b6", "#fdb863", "#e08214", "#b35806", "#7f3b08"]

BrBG3       = ["#5ab4ac", "#f5f5f5", "#d8b365"]
BrBG4       = ["#018571", "#80cdc1", "#dfc27d", "#a6611a"]
BrBG5       = ["#018571", "#80cdc1", "#f5f5f5", "#dfc27d", "#a6611a"]
BrBG6       = ["#01665e", "#5ab4ac", "#c7eae5", "#f6e8c3", "#d8b365", "#8c510a"]
BrBG7       = ["#01665e", "#5ab4ac", "#c7eae5", "#f5f5f5", "#f6e8c3", "#d8b365", "#8c510a"]
BrBG8       = ["#01665e", "#35978f", "#80cdc1", "#c7eae5", "#f6e8c3", "#dfc27d", "#bf812d", "#8c510a"]
BrBG9       = ["#01665e", "#35978f", "#80cdc1", "#c7eae5", "#f5f5f5", "#f6e8c3", "#dfc27d", "#bf812d", "#8c510a"]
BrBG10      = ["#003c30", "#01665e", "#35978f", "#80cdc1", "#c7eae5", "#f6e8c3", "#dfc27d", "#bf812d", "#8c510a", "#543005"]
BrBG11      = ["#003c30", "#01665e", "#35978f", "#80cdc1", "#c7eae5", "#f5f5f5", "#f6e8c3", "#dfc27d", "#bf812d", "#8c510a", "#543005"]

PRGn3       = ["#7fbf7b", "#f7f7f7", "#af8dc3"]
PRGn4       = ["#008837", "#a6dba0", "#c2a5cf", "#7b3294"]
PRGn5       = ["#008837", "#a6dba0", "#f7f7f7", "#c2a5cf", "#7b3294"]
PRGn6       = ["#1b7837", "#7fbf7b", "#d9f0d3", "#e7d4e8", "#af8dc3", "#762a83"]
PRGn7       = ["#1b7837", "#7fbf7b", "#d9f0d3", "#f7f7f7", "#e7d4e8", "#af8dc3", "#762a83"]
PRGn8       = ["#1b7837", "#5aae61", "#a6dba0", "#d9f0d3", "#e7d4e8", "#c2a5cf", "#9970ab", "#762a83"]
PRGn9       = ["#1b7837", "#5aae61", "#a6dba0", "#d9f0d3", "#f7f7f7", "#e7d4e8", "#c2a5cf", "#9970ab", "#762a83"]
PRGn10      = ["#00441b", "#1b7837", "#5aae61", "#a6dba0", "#d9f0d3", "#e7d4e8", "#c2a5cf", "#9970ab", "#762a83", "#40004b"]
PRGn11      = ["#00441b", "#1b7837", "#5aae61", "#a6dba0", "#d9f0d3", "#f7f7f7", "#e7d4e8", "#c2a5cf", "#9970ab", "#762a83", "#40004b"]

PiYG3       = ["#a1d76a", "#f7f7f7", "#e9a3c9"]
PiYG4       = ["#4dac26", "#b8e186", "#f1b6da", "#d01c8b"]
PiYG5       = ["#4dac26", "#b8e186", "#f7f7f7", "#f1b6da", "#d01c8b"]
PiYG6       = ["#4d9221", "#a1d76a", "#e6f5d0", "#fde0ef", "#e9a3c9", "#c51b7d"]
PiYG7       = ["#4d9221", "#a1d76a", "#e6f5d0", "#f7f7f7", "#fde0ef", "#e9a3c9", "#c51b7d"]
PiYG8       = ["#4d9221", "#7fbc41", "#b8e186", "#e6f5d0", "#fde0ef", "#f1b6da", "#de77ae", "#c51b7d"]
PiYG9       = ["#4d9221", "#7fbc41", "#b8e186", "#e6f5d0", "#f7f7f7", "#fde0ef", "#f1b6da", "#de77ae", "#c51b7d"]
PiYG10      = ["#276419", "#4d9221", "#7fbc41", "#b8e186", "#e6f5d0", "#fde0ef", "#f1b6da", "#de77ae", "#c51b7d", "#8e0152"]
PiYG11      = ["#276419", "#4d9221", "#7fbc41", "#b8e186", "#e6f5d0", "#f7f7f7", "#fde0ef", "#f1b6da", "#de77ae", "#c51b7d", "#8e0152"]

RdBu3       = ["#67a9cf", "#f7f7f7", "#ef8a62"]
RdBu4       = ["#0571b0", "#92c5de", "#f4a582", "#ca0020"]
RdBu5       = ["#0571b0", "#92c5de", "#f7f7f7", "#f4a582", "#ca0020"]
RdBu6       = ["#2166ac", "#67a9cf", "#d1e5f0", "#fddbc7", "#ef8a62", "#b2182b"]
RdBu7       = ["#2166ac", "#67a9cf", "#d1e5f0", "#f7f7f7", "#fddbc7", "#ef8a62", "#b2182b"]
RdBu8       = ["#2166ac", "#4393c3", "#92c5de", "#d1e5f0", "#fddbc7", "#f4a582", "#d6604d", "#b2182b"]
RdBu9       = ["#2166ac", "#4393c3", "#92c5de", "#d1e5f0", "#f7f7f7", "#fddbc7", "#f4a582", "#d6604d", "#b2182b"]
RdBu10      = ["#053061", "#2166ac", "#4393c3", "#92c5de", "#d1e5f0", "#fddbc7", "#f4a582", "#d6604d", "#b2182b", "#67001f"]
RdBu11      = ["#053061", "#2166ac", "#4393c3", "#92c5de", "#d1e5f0", "#f7f7f7", "#fddbc7", "#f4a582", "#d6604d", "#b2182b", "#67001f"]

RdGy3       = ["#999999", "#ffffff", "#ef8a62"]
RdGy4       = ["#404040", "#bababa", "#f4a582", "#ca0020"]
RdGy5       = ["#404040", "#bababa", "#ffffff", "#f4a582", "#ca0020"]
RdGy6       = ["#4d4d4d", "#999999", "#e0e0e0", "#fddbc7", "#ef8a62", "#b2182b"]
RdGy7       = ["#4d4d4d", "#999999", "#e0e0e0", "#ffffff", "#fddbc7", "#ef8a62", "#b2182b"]
RdGy8       = ["#4d4d4d", "#878787", "#bababa", "#e0e0e0", "#fddbc7", "#f4a582", "#d6604d", "#b2182b"]
RdGy9       = ["#4d4d4d", "#878787", "#bababa", "#e0e0e0", "#ffffff", "#fddbc7", "#f4a582", "#d6604d", "#b2182b"]
RdGy10      = ["#1a1a1a", "#4d4d4d", "#878787", "#bababa", "#e0e0e0", "#fddbc7", "#f4a582", "#d6604d", "#b2182b", "#67001f"]
RdGy11      = ["#1a1a1a", "#4d4d4d", "#878787", "#bababa", "#e0e0e0", "#ffffff", "#fddbc7", "#f4a582", "#d6604d", "#b2182b", "#67001f"]

RdYlBu3     = ["#91bfdb", "#ffffbf", "#fc8d59"]
RdYlBu4     = ["#2c7bb6", "#abd9e9", "#fdae61", "#d7191c"]
RdYlBu5     = ["#2c7bb6", "#abd9e9", "#ffffbf", "#fdae61", "#d7191c"]
RdYlBu6     = ["#4575b4", "#91bfdb", "#e0f3f8", "#fee090", "#fc8d59", "#d73027"]
RdYlBu7     = ["#4575b4", "#91bfdb", "#e0f3f8", "#ffffbf", "#fee090", "#fc8d59", "#d73027"]
RdYlBu8     = ["#4575b4", "#74add1", "#abd9e9", "#e0f3f8", "#fee090", "#fdae61", "#f46d43", "#d73027"]
RdYlBu9     = ["#4575b4", "#74add1", "#abd9e9", "#e0f3f8", "#ffffbf", "#fee090", "#fdae61", "#f46d43", "#d73027"]
RdYlBu10    = ["#313695", "#4575b4", "#74add1", "#abd9e9", "#e0f3f8", "#fee090", "#fdae61", "#f46d43", "#d73027", "#a50026"]
RdYlBu11    = ["#313695", "#4575b4", "#74add1", "#abd9e9", "#e0f3f8", "#ffffbf", "#fee090", "#fdae61", "#f46d43", "#d73027", "#a50026"]

Spectral3   = ["#99d594", "#ffffbf", "#fc8d59"]
Spectral4   = ["#2b83ba", "#abdda4", "#fdae61", "#d7191c"]
Spectral5   = ["#2b83ba", "#abdda4", "#ffffbf", "#fdae61", "#d7191c"]
Spectral6   = ["#3288bd", "#99d594", "#e6f598", "#fee08b", "#fc8d59", "#d53e4f"]
Spectral7   = ["#3288bd", "#99d594", "#e6f598", "#ffffbf", "#fee08b", "#fc8d59", "#d53e4f"]
Spectral8   = ["#3288bd", "#66c2a5", "#abdda4", "#e6f598", "#fee08b", "#fdae61", "#f46d43", "#d53e4f"]
Spectral9   = ["#3288bd", "#66c2a5", "#abdda4", "#e6f598", "#ffffbf", "#fee08b", "#fdae61", "#f46d43", "#d53e4f"]
Spectral10  = ["#5e4fa2", "#3288bd", "#66c2a5", "#abdda4", "#e6f598", "#fee08b", "#fdae61", "#f46d43", "#d53e4f", "#9e0142"]
Spectral11  = ["#5e4fa2", "#3288bd", "#66c2a5", "#abdda4", "#e6f598", "#ffffbf", "#fee08b", "#fdae61", "#f46d43", "#d53e4f", "#9e0142"]

RdYlGn3     = ["#91cf60", "#ffffbf", "#fc8d59"]
RdYlGn4     = ["#1a9641", "#a6d96a", "#fdae61", "#d7191c"]
RdYlGn5     = ["#1a9641", "#a6d96a", "#ffffbf", "#fdae61", "#d7191c"]
RdYlGn6     = ["#1a9850", "#91cf60", "#d9ef8b", "#fee08b", "#fc8d59", "#d73027"]
RdYlGn7     = ["#1a9850", "#91cf60", "#d9ef8b", "#ffffbf", "#fee08b", "#fc8d59", "#d73027"]
RdYlGn8     = ["#1a9850", "#66bd63", "#a6d96a", "#d9ef8b", "#fee08b", "#fdae61", "#f46d43", "#d73027"]
RdYlGn9     = ["#1a9850", "#66bd63", "#a6d96a", "#d9ef8b", "#ffffbf", "#fee08b", "#fdae61", "#f46d43", "#d73027"]
RdYlGn10    = ["#006837", "#1a9850", "#66bd63", "#a6d96a", "#d9ef8b", "#fee08b", "#fdae61", "#f46d43", "#d73027", "#a50026"]
RdYlGn11    = ["#006837", "#1a9850", "#66bd63", "#a6d96a", "#d9ef8b", "#ffffbf", "#fee08b", "#fdae61", "#f46d43", "#d73027", "#a50026"]

Inferno3    = ['#000003', '#BA3655', '#FCFEA4']
Inferno4    = ['#000003', '#781C6D', '#ED6825', '#FCFEA4']
Inferno5    = ['#000003', '#550F6D', '#BA3655', '#F98C09', '#FCFEA4']
Inferno6    = ['#000003', '#410967', '#932567', '#DC5039', '#FBA40A', '#FCFEA4']
Inferno7    = ['#000003', '#32095D', '#781C6D', '#BA3655', '#ED6825', '#FBB318', '#FCFEA4']
Inferno8    = ['#000003', '#270B52', '#63146E', '#9E2963', '#D24742', '#F57C15', '#FABF25', '#FCFEA4']
Inferno9    = ['#000003', '#1F0C47', '#550F6D', '#88216A', '#BA3655', '#E35832', '#F98C09', '#F8C931', '#FCFEA4']
Inferno10   = ['#000003', '#1A0B40', '#4A0B6A', '#781C6D', '#A42C60', '#CD4247', '#ED6825', '#FB9906', '#F7CF3A', '#FCFEA4']
Inferno11   = ['#000003', '#160B39', '#410967', '#6A176E', '#932567', '#BA3655', '#DC5039', '#F2751A', '#FBA40A', '#F6D542', '#FCFEA4']
Inferno256  = [
    '#000003', '#000004', '#000006', '#010007', '#010109', '#01010B', '#02010E', '#020210', '#030212', '#040314', '#040316', '#050418',
    '#06041B', '#07051D', '#08061F', '#090621', '#0A0723', '#0B0726', '#0D0828', '#0E082A', '#0F092D', '#10092F', '#120A32', '#130A34',
    '#140B36', '#160B39', '#170B3B', '#190B3E', '#1A0B40', '#1C0C43', '#1D0C45', '#1F0C47', '#200C4A', '#220B4C', '#240B4E', '#260B50',
    '#270B52', '#290B54', '#2B0A56', '#2D0A58', '#2E0A5A', '#300A5C', '#32095D', '#34095F', '#350960', '#370961', '#390962', '#3B0964',
    '#3C0965', '#3E0966', '#400966', '#410967', '#430A68', '#450A69', '#460A69', '#480B6A', '#4A0B6A', '#4B0C6B', '#4D0C6B', '#4F0D6C',
    '#500D6C', '#520E6C', '#530E6D', '#550F6D', '#570F6D', '#58106D', '#5A116D', '#5B116E', '#5D126E', '#5F126E', '#60136E', '#62146E',
    '#63146E', '#65156E', '#66156E', '#68166E', '#6A176E', '#6B176E', '#6D186E', '#6E186E', '#70196E', '#72196D', '#731A6D', '#751B6D',
    '#761B6D', '#781C6D', '#7A1C6D', '#7B1D6C', '#7D1D6C', '#7E1E6C', '#801F6B', '#811F6B', '#83206B', '#85206A', '#86216A', '#88216A',
    '#892269', '#8B2269', '#8D2369', '#8E2468', '#902468', '#912567', '#932567', '#952666', '#962666', '#982765', '#992864', '#9B2864',
    '#9C2963', '#9E2963', '#A02A62', '#A12B61', '#A32B61', '#A42C60', '#A62C5F', '#A72D5F', '#A92E5E', '#AB2E5D', '#AC2F5C', '#AE305B',
    '#AF315B', '#B1315A', '#B23259', '#B43358', '#B53357', '#B73456', '#B83556', '#BA3655', '#BB3754', '#BD3753', '#BE3852', '#BF3951',
    '#C13A50', '#C23B4F', '#C43C4E', '#C53D4D', '#C73E4C', '#C83E4B', '#C93F4A', '#CB4049', '#CC4148', '#CD4247', '#CF4446', '#D04544',
    '#D14643', '#D24742', '#D44841', '#D54940', '#D64A3F', '#D74B3E', '#D94D3D', '#DA4E3B', '#DB4F3A', '#DC5039', '#DD5238', '#DE5337',
    '#DF5436', '#E05634', '#E25733', '#E35832', '#E45A31', '#E55B30', '#E65C2E', '#E65E2D', '#E75F2C', '#E8612B', '#E9622A', '#EA6428',
    '#EB6527', '#EC6726', '#ED6825', '#ED6A23', '#EE6C22', '#EF6D21', '#F06F1F', '#F0701E', '#F1721D', '#F2741C', '#F2751A', '#F37719',
    '#F37918', '#F47A16', '#F57C15', '#F57E14', '#F68012', '#F68111', '#F78310', '#F7850E', '#F8870D', '#F8880C', '#F88A0B', '#F98C09',
    '#F98E08', '#F99008', '#FA9107', '#FA9306', '#FA9506', '#FA9706', '#FB9906', '#FB9B06', '#FB9D06', '#FB9E07', '#FBA007', '#FBA208',
    '#FBA40A', '#FBA60B', '#FBA80D', '#FBAA0E', '#FBAC10', '#FBAE12', '#FBB014', '#FBB116', '#FBB318', '#FBB51A', '#FBB71C', '#FBB91E',
    '#FABB21', '#FABD23', '#FABF25', '#FAC128', '#F9C32A', '#F9C52C', '#F9C72F', '#F8C931', '#F8CB34', '#F8CD37', '#F7CF3A', '#F7D13C',
    '#F6D33F', '#F6D542', '#F5D745', '#F5D948', '#F4DB4B', '#F4DC4F', '#F3DE52', '#F3E056', '#F3E259', '#F2E45D', '#F2E660', '#F1E864',
    '#F1E968', '#F1EB6C', '#F1ED70', '#F1EE74', '#F1F079', '#F1F27D', '#F2F381', '#F2F485', '#F3F689', '#F4F78D', '#F5F891', '#F6FA95',
    '#F7FB99', '#F9FC9D', '#FAFDA0', '#FCFEA4']

Magma3      = ['#000003', '#B53679', '#FBFCBF']
Magma4      = ['#000003', '#711F81', '#F0605D', '#FBFCBF']
Magma5      = ['#000003', '#4F117B', '#B53679', '#FB8660', '#FBFCBF']
Magma6      = ['#000003', '#3B0F6F', '#8C2980', '#DD4968', '#FD9F6C', '#FBFCBF']
Magma7      = ['#000003', '#2B115E', '#711F81', '#B53679', '#F0605D', '#FEAE76', '#FBFCBF']
Magma8      = ['#000003', '#221150', '#5D177E', '#972C7F', '#D1426E', '#F8755C', '#FEB97F', '#FBFCBF']
Magma9      = ['#000003', '#1B1044', '#4F117B', '#812581', '#B53679', '#E55063', '#FB8660', '#FEC286', '#FBFCBF']
Magma10     = ['#000003', '#170F3C', '#430F75', '#711F81', '#9E2E7E', '#CB3E71', '#F0605D', '#FC9366', '#FEC78B', '#FBFCBF']
Magma11     = ['#000003', '#140D35', '#3B0F6F', '#63197F', '#8C2980', '#B53679', '#DD4968', '#F66E5B', '#FD9F6C', '#FDCD90', '#FBFCBF']
Magma256    = [
    '#000003', '#000004', '#000006', '#010007', '#010109', '#01010B', '#02020D', '#02020F', '#030311', '#040313', '#040415', '#050417',
    '#060519', '#07051B', '#08061D', '#09071F', '#0A0722', '#0B0824', '#0C0926', '#0D0A28', '#0E0A2A', '#0F0B2C', '#100C2F', '#110C31',
    '#120D33', '#140D35', '#150E38', '#160E3A', '#170F3C', '#180F3F', '#1A1041', '#1B1044', '#1C1046', '#1E1049', '#1F114B', '#20114D',
    '#221150', '#231152', '#251155', '#261157', '#281159', '#2A115C', '#2B115E', '#2D1060', '#2F1062', '#301065', '#321067', '#341068',
    '#350F6A', '#370F6C', '#390F6E', '#3B0F6F', '#3C0F71', '#3E0F72', '#400F73', '#420F74', '#430F75', '#450F76', '#470F77', '#481078',
    '#4A1079', '#4B1079', '#4D117A', '#4F117B', '#50127B', '#52127C', '#53137C', '#55137D', '#57147D', '#58157E', '#5A157E', '#5B167E',
    '#5D177E', '#5E177F', '#60187F', '#61187F', '#63197F', '#651A80', '#661A80', '#681B80', '#691C80', '#6B1C80', '#6C1D80', '#6E1E81',
    '#6F1E81', '#711F81', '#731F81', '#742081', '#762181', '#772181', '#792281', '#7A2281', '#7C2381', '#7E2481', '#7F2481', '#812581',
    '#822581', '#842681', '#852681', '#872781', '#892881', '#8A2881', '#8C2980', '#8D2980', '#8F2A80', '#912A80', '#922B80', '#942B80',
    '#952C80', '#972C7F', '#992D7F', '#9A2D7F', '#9C2E7F', '#9E2E7E', '#9F2F7E', '#A12F7E', '#A3307E', '#A4307D', '#A6317D', '#A7317D',
    '#A9327C', '#AB337C', '#AC337B', '#AE347B', '#B0347B', '#B1357A', '#B3357A', '#B53679', '#B63679', '#B83778', '#B93778', '#BB3877',
    '#BD3977', '#BE3976', '#C03A75', '#C23A75', '#C33B74', '#C53C74', '#C63C73', '#C83D72', '#CA3E72', '#CB3E71', '#CD3F70', '#CE4070',
    '#D0416F', '#D1426E', '#D3426D', '#D4436D', '#D6446C', '#D7456B', '#D9466A', '#DA4769', '#DC4869', '#DD4968', '#DE4A67', '#E04B66',
    '#E14C66', '#E24D65', '#E44E64', '#E55063', '#E65162', '#E75262', '#E85461', '#EA5560', '#EB5660', '#EC585F', '#ED595F', '#EE5B5E',
    '#EE5D5D', '#EF5E5D', '#F0605D', '#F1615C', '#F2635C', '#F3655C', '#F3675B', '#F4685B', '#F56A5B', '#F56C5B', '#F66E5B', '#F6705B',
    '#F7715B', '#F7735C', '#F8755C', '#F8775C', '#F9795C', '#F97B5D', '#F97D5D', '#FA7F5E', '#FA805E', '#FA825F', '#FB8460', '#FB8660',
    '#FB8861', '#FB8A62', '#FC8C63', '#FC8E63', '#FC9064', '#FC9265', '#FC9366', '#FD9567', '#FD9768', '#FD9969', '#FD9B6A', '#FD9D6B',
    '#FD9F6C', '#FDA16E', '#FDA26F', '#FDA470', '#FEA671', '#FEA873', '#FEAA74', '#FEAC75', '#FEAE76', '#FEAF78', '#FEB179', '#FEB37B',
    '#FEB57C', '#FEB77D', '#FEB97F', '#FEBB80', '#FEBC82', '#FEBE83', '#FEC085', '#FEC286', '#FEC488', '#FEC689', '#FEC78B', '#FEC98D',
    '#FECB8E', '#FDCD90', '#FDCF92', '#FDD193', '#FDD295', '#FDD497', '#FDD698', '#FDD89A', '#FDDA9C', '#FDDC9D', '#FDDD9F', '#FDDFA1',
    '#FDE1A3', '#FCE3A5', '#FCE5A6', '#FCE6A8', '#FCE8AA', '#FCEAAC', '#FCECAE', '#FCEEB0', '#FCF0B1', '#FCF1B3', '#FCF3B5', '#FCF5B7',
    '#FBF7B9', '#FBF9BB', '#FBFABD', '#FBFCBF']

Plasma3     = ['#0C0786', '#CA4678', '#EFF821']
Plasma4     = ['#0C0786', '#9B179E', '#EC7853', '#EFF821']
Plasma5     = ['#0C0786', '#7C02A7', '#CA4678', '#F79341', '#EFF821']
Plasma6     = ['#0C0786', '#6A00A7', '#B02A8F', '#E06461', '#FCA635', '#EFF821']
Plasma7     = ['#0C0786', '#5C00A5', '#9B179E', '#CA4678', '#EC7853', '#FDB22F', '#EFF821']
Plasma8     = ['#0C0786', '#5201A3', '#8908A5', '#B83289', '#DA5A68', '#F38748', '#FDBB2B', '#EFF821']
Plasma9     = ['#0C0786', '#4A02A0', '#7C02A7', '#A82296', '#CA4678', '#E56B5C', '#F79341', '#FDC328', '#EFF821']
Plasma10    = ['#0C0786', '#45039E', '#7200A8', '#9B179E', '#BC3685', '#D7566C', '#EC7853', '#FA9D3A', '#FCC726', '#EFF821']
Plasma11    = ['#0C0786', '#40039C', '#6A00A7', '#8F0DA3', '#B02A8F', '#CA4678', '#E06461', '#F1824C', '#FCA635', '#FCCC25', '#EFF821']
Plasma256   = [
    '#0C0786', '#100787', '#130689', '#15068A', '#18068B', '#1B068C', '#1D068D', '#1F058E', '#21058F', '#230590', '#250591', '#270592',
    '#290593', '#2B0594', '#2D0494', '#2F0495', '#310496', '#330497', '#340498', '#360498', '#380499', '#3A049A', '#3B039A', '#3D039B',
    '#3F039C', '#40039C', '#42039D', '#44039E', '#45039E', '#47029F', '#49029F', '#4A02A0', '#4C02A1', '#4E02A1', '#4F02A2', '#5101A2',
    '#5201A3', '#5401A3', '#5601A3', '#5701A4', '#5901A4', '#5A00A5', '#5C00A5', '#5E00A5', '#5F00A6', '#6100A6', '#6200A6', '#6400A7',
    '#6500A7', '#6700A7', '#6800A7', '#6A00A7', '#6C00A8', '#6D00A8', '#6F00A8', '#7000A8', '#7200A8', '#7300A8', '#7500A8', '#7601A8',
    '#7801A8', '#7901A8', '#7B02A8', '#7C02A7', '#7E03A7', '#7F03A7', '#8104A7', '#8204A7', '#8405A6', '#8506A6', '#8607A6', '#8807A5',
    '#8908A5', '#8B09A4', '#8C0AA4', '#8E0CA4', '#8F0DA3', '#900EA3', '#920FA2', '#9310A1', '#9511A1', '#9612A0', '#9713A0', '#99149F',
    '#9A159E', '#9B179E', '#9D189D', '#9E199C', '#9F1A9B', '#A01B9B', '#A21C9A', '#A31D99', '#A41E98', '#A51F97', '#A72197', '#A82296',
    '#A92395', '#AA2494', '#AC2593', '#AD2692', '#AE2791', '#AF2890', '#B02A8F', '#B12B8F', '#B22C8E', '#B42D8D', '#B52E8C', '#B62F8B',
    '#B7308A', '#B83289', '#B93388', '#BA3487', '#BB3586', '#BC3685', '#BD3784', '#BE3883', '#BF3982', '#C03B81', '#C13C80', '#C23D80',
    '#C33E7F', '#C43F7E', '#C5407D', '#C6417C', '#C7427B', '#C8447A', '#C94579', '#CA4678', '#CB4777', '#CC4876', '#CD4975', '#CE4A75',
    '#CF4B74', '#D04D73', '#D14E72', '#D14F71', '#D25070', '#D3516F', '#D4526E', '#D5536D', '#D6556D', '#D7566C', '#D7576B', '#D8586A',
    '#D95969', '#DA5A68', '#DB5B67', '#DC5D66', '#DC5E66', '#DD5F65', '#DE6064', '#DF6163', '#DF6262', '#E06461', '#E16560', '#E26660',
    '#E3675F', '#E3685E', '#E46A5D', '#E56B5C', '#E56C5B', '#E66D5A', '#E76E5A', '#E87059', '#E87158', '#E97257', '#EA7356', '#EA7455',
    '#EB7654', '#EC7754', '#EC7853', '#ED7952', '#ED7B51', '#EE7C50', '#EF7D4F', '#EF7E4E', '#F0804D', '#F0814D', '#F1824C', '#F2844B',
    '#F2854A', '#F38649', '#F38748', '#F48947', '#F48A47', '#F58B46', '#F58D45', '#F68E44', '#F68F43', '#F69142', '#F79241', '#F79341',
    '#F89540', '#F8963F', '#F8983E', '#F9993D', '#F99A3C', '#FA9C3B', '#FA9D3A', '#FA9F3A', '#FAA039', '#FBA238', '#FBA337', '#FBA436',
    '#FCA635', '#FCA735', '#FCA934', '#FCAA33', '#FCAC32', '#FCAD31', '#FDAF31', '#FDB030', '#FDB22F', '#FDB32E', '#FDB52D', '#FDB62D',
    '#FDB82C', '#FDB92B', '#FDBB2B', '#FDBC2A', '#FDBE29', '#FDC029', '#FDC128', '#FDC328', '#FDC427', '#FDC626', '#FCC726', '#FCC926',
    '#FCCB25', '#FCCC25', '#FCCE25', '#FBD024', '#FBD124', '#FBD324', '#FAD524', '#FAD624', '#FAD824', '#F9D924', '#F9DB24', '#F8DD24',
    '#F8DF24', '#F7E024', '#F7E225', '#F6E425', '#F6E525', '#F5E726', '#F5E926', '#F4EA26', '#F3EC26', '#F3EE26', '#F2F026', '#F2F126',
    '#F1F326', '#F0F525', '#F0F623', '#EFF821']

Viridis3    = ['#440154', '#208F8C', '#FDE724']
Viridis4    = ['#440154', '#30678D', '#35B778', '#FDE724']
Viridis5    = ['#440154', '#3B518A', '#208F8C', '#5BC862', '#FDE724']
Viridis6    = ['#440154', '#404387', '#29788E', '#22A784', '#79D151', '#FDE724']
Viridis7    = ['#440154', '#443982', '#30678D', '#208F8C', '#35B778', '#8DD644', '#FDE724']
Viridis8    = ['#440154', '#46317E', '#365A8C', '#277E8E', '#1EA087', '#49C16D', '#9DD93A', '#FDE724']
Viridis9    = ['#440154', '#472B7A', '#3B518A', '#2C718E', '#208F8C', '#27AD80', '#5BC862', '#AADB32', '#FDE724']
Viridis10   = ['#440154', '#472777', '#3E4989', '#30678D', '#25828E', '#1E9C89', '#35B778', '#6BCD59', '#B2DD2C', '#FDE724']
Viridis11   = ['#440154', '#482374', '#404387', '#345E8D', '#29788E', '#208F8C', '#22A784', '#42BE71', '#79D151', '#BADE27', '#FDE724']
Viridis256  = [
    '#440154', '#440255', '#440357', '#450558', '#45065A', '#45085B', '#46095C', '#460B5E', '#460C5F', '#460E61', '#470F62', '#471163',
    '#471265', '#471466', '#471567', '#471669', '#47186A', '#48196B', '#481A6C', '#481C6E', '#481D6F', '#481E70', '#482071', '#482172',
    '#482273', '#482374', '#472575', '#472676', '#472777', '#472878', '#472A79', '#472B7A', '#472C7B', '#462D7C', '#462F7C', '#46307D',
    '#46317E', '#45327F', '#45347F', '#453580', '#453681', '#443781', '#443982', '#433A83', '#433B83', '#433C84', '#423D84', '#423E85',
    '#424085', '#414186', '#414286', '#404387', '#404487', '#3F4587', '#3F4788', '#3E4888', '#3E4989', '#3D4A89', '#3D4B89', '#3D4C89',
    '#3C4D8A', '#3C4E8A', '#3B508A', '#3B518A', '#3A528B', '#3A538B', '#39548B', '#39558B', '#38568B', '#38578C', '#37588C', '#37598C',
    '#365A8C', '#365B8C', '#355C8C', '#355D8C', '#345E8D', '#345F8D', '#33608D', '#33618D', '#32628D', '#32638D', '#31648D', '#31658D',
    '#31668D', '#30678D', '#30688D', '#2F698D', '#2F6A8D', '#2E6B8E', '#2E6C8E', '#2E6D8E', '#2D6E8E', '#2D6F8E', '#2C708E', '#2C718E',
    '#2C728E', '#2B738E', '#2B748E', '#2A758E', '#2A768E', '#2A778E', '#29788E', '#29798E', '#287A8E', '#287A8E', '#287B8E', '#277C8E',
    '#277D8E', '#277E8E', '#267F8E', '#26808E', '#26818E', '#25828E', '#25838D', '#24848D', '#24858D', '#24868D', '#23878D', '#23888D',
    '#23898D', '#22898D', '#228A8D', '#228B8D', '#218C8D', '#218D8C', '#218E8C', '#208F8C', '#20908C', '#20918C', '#1F928C', '#1F938B',
    '#1F948B', '#1F958B', '#1F968B', '#1E978A', '#1E988A', '#1E998A', '#1E998A', '#1E9A89', '#1E9B89', '#1E9C89', '#1E9D88', '#1E9E88',
    '#1E9F88', '#1EA087', '#1FA187', '#1FA286', '#1FA386', '#20A485', '#20A585', '#21A685', '#21A784', '#22A784', '#23A883', '#23A982',
    '#24AA82', '#25AB81', '#26AC81', '#27AD80', '#28AE7F', '#29AF7F', '#2AB07E', '#2BB17D', '#2CB17D', '#2EB27C', '#2FB37B', '#30B47A',
    '#32B57A', '#33B679', '#35B778', '#36B877', '#38B976', '#39B976', '#3BBA75', '#3DBB74', '#3EBC73', '#40BD72', '#42BE71', '#44BE70',
    '#45BF6F', '#47C06E', '#49C16D', '#4BC26C', '#4DC26B', '#4FC369', '#51C468', '#53C567', '#55C666', '#57C665', '#59C764', '#5BC862',
    '#5EC961', '#60C960', '#62CA5F', '#64CB5D', '#67CC5C', '#69CC5B', '#6BCD59', '#6DCE58', '#70CE56', '#72CF55', '#74D054', '#77D052',
    '#79D151', '#7CD24F', '#7ED24E', '#81D34C', '#83D34B', '#86D449', '#88D547', '#8BD546', '#8DD644', '#90D643', '#92D741', '#95D73F',
    '#97D83E', '#9AD83C', '#9DD93A', '#9FD938', '#A2DA37', '#A5DA35', '#A7DB33', '#AADB32', '#ADDC30', '#AFDC2E', '#B2DD2C', '#B5DD2B',
    '#B7DD29', '#BADE27', '#BDDE26', '#BFDF24', '#C2DF22', '#C5DF21', '#C7E01F', '#CAE01E', '#CDE01D', '#CFE11C', '#D2E11B', '#D4E11A',
    '#D7E219', '#DAE218', '#DCE218', '#DFE318', '#E1E318', '#E4E318', '#E7E419', '#E9E419', '#ECE41A', '#EEE51B', '#F1E51C', '#F3E51E',
    '#F6E61F', '#F8E621', '#FAE622', '#FDE724']

# http://colorbrewer2.org/?type=qualitative&scheme=Accent&n=8
Accent3 = ['#7fc97f', '#beaed4', '#fdc086']
Accent4 = ['#7fc97f', '#beaed4', '#fdc086', '#ffff99']
Accent5 = ['#7fc97f', '#beaed4', '#fdc086', '#ffff99', '#386cb0']
Accent6 = ['#7fc97f', '#beaed4', '#fdc086', '#ffff99', '#386cb0', '#f0027f']
Accent7 = ['#7fc97f', '#beaed4', '#fdc086', '#ffff99', '#386cb0', '#f0027f', '#bf5b17']
Accent8 = ['#7fc97f', '#beaed4', '#fdc086', '#ffff99', '#386cb0', '#f0027f', '#bf5b17', '#666666']

# http://colorbrewer2.org/?type=qualitative&scheme=Dark2&n=8
Dark2_3 = ['#1b9e77', '#d95f02', '#7570b3']
Dark2_4 = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a']
Dark2_5 = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e']
Dark2_6 = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e', '#e6ab02']
Dark2_7 = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e', '#e6ab02', '#a6761d']
Dark2_8 = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e', '#e6ab02', '#a6761d', '#666666']

# http://colorbrewer2.org/?type=qualitative&scheme=Paired&n=12
Paired3 = ['#a6cee3', '#1f78b4', '#b2df8a']
Paired4 = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c']
Paired5 = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99']
Paired6 = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c']
Paired7 = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f']
Paired8 = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00']
Paired9 = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6']
Paired10 = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a']
Paired11 = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a', '#ffff99']
Paired12 = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a', '#ffff99', '#b15928']

# http://colorbrewer2.org/?type=qualitative&scheme=Pastel1&n=9
Pastel1_3 = ['#fbb4ae', '#b3cde3', '#ccebc5']
Pastel1_4 = ['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4']
Pastel1_5 = ['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6']
Pastel1_6 = ['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#ffffcc']
Pastel1_7 = ['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#ffffcc', '#e5d8bd']
Pastel1_8 = ['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#ffffcc', '#e5d8bd', '#fddaec']
Pastel1_9 = ['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#ffffcc', '#e5d8bd', '#fddaec', '#f2f2f2']

# http://colorbrewer2.org/?type=qualitative&scheme=Pastel2&n=8
Pastel2_3 = ['#b3e2cd', '#fdcdac', '#cbd5e8']
Pastel2_4 = ['#b3e2cd', '#fdcdac', '#cbd5e8', '#f4cae4']
Pastel2_5 = ['#b3e2cd', '#fdcdac', '#cbd5e8', '#f4cae4', '#e6f5c9']
Pastel2_6 = ['#b3e2cd', '#fdcdac', '#cbd5e8', '#f4cae4', '#e6f5c9', '#fff2ae']
Pastel2_7 = ['#b3e2cd', '#fdcdac', '#cbd5e8', '#f4cae4', '#e6f5c9', '#fff2ae', '#f1e2cc']
Pastel2_8 = ['#b3e2cd', '#fdcdac', '#cbd5e8', '#f4cae4', '#e6f5c9', '#fff2ae', '#f1e2cc', '#cccccc']

# http://colorbrewer2.org/?type=qualitative&scheme=Set1&n=9
Set1_3 = ['#e41a1c', '#377eb8', '#4daf4a']
Set1_4 = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3']
Set1_5 = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']
Set1_6 = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33']
Set1_7 = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33', '#a65628']
Set1_8 = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33', '#a65628', '#f781bf']
Set1_9 = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33', '#a65628', '#f781bf', '#999999']

# http://colorbrewer2.org/?type=qualitative&scheme=Set2&n=8
Set2_3 = ['#66c2a5', '#fc8d62', '#8da0cb']
Set2_4 = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3']
Set2_5 = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']
Set2_6 = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f']
Set2_7 = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', '#e5c494']
Set2_8 = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', '#e5c494', '#b3b3b3']

# http://colorbrewer2.org/?type=qualitative&scheme=Set3&n=12
Set3_3 = ['#8dd3c7', '#ffffb3', '#bebada']
Set3_4 = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072']
Set3_5 = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3']
Set3_6 = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462']
Set3_7 = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69']
Set3_8 = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5']
Set3_9 = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5', '#d9d9d9']
Set3_10 = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5', '#d9d9d9', '#bc80bd']
Set3_11 = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5', '#d9d9d9', '#bc80bd', '#ccebc5']
Set3_12 = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5', '#d9d9d9', '#bc80bd', '#ccebc5', '#ffed6f']


__palettes__ = [
    "YlGn3",      "YlGn4",      "YlGn5",      "YlGn6",      "YlGn7",      "YlGn8",      "YlGn9",
    "YlGnBu3",    "YlGnBu4",    "YlGnBu5",    "YlGnBu6",    "YlGnBu7",    "YlGnBu8",    "YlGnBu9",
    "GnBu3",      "GnBu4",      "GnBu5",      "GnBu6",      "GnBu7",      "GnBu8",      "GnBu9",
    "BuGn3",      "BuGn4",      "BuGn5",      "BuGn6",      "BuGn7",      "BuGn8",      "BuGn9",
    "PuBuGn3",    "PuBuGn4",    "PuBuGn5",    "PuBuGn6",    "PuBuGn7",    "PuBuGn8",    "PuBuGn9",
    "PuBu3",      "PuBu4",      "PuBu5",      "PuBu6",      "PuBu7",      "PuBu8",      "PuBu9",
    "BuPu3",      "BuPu4",      "BuPu5",      "BuPu6",      "BuPu7",      "BuPu8",      "BuPu9",
    "RdPu3",      "RdPu4",      "RdPu5",      "RdPu6",      "RdPu7",      "RdPu8",      "RdPu9",
    "PuRd3",      "PuRd4",      "PuRd5",      "PuRd6",      "PuRd7",      "PuRd8",      "PuRd9",
    "OrRd3",      "OrRd4",      "OrRd5",      "OrRd6",      "OrRd7",      "OrRd8",      "OrRd9",
    "YlOrRd3",    "YlOrRd4",    "YlOrRd5",    "YlOrRd6",    "YlOrRd7",    "YlOrRd8",    "YlOrRd9",
    "YlOrBr3",    "YlOrBr4",    "YlOrBr5",    "YlOrBr6",    "YlOrBr7",    "YlOrBr8",    "YlOrBr9",
    "Purples3",   "Purples4",   "Purples5",   "Purples6",   "Purples7",   "Purples8",   "Purples9",
    "Blues3",     "Blues4",     "Blues5",     "Blues6",     "Blues7",     "Blues8",     "Blues9",
    "Greens3",    "Greens4",    "Greens5",    "Greens6",    "Greens7",    "Greens8",    "Greens9",
    "Oranges3",   "Oranges4",   "Oranges5",   "Oranges6",   "Oranges7",   "Oranges8",   "Oranges9",
    "Reds3",      "Reds4",      "Reds5",      "Reds6",      "Reds7",      "Reds8",      "Reds9",
    "Greys3",     "Greys4",     "Greys5",     "Greys6",     "Greys7",     "Greys8",     "Greys9",     "Greys10",     "Greys11",     "Greys256",
    "PuOr3",      "PuOr4",      "PuOr5",      "PuOr6",      "PuOr7",      "PuOr8",      "PuOr9",      "PuOr10",      "PuOr11",
    "BrBG3",      "BrBG4",      "BrBG5",      "BrBG6",      "BrBG7",      "BrBG8",      "BrBG9",      "BrBG10",      "BrBG11",
    "PRGn3",      "PRGn4",      "PRGn5",      "PRGn6",      "PRGn7",      "PRGn8",      "PRGn9",      "PRGn10",      "PRGn11",
    "PiYG3",      "PiYG4",      "PiYG5",      "PiYG6",      "PiYG7",      "PiYG8",      "PiYG9",      "PiYG10",      "PiYG11",
    "RdBu3",      "RdBu4",      "RdBu5",      "RdBu6",      "RdBu7",      "RdBu8",      "RdBu9",      "RdBu10",      "RdBu11",
    "RdGy3",      "RdGy4",      "RdGy5",      "RdGy6",      "RdGy7",      "RdGy8",      "RdGy9",      "RdGy10",      "RdGy11",
    "RdYlBu3",    "RdYlBu4",    "RdYlBu5",    "RdYlBu6",    "RdYlBu7",    "RdYlBu8",    "RdYlBu9",    "RdYlBu10",    "RdYlBu11",
    "Spectral3",  "Spectral4",  "Spectral5",  "Spectral6",  "Spectral7",  "Spectral8",  "Spectral9",  "Spectral10",  "Spectral11",
    "RdYlGn3",    "RdYlGn4",    "RdYlGn5",    "RdYlGn6",    "RdYlGn7",    "RdYlGn8",    "RdYlGn9",    "RdYlGn10",    "RdYlGn11",
    "Magma3",     "Magma4",     "Magma5",     "Magma6",     "Magma7",     "Magma8",     "Magma9",     "Magma10",     "Magma11",     "Magma256",
    "Inferno3",   "Inferno4",   "Inferno5",   "Inferno6",   "Inferno7",   "Inferno8",   "Inferno9",   "Inferno10",   "Inferno11",   "Inferno256",
    "Plasma3",    "Plasma4",    "Plasma5",    "Plasma6",    "Plasma7",    "Plasma8",    "Plasma9",    "Plasma10",    "Plasma11",    "Plasma256",
    "Viridis3",   "Viridis4",   "Viridis5",   "Viridis6",   "Viridis7",   "Viridis8",   "Viridis9",   "Viridis10",   "Viridis11",   "Viridis256",
    "Accent3",    "Accent4",    "Accent5",    "Accent6",    "Accent7",    "Accent8",
    "Dark2_3",    "Dark2_4",    "Dark2_5",    "Dark2_6",    "Dark2_7",    "Dark2_8",
    "Paired3",    "Paired4",    "Paired5",    "Paired6",    "Paired7",    "Paired8",    "Paired9",    "Paired10",    "Paired11",    "Paired12",
    "Pastel1_3",  "Pastel1_4",  "Pastel1_5",  "Pastel1_6",  "Pastel1_7",  "Pastel1_8",  "Pastel1_9",
    "Pastel2_3",  "Pastel2_4",  "Pastel2_5",  "Pastel2_6",  "Pastel2_7",  "Pastel2_8",
    "Set1_3",     "Set1_4",     "Set1_5",     "Set1_6",     "Set1_7",     "Set1_8",     "Set1_9",
    "Set2_3",     "Set2_4",     "Set2_5",     "Set2_6",     "Set2_7",     "Set2_8",
    "Set3_3",     "Set3_4",     "Set3_5",     "Set3_6",     "Set3_7",     "Set3_8",     "Set3_9",     "Set3_10",     "Set3_11",     "Set3_12"
]


brewer = {
    "YlGn"     : { 3: YlGn3,     4: YlGn4,     5: YlGn5,     6: YlGn6,     7: YlGn7,     8: YlGn8,     9: YlGn9 },
    "YlGnBu"   : { 3: YlGnBu3,   4: YlGnBu4,   5: YlGnBu5,   6: YlGnBu6,   7: YlGnBu7,   8: YlGnBu8,   9: YlGnBu9 },
    "GnBu"     : { 3: GnBu3,     4: GnBu4,     5: GnBu5,     6: GnBu6,     7: GnBu7,     8: GnBu8,     9: GnBu9 },
    "BuGn"     : { 3: BuGn3,     4: BuGn4,     5: BuGn5,     6: BuGn6,     7: BuGn7,     8: BuGn8,     9: BuGn9 },
    "PuBuGn"   : { 3: PuBuGn3,   4: PuBuGn4,   5: PuBuGn5,   6: PuBuGn6,   7: PuBuGn7,   8: PuBuGn8,   9: PuBuGn9 },
    "PuBu"     : { 3: PuBu3,     4: PuBu4,     5: PuBu5,     6: PuBu6,     7: PuBu7,     8: PuBu8,     9: PuBu9 },
    "BuPu"     : { 3: BuPu3,     4: BuPu4,     5: BuPu5,     6: BuPu6,     7: BuPu7,     8: BuPu8,     9: BuPu9 },
    "RdPu"     : { 3: RdPu3,     4: RdPu4,     5: RdPu5,     6: RdPu6,     7: RdPu7,     8: RdPu8,     9: RdPu9 },
    "PuRd"     : { 3: PuRd3,     4: PuRd4,     5: PuRd5,     6: PuRd6,     7: PuRd7,     8: PuRd8,     9: PuRd9 },
    "OrRd"     : { 3: OrRd3,     4: OrRd4,     5: OrRd5,     6: OrRd6,     7: OrRd7,     8: OrRd8,     9: OrRd9 },
    "YlOrRd"   : { 3: YlOrRd3,   4: YlOrRd4,   5: YlOrRd5,   6: YlOrRd6,   7: YlOrRd7,   8: YlOrRd8,   9: YlOrRd9 },
    "YlOrBr"   : { 3: YlOrBr3,   4: YlOrBr4,   5: YlOrBr5,   6: YlOrBr6,   7: YlOrBr7,   8: YlOrBr8,   9: YlOrBr9 },
    "Purples"  : { 3: Purples3,  4: Purples4,  5: Purples5,  6: Purples6,  7: Purples7,  8: Purples8,  9: Purples9 },
    "Blues"    : { 3: Blues3,    4: Blues4,    5: Blues5,    6: Blues6,    7: Blues7,    8: Blues8,    9: Blues9 },
    "Greens"   : { 3: Greens3,   4: Greens4,   5: Greens5,   6: Greens6,   7: Greens7,   8: Greens8,   9: Greens9 },
    "Oranges"  : { 3: Oranges3,  4: Oranges4,  5: Oranges5,  6: Oranges6,  7: Oranges7,  8: Oranges8,  9: Oranges9 },
    "Reds"     : { 3: Reds3,     4: Reds4,     5: Reds5,     6: Reds6,     7: Reds7,     8: Reds8,     9: Reds9 },
    "Greys"    : { 3: Greys3,    4: Greys4,    5: Greys5,    6: Greys6,    7: Greys7,    8: Greys8,    9: Greys9 },
    "PuOr"     : { 3: PuOr3,     4: PuOr4,     5: PuOr5,     6: PuOr6,     7: PuOr7,     8: PuOr8,     9: PuOr9,      10: PuOr10,     11: PuOr11 },
    "BrBG"     : { 3: BrBG3,     4: BrBG4,     5: BrBG5,     6: BrBG6,     7: BrBG7,     8: BrBG8,     9: BrBG9,      10: BrBG10,     11: BrBG11 },
    "PRGn"     : { 3: PRGn3,     4: PRGn4,     5: PRGn5,     6: PRGn6,     7: PRGn7,     8: PRGn8,     9: PRGn9,      10: PRGn10,     11: PRGn11 },
    "PiYG"     : { 3: PiYG3,     4: PiYG4,     5: PiYG5,     6: PiYG6,     7: PiYG7,     8: PiYG8,     9: PiYG9,      10: PiYG10,     11: PiYG11 },
    "RdBu"     : { 3: RdBu3,     4: RdBu4,     5: RdBu5,     6: RdBu6,     7: RdBu7,     8: RdBu8,     9: RdBu9,      10: RdBu10,     11: RdBu11 },
    "RdGy"     : { 3: RdGy3,     4: RdGy4,     5: RdGy5,     6: RdGy6,     7: RdGy7,     8: RdGy8,     9: RdGy9,      10: RdGy10,     11: RdGy11 },
    "RdYlBu"   : { 3: RdYlBu3,   4: RdYlBu4,   5: RdYlBu5,   6: RdYlBu6,   7: RdYlBu7,   8: RdYlBu8,   9: RdYlBu9,    10: RdYlBu10,   11: RdYlBu11 },
    "Spectral" : { 3: Spectral3, 4: Spectral4, 5: Spectral5, 6: Spectral6, 7: Spectral7, 8: Spectral8, 9: Spectral9,  10: Spectral10, 11: Spectral11 },
    "RdYlGn"   : { 3: RdYlGn3,   4: RdYlGn4,   5: RdYlGn5,   6: RdYlGn6,   7: RdYlGn7,   8: RdYlGn8,   9: RdYlGn9,    10: RdYlGn10,   11: RdYlGn11 },
    "Accent"   : { 3: Accent3,   4: Accent4,   5: Accent5,   6: Accent6,   7: Accent7,   8: Accent8 },
    "Dark2"   : { 3: Dark2_3,   4: Dark2_4,   5: Dark2_5,   6: Dark2_6,   7: Dark2_7,   8: Dark2_8 },
    "Paired"   : { 3: Paired3,   4: Paired4,   5: Paired5,   6: Paired6,   7: Paired7,   8: Paired8,   9: Paired9,    10: Paired10,   11: Paired11,
                   12: Paired12 },
    "Pastel1"  : { 3: Pastel1_3, 4: Pastel1_4, 5: Pastel1_5, 6: Pastel1_6, 7: Pastel1_7, 8: Pastel1_8, 9: Pastel1_9 },
    "Pastel2"  : { 3: Pastel2_3, 4: Pastel2_4, 5: Pastel2_5, 6: Pastel2_6, 7: Pastel2_7, 8: Pastel2_8 },
    "Set1"     : { 3: Set1_3,    4: Set1_4,    5: Set1_5,    6: Set1_6,    7: Set1_7,    8: Set1_8,    9: Set1_9 },
    "Set2"     : { 3: Set2_3 ,   4: Set2_4,    5: Set2_5,    6: Set2_6,    7: Set2_7,    8: Set2_8 },
    "Set3"     : { 3: Set3_3,    4: Set3_4,    5: Set3_5,    6: Set3_6,    7: Set3_7,    8: Set3_8,    9: Set3_9,     10: Set3_10,    11: Set3_11,
                   12: Set3_12 },
}

small_palettes = dict(brewer)
small_palettes.update({
    "Magma"   : { 3: Magma3,   4: Magma4,   5: Magma5,   6: Magma6,   7: Magma7,   8: Magma8,   9: Magma9,    10: Magma10,   11: Magma11   },
    "Inferno" : { 3: Inferno3, 4: Inferno4, 5: Inferno5, 6: Inferno6, 7: Inferno7, 8: Inferno8, 9: Inferno9,  10: Inferno10, 11: Inferno11 },
    "Plasma"  : { 3: Plasma3,  4: Plasma4,  5: Plasma5,  6: Plasma6,  7: Plasma7,  8: Plasma8,  9: Plasma9,   10: Plasma10,  11: Plasma11  },
    "Viridis" : { 3: Viridis3, 4: Viridis4, 5: Viridis5, 6: Viridis6, 7: Viridis7, 8: Viridis8, 9: Viridis9,  10: Viridis10, 11: Viridis11 },
})

def _linear_cmap_func_generator(name, cmap):
    def func(n):
        if n>len(cmap): raise ValueError("Requested %(r)s colors, function can only return colors up to the base palette's length (%(l)s)"
            %{'r':n,'l':len(cmap)})
        return [cmap[int(math.floor(i))] for i in np.linspace(0, len(cmap)-1, num=n)]
    func.__name__ = name
    return func

def _linear_grey_cmap_func_generator(name):
    def func(n):
        cmap = Greys256
        if n>256: raise ValueError("Hexidecimals support only up to 256 shades of grey")
        return [cmap[int(math.floor(i))] for i in np.linspace(0, len(cmap)-1, num=n)]
    func.__name__ = name
    return func


_cmaps = {name: _linear_cmap_func_generator(name, cmap) for name, cmap in (('magma', Magma256),
                                                                    ('inferno', Inferno256),
                                                                    ('plasma', Plasma256),
                                                                    ('viridis', Viridis256))}

magma = _cmaps['magma']
inferno = _cmaps['inferno']
plasma = _cmaps['plasma']
viridis = _cmaps['viridis']
grey = _linear_grey_cmap_func_generator('grey')
gray = _linear_grey_cmap_func_generator('gray')
