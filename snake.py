'''
Authors: Kunal Dani, Shyanne Salen, Marina Morrow
Last Modified: April 29th, 2019
Snake Project w/ Different Game Modes
Software Carpentry
Snake Code

This file is the main file for our Snake game. This file contains of 
the function that helps facilitate the initialization of Snake 
gameplay. The classic game consist of a snake the user manipulates
using the arrow keys. The goal of the game is for the snake eat as 
many apples as possibly without hitting the walls or eating itself. 
As the snake continues to eat the apples, it grows by one unit. Our 
snake game consists of three other modes. For all game modes, the 
snake is still manuvered using the arrow keys to try to eat the apples.
In all game modes, if the snake hits a wall or itself, then the game 
is over.

The other game modes include:
1.) Color Changing Mode - Snake, apple and grid change colors randomly 
after the snake eats an apple.
2.) Rotten Apple Mode - The snake must avoid eating the rotten apples 
while continuing to try to eat normal apples.
3.) Random Snake Mode - Snake must avoid eating the random snakes that 
appear and move randomly around the screen.

This code relies on the classic_snake.py file to function.

**Files**
    tile_screens.py
        This file contains the code for the title screen, mode screen,
        and game over screen.
    snake_game_modes.py
        This file contains the code that runs the classic game mode
        of snake in the move_snake function. It also contains the
        code for the three other game modes. The classic_snake.py
        file is referenced by this file.
    classic_snake.py
        This file contains the code for the classic game of snake. It
        includes the snake and apple classes. It also contains the code 
        that places a snake and an apple on the screen. Additionally, 
        the get_key_pressed function determines how the snake moves 
        based on the key input. The show score function keeps track of 
        the number of apples eaten and displays it on the screen.

***Functions***
    play_game
        This function combines the functions from the files above to
        play the game snake with the tile, mode, and game over screens
        and all four game modes.
'''
from pygame.locals import *
import pygame, sys
import random
from title_screens import title_screen, mode_screen, game_over_screen
from snake_game_modes import move_snake

def play_game(game_width = 500, game_height = 500, FPS = 10, block_size = 20):
    '''
    This function initializes pygame and runs the game snake with all
    the title, mode, and game over screens. This game allows you to
    run 4 different modes of the snake game.

    **Parameters**
        game_width: *int*
            This integer corresponds to the width of the screen the 
            game.
        game_height: *int*
            This integer corresponds to the height of the screen the 
            game. These must be divisible by block_size.
        FPS: *int*
            This integer represents to the frames per seconds or the 
            speed at which the game is played. These must be
            divisible by block_size
        block_size: *int*
            This integer represents the size of the blocks used to 
            create all snake and apple objects present during gameplay.

    **Returns**
        play_again: *boolean*
            This determines the the user has pressed any key except
            escape during the game over screen to continue to play the
            game another time.
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
    score = move_snake(DISPLAYSURF, block_size, fpsClock, FPS, game_width, \
     nblocks_width, nblocks_height, game_mode)
    play_again = game_over_screen(DISPLAYSURF, game_width, score)
    return play_again

if __name__ == '__main__':
    play_again = play_game()
    while play_again:
        play_game()
