from pygame.locals import *
import pygame, sys
import random

class Test_Snake(object):
	'''
	'''
	def get_colors_UT(self, colors):
		'''
		'''
		assert (type(colors) == dict), "The colors are not a dictionary"

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
			if (snake.x[0], snake.y[0]) == (rotten_apples[i].x, rotten_apples[i].y):
				assert hit_rotten_apple == True, 'Did not actually hit apple'

	def block_size_UT(self, block_size, game_height, game_width):
		'''
		'''
		assert game_height % block_size == 0, 'game height is not divisible by block_size'
		assert game_width % block_size == 0, 'game width is not divisible by block_size'