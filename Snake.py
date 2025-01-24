import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game settings
SNAKE_BLOCK = 20
SNAKE_SPEED = 10  

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def your_score(score):
    """Display the current score."""
    value = score_font.render(f"Your Score: {score}", True, GREEN)
    screen.blit(value, [10, 10])


def draw_snake(snake_block, snake_list):
    """Draw the snake with a rounded head."""
    for i, block in enumerate(snake_list):
        if i == len(snake_list) - 1:  # Snake head
            pygame.draw.ellipse(screen, BLUE, [block[0], block[1], snake_block, snake_block])
        else:  # Snake body
            pygame.draw.rect(screen, BLUE, [block[0], block[1], snake_block, snake_block])


def message(msg, color):
    """Display a message on the screen."""
    msg_surface = font_style.render(msg, True, color)
    screen.blit(msg_surface, [WIDTH // 6, HEIGHT // 3])


def game_loop():
    """Main game loop."""
    game_over = False
    game_close = False

    # Initial position of the snake
    x1, y1 = WIDTH // 2, HEIGHT // 2

    # Change in position
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Food position
    food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 20.0) * 20.0
    food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("Game Over! Press C to Play Again or Q to Quit", RED)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        # Wrap-around behavior
        x1 = (x1 + x1_change) % WIDTH
        y1 = (y1 + y1_change) % HEIGHT

        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 20.0) * 20.0
            food_y = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()



game_loop()
