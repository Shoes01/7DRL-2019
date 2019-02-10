from game import GameStates, FOV_RADIUS
from systems.ai import take_turn
from systems.movement import move

def update(action, entities, fov_map, game, game_map, player):
    # Possible actions.
    _exit = action.get('exit')
    _move = action.get('move')
    _wait = action.get('wait')

    turn_results = []

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
    
    handle_turn_results(game, turn_results)

    # Handle things that may occur at any time.
    if _exit or game.state == GameStates.PLAYER_DEAD:
        game.state = GameStates.EXIT

def handle_turn_results(game, results):
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
            pass

        elif _player_dead:
            game.state = GameStates.PLAYER_DEAD