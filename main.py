import sys
import pygame

from grid import Grid
from blocks import *

pygame.init()
screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("My little tertis game")

dark_blue = (44,44,127)

game_grid = Grid()
block = LBlock()
game_grid.print_grid()

clock = pygame.time.Clock()
running = True

while running:    #check game event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #drawing the screen
    screen.fill(dark_blue)
    game_grid.draw(screen)
    block.draw(screen)
    pygame.display.update()
    clock.tick(60)
        