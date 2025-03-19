import pygame
import random

# inisiasi game
pygame.init()

#konstanta permainan
LEBAR, TINGGI = 400, 600
WARNA_LATAR = (135, 206, 250)
GRAVITASI = 0.5
LOMPAT = -10
KECEPATAN_PIPA = 4
JARAK_PIPA = 150

# Membuat layar permainan
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Flappy Bird Clone")

# inisiasi burung
burung = pygame.Rect(50, TINGGI // 2, 40, 30)
kecepatan_burung = 0

# inisiasi pipa 
pipa_list = []
for i in range(3):
    tinggi_pipa_atas = random.randint(100, 400)
    pipa_list.append(pygame.Rect(LEBAR + i * 200, 0, 70, tinggi_pipa_atas))
    pipa_list.append(pygame.Rect(LEBAR + i * 200, tinggi_pipa_atas + JARAK_PIPA, 70, TINGGI - tinggi_pipa_atas - JARAK_PIPA ))

#score awal
skor = 0
font = pygame.font.Font(None, 36)

# Loop utama permainan
running = True
while running:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                kecepatan_burung = LOMPAT

    # pergerakan burung
    kecepatan_burung += GRAVITASI
    burung.y += kecepatan_burung

    # pergerakan pipa
    for pipa in pipa_list:
        pipa.x -= KECEPATAN_PIPA

    # Menambahkan pipa baru dan menghapus yang lama
    if pipa_list[0   ].x< -70:
        del pipa_list[:2]
        tinggi_pipa_atas = random.randint(100, 400)
        pipa_list.append(pygame.Rect(LEBAR, 0, 70, tinggi_pipa_atas))
        pipa_list.append(pygame.Rect(LEBAR, tinggi_pipa_atas +JARAK_PIPA, 70, TINGGI - tinggi_pipa_atas - JARAK_PIPA))
        skor += 1

    # cek tabrakan
    if burung.y <= 0 or burung.y >= TINGGI:
        running = False
    for pipa in pipa_list:
        if burung.colliderect(pipa):
            running = False

    # menggambar layar
    layar.fill(WARNA_LATAR)
    pygame.draw.rect(layar, (255, 255, 0), burung)
    for pipa in pipa_list:
        pygame.draw.rect(layar, (0, 255, 9), pipa)

    # menampilkan skor
    teks_skor = font.render(f"Skor: {skor}", True, (255, 255, 255))
    layar.blit(teks_skor, (10, 10))

    pygame.display.flip()

# keluar dari game
pygame.quit()