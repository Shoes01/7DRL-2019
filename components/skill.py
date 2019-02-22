import numpy as np

class Skill():
    def __init__(self, nature, skill):
        self.skill = skill
        self.nature = nature

        self.selected = False

        self.targeting_arrays = {}
        self.array_size = 0

        if self.skill == 'pierce':
            self.targeting_arrays['E'] = np.array(
                [   [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 9, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]]
            )
            self.targeting_arrays['NE'] = np.array(
                [   [0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 9, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]]
            )
            self.array_size, _ = self.targeting_arrays['E'].shape
            self.generate_other_arrays()
    
    def generate_other_arrays(self):
        self.targeting_arrays['N'] = np.rot90(self.targeting_arrays['E'])
        self.targeting_arrays['W'] = np.rot90(self.targeting_arrays['N'])
        self.targeting_arrays['S'] = np.rot90(self.targeting_arrays['W'])
        self.targeting_arrays['NW'] = np.rot90(self.targeting_arrays['NE'])
        self.targeting_arrays['SW'] = np.rot90(self.targeting_arrays['NW'])
        self.targeting_arrays['SE'] = np.rot90(self.targeting_arrays['SW'])