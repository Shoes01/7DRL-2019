import tcod as libtcod

from game import PANEL
from systems.helper_stats import get_stats

def render_panel(consoles, player):
    console_panel = consoles['panel']
    console_root = consoles['root']
    # Reset the console.
    console_panel.clear()

    # Print to the console.
    # TODO: This is a singlue-use function, so I don't need to try to generalize it. I can be as messy as I want.
    # It should read "ATT: {0} + {1}", where 0: base_attack, 1:bonus_attack, and bonus is green
    console_panel.print(0, 0, get_stat_string(player), fg=libtcod.light_gray, bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)

    # Send to console.
    console_panel.blit(dest=console_root, dest_x=PANEL.X, dest_y=PANEL.Y, width=PANEL.W, height=PANEL.H)

def get_stat_string(player):
    stat_string = ""
    
    hp_string = str(player.stats.hp) + "/" + str(get_stats(player, 'hp_max'))
    
    attack_string = "ATT: " + str(get_stats(player, 'attack'))

    defense_string = "DEF: " + str(get_stats(player, 'defense'))

    level_string = "LVL: " + str(player.stats.level) + " (" + str(player.stats.exp) + "/" + str(player.stats.exp_needed_for_next_level) + ")"

    stat_string += hp_string + "\n" + attack_string + "\n" + defense_string + "\n" + level_string

    return stat_string