import tcod as libtcod

from enum import Enum
from random import randint

class Rank(Enum):
    ZOMBIE =    {'name': 'zombie',      'rank': 0, 'color': libtcod.dark_cyan}
    HUSK =      {'name': 'husk',        'rank': 1, 'color': libtcod.dark_sea}
    THURLL =    {'name': 'thrull',      'rank': 2,  'color': libtcod.dark_chartreuse}
    SOLDIER =   {'name': 'soldier',     'rank': 3,  'color': libtcod.dark_yellow}
    HERO =      {'name': 'hero',        'rank': 5,  'color': libtcod.dark_orange}
    CHAMPION =  {'name': 'champion',    'rank': 10, 'color': libtcod.dark_red}
    DEMON =     {'name': '',            'rank': 20, 'color': libtcod.gold}

def pick_rank(difficulty=0):
    choice = randint(1, 100)
    
    if choice < 30 - difficulty * 3:
        return Rank.ZOMBIE
    if choice < 60 - difficulty * 3:
        return Rank.HUSK
    if choice < 80 - difficulty * 2:
        return Rank.THURLL
    if choice < 90 - difficulty * 2:
        return Rank.SOLDIER
    if choice < 95 - difficulty * 1:
        return Rank.HERO

    return Rank.CHAMPION