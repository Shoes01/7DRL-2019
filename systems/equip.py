import tcod as libtcod

from components.body import Bodyparts

def swap_items(entities, player):
    turn_results = []

    floor_item = None
    equipped_item = None

    x, y = player.pos.x, player.pos.y

    for item in entities:
        if item.pos.x == x and item.pos.y == y:
            floor_item = item

    # Disgusting block of code.
    if floor_item.equip.slot == Bodyparts.Head.name:
        equipped_item = player.body.head
        player.body.head = floor_item
    elif floor_item.equip.slot == Bodyparts.Torso.name:
        equipped_item = player.body.torso
        player.body.torso = floor_item
    elif floor_item.equip.slot == Bodyparts.MainHand.name:
        equipped_item = player.body.main_hand
        player.body.main_hand = floor_item
    elif floor_item.equip.slot == Bodyparts.OffHand.name:
        equipped_item = player.body.off_hand
        player.body.off_hand = floor_item
    elif floor_item.equip.slot == Bodyparts.Feet.name:
        equipped_item = player.body.feet
        player.body.feet = floor_item

    entities.remove(floor_item)
    entities.append(equipped_item)
    
    equipped_item.pos.x, equipped_item.pos.y = x, y

    return turn_results

def equip_(entities, item, player):
    turn_results = []

    # Disgusting block of code.
    if item.equip.slot == Bodyparts.Head.name and player.body.head is None:
        player.body.head = item
    elif item.equip.slot == Bodyparts.Torso.name and player.body.torso is None:
        player.body.torso = item
    elif item.equip.slot == Bodyparts.MainHand.name and player.body.main_hand is None:
        player.body.main_hand = item
    elif item.equip.slot == Bodyparts.OffHand.name and player.body.off_hand is None:
        player.body.off_hand = item
    elif item.equip.slot == Bodyparts.Feet.name and player.body.feet is None:
        player.body.feet = item
    else:
        return False
    
    entities.remove(item)
        
    _message = 'The {0} equips the {1}.'.format(player.base.name.capitalize(), item.base.name.capitalize())
    _color = libtcod.blue
    turn_results.append({'message': (_message, _color)})

    return turn_results

def equip(player):
    turn_results = []

    item = player.inv.selected

    if item is None:
        return

    if not item.equip:
        _message = 'You cannot equip your {0}.'.format(item.base.name.capitalize())
        _color = libtcod.red
        turn_results.append({'message': (_message, _color)})
        return turn_results

    if item.equip.slot == Bodyparts.Head.name and player.body.head is None:
        player.body.head = item
    elif item.equip.slot == Bodyparts.Torso.name and player.body.torso is None:
        player.body.torso = item
    elif item.equip.slot == Bodyparts.MainHand.name and player.body.main_hand is None:
        player.body.main_hand = item
    elif item.equip.slot == Bodyparts.OffHand.name and player.body.off_hand is None:
        player.body.off_hand = item
    elif item.equip.slot == Bodyparts.Feet.name and player.body.feet is None:
        player.body.feet = item
    else:
        _message = 'You must unequip the item on your {0}.'.format(item.equip.slot.capitalize())
        _color = libtcod.red
        turn_results.append({'message': (_message, _color)})
        item = None
        return turn_results

    _message = 'You equip your {0} on your {1}.'.format(item.base.name.capitalize(), item.equip.slot.capitalize())
    _color = libtcod.blue
    turn_results.append({'message': (_message, _color)})
    item = None

    return turn_results

def unequip(player):
    turn_results = []
    
    item = player.inv.selected

    if not item.equip:
        _message = 'Your {0} was never equipped.'.format(item.base.name.capitalize())
        _color = libtcod.red
        turn_results.append({'message': (_message, _color)})
        return turn_results

    if item.equip.slot == Bodyparts.Head.name:
        player.body.head = None
    elif item.equip.slot == Bodyparts.Torso.name:
        player.body.torso = None
    elif item.equip.slot == Bodyparts.MainHand.name:
        player.body.main_hand = None
    elif item.equip.slot == Bodyparts.OffHand.name:
        player.body.off_hand = None
    elif item.equip.slot == Bodyparts.Feet.name:
        player.body.feet = None
    else:
        _message = 'Your {0} was never equipped.'.format(item.base.name.capitalize())
        _color = libtcod.red
        turn_results.append({'message': (_message, _color)})
        return turn_results

    _message = 'You unequip your {0} from your {1}.'.format(item.base.name.capitalize(), item.equip.slot.capitalize())
    _color = libtcod.blue
    turn_results.append({'message': (_message, _color)})
    item = None
    
    return turn_results