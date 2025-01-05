import sys
import pygame

from grid import Grid
from setting import Setting
from blocks import *
from game import Game
from colors import Colors

pygame.init()
screen = pygame.display.set_mode((500,620))
pygame.display.set_caption("My little tertis game")

clock = pygame.time.Clock()

game = Game()
setting = Setting()

tilt_font = setting.font
score_surface = tilt_font.render("Score", True, Colors.white)
next_surface = tilt_font.render("Next", True, Colors.white) 
game_over_surface = tilt_font.render("GAME OVER", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, setting.delay)

running = True

while running:    #check game event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            elif event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            elif event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            elif event.key == pygame.K_SPACE and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    #drawing the screen
    score_value_surface = tilt_font.render(str(game.score), True, Colors.white)
    screen.fill(setting.bg_color)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))
    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, 
		centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)
    pygame.display.update()
    clock.tick(60)
        