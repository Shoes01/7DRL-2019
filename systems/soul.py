import numpy as np
import random

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

def soul_pairing(soul):
    pass