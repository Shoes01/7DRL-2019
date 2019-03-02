import numpy as np
import random

from systems.soul import generate_soul

class Soul():
    def __init__ (self, eccentricity, rank):
        ' The soul is a 2x3 matrix that holds integers. The values are used to inform the stat values. '  
        self.eccentricity = eccentricity    # The greatest distance between two integers
        self.rank = rank                    # The sum total of the integers

        self.soul = self.generate_soul(self.eccentricity, self.rank)