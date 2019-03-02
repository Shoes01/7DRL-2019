import tcod as libtcod

from enum import Enum

_brown = (160, 82, 45)

class Job(Enum):
    ' Jobs determine which part of the soul number is used for which stat. '
    NINJA =     {'stats': ('SPD', 'ATK', 'MAG', 'RES', 'HP', 'DEF'), 'color': libtcod.blue,     'name': 'ninja'}
    PALADIN =   {'stats': ('RES', 'HP', 'ATK', 'DEF', 'MAG', 'SPD'), 'color': libtcod.red,      'name': 'paladin'}
    PHALANX =   {'stats': ('DEF', 'HP', 'RES', 'ATK', 'SPD', 'MAG'), 'color': _brown,           'name': 'phalanx'}