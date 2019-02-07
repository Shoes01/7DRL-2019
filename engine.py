import tcod as libtcod

from game import GameStates, GAME_TITLE, SCREEN_HEIGHT, SCREEN_WIDTH, initialize_new_game
from input_handlers import handle_keys
from map_functions import GameMap
from systems.render import clear_all, render_all
from systems.update import update

def main():
    libtcod.console_set_custom_font('rexpaint_cp437_10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)
    libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, title=GAME_TITLE)

    con, entities, game, game_map, key, mouse, player = initialize_new_game()

    while not libtcod.console_is_window_closed():
        # Process input.
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        action = handle_keys(key)

        # Update game.
        update(action, entities, game, player)
        if game.state == GameStates.EXIT:
                return True

        # Render results.
        render_all(con, entities, game_map)
        libtcod.console_flush()
        clear_all(con, entities)

if __name__ == '__main__':
    main()