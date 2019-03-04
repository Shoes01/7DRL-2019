import tcod as libtcod

from game import COLORS, INFO
from systems.stats import get_stats

def render_panel(consoles, player):
    console_panel = consoles['info']
    console_root = consoles['root']
    # Reset the console.
    console_panel.clear()

    # Print to the console.
    stats = get_stats(player)

    HP = 'HP : {:>3}/{:>3}'.format(str(player.health.points), str(stats.get('HP'))) # TODO: If HP gets moved out of stats, this will need to change too
    ATK = 'ATK: {:>2}'.format(str(stats.get('ATK')))
    DEF = 'DEF: {:>2}'.format(str(stats.get('DEF')))
    MAG = 'MAG: {:>2}'.format(str(stats.get('MAG')))
    RES = 'RES: {:>2}'.format(str(stats.get('RES')))
    SPD = 'SPD: {:>2}'.format(str(stats.get('SPD')))

    console_panel.print(0, 3, HP , fg=COLORS['hud_text'], bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)
    console_panel.print(0, 4, ATK, fg=COLORS['hud_text'], bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)
    console_panel.print(0, 5, DEF, fg=COLORS['hud_text'], bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)
    console_panel.print(0, 6, MAG, fg=COLORS['hud_text'], bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)
    console_panel.print(0, 7, RES, fg=COLORS['hud_text'], bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)
    console_panel.print(0, 8, SPD, fg=COLORS['hud_text'], bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)

    # Send to console.
    console_panel.blit(dest=console_root, dest_x=INFO.X, dest_y=INFO.Y, width=INFO.W, height=INFO.H)