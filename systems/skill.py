import numpy as np

from map_functions import tile_occupied, path_unblocked
from systems.combat import attack
from systems.helper_stats import get_stats

def generate_targeting_array(game_map, player, skill):
    skill.legal_targeting_arrays['E'] = skill.template_E
    skill.legal_targeting_arrays['NE'] = skill.template_NE

    skill.legal_targeting_arrays['N'] = np.rot90(skill.legal_targeting_arrays['E'])
    skill.legal_targeting_arrays['W'] = np.rot90(skill.legal_targeting_arrays['N'])
    skill.legal_targeting_arrays['S'] = np.rot90(skill.legal_targeting_arrays['W'])
    skill.legal_targeting_arrays['NW'] = np.rot90(skill.legal_targeting_arrays['NE'])
    skill.legal_targeting_arrays['SW'] = np.rot90(skill.legal_targeting_arrays['NW'])
    skill.legal_targeting_arrays['SE'] = np.rot90(skill.legal_targeting_arrays['SW'])

    xo = player.pos.x - skill.array_size // 2
    yo = player.pos.y - skill.array_size // 2

    if skill.nature == 'direct':
        for direction, array in skill.legal_targeting_arrays.items():
            for (x, y), value in np.ndenumerate(array):
                _, blocks_path, _ = game_map.tiles[xo + x][yo + y]

                if blocks_path and value:
                    # Zero the array
                    skill.legal_targeting_arrays[direction] = None
                    break

def skill_choice(body_part, game_map, player):
    turn_results = []

    item = player.body.parts[body_part]

    if item and item.skill:
        item.skill.selected = True
        generate_targeting_array(game_map, player, item.skill)
        turn_results.append({'targeting_state': True})

    return turn_results

def get_single_targeting_array(direction, player):
    skill = chosen_skill(player)
    
    if direction is None or skill is None:
        return None
    if direction == (0, 1):
        return skill.legal_targeting_arrays['E']
    if direction == (-1, 1):
        return skill.legal_targeting_arrays['NE']
    if direction == (-1, 0):
        return skill.legal_targeting_arrays['N']
    if direction == (-1, -1):
        return skill.legal_targeting_arrays['NW']
    if direction == (0, -1):
        return skill.legal_targeting_arrays['W']
    if direction == (1, -1):
        return skill.legal_targeting_arrays['SW']
    if direction == (1, 0):
        return skill.legal_targeting_arrays['S']
    if direction == (1, 1):
        return skill.legal_targeting_arrays['SE']

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

    if target_array is not None:
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

    else:
        turn_results.extend(cancel_skill(player))

    return turn_results

def chosen_skill(player):
    for _, item in player.body.parts.items():
        if item and item.skill and item.skill.selected:
            return item.skill
    else:
        return None