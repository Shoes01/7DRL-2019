from enum import Enum
from random import randint, choice

class Race(Enum):
    # The player is the only human.
    HUMAN = {
        'bonus': 5,    
        'char': 'H', 
        'name': 'human',   
        'eccentricity': 4,  
        'loadout': []}

    GOBLIN = {
        'bonus': 3,    
        'char': 'g', 
        'name': 'goblin',  
        'eccentricity': 3,  
        'loadout': [
            ('sword', 'copper'), 
            ('chain mail', 'copper'), 
            ('buckler', 'iron'), 
            ('cap', 'leather'), 
            ('low boots', 'steel'), 
            ('ring', 'quartz')
            ]
        }
    
    ORC = {
        'bonus': 9,    
        'char': 'O', 
        'name': 'orc',     
        'eccentricity': 6,  
        'loadout': [
            ('helm', 'copper'), 
            ('spear', 'iron'), 
            ('ring', 'hematite'), 
            ('plate mail', 'iron'), 
            ('shield', 'steel'), 
            ('greaves', 'steel')
            ]
        }
    
    KOBOLD = {
        'bonus': 1,
        'char': 'k',
        'name': 'kobold',
        'eccentricity': 10,
        'loadout': [
            ('wand', 'MDF'),
            ('boots', 'leather'),
            ('boots', 'leather'),
            ('boots', 'leather'),
            ('boots', 'leather'),
            ('boots', 'leather')
        ]
    }

    DEMON = {
        'bonus': 15,    
        'char': '&', 
        'name': 'demon',     
        'eccentricity': 10,  
        'loadout': []
        }

def pick_race(difficulty=0):
    _choice = randint(1, 100)
    
    if _choice < 75 - difficulty * 5:
        return choice((Race.KOBOLD, Race.GOBLIN))
    
    return Race.ORC