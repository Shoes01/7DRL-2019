import tcod as libtcod

from components.ai import AI, BRAIN
from components.base import Base, RenderOrder
from components.pos import Position
from components.stats import Stats
from entity import Entity

def create_monster():
    _ai = AI(brain=BRAIN.ZOMBIE)
    _base = Base('Zombie', 'Z', libtcod.green, RenderOrder.ACTOR)
    _pos = Position(0, 0)
    _stats = Stats(attack=5, defense=3, hp_max=30, exp=101)

    monster = Entity(ai=_ai, base=_base, pos=_pos, stats=_stats)

    return monster