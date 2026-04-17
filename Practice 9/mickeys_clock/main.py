import pygame
import sys
from clock import Clock

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

my_clock = Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    my_clock.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()