import tcod as libtcod

from game import PANEL

def render_panel(consoles, message_log, player):
    console_panel = consoles['panel']
    console_root = consoles['root']
    # Reset the console.
    console_panel.default_bg = libtcod.black
    console_panel.clear()

    # Print to the console.
    ' Player stats. '
    console_panel.default_fg = libtcod.light_gray
    console_panel.print_(0, 0, get_stat_string(player), libtcod.BKGND_NONE, libtcod.LEFT)
    
    ' Message Log '
    y = 1
    for message in message_log.messages:
        console_panel.default_fg = message.color
        console_panel.print_(message_log.x, y, message.text, libtcod.BKGND_NONE, libtcod.LEFT)
        y += 1

    # Send to console.
    console_panel.blit(dest=console_root, dest_x=0, dest_y=PANEL.Y, src_x=0, src_y=0, width=PANEL.W, height=PANEL.H)

def get_stat_string(player):
    stat_string = ""
    
    hp_string = str(player.stats.hp) + "/" + str(player.stats.hp_max)
    
    attack_string = "ATT: " + str(player.stats.attack)

    defense_string = "DEF: " + str(player.stats.defense)

    stat_string += hp_string + "\n" + attack_string + "\n" + defense_string

    return stat_string