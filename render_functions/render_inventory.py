import tcod as libtcod

from game import INVENTORY

def render_inventory(consoles, player):
    console_inventory = consoles['inventory']
    console_root = consoles['root']
    # Reset the console.
    console_inventory.default_bg = libtcod.black
    console_inventory.clear()

    # Print to the console.
    console_inventory.default_fg = libtcod.light_gray
    console_inventory.print_(0, 0, get_inventory_string(player), libtcod.BKGND_NONE, libtcod.LEFT)

    # Send to console.
    console_inventory.blit(dest=console_root, dest_x=INVENTORY.X, dest_y=INVENTORY.Y, width=INVENTORY.W, height=INVENTORY.H)

def get_inventory_string(player):
    string = ''

    for item in player.inv.contents:
        string += item.base.name.capitalize() + ','
    
    if len(string) == 0:
        string = 'There is nothing in your inventory.'
    else:
        string += '.'
    
    return string