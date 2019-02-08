import tcod as libtcod

from game import FOV_RADIUS, GameStates, GAME_TITLE, SCREEN_HEIGHT, SCREEN_WIDTH, initialize_new_game
from input_handlers import handle_keys
from systems.fov import recompute_fov
from systems.render import clear_all, render_all
from systems.update import update

def main():
    libtcod.console_set_custom_font('rexpaint_cp437_10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)
    libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, title=GAME_TITLE)

    con, entities, fov_map, game, game_map, key, mouse, player = initialize_new_game()

    recompute_fov(fov_map, player.pos.x, player.pos.y, FOV_RADIUS)

    while not libtcod.console_is_window_closed():
        # Process input.
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        action = handle_keys(key)

        # Update game.
        update(action, entities, game, player)

        if game.state == GameStates.EXIT:
                return True

        # Render results.
        if action:
                recompute_fov(fov_map, player.pos.x, player.pos.y, FOV_RADIUS)

        render_all(con, entities, fov_map, game_map)
        libtcod.console_flush()
        clear_all(con, entities)

if __name__ == '__main__':
    main()