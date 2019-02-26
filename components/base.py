from enum import Enum

class RenderOrder(Enum):
    CORPSE = 0
    ITEM = 1
    ACTOR = 2

class Base:
    def __init__(self, name, char, color, render_order):
        self.name = name
        self.char = char
        self.color = color
        self.render_order = render_order