import tcod as libtcod

from components.body import Bodyparts

def handle_keys(game_state_machine, key):
    _game_state = game_state_machine.state.__str__()

    if _game_state == 'OpenInventory':
        return handle_inventory_keys(key)
    elif _game_state == 'LeveledUp':
        return handle_level_up_keys(key)
    elif _game_state == 'TargetingState':
        return handle_targeting_state_keys(key)
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

    # Inventory related keys.
    if key_char == 'g':
        return {'grab': True}
    if key_char == 'i':
        return {'inventory': True}

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

def handle_inventory_keys(key):
    index = key.c - ord('a')
    key_char = chr(key.c)

    if key_char == 'd' and key.shift:
        return {'drop': True}

    if key_char == 'e' and key.shift:
        return {'equip': True}

    if key_char == 'u' and key.shift:
        return {'unequip': True}

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

def handle_targeting_state_keys(key):
    # Movement keys
    movement = handle_generic_movement_keys(key)
    if movement:
        return movement
    
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

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