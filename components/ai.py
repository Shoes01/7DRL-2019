from enum import Enum

class BRAIN(Enum):
    ZOMBIE = 0

class AI():
    def __init__(self, brain=None):
        self.awake = False
        self.lost = 0
        self.brain = brain