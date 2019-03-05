import tcod as libtcod

from game import ITEMMENU

def render_item_menu(consoles, player):
    console = consoles['item_menu']
    console_root = consoles['root']

    # Reset console.
    console.clear()

    # Print to console.
    """
    Q: Ring Finger
    W: Helmet
    E: Feet
    A: Main Hand
    S: Torso
    D: Off Hand
    """
    
    ' Print the Q square. '
    _color = libtcod.grey
    if player.body.ring_finger is not None:
        _color = libtcod.white
        if player.body.ring_finger.skill.selected:
            _color = libtcod.green

        if player.body.ring_finger.skill.cooldown_timer:
            _string = '{:>2}'.format(player.body.ring_finger.skill.cooldown_timer)
            _color = libtcod.light_red
            console.print(2, 2, _string, fg=_color)
    draw_box(_color, console, 1, 0)
    console.print(2, 1, 'Q', fg=_color)

    ' Print the W square. '
    _color = libtcod.grey
    if player.body.head is not None:
        _color = libtcod.white
        if player.body.head.skill.selected:
            _color = libtcod.green

        if player.body.head.skill.cooldown_timer:
            _string = '{:>2}'.format(player.body.head.skill.cooldown_timer)
            _color = libtcod.light_red
            console.print(6, 2, _string, fg=_color)
    draw_box(_color, console, 5, 0)
    console.print(6, 1, 'W', fg=_color)

    ' Print the E square. '
    _color = libtcod.grey
    if player.body.feet is not None:
        _color = libtcod.white
        if player.body.feet.skill.selected:
            _color = libtcod.green

        if player.body.feet.skill.cooldown_timer:
            _string = '{:>2}'.format(player.body.feet.skill.cooldown_timer)
            _color = libtcod.light_red
            console.print(10, 2, _string, fg=_color)
    draw_box(_color, console, 9, 0)
    console.print(10, 1, 'E', fg=_color)

    ' Print the A square. '
    _color = libtcod.grey
    if player.body.off_hand is not None:
        _color = libtcod.white
        if player.body.off_hand.skill.selected:
            _color = libtcod.green

        if player.body.off_hand.skill.cooldown_timer:
            _string = '{:>2}'.format(player.body.off_hand.skill.cooldown_timer)
            _color = libtcod.light_red
            console.print(2, 6, _string, fg=_color)
    draw_box(_color, console, 1, 4)
    console.print(2, 5, 'A', fg=_color)

    ' Print the S square. '
    _color = libtcod.grey
    if player.body.torso is not None:
        _color = libtcod.white
        if player.body.torso.skill.selected:
            _color = libtcod.green

        if player.body.torso.skill.cooldown_timer:
            _string = '{:>2}'.format(player.body.torso.skill.cooldown_timer)
            _color = libtcod.light_red
            console.print(6, 6, _string, fg=_color)
    draw_box(_color, console, 5, 4)
    console.print(6, 5, 'S', fg=_color)

    ' Print the D square. '
    _color = libtcod.grey
    if player.body.main_hand is not None:
        _color = libtcod.white
        if player.body.main_hand.skill.selected:
            _color = libtcod.green
        
        if player.body.main_hand.skill.cooldown_timer:
            _string = '{:>2}'.format(player.body.main_hand.skill.cooldown_timer)
            _color = libtcod.light_red
            console.print(10, 6, _string, fg=_color)
    draw_box(_color, console, 9, 4)
    console.print(10, 5, 'D', fg=_color)

    ' Print decorative border. '
    for y in range(ITEMMENU.H):
        console.print(ITEMMENU.X - 1, y, u'\u2591')
        console.print(ITEMMENU.X + ITEMMENU.W - 2, y, u'\u2591')

    # Send to console.
    # console.clear(ch=5, fg=libtcod.blue, bg=libtcod.blue) # DEBUG code.
    console.blit(console_root, ITEMMENU.X, ITEMMENU.Y, 0, 0, ITEMMENU.W, ITEMMENU.H)

def draw_box(color, console, x, y):
    # Unicode charcaters.
    SE = u'\u250c'
    NS = u'\u2502'
    NE = u'\u2510'
    WS = u'\u2514'
    EW = u'\u2500'
    NW = u'\u2518'

    # Corners.
    console.print(x, y, SE, fg=color)
    console.print(x, y + 3, WS, fg=color)
    console.print(x + 3, y, NE, fg=color)
    console.print(x + 3, y + 3, NW, fg=color)

    # Lines
    console.print(x, y + 1, NS, fg=color)
    console.print(x, y + 2, NS, fg=color)
    console.print(x + 3, y + 1, NS, fg=color)
    console.print(x + 3, y + 2, NS, fg=color)
    console.print(x + 1, y, EW, fg=color)
    console.print(x + 2, y, EW, fg=color)
    console.print(x + 1, y + 3, EW, fg=color)
    console.print(x + 2, y + 3, EW, fg=color)