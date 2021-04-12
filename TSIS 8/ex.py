import pygame
import random
from time import sleep

pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("Road.png")
pygame.display.set_caption("Car Game")
font = pygame.font.SysFont("Times new roman", 60)
screen_end = font.render("Game Over", True, (0, 0, 0))

done = False

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

player_x = 380
player_y = 490
coin = 0

enemy_x = random.randint(240, 510)
enemy_y = random.randint(5, 10)

coin_x = random.randint(240, 510)
coin_y = random.randint(5, 10)
coin_dy = random.randint(1, 5)

playerImage = pygame.image.load("Player.png")
enemyImage = pygame.image.load("Enemy.png")
coinImage = pygame.image.load("coin.png")


def show_player(x, y):
    screen.blit(playerImage, (x, y))

def show_enemy(x, y):
    screen.blit(enemyImage, (x, y))

def show_coin(x, y):
    screen.blit(coinImage, (x, y))

def Crash(enemyX, enemyY, playerX, playerY):
    if enemyX in range(playerX, playerX + 5) and enemyY in range(playerY, playerY + 5):
        return True
    return False

sleep(0.5)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    enemy_dy = random.randint(1, 3)
    coin_dy = random.randint(1, 3)

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

    screen.blit(background, (200, 0))

    show_player(player_x, player_y)
    show_enemy(enemy_x, enemy_y)
    show_coin(coin_x, coin_y)

    pygame.display.update()