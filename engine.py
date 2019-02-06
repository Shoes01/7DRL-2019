import tcod as libtcod

from game import GAME_TITLE, SCREEN_HEIGHT, SCREEN_WIDTH
from input_handlers import handle_keys
from map_functions import GameMap
from systems.render import clear, render
from systems.update import update

def main():
    libtcod.console_set_custom_font('rexpaint_cp437_10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)
    libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, title=GAME_TITLE)

    con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
    game_map = GameMap(SCREEN_WIDTH, SCREEN_HEIGHT)
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        # Process input.
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        action = handle_keys(key)

        # Update game.
        update(action)

        # Render results.
        render(con, game_map)   # TODO: Need a system for this.
        libtcod.console_flush
        clear()                 # TODO: Need a system for this too.

if __name__ == '__main__':
    main()