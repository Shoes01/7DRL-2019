import numpy as np
import tcod as libtcod

from game import COLORS, FOV_RADIUS, MAP
from render_functions.fov import recompute_fov
from systems.skill import chosen_skill

def render_map(action, consoles, entities, fov_map, game, game_map, player):
    ' Render all things that appear on the map. '
    console_map = consoles['map']
    console_root = consoles['root']
    # Recompute FOV, if needed.
    if action:
        recompute_fov(fov_map, player.pos.x, player.pos.y, FOV_RADIUS)
    
    # Draw the game_map tiles that are in the fov.
    for (x, y), _ in np.ndenumerate(game_map.tiles):
            draw_tile(console_map, fov_map, game, game_map, x, y)
    game.redraw_map = False

    # Draw the skill arrays onto the map.
    skill = chosen_skill(player)
    if skill:
        for _, array in skill.legal_targeting_arrays.items():
            center = skill.array_size // 2
            xo, yo = player.pos.x - center, player.pos.y - center
            if array is not None:
                highlight_tiles(console_map, array, xo, yo)
    
    # Sort the entities, then draw them.
    entities_in_render_order = sorted(entities, key=lambda x: x.base.render_order.value)
    
    for entity in entities_in_render_order:
        draw_entity(console_map, entity, fov_map)

    # Send to console.
    console_map.blit(dest=console_root, dest_x=MAP.X, dest_y=MAP.Y, width=MAP.W, height=MAP.H)

    # Clear entities.
    clear_all(console_map, entities)

def draw_tile(console_map, fov_map, game, game_map, x, y):
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
    
    elif game.redraw_map:
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

def highlight_tiles(console_map, tiles_to_highlight, xo, yo):
    for (x, y), value in np.ndenumerate(tiles_to_highlight):
        if value == 1:
            console_map.default_bg = libtcod.light_red
            console_map.print_(xo + x, yo + y, " ", libtcod.BKGND_SET)
        elif 1 < value <= 3:
            console_map.default_bg = libtcod.red
            console_map.print_(xo + x, yo + y, " ", libtcod.BKGND_SET)
        elif value > 5:
            # The only tile that this should apply to is the player's tile.
            console_map.default_bg = libtcod.green
            console_map.print_(xo + x, yo + y, " ", libtcod.BKGND_SET)