import pygame
import random
pygame.init()
WIDTH, HEIGHT = 800, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dinochrome")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
dino = pygame.Rect(50, 300, 50, 50)
gravity = 0.5
jump_speed = -10
dino_speed_y = 0

obstacles = []
obstacle_timer = 0
def handle_jumping():
    global dino_speed_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and dino.y == 300:
        dino_speed_y = jump_speed

    dino_speed_y += gravity
    dino.y += dino_speed_y
    if dino.y >= 300:
        dino.y = 300
        dino_speed_y = 0

def create_obstacle():
    x_pos = WIDTH
    y_pos = 300
    width = 20
    height = 50
    obstacle = pygame.Rect(x_pos, y_pos, width, height)
    obstacles.append(obstacle)

def move_obstacles():
    for obstacle in obstacles:
        obstacle.x -= 5
    if obstacles and obstacles[0].x < -20:
        obstacles.pop(0)

def check_collision():
    for obstacle in obstacles:
        if dino.colliderect(obstacle):
            return True
    return False

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    handle_jumping()
    obstacle_timer += 1
    if obstacle_timer > 50:
        create_obstacle()
        obstacle_timer = 0

    move_obstacles()

    if check_collision():
        run = False

    win.fill(WHITE)
    pygame.draw.rect(win, BLACK, dino)
    for obstacle in obstacles:
        pygame.draw.rect(win, RED, obstacle)  

    pygame.display.update()

pygame.quit()
