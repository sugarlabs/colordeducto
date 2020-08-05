# -*- coding: utf-8 -*-
#Copyright (c) 2012 Walter Bender
# Ported to GTK3:
# Ignacio Rodríguez <ignaciorodriguez@sugarlabs.org
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# You should have received a copy of the GNU General Public License
# along with this library; if not, write to the Free Software
# Foundation, 51 Franklin Street, Suite 500 Boston, MA 02110-1335 USA


LEVELS_TRUE = ['def generate_pattern(self):\n\
    # Level 1: Center dot is Red\n\
    dot_list = []\n\
    for i in range(25):\n\
        dot_list.append(self._mun_color.random_hvc(0, 10, 4, 7, 3, 3))\n\
    dot_list[12] = self._mun_color.hvc(0, 5, 3)\n\
    return dot_list\n',
               'def generate_pattern(self):\n\
    # Level 2: Monochrome\n\
    dot_list = []\n\
    h = int(uniform(0, 10))\n\
    for i in range(25):\n\
        dot_list.append(self._mun_color.random_hue(h, h))\n\
    return dot_list\n',
               'def generate_pattern(self):\n\
    # Level 3: Max chroma\n\
    dot_list = []\n\
    for i in range(25):\n\
        dot_list.append(self._mun_color.random_hvc(0, 10, 4, 7, 3, 3))\n\
    return dot_list\n',
               'def generate_pattern(self):\n\
    # Level 4: lighter as it moves up\n\
    dot_list = []\n\
    for y in range(5):\n\
        for x in range(5):\n\
            dot_list.append(self._mun_color.random_hvc(\n\
                0, 10, 10-y, 10-y, 2, 3))\n\
    return dot_list\n',
               'def generate_pattern(self):\n\
    # Level 5: chroma increases to center\n\
    dot_list = []\n\
    for i in range(25):\n\
        if i in [0, 1, 2, 3, 4, 5, 9, 10, 14, 15, 19, 20, 21, 22, 23, 24]:\n\
            dot_list.append(self._mun_color.random_hvc(\n\
                0, 10, 4, 7, 1, 1))\n\
        elif i in [6, 7, 8, 11, 13, 16, 17, 18]:\n\
            dot_list.append(self._mun_color.random_hvc(\n\
                0, 10, 4, 7, 2, 2))\n\
        else:\n\
            dot_list.append(self._mun_color.random_hvc(\n\
                0, 10, 4, 7, 3, 3))\n\
    return dot_list\n',
               'def generate_pattern(self):\n\
    # Level 6: equiluminent\n\
    dot_list = []\n\
    for i in range(25):\n\
        dot_list.append(self._mun_color.random_hvc(0, 10, 6, 6, 3, 3))\n\
    return dot_list\n',
               'def generate_pattern(self):\n\
    # Level 7: complementary\n\
    dot_list = []\n\
    h = int(uniform(0, 10))\n\
    for i in range(25):\n\
        if int(uniform(0, 2)):\n\
            dot_list.append(self._mun_color.random_hvc(h, h, 6, 6, 3, 3))\n\
        else:\n\
            dot_list.append(self._mun_color.random_hvc(h+5, h+5, 6, 6, 3, 3))\n\
    return dot_list\n',
               'def generate_pattern(self):\n\
    # Level 8: hue increase down\n\
    dot_list = []\n\
    for y in range(5):\n\
        for x in range(5):\n\
            dot_list.append(self._mun_color.random_hvc(\n\
                y*2, y*2+1, 4, 7, 2, 3))\n\
    return dot_list\n',
               'def generate_pattern(self):\n\
    # Level 9: interlocking hues\n\
    dot_list = []\n\
    h = int(uniform(0, 10))\n\
    for i in range(25):\n\
        if i in [0, 1, 2, 3, 4, 9, 14, 19, 18, 17, 16, 11]:\n\
            dot_list.append(self._mun_color.random_hvc(\n\
                h, h, 4, 7, 2, 3))\n\
        elif i == 12:\n\
            dot_list.append(self._mun_color.random_hvc(\n\
                h + 2, h + 2, 4, 7, 0, 2))\n\
        else:\n\
            dot_list.append(self._mun_color.random_hvc(\n\
                h + 4, h + 4, 4, 7, 2, 3))\n\
    return dot_list\n',
               'def generate_pattern(self):\n\
    # Level 10: checkerboard\n\
    dot_list = []\n\
    for i in range(25):\n\
        if i % 2 == 0:\n\
            dot_list.append(self._mun_color.random_hvc(\n\
                0, 10, 4, 5, 1, 1))\n\
        else:\n\
            dot_list.append(self._mun_color.random_hvc(\n\
                0, 10, 7, 8, 3, 3))\n\
    return dot_list\n']
LEVELS_FALSE = ['def generate_pattern(self):\n\
    # Level 1: Center dot is not Red\n\
    dot_list = []\n\
    for i in range(25):\n\
        dot_list.append(self._mun_color.random_hvc(0, 10, 4, 7, 3, 3))\n\
    dot_list[12] = self._mun_color.random_hvc(1, 10, 4, 7, 3, 3)\n\
    return dot_list\n',
               'def generate_pattern(self):\n\
    # Level 2: not monochrome\n\
    dot_list = []\n\
    h = int(uniform(0, 7))\n\
    for i in range(25):\n\
        dot_list.append(self._mun_color.random_hue(h, h + 3))\n\
    return dot_list\n',
               'def generate_pattern(self):\n\
    # Level 3: not max chroma\n\
    dot_list = []\n\
    for i in range(25):\n\
        dot_list.append(self._mun_color.random_hvc(0, 10, 4, 7, 0, 3))\n\
    return dot_list\n',
               'def generate_pattern(self):\n\
    # Level 4: lighter as it moves down\n\
    dot_list = []\n\
    for y in range(5):\n\
        for x in range(5):\n\
            dot_list.append(self._mun_color.random_hvc(\n\
                0, 10, y+5, y+5, 2, 3))\n\
    return dot_list\n',
               'def generate_pattern(self):\n\
    # Level 5: chroma decreases to center\n\
    dot_list = []\n\
    for i in range(25):\n\
        if i in [0, 1, 2, 3, 4, 5, 9, 10, 14, 15, 19, 20, 21, 22, 23, 24]:\n\
            dot_list.append(self._mun_color.random_hvc(\n\
                0, 10, 4, 7, 3, 3))\n\
        elif i in [6, 7, 8, 11, 13, 16, 17, 18]:\n\
            dot_list.append(self._mun_color.random_hvc(\n\
                0, 10, 4, 7, 2, 2))\n\
        else:\n\
            dot_list.append(self._mun_color.random_hvc(\n\
                0, 10, 4, 7, 1, 1))\n\
    return dot_list\n',
               'def generate_pattern(self):\n\
    # Level 6: not equiluminent\n\
    dot_list = []\n\
    for i in range(25):\n\
        dot_list.append(self._mun_color.random_hvc(0, 10, 4, 8, 3, 3))\n\
    return dot_list\n',
               'def generate_pattern(self):\n\
    # Level 7: complementary\n\
    dot_list = []\n\
    h = int(uniform(0, 10))\n\
    for i in range(25):\n\
        if int(uniform(0, 2)):\n\
            dot_list.append(self._mun_color.random_hvc(h, h, 6, 6, 3, 3))\n\
        else:\n\
            dot_list.append(self._mun_color.random_hvc(h+2, h+2, 6, 6, 3, 3))\n\
    return dot_list\n',
               'def generate_pattern(self):\n\
    # Level 8: hue increase up\n\
    dot_list = []\n\
    for y in range(5):\n\
        for x in range(5):\n\
            dot_list.append(self._mun_color.random_hvc(\n\
                8-y*2, 9-y*2, 4, 7, 2, 3))\n\
    return dot_list\n',
               'def generate_pattern(self):\n\
    # Level 9: interlocking hues\n\
    dot_list = []\n\
    h = int(uniform(0, 10))\n\
    for i in range(25):\n\
        if i in [0, 1, 2, 3, 4, 9, 14, 19, 18, 17, 16, 11]:\n\
            dot_list.append(self._mun_color.random_hvc(\n\
                h, h, 4, 7, 2, 3))\n\
        elif i == 12:\n\
            dot_list.append(self._mun_color.random_hvc(\n\
                h, h + 1, 4, 7, 0, 2))\n\
        else:\n\
            dot_list.append(self._mun_color.random_hvc(\n\
                h + 1, h + 1, 4, 7, 2, 3))\n\
    return dot_list\n',
               'def generate_pattern(self):\n\
    # Level 10: chroma checkerboard\n\
    dot_list = []\n\
    for i in range(25):\n\
        if i % 2 == 0:\n\
            dot_list.append(self._mun_color.random_hvc(\n\
                0, 10, 5, 5, 0, 1))\n\
        else:\n\
            dot_list.append(self._mun_color.random_hvc(\n\
                0, 10, 5, 5, 3, 3))\n\
    return dot_list\n']


from gi.repository import Gdk, GdkPixbuf, GObject, Gtk
import cairo

from math import sqrt
from random import uniform

import traceback

from gettext import gettext as _

import logging
_logger = logging.getLogger('reflection-activity')

try:
    from sugar3.graphics import style
    GRID_CELL_SIZE = style.GRID_CELL_SIZE
except ImportError:
    GRID_CELL_SIZE = 0

from mun import MunColor
from sprites import Sprites, Sprite

# Grid dimensions
GRID = 5
WHITE = 2
landscape = (Gdk.Screen.height() < Gdk.Screen.width())
smallest_size = Gdk.Screen.height() if landscape else Gdk.Screen.width()
DOT_SIZE = int(0.1*smallest_size)


class Game():

    def __init__(self, canvas, parent=None, colors=['#A0FFA0', '#FF8080']):
        self._activity = parent
        self._colors = [colors[0]]
        self._colors.append(colors[1])
        self._mun_color = MunColor()
        self._dot_cache = {}

        self._canvas = canvas
        if parent is not None:
            parent.show_all()
            self._parent = parent

        self._canvas.connect("draw", self.__draw_cb)

        self._width = Gdk.Screen.width()
        self._height = Gdk.Screen.height() - (GRID_CELL_SIZE * 1.5)
        self._scale = smallest_size / (DOT_SIZE*8)
        self._dot_size = int(DOT_SIZE * self._scale)
        self._space = int(self._dot_size / 5.)
        self.max_levels = len(LEVELS_TRUE)
        self.this_pattern = False

        # Generate the sprites we'll need...
        self._sprites = Sprites(self._canvas)
        self._dots = []
        self._generate_grid()

    def _generate_grid(self):
        ''' Make a new set of dots for a grid of size edge '''
        i = 0
        for y in range(GRID):
            for x in range(GRID):
                xoffset = int((self._width - GRID * self._dot_size - \
                                   (GRID - 1) * self._space) / 2.)
                xoffset -= int(self._dot_size / 2)  # rects aren't centered
                if i < len(self._dots):
                    self._dots[i].move(
                        (xoffset + x * (self._dot_size + self._space),
                         y * (self._dot_size + self._space) + self._space))
                else:
                    self._dots.append(
                        Sprite(self._sprites,
                               xoffset + x * (self._dot_size + self._space),
                               y * (self._dot_size + self._space) + self._space,
                               self._new_dot(self._colors[0])))
                self._dots[i].type = 0
                self._dots[-1].set_label_attributes(40)
                i += 1

    def show(self, dot_list):
        for i in range(GRID * GRID):
            self._dots[i].set_shape(self._new_dot(dot_list[i]))
            self._dots[i].type = dot_list[i]

    def show_true(self):
        self.show(self._generate_pattern(LEVELS_TRUE[self._activity.level]))
        self.this_pattern = True

    def show_false(self):
        self.show(self._generate_pattern(LEVELS_FALSE[self._activity.level]))
        self.this_pattern = False

    def show_random(self):
        ''' Fill the grid with a true or false pattern '''
        if int(uniform(0, 2)) == 0:
            self.show_true()
        else:
            self.show_false()

    def _initiating(self):
        return self._activity._collab.props.leader

    def new_game(self):
        ''' Start a new game. '''
        self.show_random()

    def restore_grid(self, dot_list, boolean, color):
        ''' Restore a grid from the share '''
        self.show(dot_list)
        self.this_pattern = boolean
        self._colors = color

    def save_grid(self):
        ''' Return dot list for sharing '''
        dot_list = []
        for dot in self._dots:
            dot_list.append(dot.type)
        return dot_list, self.this_pattern, self._colors

    def _grid_to_dot(self, pos):
        ''' calculate the dot index from a column and row in the grid '''
        return pos[0] + pos[1] * GRID

    def _dot_to_grid(self, dot):
        ''' calculate the grid column and row for a dot '''
        return [dot % GRID, int(dot / GRID)]

    def _set_label(self, string):
        ''' Set the label in the toolbar or the window frame. '''
        self._activity.status.set_label(string)

    def _generate_pattern(self, f):
        ''' Run Python code passed as argument '''
        userdefined = {}
        try:
            exec(f, globals(), userdefined)
            return userdefined['generate_pattern'](self)
        except ZeroDivisionError as e:
            self._set_label('Python zero-divide error: %s' % (str(e)))
        except ValueError as e:
            self._set_label('Python value error: %s' % (str(e)))
        except SyntaxError as e:
            self._set_label('Python syntax error: %s' % (str(e)))
        except NameError as e:
            self._set_label('Python name error: %s' % (str(e)))
        except OverflowError as e:
            self._set_label('Python overflow error: %s' % (str(e)))
        except TypeError as e:
            self._set_label('Python type error: %s' % (str(e)))
        except:
            self._set_label('Python error')
        traceback.print_exc()
        return None

    def __draw_cb(self, canvas, cr):
        self._sprites.redraw_sprites(cr=cr)

    def do_expose_event(self, event):
        ''' Handle the expose-event by drawing '''
        # Restrict Cairo to the exposed area
        cr = self._canvas.window.cairo_create()
        cr.rectangle(event.area.x, event.area.y,
                event.area.width, event.area.height)
        cr.clip()
        # Refresh sprite list
        if cr is not None:
            self._sprites.redraw_sprites(cr=cr)

    def _destroy_cb(self, win, event):
        Gtk.main_quit()

    def _new_dot(self, color):
        ''' generate a dot of a color color '''
        if not color in self._dot_cache:
            self._stroke = color
            self._fill = color
            self._svg_width = self._dot_size * 2
            self._svg_height = self._dot_size * 2
            pixbuf = svg_str_to_pixbuf(
                self._header() + \
                self._rect(self._dot_size / 2., self._dot_size / 2.,
                             self._dot_size / 2.) + \
                self._footer())

            surface = cairo.ImageSurface(cairo.FORMAT_ARGB32,
                                         self._svg_width, self._svg_height)
            context = cairo.Context(surface)
            Gdk.cairo_set_source_pixbuf(context, pixbuf, 0, 0)
            context.rectangle(0, 0, self._svg_width, self._svg_height)
            context.fill()
            self._dot_cache[color] = surface

        return self._dot_cache[color]

    def _header(self):
        return '<svg\n' + 'xmlns:svg="http://www.w3.org/2000/svg"\n' + \
            'xmlns="http://www.w3.org/2000/svg"\n' + \
            'xmlns:xlink="http://www.w3.org/1999/xlink"\n' + \
            'version="1.1"\n' + 'width="' + str(self._svg_width) + '"\n' + \
            'height="' + str(self._svg_height) + '">\n'

    def _circle(self, r, cx, cy):
        return '<circle style="fill:' + str(self._fill) + ';stroke:' + \
            str(self._stroke) + ';" r="' + str(r - 0.5) + '" cx="' + \
            str(cx) + '" cy="' + str(cy) + '" />\n'

    def _rect(self, r, x, y):
        return '<rect style="fill:' + str(self._fill) + ';stroke:' + \
            str(self._stroke) + ';" width="' + str(r * 2) + '" height="' + \
            str(r * 2) + '" x="' + \
            str(x) + '" y="' + str(y) + '" />\n'

    def _footer(self):
        return '</svg>\n'


def svg_str_to_pixbuf(svg_string):
    """ Load pixbuf from SVG string """
    
    pl = GdkPixbuf.PixbufLoader.new_with_type('svg')
    pl.write(bytes(svg_string, 'utf-8'))
    pl.close()
    pixbuf = pl.get_pixbuf()
    return pixbuf
