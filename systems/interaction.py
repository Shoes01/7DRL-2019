from components.base import RenderOrder
from game import FOV_RADIUS
from systems.equip import equip_

def interact(entities, event_queue, game_map, neighborhood, player):
    # Look on the ground for an item.
    # Equip it.
    # Or look for stairs.
    # Descence them.

    turn_results = []

    x, y = player.pos.x, player.pos.y

    for item in entities:
        if item.pos.x == x and item.pos.y == y:
            if item.base.render_order == RenderOrder.ITEM:
                if equip_(item, player, entities=entities):
                    event_queue.append('player_acted')
                    # yay
                else:
                    #compare now.
                    event_queue.append('compare_items')
                break
            elif item.base.render_order == RenderOrder.SOUL:
                event_queue.append('consume_soul')
                break
            elif item.base.render_order == RenderOrder.STAIRS:
                game_map.generate_new_map(entities, player)
                neighborhood.populate_directory(game_map)
                neighborhood.update_dijkstra_map(entities, (player.pos.x, player.pos.y))
                break

    else:
        event_queue.append('open_character_sheet')

    return turn_results