import tcod as libtcod

from components.race import Race
from enum import Enum

_brown = (160, 82, 45)

class Job(Enum):
    ' Jobs determine which part of the soul number is used for which stat. '
    NINJA =     {'stats': ('SPD', 'ATK', 'MAG', 'RES',  'HP', 'DEF'), 'color': libtcod.blue,    'name': 'ninja'}
    PALADIN =   {'stats': ('RES',  'HP', 'ATK', 'DEF', 'MAG', 'SPD'), 'color': libtcod.red,     'name': 'paladin'}
    PHALANX =   {'stats': ('DEF',  'HP', 'RES', 'ATK', 'SPD', 'MAG'), 'color': _brown,          'name': 'phalanx'}
    WARRIOR =   {'stats': ('DEF',  'HP', 'ATK', 'SPD', 'RES', 'MAG'), 'color': libtcod.green,   'name': 'warrior'}
    WIZARD =    {'stats': ('MAG', 'RES', 'DEF', 'SPD',  'HP', 'ATK'), 'color': libtcod.blue,    'name': 'wizard'}
    BOSS =      {'stats': ('ATK', 'MAG', 'SPD',  'HP', 'DEF', 'RES'), 'color': libtcod.darker_crimson,    'name': 'prince'}
    BARBARIAN = {'stats': ('ATK',  'HP', 'SPD', 'DEF', 'RES', 'MAG'), 'color': libtcod.red,     'name': 'barbarian'}

def pick_job(race):
    if race == Race.GOBLIN:
        return Job.WARRIOR
    if race == Race.ORC:
        return Job.WARRIOR
    if race == Race.KOBOLD:
        return Job.WIZARD