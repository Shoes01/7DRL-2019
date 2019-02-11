import tcod as libtcod

from game import MAP_HEIGHT, PANEL_HEIGHT, PANEL_WIDTH

def render_panel(console_panel):
    # Reset the console.
    libtcod.console_set_default_background(console_panel, libtcod.black)
    libtcod.console_clear(console_panel)

    # Print to the console.
    libtcod.console_set_default_foreground(console_panel, libtcod.light_gray)
    libtcod.console_print_ex(console_panel, 0, 0, libtcod.BKGND_NONE, libtcod.LEFT, 'TEST STRING')

    # Send to console.
    libtcod.console_blit(console_panel, 0, 0, PANEL_WIDTH, PANEL_HEIGHT, 0, 0, MAP_HEIGHT)