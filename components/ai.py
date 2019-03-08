from enum import Enum

class BRAIN(Enum):
    ZOMBIE = 0
    DEMON = 1

class AI:
    def __init__(self, brain=None):
        self.awake = False
        self.lost = 0
        self.brain = brain
        self.scary_message_1 = False
        self.scary_message_2 = False
        self.low_hp_message_1 = False