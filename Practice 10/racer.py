import pygame
import random
import sys
import time
import os

pygame.init()
pygame.mixer.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

clock = pygame.time.Clock()
FPS = 60


BASE_DIR = os.path.dirname(__file__)

def load(path):
    return pygame.image.load(os.path.join(BASE_DIR, path))
background = load("images/AnimatedStreet.png")
player_img = load("images/Player.png")
enemy_img = load("images/Enemy.png")
coin_img = load("images/coin.png")

crash_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "sounds/crash.wav"))
pygame.mixer.music.load(os.path.join(BASE_DIR, "sounds/background.wav"))
pygame.mixer.music.play(-1)

font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 60)


PLAYER_SPEED = 5
ENEMY_SPEED = 6

coin_score = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 70)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED

        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += PLAYER_SPEED


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -100

    def move(self):
        self.rect.y += ENEMY_SPEED
        if self.rect.top > HEIGHT:
            self.reset()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-400, -50)

    def move(self):
        self.rect.y += ENEMY_SPEED
        if self.rect.top > HEIGHT:
            self.reset()


player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group(player, enemy, coin)
enemies = pygame.sprite.Group(enemy)
coins = pygame.sprite.Group(coin)


running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move()
    enemy.move()
    coin.move()

    if pygame.sprite.spritecollide(player, coins, False):
        coin_score += 1
        coin.reset()

    if pygame.sprite.spritecollide(player, enemies, False):
        crash_sound.play()

        screen.fill((255, 0, 0))

        text = big_font.render("GAME OVER", True, (0, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        screen.blit(text, text_rect)

        pygame.display.update()
        pygame.time.delay(2000)

        running = False

    screen.blit(background, (0, 0))

    for obj in all_sprites:
        screen.blit(obj.image, obj.rect)

    score_text = font.render(f"Coins: {coin_score}", True, (0, 0, 0))
    screen.blit(score_text, (WIDTH - 120, 10))

    pygame.display.update()

pygame.quit()
sys.exit()