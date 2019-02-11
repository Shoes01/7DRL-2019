import tcod as libtcod

from render_functions.render_panel import render_panel
from render_functions.render_map import render_map

def render_all(action, consoles, entities, fov_map, game_map, player):
    ' Render all things that appear on the screen. '
    render_map(action, consoles['map'], entities, fov_map, game_map, player)
    render_panel(consoles['panel'])

    libtcod.console_flush()