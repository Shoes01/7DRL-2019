from enum import Enum
from random import randint

class Race(Enum):
    HUMAN =     {'bonus': 7,    'char': 'H', 'name': 'human',   'eccentricity': 4,  'loadout': []}

    GOBLIN =    {'bonus': 3,    'char': 'g', 'name': 'goblin',  'eccentricity': 3,  'loadout': [
        ('sword', 'copper'), ('chain mail', 'copper'), ('buckler', 'iron'), ('cap', 'leather'), ('low boots', 'steel'), ('ring', 'quartz')
    ]}
    
    ORC =       {'bonus': 9,    'char': 'O', 'name': 'orc',     'eccentricity': 6,  'loadout': [
        ('helm', 'copper'), ('war hammer', 'iron'), ('ring', 'hematite'), ('plate mail', 'iron'), ('shield', 'steel'), ('greaves', 'steel')
    ]}

def pick_race(difficulty=0):
    choice = randint(1, 100)
    
    if choice < 75 - difficulty * 5:
        return Race.GOBLIN
    
    return Race.ORC