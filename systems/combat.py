import tcod as libtcod

from components.equippable import example_profile
from systems.death import kill
from systems.progression import gain_exp
from systems.stats import get_stats

def attack(attacker, defender, entities):
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

    ' If they are not using a skill, look at their torso armor. '
    if profile is None:
        if attacker.body.torso:
            profile = attacker.body.main_hand.equip.profile
        else:
            profile = example_profile

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
            profile = example_profile

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
    if damage <= 0:
        damage = 0
        _message = 'The {0} takes no damage!'.format(defender.base.name.capitalize())
        _color = libtcod.light_yellow
        turn_results.append({'message': (_message, _color)})
    else:
        defender.stats.hp -= damage
        turn_results.append({'message': ('The {0} deals {1} ATK damage and {2} MAG damage to the {3}.'.format(attacker.base.name.capitalize(), ATK_damage, MAG_damage, defender.base.name.capitalize()), libtcod.yellow)})

    if defender.stats.hp <= 0:
        turn_results.extend(kill(defender, entities))
        if not attacker.ai:
            turn_results.extend(gain_exp(defender.stats.exp, attacker))
    
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
        number += int(entity.stats.hp * profile.get('HP'))
    if profile.get('SPD'):
        number += int(stats.get('SPD') * profile.get('SPD'))
    
    return number