import sys
import pygame

from grid import Grid
from setting import Setting
from blocks import *
from game import Game

pygame.init()
screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("My little tertis game")

clock = pygame.time.Clock()

game = Game()
setting = Setting()

running = True

while running:    #check game event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            elif event.key == pygame.K_RIGHT:
                game.move_right()
            elif event.key == pygame.K_DOWN:
                game.move_down()
            elif event.key == pygame.K_SPACE:
                game.rotate()

    #drawing the screen
    screen.fill(setting.bg_color)
    game.draw(screen)
    pygame.display.update()
    clock.tick(60)
        