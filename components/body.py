from enum import Enum

class Bodyparts(Enum):
    Head = 0
    Torso = 1
    LeftHand = 2
    RightHand = 3
    Feet = 4

class Body():
    def __init__(self):
        self.head = None
        self.torso = None
        self.left_hand = None
        self.right_hand = None
        self.feet = None

    @property
    def parts(self):
        parts = {Bodyparts.Head.name: self.head,
                Bodyparts.Torso.name: self.torso,
                Bodyparts.LeftHand.name: self.left_hand,
                Bodyparts.RightHand.name: self.right_hand,
                Bodyparts.Feet.name: self.feet}
        
        return parts