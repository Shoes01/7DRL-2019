from enum import auto, Enum

class RenderOrder(Enum):
    CORPSE = auto()
    ITEM = auto()
    ACTOR = auto()

class Base:
    def __init__(self, name, char, color, render_order):
        self.name = name
        self.char = char
        self.color = color
        self.render_order = render_order