from game import MAP
from render_functions.render_consume_soul import print_border

def render_opening_screen(consoles):
    console = consoles['map']
    console_root = consoles['root']

    console.clear()

    print_border(console)

    console.print(3, 3, 'You must defeat the demon prince of this dungeon! Go on.')

    console.print(3, 5, 'Additionally, here is some information on how to play.')
    console.print(3, 6, 'Use the numpad to move. Use Spacebar to equip items from the ground, or to inspect souls before consuming them. Press 5 on the numpad to confirm choice.')
    console.print(3, 7, 'QWEASD keys use skills associated with the item you picked up. I think that is all you need!!')

    console.print(3, 9, 'Press any of these actions to begin.')

    console.blit(console_root, MAP.X, MAP.Y, 0, 0, MAP.W, MAP.H)
