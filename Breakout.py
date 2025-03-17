import pygame

#Inisiasi pygame
pygame.init()

#konstanta permainan
LEBAR, TINGGI = 800, 600
WARNA_LATAR =(0, 0, 0)
WARNA_PUTIH = (255, 255, 255)
WARNA_BLOCK = (0, 255,0)

# Membuat layar permainan
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Breakout Game")

# Variabel permainan
bola = pygame.Rect(LEBAR // 2 - 10, TINGGI // 2 - 10, 20, 20)
paddle = pygame.Rect(LEBAR// 2 - 60, TINGGI - 20, 120, 10)
Kecepatan_bola = [4, -4]
Kecepatan_paddle = 8

# Membuat Block
blok_list =[]
for i in range(5):
    for j in range(8):
        blok = pygame.Rect(10 + j * 100, 50 + i * 30, 80, 20)
        blok_list.append(blok)

# Skor awal
skor = 0
font = pygame.font.Font(None, 36)

# Loop utama permainan
running = True
while running:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # mengambil innput pemain
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left> 0 :
        paddle.x -= Kecepatan_paddle
    if keys[pygame.K_RIGHT] and paddle.right < LEBAR:
        paddle.x += Kecepatan_paddle
    
    # pergerakan bola
    bola.x += Kecepatan_bola[0]
    bola.y += Kecepatan_bola[1]

    # Pantulan bola di dinding
    if bola.left <= 0 or bola.right >= LEBAR:
        Kecepatan_bola[0] = -Kecepatan_bola[0]
    if bola.top <= 0:
        Kecepatan_bola[1] = -Kecepatan_bola[1]

    # Pantulan bola di paddle
    if bola.colliderect(paddle):
        Kecepatan_bola[1] = -Kecepatan_bola[1]

    # Deteksi tabrakan dengan blok
    for blok in blok_list[:]:
        if bola.colliderect(blok):
            blok_list.remove(blok)
            skor += 1
            Kecepatan_bola[1] = -Kecepatan_bola[1]
    
    # Game over jika bola jatuh ke bawah
    if bola.bottom >= TINGGI:
        running = False
    
    # Mengambar objek di layar
    layar.fill(WARNA_LATAR)
    pygame.draw.rect(layar, WARNA_PUTIH, paddle)
    pygame.draw.ellipse(layar, WARNA_PUTIH, bola)
    for blok in blok_list:
        pygame.draw.rect(layar, WARNA_BLOCK, blok)

    # Menampilkan score
    teks_skor = font.render(f"Skor : {skor}", True, WARNA_PUTIH)
    layar.blit(teks_skor, (10, 10))

    # update tampilan
    pygame.display.flip()

#keluar dari permainan
pygame.quit()