import tcod as libtcod

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
ROOT_HEIGHT = 60
ROOT_WIDTH = 80

MAP_HEIGHT = 50
MAP_WIDTH = ROOT_WIDTH
PANEL_HEIGHT = ROOT_HEIGHT - MAP_HEIGHT
PANEL_WIDTH = ROOT_WIDTH

MESSAGE_HEIGHT = PANEL_HEIGHT - 1
MESSAGE_WIDTH = 2 * ROOT_WIDTH // 3
MESSAGE_X = ROOT_WIDTH - MESSAGE_WIDTH

class GameStates(Enum):
    EXIT = 0
    PLAYER_TURN = 1
    ENEMY_TURN = 2
    PLAYER_DEAD = 3

def initialize_new_game():
    # Create player entity.
    _base = Base('player', '@', libtcod.white, RenderOrder.ACTOR)
    _inv = Inventory()
    _pos = Position(15, 15)
    _stats = Stats(attack=8, defense=3, hp_max=50)
    player = Entity(base=_base, inv=_inv, pos=_pos, stats=_stats)

    # Fill entities list.
    entities = []
    entities.append(player)

    # Create other basic functions.
    consoles = {}
    consoles['panel'] = libtcod.console.Console(PANEL_WIDTH, PANEL_HEIGHT, order='F')
    consoles['map'] = libtcod.console.Console(MAP_WIDTH, MAP_HEIGHT, order='F')
    game = GameThing()
    game_map = GameMap(MAP_WIDTH, MAP_HEIGHT)
    key = libtcod.Key()
    message_log = MessageLog(MESSAGE_X, MESSAGE_WIDTH, MESSAGE_HEIGHT)
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