import pygame
import random
import numpy as np

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
            self.grid[i][j] = 2 if random.random() < 0.9 else 4

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
                print(self.grid)
                print(i)
                for j in range(0, len(self.grid[i])):
                    if self.grid[i, j] != 0:
                        i1, j1 = i, j
                        val = self.grid[i, j]
                        if i1 >= len(self.grid) - 1:
                            continue
                        print(i1, j1)
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
                print(self.grid)
                print(i)
                for j in range(len(self.grid[i]) - 1, -1, -1):
                    if self.grid[i, j] != 0:
                        i1, j1 = i, j
                        val = self.grid[i, j]
                        if j1 >= len(self.grid[i]) - 1:
                            continue
                        print(i1, j1)
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

class View:
    def __init__(self, model, width=400, height=400):
        self.model = model
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("2048 Game")
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (200, 200, 200)
        self.font = pygame.font.Font(None, 36)

    def draw_grid(self):
        for i in range(self.model.grid_size):
            for j in range(self.model.grid_size):
                pygame.draw.rect(self.screen, self.WHITE, (j * (self.width // self.model.grid_size), i * (self.height // self.model.grid_size), self.width // self.model.grid_size, self.height // self.model.grid_size))
                value = self.model.grid[i][j]
                if value != 0:
                    text = self.font.render(str(value), True, self.BLACK)
                    text_rect = text.get_rect(center=(j * (self.width // self.model.grid_size) + (self.width // (2 * self.model.grid_size)),
                                                      i * (self.height // self.model.grid_size) + (self.height // (2 * self.model.grid_size))))
                    self.screen.blit(text, text_rect)

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.model.move_tiles('up')
                elif event.key == pygame.K_DOWN:
                    self.model.move_tiles('down')
                elif event.key == pygame.K_LEFT:
                    self.model.move_tiles('left')
                elif event.key == pygame.K_RIGHT:
                    self.model.move_tiles('right')
                self.view.draw_grid()

def main():
    pygame.init()
    grid_size = 4
    model = Model(grid_size)
    view = View(model)
    controller = Controller(model, view)

    while True:
        view.screen.fill(view.GRAY)
        view.draw_grid()
        controller.handle_events()
        pygame.display.flip()
        pygame.time.Clock().tick(30)

if __name__ == "__main__":
    main()
