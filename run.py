import pygame
import sys

from model import Model
from view import View
from controller import Controller


class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, text_color, action):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.action = action
        self.is_hovered = False
        self.scale = 1.0

    def draw(self, surface, font):
        if self.is_hovered:
            self.scale = min(1.15, self.scale + 0.0005)
            width = int(self.width * self.scale)
            height = int(self.height * self.scale)
            x = self.x - (width - self.width) // 2
            y = self.y - (height - self.height) // 2
            pygame.draw.rect(surface, self.hover_color, (x, y, width, height))
        else:
            self.scale = max(1.0, self.scale - 0.0005)
            width = int(self.width * self.scale)
            height = int(self.height * self.scale)
            x = self.x - (width - self.width) // 2
            y = self.y - (height - self.height) // 2
            pygame.draw.rect(surface, self.color, (x, y, width, height))

        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x + (self.width // 2), self.y + (self.height // 2))
        surface.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        if self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height:
            self.is_hovered = True
        else:
            self.is_hovered = False


class Menu:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("2048")

        self.color1 = (238, 228, 218)
        self.color2 = (237, 224, 200)
        self.color3 = (242, 177, 121)
        self.color4 = (245, 149, 99)
        self.BROWN = (119, 110, 101)
        self.WHITE = (249, 246, 242)

        self.font = pygame.font.Font('ClearSans-Bold.ttf', 20)

        self.buttons = [
            Button('Новая игра', 100, 40, 200, 50, self.color1, self.color1, self.BROWN, self.new_game),
            Button('Загрузить игру', 100, 130, 200, 50, self.color2, self.color2, self.BROWN, self.load_game),
            Button('Настройки', 100, 220, 200, 50, self.color3, self.color3, self.WHITE, self.settings),
            Button('Выход', 100, 310, 200, 50, self.color4, self.color4, self.WHITE, self.exit)
        ]

    def new_game(self):
        pygame.init()
        grid_size = 4
        model = Model(grid_size)
        view = View(model)
        controller = Controller(model, view)

        while True:
            view.screen.fill(view.WHITE)
            view.draw_grid()
            controller.handle_events()
            pygame.display.flip()
            pygame.time.Clock().tick(30)

    def load_game(self):
        pass

    def settings(self):
        pass

    def exit(self):
        pygame.quit()
        sys.exit()

    def run(self):
        while True:
            self.screen.fill('white')
            pygame.event.pump()
            mouse_pos = pygame.mouse.get_pos()

            for button in self.buttons:
                button.check_hover(mouse_pos)
                button.draw(self.screen, self.font)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        if button.is_hovered:
                            button.action()

            pygame.display.update()


if __name__ == "__main__":
    menu = Menu(400, 400)
    menu.run()
