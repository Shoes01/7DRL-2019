import tcod as libtcod

from systems.movement import move

def take_turn(entity, entities, game_map, fov_map, player):
    turn_results = []
    player_spotted = fov_map.fov[entity.pos.x, entity.pos.y]

    if player_spotted:
        entity.ai.lost = 0
        
        if entity.ai.awake:
            turn_results.extend(hunt_player(entity, entities, game_map, player))
        else:
            entity.ai.awake = True
            turn_results.append({'message': ('The {0} wakes up!'.format(entity.base.name.capitalize()), libtcod.light_grey)})
    elif entity.ai.awake:
        entity.ai.lost += 1

        if entity.ai.lost > 5:
            entity.ai.awake = False
            turn_results.append({'message': ('The {0} falls asleep.'.format(entity.base.name.capitalize()), libtcod.light_grey)})
    
    return turn_results

def hunt_player(entity, entities, game_map, player):
    turn_results = []
    
    xd, yd = player.pos.x, player.pos.y
    xo, yo = entity.pos.x, entity.pos.y
    
    dx = xd - xo
    dy = yd - yo

    if dx:
        dx = dx // abs(dx)
    if dy:
        dy = dy // abs(dy)
    
    d_move = dx, dy
    
    turn_results.extend(move(d_move, entity, entities, game_map))

    return turn_results
    