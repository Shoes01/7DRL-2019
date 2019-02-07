def move(entity, d_move):
    dx, dy = d_move

    entity.pos.x += dx
    entity.pos.y += dy