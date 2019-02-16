import tcod as libtcod

from collections import namedtuple
from entity import Entity
from enum import Enum
from components.base import Base, RenderOrder
from components.inventory import Inventory
from components.pos import Position
from components.stats import Stats
from map_functions import GameMap
from render_functions.fov import initialize_fov, recompute_fov
from systems.message_log import MessageLog

COLORS = {  'dark_floor': libtcod.light_blue,
            'dark_wall': libtcod.dark_blue,
            'light_floor': libtcod.light_yellow,
            'light_wall': libtcod.dark_yellow}
FOV_RADIUS = 18
GAME_TITLE = '7DRL 2019'
' Console constants. '
Console = namedtuple('Console', ['X', 'Y', 'W', 'H'])
ROOT = Console(
    X=0, 
    Y=0, 
    W=80, 
    H=60)

MAP = Console(
    X=0, 
    Y=0, 
    W=ROOT.W,   # 80
    H=50)
MENU = Console(
    X=10,           
    Y=10,           
    W=ROOT.W - 2 * 10,  # 60 
    H=ROOT.H - 3 * 10)  # 40
PANEL = Console(
    X=0, 
    Y=MAP.H,            # 50
    W=ROOT.W // 4,      # 20
    H=ROOT.H - MAP.H)   # 10

MESSAGE = Console(
    X=PANEL.W,          # 20
    Y=PANEL.Y,          # 50
    W=ROOT.W - PANEL.W, # 60 
    H=PANEL.H)          # 10

class GameStates(Enum):
    EXIT = 0
    PLAYER_TURN = 1
    ENEMY_TURN = 2
    PLAYER_DEAD = 3
    OPEN_INVENTORY = 4

def initialize_new_game():
    # Create player entity.
    _base = Base('player', '@', libtcod.white, RenderOrder.ACTOR)
    _inv = Inventory()
    _pos = Position(15, 15)
    _stats = Stats(attack=8, defense=3, hp_max=50)
    player = Entity(base=_base, inv=_inv, pos=_pos, stats=_stats)
    
    # Fill the player's inventory with DEBUG junk
    _base = Base('debug_junk_1', ',', libtcod.pink, RenderOrder.ITEM)
    _pos = Position(-1, -1)
    debug_junk_1 = Entity(base=_base, pos=_pos)
    _base = Base('debug_junk_2', ',', libtcod.pink, RenderOrder.ITEM)
    _pos = Position(-1, -1)
    debug_junk_2 = Entity(base=_base, pos=_pos)
    _base = Base('debug_junk_3', ',', libtcod.pink, RenderOrder.ITEM)
    _pos = Position(-1, -1)
    debug_junk_3 = Entity(base=_base, pos=_pos)
    player.inv.contents.append(debug_junk_1)
    player.inv.contents.append(debug_junk_2)
    player.inv.contents.append(debug_junk_3)

    # Fill entities list.
    entities = []
    entities.append(player)

    # Create consoles.
    libtcod.console_set_custom_font('rexpaint_cp437_10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)
    consoles = {}
    consoles['root'] = libtcod.console_init_root(ROOT.W, ROOT.H, title=GAME_TITLE)
    consoles['map'] = libtcod.console.Console(MAP.W, MAP.H, order='F')
    consoles['menu'] = libtcod.console.Console(MENU.W, MENU.H, order='F')
    consoles['message_log'] = libtcod.console.Console(MESSAGE.W, MESSAGE.H, order='F')
    consoles['panel'] = libtcod.console.Console(PANEL.W, PANEL.H, order='F')

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

    return consoles, entities, fov_map, game, game_map, key, message_log, mouse, player

class GameThing:
    def __init__(self):
        self.state = GameStates.PLAYER_TURN
        self.redraw_map = False