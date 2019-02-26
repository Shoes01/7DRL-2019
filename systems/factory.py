import tcod as libtcod

from components.ai import AI, BRAIN
from components.base import Base, RenderOrder
from components.body import Body, Bodyparts
from components.pos import Position
from components.equippable import Equippable
from components.skill import Skill
from components.stats import Stats
from entity import Entity

def create_monster(name):
    if name == 'zombie':
        _ai = AI(brain=BRAIN.ZOMBIE)
        _base = Base(name='zombie', char='Z', color=libtcod.green, render_order=RenderOrder.ACTOR)
        _body = Body()
        _pos = Position()
        _stats = Stats(attack=5, defense=3,  exp=101, hp_max=30, magic=0, resistance=0, speed=0)

        monster = Entity(ai=_ai, base=_base, body=_body, pos=_pos, stats=_stats)

    return monster

def create_item(name):
    if name == 'sword':
        _base = Base(name='sword', char=')', color=libtcod.dark_grey, render_order=RenderOrder.ITEM)
        _equip = Equippable(slot=Bodyparts.MainHand.name)
        _pos = Position()
        _skill = Skill(nature='direct', skill='pierce')
        _stats = Stats(1, 0, 0, 0, 0, 0, 0)

        item = Entity(base=_base, equip=_equip, pos=_pos, skill=_skill, stats=_stats)
    
    return item