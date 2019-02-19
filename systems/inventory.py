import tcod as libtcod

from components.base import RenderOrder
from game import GameStates

def pick_up(player, entities):
    ' Pick up the item found under the player. '
    turn_results = []

    x, y = player.pos.x, player.pos.y

    for entity in entities:
        if entity.pos.x == x and entity.pos.y == y and entity.base.render_order == RenderOrder.ITEM:
            player.inv.contents.append(entity)
            entities.remove(entity)
            turn_results.append({'message': ('The {0} picks up the {1}.'.format(player.base.name.capitalize(), entity.base.name.capitalize()), libtcod.light_blue)})
            break
    else:
        turn_results.append({'message': ('There is nothing here to pickup.', libtcod.light_grey)})

    return turn_results

def open_inventory(game):
    turn_results = []

    game.state = GameStates.OPEN_INVENTORY
    message = 'You open your inventory.'
    color = libtcod.white
    turn_results.append({'message': (message, color)})
    
    return turn_results

def close_inventory(player):
    turn_results = []

    if player.inv.selected:
        player.inv.selected = None
    message = 'You close your inventory.'
    color = libtcod.white
    turn_results.append({'message': (message, color)})
    turn_results.append({'previous_state': True})
    turn_results.append({'redraw_map': True})

    return turn_results

def inventory_choice(index, player):
    turn_results = []

    iter = 0
    for content in player.inv.contents:
        if index == iter:
            if player.inv.selected == None:
                # You select an item.
                player.inv.selected = content
                message = 'You select the {0}.'.format(content.base.name.capitalize())
                color = libtcod.cyan
                turn_results.append({'message': (message, color)})
            elif player.inv.selected == content:
                # You deselect the item you already chose.
                player.inv.selected = None
                message = 'You deselect the {0}.'.format(content.base.name.capitalize())
                color = libtcod.cyan
                turn_results.append({'message': (message, color)})
            elif player.inv.selected:
                # You select a different item, deslecting the one you already chose.
                player.inv.selected = content
                message = 'You select the {0}.'.format(content.base.name.capitalize())
                color = libtcod.cyan
                turn_results.append({'message': (message, color)})
            break
        iter += 1

    return turn_results

def drop_item(entities, player):
    turn_results = []
    
    item = player.inv.selected

    if item:
        item.pos.x, item.pos.y = player.pos.x, player.pos.y
        entities.append(item)
        player.inv.contents.remove(item)
        message = 'You drop the {0}'.format(item.base.name.capitalize())
        color = libtcod.light_blue
        turn_results.append({'message': (message, color)})
        player.inv.selected = None
    
    return turn_results

def equip_item(player):
    turn_results = []

    item = player.inv.selected

    if item and item.base.slot:
        if player.base.body[item.base.slot] == None:
            player.base.body[item.base.slot] = item
            _message = 'You equip your {0} to your {1}.'.format(item.base.name, item.base.slot)
            _color = libtcod.blue
            turn_results.append({'message': (_message, _color)})
        else:
            _message = 'You must unequip your {0} before equipping your {1}.'.format(player.base.body[item.base.slot].base.name, item.base.name)
            _color = libtcod.red
            turn_results.append({'message': (_message, _color)})
    else:
        _message = 'You do not know how to equip a {0}.'.format(item.base.name)
        _color = libtcod.red
        turn_results.append({'message': (_message, _color)})


    return turn_results

def unequip_item(player):
    turn_results = []

    item = player.inv.selected

    if item and item.base.slot:
        if player.base.body[item.base.slot] == item:
            player.base.body[item.base.slot] = None
            _message = 'You unequip your {0}.'.format(item.base.name)
            _color = libtcod.blue
            turn_results.append({'message': (_message, _color)})
        else:
            _message = 'You are not wielding the {0}.'.format(item.base.name)
            _color = libtcod.grey
            turn_results.append({'message': (_message, _color)})

    return turn_results