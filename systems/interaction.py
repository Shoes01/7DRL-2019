import tcod as libtcod

from components.base import RenderOrder
from systems.equip import equip_

def interact(entities, event_queue, player):
    # Look on the ground for an item.
    # Equip it.

    turn_results = []

    x, y = player.pos.x, player.pos.y

    for item in entities:
        if item.pos.x == x and item.pos.y == y and item.base.render_order == RenderOrder.ITEM:
            if equip_(entities, item, player):
                event_queue.append('player_acted')
                # yay
            else:
                #compare now.
                event_queue.append('compare_items')
            break
    else:
        turn_results.append({'message': ('There is nothing here.', libtcod.light_grey)})

    return turn_results