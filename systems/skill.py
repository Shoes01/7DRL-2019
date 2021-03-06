import numpy as np
import tcod as libtcod

from map_functions import tile_occupied, path_unblocked
from systems.combat import attack
from systems.movement import move, push

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
                if 0 < xo + x < game_map.width and 0 < yo + y < game_map.height:
                    _, blocks_path, _ = game_map.tiles[xo + x][yo + y]

                    if blocks_path and value:
                        # Zero the array
                        skill.legal_targeting_arrays[direction] = None
                        break
                elif value:
                    # Zero the array
                    skill.legal_targeting_arrays[direction] = None
                    break

def skill_choice(body_part, event_queue, game_map, player, _game_state):
    turn_results = []

    item = player.body.parts[body_part]
    other_item = None

    for _, value in player.body.parts.items():
        if value and value.skill and value.skill.selected:
            other_item = value

    if _game_state == 'TargetingState' and other_item == item:
        # We clicked the skill again. Cancel targeting.
        other_item.skill.selected = False
        event_queue.append('cancel_targeting')
        return turn_results
    
    elif _game_state == 'TargetingState' and other_item != item:
        other_item.skill.selected = False
        
    if item and item.skill and item.skill.cooldown_timer == 0:
        item.skill.selected = True
        generate_targeting_array(game_map, player, item.skill)
        if _game_state == 'PlayerTurn':
            event_queue.append('skill_selected')

    elif item and item.skill and item.skill.cooldown_timer > 0:
        _message = 'This skill is still on cooldown.'
        _color = libtcod.red
        turn_results.append({'message': (_message, _color)})

    else:
        _message = 'There is no item equipped in this slot.'
        _color = libtcod.red
        turn_results.append({'message': (_message, _color)})

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
    if direction is True:
        return skill.legal_targeting_arrays['E']

def cancel_skill(player):
    turn_results = []

    for _, item in player.body.parts.items():
        if item and item.skill:
            item.skill.selected = False
            item.skill.direction = None

    return turn_results

def execute_skill(direction, entities, event_queue, game_map, player):
    turn_results = []    

    target_array = get_single_targeting_array(direction, player)

    _confirmed = False
    skill = chosen_skill(player)
    if skill.direction == direction:
        _confirmed = True
    else:
        skill.direction = direction
        return turn_results

    if skill is not None and target_array is not None:
        center, _ = target_array.shape
        center = center // 2
        xo, yo = player.pos.x - center, player.pos.y - center
        event_queue.append('player_acted') # Order is important, so that the player may have a chance to level up before the enemy turn.
        skill.cooldown_timer = skill.cooldown

        if direction is True:
            # We are targeting ourselves.
            for (x, y), value in np.ndenumerate(target_array):
                if value and value % 19 == 0:
                    if value % 37 == 0:
                        # This grants a healing buff
                        player.status.healing = skill.duration
                        player.status.healing_power = skill.power

        for (x, y), value in np.ndenumerate(target_array):
            entity = tile_occupied(entities, xo + x, yo + y)
          
            if value and value % 23 == 0:
                # This is a special value that represents where the player will land.
                player.pos.x += x - center
                player.pos.y += y - center
            
            if value and value % 29 == 0 and entity:
                # This represents a knockback value
                dx = (xo + x) - player.pos.x
                dy = (yo + y) - player.pos.y
                
                if dx:
                    dx = dx // abs(dx)
                if dy:
                    dy = dy // abs(dy)

                d_move = (dx, dy)
                force = skill.knockback_force

                turn_results.extend(push(d_move, entity, entities, force, game_map))

            if value and value % 31 == 0 and entity:
                # This grants a healing buff
                entity.status.healing = skill.duration
                entity.status.healing_power = skill.power

            if value and value % 37 == 0:
                # This damages units.
                if skill.nature == 'direct':
                    _path_unblocked = path_unblocked(game_map, player.pos.x, player.pos.y, xo + x, yo + y)

                if entity and entity is not player and _path_unblocked:
                    _attack = player
                    _defender = entity
                    turn_results.extend(attack(_attack, _defender, entities, game_map))
            
    else:
        _message = "You can't use that here!"
        _color = libtcod.red
        turn_results.append({'message': (_message, _color)})
        turn_results.append({'skill_failed': True})

    event_queue.append('chose_direction')
    turn_results.extend(cancel_skill(player))

    return turn_results

def chosen_skill(player):
    for _, item in player.body.parts.items():
        if item and item.skill and item.skill.selected:
            return item.skill
    else:
        return None

def reduce_cooldown_timer(player):
    for _, item in player.body.parts.items():
        if item and item.skill and item.skill.cooldown_timer > 0:
            item.skill.cooldown_timer -= 1