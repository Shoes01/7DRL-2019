from map_functions import tile_occupied
from systems.combat import attack

def move(d_move, entity, entities, game_map):
    turn_results = []

    dx, dy = d_move
    xt, yt = entity.pos.x + dx, entity.pos.y + dy

    blocks_path = game_map.tiles['blocks_path'][xt, yt]
    tile_occupant = tile_occupied(entities, xt, yt)

    if not blocks_path and not tile_occupant:
        entity.pos.x += dx
        entity.pos.y += dy
        turn_results.append({'moved': True})
    
    if tile_occupant:
        turn_results.extend(attack(entity, tile_occupant))
    
    return turn_results