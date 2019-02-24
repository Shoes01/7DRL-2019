import tcod as libtcod

from render_functions.render_map import render_map
from render_functions.render_menu import render_menu
from render_functions.render_message_log import render_message_log
from render_functions.render_panel import render_panel

def render_all(action, consoles, entities, fov_map, game, game_map, game_state_machine, message_log, player):
    ' Render all things that appear on the screen. '
    render_map(action, consoles, entities, fov_map, game, game_map, game_state_machine, player)
    render_panel(consoles, player)
    render_message_log(consoles, message_log)
    
    _game_state = game_state_machine.state.__str__()

    if _game_state == 'OpenInventory':
        render_menu(consoles, player, type_='inventory')
    
    if _game_state == 'LeveledUp':
        render_menu(consoles, player, type_='level_up')

    libtcod.console_flush()