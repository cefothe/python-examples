import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
ENEMY_SIZE = 30
PLAYER_SPEED = 8
ENEMY_SPEED = 5
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodger Game")

# Load images
player_image = pygame.image.load("player.png")  # Replace "player.png" with your player image
enemy_image = pygame.image.load("alien.png")    # Replace "enemy.png" with your enemy image
player_image = pygame.transform.scale(player_image, (PLAYER_SIZE, PLAYER_SIZE))
enemy_image = pygame.transform.scale(enemy_image, (ENEMY_SIZE, ENEMY_SIZE))

# Initial player position
player_x = WIDTH // 2 - PLAYER_SIZE // 2
player_y = HEIGHT - PLAYER_SIZE - 10

# Initial enemy position
enemy_x = random.randint(0, WIDTH - ENEMY_SIZE)
enemy_y = -ENEMY_SIZE

# Score
score = 0

# Create font
font = pygame.font.Font(None, 36)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Update player position based on arrow key inputs
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += PLAYER_SPEED

    # Update enemy position
    enemy_y += ENEMY_SPEED

    # Check for collision
    if (
        player_x < enemy_x + ENEMY_SIZE
        and player_x + PLAYER_SIZE > enemy_x
        and player_y < enemy_y + ENEMY_SIZE
        and player_y + PLAYER_SIZE > enemy_y
    ):
        print("Game Over! Your Score:", score)
        pygame.quit()
        sys.exit()

    # If enemy reaches the bottom, reset its position and increase score
    if enemy_y > HEIGHT:
        enemy_x = random.randint(0, WIDTH - ENEMY_SIZE)
        enemy_y = -ENEMY_SIZE
        score += 1

    # Draw background, player, enemy, and score
    screen.fill(WHITE)
    screen.blit(player_image, (player_x, player_y))
    screen.blit(enemy_image, (enemy_x, enemy_y))

    # Display the score
    score_text = font.render("Score: " + str(score), True, RED)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Control frame rate
    pygame.time.Clock().tick(60)
