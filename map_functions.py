import numpy as np

class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        # Create a numpy array full of zeros.
        tiles = np.zeros([self.width, self.height], dtype=[('blocks_sight', bool), ('blocks_path', bool)])

        # TODO: Find out where to put mapgen code... in a system?
        tiles[30][30] = (True, True)
        tiles[30][31] = (True, True)
        tiles[30][32] = (True, True)

        return tiles