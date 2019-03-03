import random

from systems.factory import create_item

def drop_loot(entity, entities):
    turn_results = []
    
    directions = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

    x, y = entity.pos.x, entity.pos.y

    item = create_item('sword')
    direction = random.choice(directions)
    directions.remove(direction)    
    item.pos.x, item.pos.y = x + direction[0], y + direction[0]
    entities.append(item)

    item = create_item('boots')
    direction = random.choice(directions)
    directions.remove(direction)    
    item.pos.x, item.pos.y = x + direction[0], y + direction[0]
    entities.append(item)

    item = create_item('chainmail')
    direction = random.choice(directions)
    directions.remove(direction)    
    item.pos.x, item.pos.y = x + direction[0], y + direction[0]
    entities.append(item)

    item = create_item('shield')
    direction = random.choice(directions)
    directions.remove(direction)    
    item.pos.x, item.pos.y = x + direction[0], y + direction[0]
    entities.append(item)

    return turn_results