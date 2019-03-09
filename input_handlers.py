import tcod as libtcod

from components.body import Bodyparts

def handle_keys(game_state_machine, key):
    _game_state = game_state_machine.state.__str__()

    if _game_state == 'CompareItems':
        return handle_compare_items_keys(key)
    elif _game_state == 'ConsumeSoul':
        return handle_consume_soul_keys(key)
    else:
        return handle_general_keys(key)

def handle_general_keys(key):
    key_char = chr(key.c)

    # Movement keys
    movement = handle_generic_movement_keys(key)
    if movement:
        return movement

    # Item related keys.
    if key_char == 'q':
        return {'skill_choice': Bodyparts.RingFinger.name}
    if key_char == 'w':
        return {'skill_choice': Bodyparts.Head.name}
    if key_char == 'e':
        return {'skill_choice': Bodyparts.Feet.name}
    if key_char == 'a':
        return {'skill_choice': Bodyparts.OffHand.name}
    if key_char == 's':
        return {'skill_choice': Bodyparts.Torso.name}
    if key_char == 'd' and not key.lctrl:
        return {'skill_choice': Bodyparts.MainHand.name}

    # General purpose key.
    if key.vk == libtcod.KEY_SPACE:
        return {'interact': True}

    # Other keys
    if key_char == 'd' and key.lctrl:
        return {'debug_toggle': True}
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}

def handle_generic_movement_keys(key):
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
    
    return {}

def handle_compare_items_keys(key):
    if key.vk == libtcod.KEY_KP5 or key.vk == libtcod.KEY_KPENTER or key.vk == libtcod.KEY_ENTER:
        return {'confirm': True}
    elif key.vk == libtcod.KEY_SPACE:
        return {'confirm': False}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}
    
    return {}

def handle_consume_soul_keys(key):
    key_char = chr(key.c)

    # Flip the soul.
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

    # Confirmation keys.
    if key.vk == libtcod.KEY_KP5 or key.vk == libtcod.KEY_KPENTER or key.vk == libtcod.KEY_ENTER:
        return {'confirm': True}
    elif key.vk == libtcod.KEY_SPACE:
        return {'confirm': False}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}
    
    return {}