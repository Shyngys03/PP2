import pygame, random
from time import sleep

pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("Road.png")
pygame.display.set_caption("Car Game")
font = pygame.font.SysFont("Times new roman", 40)
screen_end = font.render("Game Over", True, (0, 0, 0))

pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)

done = False

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

player_x = 380
player_y = 490

enemy_x = random.randint(240, 510)
enemy_y = 0

coin_x = random.randint(240, 510)
coin_y = 0
coin_size = 50

playerImage = pygame.image.load("Player.png")
enemyImage = pygame.image.load("Enemy.png")
coinImage = pygame.image.load("coin.png")
black = pygame.image.load("blackback.png")

def show_player(x, y):
    screen.blit(playerImage, (x, y))

def show_enemy(x, y):
    screen.blit(enemyImage, (x, y))

def show_coin(x, y):
    screen.blit(coinImage, (x, y))

def Crash(enemyX, enemyY, playerX, playerY):
    if enemyX - playerX <= 48 and playerX - enemyX <= 48:
        if enemyY - playerY <= 96 and playerY - enemyY <= 93:
            return True
    return False

def collect_coin(player_x, player_y, coin_x, coin_y):
    if player_x - coin_x <= 50 and coin_x - player_x <= 44:
        if player_y - coin_y <= 50 and coin_y - player_y <= 96:
            return True
    return False

coins = 0
def show_score(x, y):
    screen.blit(black, (x, y))
    s = font.render("Coins: " + str(coins), True, (255, 255, 0))
    screen.blit(s, (x, y))

sleep(0.5)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    enemy_dy = random.randint(1, 2)
    coin_dy = random.randint(1, 2)
    score_end = font.render("Score: " + str(coins), True, (0, 0, 0))

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        player_x -= 1
    
    if pressed[pygame.K_RIGHT]:
        player_x += 1

    if player_x < 240:
        player_x = 240
    if player_x > 515:
        player_x = 515

    enemy_y += enemy_dy
    coin_y += coin_dy

    if coin_y >= 600:
        coin_x = random.randint(240, 510)
        coin_y = random.randint(5, 10)

    if enemy_y >= 600:
        enemy_x = random.randint(240, 510)
        enemy_y = random.randint(5, 10)

    if collect_coin(player_x, player_y, coin_x, coin_y):
        coins += 1
        coin_x = random.randint(240, 510)
        coin_y = random.randint(5, 10)
        pygame.display.update()

    screen.blit(background, (200, 0))

    if enemy_x - coin_x <= 50 and coin_x - enemy_x <= 48:
        if enemy_y - coin_y <= 50 and coin_y - enemy_y <= 93:
            show_enemy(enemy_x, enemy_y)
        else:
            show_enemy(enemy_x, enemy_y)
            show_coin(coin_x, coin_y)
    else:
        show_enemy(enemy_x, enemy_y)
        show_coin(coin_x, coin_y)

    if Crash(enemy_x, enemy_y, player_x, player_y):
        pygame.mixer.music.load("crash.wav")
        pygame.mixer.music.play(-1)
        screen.fill(red)
        screen.blit(screen_end, (325, 275))
        screen.blit(score_end, (600, 60))
        pygame.display.update()
        sleep(4)
        pygame.quit()

    show_player(player_x, player_y)
    show_score(600, 60)

    pygame.display.update()