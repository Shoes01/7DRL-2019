from enum import auto, Enum

class Bodyparts(Enum):
    HEAD = 0
    OFFENSIVE_HAND = 1
    DEFENSIVE_HAND = 2
    TORSO = 3
    FEET = 4

class RenderOrder(Enum):
    CORPSE = auto()
    ITEM = auto()
    ACTOR = auto()

class Base:
    def __init__(self, name, char, color, render_order, body=True, slot=None):
        self.name = name
        self.char = char
        self.color = color
        self.render_order = render_order
        
        if body:
            self.body = {   Bodyparts.HEAD.name: None,
                            Bodyparts.OFFENSIVE_HAND.name: None,
                            Bodyparts.DEFENSIVE_HAND: None,
                            Bodyparts.TORSO.name: None,
                            Bodyparts.FEET.name: None}
        
        self.slot = slot