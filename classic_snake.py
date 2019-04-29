'''
Authors: Kunal Dani, Shyanne Salen, Marina Morrow
Last Modified: April 29th, 2019
Lazor Project
Software Carpentry
Classic Snake

This file contains the Snake and Apple classes that facilitate the attributes
of the snake and apple, respectively. It also contains functions that will
define the starting snake, create the apples, show score during gameplay, and
help make the snake move using the arrow keys on a keyboard.

***CLASS***
    Apple
        This class creates an apple object and assigns it with
        specific dimensions and color
    Snake
        This class creates a snake object and assigns it with specific
        dimensions, color, speed and direction. The class also contains
        the move function that helps facilitate how and with what speed
        the snake will move. There is an additional function that helps
        append a new piece to the end of the snake, which is necessary for
        when the snake eats an apple or interacts with a random snake.
***FUNCTIONS***
    initial_snake
        This function creates the snake upon start up of the game
    spawn_apple
        This function facilitates how the apple will spawn on the gameboard
    show_score
        This function will show the current score while playing the game
        and will update the score as the game progresses
    get_key_pressed
        This function will help facilitate how the snake moves based on which
        of the arrow keys are pressed.

'''

from pygame.locals import *
import pygame
import sys
import random


class Apple(object):
    '''
    The Apple class creates an apple object with
    the color red and position x and y

    ***Functions***
        __init__
            This determines self for the apple.
    '''

    def __init__(self):
        '''
        This function determines self for the apple and can be used to create
        instance of the object. The apple consists of assigned color (red) and
        position in the form of color, x, and y, respectively.
        '''
        self.color = 2
        self.x = 20
        self.y = 20


class Snake():
    '''
    The Snake class creates a snake object that can move around the board
    in four different directions and a particular speed.

    ***Functions***
        __init__
            This determines self for the snake
        move
            This function facilitates the movements of the snake
    '''
    def __init__(self):
        '''
        This function determines self for the snake and can be used to create
        an instance of the object. The snake is composed of a position (x,y),
        speed, color and direction.
        '''
        self.x = 10
        self.y = 10
        self.speed = 1
        self.color = 3
        self.direction = "right"

    def move(self):
        '''
        This function allows the snake to navigate around the board in four
        different directions (right, left, up or down). It also ensure that
        the position of each component of the snake is such that the snake
        remains continuous.
        '''
        if self.direction == "right":
            self.x[0] = self.x[0] + self.speed
        elif self.direction == "left":
            self.x[0] = self.x[0] - self.speed
        elif self.direction == "up":
            self.y[0] = self.y[0] - self.speed
        elif self.direction == "down":
            self.y[0] = self.y[0] + self.speed

        for i in range(len(self.x) - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

    def add_snake_pieces(self):
        '''
        This function appends a piece of the snake to the
        end of the snake by appending a new position to the list of
        positions the snake already occupies

        Necessary during gameplay either when the snake eats an apple or
        intersects with the random snakes.
        '''
        if self.x[-1] == self.x[-2]:
            self.x.append(self.x[-1])
            self.y.append(self.y[- 1] - 1)
        elif self.y[-1] == self.y[- 2]:
            self.x.append(self.x[- 1] - 1)
            self.y.append(self.y[- 1])


def initial_snake(snake_size, nblocks_width, nblocks_height):
    '''
    This function will create the first snake that appears in the game

    **Parameters**
        snake_size: *int*
            This is an integer representing the initial size of the snake
        nblocks_width: *int*
            This value corresponds to the number of
            blocks that make the width of the overall grid
        nblocks_height: *int*
            This value corresponds to the number of blocks that
            make the height of the overall grid
    **Returns**
        snake: *class, list*
            The coordinates of the snake object from the snake class
            are returned in the form of a list corresponding to the
            components of the snake
    '''
    snake = Snake()
    x = random.randint(2 + snake_size, (int(nblocks_width / 2)))
    y = random.randint(2 + snake_size, (int(nblocks_height / 2)))
    snake.x = [x]
    snake.y = [y]
    for i in range(snake_size):
        snake.x.append(snake.x[0] - i)
        snake.y.append(snake.y[0])
    return snake


def spawn_apple(nblocks_width, nblocks_height, snake, game_mode):
    '''
    This function will create an apple object randomly on the game board

    **Parameters**
        nblocks_width: *int*
            This value corresponds to the number of
            blocks that make the width of the overall grid
        nblocks_height: *int*
            This value corresponds to the number of blocks that
            make the height of the overall grid
        snake: *class obj*
            This corresponds to an object within the snake class
        game_mode: *str*
            The string corresponds to the type of game mode the user is playing

    **Returns**
        apple: *class, obj*
            An object from the apple class a certain color and position

    '''
    apple = Apple()
    apple.x = random.randint(2, nblocks_width - 2)
    apple.y = random.randint(2, nblocks_height - 2)
    while (apple.x, apple.y) in zip(snake.x, snake.y):
        apple.x = random.randint(2, nblocks_width - 2)
        apple.y = random.randint(2, nblocks_height - 2)
    if game_mode == "Rotten Apples Mode":
        while snake.x[0] < apple.x < snake.x[0] + 10 and snake.y[0] < apple.y < snake.y[0] + 10:
            apple.x = random.randint(2, nblocks_width - 2)
            apple.y = random.randint(2, nblocks_height - 2)
    return apple


def show_score(current_score, game_width, DISPLAYSURF, score_color, colors):
    '''
    This function will facilitate how the score is displayed on
    the screen during gameplay.during

    **Parameters**
        current_score: *int*
            An integer representing the current score during gameplay
        game_width: *int*
            An integer corresponding to the width of the game grid
        DISPLAYSURF: *class*
            This is the pygame.Surface class taken from the pygame module
        score_color: *int*
            This is an integer consisting of 0 or 1 corresponding to either
            a black or white background respectively.
        colors: *dict, tuple*
            This is a dictionary of 17 tuples corresponding to 17 colors
            used throughout gameplay
    '''
    font = pygame.font.SysFont('lucidabright', 20)
    score = font.render('Score: %s' % (current_score), True, colors[score_color])
    score_rect = score.get_rect()
    score_rect.topleft = (game_width - 120, 10)
    DISPLAYSURF.blit(score, score_rect)


def get_key_pressed(snake):
    '''
    This is a function that facilitates how the snake object moves
    upon pressing one of the fours arrow keys during gameplay

    **Parameters**
        snake: *class, obj*
            This is the snake object from the snake class that is
            seen and used during gameplay
    '''
    key_pressed = pygame.event.get(KEYUP)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if len(key_pressed) > 0:
        if key_pressed[0].key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif key_pressed[0].key == K_RIGHT:
            if snake.direction == "up" or snake.direction == "down":
                snake.direction = "right"
        elif key_pressed[0].key == K_LEFT:
            if snake.direction == "up" or snake.direction == "down":
                snake.direction = "left"
        elif key_pressed[0].key == K_UP:
            if snake.direction == "right" or snake.direction == "left":
                snake.direction = "up"
        elif key_pressed[0].key == K_DOWN:
            if snake.direction == "right" or snake.direction == "left":
                snake.direction = "down"
