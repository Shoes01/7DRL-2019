from systems.factory import create_item

def drop_loot(entity, entities):
    turn_results = []
    
    x, y = entity.pos.x, entity.pos.y
    
    item = create_item('sword')

    item.pos.x, item.pos.y = x, y

    entities.append(item)

    item = create_item('boots')

    item.pos.x, item.pos.y = x, y

    entities.append(item)

    item = create_item('chainmail')

    item.pos.x, item.pos.y = x, y

    entities.append(item)

    return turn_results