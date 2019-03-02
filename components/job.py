from enum import Enum

class Job(Enum):
    ' Jobs determine which part of the soul number is used for which stat. '
    NINJA = ('SPD', 'ATT', 'MAG', 'RES', 'HP', 'DEF')
    PALADIN = ('RES', 'HP', 'ATT', 'DEF', 'MAG', 'SPD')
    PHALANX = ('DEF', 'HP', 'RES', 'ATT', 'SPD', 'MAG')