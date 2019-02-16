import tcod as libtcod

from systems.death import kill
from systems.progression import gain_exp

def attack(attacker, defender):
    turn_results = []
    
    damage = attacker.stats.attack - defender.stats.defense

    defender.stats.hp -= damage

    turn_results.append({'message': ('The {0} deals {1} damage to the {2}.'.format(attacker.base.name.capitalize(), damage, defender.base.name.capitalize()), libtcod.yellow)})

    if defender.stats.hp <= 0:
        turn_results.extend(kill(defender))
        if not attacker.ai:
            turn_results.extend(gain_exp(defender.stats.exp, attacker))
    
    return turn_results