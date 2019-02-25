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
    
    elif stat == 'hp':
        hp = player.stats.hp

        return hp
    
    elif stat == 'magic':
        magic = player.stats.magic
        
        for _, item in player.body.parts.items():
            if item:
                magic += item.stats.magic
        
        return magic

    elif stat == 'resistance':
        resistance = player.stats.resistance
        
        for _, item in player.body.parts.items():
            if item:
                resistance += item.stats.resistance
        
        return resistance

    elif stat == 'speed':
        speed = player.stats.speed
        
        for _, item in player.body.parts.items():
            if item:
                speed += item.stats.speed
        
        return speed

    elif stat == 'level':
        level = player.stats.level
        
        for _, item in player.body.parts.items():
            if item:
                level += item.stats.level
        
        return level