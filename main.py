import pygame
import random
import numpy as np

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Инициализация окна игры
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2048 Game")

# Инициализация переменных игры
grid_size = 8
grid = np.array([np.array([0] * grid_size) * grid_size for _ in range(grid_size)])

# Функция для начальной инициализации двух ячеек
def spawn_tile():
    empty_cells = [(i, j) for i in range(grid_size) for j in range(grid_size) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = 2 if random.random() < 0.9 else 4

# Функция для отрисовки сетки
def draw_grid():
    for i in range(grid_size):
        for j in range(grid_size):
            pygame.draw.rect(screen, WHITE, (j * (width // grid_size), i * (height // grid_size), width // grid_size, height // grid_size))
            value = grid[i][j]
            if value != 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(value), True, BLACK)
                text_rect = text.get_rect(center=(j * (width // grid_size) + (width // (2 * grid_size)),
                                                  i * (height // grid_size) + (height // (2 * grid_size))))
                screen.blit(text, text_rect)

# Функция для обработки событий
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_tiles('up')
            elif event.key == pygame.K_DOWN:
                move_tiles('down')
            elif event.key == pygame.K_LEFT:
                move_tiles('left')
            elif event.key == pygame.K_RIGHT:
                move_tiles('right')

# Функция для перемещения плиток
def move_tiles(direction):
    if direction == 'up':
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i, j] != 0:
                    i1, j1 = i, j
                    val = grid[i, j]
                    while (grid[i1 - 1, j1] == 0 or grid[i1 - 1, j1] == val) and i1 > 0:
                        if grid[i1 - 1, j1] == val:
                            grid[i1 - 1, j1] = val * 2
                            grid[i1, j1] = 0
                            break
                        grid[i1 - 1, j1] = val
                        grid[i1, j1] = 0
                        i1 -= 1

    elif direction == 'down':
        for i in range(len(grid) - 1, -1, -1):
            print(grid)
            print(i)
            for j in range(0, len(grid[i])):
                if grid[i, j] != 0:
                    i1, j1 = i, j
                    val = grid[i, j]
                    if i1 >= len(grid) - 1:
                        continue
                    print(i1, j1)
                    while (grid[i1 + 1, j1] == 0 or grid[i1 + 1, j1] == val) and i1 < len(grid) - 1:
                        if grid[i1 + 1, j1] == val:
                            grid[i1 + 1, j1] = val * 2
                            grid[i1, j1] = 0
                            break
                        grid[i1 + 1, j1] = val
                        grid[i1, j1] = 0
                        i1 += 1
                        if i1 >= len(grid) - 1:
                            break

    elif direction == 'left':
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i, j] != 0:
                    i1, j1 = i, j
                    val = grid[i, j]
                    while (grid[i1, j1 - 1] == 0 or grid[i1, j1 - 1] == val) and j1 > 0:
                        if grid[i1, j1 - 1] == val:
                            grid[i1, j1 - 1] = val * 2
                            grid[i1, j1] = 0
                            break
                        grid[i1, j1 - 1] = val
                        grid[i1, j1] = 0
                        j1 -= 1

    elif direction == 'right':
        for i in range(0, len(grid)):
            print(grid)
            print(i)
            for j in range(len(grid[i]) - 1, -1, -1):
                if grid[i, j] != 0:
                    i1, j1 = i, j
                    val = grid[i, j]
                    if j1 >= len(grid[i]) - 1:
                        continue
                    print(i1, j1)
                    while (grid[i1, j1 + 1] == 0 or grid[i1, j1 + 1] == val) and j1 < len(grid[i]) - 1:
                        if grid[i1, j1 + 1] == val:
                            grid[i1, j1 + 1] = val * 2
                            grid[i1, j1] = 0
                            break
                        grid[i1, j1 + 1] = val
                        grid[i1, j1] = 0
                        j1 += 1
                        if j1 >= len(grid[i]) - 1:
                            break
    spawn_tile()
    draw_grid()


# Основной игровой цикл
spawn_tile()
spawn_tile()
while True:
    screen.fill(GRAY)
    draw_grid()
    handle_events()
    pygame.display.flip()
    pygame.time.Clock().tick(30)
