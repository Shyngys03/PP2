import pygame
import random 
import time


pygame.init()

WIDTH = 600
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
font = pygame.font.SysFont('Times new roman', 32) 

running = True

d = 5
FPS = 30
clock = pygame.time.Clock()


class Snake:

    def __init__(self):
        self.size = 1
        self.elements = [[100, 100]]
        self.radius = 10
        self.dx = 5
        self.dy = 0
        self.score = 0
        self.is_add = False

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (255, 10, 255), element, self.radius)

    def add_to_snake(self):
        self.size += 1
        self.score += 1
        self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy


class Food:

    def __init__(self):
        self.x = random.randint(30, WIDTH - 50)
        self.y = random.randint(30, HEIGHT - 50)
        # self.radius = 10
        self.image = pygame.image.load("apple.png")
        self.pos = (random.randint(0, 468), random.randint(0, 368))
        self.food_append = True

    def draw(self):
        for i in self.pos:
            screen.blit(self.image, (self.x, self.y))


def in_walls(Snake):
    if Snake.elements[0][0] > WIDTH - 24 or Snake.elements[0][0] < 24:
        return True
    if Snake.elements[0][1] > HEIGHT - 24 or Snake.elements[0][1] < 24:
        return True
    return False


def game_over(snake1, snake2):
    screen.fill((255, 0, 0))
    res = font.render('GAME  OVER!', True, (0, 0, 255))
    res1 = font.render("1st player's score: " + str(snake1.score), True, (0, 0, 255))
    res2 = font.render("2nd player's score: " + str(snake2.score), True, (0, 0, 255))
    screen.blit(res, (175,150))
    screen.blit(res1, (150,250))
    screen.blit(res2, (150, 300))
    pygame.display.update()
    pygame.image.save(screen, 'save.png')
    time.sleep(3)
    pygame.quit()



def collision(food, Snake):
    if (food.x in range(Snake.elements[0][0] - 28, Snake.elements[0][0])) and  (food.y  in range(Snake.elements[0][1] - 28, Snake.elements[0][1])) :
        Snake.is_add = True 
        if Snake.is_add == True:
            food.x = random.randint(50, WIDTH - 50)
            food.y = random.randint(50, HEIGHT - 50)

def scores (x1,y1, x2, y2, score1, score2):
    res = font.render('1st score:  ' + str(snake1.score), True, (0, 90, 255))
    res1 = font.render('2nd score:  ' + str(snake2.score), True, (0, 90, 255))
    screen.blit(res, (x1, y1))
    screen.blit(res1, (x2, y2))

wallImage = pygame.image.load('wall.png')

def show_walls():
    for i in range(0, WIDTH, 10):
        screen.blit(wallImage, (i, 0))
        screen.blit(wallImage, (i, HEIGHT - 20))
        screen.blit(wallImage, (0, i))
        screen.blit(wallImage, (WIDTH - 24, i))


snake1 = Snake()
snake2 = Snake()
food = Food()

while running:
    mil = clock.tick(FPS)
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT:
                snake1.dx = d
                snake1.dy = 0
            if event.key == pygame.K_LEFT:
                snake1.dx = -d
                snake1.dy = 0
            if event.key == pygame.K_UP:
                snake1.dx = 0
                snake1.dy = -d
            if event.key == pygame.K_DOWN:
                snake1.dx = 0
                snake1.dy = d
            if event.key == pygame.K_d:
                snake2.dx = d
                snake2.dy = 0
            if event.key == pygame.K_a:
                snake2.dx = -d
                snake2.dy = 0
            if event.key == pygame.K_w:
                snake2.dx = 0
                snake2.dy = -d
            if event.key == pygame.K_s:
                snake2.dx = 0
                snake2.dy = d
   
    
    for i in range(1, len(snake1.elements)):
        if (snake1.elements[0][0] == snake1.elements[i][0] and snake1.elements[0][1] == snake1.elements[i][1]):
            game_over()
            running = False
    for i in range(1, len(snake2.elements)):
        if (snake2.elements[0][0] == snake2.elements[i][0] and snake2.elements[0][1] == snake2.elements[i][1]):
            game_over()
            running = False

    if in_walls(snake1) or in_walls(snake2):
        game_over(snake1, snake2)
        running = False
        
    collision(food, snake1)
    collision(food, snake2)
    snake1.move()
    snake2.move()
    snake1.draw()
    snake2.draw()
    food.draw()
    scores(25, 25,25, 50, snake1.score, snake2.score)
    show_walls()
    pygame.display.flip()
pygame.quit()