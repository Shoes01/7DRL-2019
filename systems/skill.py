import numpy as np

from map_functions import tile_occupied, path_unblocked
from systems.combat import attack
from systems.helper_stats import get_stats

def skill_choice(body_part, player):
    turn_results = []

    item = player.body.parts[body_part]

    if item and item.skill:
        item.skill.selected = True
        turn_results.append({'targeting_state': True})

    return turn_results

def get_targeting_array(player):
    east = np.zeros((5, 5), dtype=int, order='F')

    for _, item in player.body.parts.items():
        if item and item.skill and item.skill.selected:
            east = item.skill.targeting_array_E
            north_east = item.skill.targeting_array_NE

    if not east.any():
        #print('ERROR: The selected item has no skill.')
        return east

    north = np.rot90(east)
    west = np.rot90(north)
    south = np.rot90(west)

    north_west = np.rot90(north_east)
    south_west = np.rot90(north_west)
    south_east = np.rot90(south_west)

    targeting_array = east + north + west + south + north_east + north_west + south_west + south_east

    return targeting_array

def get_single_targeting_array(direction, player):
    east = np.zeros((5, 5), dtype=int, order='F')

    for _, item in player.body.parts.items():
        if item and item.skill and item.skill.selected:
            east = item.skill.targeting_array_E
            north_east = item.skill.targeting_array_NE

    if not east.any():
        #print('ERROR: The selected item has no skill.')
        return east

    north = np.rot90(east)
    west = np.rot90(north)
    south = np.rot90(west)

    north_west = np.rot90(north_east)
    south_west = np.rot90(north_west)
    south_east = np.rot90(south_west)

    if direction == (0, 1):
        return east
    if direction == (-1, 1):
        return north_east
    if direction == (-1, 0):
        return north
    if direction == (-1, -1):
        return north_west
    if direction == (0, -1):
        return west
    if direction == (1, -1):
        return south_west
    if direction == (1, 0):
        return south
    if direction == (1, 1):
        return south_east

def cancel_skill(player):
    turn_results = []

    for _, item in player.body.parts.items():
        if item and item.skill:
            item.skill.selected = False
    
    turn_results.append({'previous_state': True})

    return turn_results

def execute_skill(direction, entities, game_map, player):
    turn_results = []    

    target_array = get_single_targeting_array(direction, player)

    if target_array.any():
        center, _ = target_array.shape
        center = center // 2
        xo, yo = player.pos.x - center, player.pos.y - center

        for (x, y), value in np.ndenumerate(target_array):
            if value:
                entity = tile_occupied(entities, xo + x, yo + y)
                
                skill = chosen_skill(player)

                if skill.nature == 'direct':
                    _path_unblocked = path_unblocked(game_map, player.pos.x, player.pos.y, xo + x, yo + y)
                

                if entity and entity is not player and _path_unblocked:
                    turn_results.extend(attack(player, entity, entities))

    turn_results.extend(cancel_skill(player))

    return turn_results

def chosen_skill(player):
    for _, item in player.body.parts.items():
        if item and item.skill and item.skill.selected:
            return item.skill
    else:
        return None