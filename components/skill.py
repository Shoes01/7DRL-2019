import numpy as np

class Skill():
    def __init__(self, cooldown, nature, skill):
        self.cooldown = cooldown
        self.skill = skill
        self.nature = nature

        self.selected = False        
        self.legal_targeting_arrays = {}
        self.cooldown_timer = 0

        self.template_E = np.array([])
        self.template_NE = np.array([])
        self.array_size = 0

        if self.skill == 'pierce':
            self.template_E = np.array(
                [   [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 9, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]]
            )
            self.template_NE = np.array(
                [   [0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 9, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]]
            )
            self.array_size, _ = self.template_E.shape