import numpy as np
import random
import tcod as libtcod

from components.base import RenderOrder
from systems.factory import create_boss, create_monster_, create_stairs

class GameMap:
    def __init__(self, width, height, fov_radius, max_depth):
        self.width = width
        self.height = height
        self.depth = 0
        self.max_depth = max_depth
        self.tiles = self.initialize_tiles()
        self.fov_map = libtcod.map.Map(self.width, self.height, order='F')
        self.fov_radius = fov_radius

        self.rooms = []
        self.leaf_rooms = []

    def initialize_tiles(self):
        # Create a numpy array full of ones.
        tiles = np.ones([self.width, self.height], dtype=[('blocks_sight', bool), ('blocks_path', bool), ('explored', bool)], order='F')
        tiles['explored'] = np.zeros([self.width, self.height], dtype=int)

        return tiles

    def initialize_fov(self):
        fov_map = libtcod.map.Map(self.width, self.height, order='F')

        fov_map.walkable[...] = ~self.tiles['blocks_path']
        fov_map.transparent[...] = ~self.tiles['blocks_sight']
        
        return fov_map

    def recompute_fov(self, x, y, light_walls=True, algorithm=0):
        self.fov_map.compute_fov(x=x, y=y, radius=self.fov_radius, light_walls=light_walls, algorithm=algorithm)

    def generate_new_map(self, entities, player):
        self.tiles = self.initialize_tiles()

        bsp = libtcod.bsp.BSP(x=0, y=0, width=self.width, height=self.height)
        bsp.split_recursive(
            depth=5,
            min_width=6,
            min_height=6,
            max_horizontal_ratio=1.5,
            max_vertical_ratio=1.5,
        )

        for node in bsp.pre_order():
            if node.children:
                node1, node2 = node.children
                self.connect_rooms(node1, node2)
            else:
                self.dig_room(node)
        
        entities.clear()
        
        self.place_player(entities, player)

        if self.depth == self.max_depth:
            self.place_boss(entities)
        else:
            self.place_stairs(entities)
            self.depth += 1

        self.place_monsters(entities)
        self.fov_map = self.initialize_fov()
        self.recompute_fov(player.pos.x, player.pos.y)
    
    def dig_room(self, node):
        ' Dig out a room in the center. Nothing fancy. '
        self.rooms.append(node)
        if len(node.children) == 0:
            self.leaf_rooms.append(node)
        for x in range(node.x + 1, node.x + node.w - 1):
            for y in range(node.y + 1, node.y + node.h - 1):
                self.tiles[x, y] = False, False, False

    def connect_rooms(self, node1, node2):
        ' Connect the middle of the rooms. Or nodes. '
        x1c = node1.x + ( node1.w ) // 2
        y1c = node1.y + ( node1.h ) // 2
        x2c = node2.x + ( node2.w ) // 2
        y2c = node2.y + ( node2.h ) // 2
        if x1c == x2c:
            start = 99
            end = 0
            if y1c < y2c:
                start = y1c
                end = y2c
            else:
                end = y1c
                start = y2c
        
            for y in range(start + 1, end):
                self.tiles[x1c, y] = False, False, False
        if y1c == y2c:
            start = 99
            end = 0
            if x1c < x2c:
                start = x1c
                end = x2c
            else:
                end = x1c
                start = x2c
        
            for x in range(start + 1, end):
                self.tiles[x, y1c] = False, False, False
        
    def place_player(self, entities, player):
        room = self.leaf_rooms.pop(random.randint(0, len(self.leaf_rooms) - 1))
        self.rooms.remove(room)

        success = False
        while not success:
            player.pos.x = random.randint(room.x, room.x + room.w - 1)
            player.pos.y = random.randint(room.y, room.y + room.h - 1)

            _, blocks_path, _ = self.tiles[player.pos.x, player.pos.y]

            if not blocks_path:
                success = True
        
        entities.append(player)
    
    def place_stairs(self, entities):
        room = self.leaf_rooms.pop(random.randint(0, len(self.leaf_rooms) - 1))
        self.rooms.remove(room)

        stairs = create_stairs()
        entities.append(stairs)

        success = False
        while not success:
            stairs.pos.x = random.randint(room.x, room.x + room.w - 1)
            stairs.pos.y = random.randint(room.y, room.y + room.h - 1)

            _, blocks_path, _ = self.tiles[stairs.pos.x, stairs.pos.y]

            if not blocks_path:
                success = True
    
    def place_monsters(self, entities):
        for room in self.rooms:
            size = room.h + room.w
            number_of_monsters = size // 5  # This controls monster density

            while number_of_monsters > 0:
                monster = create_monster_(difficulty=self.depth)

                x = random.randint(room.x, room.x + room.w - 1)
                y = random.randint(room.y, room.y + room.h - 1)
                monster.pos.x, monster.pos.y = x, y

                _, blocks_path, _ = self.tiles[x, y]

                if not blocks_path and not tile_occupied(entities, x, y):
                    entities.append(monster)

                number_of_monsters -= 1

    def place_boss(self, entities):
        room = self.leaf_rooms.pop(random.randint(0, len(self.leaf_rooms) - 1))
        self.rooms.remove(room)

        boss = create_boss(difficulty=self.depth)

        success = False
        while not success:
            boss.pos.x = random.randint(room.x, room.x + room.w - 1)
            boss.pos.y = random.randint(room.y, room.y + room.h - 1)

            _, blocks_path, _ = self.tiles[boss.pos.x, boss.pos.y]

            if not blocks_path:
                success = True
        
        entities.append(boss)

def is_stairs(entities, x, y):
    for entity in entities:
        if entity.pos.x == x and entities.pos.y == y and entity.base.render_order is RenderOrder.STAIRS:
            return True
    return False

def tile_occupied(entities, x, y):
    for entity in entities:
        if entity.health and entity.health.points > 0 and x == entity.pos.x and y == entity.pos.y and entity.base.render_order is not RenderOrder.STAIRS:
            return entity
    else:
        return None

def tile_empty(entities, game_map, x, y):
    for entity in entities:
        if (x == entity.pos.x and y == entity.pos.y) or game_map.tiles['blocks_path'][x, y]:
            return False
    
    return True

def path_unblocked(game_map, xo, yo, xd, yd):
    path = list(libtcod.line_iter(xo, yo, xd, yd))

    for (x, y) in path:
        if 0 < x < game_map.width and 0 < y < game_map.height and not game_map.tiles['blocks_path'][x][y]:
            return True
    else:
        return False