import random
import tcod as libtcod

from components.ai import AI, BRAIN
from components.base import Base, RenderOrder
from components.body import Body, Bodyparts
from components.equippable import Equippable, example_profile
from components.health import Health
from components.inventory import Inventory
from components.job import Job
from components.pos import Position
from components.race import Race, pick_race
from components.rank import Rank, pick_rank
from components.skill import Skill
from components.soul import Soul
from components.stats import Stats
from components.status import Status
from entity import Entity
from systems.stats import get_stats

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
    'ruby ring',
    'sapphire ring',
    'quartz ring',
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

def create_soul(entity):
    _soul_rank = entity.soul.rank
    _soul_eccentricity = entity.soul.eccentricity
    _soul_number = entity.soul.soul

    _soul = Soul(_soul_eccentricity, _soul_rank)
    _soul.number = _soul_number

    _base = Base(name='soul', char='*', color=libtcod.dark_green, render_order=RenderOrder.SOUL)
    _pos = Position()

    soul_item = Entity(base=_base, pos=_pos, soul=_soul)

    return soul_item

def create_monster(name, difficulty=0):
    if name == 'player':
        _base = Base(name='player', char='@', color=libtcod.white, render_order=RenderOrder.ACTOR)
        _body = Body()
        _health = Health()
        _inv = Inventory()
        _job = Job.PALADIN
        _pos = Position()
        _race = Race.DEBUG # Players will be HUMAN...
        _soul = Soul(eccentricity=5, rank=10)
        _status = Status()

        monster = Entity(base=_base, body=_body, health=_health, inv=_inv, job=_job, pos=_pos, race=_race, soul=_soul, status=_status)
        monster.health.points = monster.health.max

    elif name == 'zombie':
        _ai = AI(brain=BRAIN.ZOMBIE)
        _body = Body()
        _health = Health()
        _job = random.choice(list(Job))
        _pos = Position()
        _race = random.choice(list(Race))
        _soul = Soul(eccentricity=3, rank=-1)
        _status = Status()

        _name = 'Zombie' + ' ' + str(_race.value['name']).capitalize() + ' ' + str(_job.value['name']).capitalize()
        _color = _job.value['color']
        _char = _race.value['char']

        _base = Base(name=_name, char=_char, color=_color, render_order=RenderOrder.ACTOR)

        monster = Entity(ai=_ai, base=_base, body=_body, health=_health, job=_job, pos=_pos, race=_race, soul=_soul, status=_status)
        monster.health.points = monster.health.max

    return monster

def create_monster_(difficulty):
    _rank = pick_rank(difficulty)
    _race = pick_race(difficulty)
    _job = random.choice(list(Job)) # Monsters might not have jobs....

    _ai = AI(brain=BRAIN.ZOMBIE)
    _body = Body()
    _health = Health()
    _pos = Position()
    _soul = Soul(eccentricity=3, rank=_rank.value)
    _status = Status()




def create_item(name):
    _pos = Position()
    
    if name == 'sword':
        _base = Base(name='sword', char=')', color=libtcod.dark_grey, render_order=RenderOrder.ITEM)
        
        _profile = {}
        _profile = example_profile()
        _profile['ATK']['ATK'] = 1.2
        
        _equip = Equippable(slot=Bodyparts.MainHand.name, profile=_profile)

        _profile = {}
        _profile = example_profile()
        _profile['ATK']['ATK'] = 1.6
        _profile['ATK']['MAG'] = 0.2

        _skill = Skill(cooldown=12, name='pierce', nature='direct', profile=_profile)
    
    elif name == 'boots':
        _base = Base(name='boots', char='[', color=libtcod.dark_grey, render_order=RenderOrder.ITEM)
        _equip = Equippable(slot=Bodyparts.Feet.name)
        _skill = Skill(cooldown=5, name='leap', nature='direct')
    
    elif name == 'chainmail':
        _base = Base(name='chainmail', char='[', color=libtcod.dark_grey, render_order=RenderOrder.ITEM)
        
        _profile = {}
        _profile = example_profile()
        _profile['DEF']['DEF'] = 1.5
        _profile['RES']['RES'] = 0.5

        _equip = Equippable(slot=Bodyparts.Torso.name, profile=_profile)
        _skill = Skill(cooldown=0, name='none', nature='none')

    elif name == 'shield':
        _base = Base(name='shield', char='[', color=libtcod.dark_grey, render_order=RenderOrder.ITEM)        
        _equip = Equippable(slot=Bodyparts.OffHand.name)

        _profile = {}
        _profile = example_profile()
        _profile['ATK']['DEF'] = 2.0

        _skill = Skill(cooldown=5, name='bash', nature='direct', profile=_profile)

    return Entity(base=_base, equip=_equip, pos=_pos, skill=_skill)