import pygame
import time
import random

pygame.init()

snake_speed = 15

window_x = 720
window_y = 480

block_size = 10

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

pygame.display.set_caption("Snake Game")
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

snake_position = [100, 50]

snake_body = [
    [100, 50],
    [90, 50],
    [80, 50]
]

fruit_position = [
    random.randrange(1, (window_x // block_size)) * block_size,
    random.randrange(1, (window_y // block_size)) * block_size
]

fruit_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0
level = 1
food_counter = 0


def show_score():
    font = pygame.font.SysFont("times new roman", 20)

    score_surface = font.render("Score: " + str(score), True, white)
    level_surface = font.render("Level: " + str(level), True, white)

    game_window.blit(score_surface, (10, 10))
    game_window.blit(level_surface, (window_x - 100, 10))


def game_over():
    font = pygame.font.SysFont("times new roman", 50)

    text = font.render("GAME OVER", True, red)
    rect = text.get_rect()
    rect.center = (window_x // 2, window_y // 3)

    game_window.fill(black)
    game_window.blit(text, rect)

    pygame.display.flip()
    time.sleep(2)

    pygame.quit()
    quit()


def generate_food():
    while True:
        x = random.randrange(1, (window_x // block_size)) * block_size
        y = random.randrange(1, (window_y // block_size)) * block_size

        if [x, y] not in snake_body:
            return [x, y]


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

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] -= block_size
    if direction == 'DOWN':
        snake_position[1] += block_size
    if direction == 'LEFT':
        snake_position[0] -= block_size
    if direction == 'RIGHT':
        snake_position[0] += block_size

    snake_body.insert(0, list(snake_position))

    if snake_position == fruit_position:
        score += 10
        food_counter += 1
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = generate_food()
        fruit_spawn = True

    if food_counter >= 3:
        level += 1
        snake_speed += 2
        food_counter = 0

    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(
            game_window,
            green,
            pygame.Rect(pos[0], pos[1], block_size, block_size)
        )

    pygame.draw.rect(
        game_window,
        white,
        pygame.Rect(fruit_position[0], fruit_position[1], block_size, block_size)
    )

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