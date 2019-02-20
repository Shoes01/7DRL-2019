import cProfile
import tcod as libtcod

from game import GameStates, initialize_new_game
from input_handlers import handle_keys
from render_functions.render import render_all
from systems.update import update

def main():
    consoles, entities, fov_map, game, game_map, key, message_log, mouse, player = initialize_new_game()

    while not libtcod.console_is_window_closed():
        # Process input.
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        action = handle_keys(game, key)

        # Update game.
        update(action, entities, fov_map, game, game_map, message_log, player)

        # Render results.
        render_all(action, consoles, entities, fov_map, game, game_map, message_log, player)

        if game.state == GameStates.EXIT:
                return True

if __name__ == '__main__':
    # icProfile.run('main()') # This runs the profiler
    main()