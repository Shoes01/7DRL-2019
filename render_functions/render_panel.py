import tcod as libtcod

from game import INFO
from systems.helper_stats import get_stats

def render_panel(consoles, player):
    console_panel = consoles['info']
    console_root = consoles['root']
    # Reset the console.
    console_panel.clear()

    # Print to the console.
    HP = 'HP : {:>3}/{:>3}'.format(str(get_stats(player, 'hp')), str(get_stats(player, 'hp_max')))
    ATT = 'ATT: {:>2}'.format(str(get_stats(player, 'attack')))
    DEF = 'DEF: {:>2}'.format(str(get_stats(player, 'defense')))
    console_panel.print(0, 1, HP , fg=libtcod.white, bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)
    console_panel.print(0, 2, ATT, fg=libtcod.white, bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)
    console_panel.print(0, 3, DEF, fg=libtcod.white, bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)

    # Send to console.
    console_panel.blit(dest=console_root, dest_x=INFO.X, dest_y=INFO.Y, width=INFO.W, height=INFO.H)