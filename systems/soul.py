import numpy as np
import random
import tcod as libtcod

def generate_soul(eccentricity, rank):
    attempts = 0
    soul_attempt = np.zeros((2, 3), dtype=int, order='F')

    while attempts < 100:
        with np.nditer(soul_attempt, op_flags=['readwrite']) as it:
            for x in it:
                x[...] = random.randint(-eccentricity, eccentricity)
        
        if soul_attempt.sum() == rank:
            return soul_attempt

        attempts += 1
    
    return np.zeros((2, 3), dtype=int, order='F')

def rotate_soul(entities, player):
    turn_results = []

    _message = 'Soul is rotated! (not rly).'
    _color = libtcod.blue
    turn_results.append({'message': (_message, _color)})

    return turn_results

def merge_soul(entities, player):
    turn_results = []

    _message = 'Soul is merged! (not rly).'
    _color = libtcod.blue
    turn_results.append({'message': (_message, _color)})

    return turn_results