import tcod as libtcod

from components.ai import AI, BRAIN
from components.base import Base, RenderOrder
from components.body import Body, Bodyparts
from components.pos import Position
from components.equippable import Equippable
from components.skill import Skill
from components.stats import Stats
from entity import Entity

item_list = [
    # Main hand items
    'sword',
    'dagger',
    'hatchet',
    'knife',
    'longsword',
    'axe',
    'wand',
    'mystic wand',
    'staff',
    'mystic staff',
    'cudgel',
    'club',
    # Off hand items
    'shield',
    'buckler',
    'tower shield',
    # Head items
    'helm',
    'great helm',
    'hood',
    # Ring finger items
    'ring',
    # Feet items
    'greaves',
    'sabatons',
    'boots',
    'crakows',
    # Torso items
    'chainmail',
    'tunic',
    'robe',
    'platemail'
]

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
    _pos = Position()
    
    if name == 'sword':
        _base = Base(name='sword', char=')', color=libtcod.dark_grey, render_order=RenderOrder.ITEM)
        
        _profile = {}
        _ATK_profile = {'ATK': 1.2}
        _profile['ATK'] = _ATK_profile
        
        _equip = Equippable(slot=Bodyparts.MainHand.name, profile=_profile)

        _profile = {}
        _ATK_profile = {'ATK': 1.6, 'MAG': 0.2}
        _profile['ATK'] = _ATK_profile

        _skill = Skill(cooldown=12, name='pierce', nature='direct', profile=_profile)
    
    elif name == 'boots':
        _base = Base(name='boots', char='[', color=libtcod.dark_grey, render_order=RenderOrder.ITEM)
        _equip = Equippable(slot=Bodyparts.Feet.name)
        _skill = Skill(cooldown=5, name='leap', nature='direct')
    
    elif name == 'chainmail':
        _base = Base(name='chainmail', char='[', color=libtcod.dark_grey, render_order=RenderOrder.ITEM)
        
        _profile = {}
        _DEF_profile = {'DEF': 1.5}
        _RES_profile = {'RES': 0.5}
        _profile['DEF'] = _DEF_profile
        _profile['RES'] = _RES_profile

        _equip = Equippable(slot=Bodyparts.Torso.name, profile=_profile)
        _skill = Skill(cooldown=0, name='none', nature='none')

    return Entity(base=_base, equip=_equip, pos=_pos, skill=_skill)