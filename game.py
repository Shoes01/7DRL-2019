import tcod as libtcod

from collections import namedtuple
from entity import Entity
from dijkstra import Neighborhood
from game_state_machine import GameStateMachine
from map_functions import GameMap
from render_functions.fov import initialize_fov, recompute_fov
from systems.factory import create_monster
from systems.message_log import MessageLog

COLORS = {  'dark_floor': libtcod.light_blue,
            'dark_wall': libtcod.dark_blue,
            'light_floor': libtcod.light_yellow,
            'light_wall': libtcod.dark_yellow,
            'hud_border_fg': libtcod.light_grey,
            'hud_text': libtcod.white,
            'hud_skill_description': libtcod.lime}
FOV_RADIUS = 18
GAME_TITLE = '7DRL 2019'
' Console constants. '
Console = namedtuple('Console', ['X', 'Y', 'W', 'H'])
_vertical_hud_width = 12
_horizontal_hud_height = 8
ROOT = Console(
    X=0, 
    Y=0, 
    W=80, 
    H=60)
MAP = Console(
    X=14, 
    Y=0, 
    W=66,
    H=50)
MENU = Console(
    X=14,           
    Y=10,           
    W=66,
    H=31)
INFO = Console(
    X=1, 
    Y=1,
    W= _vertical_hud_width,
    H=14)
INVENTORY = Console(
    X=1,
    Y=16,
    W= _vertical_hud_width,
    H=19)
MONSTERS = Console(
    X=1,
    Y=36,
    W= _vertical_hud_width,
    H=14)
MESSAGE = Console(
    X=41,
    Y=51,
    W=38,
    H= _horizontal_hud_height)
ITEMDESC = Console(
    X=14,
    Y=51,
    W=26,
    H= _horizontal_hud_height)
ITEMMENU = Console(
    X=1,
    Y=51,
    W= _vertical_hud_width,
    H= _horizontal_hud_height)

def initialize_new_game():
    # Create player entity.
    player = create_monster('player')    

    # Fill entities list.
    entities = []
    entities.append(player)

    # Create consoles.
    libtcod.console_set_custom_font('rexpaint_cp437_10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_CP437)
    consoles = {}
    consoles['root'] = libtcod.console_init_root(ROOT.W, ROOT.H, title=GAME_TITLE, order='F')
    consoles['map'] = libtcod.console.Console(MAP.W, MAP.H, order='F')
    consoles['menu'] = libtcod.console.Console(MENU.W, MENU.H, order='F')
    consoles['message_log'] = libtcod.console.Console(MESSAGE.W, MESSAGE.H, order='F')
    consoles['info'] = libtcod.console.Console(INFO.W, INFO.H, order='F')
    consoles['inventory'] = libtcod.console.Console(INVENTORY.W, INVENTORY.H, order='F')
    consoles['monsters'] = libtcod.console.Console(MONSTERS.W, MONSTERS.H, order='F')
    consoles['item_description'] = libtcod.console.Console(ITEMDESC.W, ITEMDESC.H, order='F')
    consoles['item_menu'] = libtcod.console.Console(ITEMMENU.W, ITEMMENU.H, order='F')

    # Create other basic functions.
    game = GameThing()
    game_map = GameMap(MAP.W, MAP.H)
    key = libtcod.Key()
    message_log = MessageLog(MESSAGE.W, MESSAGE.H)
    mouse = libtcod.Mouse()

    # Create a first map.
    game_map.generate_new_map()

    # Place player and monsters.
    player.pos = game_map.place_player(game_map, player.pos)
    game_map.place_monsters(entities, game_map)

    # Create fov map.
    fov_map = initialize_fov(game_map)
    recompute_fov(fov_map, player.pos.x, player.pos.y, FOV_RADIUS)

    # Create game state machine.
    game_state_machine = GameStateMachine()

    # Create a neighborhood.
    neighborhood = Neighborhood(game_map)

    neighborhood.update_dijkstra_map(entities, (player.pos.x, player.pos.y))

    return consoles, entities, fov_map, game, game_map, game_state_machine, key, message_log, mouse, neighborhood, player

class GameThing:
    def __init__(self):
        self.debug_mode = False
        self.redraw_map = False