class Stats:
    def __init__(self, attack, defense, hp_max, exp):
        self.attack = attack
        self.defense = defense
        self.hp_max = hp_max
        self.hp = hp_max
        self.exp = exp
        self.level = 1
        self.leveling_factor = 1.1
        self.exp_needed_for_next_level = 1

        self.selected = None