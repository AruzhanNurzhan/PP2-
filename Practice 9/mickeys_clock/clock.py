import pygame
import datetime
import os


class Clock:

    def __init__(self):

        BASE_DIR = os.path.dirname(__file__)
        IMG_DIR = os.path.join(BASE_DIR, "images")

        self.clock_img = pygame.image.load(os.path.join(IMG_DIR, "clock.png"))

        self.minute_hand = pygame.image.load(os.path.join(IMG_DIR, "rightarm.png"))
        self.second_hand = pygame.image.load(os.path.join(IMG_DIR, "leftarm.png"))

        self.base_fix = -90

    def get_time_angles(self):

        now = datetime.datetime.now()

        minutes = now.minute
        seconds = now.second

        minute_angle = -6 * minutes
        second_angle = -6 * seconds

        return minute_angle, second_angle

    def draw(self, screen):

        center = screen.get_rect().center

        clock_rect = self.clock_img.get_rect(center=center)
        screen.blit(self.clock_img, clock_rect)

        minute_angle, second_angle = self.get_time_angles()

        minute_img = pygame.transform.rotate(
            self.minute_hand,
            minute_angle + self.base_fix
        )

        second_img = pygame.transform.rotate(
            self.second_hand,
            second_angle + self.base_fix
        )

        minute_rect = minute_img.get_rect(center=center)
        second_rect = second_img.get_rect(center=center)

        screen.blit(minute_img, minute_rect)
        screen.blit(second_img, second_rect)