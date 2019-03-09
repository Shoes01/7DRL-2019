import tcod as libtcod

from components.base import RenderOrder
from game import COLORS, MAP
from systems.stats import get_ordered_soul, get_stats

def render_consume_soul(consoles, entities, player):
    console = consoles['map']
    console_root = consoles['root']

    # Clear console.
    console.clear()

    # Print to console.
    print_border(console)
    print_text(console, entities, player)

    # Send to console.
    console.blit(console_root, MAP.X, MAP.Y, 0, 0, MAP.W, MAP.H)


def print_text(console, entities, player):
    soul = player.soul.soul
    new_soul = None

    for entity in entities:
        if entity.base.render_order == RenderOrder.SOUL and entity.pos.x == player.pos.x and entity.pos.y == player.pos.y:
            new_soul = entity.soul.soul

    console.print(3, 3, 'Proposed soul consumption:')
    console.print(4, 4, 'Use the numpas to rotate the soul before consumption.')

    console.print(4, 6, str(soul))
    console.print(20, 6, '+')
    console.print(22, 6, str(new_soul))
    console.print(35, 6, '=')
    console.print(37, 6, str(soul + new_soul))
    
    console.print(3, 9, 'Stat calculation')
    console.print(4, 10, 'Your race grants a flat bonus to your stats. Race: {0}. Bonus: {1}.'.format(player.race.value['name'].capitalize(), player.race.value['bonus']))
    console.print(4, 11, 'Your job determines the order of the stats.')
    console.print(4, 12, 'HP is x4. If the total is less than 10, it is 10 instead.')

    old_stats = get_ordered_soul(None, player.job, soul)
    new_stats = get_ordered_soul(None, player.job, new_soul + soul)
    total_stats = get_stats(None, player.job, player.race, new_soul + soul)

    order = player.job.value['stats']
    y = 0
    for stat in order:
        _diff = new_stats[stat] - old_stats[stat]
        _string = stat + ': ' + '{:>3}'.format(total_stats[stat]) + ' ({:>3})'.format(_diff)
        if stat == 'HP':
            _string = stat + ' : ' + '{:>3}'.format(total_stats[stat] // 4) + ' ({:>3})'.format(_diff // 4)
        console.print(4, 14 + y, _string)
        y += 1

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
        console.print(MAP.W - 1, y, NS, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)

    # Corners
    console.print(0, 0, ES, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(MAP.W - 1, 0, SW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(0, MAP.H - 1, NE, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(MAP.W - 1, MAP.H - 1, NW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)

    # Column splitter thing
    console.print((MAP.W - 1)//2, 0, WSE_special, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print((MAP.W - 1)//2, MAP.H - 1, NWS_special, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
