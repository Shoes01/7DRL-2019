import numpy as np
import random
import tcod as libtcod

from systems.factory import create_monster

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()
        
        self.rooms = []

    def initialize_tiles(self):
        # Create a numpy array full of ones.
        tiles = np.ones([self.width, self.height], dtype=[('blocks_sight', bool), ('blocks_path', bool), ('explored', bool)], order='F')

        tiles['explored'] = np.zeros([self.width, self.height], dtype=int)

        return tiles
    
    def generate_new_map(self):
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
    
    def dig_room(self, node):
        ' Dig out a room in the center. Nothing fancy. '
        self.rooms.append(node)
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
        
    def place_player(self, game_map, position):
        room = self.rooms.pop(random.randint(0, len(self.rooms) - 1))

        success = False
        while not success:
            position.x = random.randint(room.x, room.x + room.w - 1)
            position.y = random.randint(room.y, room.y + room.h - 1)

            _, blocks_path, _ = game_map.tiles[position.x, position.y]

            if not blocks_path:
                success = True

        return position
    
    def place_monsters(self, entities, game_map):
        for room in self.rooms:
            size = room.h + room.w
            number_of_monsters = size // 5  # This controls monster density

            while number_of_monsters > 0:
                monster = create_monster('zombie')

                x = random.randint(room.x, room.x + room.w - 1)
                y = random.randint(room.y, room.y + room.h - 1)
                monster.pos.x, monster.pos.y = x, y

                _, blocks_path, _ = game_map.tiles[x, y]

                if not blocks_path and not tile_occupied(entities, x, y):
                    entities.append(monster)

                number_of_monsters -= 1

def tile_occupied(entities, x, y):
    for entity in entities:
        if entity.stats and entity.stats.hp > 0 and x == entity.pos.x and y == entity.pos.y:
            return entity
    else:
        return None

def path_unblocked(game_map, xo, yo, xd, yd):
    path = list(libtcod.line_iter(xo, yo, xd, yd))

    for (x, y) in path:
        if 0 < x < game_map.width and 0 < y < game_map.height and not game_map.tiles['blocks_path'][x][y]:
            return True
    else:
        return False