import tcod as libtcod

from game import MAP

def render_character_sheet(consoles, player):
    console = consoles['map']
    console_root = consoles['root']

    # Clear console.
    console.clear()

    # Print text.
    print_text(console, player)

    # Send to console.
    console.blit(console_root, MAP.X, MAP.Y, 0, 0, MAP.W, MAP.H)

def print_text(console, player):
    # Print the items
    # Print the soul number

    soul = player.soul.soul

    string_1 = 'Your soul:\n' + str(soul)
    console.print(2, 2, string_1, bg=libtcod.black, bg_blend=libtcod.BKGND_SET)