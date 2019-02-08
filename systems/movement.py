def move(entity, d_move, game_map):
    dx, dy = d_move
    xt, yt = entity.pos.x + dx, entity.pos.y + dy

    blocks_path = game_map.tiles['blocks_path'][xt, yt]

    if not blocks_path:
        entity.pos.x += dx
        entity.pos.y += dy