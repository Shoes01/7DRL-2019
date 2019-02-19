import tcod as libtcod

from components.ai import AI, BRAIN
from components.base import Base, Bodyparts, RenderOrder
from components.pos import Position
from components.stats import Stats
from entity import Entity

def create_monster(name):
    if name == 'zombie':
        _ai = AI(brain=BRAIN.ZOMBIE)
        _base = Base(name='zombie', char='Z', color=libtcod.green, render_order=RenderOrder.ACTOR, body=True)
        _pos = Position(0, 0)
        _stats = Stats(attack=5, defense=3, hp_max=30, exp=101)

        monster = Entity(ai=_ai, base=_base, pos=_pos, stats=_stats)

    return monster

def create_item(name):
    if name == 'sword':
        _base = Base(name='sword', char=')', color=libtcod.dark_grey, render_order=RenderOrder.ITEM, body=False, slot=Bodyparts.OFFENSIVE_HAND.name)
        _pos = Position(0, 0)
        _stats = Stats(attack=1, defense=0, hp_max=0, exp=0)

        item = Entity(base=_base, pos=_pos, stats=_stats)
    
    return item