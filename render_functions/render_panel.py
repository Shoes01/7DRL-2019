import tcod as libtcod

from game import PANEL

def render_panel(consoles, player):
    console_panel = consoles['panel']
    console_root = consoles['root']
    # Reset the console.
    console_panel.default_bg = libtcod.black
    console_panel.clear()

    # Print to the console.
    console_panel.default_fg = libtcod.light_gray
    console_panel.print_(0, 0, get_stat_string(player), libtcod.BKGND_NONE, libtcod.LEFT)

    # Send to console.
    console_panel.blit(dest=console_root, dest_x=PANEL.X, dest_y=PANEL.Y, width=PANEL.W, height=PANEL.H)

def get_stat_string(player):
    stat_string = ""
    
    hp_string = str(player.stats.hp) + "/" + str(player.stats.hp_max)
    
    attack_string = "ATT: " + str(player.stats.attack)

    defense_string = "DEF: " + str(player.stats.defense)

    level_string = "LVL: " + str(player.stats.level) + " (" + str(player.stats.exp) + "/" + str(player.stats.exp_needed_for_next_level) + ")"

    stat_string += hp_string + "\n" + attack_string + "\n" + defense_string + "\n" + level_string

    return stat_string