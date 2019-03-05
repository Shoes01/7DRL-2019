import tcod as libtcod

from components.equippable import example_profile
from game import COLORS
from systems.death import kill
from systems.progression import gain_exp
from systems.stats import get_stats

def attack(attacker, defender, entities, game_map):
    turn_results = []
    ### COMBAT RULES
    # Damage is dealt by skills or by main hand items.
    # Damage is prevented by skills or torso items.
    # Typically, the other items do the following:
        # Offhand items have blocking/parry skills
        # Feet items have leaping/movement skills
        # Ring finger items have powerful long cooldown skills
        # Head items have debuff skills ..?
    
    ### ATTACKER CALCULATIONS
    item = None
    profile = None

    ' Look to see if the attacker is using a skill. '
    for _, temp_item in attacker.body.parts.items():
        if temp_item and temp_item.skill and temp_item.skill.selected:
            profile = temp_item.skill.profile
    
    ' If they are not using a skill, look at their main hand weapon. '
    if item is None:
        item = attacker.body.main_hand

    ' If they are not using a skill, look at their main hand weapon. '
    if profile is None:
        if attacker.body.main_hand:
            profile = attacker.body.main_hand.equip.profile
        else:
            profile = example_profile()
            profile['ATK']['ATK'] = 0.5
            profile['MAG']['MAG'] = 0.5

    ' Infer damage values. '
    ATK_value = calculate_profile_number(attacker, profile.get('ATK'))
    MAG_value = calculate_profile_number(attacker, profile.get('MAG'))

    ### DEFENDER CALCULATIONS
    ' Do the same for the defender. '
    item = None
    profile = None

    ' Look to see if the defender is using a skill. '
    for _, temp_item in defender.body.parts.items():
        if temp_item and temp_item.skill and temp_item.skill.selected:
            profile = temp_item.skill.profile
    
    ' If they are not using a skill, look at their torso armor. '
    if profile is None:
        if defender.body.torso:
            profile = defender.body.torso.equip.profile
        else:
            profile = example_profile()
            profile['DEF']['DEF'] = 0.5
            profile['RES']['RES'] = 0.5

    ' Infer defensive values. '
    DEF_value = calculate_profile_number(defender, profile.get('DEF'))
    RES_value = calculate_profile_number(defender, profile.get('RES'))
    
    ### DAMAGE CALCULATIONS
    ' Calculate the damage. '
    ATK_damage = ATK_value - DEF_value
    MAG_damage = MAG_value - RES_value

    if ATK_damage < 0:
        ATK_damage = 0
    if MAG_damage < 0:
        MAG_damage = 0
    
    damage = ATK_damage + MAG_damage

    ### DAMAGE APPLICATIONS
    defender.health.points -= damage

    ### CREATE MESSAGE
    if attacker.base.name == 'player':
        if damage == 0:
            _message = 'You hit the {0}, but do no damage!'.format(defender.base.name)
            _color = COLORS['message_very_bad']
            turn_results.append({'message': (_message, _color)})
        else:
            _message = 'You hit the {0}, dealing {1} ATK and {2} MAG ({3} total damage).'.format(defender.base.name, ATK_damage, MAG_damage, ATK_damage+MAG_damage)
            _color = COLORS['message_good']
            turn_results.append({'message': (_message, _color)})
    elif defender.base.name == 'player':
        if damage == 0:
            _message = 'The {0} hits you, but you take no damage!'.format(attacker.base.name)
            _color = COLORS['message_very_good']
            turn_results.append({'message': (_message, _color)})
        else:
            _message = 'The {0} hits you, dealing {1} ATK and {2} MAG ({3} total damage).'.format(attacker.base.name, ATK_damage, MAG_damage, ATK_damage+MAG_damage)
            _color = COLORS['message_bad']
            turn_results.append({'message': (_message, _color)})
    else:
        if damage == 0:
            _message = 'The {0} hits the {1}, but does no damage.'.format(attacker.base.name, defender.base.name)
            _color = COLORS['message_ok']
            turn_results.append({'message': (_message, _color)})
        else:
            _message = 'The {0} hits the {1}, dealing {2} ATK and {3} MAG ({4} total damage).'.format(attacker.base.name, defender.base.name, ATK_damage, MAG_damage, ATK_damage+MAG_damage)
            _color = COLORS['message_ok']
            turn_results.append({'message': (_message, _color)})
    
    if defender.health.points <= 0:
        _death_message = kill(defender, entities, game_map)
        _death_message.extend(turn_results)
        turn_results = _death_message

    return turn_results

def calculate_profile_number(entity, profile):
    # Given a stat's profile, go through and calculate the damage/defense profile.
    number = 0
    stats = get_stats(entity)

    if profile is None:
        return number

    if profile.get('ATK'):
        number += int(stats.get('ATK') * profile.get('ATK'))
    if profile.get('DEF'):
        number += int(stats.get('DEF') * profile.get('DEF'))
    if profile.get('MAG'):
        number += int(stats.get('MAG') * profile.get('MAG'))
    if profile.get('RES'):
        number += int(stats.get('RES') * profile.get('RES'))
    if profile.get('HP'):
        # Using HP instead of HP_MAX is more interesting, I think!
        number += int(entity.health.points * profile.get('HP'))
    if profile.get('SPD'):
        number += int(stats.get('SPD') * profile.get('SPD'))
    
    return number