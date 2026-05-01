import pygame
import time
import random

pygame.init()

# GAME SETTINGS
window_x = 720
window_y = 480
block_size = 10

snake_speed = 15

# COLORS
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Snake Game")

fps = pygame.time.Clock()

# SNAKE INITIAL POSITION
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# FOOD GENERATION
def generate_food():
    while True:
        x = random.randrange(1, window_x // block_size) * block_size
        y = random.randrange(1, window_y // block_size) * block_size
        if [x, y] not in snake_body:
            return [x, y]

fruit_position = generate_food()
fruit_spawn = True

# FOOD WEIGHT AND TIMER
fruit_weight = random.choice([1, 2, 3])
food_spawn_time = time.time()
FOOD_LIFETIME = 5

# GAME STATE
direction = 'RIGHT'
change_to = direction

score = 0
level = 1
food_counter = 0

# SCORE DISPLAY
def show_score():
    font = pygame.font.SysFont("times new roman", 20)
    game_window.blit(font.render(f"Score: {score}", True, white), (10, 10))
    game_window.blit(font.render(f"Level: {level}", True, white), (600, 10))

# GAME OVER SCREEN
def game_over():
    font = pygame.font.SysFont("times new roman", 50)

    game_window.fill(black)
    text = font.render("GAME OVER", True, red)

    game_window.blit(text, text.get_rect(center=(window_x//2, window_y//3)))
    pygame.display.update()

    time.sleep(2)
    pygame.quit()
    quit()

# MAIN LOOP
while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # DIRECTION LOGIC
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # MOVEMENT
    if direction == 'UP':
        snake_position[1] -= block_size
    if direction == 'DOWN':
        snake_position[1] += block_size
    if direction == 'LEFT':
        snake_position[0] -= block_size
    if direction == 'RIGHT':
        snake_position[0] += block_size

    snake_body.insert(0, list(snake_position))

    # FOOD TIMER SYSTEM
    if time.time() - food_spawn_time > FOOD_LIFETIME:
        fruit_position = generate_food()
        fruit_weight = random.choice([1, 2, 3])
        food_spawn_time = time.time()

    # FOOD EAT LOGIC
    if snake_position == fruit_position:
        score += 10 * fruit_weight
        food_counter += 1
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = generate_food()
        fruit_weight = random.choice([1, 2, 3])
        fruit_spawn = True
        food_spawn_time = time.time()

    # LEVEL SYSTEM
    if food_counter >= 3:
        level += 1
        snake_speed += 2
        food_counter = 0

    # DRAWING
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], block_size, block_size))

    pygame.draw.rect(game_window, white, pygame.Rect(*fruit_position, block_size, block_size))

    # COLLISIONS
    if snake_position[0] < 0 or snake_position[0] >= window_x:
        game_over()
    if snake_position[1] < 0 or snake_position[1] >= window_y:
        game_over()

    for block in snake_body[1:]:
        if snake_position == block:
            game_over()

    show_score()
    pygame.display.update()
    fps.tick(snake_speed)