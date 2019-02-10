import tcod as libtcod

from components.ai import ZombieAI
from components.base import Base
from components.pos import Position
from entity import Entity

def create_monster():
    _ai = ZombieAI()
    _base = Base('Monster', 'M', libtcod.green)
    _pos = Position(0, 0)

    monster = Entity(ai=_ai, base=_base, pos=_pos)

    return monster