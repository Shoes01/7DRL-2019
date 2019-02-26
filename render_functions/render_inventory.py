import tcod as libtcod

from game import COLORS, INVENTORY

def render_inventory(consoles, player):
    console_root = consoles['root']
    console = consoles['inventory']

    # Reset console.
    console.clear()

    # Print to console.
    y = 1
    for item in player.inv.contents:
        console.print(0, y, item.base.name.capitalize(), fg=COLORS['hud_text'], bg_blend=libtcod.BKGND_NONE, alignment=libtcod.LEFT)
        y += 1
    
    # Send to console.
    console.blit(console_root, INVENTORY.X, INVENTORY.Y, 0, 0, INVENTORY.W, INVENTORY.H - 1)