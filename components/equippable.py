example_profile = {
    'ATK': {
        'ATK': 1.0,
    },
    'DEF': {
        'DEF': 1.0,
    },
    'MAG': {
        'MAG': 1.0
    },
    'RES': {
        'RES': 1.0
    }
}

class Equippable():
    def __init__(self, slot, profile=example_profile):
        # Slot choices must be from the Bodypart Enum (found in Body.py). It is the name of the Enum.
        self.slot = slot 
        ' Profiles contains the information that dictate how an item deals or prevents damage. '
        self.profile = profile