import numpy as np

from components.equippable import example_profile

class Skill():
    def __init__(self, cooldown, name, nature, profile=example_profile):
        ' Skill essential data. '
        self.cooldown = cooldown
        self.name = name
        self.nature = nature
        self.profile = profile
        
        ' Skill data that changes with use. '
        self.cooldown_timer = 0
        self.selected = False
        
        ' Skill data that is generated from its name. '
        self.description = 'There is no description.'
        self.legal_targeting_arrays = {}
        self.template_E = np.array([])
        self.template_NE = np.array([])
        self.array_size = 0
        self.knockback_force = 0

        self.initialize_data()
    
    def initialize_data(self):
        # 17: represents tiles the player must be able to path through.
        # 19: represents where the player is standing.
        # 23: represents where the player will land after using the skill. Does not deal adamage. Must not have an enemy.
        # 29: represents tiles the player will knock back.
        if self.name == 'pierce':
            self.description = 'This skill deals full damage in a straight line.'
            self.template_E = np.array(
                [   [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0, 19,  1,  1,  1],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0]]
            )
            self.template_NE = np.array(
                [   [0,  0,  0,  0,  0,  0,  1],
                    [0,  0,  0,  0,  0,  1,  0],
                    [0,  0,  0,  0,  1,  0,  0],
                    [0,  0,  0, 19,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0]]
            )
        elif self.name == 'leap':
            self.description = 'This skill allows the player to leap to another location.'
            self.template_E = np.array(
                [   [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0, 19, 17, 17, 23],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0]]
            )
            self.template_NE = np.array(
                [   [0,  0,  0,  0,  0,  0, 23],
                    [0,  0,  0,  0,  0, 17,  0],
                    [0,  0,  0,  0, 17,  0,  0],
                    [0,  0,  0, 19,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0]]
            )
        elif self.name == 'none':
            self.description = 'This item has no skill.'
            self.template_E = np.array(
                [   [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0, 19,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0]]
            )
            self.template_NE = np.array(
                [   [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0, 19,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0]]
            )
        elif self.name == 'bash':
            self.description: 'This skill knocks enemies back.'
            self.knockback_force = 3
            self.template_E = np.array(
                [   [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0, 29,  0,  0],
                    [0,  0,  0, 19, 29,  0,  0],
                    [0,  0,  0,  0, 29,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0]]
            )
            self.template_NE = np.array(
                [   [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0, 29, 29,  0,  0],
                    [0,  0,  0, 19, 29,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0],
                    [0,  0,  0,  0,  0,  0,  0]]
            )
        
        self.array_size, _ = self.template_E.shape