import numpy as np

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        # Create a numpy array full of zeros.
        tiles = np.zeros([self.width, self.height], dtype=[('blocks_sight', bool), ('blocks_path', bool)], order='F')

        # TODO: Find out where to put mapgen code... in a system?
        tiles[20, 20] = True, True
        tiles[20, 21] = True, True
        tiles[20, 22] = True, True

        return tiles