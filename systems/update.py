import tcod as libtcod

from game import FOV_RADIUS
from systems.ai import take_turn
from systems.equip import equip, swap_items, unequip
from systems.interaction import interact
from systems.inventory import close_inventory, drop_item, inventory_choice, open_inventory, pick_up
from systems.message_log import Message
from systems.movement import move
from systems.progression import confirm_stat_gain, level_up_choice
from systems.skill import cancel_skill, reduce_cooldown_timer, execute_skill, skill_choice
from systems.soul import merge_soul, flip_soul
from systems.status import tick

def update(action, entities, event_queue, game, game_map, game_state_machine, message_log, neighborhood, player):
    turn_results = []
    
    # Game state.
    _game_state = game_state_machine.state.__str__()

    # Possible actions.
    _confirm = action.get('confirm')
    _debug_toggle = action.get('debug_toggle')
    _drop = action.get('drop')
    _equip = action.get('equip')
    _exit = action.get('exit')
    _grab = action.get('grab')
    _interact = action.get('interact')
    _inventory = action.get('inventory')
    _inventory_choice = action.get('inventory_choice')
    _level_up_choice = action.get('level_up_choice')
    _move = action.get('move')
    _skill_choice = action.get('skill_choice')
    _unequip = action.get('unequip')
    _wait = action.get('wait')

    # Should the following be in a better place?
    if _debug_toggle:
        game.debug_mode = not game.debug_mode
        game.redraw_map = True
        player.health.points = player.health.max

    if _game_state == 'OpeningScreen':
        if _interact or _move or _wait or _skill_choice or _confirm:
            event_queue.append('begin')

    # Handle the player turn.
    if _game_state == 'PlayerTurn':
        # The player may act.
        if _interact:
            turn_results.extend(interact(entities, event_queue, game_map, neighborhood, player))

        if _move:
            turn_results.extend(move(_move, player, entities, game_map))
            event_queue.append('player_acted')
        
        if _skill_choice:
            _bodypart = _skill_choice
            turn_results.extend(skill_choice(_bodypart, event_queue, game_map, player, _game_state))

        if _wait:
            event_queue.append('player_acted')
    
    # Handle the comparison of items.
    elif _game_state == 'CompareItems':
        if _confirm is True:
            turn_results.extend(swap_items(entities, player))
            event_queue.append('done_comparing')

        elif _confirm is False or _exit:
            _exit = None
            event_queue.append('done_comparing')

    elif _game_state == 'ConsumeSoul':
        if _move:
            d_move = _move
            turn_results.extend(flip_soul(d_move, entities, player))
        
        if _confirm is True:
            turn_results.extend(merge_soul(entities, player))
            event_queue.append('done_consuming')
        
        if _confirm is False or _exit:
            # Do not merge souls.
            _exit = None
            event_queue.append('done_consuming')

    elif _game_state == 'CharacterSheet':
        if _interact:
            event_queue.append('close_character_sheet')

    # Handle the enemy turn.
    elif _game_state == 'EnemyTurn':
        # Each entity gets to take a turn.
        for entity in entities:
            if entity.ai:
                turn_results.extend(take_turn(entity, entities, game_map, neighborhood, player))
        
        event_queue.append('enemies_acted')
        if player.health.points <= 0:
            event_queue.append('player_dead')
        reduce_cooldown_timer(player)
        game.redraw_map = True
    
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
        if _exit:
            turn_results.extend(cancel_skill(player))
            event_queue.append('cancel_targeting')
            _exit = None

        if _skill_choice:
            _bodypart = _skill_choice
            turn_results.extend(skill_choice(_bodypart, event_queue, game_map, player, _game_state))
        
        if _move:
            _direction = _move
            turn_results.extend(execute_skill(_direction, entities, event_queue, game_map, player))

        if _wait:
            _direction = _wait
            turn_results.extend(execute_skill(_direction, entities, event_queue, game_map, player))

    # Handle things that may occur at any time.
    if _exit:
        event_queue.append('exit')

    if 'player_acted' in event_queue and game_state_machine.state.__str__() == 'PlayerTurn':
        # The player has acted, their turn is done. It is the enemy's turn!
        neighborhood.update_dijkstra_map(entities, (player.pos.x, player.pos.y))
    if 'enemies_acted' in event_queue and game_state_machine.state.__str__() == 'EnemyTurn':
        # The enemies have acted, their turn is done. It will be the player's turn!
        turn_results.extend(tick(entities))

    handle_turn_results(event_queue, game, message_log, turn_results)

    if event_queue:
        handle_events(event_queue, game, game_state_machine, player)

def handle_events(event_queue, game, game_state_machine, player):
    temp_event_queue = event_queue.copy()
    for event in temp_event_queue:
        _old_state = game_state_machine.state
        if _old_state != game_state_machine.on_event(event):
            # The state has changed!
            game.redraw_map = True
            event_queue.remove(event)

def handle_turn_results(event_queue, game, message_log, results):
    while True:
        if len(results) == 0:
            return False
        
        result = results.pop()
    
        # Possible results.
        _message = result.get('message')
        _redraw_map = result.get('redraw_map')
        _victory = result.get('victory')

        if _message:
            _text, _color = _message
            message_log.add_message(Message(_text, _color))

        elif _redraw_map:
            game.redraw_map = True
        
        elif _victory:
            event_queue.append('victory')