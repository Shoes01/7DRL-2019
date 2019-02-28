import tcod as libtcod

from map_functions import tile_occupied
from systems.movement import move

def take_turn(entity, entities, game_map, fov_map, neighborhood, player):
    turn_results = []
    player_spotted = fov_map.fov[entity.pos.x, entity.pos.y]

    if entity.ai.awake:
        turn_results.extend(hunt_player(entity, entities, game_map, player, neighborhood))

        if not player_spotted:
            entity.ai.lost += 1
            if entity.ai.lost > 5:
                entity.ai.awake = False
                turn_results.append({'message': ('The {0} falls asleep.'.format(entity.base.name.capitalize()), libtcod.light_grey)})

    if player_spotted:
        entity.ai.lost = 0
        
        if not entity.ai.awake:
            entity.ai.awake = True
            turn_results.append({'message': ('The {0} wakes up!'.format(entity.base.name.capitalize()), libtcod.light_grey)})
    
    return turn_results

def hunt_player(entity, entities, game_map, player, neighborhood):
    turn_results = []
    
    x, y = entity.pos.x, entity.pos.y

    directions = [(-1, 1), (1, -1), (1, 1), (-1, -1), (0, -1), (0, 1), (-1, 0), (1, 0)]

    lowest_value = neighborhood.dijkstra_map[y, x]
    best_direction = (0, 0)
    for direction in directions:
        new_value = neighborhood.dijkstra_map[y + direction[1], x + direction[0]]
        if new_value <= lowest_value and tile_occupied(entities, direction[0], direction[1]) is None:
            lowest_value = new_value
            best_direction = direction

    turn_results.extend(move(best_direction, entity, entities, game_map))

    return turn_results
    