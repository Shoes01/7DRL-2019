import tcod as libtcod

from components.equippable import example_profile
from systems.death import kill
from systems.progression import gain_exp

def attack(attacker, defender, entities):
    turn_results = []
    ### COMBAT RULES
    # Main hand weapons deal damage.
    # Offhand weapons negate damage.
    
    ### ATTACKER CALCULATIONS
    item = None
    profile = None
    ' Look to see if the player is using a skill. '
    for _, temp_item in attacker.body.parts.items():
        if temp_item and temp_item.skill and temp_item.skill.selected:
            item = temp_item
    
    ' If they are not using a skill, look at their main hand weapon. '
    if item is None:
        item = attacker.body.main_hand

    ' If they do not have one, use an example damage profile. '
    if item is None:
        profile = example_profile
    else:
        profile = item.equip.profile

    ' Infer damage values. '
    ATK_value = calculate_profile_number(attacker, profile.get('ATK'))
    MAG_value = calculate_profile_number(attacker, profile.get('MAG'))

    ### DEFENDER CALCULATIONS
    ' Do the same for the defender. '
    item = None
    profile = None
    ' Look to see if the player is using a skill. '
    for _, temp_item in defender.body.parts.items():
        if temp_item and temp_item.skill and temp_item.skill.selected:
            item = temp_item
    
    ' If they are not using a skill, look at their main hand weapon. '
    if item is None:
        item = defender.body.main_hand

    ' If they do not have one, use an example damage profile. '
    if item is None:
        profile = example_profile
    else:
        profile = item.equip.profile

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
        turn_results.append({'message': ('The {0} deals {1} damage to the {2}.'.format(attacker.base.name.capitalize(), damage, defender.base.name.capitalize()), libtcod.yellow)})

    if defender.stats.hp <= 0:
        turn_results.extend(kill(defender, entities))
        if not attacker.ai:
            turn_results.extend(gain_exp(defender.stats.exp, attacker))
    
    return turn_results

def calculate_profile_number(player, profile):
    # Given a stat's profile, go through and calculate the damage/defense profile.
    number = 0

    if profile is None:
        return number

    if profile.get('ATK'):
        number += int(player.stats.attack * profile.get('ATK'))
    if profile.get('DEF'):
        number += int(player.stats.defense * profile.get('DEF'))
    if profile.get('MAG'):
        number += int(player.stats.magic * profile.get('MAG'))
    if profile.get('RES'):
        number += int(player.stats.resistance * profile.get('RES'))
    if profile.get('HP'):
        # Using HP instead of HP_MAX is more interesting, I think!
        number += int(player.stats.hp * profile.get('HP'))
    if profile.get('SPD'):
        number += int(player.stats.speed * profile.get('SPD'))
    
    return number

### COMBAT
"""
The GUI should have a "damage output" number.
    When no skill is active, it shows the bump attack output.

Bump attacks:
    A bump attack looks at the weapon to apply appropriate damage. It should only deal ATK or MAG damage.
    
    OR easymode: A bump attack uses ATK.
    
Skilled attacks:
    A skill may use any stat to deal damage.
    ATK goes against DEF
    MAG goes against RES

    SPD, DEF, RES or HP all deal pure damage.
    OR these are deals _as_ ATK or MAG. 

"""