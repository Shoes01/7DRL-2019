from game import GameStates, FOV_RADIUS
from systems.ai import take_turn
from systems.message_log import Message
from systems.movement import move

def update(action, entities, fov_map, game, game_map, message_log, player):
    turn_results = []
    
    # Possible actions.
    _exit = action.get('exit')
    _move = action.get('move')
    _wait = action.get('wait')

    # Handle the player turn.
    if game.state == GameStates.PLAYER_TURN:
        # The player may act.
        if _move:
            turn_results.extend(move(_move, player, entities, game_map))
            turn_results.append({'acted': True})
        
        if _wait:
            turn_results.append({'acted': True})
    
    # Handle the enemy turn.
    elif game.state == GameStates.ENEMY_TURN:
        # Each entity gets to take a turn.
        for entity in entities:
            if entity.ai:
                turn_results.extend(take_turn(entity, entities, game_map, fov_map, player))
        
        turn_results.append({'end_enemy_turn': True})
    
    handle_turn_results(game, message_log, turn_results)

    # Handle things that may occur at any time.
    if _exit:
        game.state = GameStates.EXIT

def handle_turn_results(game, message_log, results):
    for result in results:
        # Possible results.
        _acted = result.get('acted')
        _end_enemy_turn = result.get('end_enemy_turn')
        _message = result.get('message')
        _player_dead = result.get('player_dead')

        if _acted:
            game.state = GameStates.ENEMY_TURN

        elif _end_enemy_turn:
            game.state = GameStates.PLAYER_TURN

        elif _message:
            _text, _color = _message
            message_log.add_message(Message(_text, _color))

        elif _player_dead:
            game.state = GameStates.PLAYER_DEAD
            break