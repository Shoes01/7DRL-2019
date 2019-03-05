import numpy as np
import random
import tcod as libtcod

from components.base import RenderOrder

def generate_soul(eccentricity, rank):
    attempts = 0
    soul_attempt = np.zeros((2, 3), dtype=int, order='F')

    if eccentricity * 6 < rank:
        print('WARNING: This could is impossible to make.')
        eccentricity += 2

    while attempts < 400:
        with np.nditer(soul_attempt, op_flags=['readwrite']) as it:
            for x in it:
                x[...] = random.randint(-eccentricity, eccentricity)
        
        if soul_attempt.sum() == rank:
            return soul_attempt

        attempts += 1
        if attempts > 300:
            rank = 3 * rank // 4
    
    print('Soul failed. Rank: {0}. Eccentricity: {1}'.format(rank, eccentricity))
    return np.zeros((2, 3), dtype=int, order='F')

def flip_soul(d_move, entities, player):
    turn_results = []
    
    soul_entity = find_soul(entities, player)
    x, y = d_move

    if x:
        soul_entity.soul.soul = np.fliplr(soul_entity.soul.soul)
    if y:
        soul_entity.soul.soul = np.flipud(soul_entity.soul.soul)

    return turn_results

def merge_soul(entities, player):
    turn_results = []

    soul = find_soul(entities, player)

    player.soul.soul += soul.soul.soul # lol

    entities.remove(soul)

    _message = 'Soul is merged!'
    _color = libtcod.blue
    turn_results.append({'message': (_message, _color)})

    return turn_results

def find_soul(entities, player):
    for entity in entities:
        if entity.base.render_order == RenderOrder.SOUL and entity.pos.x == player.pos.x and entity.pos.y == player.pos.y:
            return entity
    return None