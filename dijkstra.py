import numpy as np

from collections import deque

class Neighborhood():
    def __init__ (self, game_map):
        self.directory = {}
        self.dijkstra_map = np.zeros((game_map.height, game_map.width), dtype=int, order='F')
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
    
    def update_dijkstra_map(self, start):
        frontier = deque()
        frontier.append(start)
        visited = {}
        visited[start] = True

        dijkstra_value = 0
        while len(frontier):
            dijkstra_value += 1
            current = frontier.popleft()
            for neighbor in self.neighbors(current):
                if neighbor not in visited:
                    frontier.append(neighbor)
                    self.dijkstra_map[neighbor[1], neighbor[0]] = dijkstra_value
                    visited[neighbor] = True