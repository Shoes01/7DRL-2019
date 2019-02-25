import cProfile
import tcod as libtcod
import warnings

from game import initialize_new_game
from input_handlers import handle_keys
from render_functions.render import render_all, render_borders
from systems.update import update

def main():
    consoles, entities, fov_map, game, game_map, game_state_machine, key, message_log, mouse, player = initialize_new_game()

    event_queue = []

    action = True
    render_borders(consoles['root'])
    render_all(action, consoles, entities, fov_map, game, game_map, game_state_machine, message_log, player)

    while not libtcod.console_is_window_closed():
        # Process input.
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        action = handle_keys(game_state_machine, key)

        # Update game.
        update(action, entities, event_queue, fov_map, game, game_map, game_state_machine, message_log, player)

        # Render results.
        render_all(action, consoles, entities, fov_map, game, game_map, game_state_machine, message_log, player)

        if game_state_machine.state.__str__() == 'Exit':
            return True
        
        warnings.simplefilter("default")

if __name__ == '__main__':
    # cProfile.run('main()') # This runs the profiler
    main()