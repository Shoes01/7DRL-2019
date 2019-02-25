class Stats:
    def __init__(self, attack, defense, exp, hp_max, magic, resistance, speed):
        self.attack = attack
        self.defense = defense
        self.exp = exp
        self.hp_max = hp_max
        self.magic = magic
        self.resistance = resistance
        self.speed = speed

        self.level = 1
        self.leveling_factor = 1.1
        self.exp_needed_for_next_level = 1
        self.hp = hp_max

        self.selected = None