import numpy as np

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

def cancel_skill(player):
    turn_results = []

    for _, item in player.body.parts.items():
        if item and item.skill:
            item.skill.selected = False
    
    turn_results.append({'previous_state': True})

    return turn_results

def execute_skill():
    turn_results = []
    return turn_results