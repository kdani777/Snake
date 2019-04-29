from pygame.locals import *
import pygame, sys
import random
from title_screens import title_screen, mode_screen, game_over_screen
from snake_game_modes import move_snake

class test_snake(object):
	def game_over_UT(self, hit_rotten_apple, hit_random_snake, snake, nblocks):
		hit_rotten_apple, hit_random_snake, snake = game_over #not sure this is right but we had it in our last unit test
		assert hit_rotten_apple == True, 'Did not actually hit apple'
		assert hit_random_snake == True, 'Did not actually hit snake'
		assert snake.x[0] == nblocks_width or snake.y[0] == nblocks_height, 'did not actually hit wall'

	def hit_apple_UT(self, rotten_apples):
		for i in range(random_number_rotten):
        	if (snake.x[0], snake.y[0]) == (rotten_apples[i].x, rotten_apples[i].y):
            	assert hit_rotten_apple == True, 'Did not actually hit apple'

    def size_UT(nblocks, apple):
    	assert nblocks_height % apple.y == 0, 'size not loaded correctly'
    	assert nblocks_width % apple.x == 0, 'size not loaded correctly'
