import tcod as libtcod

from game import GameStates, FOV_RADIUS
from systems.ai import take_turn
from systems.equip import equip, unequip
from systems.inventory import close_inventory, drop_item, inventory_choice, open_inventory, pick_up
from systems.message_log import Message
from systems.movement import move
from systems.progression import confirm_stat_gain, level_up_choice
from systems.skill import cancel_skill, execute_skill, skill_choice

def update(action, entities, event_queue, fov_map, game, game_map, game_state_machine, message_log, player):
    turn_results = []
    
    # Game state.
    _game_state = game_state_machine.state.__str__()

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
    if _game_state == 'PlayerTurn':
        # The player may act.
        if _inventory:
            turn_results.extend(open_inventory())
            event_queue.append('open_inventory')

        if _grab:
            turn_results.extend(pick_up(player, entities))
            event_queue.append('player_acted')

        if _move:
            turn_results.extend(move(_move, player, entities, game_map))
            event_queue.append('player_acted')
        
        if _skill_choice:
            _bodypart = _skill_choice
            turn_results.extend(skill_choice(_bodypart, game_map, player))
            event_queue.append('skill_selected')

        if _wait:
            event_queue.append('player_acted')

        # Check to see if the player has leveled up. This is a persistent event.
        if player.stats.exp > player.stats.exp_needed_for_next_level:
            if event_queue.count('leveled_up') == 0:
                event_queue.insert(0, 'leveled_up')
    
    # Handle the enemy turn.
    elif _game_state == 'EnemyTurn':
        # Each entity gets to take a turn.
        for entity in entities:
            if entity.ai:
                turn_results.extend(take_turn(entity, entities, game_map, fov_map, player))
        
        event_queue.append('enemies_acted')
        if player.stats.hp <= 0:
            event_queue.append('player_dead')
    
    elif _game_state == 'OpenInventory':
        if _drop:
            turn_results.extend(drop_item(entities, player))
        
        if _equip:
            turn_results.extend(equip(player))

        if _exit:
            turn_results.extend(close_inventory(player))
            event_queue.append('close_inventory')
            _exit = None

        if _inventory_choice is not None:
            turn_results.extend(inventory_choice(_inventory_choice, player))
        
        if _unequip:
            turn_results.extend(unequip(player))
    
    elif _game_state == 'LeveledUp':
        if _confirm:
            turn_results.extend(confirm_stat_gain(player))
            event_queue.append('chose_stat')

        if _exit:
            # TODO: Maybe this should be moved into the system...
            _message = 'You have to select a stat to increase!'
            _color = libtcod.light_purple
            turn_results.append({'message': (_message, _color)})
            _exit = None
        
        if _level_up_choice is not None:
            turn_results.extend(level_up_choice(_level_up_choice, player))
    
    elif _game_state == 'TargetingState':
        # _previous_state is how to get out of this state.
        # Any button other than a directional should trigger it.
        if _exit:
            turn_results.extend(cancel_skill(player))
            event_queue.append('cancel_targeting')
            _exit = None
        
        if _move:
            _direction = _move
            turn_results.extend(execute_skill(_direction, entities, game_map, player))
            event_queue.append('player_acted') # Order is important, so that the player may have a chance to level up before the enemy turn.
            event_queue.append('chose_direction')

    # Handle things that may occur at any time.
    if _exit:
        event_queue.append('exit')

    handle_turn_results(game, message_log, turn_results)

    if event_queue:
        handle_events(event_queue, game_state_machine)

def handle_events(event_queue, game_state_machine):
    # TODO
    # There may be events in the queue that don't get processed this turn. 
    # Find a way to loop through the events, removing the ones that succeeded.
    temp_event_queue = event_queue.copy()
    for event in temp_event_queue:
        _old_state = game_state_machine.state
        if _old_state != game_state_machine.on_event(event):
            # The state has changed!
            event_queue.remove(event)
    """
    new_state = False
    while not new_state:
        event = event_queue.pop()
        _old_state = game_state_machine.state
        game_state_machine.on_event(event)
        _new_state = game_state_machine.state
        if _old_state is not _new_state:
            new_state = True
        else:
            event_queue.append(event)
    """


def handle_turn_results(game, message_log, results):
    while True:
        if len(results) == 0:
            return False
        
        result = results.pop()
    
        # Possible results.
        _message = result.get('message')
        _redraw_map = result.get('redraw_map')

        if _message:
            _text, _color = _message
            message_log.add_message(Message(_text, _color))

        elif _redraw_map:
            game.redraw_map = True