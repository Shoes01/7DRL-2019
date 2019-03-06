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
            'hud_skill_description': libtcod.lime,
            'status_stunned': libtcod.purple,
            'message_very_good': libtcod.cyan,
            'message_good': libtcod.green,
            'message_ok': libtcod.white,
            'message_bad': libtcod.crimson,
            'message_very_bad': libtcod.red,
            'message_kill': libtcod.darker_red}
FOV_RADIUS = 18
GAME_TITLE = '7DRL 2019'

' Console constants. '
Console = namedtuple('Console', ['X', 'Y', 'W', 'H'])

ROOT = Console(
    X=0, 
    Y=0, 
    W=100, 
    H=60)

MAP = Console(
    X=0, 
    Y=0, 
    W=100,
    H=42)

LOG = Console(
    X=16, 
    Y=43,
    W=83,
    H=16)

INFO = Console(
    X=1, 
    Y=43,
    W=14,
    H=7)

ITEMMENU = Console(
    X=1,
    Y=51,
    W=14,
    H=8)

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
    consoles['log'] = libtcod.console.Console(LOG.W, LOG.H, order='F')
    consoles['info'] = libtcod.console.Console(INFO.W, INFO.H, order='F')
    consoles['item_menu'] = libtcod.console.Console(ITEMMENU.W, ITEMMENU.H, order='F')

    # Create other basic functions.
    game = GameThing()
    game_map = GameMap(MAP.W, MAP.H)
    key = libtcod.Key()
    message_log = MessageLog(LOG.W, LOG.H)
    mouse = libtcod.Mouse()

    # Create a first map.
    game_map.generate_new_map(entities, player)

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