import numpy as np

class Skill():
    def __init__(self, cooldown, name, nature):
        ' Skill essential data. '
        self.cooldown = cooldown
        self.name = name
        self.nature = nature
        
        ' Skill data that changes with use. '
        self.cooldown_timer = 0
        self.selected = False
        
        ' Skill data that is generated from its name. '
        self.description = 'There is no description.'
        self.legal_targeting_arrays = {}
        self.template_E = np.array([])
        self.template_NE = np.array([])
        self.array_size = 0

        self.initialize_data()
    
    def initialize_data(self):
        if self.name == 'pierce':
            self.description = 'This skill deals full damage in a straight line.'
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