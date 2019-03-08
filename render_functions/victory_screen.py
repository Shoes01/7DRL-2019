from game import MAP
from render_functions.render_consume_soul import print_border

def render_victory_screen(consoles):
    console = consoles['map']
    console_root = consoles['root']

    console.clear()

    print_border(console)

    console.print(3, 3, 'You have defeated the demon prince of this dungeon! Way to go.')

    console.blit(console_root, MAP.X, MAP.Y, 0, 0, MAP.W, MAP.H)