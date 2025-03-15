import pygame
import random

# Inisiasi Game
pygame.init()

# Konstanta permainan
LEBAR, TINGGI = 600, 400
WARNA_LATAR = (0, 0, 0)
WARNA_ULAR = (0, 255, 0)
WARNA_MAKANAN =(255, 0, 0)

# Ukuran Grid
UKURAN_BLOK = 20
kecepatan = 10

# Membuat layar permainan
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Snake Game")

# fungsi untuk membuat makanan di lokasi acak
def buat_makanan():
    return[random.randrange(0, LEBAR // UKURAN_BLOK)* UKURAN_BLOK,
           random.randrange(0, TINGGI // UKURAN_BLOK)* UKURAN_BLOK]

# Inisiasi Ular
ular = [[LEBAR // 2, TINGGI // 2]]
makanan = buat_makanan()

# Arah awal
arah = "KANAN"
delta = {"KIRI": (-UKURAN_BLOK, 0), "KANAN": (UKURAN_BLOK, 0), "ATAS": (0, -UKURAN_BLOK), "BAWAH": (0, UKURAN_BLOK)}

# SKOR Awal
skor = 0
font = pygame.font.Font(None, 36)


# Loop utama permainan
running = True
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and arah != "KANAN":
                arah = "KIRI"
            elif event.key == pygame.K_RIGHT and arah !="KIRI":
                arah = "KANAN"
            elif event.key == pygame.K_UP and arah != "BAWAH":
                arah = "ATAS"
            elif event.key == pygame.K_DOWN and arah != "ATAS":
                arah = "BAWAH"

    # Gerakan Ular
    kepala_baru = [ular[0][0] + delta[arah][0], ular[0][1] + delta[arah][1]]
    ular.insert(0, kepala_baru)

    # cek apakah makan makanan
    if kepala_baru == makanan:
        skor += 1
        makanan = buat_makanan()
    else:
        ular.pop()

    # cek tabrakan
    if(kepala_baru[0] < 0 or kepala_baru[0]>= LEBAR or
       kepala_baru[1] < 0 or kepala_baru[1] >= TINGGI or
       kepala_baru in ular[1:]):
        running = False

    # gambar ulang layar
    layar.fill(WARNA_LATAR)
    for segmen in ular:
        pygame.draw.rect(layar, WARNA_ULAR, pygame.Rect(segmen[0], segmen[1], UKURAN_BLOK, UKURAN_BLOK))
    pygame.draw.rect(layar, WARNA_MAKANAN, pygame.Rect(makanan[0], makanan[1], UKURAN_BLOK, UKURAN_BLOK))

    # Tampilkan skor
    teks_skor = font.render(f"Skor: {skor}", True, (255, 255, 255))
    layar.blit(teks_skor, (10, 10))

    pygame.display.flip()

#keluar dari permainan
pygame.quit()