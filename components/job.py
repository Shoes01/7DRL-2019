from enum import Enum

class Job(Enum):
    ' Jobs determine which part of the soul number is used for which stat. '
    NINJA = ('SPD', 'ATK', 'MAG', 'RES', 'HP', 'DEF')
    PALADIN = ('RES', 'HP', 'ATK', 'DEF', 'MAG', 'SPD')
    PHALANX = ('DEF', 'HP', 'RES', 'ATK', 'SPD', 'MAG')