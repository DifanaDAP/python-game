import pygame
import sys

# inisiasi game
pygame.init()

# konstanta permainan
LEBAR, TINGGI = 300, 300
WARNA_LATAR = (255, 255, 255)
WARNA_GARIS = (0, 0, 0)
WARNA_XO = (0, 0, 255)
UKURAN_GRID = 100

# Membuat layar permainan
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Tic-TAc-Toe")

# Grid permainan
grid = [[None, None, None], [None, None, None], [None, None, None]]
turn = "X"

# fungsi menggambar grid
def gambar_grid():
    layar.fill(WARNA_LATAR)
    for i in range(1, 3):
        pygame.draw.line(layar, WARNA_GARIS, (0, i * UKURAN_GRID), (LEBAR, i * UKURAN_GRID), 3)
        pygame.draw.line(layar, WARNA_GARIS, (i * UKURAN_GRID, 0), (i * UKURAN_GRID, TINGGI), 3)
    for y in range(3):
        for x in range(3):
            if grid[y][x] == "X":
                pygame.draw.line(layar, WARNA_XO, (x * UKURAN_GRID + 20, y * UKURAN_GRID + 20),
                                 ((x + 1) * UKURAN_GRID - 20, (y + 1) * UKURAN_GRID - 20), 3)
                pygame.draw.line(layar, WARNA_XO, ((x + 1) * UKURAN_GRID - 20, y * UKURAN_GRID + 20),
                                 (x * UKURAN_GRID + 20, (y + 1) * UKURAN_GRID - 20), 3)
            elif grid[y][x] == "O":
                pygame.draw.circle(layar, WARNA_XO, ((x * UKURAN_GRID + UKURAN_GRID // 2),
                                (y * UKURAN_GRID + UKURAN_GRID // 2)), 40, 3)
    pygame.display.flip()

# fungsi mengecek kemenangan
def cek_kemenangan():
    for row in grid:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] is not None:
            return grid[0][col]
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] is not None:
        return grid[0][0]
    if grid[0][2] == grid [1][1] == grid[2][0] and grid[0][2] is not None:
        return grid[0][2]
    return None

# looping utama
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            grid_x, grid_y = x // UKURAN_GRID, y // UKURAN_GRID
            if grid[grid_y][grid_x] is None:
                grid[grid_y][grid_x] = turn
                turn = "O" if turn == "X" else "X"

    gambar_grid()
    pemenang = cek_kemenangan()
    if pemenang:
        print(f"Pemenang: {pemenang}")
        pygame.time.delay(2000)
        running = False

pygame.quit()
sys.exit()