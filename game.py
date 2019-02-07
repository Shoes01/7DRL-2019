import tcod as libtcod

from entity import Entity
from enum import Enum
from components.base import Base
from components.pos import Position
from map_functions import GameMap

GAME_TITLE = '7DRL 2019'
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 60

COLORS = {  'dark_floor': libtcod.blue,
            'dark_wall': libtcod.dark_blue,
            'light_floor': libtcod.yellow,
            'light_wall': libtcod.dark_yellow}

class GameStates(Enum):
    EXIT = 0
    PLAYER_TURN = 1

def initialize_new_game():
    # Create player entity.
    _base = Base('player', '@', libtcod.white)
    _pos = Position(15, 15)
    player = Entity(_base, _pos)

    # Fill entities list.
    entities = []
    entities.append(player)

    # Create other basic functions.
    con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
    game = Game()
    game_map = GameMap(SCREEN_WIDTH, SCREEN_HEIGHT)
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    return con, entities, game, game_map, key, mouse, player

class Game():
    def __init__(self):
        self.state = GameStates.PLAYER_TURN