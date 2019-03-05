from enum import Enum
from random import randint

class Rank(Enum):
    ZOMBIE = {'name': 'zombie', 'rank': -3}
    HUSK = {'name': 'husk', 'rank': -1}
    THURLL = {'name': 'thrull', 'rank': 0}
    SOLDIER = {'name': 'soldier', 'rank': 3}
    HERO = {'name': 'hero', 'rank': 6}
    CHAMPION = {'name': 'champion', 'rank': 10}

def pick_rank(difficulty=0):
    choice = randint(1, 100)
    
    if choice < 50 - difficulty * 3:
        return Rank.ZOMBIE
    if choice < 70 - difficulty * 3:
        return Rank.HUSK
    if choice < 90 - difficulty * 2:
        return Rank.THURLL
    if choice < 95 - difficulty * 2:
        return Rank.SOLDIER
    if choice < 99 - difficulty * 1:
        return Rank.HERO

    return Rank.CHAMPION