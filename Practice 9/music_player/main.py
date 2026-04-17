import pygame
import sys
import os
from player import Player

# фиксируем путь
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

pygame.init()

screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Music Player")

font = pygame.font.Font(None, 36)

songs = [
    os.path.join(BASE_DIR, "music/track1.wav"),
    os.path.join(BASE_DIR, "music/track2.wav")
]

player = Player(songs)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                player.play()

            if event.key == pygame.K_s:
                player.stop()

            if event.key == pygame.K_n:
                player.next()

            if event.key == pygame.K_b:
                player.prev()

            if event.key == pygame.K_q:
                running = False

   
    screen.fill((255, 255, 255))

    track_text = font.render("Track: " + player.get_track_name(), True, (0, 0, 0))
    screen.blit(track_text, (20, 50))

    state_text = font.render("State: " + player.state, True, (0, 0, 0))
    screen.blit(state_text, (20, 100))

    help_text = font.render("P play | S stop | N next | B back | Q quit", True, (100, 100, 100))
    screen.blit(help_text, (20, 200))

    pygame.display.flip()

pygame.quit()
sys.exit()