import numpy as np
import tcod as libtcod

def initialize_fov(game_map):
    fov_map = libtcod.map.Map(game_map.width, game_map.height, order='F')

    fov_map.walkable[...] = ~game_map.tiles['blocks_path']
    fov_map.transparent[...] = ~game_map.tiles['blocks_sight']
    
    return fov_map

def recompute_fov(fov_map, x, y, radius, light_walls=True, algorithm=0):
    fov_map.compute_fov(x, y, radius, light_walls, algorithm)