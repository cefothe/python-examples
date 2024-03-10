import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodger Game")

player_image = pygame.image.load("player.png")

PLAYER_SIZE = 50
player_image = pygame.transform.scale(player_image, (PLAYER_SIZE, PLAYER_SIZE))

player_x = WIDTH // 2 - PLAYER_SIZE // 2
player_y = HEIGHT - PLAYER_SIZE - 10

ENEMY_SIZE = 30
ENEMY_SPEED = 5
enemy_image = pygame.image.load("alien.png")
enemy_image = pygame.transform.scale(enemy_image, (ENEMY_SIZE, ENEMY_SIZE))

enemy_x = random.randint(0, WIDTH - ENEMY_SIZE)
enemy_y = -ENEMY_SIZE

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 8
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += 8

    

    screen.fill((255,255,255))
    screen.blit(player_image, (player_x, player_y))

    if enemy_y > HEIGHT:
        enemy_x = random.randint(0, WIDTH - ENEMY_SIZE)
        enemy_y = -ENEMY_SIZE

    enemy_y += ENEMY_SPEED
    screen.blit(enemy_image, (enemy_x, enemy_y))
    pygame.display.flip()
    pygame.time.Clock().tick(60)