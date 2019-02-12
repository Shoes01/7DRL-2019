import tcod as libtcod

from components.base import RenderOrder

def kill(entity):
    turn_results = []

    turn_results.append({'message': ('The {0} has been killed!'.format(entity.base.name.capitalize()), libtcod.red)})

    if entity.ai == None:
        turn_results.append({'player_dead': True})
    
    entity.ai = None
    entity.base.char = '%'
    entity.base.color = libtcod.red
    entity.base.name = 'remains of ' + entity.base.name
    entity.base.render_order = RenderOrder.CORPSE

    return turn_results