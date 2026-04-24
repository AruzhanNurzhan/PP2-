import pygame
import os

pygame.init()

WIDTH = 1200
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()
FPS = 60

BASE_DIR = os.path.dirname(__file__)

def load_image(name):
    return pygame.image.load(os.path.join(BASE_DIR, "images", name))

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

image_rectangle = load_image("rectangle.png")
image_circle = load_image("circle.png")

rect_icon = image_rectangle.get_rect(topleft=(10, 10))
circle_icon = image_circle.get_rect(topleft=(60, 10))

colors = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
]

palette = []
for i, color in enumerate(colors):
    r = pygame.Rect(10 + i * 40, 60, 30, 30)
    palette.append((r, color))

color = (0, 0, 0)
brush_size = 5

tool = "brush"
drawing = False
start_pos = None
prev_pos = None

running = True

while running:
    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            if rect_icon.collidepoint(pos):
                tool = "rect"
            elif circle_icon.collidepoint(pos):
                tool = "circle"
            else:
                for r, c in palette:
                    if r.collidepoint(pos):
                        color = c

                if tool in ["rect", "circle"]:
                    start_pos = pos
                    drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = event.pos

                x1, y1 = start_pos
                x2, y2 = end_pos

                w = abs(x2 - x1)
                h = abs(y2 - y1)

                top_left = (min(x1, x2), min(y1, y2))

                if tool == "rect":
                    pygame.draw.rect(canvas, color, (*top_left, w, h), 2)

                if tool == "circle":
                    radius = max(w, h) // 2
                    center = (x1 + (x2 - x1)//2, y1 + (y2 - y1)//2)
                    pygame.draw.circle(canvas, color, center, radius, 2)

            drawing = False
            start_pos = None
            prev_pos = None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                tool = "brush"
            if event.key == pygame.K_e:
                tool = "eraser"

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()

        if tool in ["brush", "eraser"]:
            draw_color = (255, 255, 255) if tool == "eraser" else color

            if prev_pos:
                pygame.draw.line(canvas, draw_color, prev_pos, pos, brush_size * 2)

            prev_pos = pos
    else:
        prev_pos = None

    screen.blit(canvas, (0, 0))

    screen.blit(image_rectangle, rect_icon)
    screen.blit(image_circle, circle_icon)

    for r, c in palette:
        pygame.draw.rect(screen, c, r)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()