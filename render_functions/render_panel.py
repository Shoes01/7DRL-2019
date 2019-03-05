import tcod as libtcod

from game import COLORS, INFO
from systems.stats import get_stats

def render_panel(consoles, player):
    console = consoles['info']
    console_root = consoles['root']
    # Reset the console.
    console.clear()

    # Print to the console.
    stats = get_stats(player)

    HP = 'HP :{:>3}/{:>3}'.format(str(player.health.points), str(player.health.max))
    SPD = 'SPD:{:>2}'.format(str(stats.get('SPD')))
    ATK = 'ATK:{:>2}'.format(str(stats.get('ATK')))
    DEF = 'DEF:{:>2}'.format(str(stats.get('DEF')))
    MAG = 'MAG:{:>2}'.format(str(stats.get('MAG')))
    RES = 'RES:{:>2}'.format(str(stats.get('RES')))

    console.print(0, 1, HP , fg=COLORS['hud_text'], bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)
    console.print(0, 3, SPD, fg=COLORS['hud_text'], bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)
    console.print(0, 4, ATK, fg=COLORS['hud_text'], bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)
    console.print(7, 4, DEF, fg=COLORS['hud_text'], bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)
    console.print(0, 5, MAG, fg=COLORS['hud_text'], bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)
    console.print(7, 5, RES, fg=COLORS['hud_text'], bg=libtcod.black, bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)
    

    # Send to console.
    # console.clear(ch=5, fg=libtcod.red, bg=libtcod.red) # DEBUG code.
    console.blit(dest=console_root, dest_x=INFO.X, dest_y=INFO.Y, width=INFO.W, height=INFO.H)