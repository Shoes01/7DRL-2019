import tcod as libtcod

from entity import Entity
from enum import Enum
from components.base import Base
from components.pos import Position
from map_functions import GameMap
from systems.fov import initialize_fov

COLORS = {  'dark_floor': libtcod.light_blue,
            'dark_wall': libtcod.dark_blue,
            'light_floor': libtcod.light_yellow,
            'light_wall': libtcod.dark_yellow}
FOV_RADIUS = 18
GAME_TITLE = '7DRL 2019'
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 60

class GameStates(Enum):
    EXIT = 0
    PLAYER_TURN = 1
    ENEMY_TURN = 2

def initialize_new_game():
    # Create player entity.
    _base = Base('player', '@', libtcod.white)
    _pos = Position(15, 15)
    player = Entity(base=_base, pos=_pos)

    # Fill entities list.
    entities = []
    entities.append(player)

    # Create other basic functions.
    con = libtcod.console.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order='F')
    game = GameThing()
    game_map = GameMap(SCREEN_WIDTH, SCREEN_HEIGHT)
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    # Create a first map.
    game_map.generate_new_map()

    # Create fov map.
    fov_map = initialize_fov(game_map)

    # Place player.
    player.pos = game_map.place_player(game_map, player.pos)

    # Generate monsters.
    game_map.place_monsters(entities, game_map)

    return con, entities, fov_map, game, game_map, key, mouse, player

class GameThing():
    def __init__(self):
        self.state = GameStates.PLAYER_TURN