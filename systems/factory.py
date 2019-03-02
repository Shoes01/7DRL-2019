import random
import tcod as libtcod

from components.ai import AI, BRAIN
from components.base import Base, RenderOrder
from components.body import Body, Bodyparts
from components.equippable import Equippable
from components.inventory import Inventory
from components.job import Job
from components.pos import Position
from components.race import Race
from components.skill import Skill
from components.soul import Soul
from components.stats import Stats
from components.status import Status
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
    if name == 'player':
        _base = Base(name='player', char='@', color=libtcod.white, render_order=RenderOrder.ACTOR)
        _body = Body()
        _inv = Inventory()
        _job = Job.PALADIN
        _pos = Position(15, 15)
        _race = Race.HUMAN
        _soul = Soul(eccentricity=1, rank=-3)
        _stats = Stats(attack=8, defense=3, exp=0, hp_max=50, magic=0, resistance=0, speed=0)
        _status = Status()

        monster = Entity(base=_base, body=_body, inv=_inv, job=_job, pos=_pos, race=_race, soul=_soul, stats=_stats, status=_status)

    elif name == 'zombie':
        _ai = AI(brain=BRAIN.ZOMBIE)
        _body = Body()
        _job = random.choice(list(Job))
        _pos = Position()
        _race = random.choice(list(Race))
        _soul = Soul(eccentricity=3, rank=-1)
        _stats = Stats(attack=5, defense=3,  exp=101, hp_max=10, magic=0, resistance=0, speed=0)
        _status = Status()

        _name = 'Zombie' + ' ' + str(_race.value['name']).capitalize() + ' ' + str(_job.value['name']).capitalize()
        _color = _job.value['color']
        _char = _race.value['char']

        _base = Base(name=_name, char=_char, color=_color, render_order=RenderOrder.ACTOR)

        monster = Entity(ai=_ai, base=_base, body=_body, job=_job, pos=_pos, race=_race, soul=_soul, stats=_stats, status=_status)

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

    elif name == 'shield':
        _base = Base(name='shield', char='[', color=libtcod.dark_grey, render_order=RenderOrder.ITEM)
        
        _profile = {}
        _DEF_profile = {'DEF': 1.5}
        _profile['DEF'] = _DEF_profile
        
        _equip = Equippable(slot=Bodyparts.OffHand.name, profile=_profile)

        _profile = {}
        _ATK_profile = {'DEF': 2.0}
        _profile['ATK'] = _ATK_profile

        _skill = Skill(cooldown=5, name='bash', nature='direct', profile=_profile)


    return Entity(base=_base, equip=_equip, pos=_pos, skill=_skill)