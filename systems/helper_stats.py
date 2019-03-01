def get_stats(player, stat):
    if stat == 'attack':
        attack = player.stats.attack
        
        return attack

    elif stat == 'defense':
        defense = player.stats.defense

        return defense
        
    elif stat == 'hp_max':
        hp_max = player.stats.hp_max

        return hp_max
    
    elif stat == 'hp':
        hp = player.stats.hp

        return hp
    
    elif stat == 'magic':
        magic = player.stats.magic

        return magic

    elif stat == 'resistance':
        resistance = player.stats.resistance

        return resistance

    elif stat == 'speed':
        speed = player.stats.speed

        return speed

    elif stat == 'level':
        level = player.stats.level

        return level