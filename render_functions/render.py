import tcod as libtcod

from game import COLORS, INFO, INVENTORY, ITEMDESC, ITEMMENU, MAP, MESSAGE, MONSTERS, ROOT
from render_functions.render_compare_items import render_compare_items
from render_functions.render_consume_soul import render_consume_soul
from render_functions.render_inventory import render_inventory
from render_functions.render_item_description import render_item_description
from render_functions.render_item_menu import render_item_menu
from render_functions.render_map import render_map
from render_functions.render_menu import render_menu
from render_functions.render_message_log import render_message_log
from render_functions.render_monster_list import render_monster_list
from render_functions.render_panel import render_panel

def render_all(action, consoles, entities, fov_map, game, game_map, game_state_machine, message_log, mouse, neighborhood, player):
    ' Render all things that appear on the screen. '
    if game.debug_mode and not action:
        action = True
    render_map(action, consoles, entities, fov_map, game, game_map, game_state_machine, neighborhood, player)

    if action or game.redraw_map:
        render_inventory(consoles, player)
        render_item_description(consoles, player)
        render_item_menu(consoles, player)
        render_message_log(consoles, message_log)
        render_monster_list(consoles, entities, fov_map)
        render_panel(consoles, player)
    
    _game_state = game_state_machine.state.__str__()

    if _game_state == 'OpenInventory':
        render_menu(consoles, player, type_='inventory')
    
    if _game_state == 'LeveledUp':
        render_menu(consoles, player, type_='level_up')
    
    if _game_state == 'CompareItems':
        render_compare_items(consoles, entities, player)
    
    if _game_state == 'ConsumeSoul':
        render_consume_soul(consoles, entities, player)

    if game.debug_mode == True:
        get_things_under_mouse(consoles, entities, game_map, neighborhood, mouse)

    libtcod.console_flush()

def get_things_under_mouse(consoles, entities, game_map, neighborhood, mouse):
    console = consoles['map']
    console_root = consoles['root']

    string = 'Coordinate: ({:>2}, {:>2}). '.format(mouse.cx, mouse.cy)

    map_x = mouse.cx - MAP.X
    map_y = mouse.cy - MAP.Y

    if 0 <= map_x < MAP.W and 0 <= map_y < MAP.H:
        # We are inside the game_map. Print things!
        blocks_sight, blocks_path, explored = game_map.tiles[map_x, map_y]
        
        string += 'Map coordinate: ({:>2}, {:>2}).\n'.format(map_x, map_y)
        string += 'Dijkstra value: {0}.\n'.format(neighborhood.dijkstra_map[map_y, map_x])
        string += 'Blocks sight: {:>1}. Blocks path: {:>1}. Explored: {:>1}.'.format(blocks_sight, blocks_path, explored)

        for entity in entities:
            if entity.pos.x == map_x and entity.pos.y == map_y:
                string += '\nEntity: {0}.'.format(entity.base.name.capitalize())

    console.print(0, 0, string, fg=libtcod.white, bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.blit(dest=console_root, dest_x=MAP.X, dest_y=MAP.Y, width=MAP.W, height=MAP.H)

def render_borders(console):
    ' This function renders the borders of the HUD. It should only need to be done once. '
    # Unicode codes for box drawing.
    # Order: NESW
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

    _column_1 = ROOT.X
    _column_2 = ROOT.X + INFO.W + 1
    _column_3 = ROOT.X + ITEMMENU.W + 1
    # if y >= 50
    _column_4 = ROOT.X + ITEMMENU.W + 1 + ITEMDESC.W + 1
    _column_5 = ROOT.X + ITEMMENU.W + 1 + ITEMDESC.W + 1 + MESSAGE.W + 1

    for y in range(ROOT.H):
        console.print(_column_1, ROOT.Y + y, NS, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
        console.print(_column_2, ROOT.Y + y, NS, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
        if y >=50:
            console.print(_column_3, ROOT.Y + y, NS, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
            console.print(_column_4, ROOT.Y + y, NS, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
            console.print(_column_5, ROOT.Y + y, NS, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)

    _row_1 = ROOT.Y
    _row_2 = ROOT.Y + INFO.H + 1
    _row_3 = ROOT.Y + INFO.H + 1 + INVENTORY.H + 1
    _row_4 = ROOT.Y + INFO.H + 1 + INVENTORY.H + 1 + MONSTERS.H + 1
    _row_5 = ROOT.Y + INFO.H + 1 + INVENTORY.H + 1 + MONSTERS.H + 1 + ITEMDESC.H + 1

    for x in range(ROOT.W):
        if x <= INFO.W + 2:
            console.print(ROOT.X + x, _row_1, EW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
            console.print(ROOT.X + x, _row_2, EW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
            console.print(ROOT.X + x, _row_3, EW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
        console.print(ROOT.X + x, _row_4, EW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
        console.print(ROOT.X + x, _row_5, EW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    
    # Print connecting bits.
    console.print(
        0, 
        0, 
        ES, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(
        0, 
        ROOT.H - 1, 
        NE, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(
        ROOT.W - 1, 
        ROOT.H - 1, 
        NW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(
        INFO.W + 1, 
        0, 
        SW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(
        ROOT.W - 1, 
        MAP.H, 
        SW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(
        INFO.W + 1, 
        INFO.H + 1, 
        NES, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(
        INFO.W + 1, 
        INFO.H + INVENTORY.H + 2, 
        NES, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(
        0, 
        INFO.H + 1, 
        NSW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(
        0, 
        INFO.H + INVENTORY.H + 2, 
        NSW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(
        0, 
        MAP.H, 
        NSW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(
        INFO.W + 1, 
        MAP.H, 
        NEW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(
        ITEMMENU.W + ITEMDESC.W + 2, 
        MAP.H, 
        ESW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(
        ITEMMENU.W + 1, 
        MAP.H, 
        ESW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(
        ITEMMENU.W + 1, 
        ROOT.H - 1, 
        NEW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(
        ITEMMENU.W + ITEMDESC.W + 2, 
        ROOT.H - 1, 
        NEW, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)

    # Print titles and bookens.
    console.print(1, 0, left_bookend, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(2, 0, '  PLAYER  ', fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET, alignment=libtcod.LEFT)
    console.print(12, 0, right_bookend, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)

    console.print(1, 15, left_bookend, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(7, 15, ' Invntory ', fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET, alignment=libtcod.CENTER)
    console.print(12, 15, right_bookend, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)

    console.print(1, 35, left_bookend, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(7, 35, ' Monsters ', fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET, alignment=libtcod.CENTER)
    console.print(12, 35, right_bookend, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)

    console.print(1, 50, left_bookend, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(7, 50, ' ItemMenu ', fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET, alignment=libtcod.CENTER)
    console.print(12, 50, right_bookend, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)

    console.print(21, 50, left_bookend, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(27, 50, ' ItemDesc ', fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET, alignment=libtcod.CENTER)
    console.print(32, 50, right_bookend, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)

    console.print(54, 50, left_bookend, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)
    console.print(60, 50, ' MessgLog ', fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET, alignment=libtcod.CENTER)
    console.print(65, 50, right_bookend, fg=COLORS['hud_border_fg'], bg=libtcod.black, bg_blend=libtcod.BKGND_SET)

    console.blit(dest=console, dest_x=ROOT.X, dest_y=ROOT.Y, width=ROOT.W, height=ROOT.H)

    libtcod.console_flush()