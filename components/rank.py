from enum import Enum
from random import randint

class Rank(Enum):
    ZOMBIE = -3
    HUSK = -1
    THURLL = 0
    SOLDIER = 3
    HERO = 6
    CHAMPION = 10

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