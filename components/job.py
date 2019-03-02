import tcod as libtcod

from enum import Enum

class Job(Enum):
    ' Jobs determine which part of the soul number is used for which stat. '
    NINJA = {'stats': ('SPD', 'ATK', 'MAG', 'RES', 'HP', 'DEF'), 'color': libtcod.blue}
    PALADIN = {'stats': ('RES', 'HP', 'ATK', 'DEF', 'MAG', 'SPD'), 'color': libtcod.red}
    PHALANX = {'stats': ('DEF', 'HP', 'RES', 'ATK', 'SPD', 'MAG'), 'color': (160, 82, 45)} # Brown