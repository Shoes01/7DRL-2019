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

def inventory_choice(char, player):
    turn_results = []

    iter = 0
    for content in player.inv.contents:
        order = ord(char) - 97
        if order == iter:
            if player.inv.selected == None:
                # You select an item.
                player.inv.selected = content
                player.inv.selected.base.highlighted = True
                message = 'You select the {0}.'.format(content.base.name.capitalize())
                color = libtcod.cyan
                turn_results.append({'message': (message, color)})
            if player.inv.selected == content:
                # You deselect the item you already chose.
                player.inv.selected.base.highlighted = False
                player.inv.selected = None
                message = 'You deselect the {0}.'.format(content.base.name.capitalize())
                color = libtcod.cyan
                turn_results.append({'message': (message, color)})
            elif player.inv.selected:
                # You select a different item, deslecting the one you already chose.
                player.inv.selected.base.highlighted = False
                player.inv.selected = content
                player.inv.selected.base.highlighted = True
                message = 'You select the {0}.'.format(content.base.name.capitalize())
                color = libtcod.cyan
                turn_results.append({'message': (message, color)})
            break
        iter += 1

    return turn_results
