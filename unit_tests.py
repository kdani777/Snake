'''
Authors: Kunal Dani, Marina Morrow, Shyanne Salen,
Last Modified: April 29th, 2019
Snake Project
Software Carpentry
Classic Snake

This file unit tests our functions in our snake game to see where the 
errors occur.

***CLASS***
	Test_Snake
		This function test our snake game.
'''

from pygame.locals import *
import pygame, sys
import random

class Test_Snake(object):
	'''
	This class contains the unit tests to test our functions.
	'''
	def get_colors_UT(self, colors):
		'''
		This function tests to see if get_colors returns a 
		dictionary.

		***Parameter***
			colors: *dict*
				Dictionary from the get colors function.
		'''
		assert (type(colors) == dict), "The colors are not a " \
		"dictionary"

	def hit_random_snake_UT(self, hit_random_snake):
		'''
		'''
		assert hit_random_snake == True, 'Did not actually hit snake'

	def hit_rotten_apple_UT(self, hit_rotten_apple):
		assert hit_rotten_apple == True, 'Did not actually hit apple'

	def hit_apple_UT(self, rotten_apples, snake, hit_rotten_apple):
		'''
		'''
		for i in range(random_number_rotten):
			if (snake.x[0], snake.y[0]) == (rotten_apples[i].x, \
				rotten_apples[i].y):
				assert hit_rotten_apple == True, 'Did not actually' \
				' hit apple'

	def block_size_UT(self, block_size, game_height, game_width):
		'''
		'''
		assert game_height % block_size == 0, 'game height is not divisible' \
		' by block_size'
		assert game_width % block_size == 0, 'game width is not divisible by' \
		' block_size'