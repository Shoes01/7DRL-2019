import tcod as libtcod

from game import COLORS, INFO
from systems.helper_stats import get_stats

def render_panel(consoles, player):
    console_panel = consoles['info']
    console_root = consoles['root']
    # Reset the console.
    console_panel.clear()

    # Print to the console.
    LVL = 'LVL: {:>2}'.format(str(get_stats(player, 'level')))
    HP = 'HP : {:>3}/{:>3}'.format(str(get_stats(player, 'hp')), str(get_stats(player, 'hp_max')))
    ATT = 'ATT: {:>2}'.format(str(get_stats(player, 'attack')))
    DEF = 'DEF: {:>2}'.format(str(get_stats(player, 'defense')))
    MAG = 'MAG: {:>2}'.format(str(get_stats(player, 'magic')))
    RES = 'RES: {:>2}'.format(str(get_stats(player, 'resistance')))
    SPD = 'SPD: {:>2}'.format(str(get_stats(player, 'speed')))
    console_panel.print(0, 1, LVL, fg=COLORS['hud_text'], bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)    
    console_panel.print(0, 3, HP , fg=COLORS['hud_text'], bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)
    console_panel.print(0, 4, ATT, fg=COLORS['hud_text'], bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)
    console_panel.print(0, 5, DEF, fg=COLORS['hud_text'], bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)
    console_panel.print(0, 6, MAG, fg=COLORS['hud_text'], bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)
    console_panel.print(0, 7, RES, fg=COLORS['hud_text'], bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)
    console_panel.print(0, 8, SPD, fg=COLORS['hud_text'], bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)

    # Send to console.
    console_panel.blit(dest=console_root, dest_x=INFO.X, dest_y=INFO.Y, width=INFO.W, height=INFO.H)