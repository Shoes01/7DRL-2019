import tcod as libtcod

from game import GameStates
from render_functions.render_map import render_map
from render_functions.render_menu import render_menu
from render_functions.render_message_log import render_message_log
from render_functions.render_panel import render_panel

def render_all(action, consoles, entities, fov_map, game, game_map, message_log, player):
    ' Render all things that appear on the screen. '
    render_map(action, consoles, entities, fov_map, game, game_map, player)
    render_panel(consoles, player)
    render_message_log(consoles, message_log)
    
    if game.state == GameStates.OPEN_INVENTORY:
        render_menu(consoles, player, type_='inventory')

    libtcod.console_flush()