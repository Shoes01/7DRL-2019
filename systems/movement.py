from map_functions import tile_occupied

def move(d_move, entity, entities, game_map):
    dx, dy = d_move
    xt, yt = entity.pos.x + dx, entity.pos.y + dy

    blocks_path = game_map.tiles['blocks_path'][xt, yt]
    _tile_occupied = tile_occupied(entities, xt, yt)

    if not blocks_path and not _tile_occupied:
        entity.pos.x += dx
        entity.pos.y += dy