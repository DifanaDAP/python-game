import pygame
import random

# Inisialisasi pygame
pygame.init()

# Konstanta permainan
LEBAR, TINGGI = 300, 300
GRID_SIZE = 5
KOTAK_SIZE = LEBAR // GRID_SIZE
WARNA_LATAR = (200, 200, 200)
WARNA_GARIS = (0, 0, 0)
WARNA_TEKS = (0, 0, 0)

# Membuat layar permainan
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Minesweeper Sederhana")

# Mengatur papan permainan
papan = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
terbuka = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
jumlah_bom = 5
bom_posisi = random.sample([(x, y) for x in range(GRID_SIZE) for y in range(GRID_SIZE)], jumlah_bom)

for bx, by in bom_posisi:
    papan[by][bx] = -1
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = bx + dx, by + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and papan[ny][nx] != -1:
                papan[ny][nx] += 1

# Font untuk teks
font = pygame.font.Font(None, 36)

# Fungsi menggambar grid
def gambar_grid():
    layar.fill(WARNA_LATAR)
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            rect = pygame.Rect(x * KOTAK_SIZE, y * KOTAK_SIZE, KOTAK_SIZE, KOTAK_SIZE)
            pygame.draw.rect(layar, WARNA_GARIS, rect, 2)
            if terbuka[y][x]:
                if papan[y][x] == -1:
                    pygame.draw.circle(layar, (255, 0, 0), rect.center, KOTAK_SIZE // 4)
                else:
                    teks = font.render(str(papan[y][x]) if papan[y][x] > 0 else "", True, WARNA_TEKS)
                    layar.blit(teks, (x * KOTAK_SIZE + 10, y * KOTAK_SIZE + 5))
    pygame.display.flip()

# Loop utama permainan
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            grid_x, grid_y = x // KOTAK_SIZE, y // KOTAK_SIZE
            terbuka[grid_y][grid_x] = True
            if papan[grid_y][grid_x] == -1:
                print("Game Over!")
                running = False
    
    gambar_grid()

pygame.quit()
