from systems.death import kill

def attack(attacker, defender):
    damage = attacker.stats.attack - defender.stats.defense

    defender.stats.hp -= damage

    if defender.stats.hp <= 0:
        kill(defender)