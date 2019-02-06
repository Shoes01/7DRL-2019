import numpy as np

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = np.zeros([self.width, self.height], dtype=int)
        # TODO: Use an Enum system here?
        tiles[30][22] = 1
        tiles[31][22] = 1
        tiles[32][22] = 1

        return tiles