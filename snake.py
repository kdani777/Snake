'''
Authors: Kunal Dani, Shyanne Salen, Marina Morrow
Last Modified: April 29th, 2019
Snake Project w/ Different Game Modes
Software Carpentry
Snake Code

This code consists of the function that helps facilitate the initialization of Snake gameplay.
The classic game consist of a snake the user can manipulate using the arrow keys.
The goal of the game is for the snake eat as many apples as possibly without hitting 
the walls or eating itself. As the snake continues to eat the apples, it grows by one unit.

Other game modes include:
1.) Color Changing Mode - Snake, apple and grid changing colors after the snake eats an apple
2.) Rotton Apple Mode - The snake must avoid eating the rotton apples while continuing tryin to eat normal apples.
3.) Random Snake Mode - Snake must avoid eating the random snakes that appear after eating each apples
'''
from pygame.locals import *
import pygame, sys
import random
from title_screens import title_screen, mode_screen, game_over_screen
from snake_game_modes import move_snake

def play_game(game_width = 500, game_height = 500, FPS = 10, block_size = 20):
    '''
    This function initializes pygame and runs the game snake

    **Parameters**
        game_width: *int*
            This integer corresponds to the width of the screen the game is played on
        game_height: *int*
            This integer corresponds to the height of the screen the game is played on
        FPS: *int*
            This integer represents to the frames per seconds or the speed at which
            the game is played
        block_size: *int*
            This integer represents the size of the blocks used to initially create all snake
            and apple objects present during gameplay
    '''
    pygame.init()
    nblocks_width = int(game_width/block_size)
    nblocks_height = int(game_height/block_size)
    DISPLAYSURF = pygame.display.set_mode((game_width, game_height))
    pygame.display.set_caption('Snake')
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((game_width, game_height))
    title_screen(DISPLAYSURF, game_width)
    game_mode = mode_screen(DISPLAYSURF, game_width)
    score = move_snake(DISPLAYSURF, block_size, fpsClock, FPS, game_width, nblocks_width, nblocks_height, game_mode)
    play_again = game_over_screen(DISPLAYSURF, game_width, score)
    return play_again

if __name__ == '__main__':
    play_again = play_game()
    while play_again:
        play_game()