import random
import tcod as libtcod

from components.ai import BRAIN
from game import COLORS
from map_functions import tile_occupied
from systems.movement import move

def take_turn(entity, entities, game_map, neighborhood, player):
    turn_results = []

    if entity.status.stunned:
        return turn_results

    if entity.ai.brain == BRAIN.ZOMBIE:
        turn_results.extend(handle_zombie_brain(entity, entities, game_map, neighborhood, player))
    elif entity.ai.brain == BRAIN.DEMON:
        turn_results.extend(handle_demon_brain(entity, entities, game_map, neighborhood, player))

    return turn_results

def handle_demon_brain(entity, entities, game_map, neighborhood, player):
    turn_results = []
    x = entity.pos.x
    y = entity.pos.y

    d_value = neighborhood.dijkstra_map[y, x] - 15 # The 15 is the value added when a tile is occupied

    if d_value <= 20 and entity.ai.scary_message_1 is False:
        entity.ai.awake = True
        entity.ai.scary_message_1 = True
        _message = '"YOU HAVE FINALLY ARRIVED" bellows the {0}.'.format(entity.base.name.capitalize())
        _color = COLORS['message_very_bad']
        turn_results.append({'message': (_message, _color)})

    if d_value <= 15 and entity.ai.scary_message_2 is False:
        entity.ai.scary_message_2 = True
        _message = '"BRING ME YOUR SOUL."'
        _color = COLORS['message_very_bad']
        turn_results.append({'message': (_message, _color)})

    if entity.health.points <= int(entity.health.max * 0.3) and entity.ai.low_hp_message_1 is False:
        entity.ai.low_hp_message_1 = True
        _message = '"HOW DARE YOU FORCE ME TO EXERT MYSELF."'
        _color = COLORS['message_very_bad']
        turn_results.append({'message': (_message, _color)})

    if entity.ai.awake:
        turn_results.extend(hunt_player(entity, entities, game_map, player, neighborhood))

    return turn_results

def handle_zombie_brain(entity, entities, game_map, neighborhood, player):
    turn_results = []
    player_spotted = game_map.fov_map.fov[entity.pos.x, entity.pos.y]

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
        if new_value != 999 and new_value <= lowest_value and tile_occupied(entities, direction[0], direction[1]) is None:
            lowest_value = new_value
            best_direction = direction
            
    if best_direction == (0, 0):
        best_direction = random.choice(directions)

    turn_results.extend(move(best_direction, entity, entities, game_map))

    return turn_results
    