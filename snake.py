'''
Authors: Kunal Dani, Shyanne Salen, Marina Morrow
Last Modified: April 18th, 2019


Ideas for interesting twists - Levels game, color-changing, shrinking
screen, new blocks come up to avoid.
'''
from pygame.locals import *
import pygame, sys
import random
from title_screens import title_screen, mode_screen, game_over_screen
from snake_game_modes import move_snake

def play_game(game_width = 500, game_height = 500, FPS = 7, block_size = 20):
    pygame.init()
    nblocks_width = int(game_width/block_size)
    nblocks_height = int(game_height/block_size)
    DISPLAYSURF = pygame.display.set_mode((game_width, game_height))
    pygame.display.set_caption('Snake')
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((game_width, game_height))
    title_screen(DISPLAYSURF, game_width, game_height)
    game_mode = mode_screen(DISPLAYSURF, game_width, game_height)
    print game_mode
    move_snake(DISPLAYSURF, block_size, fpsClock, FPS, game_width, game_height, nblocks_width, nblocks_height, game_mode)
    play_again = game_over_screen(DISPLAYSURF, block_size, fpsClock, FPS, game_height, game_width, nblocks_width, nblocks_height)
    print "game_over"
    return play_again

if __name__ == '__main__':
    play_again = play_game()
    while play_again:
        play_game()