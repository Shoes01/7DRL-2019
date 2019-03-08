import cProfile
import tcod as libtcod
import warnings

from game import initialize_new_game
from input_handlers import handle_keys
from render_functions.borders import render_borders
from render_functions.render import render_all
from systems.update import update

def main():
    consoles, entities, game, game_map, game_state_machine, key, message_log, mouse, neighborhood, player = initialize_new_game()

    event_queue = []

    action = True
    render_borders(consoles['root'])
    render_all(action, consoles, entities, game, game_map, game_state_machine, message_log, mouse, neighborhood, player)

    while True:
        # Process input.
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        action = handle_keys(game_state_machine, key)

        # Update game.
        update(action, entities, event_queue, game, game_map, game_state_machine, message_log, neighborhood, player)

        # Render results.
        render_all(action, consoles, entities, game, game_map, game_state_machine, message_log, mouse, neighborhood, player)

        if game_state_machine.state.__str__() == 'Exit':
            consoles['root'].__exit__()
            return False
        
        warnings.simplefilter("default")

if __name__ == '__main__':
    # cProfile.run('main()') # This runs the profiler
    main()