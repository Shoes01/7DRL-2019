import tcod as libtcod

"""
This system handles the level progression of the player.
The formula is: S = 100 * (1 - 1.1^n) / (1 - 1.1), where n is the current level.
In short, the player needs 10% more exp for the next level.
"""

def gain_exp(exp, player):
    turn_results = []

    player.stats.exp += exp
    message = 'You gain {0} experience.'.format(exp)
    color = libtcod.purple
    turn_results.append({'message': (message, color)})

    if player.stats.exp >= player.stats.exp_needed_for_next_level:
        player.stats.level += 1
        turn_results.append({'level_up': True})
        message = 'You are now level {0}.'.format(player.stats.level)
        color = libtcod.purple
        turn_results.append({'message': (message, color)})

        turn_results.append({'redraw_map': True})
    
    return turn_results

def level_up_choice(index, player):
    turn_results = []

    iter = 0
    for stat in list(player.stats.__dict__.keys()):
        if index == iter:
            if player.stats.selected == None:
                # You choose this stat.
                player.stats.selected = stat
                message = 'You select the {0}.'.format(stat.capitalize())
                color = libtcod.cyan
                turn_results.append({'message': (message, color)})
            elif player.stats.selected == stat:
                # You deselect the item you already chose.
                player.stats.selected = None
                message = 'You deselect the {0}.'.format(stat.capitalize())
                color = libtcod.cyan
                turn_results.append({'message': (message, color)})
            elif player.stats.selected:
                # You select a different item, deslecting the one you already chose.
                player.stats.selected = stat
                message = 'You select the {0}.'.format(stat.capitalize())
                color = libtcod.cyan
                turn_results.append({'message': (message, color)})
            break
        iter += 1

    return turn_results

def confirm_stat_gain(player):
    turn_results = []

    if player.stats.selected == 'base_attack':
        player.stats.base_attack += 2
    elif player.stats.selected == 'base_defense':
        player.stats.base_defense += 2
    elif player.stats.selected == 'base_hp_max':
        player.stats.hp += 10
        player.stats.base_hp_max += 10
    else:
        _message = 'You must pick a stat to upgrade.'
        _color = libtcod.red
        turn_results.append({'message': (_message, _color)})
        return turn_results

    
    _message = 'You feel stronger!'
    _color = libtcod.purple
    turn_results.append({'message': (_message, _color)})
    turn_results.append({'previous_state': True})

    player.stats.selected = None

    return turn_results