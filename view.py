import os
import sys
import pygame
from button import AnimatedButton
from const import WIDTH, HEIGHT, FONT_PATH, COLORS, BROWN, WHITE


class View:
    def __init__(self, game):
        # game object
        self.game = game
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("2048")
        # final screen sounds
        self.menu_sound = pygame.mixer.Sound('sounds/menu.wav')
        self.exit_sound = pygame.mixer.Sound('sounds/exit.wav')
        # gap sizes and fonts
        self.title_font = pygame.font.Font(FONT_PATH, 36)
        self.score_font = pygame.font.Font(FONT_PATH, 30)
        if self.game.grid_size == 4:
            self.gap_size = 5
            self.cell_font = pygame.font.Font(FONT_PATH, 26)
        elif self.game.grid_size == 8:
            self.gap_size = 3
            self.cell_font = pygame.font.Font(FONT_PATH, 16)
        else:
            self.gap_size = 1
            self.cell_font = pygame.font.Font(FONT_PATH, 8)

    def draw_grid(self):
        self.screen.fill(WHITE)
        for i in range(self.game.grid_size):
            for j in range(self.game.grid_size):
                value = self.game.grid[i][j]
                # select cell color
                if value > 4096:
                    cell_color = COLORS[4096]
                else:
                    cell_color = COLORS[value]
                # draw cell
                pygame.draw.rect(self.screen, cell_color, (
                    j * (WIDTH // self.game.grid_size) + self.gap_size,
                    i * (HEIGHT // self.game.grid_size) + self.gap_size,
                    WIDTH // self.game.grid_size - self.gap_size * 2, HEIGHT // self.game.grid_size - self.gap_size * 2))
                # render cell text
                if value != 0:
                    if value == 2 or value == 4:
                        text = self.cell_font.render(str(value), True, BROWN)
                    else:
                        text = self.cell_font.render(str(value), True, WHITE)
                    text_rect = text.get_rect(
                        center=(j * (WIDTH // self.game.grid_size) + (WIDTH // (2 * self.game.grid_size)),
                                i * (HEIGHT // self.game.grid_size) + (
                                        HEIGHT // (2 * self.game.grid_size))))
                    self.screen.blit(text, text_rect)
        # render score text
        score_text = self.cell_font.render(str(self.game.score), True, BROWN)
        self.screen.blit(score_text, (10, 10))

    def final_screen(self, title_text):
        # buttons and titles
        buttons = [
            AnimatedButton('Menu', 100, 180, 200, 70, COLORS[4], BROWN, 20, self.menu),
            AnimatedButton('Exit', 100, 285, 200, 70, COLORS[16], WHITE, 20, self.exit)]
        title = self.title_font.render(title_text, True, BROWN)
        score_text = self.score_font.render('Score: ' + str(self.game.score), True, BROWN)
        while True:
            # update screen
            self.screen.fill(WHITE)
            mouse_pos = pygame.mouse.get_pos()
            # check buttons hover
            for button in buttons:
                button.check_hover(mouse_pos)
                button.draw(self.screen)
            # draw win title and score title
            self.screen.blit(title, title.get_rect(center=(200, 50)))
            self.screen.blit(score_text, score_text.get_rect(center=(200, 120)))
            # check pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # check buttons click
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons:
                        if button.is_hovered:
                            button.action()
            pygame.display.update()

    def menu(self):
        # restart program
        self.menu_sound.play()
        pygame.time.wait(250)
        pygame.quit()
        os.system("python run.py")
        sys.exit()

    def exit(self):
        self.exit_sound.play()
        pygame.time.wait(250)
        pygame.quit()
        sys.exit()
