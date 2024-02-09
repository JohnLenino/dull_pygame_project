import pygame


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
