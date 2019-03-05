import tcod as libtcod

def stun(entity, duration):
    entity.status.stunned = duration

    _message = 'The {0} is stunned for {1} turn(s).'.format(entity.base.name.capitalize(), duration)
    _color = libtcod.light_blue
    return [{'message': (_message, _color)}]

def tick(entities):
    turn_results = []

    for entity in entities:
        if entity.status:
            if entity.status.stunned > 0:
                turn_results.extend(handle_stunned(entity))
            if entity.status.healing > 0:
                turn_results.extend(handle_healing(entity))


    return turn_results

def handle_stunned(entity):
    turn_results = []

    entity.status.stunned -= 1

    if entity.status.stunned == 0:
        _message = 'The {0} is no longer stunned!'.format(entity.base.name.capitalize())
        _color = libtcod.light_red
        turn_results.append({'message': (_message, _color)})
    
    return turn_results

def handle_healing(entity):
    turn_results = []

    entity.status.healing -= 1
    entity.health.points += entity.status.healing_power

    if entity.status.healing == 0:
        entity.status.healing_power = 0
        _message = 'The {0} is no longer healing!'.format(entity.base.name.capitalize())
        _color = libtcod.light_red
        turn_results.append({'message': (_message, _color)})
    
    return turn_results