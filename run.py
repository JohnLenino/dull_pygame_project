import sys
import pygame
import time
from logic import Game
from view import View
from controller import Controller
from button import AnimatedButton
from const import WIDTH, HEIGHT, FONT_PATH, COLOR2, COLOR4, COLOR8, COLOR16, WHITE, BROWN


class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("2048")
        # read best score data
        file = open('data.txt')
        data = file.readlines()
        file.close()
        self.best_score = data[0].rstrip()
        self.grid_size = data[1].rstrip()
        # create best score title
        self.best_score_text = pygame.font.Font(FONT_PATH, 30).render('Best score: ' + self.best_score, True, BROWN)
        self.best_score_text_rect = self.best_score_text.get_rect(center=(200, 65))
        # sounds
        self.click_sound = pygame.mixer.Sound('sounds/click.wav')
        self.exit_sound = pygame.mixer.Sound('sounds/exit.wav')
        # create menu buttons
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        # color grid size buttons
        button_4_color, button_8_color, button_16_color = COLOR4, COLOR4, COLOR4
        if self.grid_size == '4':
            button_4_color = COLOR8
        elif self.grid_size == '8':
            button_8_color = COLOR8
        else:
            button_16_color = COLOR8
        # create button list
        self.buttons = [
            AnimatedButton('New game', 100, 130, 200, 50, COLOR2, BROWN, 20, self.new_game),
            AnimatedButton('4', 60, 205, 70, 70, button_4_color, WHITE, 20, self.change_gs4, animated=False),
            AnimatedButton('8', 160, 205, 70, 70, button_8_color, WHITE, 20, self.change_gs8, animated=False),
            AnimatedButton('16', 260, 205, 70, 70, button_16_color, WHITE, 20, self.change_gs16, animated=False),
            AnimatedButton('Exit', 100, 310, 200, 50, COLOR16, WHITE, 20, self.exit)]

    def new_game(self):
        # create new game
        pygame.init()
        game = Game(int(self.grid_size), 2048 * (int(self.grid_size) ** 2 // 16))
        view = View(game)
        controller = Controller(game, view)
        while True:
            # update screen and check events
            controller.handle_events()
            controller.check_win_losing()
            pygame.display.flip()

    def change_gs4(self):
        # set grid size value to 4 and create buttons again
        self.grid_size = '4'
        self.create_buttons()

    def change_gs8(self):
        # set grid size value to 8 and create buttons again
        self.grid_size = '8'
        self.create_buttons()

    def change_gs16(self):
        # set grid size value to 16 and create buttons again
        self.grid_size = '16'
        self.create_buttons()

    def exit(self):
        self.exit_sound.play()
        pygame.time.wait(250)
        pygame.quit()
        sys.exit()

    def run(self):
        while True:
            # update screen
            self.screen.fill(WHITE)
            mouse_pos = pygame.mouse.get_pos()
            # check buttons hover
            for button in self.buttons:
                button.check_hover(mouse_pos)
                button.draw(self.screen)
            # draw best score title
            self.screen.blit(self.best_score_text, self.best_score_text_rect)
            # check pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # check buttons click
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        if button.is_hovered:
                            self.click_sound.play()
                            button.action()
            pygame.display.update()


if __name__ == "__main__":
    menu = Menu()
    menu.run()
