import numpy as np
import random

class Soul():
    def __init__ (self, eccentricity, rank):
        ' The soul is a 2x3 matrix that holds integers. The values are used to inform the stat values. '  
        self.eccentricity = eccentricity    # The greatest distance between two integers
        self.rank = rank                    # The sum total of the integers
    
        self.soul = np.zeros((2, 3), dtype=int, order='F')

        self.generate_soul()
    
    def generate_soul(self):
        attempts = 0
        soul_attempt = np.zeros((2, 3), dtype=int, order='F')

        while True:
            with np.nditer(soul_attempt, op_flags=['readwrite']) as it:
                for x in it:
                    x[...] = random.randint(-self.eccentricity, self.eccentricity)
            
            if soul_attempt.sum() == self.rank:
                self.soul = soul_attempt
                return False
                
            elif attempts == 100:
                return False
            
            attempts += 1