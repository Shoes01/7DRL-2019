import tcod as libtcod

from components.base import RenderOrder
from components.body import Bodyparts
from game import COLORS, MAP

def render_compare_items(consoles, entities, player):
    # Display the worn items on the left
    # Display the ground item on the right
    # Display damage profiles
    # Display both their skills
    # Render a little square showing the skills
    
    console = consoles['map'] # This is risky?
    console_root = consoles['root']

    # Clear the console.
    console.clear()

    # Print to the console.
    ' Print the border first. '
    print_border(console)

    ' Print some text. '
    print_text(console, entities, player)

    # Send to console.
    console.blit(console_root, MAP.X, MAP.Y, 0, 0, MAP.W, MAP.H)

def print_text(console, entities, player):
    item = None
    for entity in entities:
        if entity.pos.x == player.pos.x and entity.pos.y == player.pos.y and entity.base.render_order == RenderOrder.ITEM:
            item = entity
            break

    equipped_item = player.body.parts.get(item.equip.slot)

    print_column(console, equipped_item, left=True)
    print_column(console, item, left=False)

def print_column(console, item, left):
    # If side is left, add a constant to all the x coords.

    right = 0
    if not left:
        right = MAP.W // 2

    # Title
    console.print(2 + right, 2, 'Equipped item\n  ' + item.base.name.capitalize())
    
    # Main hand items!
    if item.equip.slot == Bodyparts.MainHand.name:
        # Sub title 1
        console.print(2 + right, 6, '--- Bump Attack ---\n  ATK profile')

        # Bump profiles
        profile = item.equip.profile
        print_stats(console, profile['ATK'], 2 + right, 7)

        console.print(2 + right, 15, '  MAG profile')
        print_stats(console, profile['DEF'], 2 + right, 16)

        # Skill profiles
        console.print(2 + right, 23, '--- Skill Attack ---\n  ATK profile')
        profile = item.skill.profile
        print_stats(console, profile['ATK'], 2 + right, 25)

        console.print(2 + right, 32, '  MAG profile')
        print_stats(console, profile['DEF'], 2 + right, 33)

    # Torso items!
    if item.equip.slot == Bodyparts.Torso.name:
        # Sub title 1
        console.print(2 + right, 6, '--- Damage Mitigation ---\n  DEF profile')

        # Bump profiles
        profile = item.equip.profile
        print_stats(console, profile['DEF'], 2 + right, 7)

        console.print(2 + right, 15, '  RES profile')
        print_stats(console, profile['RES'], 2 + right, 16)

        # Skill profiles
        console.print(2 + right, 23, '--- Buff Skill ---\n  DEF profile')
        profile = item.skill.profile
        print_stats(console, profile['DEF'], 2 + right, 25)

        console.print(2 + right, 32, '  RES profile')
        print_stats(console, profile['RES'], 2 + right, 33)

    # Off hand items!
    if item.equip.slot == Bodyparts.OffHand.name:
        # Skill profiles
        console.print(2 + right, 23, '--- Skill Defense ---\n  DEF profile')
        profile = item.skill.profile
        print_stats(console, profile['DEF'], 2 + right, 25)

        console.print(2 + right, 32, '  RES profile')
        print_stats(console, profile['RES'], 2 + right, 33)

def print_stats(console, profile, x, y):
    dy = 0
    for name, value in profile.items():
        string = '   ' + name + ' x ' + str(value)
        if name is 'HP':
            string = '   ' + name + '  x ' + str(value) # One extra space
        if value == 0:
            console.print(x, y + dy, string, fg=libtcod.dark_grey)
        else:
            console.print(x, y + dy, string, fg=libtcod.white)
        dy += 1
    
def print_border(console):
    # Unicode cheat sheet.
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
    WSE_special = u'\u2564'
    NWS_special = u'\u2567'
    NS_special = u'\u2502'
    left_bookend = u'\u2561'
    right_bookend = u'\u255e'

    # Outline of the menu
    for x in range(MAP.W):
        console.print(x, 0, EW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
        console.print(x, MAP.H - 1, EW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    
    for y in range(MAP.H):
        console.print(0, y, NS, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
        console.print((MAP.W - 1) // 2, y, NS_special, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
        console.print(MAP.W - 1, y, NS, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)

    # Corners
    console.print(0, 0, ES, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(MAP.W - 1, 0, SW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(0, MAP.H - 1, NE, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(MAP.W - 1, MAP.H - 1, NW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)

    # Column splitter thing
    console.print((MAP.W - 1)//2, 0, WSE_special, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print((MAP.W - 1)//2, MAP.H - 1, NWS_special, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)