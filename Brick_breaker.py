import pygame
import random

# inisiasi pygame
pygame.init()

# Ukuran layar
LEBAR, TINGGI = 600, 400
layar = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Brick Breker")

# Warna
HITAM = (0, 0, 0)
PUTIH = (255, 255, 255)
MERAH = (255, 0, 0)
BIRU = (0, 0, 255)

# Paddle
paddle = pygame.Rect(LEBAR // 2 - 50, TINGGI - 30, 100, 10)
paddle_speed = 10

# bola
bola = pygame.Rect(LEBAR // 2, TINGGI // 2, 10, 10)
bola_speed = [4, -4]

# Balok
balok_list = []
for y in range(5):
    for x in range(10):
        balok = pygame.Rect( x * 60 + 5, y * 20 + 5, 50, 15)
        balok_list.append(balok)

#font
font = pygame.font.Font(None, 37)

# Game loop
running = True
while running:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Gerakan paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < LEBAR:
        paddle.x += paddle_speed

    # gerakan bola
    bola.x += bola_speed[0]
    bola.y += bola_speed[1]

    # Tabrakan dengan dinding
    if bola.left <= 0 or bola.right >= LEBAR:
        bola_speed[0] = -bola_speed[0]
    if bola.top <= 0:
        bola_speed[1] = -bola_speed[1]
    
    # Tabrakan dengan paddle
    if bola.colliderect(paddle):
        bola_speed[1] = -bola_speed[1]

    # Tabrakan dengan balok
    for balok in balok_list[:]:
        if bola.colliderect(balok):
            balok_list.remove(balok)
            bola_speed[1] = -bola_speed[1]
            break
    
    # game over
    if bola.bottom >= TINGGI:
        print("Game over!")
        running = False

    # kemenangan
    if not balok_list:
        print("Kamu menang!")
        running = False

    # Gambar
    layar.fill(HITAM)
    pygame.draw.rect(layar, BIRU, paddle)
    pygame.draw.ellipse(layar, PUTIH, bola)
    for balok in balok_list:
        pygame.draw.rect(layar, MERAH, balok)
    pygame.display.flip()

pygame.quit()