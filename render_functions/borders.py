from game import COLORS, ROOT

def render_borders(console):
    # Clear console.
    console.clear()

    # Print to console.
    print_borders(console)

    # Send to console.
    console.blit(dest=console, dest_x=ROOT.X, dest_y=ROOT.Y, width=ROOT.W, height=ROOT.H)

def print_borders(console):
    ### Helper things
    NS = u'\u2551'
    EW = u'\u2550'
    ES = u'\u2554'
    NE = u'\u255a'
    NW = u'\u255d'
    SW = u'\u2557'
    NSW = u'\u2560'
    NES = u'\u2563'
    ESW = u'\u2566'
    NEW = u'\u2569'
    NESW = u'\u256c'
    left_bookend = u'\u2561'
    right_bookend = u'\u255e'
    
    _panel_height = 16
    _panel_width = 14

    for y in range(ROOT.H - _panel_height - 1, ROOT.H):
        console.print(0, y, NS)
        console.print(_panel_width + 1, y, NS)
        console.print(ROOT.W - 1, y, NS)

    for x in range(ROOT.W):
        if x < 16:
            console.print(x, ROOT.H - _panel_height // 2 - 2, EW)
        console.print(x, ROOT.H - _panel_height - 2, EW)        
        console.print(x, ROOT.H - 1, EW)


    # TODO: the nice bits.