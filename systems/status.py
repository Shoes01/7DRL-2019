import tcod as libtcod

def stun(entity, duration):
    entity.status.stunned = duration
    
    _message = 'The {0} is stunned for {1} turns.'.format(entity.base.name.capitalize(), duration)
    _color = libtcod.light_blue
    return {'message': (_message, _color)}

def tick(entity):
    if entity.status.stunned > 0:
        entity.status.stunned -= 1