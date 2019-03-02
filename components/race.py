from enum import Enum

class Race(Enum):
    RAT =       {'bonus': 1,    'char': 'r', 'name': 'rat'}
    KOBOLD =    {'bonus': 2,    'char': 'k', 'name': 'kobold'}
    GOBLIN =    {'bonus': 3,    'char': 'g', 'name': 'goblin'}
    DWARF =     {'bonus': 5,    'char': 'D', 'name': 'dwarf'}
    HUMAN =     {'bonus': 7,    'char': 'H', 'name': 'human'}
    ORC =       {'bonus': 9,    'char': 'O', 'name': 'orc'}
    TROLL =     {'bonus': 12,   'char': 'T', 'name': 'troll'}