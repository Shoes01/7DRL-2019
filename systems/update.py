from game import GameStates, FOV_RADIUS
from systems.movement import move

def update(action, entities, game, game_map, player):
    # Possible actions.
    _move = action.get('move')
    _exit = action.get('exit')

    if _move:
        move(player, _move, game_map)
    
    if _exit:
        game.state = GameStates.EXIT