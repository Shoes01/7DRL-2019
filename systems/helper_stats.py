def get_stats(player, stat):
    if stat == 'attack':
        attack = player.stats.attack
        
        for _, item in player.body.parts.items():
            if item:
                attack += item.stats.attack
        
        return attack

    elif stat == 'defense':
        defense = player.stats.defense
        
        for _, item in player.body.parts.items():
            if item:
                defense += item.stats.defense
        
        return defense
        
    elif stat == 'hp_max':
        hp_max = player.stats.hp_max
        
        for _, item in player.body.parts.items():
            if item:
                hp_max += item.stats.hp_max
        
        return hp_max