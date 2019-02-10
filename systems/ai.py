import tcod as libtcod

from systems.movement import move

def take_turn(entity, entities, game_map, fov_map, player):
    player_spotted = libtcod.map_is_in_fov(fov_map, player.pos.x, player.pos.y)

    if player_spotted:
        if entity.ai.awake:
            hunt_player(entity, entities, game_map, player)
        else:
            entity.ai.awake = True
    elif entity.ai.awake:
        entity.ai.lost += 1

        if entity.ai.lost > 5:
            entity.ai.awake = False

def hunt_player(entity, entities, game_map, player):
    xd, yd = player.pos.x, player.pos.y
    xo, yo = entity.pos.x, entity.pos.y
    
    dx = xd - xo
    dy = yd - yo

    if dx:
        dx = dx // abs(dx)
    if dy:
        dy = dy // abs(dy)
    
    d_move = dx, dy
    
    move(d_move, entity, entities, game_map)
    