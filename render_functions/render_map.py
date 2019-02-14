import numpy as np
import tcod as libtcod

from game import COLORS, FOV_RADIUS, MAP
from render_functions.fov import recompute_fov

def render_map(action, consoles, entities, fov_map, game_map, player):
    ' Render all things that appear on the map. '
    console_map = consoles['map']
    console_root = consoles['root']
    # Recompute FOV, if needed.
    if action:
        recompute_fov(fov_map, player.pos.x, player.pos.y, FOV_RADIUS)
    
    # Draw the game_map tiles that are in the fov.
    for (x, y), _ in np.ndenumerate(game_map.tiles):
            draw_tile(console_map, fov_map, game_map, x, y)
    
    # Sort the entities, then draw them.
    entities_in_render_order = sorted(entities, key=lambda x: x.base.render_order.value)
    
    for entity in entities_in_render_order:
        draw_entity(console_map, entity, fov_map)

    # Send to console.
    console_map.blit(console_root)

    # Clear entities
    clear_all(console_map, entities)

def draw_tile(console_map, fov_map, game_map, x, y):
    visible = libtcod.map_is_in_fov(fov_map, x, y)
    _, blocks_path, explored = game_map.tiles[x, y]
    
    if visible:
        # Visible. Light it up.
        if blocks_path:
            libtcod.console_set_char_background(console_map, x, y, COLORS['light_wall'], libtcod.BKGND_SET)
        else:
            libtcod.console_set_char_background(console_map, x, y, COLORS['light_floor'], libtcod.BKGND_SET)
        
        if not explored:
            game_map.tiles['explored'][x, y] = True
    
    elif explored:
        # Explored, but not visisble. Use map memory.
        if blocks_path:
            libtcod.console_set_char_background(console_map, x, y, COLORS['dark_wall'], libtcod.BKGND_SET)
        else:
            libtcod.console_set_char_background(console_map, x, y, COLORS['dark_floor'], libtcod.BKGND_SET)
    
    else:
        # If neither visible nor explored, it is just black.
        libtcod.console_set_char_background(console_map, x, y, libtcod.black, libtcod.BKGND_SET)

def draw_entity(console_map, entity, fov_map):
    char = entity.base.char
    color = entity.base.color
    x = entity.pos.x
    y = entity.pos.y
    
    if libtcod.map_is_in_fov(fov_map, x, y):
        libtcod.console_set_default_foreground(console_map, color)
        libtcod.console_put_char(console_map, x, y, char, libtcod.BKGND_NONE)

def clear_all(console_map, entities):
    for entity in entities:
        clear(console_map, entity)

def clear(console_map, entity):
    x = entity.pos.x
    y = entity.pos.y

    libtcod.console_put_char(console_map, x, y, ' ', libtcod.BKGND_NONE)
