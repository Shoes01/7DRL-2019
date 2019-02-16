import tcod as libtcod

from game import MENU

def render_menu(consoles, player, type_):
    console_menu = consoles['menu']
    console_root = consoles['root']
    header = ""
    options = []
    reminder_text = ""
    
    # Reset the console.
    console_menu.default_fg = libtcod.white
    console_menu.default_bg = libtcod.dark_gray
    console_menu.clear()

    if type_ == 'inventory':
        header, options, reminder_text = render_inventory_menu(player.inv)
    elif type_ == 'level_up':
        header, options, reminder_text = render_level_up(player.stats)

    # Print to console.
    console_menu.print_(0, 0, header, libtcod.BKGND_NONE, libtcod.LEFT)
    y = 1
    for option in options:
        text, color = option
        console_menu.default_fg = color
        console_menu.print_(0, y, text, libtcod.BKGND_NONE, libtcod.LEFT)
        y += 1
    
    
    console_menu.default_fg = libtcod.white
    console_menu.print_(MENU.W // 2, MENU.H - 1, reminder_text, libtcod.BKGND_NONE, libtcod.CENTER)

    # Send to console.
    console_menu.blit(dest=console_root, dest_x=MENU.X, dest_y=MENU.Y, width=MENU.W, height=MENU.H)

def render_inventory_menu(inventory):
    header = "Inventory"
    options = []
    reminder_text = "To drop an item, select it from the menu and press D."

    letter_index = ord('a')
    for content in inventory.contents:
        text = '(' + chr(letter_index) + ') ' + content.base.name.capitalize()
        if content == inventory.selected:
            color = libtcod.green
            text = '  ' + text
        else:
            color = libtcod.white
        options.append((text, color))
        letter_index += 1
    
    return header, options, reminder_text

def render_level_up(stats):
    header = "LEVEL UP"
    options = []
    reminder_text = "Pick which stat you want to increase. Press Enter to confirm."

    # Generate a list of options prepended with letters, like the inventory.
    ### Will need to use stats_list = list(stats.__dict__.keys()) ; only loop the first 3.
    
    letter_index = ord('a')
    max_index = ord('a') + 3
    for stat in list(stats.__dict__.keys()):
        text = '(' + chr(letter_index) + ') ' + stat.capitalize()
        
        if stats.selected == stat:
            color = libtcod.green
            text = '  ' + text
        else:
            color = libtcod.white
        
        options.append((text, color))

        letter_index += 1
        if letter_index == max_index:
            break
    
    return header, options, reminder_text