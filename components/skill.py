import numpy as np

class Skill():
    def __init__(self, skill):
        self.skill = skill

        self.selected = False

        if self.skill == 'pierce':
            self.targeting_array_E = np.array(
                [   [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]
            )
            self.targeting_array_NE = np.array(
                [   [0, 0, 0, 0, 1],
                    [0, 0, 0, 1, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]
            )