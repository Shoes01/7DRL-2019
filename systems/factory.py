import random
import tcod as libtcod

from components.ai import AI, BRAIN
from components.base import Base, RenderOrder
from components.body import Body, Bodyparts
from components.equippable import Equippable, example_profile
from components.health import Health
from components.inventory import Inventory
from components.job import Job, pick_job
from components.pos import Position
from components.race import Race, pick_race
from components.rank import Rank, pick_rank
from components.skill import Skill
from components.soul import Soul
from components.stats import Stats
from components.status import Status
from entity import Entity
from systems.equip import equip_
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

def create_monster(name):
    if name == 'player':
        _base = Base(name='player', char='@', color=libtcod.white, render_order=RenderOrder.ACTOR)
        _body = Body()
        _health = Health()
        _inv = Inventory()
        _job = Job.PALADIN
        _pos = Position()
        _race = Race.HUMAN
        _soul = Soul(eccentricity=5, rank=10)
        _status = Status()

        monster = Entity(base=_base, body=_body, health=_health, inv=_inv, job=_job, pos=_pos, race=_race, soul=_soul, status=_status)
        monster.health.points = monster.health.max

    return monster

def create_monster_(difficulty):
    _rank = pick_rank(difficulty)
    _race = pick_race(difficulty)
    _job = pick_job(_race)

    _ai = AI(brain=BRAIN.ZOMBIE)
    _body = Body()
    _health = Health()
    _pos = Position()
    _soul = Soul(eccentricity=_race.value['eccentricity'], rank=_rank.value['rank'])
    _status = Status()

    _name = str(_rank.value['name']).capitalize() + ' ' + str(_race.value['name']).capitalize() + ' ' + str(_job.value['name']).capitalize()
    _color = _rank.value['color']
    _char = _race.value['char']

    _base = Base(name=_name, char=_char, color=_color, render_order=RenderOrder.ACTOR)

    monster = Entity(ai=_ai, base=_base, body=_body, health=_health, job=_job, pos=_pos, race=_race, soul=_soul, status=_status)
    monster.health.points = monster.health.max

    equip_monster(monster)

    return monster

def equip_monster(monster):
    for value in monster.race.value['loadout']:
        _name = value[0]
        _material = value[1]

        item = create_item_(_name, _material)

        if item:
            equip_(item, monster)            

material_dict = {
    'leather':  (0.1, libtcod.sepia),
    'copper':   (0.2, libtcod.brass),
    'iron':     (0.5, libtcod.dark_grey),
    'steel':    (1.0, libtcod.silver),
    'quartz':   (0.0, (221, 221, 223)),
    'hematite': (0.0, libtcod.darker_crimson)
}

def create_item_(name, material):
    _base, _equip, _skill = None, None, None

    _base, _equip, _skill = create_mainhand_item(name, material)
    if _base:
        return Entity(base=_base, equip=_equip, pos=Position(), skill=_skill)
    _base, _equip, _skill = create_torso_item(name, material)
    if _base:
        return Entity(base=_base, equip=_equip, pos=Position(), skill=_skill)
    _base, _equip, _skill = create_offhand_item(name, material)
    if _base:
        return Entity(base=_base, equip=_equip, pos=Position(), skill=_skill)
    
    return None

def create_mainhand_item(name, material):
    _bonus = material_dict[material][0]
    _color = material_dict[material][1]

    _base, _equip, _skill = None, None, None

    if name == 'sword':
        _base = Base(name=name, char=u'\u2193', color=_color, render_order=RenderOrder.ITEM)

        _profile = {}
        _profile = example_profile()
        _profile['ATK']['ATK'] = 1.8 + _bonus

        _equip = Equippable(slot=Bodyparts.MainHand.name, profile=_profile)

        _profile = {}
        _profile = example_profile()
        _profile['ATK']['ATK'] = 1.6 + _bonus
        _profile['ATK']['MAG'] = 0.2 + _bonus

        _skill = Skill(cooldown=12, name='pierce', nature='direct', profile=_profile)

    if name == 'spear':
        _base = Base(name=name, char=u'\u2191', color=_color, render_order=RenderOrder.ITEM)

        _profile = {}
        _profile = example_profile()
        _profile['ATK']['ATK'] = 1.2 + _bonus

        _equip = Equippable(slot=Bodyparts.MainHand.name, profile=_profile)

        _profile = {}
        _profile = example_profile()
        _profile['ATK']['ATK'] = 1.6 + _bonus
        _profile['ATK']['SPD'] = 0.2 + _bonus

        _skill = Skill(cooldown=5, name='pierce', nature='direct', profile=_profile)
    
    return _base, _equip, _skill

def create_torso_item(name, material):
    _bonus = material_dict[material][0]
    _color = material_dict[material][1]

    _base, _equip, _skill = None, None, None

    if name == 'chain mail':
        _base = Base(name=name, char=u'\u2591', color=_color, render_order=RenderOrder.ITEM)

        _profile = {}
        _profile = example_profile()
        _profile['DEF']['DEF'] = 1.2 + _bonus
        _profile['MAG']['MAG'] = 1.0 + _bonus

        _equip = Equippable(slot=Bodyparts.Torso.name, profile=_profile)

        _skill = Skill()
    
    if name == 'plate mail':
        _base = Base(name=name, char=u'\u2593', color=_color, render_order=RenderOrder.ITEM)

        _profile = {}
        _profile = example_profile()
        _profile['DEF']['DEF'] = 1.9 + _bonus
        _profile['MAG']['MAG'] = 0.7 + _bonus

        _equip = Equippable(slot=Bodyparts.Torso.name, profile=_profile)

        _skill = Skill()
    
    return _base, _equip, _skill

def create_offhand_item(name, material):
    _bonus = material_dict[material][0]
    _color = material_dict[material][1]
    _base, _equip, _skill = None, None, None

    if name == 'buckler':
        _base = Base(name=name, char=u'\u03A6', color=_color, render_order=RenderOrder.ITEM)
        _equip = Equippable(slot=Bodyparts.OffHand.name)
        _skill = Skill(cooldown=5, name='bash', nature='direct')
        _skill.knockback_force = 2

    if name == 'shield':
        _base = Base(name=name, char=u'\u13A6', color=_color, render_order=RenderOrder.ITEM)
        _equip = Equippable(slot=Bodyparts.OffHand.name)
        _skill = Skill(cooldown=5, name='bash', nature='direct')
        _skill.knockback_force = 4

    return _base, _equip, _skill