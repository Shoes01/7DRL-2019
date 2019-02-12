import tcod as libtcod

from systems.death import kill

def attack(attacker, defender):
    turn_results = []
    
    damage = attacker.stats.attack - defender.stats.defense

    defender.stats.hp -= damage

    turn_results.append({'message': ('The {0} deals {1} damage to the {2}.'.format(attacker.base.name.capitalize(), damage, defender.base.name.capitalize()), libtcod.yellow)})

    if defender.stats.hp <= 0:
        turn_results.extend(kill(defender))
    
    return turn_results