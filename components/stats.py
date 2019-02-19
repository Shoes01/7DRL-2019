class Stats:
    def __init__(self, attack, defense, hp_max, exp):
        self.base_attack = attack
        self.base_defense = defense
        self.base_hp_max = hp_max
        self.hp = hp_max
        self.exp = exp
        self.level = 1
        self.leveling_factor = 1.1

        self.selected = None
    
    @property
    def exp_needed_for_next_level(self):
        return int(100 * (1 - self.leveling_factor ** self.level) / (1 - self.leveling_factor))
    
    @property
    def attack(self):
        attack = self.base_attack
        
        for _, item in self.owner.base.body.items():
            if item:
                attack += item.stats.base_attack
        
        return attack

    @property
    def defense(self):
        defense = self.base_defense
        
        for _, item in self.owner.base.body.items():
            if item:
                defense += item.stats.base_defense
        
        return defense

    @property
    def hp_max(self):
        hp_max = self.base_hp_max
        
        for _, item in self.owner.base.body.items():
            if item:
                hp_max += item.stats.base_hp_max
        
        return hp_max