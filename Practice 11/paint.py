import pygame
import os
import math

pygame.init()

# ================= SCREEN =================
WIDTH = 1200
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()
FPS = 60

# ================= LOAD IMAGES =================
BASE_DIR = os.path.dirname(__file__)

def load_image(name):
    return pygame.image.load(os.path.join(BASE_DIR, "images", name))

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

image_rectangle = load_image("rectangle.png")
image_circle = load_image("circle.png")

rect_icon = image_rectangle.get_rect(topleft=(10, 10))
circle_icon = image_circle.get_rect(topleft=(60, 10))

# ================= COLORS =================
colors = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
]

palette = []
for i, col in enumerate(colors):
    r = pygame.Rect(10 + i * 40, 60, 30, 30)
    palette.append((r, col))

color = (0, 0, 0)
brush_size = 5

# ================= TOOL STATE =================
tool = "brush"
drawing = False
start_pos = None
prev_pos = None

# ================= SHAPES =================
def draw_square(surf, color, start, end):
    x1, y1 = start
    x2, y2 = end
    size = min(abs(x2 - x1), abs(y2 - y1))
    rect = pygame.Rect(min(x1, x2), min(y1, y2), size, size)
    pygame.draw.rect(surf, color, rect, 2)


def draw_right_triangle(surf, color, start, end):
    x1, y1 = start
    x2, y2 = end
    pygame.draw.polygon(surf, color, [(x1, y2), (x1, y1), (x2, y2)], 2)


def draw_equilateral_triangle(surf, color, start, end):
    x1, y1 = start
    x2, y2 = end

    size = abs(x2 - x1)
    h = (math.sqrt(3) / 2) * size

    points = [
        (x1, y2),
        (x1 + size // 2, y2 - h),
        (x2, y2)
    ]

    pygame.draw.polygon(surf, color, points, 2)


def draw_rhombus(surf, color, start, end):
    x1, y1 = start
    x2, y2 = end

    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2

    points = [
        (cx, y1),
        (x2, cy),
        (cx, y2),
        (x1, cy)
    ]

    pygame.draw.polygon(surf, color, points, 2)

# ================= MAIN LOOP =================
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # ================= KEYBOARD =================
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_b:
                tool = "brush"

            if event.key == pygame.K_e:
                tool = "eraser"

            if event.key == pygame.K_1:
                tool = "square"

            if event.key == pygame.K_2:
                tool = "right_triangle"

            if event.key == pygame.K_3:
                tool = "equilateral_triangle"

            if event.key == pygame.K_4:
                tool = "rhombus"

        # ================= MOUSE DOWN =================
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            # TOOL SELECTION (OLD ICONS)
            if rect_icon.collidepoint(pos):
                tool = "rect"
            elif circle_icon.collidepoint(pos):
                tool = "circle"

            # COLOR SELECTION
            for r, c in palette:
                if r.collidepoint(pos):
                    color = c

            start_pos = pos
            drawing = True

        # ================= MOUSE UP =================
        if event.type == pygame.MOUSEBUTTONUP and drawing:
            end_pos = event.pos

            x1, y1 = start_pos
            x2, y2 = end_pos

            w = abs(x2 - x1)
            h = abs(y2 - y1)

            top_left = (min(x1, x2), min(y1, y2))

            # OLD SHAPES
            if tool == "rect":
                pygame.draw.rect(canvas, color, (*top_left, w, h), 2)

            elif tool == "circle":
                radius = max(w, h) // 2
                center = (x1 + w // 2, y1 + h // 2)
                pygame.draw.circle(canvas, color, center, radius, 2)

            # NEW SHAPES
            elif tool == "square":
                draw_square(canvas, color, start_pos, end_pos)

            elif tool == "right_triangle":
                draw_right_triangle(canvas, color, start_pos, end_pos)

            elif tool == "equilateral_triangle":
                draw_equilateral_triangle(canvas, color, start_pos, end_pos)

            elif tool == "rhombus":
                draw_rhombus(canvas, color, start_pos, end_pos)

            drawing = False
            start_pos = None
            prev_pos = None

    # ================= BRUSH / ERASER =================
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()

        if tool in ["brush", "eraser"]:
            draw_color = (255, 255, 255) if tool == "eraser" else color

            if prev_pos:
                pygame.draw.line(canvas, draw_color, prev_pos, pos, brush_size * 2)

            prev_pos = pos
    else:
        prev_pos = None

    # ================= DRAW =================
    screen.blit(canvas, (0, 0))

    # ICONS
    screen.blit(image_rectangle, rect_icon)
    screen.blit(image_circle, circle_icon)

    # PALETTE
    for r, c in palette:
        pygame.draw.rect(screen, c, r)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()