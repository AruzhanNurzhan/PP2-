import pygame
import os
import math

pygame.init()

# SCREEN SETTINGS
WIDTH = 1200
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()
FPS = 60

BASE_DIR = os.path.dirname(__file__)

# LOAD IMAGE FUNCTION
def load_image(name):
    return pygame.image.load(os.path.join(BASE_DIR, "images", name))

# CANVAS
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

# TOOL ICONS (OLD)
image_rectangle = load_image("rectangle.png")
image_circle = load_image("circle.png")

rect_icon = image_rectangle.get_rect(topleft=(10, 10))
circle_icon = image_circle.get_rect(topleft=(60, 10))

# TOOL ICONS (NEW SHAPES)
image_square = load_image("square.png")
image_right_triangle = load_image("triangle.png")
image_equilateral_triangle = load_image("eq_triangle.png")
image_rhombus = load_image("rhombus.png")

square_icon = image_square.get_rect(topleft=(110, 10))
right_triangle_icon = image_right_triangle.get_rect(topleft=(160, 10))
equilateral_triangle_icon = image_equilateral_triangle.get_rect(topleft=(210, 10))
rhombus_icon = image_rhombus.get_rect(topleft=(260, 10))

# COLORS
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

# SHAPES DRAW FUNCTIONS

def draw_square(surf, color, start, end):
    x1, y1 = start
    x2, y2 = end
    size = max(abs(x2-x1), abs(y2-y1))
    rect = pygame.Rect(min(x1,x2), min(y1,y2), size, size)
    pygame.draw.rect(surf, color, rect, 2)

def draw_right_triangle(surf, color, start, end):
    x1, y1 = start
    x2, y2 = end
    pygame.draw.polygon(surf, color, [(x1,y2),(x1,y1),(x2,y2)], 2)

def draw_equilateral_triangle(surf, color, start, end):
    x1, y1 = start
    x2, y2 = end
    base = abs(x2-x1)
    h = int(base * math.sqrt(3)/2)
    pygame.draw.polygon(surf, color, [(x1,y2),(x2,y2),((x1+x2)//2,y2-h)], 2)

def draw_rhombus(surf, color, start, end):
    x1,y1 = start
    x2,y2 = end
    cx = (x1+x2)//2
    cy = (y1+y2)//2
    pygame.draw.polygon(surf, color, [(cx,y1),(x2,cy),(cx,y2),(x1,cy)], 2)

# MAIN LOOP
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # MOUSE DOWN
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            # TOOL SELECTION (OLD + NEW)
            if rect_icon.collidepoint(pos):
                tool = "rect"
            elif circle_icon.collidepoint(pos):
                tool = "circle"
            elif square_icon.collidepoint(pos):
                tool = "square"
            elif right_triangle_icon.collidepoint(pos):
                tool = "right_triangle"
            elif equilateral_triangle_icon.collidepoint(pos):
                tool = "equilateral_triangle"
            elif rhombus_icon.collidepoint(pos):
                tool = "rhombus"
            else:
                for r, c in palette:
                    if r.collidepoint(pos):
                        color = c

                if tool in ["rect","circle","square","right_triangle","equilateral_triangle","rhombus"]:
                    start_pos = pos
                    drawing = True

        # MOUSE UP DRAW SHAPE
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = event.pos

                if tool == "square":
                    draw_square(canvas, color, start_pos, end_pos)

                elif tool == "right_triangle":
                    draw_right_triangle(canvas, color, start_pos, end_pos)

                elif tool == "equilateral_triangle":
                    draw_equilateral_triangle(canvas, color, start_pos, end_pos)

                elif tool == "rhombus":
                    draw_rhombus(canvas, color, start_pos, end_pos)

                elif tool == "rect":
                    x1,y1 = start_pos
                    x2,y2 = end_pos
                    pygame.draw.rect(canvas, color, (*((min(x1,x2),min(y1,y2))),abs(x2-x1),abs(y2-y1)),2)

                elif tool == "circle":
                    x1,y1 = start_pos
                    x2,y2 = end_pos
                    r = max(abs(x2-x1),abs(y2-y1))//2
                    c = (x1+(x2-x1)//2,y1+(y2-y1)//2)
                    pygame.draw.circle(canvas, color, c, r,2)

            drawing = False
            start_pos = None
            prev_pos = None

        # KEYBOARD
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                tool = "brush"
            if event.key == pygame.K_e:
                tool = "eraser"

    # BRUSH
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        if tool in ["brush","eraser"]:
            draw_color = (255,255,255) if tool=="eraser" else color
            if prev_pos:
                pygame.draw.line(canvas, draw_color, prev_pos, pos, brush_size*2)
            prev_pos = pos
    else:
        prev_pos = None

    # DRAW
    screen.blit(canvas,(0,0))

    # OLD ICONS
    screen.blit(image_rectangle, rect_icon)
    screen.blit(image_circle, circle_icon)

    # NEW ICONS
    screen.blit(image_square, square_icon)
    screen.blit(image_right_triangle, right_triangle_icon)
    screen.blit(image_equilateral_triangle, equilateral_triangle_icon)
    screen.blit(image_rhombus, rhombus_icon)

    # PALETTE
    for r,c in palette:
        pygame.draw.rect(screen,c,r)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()