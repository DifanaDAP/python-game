import pygame
import random
import time

# initialize pygame
pygame.init()

# screen size and colors
WIDTH, HEIGTH = 400, 400
GRID_SIZE = 4
TILE_SIZE = WIDTH // GRID_SIZE
BG_COLOR = (30, 30, 30)
COVER_COLOR = (50, 50, 200)
BORDER_COLOR = ( 200, 200, 200)
TEXT_COLOR = (255, 255, 255)

# setup screen and font
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Memory Macth")
font = pygame.font.Font(None, 48)

# setup card
numbers = list(range(1, (GRID_SIZE * GRID_SIZE // 2) + 1)) * 2
random.shuffle(numbers)
board = [numbers[i * GRID_SIZE:(i + 1) * GRID_SIZE] for i in range(GRID_SIZE)]
revealed = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
pairs_found = 0

# Temporary variable
selected = []

# Draw board
def draw():
    screen.fill(BG_COLOR)
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 3)
            if revealed[y][x]:
                text = font.render(str(board[y][x]), True, TEXT_COLOR)
                screen.blit(text, (x * TILE_SIZE + 25, y * TILE_SIZE + 15))
            else:
                pygame.draw.rect(screen, COVER_COLOR, rect)
    pygame.display.flip()

# game loop
running = True
while running:
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos
            x, y = mx // TILE_SIZE, my // TILE_SIZE
            if not revealed [y][x] and len(selected) < 2:
                revealed[y][x] = True
                selected.append((x, y))

    if len(selected) == 2:
        x1, y1 = selected[0]
        x2, y2 = selected[1]
        if board[y1][x1] != board[y2][x2]:
            pygame.display.flip()
            pygame.time.delay(700)
            revealed[y1][x1] = False
            revealed[y2][x2] = False
        else:
            pairs_found += 1
        selected = []

    if pairs_found ==(GRID_SIZE * GRID_SIZE) // 2:
        print("You win!")
        time.sleep(2)
        running = False

pygame.quit()