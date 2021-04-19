import pygame
import time

pygame.init()

FPS = 60

done = False

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Draw Tool')
font = pygame.font.SysFont('Times new roman', 23)
clock = pygame.time.Clock()
screen.fill((255, 255, 255))

button_save = font.render('Press S to save image', True, (0, 0, 0))
Eraser = font.render('E', True, (128, 128, 255))
Rectangle = font.render('R', True, (128, 128, 255))
Circle = font.render('C', True, (128, 128, 255))
choose_pencil = font.render('Q', True, (128, 128, 255))

BLACK = pygame.image.load('BLACK.png')
RED = pygame.image.load('RED.png')
GREEN = pygame.image.load('GREEN.png')
BLUE = pygame.image.load('BLUE.png')

colorsImage = [BLACK, RED, GREEN, BLUE]
colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)]

pencilImage = pygame.image.load('pencil.png')
eraserImage = pygame.image.load('eraser.png')
rectImage = pygame.image.load('rectangle.png')
circleImage = pygame.image.load('circle.png')

width = 2
color = (0, 0, 0)
radius = 5
drawing = False
last_pos = None
pencil = False

def show_menu():
    for i in range(len(colors)):
        screen.blit(colorsImage[i], (750 - 50 * i, 0))

    screen.blit(eraserImage, (0, 0))
    screen.blit(Eraser, (20, 50))
    screen.blit(Rectangle, (75, 50))
    screen.blit(Circle, (130, 50))
    screen.blit(choose_pencil, (180, 50))
    screen.blit(rectImage, (55, 0))
    screen.blit(circleImage, (110, 0))
    screen.blit(pencilImage, (170, 0))
    screen.blit(button_save, (280, 0))

    cnt = 1
    
    for i in range(4):
        cnt_color = font.render(str(cnt), True, (255, 255, 255))
        screen.blit(cnt_color, (615 + 50 * i, 10))
        cnt += 1
    

def draw(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)
    
rect = False
start_rect = None
end_rect = None
def draw_rectangle(screen, start, end, color):
    x1 = start[0]
    y1 = start[1]

    x2 = end[0]
    y2 = end[1]

    top = (min(x1, x2), min(y1, y2))

    width_rect = abs(max(x1, x2) - top[0])
    height_rect = abs(max(y1, y2) - top[1])

    pygame.draw.rect(screen, color, pygame.Rect(min(x1, x2), min(y1, y2), width_rect, height_rect))


is_circle = False
start_circle = None
end_circle = None
def draw_circle(screen, start, end, color):
    x1 = start[0]
    y1 = start[1]

    x2 = end[0]
    y2 = end[1]

    top = (min(x1, x2), min(y1, y2))

    radius_circle = abs(max(x1, x2) - top[0])
    center = (int((x1 + x2) / 2), int((y1 + y2) / 2))

    pygame.draw.circle(screen, color, center, radius_circle)

while not done:
    clock.tick(FPS)
    
    last_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.image.save(screen, 'image.png')
            if event.key == pygame.K_q and not pencil:
                pencil = True
                drawing = True
                rect = False
                is_circle = False
            
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_1:
                color = (0, 0, 255)
            if event.key == pygame.K_2:
                color = (0, 255, 0)
            if event.key == pygame.K_3:
                color = (255, 0, 0)
            if event.key == pygame.K_4:
                color = (0, 0, 0)
            if event.key == pygame.K_e:
                color = (255, 255, 255)
            if event.key == pygame.K_r:
                rect = True
                is_circle = False
                pencil = False
            if event.key == pygame.K_c:
                is_circle = True
                rect = False
                pencil = False
        if event.type == pygame.MOUSEBUTTONDOWN and not rect and not is_circle:
            pygame.draw.circle(screen, color, event.pos, radius)
            drawing = True
            pencil = True
        if event.type == pygame.MOUSEBUTTONDOWN and rect:
            start_rect = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP and rect:
            end_rect = pygame.mouse.get_pos()
            draw_rectangle(screen, start_rect, end_rect, color)
        if event.type == pygame.MOUSEBUTTONDOWN and is_circle:
            start_circle = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP and is_circle:
            end_circle = pygame.mouse.get_pos()
            draw_circle(screen, start_circle, end_circle, color)
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        if event.type == pygame.MOUSEMOTION:
            if drawing and pencil:
                draw(screen, last_pos, event.pos, radius, color)
                last_pos = event.pos

    show_menu()

    pygame.display.flip()

pygame.quit()