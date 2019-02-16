import tcod as libtcod

from game import GameStates

def handle_keys(game, key):
    if game.state == GameStates.OPEN_INVENTORY:
        return handle_inventory_keys(key)
    elif game.state == GameStates.LEVEL_UP:
        return handle_level_up_keys(key)
    else:
        return handle_general_keys(key)

def handle_general_keys(key):
    key_char = chr(key.c)

    # Movement keys
    if key.vk == libtcod.KEY_UP or key_char == 'k' or key.vk == libtcod.KEY_KP8:
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN or key_char == 'j' or key.vk == libtcod.KEY_KP2:
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT or key_char == 'h' or key.vk == libtcod.KEY_KP4:
        return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT or key_char == 'l' or key.vk == libtcod.KEY_KP6:
        return {'move': (1, 0)}
    elif key_char == 'y' or key.vk == libtcod.KEY_KP7:
        return {'move': (-1, -1)}
    elif key_char == 'u' or key.vk == libtcod.KEY_KP9:
        return {'move': (1, -1)}
    elif key_char == 'b' or key.vk == libtcod.KEY_KP1:
        return {'move': (-1, 1)}
    elif key_char == 'n' or key.vk == libtcod.KEY_KP3:
        return {'move': (1, 1)}
    elif key_char == '.' or key.vk == libtcod.KEY_KP5:
        return {'wait': True}

    # Inventory related keys.
    if key_char == 'g':
        return {'grab': True}
    if key_char == 'i':
        return {'inventory': True}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}

def handle_inventory_keys(key):
    index = key.c - ord('a')
    key_char = chr(key.c)

    if key_char == 'd' and key.shift:
        return {'drop': True}

    if index >= 0:
        return {'inventory_choice': index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

    return {}

def handle_level_up_keys(key):
    index = key.c - ord('a')

    if key.vk == libtcod.KEY_ENTER:
        return {'confirm': True}

    if index >= 0:
        return {'level_up_choice': index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

    return {}
