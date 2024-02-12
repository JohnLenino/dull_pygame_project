import pygame


class View:
    def __init__(self, model, width=400, height=400):
        self.model = model
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("2048")
        self.color2 = (238, 228, 218)
        self.color4 = (237, 224, 200)
        self.color8 = (242, 177, 121)
        self.color16 = (245, 149, 99)
        self.color32 = (246, 124, 96)
        self.color64 = (246, 94, 59)
        self.color128 = (237, 207, 115)
        self.color256 = (237, 204, 98)
        self.color512 = (237, 200, 80)
        self.color1024 = (237, 197, 63)
        self.color2048 = (237, 194, 45)
        self.colors = {0: (249, 246, 242),
                       2: (238, 228, 218),
                       4: (237, 224, 200),
                       8: (242, 177, 121),
                       16: (245, 149, 99),
                       32: (246, 124, 96),
                       64: (246, 94, 59),
                       128: (237, 207, 115),
                       256: (237, 204, 98),
                       512: (237, 200, 80),
                       1024: (237, 197, 63),
                       2048: (237, 194, 45)}
        self.BROWN = (119, 110, 101)
        self.WHITE = (249, 246, 242)

        self.font = pygame.font.Font('ClearSans-Bold.ttf', 20)

    def draw_grid(self):
        for i in range(self.model.grid_size):
            for j in range(self.model.grid_size):
                value = self.model.grid[i][j]
                pygame.draw.rect(self.screen, self.colors[value], (
                    j * (self.width // self.model.grid_size), i * (self.height // self.model.grid_size),
                    self.width // self.model.grid_size, self.height // self.model.grid_size))
                if value != 0:
                    if value == 2 or value == 4:
                        text = self.font.render(str(value), True, self.BROWN)
                    else:
                        text = self.font.render(str(value), True, self.WHITE)
                    text_rect = text.get_rect(
                        center=(j * (self.width // self.model.grid_size) + (self.width // (2 * self.model.grid_size)),
                                i * (self.height // self.model.grid_size) + (
                                        self.height // (2 * self.model.grid_size))))
                    self.screen.blit(text, text_rect)
