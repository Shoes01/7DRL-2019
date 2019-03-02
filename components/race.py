from enum import Enum

class Race(Enum):
    RAT = {'bonus': 1, 'char': 'r'}
    KOBOLD = {'bonus': 2, 'char': 'k'}
    GOBLIN = {'bonus': 3, 'char': 'g'}
    DWARF = {'bonus': 5, 'char': 'D'}
    HUMAN = {'bonus': 7, 'char': 'H'}
    ORC = {'bonus': 9, 'char': 'O'}
    TROLL = {'bonus': 12, 'char': 'T'}