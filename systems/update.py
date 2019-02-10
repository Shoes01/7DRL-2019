from game import GameStates, FOV_RADIUS
from systems.ai import take_turn
from systems.movement import move

def update(action, entities, fov_map, game, game_map, player):
    # Possible actions.
    _move = action.get('move')
    _exit = action.get('exit')

    if game.state == GameStates.PLAYER_TURN:
        if _move:
            move(_move, player, entities, game_map)
            game.state = GameStates.ENEMY_TURN
    
    elif game.state == GameStates.ENEMY_TURN:
        for entity in entities:
            if entity.ai:
                take_turn(entity, entities, game_map, fov_map, player)
        
        game.state = GameStates.PLAYER_TURN
        
    if _exit:
        game.state = GameStates.EXIT