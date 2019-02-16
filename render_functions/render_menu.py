import tcod as libtcod

from game import MENU

def render_menu(consoles, player, type_):
    console_menu = consoles['menu']
    console_root = consoles['root']
    header = ""
    options = []
    
    # Reset the console.
    console_menu.default_fg = libtcod.white
    console_menu.default_bg = libtcod.dark_gray
    console_menu.clear()

    if type_ == 'inventory':
        header, options = render_inventory_menu(header, options, player.inv)

    # Print to console.
    console_menu.print_(0, 0, header, libtcod.BKGND_NONE, libtcod.LEFT)
    y = 1
    for option in options:
        text, color = option
        console_menu.default_fg = color
        console_menu.print_(0, y, text, libtcod.BKGND_NONE, libtcod.LEFT)
        y += 1

    # Send to console.
    console_menu.blit(dest=console_root, dest_x=MENU.X, dest_y=MENU.Y, width=MENU.W, height=MENU.H)

def render_inventory_menu(header, options, inventory):
    header = "Inventory"

    letter_index = ord('a')
    for content in inventory.contents:
        text = '(' + chr(letter_index) + ') ' + content.base.name.capitalize()
        if content == inventory.selected:
            color = libtcod.green
        else:
            color = libtcod.white
        options.append((text, color))
        letter_index += 1
    
    return header, options
