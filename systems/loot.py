import random

from map_functions import tile_empty

def drop_loot(entity, entities, game_map):
    turn_results = []
    
    directions = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

    random.shuffle(directions)

    x, y = entity.pos.x, entity.pos.y

    loot = None
    while directions:
        direction = directions.pop()
        
        if tile_empty(entities, game_map, x + direction[0], y + direction[1]):
            ### Generate loot
            # Get a list of body parts
            # Shuffle this like
            # Loop through it until you find an item
            item_list = []
            for _, item in entity.body.parts.items():
                if item:
                    item_list.append(item)

            random.shuffle(item_list)

            if item_list:
                loot = item_list.pop()
                loot.pos.x, loot.pos.y = x + direction[0], y + direction[1]
                entities.append(loot)
                break

    return turn_results