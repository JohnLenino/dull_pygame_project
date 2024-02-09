import pygame


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
