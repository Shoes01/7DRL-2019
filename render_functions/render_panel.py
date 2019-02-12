import tcod as libtcod

from game import MAP_HEIGHT, PANEL_HEIGHT, PANEL_WIDTH

def render_panel(console_panel, message_log, player):
    # Reset the console.
    libtcod.console_set_default_background(console_panel, libtcod.black)
    libtcod.console_clear(console_panel)

    # Print to the console.
    ' Player stats. '
    libtcod.console_set_default_foreground(console_panel, libtcod.light_gray)
    libtcod.console_print_ex(console_panel, 0, 0, libtcod.BKGND_NONE, libtcod.LEFT, get_stat_string(player))
    
    ' Message Log '
    y = 1
    for message in message_log.messages:
        libtcod.console_set_default_foreground(console_panel, message.color)
        libtcod.console_print_ex(console_panel, message_log.x, y, libtcod.BKGND_NONE, libtcod.LEFT, message.text)
        y += 1

    # Send to console.
    libtcod.console_blit(console_panel, 0, 0, PANEL_WIDTH, PANEL_HEIGHT, 0, 0, MAP_HEIGHT)

def get_stat_string(player):
    stat_string = ""
    
    hp_string = str(player.stats.hp) + "/" + str(player.stats.hp_max)
    
    attack_string = "ATT: " + str(player.stats.attack)

    defense_string = "DEF: " + str(player.stats.defense)

    stat_string += hp_string + "\n" + attack_string + "\n" + defense_string

    return stat_string