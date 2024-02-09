import pygame
from model.model import Model
from view.view import View
from controller.controller import Controller


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
