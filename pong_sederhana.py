import pygame

# inisialisasi pygame
pygame.init()

# konstanta permainan
LEBAR, TINGGI = 800, 600
WARNA_LATAR = (0, 0, 0)
WARNA_PUTIH = (255, 255, 255)

# Membuat layar permainan
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("pong sederhana")

# variabel permainan
bola = pygame.Rect(LEBAR // 2 - 15, TINGGI // 2 - 15, 30, 30)
pemukul_kiri = pygame.Rect(20, TINGGI // 2 - 60, 10, 120)
pemukul_kanan = pygame.Rect(LEBAR - 30, TINGGI // 2 - 60, 10, 120)
kecepatan_bola = [4, 4]
kecepatan_pemukul = 6

# Loop utama permainan
running = True
while running:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #mengambil input pemain
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and pemukul_kiri.top > 0:
        pemukul_kiri.y -= kecepatan_pemukul
    if keys[pygame.K_s] and pemukul_kiri.bottom < TINGGI:
        pemukul_kiri.y += kecepatan_pemukul
    if keys[pygame.K_UP] and pemukul_kanan.top > 0:
        pemukul_kanan.y -= kecepatan_pemukul
    if keys[pygame.K_DOWN] and pemukul_kanan.bottom < TINGGI:
        pemukul_kanan.y += kecepatan_pemukul
    
    # Pergerakan bola
    bola.x += kecepatan_bola[0]
    bola.y += kecepatan_bola[1]

    # Pantulan bola di dinding atas dan bawah
    if bola.top <= 0 or bola.bottom >= TINGGI:
        kecepatan_bola[1] = -kecepatan_bola[1]

    # Pantulan bola di pemukul
    if bola.colliderect(pemukul_kiri) or bola.colliderect(pemukul_kanan):
        kecepatan_bola[0] = -kecepatan_bola[0]
    
    # Reset bola jika keluar dari layar
    if bola.left <=0 or bola.right >= LEBAR:
        bola.x, bola.y = LEBAR // 2 - 15, TINGGI // 2 - 15
        kecepatan_bola = [4, 4]

    # mengambar objek di layar
    layar.fill(WARNA_LATAR)
    pygame.draw.rect(layar, WARNA_PUTIH, pemukul_kiri)
    pygame.draw.rect(layar, WARNA_PUTIH, pemukul_kanan)
    pygame.draw.ellipse(layar, WARNA_PUTIH, bola)
    pygame.draw.aaline(layar, WARNA_PUTIH, (LEBAR // 2, 0), (LEBAR // 2, TINGGI))

    # update tampilan
    pygame.display.flip()

# keluar dari game
pygame.quit()