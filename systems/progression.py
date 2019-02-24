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

    if player.stats.selected == 'attack':
        player.stats.attack += 2
    elif player.stats.selected == 'defense':
        player.stats.defense += 2
    elif player.stats.selected == 'hp_max':
        player.stats.hp += 10
        player.stats.hp_max += 10
    else:
        _message = 'You must pick a stat to upgrade.'
        _color = libtcod.red
        turn_results.append({'message': (_message, _color)})
        return turn_results

    player.stats.exp_needed_for_next_level = int(100 * (1 - player.stats.leveling_factor ** player.stats.level) / (1 - player.stats.leveling_factor))
    
    _message = 'You feel stronger!'
    _color = libtcod.purple
    turn_results.append({'message': (_message, _color)})

    player.stats.selected = None

    return turn_results