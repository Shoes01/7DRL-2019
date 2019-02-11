import tcod as libtcod

from game import GameStates, GAME_TITLE, ROOT_HEIGHT, ROOT_WIDTH, initialize_new_game
from input_handlers import handle_keys
from render_functions.render import render_all
from systems.update import update

def main():
    libtcod.console_set_custom_font('rexpaint_cp437_10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)
    libtcod.console_init_root(ROOT_WIDTH, ROOT_HEIGHT, title=GAME_TITLE, order='F')

    consoles, entities, fov_map, game, game_map, key, mouse, player = initialize_new_game()

    while not libtcod.console_is_window_closed():
        # Process input.
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        action = handle_keys(key)

        # Update game.
        update(action, entities, fov_map, game, game_map, player)

        # Render results.
        render_all(action, consoles, entities, fov_map, game_map, player)

        if game.state == GameStates.EXIT:
                return True

if __name__ == '__main__':
    main()