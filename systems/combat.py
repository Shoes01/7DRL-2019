import tcod as libtcod

from systems.death import kill
from systems.progression import gain_exp

def attack(attacker, defender, entities):
    turn_results = []
    
    damage = attacker.stats.attack - defender.stats.defense

    if damage <= 0:
        damage = 0
        _message = 'The {0} takes no damage!'.format(defender.base.name.capitalize())
        _color = libtcod.light_yellow
        turn_results.append({'message': (_message, _color)})
    else:
        defender.stats.hp -= damage
        turn_results.append({'message': ('The {0} deals {1} damage to the {2}.'.format(attacker.base.name.capitalize(), damage, defender.base.name.capitalize()), libtcod.yellow)})

    if defender.stats.hp <= 0:
        turn_results.extend(kill(defender, entities))
        if not attacker.ai:
            turn_results.extend(gain_exp(defender.stats.exp, attacker))
    
    return turn_results