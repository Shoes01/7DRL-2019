import tcod as libtcod

from game import GameStates

def pick_up(player, entities):
    ' Pick up the item found under the player. '
    turn_results = []

    x, y = player.pos.x, player.pos.y

    for entity in entities:
        if entity.pos.x == x and entity.pos.y == y and entity.base.name is not 'player' and entity.ai is None:
            player.inv.contents.append(entity)
            entities.remove(entity)
            turn_results.append({'message': ('The {0} picks up the {1}.'.format(player.base.name.capitalize(), entity.base.name.capitalize()), libtcod.light_blue)})
            break
    else:
        turn_results.append({'message': ('There is nothing here to pickup.', libtcod.light_grey)})

    return turn_results

def open_inventory(game):
    turn_results = []

    if game.state is not GameStates.OPEN_INVENTORY:
        game.state = GameStates.OPEN_INVENTORY
        message = 'You open your inventory.'
        color = libtcod.white
        turn_results.append({'message': (message, color)})
    else:
        game.state = GameStates.PLAYER_TURN
        message = 'You close your inventory.'
        color = libtcod.white
        turn_results.append({'message': (message, color)})
    
    return turn_results