import numpy as np

from collections import deque
from map_functions import tile_occupied

class Neighborhood():
    def __init__ (self, game_map):
        self.directory = {}
        self.dijkstra_map = np.ones((game_map.height, game_map.width), dtype=int, order='F')
        self.populate_directory(game_map)

    def neighbors(self, location):
        return self.directory[location]

    def populate_directory(self, game_map):
        directions = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
        
        for (x, y), _ in np.ndenumerate(game_map.tiles):
            results = []
            for direction in directions:
                neighbor = (x + direction[0], y + direction[1])
                if 0 <= neighbor[0] < game_map.width and 0 <= neighbor[1] < game_map.height and not game_map.tiles['blocks_path'][neighbor[0], neighbor[1]]:
                    results.append(neighbor)
            
            self.directory[(x, y)] = results
    
    def update_dijkstra_map(self, entities, start):
        self.dijkstra_map = (self.dijkstra_map * 0 + 1) * 999
        frontier = deque()
        frontier.append(start)
        visited = {}
        visited[start] = True

        self.dijkstra_map[start[1], start[0]] = 0

        while len(frontier):
            current = frontier.popleft()
            for neighbor in self.neighbors(current):
                if neighbor not in visited:
                    if tile_occupied(entities, neighbor[0], neighbor[1]):
                        self.dijkstra_map[neighbor[1], neighbor[0]] = self.dijkstra_map[current[1], current[0]] + 5
                    else:
                        self.dijkstra_map[neighbor[1], neighbor[0]] = self.dijkstra_map[current[1], current[0]] + 1
                    
                    if not self.dijkstra_map[neighbor[1], neighbor[0]] > 50: # Cheap optimization.
                        frontier.append(neighbor)
                    visited[neighbor] = True