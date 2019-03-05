def example_profile():
    return {
                'ATK': {
                    'ATK': 0.0,
                    'DEF': 0.0,
                    'MAG': 0.0,
                    'RES': 0.0,
                    'SPD': 0.0,
                    'HP' : 0.0
                },
                'DEF': {
                    'ATK': 0.0,
                    'DEF': 0.0,
                    'MAG': 0.0,
                    'RES': 0.0,
                    'SPD': 0.0,
                    'HP' : 0.0
                },
                'MAG': {
                    'ATK': 0.0,
                    'DEF': 0.0,
                    'MAG': 0.0,
                    'RES': 0.0,
                    'SPD': 0.0,
                    'HP' : 0.0
                },
                'RES': {
                    'ATK': 0.0,
                    'DEF': 0.0,
                    'MAG': 0.0,
                    'RES': 0.0,
                    'SPD': 0.0,
                    'HP' : 0.0
                },
                'HP': {
                    'ATK': 0.0,
                    'DEF': 0.0,
                    'MAG': 0.0,
                    'RES': 0.0,
                    'SPD': 0.0,
                    'HP' : 0.0
                },
                'SPD': {
                    'ATK': 0.0,
                    'DEF': 0.0,
                    'MAG': 0.0,
                    'RES': 0.0,
                    'SPD': 1.0,     # The default for SPD should be the entity's stat
                    'HP' : 0.0
                }
            }

class Equippable():
    def __init__(self, slot, profile=example_profile()):
        # Slot choices must be from the Bodypart Enum (found in Body.py). It is the name of the Enum.
        self.slot = slot 
        ' Profiles contains the information that dictate how an item deals or prevents damage. '
        self.profile = profile