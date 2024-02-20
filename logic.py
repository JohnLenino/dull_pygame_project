import pygame
import random
import numpy as np


class Game:
    def __init__(self, grid_size, win_value):
        self.grid_size = grid_size
        self.win_value = win_value
        self.score = 0
        self.grid = np.zeros((grid_size, grid_size), dtype=int)
        self.win = False
        self.losing = False
        # spawn two tiles for starting game
        self.spawn_tile()
        self.spawn_tile()

    def spawn_tile(self):
        empty_cells = [(i, j) for i in range(self.grid_size) for j in range(self.grid_size) if self.grid[i][j] == 0]
        if empty_cells:
            # randomly select empty cells
            i, j = random.choice(empty_cells)
            # randomly select new cells value
            self.grid[i][j] = 2 if random.random() < 0.75 else 4

    def check_win(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j] == self.win_value:
                    # change win flag value to True and play sound
                    self.win = True
                    pygame.time.wait(300)

    def check_losing(self):
        # check if there is an opportunity to make a move
        for i in range(self.grid_size):
            for j in range(1, self.grid_size):
                if self.grid[i][j] == 0:
                    return
                if self.grid[i][j - 1] == self.grid[i][j]:
                    return
                if i >= 1 and self.grid[i - 1][j] == self.grid[i][j]:
                    return
            if self.grid[i][0] == 0:
                return
        # change losing flag value to True and play sound
        self.losing = True
        pygame.time.wait(300)

    def move_tiles(self, direction):
        # moving tiles by direction
        if direction == 'up':
            for i in range(0, len(self.grid)):
                for j in range(0, len(self.grid[i])):
                    if self.grid[i, j] != 0:
                        i1, j1 = i, j
                        val = self.grid[i, j]
                        while (self.grid[i1 - 1, j1] == 0 or self.grid[i1 - 1, j1] == val) and i1 > 0:
                            if self.grid[i1 - 1, j1] == val:
                                # double new cell value
                                self.grid[i1 - 1, j1] = val * 2
                                # change score
                                self.score += val * 2
                                # delete old cell value
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
                                # double new cell value
                                self.grid[i1 + 1, j1] = val * 2
                                # change score
                                self.score += val * 2
                                # delete old cell value
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
                                # double new cell value
                                self.grid[i1, j1 - 1] = val * 2
                                # change score
                                self.score += val * 2
                                # delete old cell value
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
                                # double new cell value
                                self.grid[i1, j1 + 1] = val * 2
                                # change score
                                self.score += val * 2
                                # delete old cell value
                                self.grid[i1, j1] = 0
                                break
                            self.grid[i1, j1 + 1] = val
                            self.grid[i1, j1] = 0
                            j1 += 1
                            if j1 >= len(self.grid[i]) - 1:
                                break
        # check grid changes
        self.spawn_tile()
        self.check_win()
        self.check_losing()
