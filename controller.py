import os
import pygame


class Controller:
    def __init__(self, game, view):
        # game and view objects
        self.game = game
        self.view = view
        # sounds
        self.win_sound = pygame.mixer.Sound('sounds/win.wav')
        self.losing_sound = pygame.mixer.Sound('sounds/losing.wav')

    def save_data(self):
        # check for best score and score saving
        file = open('data.txt')
        best_score = file.readlines()[0].rstrip()
        file.close()
        os.remove('data.txt')
        file = open('data.txt', 'w')
        if self.game.score > int(best_score):
            file.write(str(self.game.score) + '\n')
        else:
            file.write(best_score + '\n')
        # grid size mode saving
        file.write(str(self.game.grid_size))
        file.close()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.save_data()
                pygame.quit()
                quit()
            # game control
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.game.move_tiles('up')
                elif event.key == pygame.K_DOWN:
                    self.game.move_tiles('down')
                elif event.key == pygame.K_LEFT:
                    self.game.move_tiles('left')
                elif event.key == pygame.K_RIGHT:
                    self.game.move_tiles('right')
            # update screen
            self.view.draw_grid()

    def check_win_losing(self):
        # check win or losing event and saving data
        if self.game.win:
            self.save_data()
            self.win_sound.play()
            self.view.final_screen('You won!')
        elif self.game.losing:
            self.save_data()
            self.losing_sound.play()
            self.view.final_screen('You lose!')
