from enum import Enum

class Bodyparts(Enum):
    Head = 0
    Torso = 1
    MainHand = 2
    OffHand = 3
    Feet = 4
    RingFinger = 5

class Body():
    def __init__(self):
        self.head = None
        self.torso = None
        self.main_hand = None
        self.off_hand = None
        self.feet = None
        self.ring_finger = None

    @property
    def parts(self):
        parts = {Bodyparts.Head.name: self.head,
                Bodyparts.Torso.name: self.torso,
                Bodyparts.MainHand.name: self.main_hand,
                Bodyparts.OffHand.name: self.off_hand,
                Bodyparts.Feet.name: self.feet,
                Bodyparts.RingFinger.name: self.ring_finger}
        
        return parts