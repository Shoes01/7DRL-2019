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

    # Clear entities.
    clear_all(console_map, entities)

def draw_tile(console_map, fov_map, game_map, x, y):
    visible = libtcod.map_is_in_fov(fov_map, x, y)
    _, blocks_path, explored = game_map.tiles[x, y]
    
    if visible:
        # Visible. Light it up.
        if blocks_path:
            console_map.default_bg = COLORS['light_wall']
            console_map.print_(x, y, " ", libtcod.BKGND_SET)
        else:
            console_map.default_bg = COLORS['light_floor']
            console_map.print_(x, y, " ", libtcod.BKGND_SET)
        
        if not explored:
            game_map.tiles['explored'][x, y] = True
    
    elif explored:
        # Explored, but not visisble. Use map memory.
        if blocks_path:
            console_map.default_bg = COLORS['dark_wall']
            console_map.print_(x, y, " ", libtcod.BKGND_SET)
        else:
            console_map.default_bg = COLORS['dark_floor']
            console_map.print_(x, y, " ", libtcod.BKGND_SET)
    
    else:
        # If neither visible nor explored, it is just black.
        console_map.default_bg = libtcod.black
        console_map.print_(x, y, " ", libtcod.BKGND_SET)

def draw_entity(console_map, entity, fov_map):
    if libtcod.map_is_in_fov(fov_map, entity.pos.x, entity.pos.y):
        console_map.default_fg = entity.base.color
        console_map.print_(entity.pos.x, entity.pos.y, entity.base.char, libtcod.BKGND_NONE)

def clear_all(console_map, entities):
    for entity in entities:
        clear(console_map, entity)

def clear(console_map, entity):
    console_map.print_(entity.pos.x, entity.pos.y, " ", libtcod.BKGND_NONE)
