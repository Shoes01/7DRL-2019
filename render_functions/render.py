import tcod as libtcod

from render_functions.render_panel import render_panel
from render_functions.render_map import render_map
from render_functions.render_message_log import render_message_log

def render_all(action, consoles, entities, fov_map, game_map, message_log, player):
    ' Render all things that appear on the screen. '
    render_map(action, consoles, entities, fov_map, game_map, player)
    render_panel(consoles, player)
    render_message_log(consoles, message_log)

    libtcod.console_flush()