import numpy as np
import tcod as libtcod

def initialize_fov(game_map):
    fov_map = libtcod.map_new(game_map.width, game_map.height)

    for (x, y), _ in np.ndenumerate(game_map.tiles):
        blocks_sight, blocks_path = game_map.tiles[x][y]

        libtcod.map_set_properties(fov_map, x, y, not blocks_sight, not blocks_path)
    
    return fov_map

def recompute_fov(fov_map, x, y, radius, light_walls=True, algorithm=0):
    libtcod.map_compute_fov(fov_map, x, y, radius, light_walls, algorithm)