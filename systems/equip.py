import tcod as libtcod

from components.body import Bodyparts

def equip(player):
    turn_results = []

    item = player.inv.selected

    if not item.equip:
        _message = 'You cannot equip your {0}.'.format(item.base.name.capitalize())
        _color = libtcod.red
        turn_results.append({'message': (_message, _color)})
        return turn_results

    if item.equip.slot == Bodyparts.Head.name and player.body.head is None:
        player.body.head = item
    elif item.equip.slot == Bodyparts.Torso.name and player.body.torso is None:
        player.body.torso = item
    elif item.equip.slot == Bodyparts.LeftHand.name and player.body.left_hand is None:
        player.body.left_hand = item
    elif item.equip.slot == Bodyparts.RightHand.name and player.body.right_hand is None:
        player.body.right_hand = item
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
    elif item.equip.slot == Bodyparts.LeftHand.name:
        player.body.left_hand = None
    elif item.equip.slot == Bodyparts.RightHand.name:
        player.body.right_hand = None
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