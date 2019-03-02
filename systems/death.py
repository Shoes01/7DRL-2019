import tcod as libtcod

from components.base import RenderOrder
from components.job import SpecialJob
from components.race import Race
from systems.loot import drop_loot

def kill(entity, entities):
    turn_results = []

    turn_results.append({'message': ('The {0} has been killed!'.format(entity.base.name.capitalize()), libtcod.red)})
    
    entity.ai = None
    entity.base.char = '%'
    entity.base.color = libtcod.red
    entity.base.name = 'remains of ' + entity.base.name
    entity.base.render_order = RenderOrder.CORPSE

    entity.job = SpecialJob.CARCASS

    turn_results.extend(drop_loot(entity, entities))

    return turn_results