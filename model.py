import pygame
import numpy as np
import random


class Model:
    def __init__(self, grid_size=4):
        self.grid_size = grid_size
        self.grid = np.zeros((grid_size, grid_size), dtype=int)
        self.spawn_tile()
        self.spawn_tile()

    def spawn_tile(self):
        empty_cells = [(i, j) for i in range(self.grid_size) for j in range(self.grid_size) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2 if random.random() < 0.7 else 4

    def move_tiles(self, direction):
        if direction == 'up':
            for i in range(0, len(self.grid)):
                for j in range(0, len(self.grid[i])):
                    if self.grid[i, j] != 0:
                        i1, j1 = i, j
                        val = self.grid[i, j]
                        while (self.grid[i1 - 1, j1] == 0 or self.grid[i1 - 1, j1] == val) and i1 > 0:
                            if self.grid[i1 - 1, j1] == val:
                                self.grid[i1 - 1, j1] = val * 2
                                self.grid[i1, j1] = 0
                                break
                            self.grid[i1 - 1, j1] = val
                            self.grid[i1, j1] = 0
                            i1 -= 1

        elif direction == 'down':
            for i in range(len(self.grid) - 1, -1, -1):
                for j in range(0, len(self.grid[i])):
                    if self.grid[i, j] != 0:
                        i1, j1 = i, j
                        val = self.grid[i, j]
                        if i1 >= len(self.grid) - 1:
                            continue
                        while (self.grid[i1 + 1, j1] == 0 or self.grid[i1 + 1, j1] == val) and i1 < len(self.grid) - 1:
                            if self.grid[i1 + 1, j1] == val:
                                self.grid[i1 + 1, j1] = val * 2
                                self.grid[i1, j1] = 0
                                break
                            self.grid[i1 + 1, j1] = val
                            self.grid[i1, j1] = 0
                            i1 += 1
                            if i1 >= len(self.grid) - 1:
                                break

        elif direction == 'left':
            for i in range(0, len(self.grid)):
                for j in range(0, len(self.grid[i])):
                    if self.grid[i, j] != 0:
                        i1, j1 = i, j
                        val = self.grid[i, j]
                        while (self.grid[i1, j1 - 1] == 0 or self.grid[i1, j1 - 1] == val) and j1 > 0:
                            if self.grid[i1, j1 - 1] == val:
                                self.grid[i1, j1 - 1] = val * 2
                                self.grid[i1, j1] = 0
                                break
                            self.grid[i1, j1 - 1] = val
                            self.grid[i1, j1] = 0
                            j1 -= 1

        elif direction == 'right':
            for i in range(0, len(self.grid)):
                for j in range(len(self.grid[i]) - 1, -1, -1):
                    if self.grid[i, j] != 0:
                        i1, j1 = i, j
                        val = self.grid[i, j]
                        if j1 >= len(self.grid[i]) - 1:
                            continue
                        while (self.grid[i1, j1 + 1] == 0 or self.grid[i1, j1 + 1] == val) and j1 < len(
                                self.grid[i]) - 1:
                            if self.grid[i1, j1 + 1] == val:
                                self.grid[i1, j1 + 1] = val * 2
                                self.grid[i1, j1] = 0
                                break
                            self.grid[i1, j1 + 1] = val
                            self.grid[i1, j1] = 0
                            j1 += 1
                            if j1 >= len(self.grid[i]) - 1:
                                break
        self.spawn_tile()

