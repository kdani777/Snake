'''
Authors: Kunal Dani, Shyanne Salen, Marina Morrow
Last Modified: April 18th, 2019

'''
from pygame.locals import *
import pygame, sys

FPS = 10
game_width = 500
game_height = 500
block_size = 20

def get_colors():
    '''
    This function assigns a value to set colors to easily be able to
    assign colors to a block.

    Colors that the grid will use:
        0 - Black
        1 - White
        2 - Gray
        3 - Light blue
        4 - red
        5 - green

    **Returns**

        color_map: *dict, int, tuple*
            A dictionary that will correlate the integer key to
            a color.
    '''
    return {
        0: (169,169,169),
        1: (255, 255, 255),
        2: (0, 0, 0),
        3: (153, 204, 255),
        4: (255, 0, 0),
        5: (0, 255, 0)
    }

 
display_surf = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Snake')

global FPSCLOCK, DISPLAYSURF

pygame.init()
DISPLAYSURF = pygame.display.set_mode((game_width, game_height))

def title_screen():
    while True:
        # print pygame.font.get_fonts()
        font = pygame.font.SysFont('gillsansultra', 50)
        font2 = pygame.font.SysFont('gillsansultra', 20)
        title = font.render('Snake', True, (255,255,255))
        subtitle = font2.render('Press any key to contine, Press escape to escape', True, (155, 155, 0))
        DISPLAYSURF.blit(title, (100,100))
        DISPLAYSURF.blit(subtitle, (0, 200))
        pygame.display.update()

        key_pressed = pygame.event.get(KEYUP)
        if len(key_pressed) > 0:
            print key_pressed
            if key_pressed[0].key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            else:
                pygame.event.get()
                return
   
title_screen()
# class Snake:
#     x = 10
#     y = 10
#     speed = 1  # Can adjust how many pixels/units the snake moves

#     # Focus is on x-axis, moving left and right
#     def move_right(self):
#         self.x = self.x + self.speed

#     def move_left(self):
#         self.x = self.x - self.speed

#     # Focus is on y-axis and movements up and down
#     def move_upwards(self):
#         self.y = self.y - self.speed

#     def move_downwards(self):
#         self.y = self.y + self.speed

# # pygame.event.pump() will keep pygame in synch with our system
# # Typically want to call this once per game loop
# pg.event.pump()
# keys = pg.key.get_pressed()

# class Game:

#     width = 800
#     height = 600
#     player = 0

#     def __init__(self):
#         self._running = True
#         self._display_surf = None
#         self._image_surf = None
#         self.player = Player()

#     def on_init(self): # Upon initializing this game...
#     	pg.init()


# if (keys[pg.K_RIGHT]):
# 	print('Right arrow pressed.')