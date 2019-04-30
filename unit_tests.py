'''
Authors: Kunal Dani, Marina Morrow, Shyanne Salen
Last Modified: April 29th, 2019
Snake Project
Software Carpentry
Classic Snake

This file unit tests our functions in our snake game to see where the 
errors occur.

***CLASS***
	Test_Snake
		This function test our snake game 

***FUNCTIONS***
	get_colors_UT
		tests whether the get_colors function returns 
		a dictionary

	hit_random_snake_UT
		tests whether when a random snake is hit in
		random snake mode if it is actually hitting 
		a random snake

	hit_rotten_apple_UT 
		tests whether when a rotten apple is hit in
		rotten apple mode if it is actually hitting 
		a rotten apple

	block_size_UT
		tests whether the game height and width
		are divisible by block size

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
		This function tests to see whether when a random snake is 
		hit in random snake mode if it is actually hitting 
		a random snake

		***Parameter***
			hit_random_snake: *boolean*
				A boolean that is true if the user's snake's head intersects
            one of the random snakes.
		'''
		assert hit_random_snake == True, 'Did not actually hit snake'

	def hit_rotten_apple_UT(self, hit_rotten_apple):
		'''	
		This function tests whether when a rotten apple is hit in
		rotten apple mode if it is actually hitting 
		a rotten apple

		***Parameter***
			hit_rotten_apple: *Boolean*
          		This boolean returns true or false depending on if the 
           		snake's head position intersected the rotten apple position.
		'''
		assert hit_rotten_apple == True, 'Did not actually hit apple'

	def hit_apple_UT(self, rotten_apples, snake, hit_rotten_apple):
		'''
		This function tests whether when a rotten apple is hit in
		rotten apple mode if it is actually hitting 
		a rotten apple

		**Parameters***
		    rotten_apples: *list, obj*
            	This is a list containing objects from the apple class 
           		corresponding to the rotten apples spawned.
           	snake: *obj*
            	This is the snake object that can be moved around the 
            	screen using the move function in the snake class.
            hit_rotten_apple: *Boolean*
          		This boolean returns true or false depending on if the 
           		snake's head position intersected the rotten apple position.
		'''
		for i in range(random_number_rotten):
			if (snake.x[0], snake.y[0]) == (rotten_apples[i].x, \
				rotten_apples[i].y):
				assert hit_rotten_apple == True, 'Did not actually' \
				' hit apple'

	def block_size_UT(self, block_size, game_height, game_width):
		'''
		This function tests whether the game height and width
		are divisible by block size

		***Parameters***
		    block_size: *int*
            	This is an integer corresponding to the block size of the 
            	apple seen during gameplay,
          	game_width: *int*
            	An integer corresponding to the width of the game grid.
           	game_height: *int*
            	An integer corresponding to the height of the game grid.

		'''
		assert game_height % block_size == 0, 'game height is not divisible' \
		' by block_size'
		assert game_width % block_size == 0, 'game width is not divisible by' \
		' block_size'