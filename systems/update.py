from game import GameStates, FOV_RADIUS
from systems.movement import move

def update(action, entities, game, player):
    # Possible actions.
    _move = action.get('move')
    _exit = action.get('exit')

    if _move:
        move(player, _move)
    
    if _exit:
        game.state = GameStates.EXIT