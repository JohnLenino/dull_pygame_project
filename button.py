import pygame
from const import FONT_PATH


class AnimatedButton:
    def __init__(self, text, x, y, width, height, color, text_color, font_size, action, font_path=FONT_PATH,
                 animated=True):
        # initialize animated button class
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text_color = text_color
        self.font = pygame.font.Font(font_path, font_size)
        self.animated = animated
        self.action = action
        self.is_hovered = False
        self.scale = 1.0

    def draw(self, surface):
        if self.is_hovered:
            # if button is hovered, then increase its size
            if self.animated:
                self.scale = min(1.1, self.scale + 0.0005)
            # draw button rect
            width = int(self.width * self.scale)
            height = int(self.height * self.scale)
            x = self.x - (width - self.width) // 2
            y = self.y - (height - self.height) // 2
            pygame.draw.rect(surface, self.color, (x, y, width, height))
        else:
            # if the button is not hovered, then reduce its size
            if self.animated:
                self.scale = max(1.0, self.scale - 0.0005)
            # draw button rect
            width = int(self.width * self.scale)
            height = int(self.height * self.scale)
            x = self.x - (width - self.width) // 2
            y = self.y - (height - self.height) // 2
            pygame.draw.rect(surface, self.color, (x, y, width, height))
        # draw buttons text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x + (self.width // 2), self.y + (self.height // 2))
        surface.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        if self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height:
            # if button is hovered, then change flag to True
            self.is_hovered = True
        else:
            # if button is not hovered, then change flag to False
            self.is_hovered = False
