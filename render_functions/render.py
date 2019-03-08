import tcod as libtcod

from game import COLORS, INFO, ITEMMENU, MAP, LOG, ROOT
from render_functions.character_sheet import render_character_sheet
from render_functions.opening_screen import render_opening_screen
from render_functions.render_compare_items import render_compare_items
from render_functions.render_consume_soul import render_consume_soul
from render_functions.render_item_description import render_item_description
from render_functions.render_item_menu import render_item_menu
from render_functions.render_map import render_map
from render_functions.render_message_log import render_message_log
from render_functions.render_panel import render_panel
from render_functions.victory_screen import render_victory_screen

def render_all(action, consoles, entities, game, game_map, game_state_machine, message_log, mouse, neighborhood, player):
    ' Render all things that appear on the screen. '
    if game.debug_mode and not action:
        action = True
    
    render_map(action, consoles, entities, game, game_map, game_state_machine, neighborhood, player)

    if action or game.redraw_map:
        render_message_log(consoles, message_log)
        render_item_description(consoles, player)
        render_item_menu(consoles, player)
        render_panel(consoles, player) # TODO: Rename
    
    _game_state = game_state_machine.state.__str__()

    if _game_state == 'CompareItems':
        render_compare_items(consoles, entities, player)
    
    if _game_state == 'ConsumeSoul':
        render_consume_soul(consoles, entities, player)
    
    if _game_state == 'CharacterSheet':
        render_character_sheet(consoles, player)
    
    if _game_state == 'VictoryScreen':
        render_victory_screen(consoles)
    
    if _game_state == 'OpeningScreen':
        render_opening_screen(consoles)


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