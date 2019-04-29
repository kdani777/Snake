'''
Authors: Kunal Dani, Shyanne Salen, Marina Morrow
Last Modified: April 29th, 2019
Snake Project w/ Different Game Modes
Software Carpentry
Game Mode Code

This code helps set up the different game modes for the classic game snake.
The classic case consist of a snake the user can manipulate using the arrow keys.
The goal of the game is for the snake eat as many apples as possibly without hitting 
the walls or eating itself. As the snake continues to eat the apples, it grows by one unit.

Other game modes include:
1.) Color Changing Mode - Snake, apple and grid changing colors after the snake eats an apple
2.) Rotton Apple Mode - The snake must avoid eating the rotton apples while continuing tryin to eat normal apples.
3.) Random Snake Mode - Snake must avoid eating the random snakes that appear after eating each apples

***Functions***
    The functions in this file are:
        get_colors
            This functions a dictionary consisting of 17 different colors used during gameplay
        initial_random_snakes
            This function creates the initial random snakes that will appear during gameplay of the
            'Random Snakes' Mode
        color_changing_mode
            This function facilitates the color change of the snake, apple, background and score
            during gameplay of the 'Color Changing' Mode
        spawn_rotton_apples
            This functions creates the rotton apples that will appear during gameplay in
            'Rotton Apple' Mode
        spawn_random_snakes
            This function will facilitate the randomized spawning of the other snakes during gameplay in
            'Random Snake' game mode
        draw_rotton_apple
            This function will give the rotton apple attributes like its size and color
            as well as check if the snake intersect the rotton apple
        draw_random_snake
            This function will give the random snake attributes such as it randomized motion as well
            as identify if the user's snake will intersect with the random snakes
        move_snake
            This function will facilitate the actual gameplay of snake in these three different game modes
'''

from pygame.locals import *
import pygame, sys
import random
import time
from classic_snake import Snake, Apple, initial_snake, spawn_apple, show_score, get_key_pressed

def get_colors():
    '''
    This function assigns a value to set colors to easily be able to
    assign colors to a block.

    Colors that the grid will use:
        0 - Black
        1 - White
        2 - Red
        3 - Green
        4 - Blue
        5 - Orange
        6 - Purple
        7 - Yellow
        8 - Pink
        9 - Light Blue
        10 - Light Green
        11 - Turquoise
        12 - Lavender
        13 - Hot Pink
        14 - Coral
        15 - Dark Yellow
        16 - Dark Green
        17 - Rotten Apple brown

    **Returns**

        color_map: *dict, int, tuple*
            A dictionary that will correlate the integer key to
            a color.
    '''
    return {
        0: (0, 0, 0),
        1: (255, 255, 255),
        2: (255, 0, 0),
        3: (0, 255, 0),
        4: (0, 0, 255),
        5: (255, 128, 0),
        6: (127, 0, 255),
        7: (255, 255, 0),
        8: (255, 153, 204),
        9: (153, 204, 255),
        10: (178, 255, 102),
        11: (51, 255, 255),
        12: (204, 153, 255),
        13: (255, 51, 153),
        14: (255, 153, 153),
        15: (155, 155, 0),
        16: (0, 120, 0),
        17: (101,67,33)
    }

def initial_random_snakes(snake_size, nblocks_width, nblocks_height, snake):
    '''
    This function will initialize and create a random snake

    **Parameters**
        snake_size: *int*
            This integer composes the size of the snake.
        nblocks_width: *int*
            This value corresponds to the number of 
            blocks that make the width of the overall grid
        nblocks_height: *int*
            This value corresponds to the number of blocks that
            make the height of the overall grid
        snake: *class obj*
            This corresponds to the snake class object

    **Returns**
        random_snake: *class*
            An instance of the snake class is returned in
            the form of a random snake
    '''
    random_snake = Snake()
    x = random.randint(2+snake_size, int(nblocks_width/2))
    y = random.randint(2+snake_size, int(nblocks_height/2))
    while snake.x[0] < x < snake.x[0] + 20 and snake.y[0] < y < snake.y[0] + 20:
        x = random.randint(2, nblocks_width-2)
        y = random.randint(2, nblocks_height-2)
    while (x,y) in zip(snake.x, snake.y):
        x = random.randint(2, nblocks_width-2)
        y = random.randint(2, nblocks_height-2)
    random_snake.x = [x]
    random_snake.y = [y]
    for i in range(snake_size):
        random_snake.x.append(random_snake.x[0] - i)
        random_snake.y.append(random_snake.y[0])
    return random_snake

def color_changing_mode(apple, snake):
    '''
    This function will take will facilitate the color change of the snake, apple, 
    background and score by assigning a number corresponding to the a color to each of them.

    **Parameters**
        filename: *class*
            The inputs correspond to the 'apple' and 'snake' class objects

    **Returns**
        background: *int*
            This is an integer consisting of either 0 or 1 corresponding to either
            a black or white background respectively.
        score_color: *int*
            This is an integer consisting of either 0 or 1 corresponding to either
            a black or white background respectively.
    '''
    apple.color, snake.color = random.sample(range(2,15),2)
    background = random.randint(0,1)
    if background == 1:
        score_color = 0
    else:
        score_color = 1
    return background, score_color

def spawn_rotten_apples(nblocks_width, nblocks_height, snake, game_mode):
    '''
    This function will initialize and spawn rotten apples by taking in the grid parameters
    the snake class object and the game mode

    **Parameters**
        nblocks_width: *int*
            This value corresponds to the number of 
            blocks that make the width of the overall grid
        nblocks_height: *int*
            This value corresponds to the number of blocks that
            make the height of the overall grid
        snake: *class obj*
            The value corresponding to 'snake' is the snake object from the
            Snake class
        game_mode: *str*
            The string corresponds to the type of game mode the user is playing

    
    **Returns**
        rotten_apples: *list, class, obj*
            This is a list containing objects from the apple class corresponding to the
            rotten apples
        rotten_apples_spawned: *Boolean*
            This is a boolean that returns true if indeed rotten apples have spawned
        random_number_rotten: *int*
            This is an integer between 1 and 5 inclusive corresponding to the number of 
            rotten apples that will appear when the function is called.
    '''
    rotten_apples = []
    random_number_rotten = random.randint(1, 5)
    for a in range(random_number_rotten):
        rotten_apples.append(spawn_apple(nblocks_width, nblocks_height, snake, game_mode))
        rotten_apples[a].color = 17
        rotten_apples_spawned = True
    return rotten_apples, rotten_apples_spawned, random_number_rotten

def spawn_random_snakes(nblocks_width, nblocks_height, snake):
    '''
    This function will initialize and spawn random snakes when the function is called
    in the random snakes game mode

    **Parameters**
        nblocks_width: *int*
            This value corresponds to the number of 
            blocks that make the width of the overall grid
        nblocks_height: *int*
            This value corresponds to the number of blocks that
            make the height of the overall grid
        snake: *class obj*
            The value corresponding to 'snake' is the snake object from the
            Snake class

    **Returns**
        random_snakes: *list, class, obj*
            This is a list containing the snake class object corresponding to the 
            random snakes that appear in the game if the 'Random Snake Mode' game is played
        random_snake_spawned: *Boolean*
            This is a boolean that will return true if indeed random snakes have spawned
            in accordance with the 'Random Snake Mode' game mode
        random_number_snakes: *int*
            This value is an integer between 1 and 3 includsive corresponding 
            to the number of random snakes created.
    '''
    random_number_snakes = random.randint(1, 3)
    random_snakes = []
    for b in range(random_number_snakes):
        snake_size = random.randint(3,5)
        random_snakes.append(initial_random_snakes(snake_size, nblocks_width, nblocks_height, snake))
        random_snakes[b].color = 16
        random_snakes_spawned = True
    return random_snakes, random_snakes_spawned, random_number_snakes

def draw_rotten_apples(DISPLAYSURF, random_number_rotten, rotten_apples, snake, block_size, colors):
    '''
    This function gives the rotten apple attributes like whether or not it was hit by the snake 
    and what facilitates that it was hit by the snake

    **Parameters**
        DISPLAYSURF: *class*
            This is the pygame.Surface class taken from the pygame module
        random_number_rotten: *int*
            This is an integer between 1 and 5 inclusive corresponding to the number of 
            rotten apples that will appear on the grid during gameplay
        rotten_apples: *list, class, obj*
            This is a list containing objects from the apple class corresponding to the
            rotten apples
         snake: *class obj*
            The value corresponding to 'snake' is the snake object from the
            Snake class
        block_size: *int*
            This is an integer corresponding to the blocksize of object seen during gameplay
        colors: *dict, tuple*
            This is a dictionary of 17 sets of tuples corresponding to the 17 colors
            used throughout gameplay

    **Returns**
        hit_rotton_apple: *Boolean*
            This boolean returns true or false depending on if the snake position intersected
            the rotton apple position
    '''
    hit_rotten_apple = False
    for i in range(random_number_rotten):
        if (snake.x[0], snake.y[0]) == (rotten_apples[i].x, rotten_apples[i].y):
            hit_rotten_apple = True
            return hit_rotten_apple
        r_apple = pygame.Rect(rotten_apples[i].x*block_size, rotten_apples[i].y*block_size, block_size, block_size)
        pygame.draw.rect(DISPLAYSURF, colors[rotten_apples[i].color], r_apple)
    return hit_rotten_apple

def draw_random_snakes(random_number_snakes, random_snakes, snake, DISPLAYSURF, colors, nblocks_width, nblocks_height, block_size):
    '''
    This function gives the random snakes attributes such as it random motions and checks if the user's snake 
    ever intersects with the random snakes during gameplay

    **Parameters**
        random_number_snakes: *int*
            This value is an integer between 1 and 3 includsive corresponding 
            to the number of random snakes created.
        random_snakes: *list, class, obj*
            This is a list containing the snake class object corresponding to the 
            random snakes that appear in the game if the 'Random Snake Mode' game is played
         snake: *class obj*
            The value corresponding to 'snake' is the snake object from the
            Snake class                      
        DISPLAYSURF: *class*
            This is the pygame.Surface class taken from the pygame module    
        colors: *dict, tuple*
            This is a dictionary of 17 sets of tuples corresponding to the 17 colors
            used throughout gameplay
        nblocks_width: *int*
            This value corresponds to the number of 
            blocks that make the width of the overall grid
        nblocks_height: *int*
            This value corresponds to the number of blocks that
            make the height of the overall grid
        block_size: *int*
            This is an integer corresponding to the blocksize of object seen during gameplay

    **Returns**
        hit_random_snake: *Boolean*
            A boolean that is true if the user's snake intersects with the random snakes
            and false if they do not intersect
    '''
    hit_random_snake = False
    for j in range(random_number_snakes):
        if random_snakes[j].direction == "right":
            random_snakes[j].direction = random.choice(("up", "down", "right"))
        elif random_snakes[j].direction == "left":
            random_snakes[j].direction = random.choice(("up", "down", "left"))
        elif random_snakes[j].direction == "up":
            random_snakes[j].direction = random.choice(("right", "left", "up"))
        elif random_snakes[j].direction == "down":
            random_snakes[j].direction = random.choice(("right", "left", "down"))
        for i in range(len(random_snakes[j].x)):
            if (snake.x[0], snake.y[0]) == (random_snakes[j].x[i], random_snakes[j].y[i]):
                hit_random_snake = True
                return hit_random_snake
        random_snakes[j].move()
        if random_snakes[j].x[0] == -1:
            random_snakes[j].direction = "right"
            random_snakes[j].move()
        elif random_snakes[j].y[0] == -1:
            random_snakes[j].direction = "down"
            random_snakes[j].move()
        elif random_snakes[j].x[0] == nblocks_width:
            random_snakes[j].direction = "left"
            random_snakes[j].move()
        elif random_snakes[j].y[0] == nblocks_height:
            random_snakes[j].direction = "up"
            random_snakes[j].move()
        for i in range(len(random_snakes[j].x)):
            y = random_snakes[j].y[i]*block_size
            x = random_snakes[j].x[i]*block_size
            s = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(DISPLAYSURF, colors[random_snakes[j].color], s)
    return hit_random_snake

def move_snake(DISPLAYSURF, block_size, fpsClock, FPS, game_width, nblocks_width, nblocks_height, game_mode):
    '''
    This function corresponds to movement of the snake and facilitates the overall gameplay depending on the game mode

    **Parameters**
        DISPLAYSURF: *class*
            This is the pygame.Surface class taken from the pygame module
        block_size: *int*
            This is an integer corresponding to the blocksize of object seen during gameplay
        fpsClock: *class*
            This is the clock class
        FPS: *int*
            An integer to be used within the fpsClock class
        game_width: *int*
            An integer corresponding to the width of the game grid
        nblocks_width: *int*
            This value corresponds to the number of
            blocks that make the width of the overall grid
        nblocks_height: *int*
            This value corresponds to the number of blocks that
            make the height of the overall grid
        game_mode: *str*
            The string corresponds to the type of game mode the user is playing

    '''
    colors = get_colors()
    pygame.display.update()
    hit_apple = False
    snake = initial_snake(3, nblocks_width, nblocks_height)
    snake_turns = {}
    apple = spawn_apple(nblocks_width, nblocks_height, snake, game_mode)
    background = 0
    score_color = 1
    rotten_apples_spawned = False
    random_snakes_spawned = False

    while True:
        DISPLAYSURF.fill(colors[background])
        get_key_pressed(snake)
        snake.move()
        if (snake.x[0], snake.y[0]) == (apple.x, apple.y):
            apple = spawn_apple(nblocks_width, nblocks_height, snake, game_mode)
            snake.add_snake_pieces()
            if game_mode == "Color Changing Mode":
                background, score_color = color_changing_mode(apple, snake)
            elif game_mode == "Rotten Apples Mode":
                rotten_apples, rotten_apples_spawned, random_number_rotten = spawn_rotten_apples(nblocks_width, nblocks_height, snake, game_mode)
            elif game_mode == "Random Snakes Mode":
                random_snakes, random_snakes_spawned, random_number_snakes = spawn_random_snakes(nblocks_width, nblocks_height, snake)
        elif snake.x[0] == -1 or snake.y[0] == -1:
            score = len(snake.x)-4
            return score
        elif snake.x[0] == nblocks_width or snake.y[0] == nblocks_height:
            score = len(snake.x)-4
            return score
        elif (snake.x[0], snake.y[0]) in zip(snake.x[2:], snake.y[2:]):
            score = len(snake.x)-4
            return score
        if rotten_apples_spawned:
            hit_rotten_apple = draw_rotten_apples(DISPLAYSURF, random_number_rotten, rotten_apples, snake, block_size, colors)
            if hit_rotten_apple:
                score = len(snake.x)-4
                return score 
        if random_snakes_spawned:
            hit_random_snake = draw_random_snakes(random_number_snakes, random_snakes, snake, DISPLAYSURF, colors, nblocks_width, nblocks_height, block_size)
            if hit_random_snake:
                score = len(snake.x)-4
                return score

        apple2 = pygame.Rect(apple.x*block_size, apple.y*block_size, block_size, block_size)
        pygame.draw.rect(DISPLAYSURF, colors[apple.color], apple2)  
        for i in range(len(snake.x)):
            y = snake.y[i]*block_size
            x = snake.x[i]*block_size
            s = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(DISPLAYSURF, colors[snake.color], s)
        show_score(len(snake.x)-4, game_width, DISPLAYSURF, score_color, colors)
        pygame.display.update()
        fpsClock.tick(FPS)
