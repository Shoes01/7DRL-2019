from game import ITEMMENU

def render_item_menu(consoles, player):
    console = consoles['item_menu']
    console_root = consoles['root']

    # Reset console.
    console.clear()

    # Print to console.
    ' Print the A square first. '
    

    # Send to console.
    console.blit(console_root, ITEMMENU.X, ITEMMENU.Y, 0, 0, ITEMMENU.W, ITEMMENU.H)