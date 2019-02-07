import numpy as np
import tcod as libtcod

from game import COLORS, SCREEN_HEIGHT, SCREEN_WIDTH

def render_all(con, entities, game_map):
    ' Render all things that appear on the screen. '
    # Draw the game_map tiles.
    for (x, y), value in np.ndenumerate(game_map.tiles):
        draw_tile(con, x, y, value)
    
    # Draw the entities.
    for entity in entities:
        draw_entity(con, entity)

    # Send to console.
    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)

def draw_tile(con, x, y, value):
    if value == 0:
        libtcod.console_set_char_background(con, x, y, COLORS['dark_floor'], libtcod.BKGND_SET)
    if value == 1:
        libtcod.console_set_char_background(con, x, y, COLORS['dark_wall'], libtcod.BKGND_SET)

def draw_entity(con, entity):
    char = entity.base.char
    color = entity.base.color
    x = entity.pos.x
    y = entity.pos.y
    
    libtcod.console_set_default_foreground(con, color)
    libtcod.console_put_char(con, x, y, char, libtcod.BKGND_NONE)

def clear_all(con, entities):
    for entity in entities:
        clear(con, entity)

def clear(con, entity):
    x = entity.pos.x
    y = entity.pos.y

    libtcod.console_put_char(con, x, y, ' ', libtcod.BKGND_NONE)
