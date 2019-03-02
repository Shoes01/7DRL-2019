from map_functions import tile_occupied
from systems.combat import attack
from systems.status import stun

def move(d_move, entity, entities, game_map):
    turn_results = []

    dx, dy = d_move
    xt, yt = entity.pos.x + dx, entity.pos.y + dy

    blocks_path = game_map.tiles['blocks_path'][xt, yt]
    tile_occupant = tile_occupied(entities, xt, yt)

    if not blocks_path and not tile_occupant:
        entity.pos.x += dx
        entity.pos.y += dy
    
    if tile_occupant:
        turn_results.extend(attack(entity, tile_occupant, entities))
    
    return turn_results

def push(d_move, entity, entities, force, game_map):
    # Force determines how far the entity gets pushed
    # If the entity is pushed into an obstacle, then the entity and that obstacle are stunned for the remainder of "force"
    turn_results = []

    dx, dy = d_move

    while force:
        blocks_path = game_map.tiles['blocks_path'][entity.pos.x + dx, entity.pos.y + dy]
        tile_occupant = tile_occupied(entities, entity.pos.x + dx, entity.pos.y + dy)
        
        if not blocks_path and not tile_occupant:
            entity.pos.x += dx
            entity.pos.y += dy
        
        if blocks_path:
            turn_results.extend(stun(entity, force))
            force = 0

        if tile_occupant:
            turn_results.extend(stun(entity, force))
            turn_results.extend(stun(tile_occupant, force))
            force = 0
        
        force -= 1

    return turn_results