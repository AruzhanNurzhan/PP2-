import pygame

class Ball:
    def __init__(self, width, height):

        self.radius = 25
        self.step = 20

        # старт в центре
        self.x = width // 2
        self.y = height // 2

        self.width = width
        self.height = height

    def move(self, keys):

        # LEFT
        if keys[pygame.K_LEFT]:
            if self.x - self.radius - self.step >= 0:
                self.x -= self.step

        # RIGHT
        if keys[pygame.K_RIGHT]:
            if self.x + self.radius + self.step <= self.width:
                self.x += self.step

        # UP
        if keys[pygame.K_UP]:
            if self.y - self.radius - self.step >= 0:
                self.y -= self.step

        # DOWN
        if keys[pygame.K_DOWN]:
            if self.y + self.radius + self.step <= self.height:
                self.y += self.step

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)