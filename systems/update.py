import tcod as libtcod

from game import GameStates, FOV_RADIUS
from systems.ai import take_turn
from systems.equip import equip, unequip
from systems.inventory import close_inventory, drop_item, inventory_choice, open_inventory, pick_up
from systems.message_log import Message
from systems.movement import move
from systems.progression import confirm_stat_gain, level_up_choice
from systems.skill import cancel_skill, execute_skill, skill_choice

def update(action, entities, fov_map, game, game_map, message_log, player):
    turn_results = []
    
    # Possible actions.
    _confirm = action.get('confirm')
    _drop = action.get('drop')
    _equip = action.get('equip')
    _exit = action.get('exit')
    _grab = action.get('grab')
    _inventory = action.get('inventory')
    _inventory_choice = action.get('inventory_choice')
    _level_up_choice = action.get('level_up_choice')
    _move = action.get('move')
    _skill_choice = action.get('skill_choice')
    _unequip = action.get('unequip')
    _wait = action.get('wait')

    # Handle the player turn.
    if game.state == GameStates.PLAYER_TURN:
        # The player may act.
        if _inventory:
            turn_results.extend(open_inventory(game))

        if _grab:
            turn_results.extend(pick_up(player, entities))
            turn_results.append({'acted': True})

        if _move:
            turn_results.extend(move(_move, player, entities, game_map))
            turn_results.append({'acted': True})
        
        if _skill_choice:
            _bodypart = _skill_choice
            turn_results.extend(skill_choice(_bodypart, game_map, player))

        if _wait:
            turn_results.append({'acted': True})
    
    # Handle the enemy turn.
    elif game.state == GameStates.ENEMY_TURN:
        # Each entity gets to take a turn.
        for entity in entities:
            if entity.ai:
                turn_results.extend(take_turn(entity, entities, game_map, fov_map, player))
        
        turn_results.append({'end_enemy_turn': True})
    
    elif game.state == GameStates.OPEN_INVENTORY:
        if _drop:
            turn_results.extend(drop_item(entities, player))
        
        if _equip:
            turn_results.extend(equip(player))

        if _exit:
            turn_results.extend(close_inventory(player))
            _exit = None

        if _inventory_choice is not None:
            turn_results.extend(inventory_choice(_inventory_choice, player))
        
        if _unequip:
            turn_results.extend(unequip(player))
    
    elif game.state == GameStates.LEVEL_UP:
        if _confirm:
            turn_results.extend(confirm_stat_gain(player))
        if _exit:
            # TODO: Maybe this should be moved into the system...
            _message = 'You have to select a stat to increase!'
            _color = libtcod.light_purple
            turn_results.append({'message': (_message, _color)})
            _exit = None
        
        if _level_up_choice is not None:
            turn_results.extend(level_up_choice(_level_up_choice, player))
    
    elif game.state == GameStates.TARGETING_STATE:
        # _previous_state is how to get out of this state.
        # Any button other than a directional should trigger it.
        if _exit:
            turn_results.extend(cancel_skill(player))
            _exit = None
        
        if _move:
            _direction = _move
            turn_results.extend(execute_skill(_direction, entities, game_map, player))
            turn_results.append({'acted': True})

    handle_turn_results(game, message_log, turn_results)

    # Handle things that may occur at any time.
    if _exit:
        game.state = GameStates.EXIT

def handle_turn_results(game, message_log, results):
    while True:
        if len(results) == 0:
            return False
        
        result = results.pop()
    
        # Possible results.
        _acted = result.get('acted')
        _damage = result.get('damage')
        _end_enemy_turn = result.get('end_enemy_turn')
        _level_up = result.get('level_up')
        _message = result.get('message')
        _player_dead = result.get('player_dead')
        _previous_state = result.get('previous_state')
        _targeting_state = result.get('targeting_state')
        _redraw_map = result.get('redraw_map')

        if _acted and game.state == GameStates.PLAYER_TURN:
            game.previous_state = game.state
            game.state = GameStates.ENEMY_TURN

        elif _end_enemy_turn:
            game.previous_state = game.state
            game.state = GameStates.PLAYER_TURN
 
        elif _level_up:
            game.previous_state = game.state
            game.state = GameStates.LEVEL_UP

        elif _message:
            _text, _color = _message
            message_log.add_message(Message(_text, _color))

        elif _player_dead:
            game.previous_state = game.state
            game.state = GameStates.PLAYER_DEAD
            break

        elif _previous_state:
            game.state = game.previous_state
        
        elif _targeting_state:
            game.previous_state = game.state
            game.state = GameStates.TARGETING_STATE

        elif _redraw_map:
            game.redraw_map = True