import numpy as np
import tcod as libtcod

from game import COLORS, FOV_RADIUS, MAP
from render_functions.fov import recompute_fov
from systems.skill import chosen_skill

def render_map(action, consoles, entities, fov_map, game, game_map, game_state_machine, neighborhood, player):
    ' Render all things that appear on the map. '
    console_map = consoles['map']
    console_root = consoles['root']
    # Recompute FOV, if needed.
    if action:
        recompute_fov(fov_map, player.pos.x, player.pos.y, FOV_RADIUS)
    
        # Draw the game_map tiles that are in the fov.
        for (x, y), _ in np.ndenumerate(game_map.tiles):
                draw_tile(console_map, fov_map, game, game_map, neighborhood, x, y)
        game.redraw_map = False

    if game.debug_mode == False:
        # Draw the skill arrays onto the map.
        skill = chosen_skill(player)
        if skill and game_state_machine.state.__str__() == 'TargetingState':
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

def draw_tile(console_map, fov_map, game, game_map, neighborhood, x, y):
    visible = fov_map.fov[x, y]
    _, blocks_path, explored = game_map.tiles[x, y]
    
    if visible:
        # Visible. Light it up.
        if blocks_path:
            console_map.print(x, y, " ", bg=COLORS['light_wall'], bg_blend=libtcod.BKGND_SET)
        else:
            console_map.print(x, y, " ", bg=COLORS['light_floor'], bg_blend=libtcod.BKGND_SET)
        
        if not explored:
            game_map.tiles['explored'][x, y] = True
    
    elif explored:
        # Explored, but not visisble. Use map memory.
        if blocks_path:
            console_map.print(x, y, " ", bg=COLORS['dark_wall'], bg_blend=libtcod.BKGND_SET)
        else:
            console_map.print(x, y, " ", bg=COLORS['dark_floor'], bg_blend=libtcod.BKGND_SET)
    
    elif game.redraw_map:
        # If neither visible nor explored, it is just black.
        console_map.print(x, y, " ", bg=libtcod.black, bg_blend=libtcod.BKGND_SET)

    if game.debug_mode:
        value = neighborhood.dijkstra_map[y, x]
        if value == 999:
            console_map.print(x, y, '#', fg=libtcod.pink, bg_blend=libtcod.BKGND_NONE)    
        else:
            console_map.print(x, y, baseN(value, 35), fg=libtcod.pink, bg_blend=libtcod.BKGND_NONE)

def draw_entity(console_map, entity, fov_map):
    if fov_map.fov[entity.pos.x, entity.pos.y]:
        console_map.print(entity.pos.x, entity.pos.y, entity.base.char, fg=entity.base.color, bg_blend=libtcod.BKGND_NONE)

def clear_all(console_map, entities):
    for entity in entities:
        clear(console_map, entity)

def clear(console_map, entity):
    console_map.print(entity.pos.x, entity.pos.y, " ", bg_blend=libtcod.BKGND_NONE)

def highlight_tiles(console_map, tiles_to_highlight, xo, yo):
    for (x, y), value in np.ndenumerate(tiles_to_highlight):
        if value == 1:
            console_map.print(xo + x, yo + y, " ", bg=libtcod.light_red, bg_blend=libtcod.BKGND_SET)
        elif 1 < value <= 3:
            console_map.print(xo + x, yo + y, " ", bg=libtcod.red, bg_blend=libtcod.BKGND_SET)
        elif value and value % 17 == 0:
            # This is where the player must path through.
            console_map.print(xo + x, yo + y, " ", bg=libtcod.light_pink, bg_blend=libtcod.BKGND_SET)
        elif value and value % 19 == 0:
            # This is where the player is standing.
            console_map.print(xo + x, yo + y, " ", bg=libtcod.green, bg_blend=libtcod.BKGND_SET)
        elif value and value % 23 == 0:
            # This is where the player ends up.
            console_map.print(xo + x, yo + y, " ", bg=libtcod.pink, bg_blend=libtcod.BKGND_SET)

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])