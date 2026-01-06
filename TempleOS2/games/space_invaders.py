import pygame
import random
import math
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders - TempleOS")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_BLUE = (10, 10, 40)
GREEN = (50, 255, 50)
RED = (255, 50, 50)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()
FPS = 60

font = pygame.font.SysFont("consolas", 24)
big_font = pygame.font.SysFont("consolas", 48)

player_width = 50
player_height = 30
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 70
player_speed = 6

bullet_width = 4
bullet_height = 12
bullet_speed = 10
bullet_state = "ready"  # "ready" or "fire"
bullet_x = 0
bullet_y = player_y

enemy_width = 40
enemy_height = 30
num_enemies = 8
enemy_speed_x = 2
enemy_speed_y = 30

enemies = []
for i in range(num_enemies):
    x = random.randint(50, WIDTH - 50 - enemy_width)
    y = random.randint(40, 150)
    enemies.append([x, y])

score = 0
lives = 3
game_over = False

def draw_player(x, y):
    body_rect = pygame.Rect(x, y, player_width, player_height)
    pygame.draw.rect(screen, GREEN, body_rect)
    tip = (x + player_width // 2, y - 15)
    left = (x, y)
    right = (x + player_width, y)
    pygame.draw.polygon(screen, GREEN, [left, right, tip])

def draw_enemy(x, y):
    body_rect = pygame.Rect(x, y, enemy_width, enemy_height)
    pygame.draw.rect(screen, RED, body_rect)
    eye_radius = 4
    pygame.draw.circle(screen, YELLOW, (x + enemy_width // 3, y + enemy_height // 3), eye_radius)
    pygame.draw.circle(screen, YELLOW, (x + 2 * enemy_width // 3, y + enemy_height // 3), eye_radius)

def fire_bullet(x, y):
    global bullet_state, bullet_x, bullet_y
    bullet_state = "fire"
    bullet_x = x + player_width // 2 - bullet_width // 2
    bullet_y = y

def is_collision(ex, ey, bx, by, threshold=25):
    distance = math.sqrt((ex - bx) ** 2 + (ey - by) ** 2)
    return distance < threshold

def draw_ui():
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (WIDTH - 130, 10))

def reset_game():
    global enemies, score, lives, game_over, bullet_state
    enemies = []
    for i in range(num_enemies):
        x = random.randint(50, WIDTH - 50 - enemy_width)
        y = random.randint(40, 150)
        enemies.append([x, y])
    score = 0
    lives = 3
    game_over = False
    bullet_state = "ready"

running = True
while running:
    clock.tick(FPS)
    screen.fill(DARK_BLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if not game_over:
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        fire_bullet(player_x, player_y)
            else:
                if event.key == pygame.K_RETURN:
                    reset_game()
    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x += player_speed
        player_x = max(0, min(WIDTH - player_width, player_x))
        for i, enemy in enumerate(enemies):
            ex, ey = enemy
            ex += enemy_speed_x
            if ex <= 0 or ex >= WIDTH - enemy_width:
                enemy_speed_x *= -1
                for j in range(len(enemies)):
                    enemies[j][1] += enemy_speed_y
            if ey > player_y - 20:
                lives -= 1
                ex = random.randint(50, WIDTH - 50 - enemy_width)
                ey = random.randint(40, 150)
                if lives <= 0:
                    game_over = True

            enemies[i] = [ex, ey]
        if bullet_state == "fire":
            bullet_y -= bullet_speed
            pygame.draw.rect(screen, WHITE, (bullet_x, bullet_y, bullet_width, bullet_height))
            if bullet_y < 0:
                bullet_state = "ready"
        for i, enemy in enumerate(enemies):
            ex, ey = enemy
            if bullet_state == "fire":
                if is_collision(ex + enemy_width // 2, ey + enemy_height // 2,
                                bullet_x + bullet_width // 2, bullet_y):
                    bullet_state = "ready"
                    score += 10
                    ex = random.randint(50, WIDTH - 50 - enemy_width)
                    ey = random.randint(40, 150)
                    enemies[i] = [ex, ey]
        draw_player(player_x, player_y)
        for ex, ey in enemies:
            draw_enemy(ex, ey)
        draw_ui()
    else:
        game_over_text = big_font.render("GAME OVER", True, WHITE)
        info_text = font.render("Press ENTER to play again, ESC to quit", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2,
                                     HEIGHT // 2 - 60))
        screen.blit(info_text, (WIDTH // 2 - info_text.get_width() // 2,
                                HEIGHT // 2 + 10))
        draw_ui()
    pygame.display.flip()
pygame.quit()
sys.exit()
