'''
Authors: Kunal Dani, Shyanne Salen, Marina Morrow
Last Modified: April 18th, 2019

'''
from pygame.locals import *
import pygame, sys
import random

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

def title_screen(DISPLAYSURF):
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
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if len(key_pressed) > 0:
            print key_pressed
            if key_pressed[0].key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            else:
                pygame.event.get()
                return

class Apple(object):
    def __init__(self):
        self.color = (255, 0, 0)
        self.x = 20
        self.y = 20

class Snake():
    def __init__(self):
        self.x = 10
        self.y = 10
        self.speed = 1
        self.color = (0, 255, 0)
        self.direction = "right"
        self.block_size = 20

    def move(self):
        if self.direction == "right":
            self.x[0] = self.x[0] + self.speed
        elif self.direction == "left":
            self.x[0] = self.x[0] - self.speed
        elif self.direction == "up":
            self.y[0] = self.y[0] - self.speed  
        elif self.direction == "down":
            self.y[0] = self.y[0] + self.speed

        for i in range(len(self.x)-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

    # Focus is on x-axis, moving left and right
    def add_snake_pieces(self):
        if self.x[-1] == self.x[-2]:
            self.x.append(self.x[-1])
            self.y.append(self.y[-1]-1)
        elif self.y[-1] == self.y[-2]:
            self.x.append(self.x[-1]-1)
            self.y.append(self.y[-1])

def initial_snake(snake_size, block_size, nblocks_width, nblocks_height):
    snake = Snake()
    x = random.randint(2+snake_size, nblocks_width-5)
    y = random.randint(2+snake_size, nblocks_height-5)
    snake.x = [x]
    snake.y = [y]
    for i in range(snake_size):
        snake.x.append(snake.x[0] - i)
        snake.y.append(snake.y[0])
    return snake

def spawn_apple(nblocks_width, nblocks_height, block_size):
    apple = Apple()
    apple.x = random.randint(2, nblocks_width-2)
    apple.y = random.randint(2, nblocks_height-2)
    return apple

def move_snake(DISPLAYSURF, block_size, fpsClock, FPS, game_height, game_width, nblocks_width, nblocks_height):
    pygame.display.update()
    hit_apple = False
    snake = initial_snake(3, block_size, nblocks_width, nblocks_height)
    snake_turns = {}
    apple = spawn_apple(nblocks_width, nblocks_height, block_size)
    while True:
        DISPLAYSURF.fill((0,0,0))
        apple2 = pygame.Rect(apple.x*block_size, apple.y*block_size, block_size, block_size)
        pygame.draw.rect(DISPLAYSURF, apple.color, apple2)  
        for i in range(len(snake.x)):
            y = snake.y[i]*block_size
            x = snake.x[i]*block_size
            s = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(DISPLAYSURF, snake.color, s)
        pygame.display.update()
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
                    print "right"
                    snake.direction = "right"
            elif key_pressed[0].key == K_LEFT:
                if snake.direction == "up" or snake.direction == "down":
                    print "left"
                    snake.direction = "left"
            elif key_pressed[0].key == K_UP:
                if snake.direction == "right" or snake.direction == "left":
                    snake.direction = "up"
                    print "up"
            elif key_pressed[0].key == K_DOWN:
                if snake.direction == "right" or snake.direction == "left":
                    snake.direction = "down"
                    print "down"
        snake.move() 
        if (snake.x[0], snake.y[0]) == (apple.x, apple.y):
            print "hit apple"
            apple = spawn_apple(nblocks_width, nblocks_height, block_size)
            snake.add_snake_pieces()
        elif snake.x[0] == -1 or snake.y[0] == -1:
            print "wall"
            return
        elif snake.x[0] == nblocks_width or snake.y[0] == nblocks_height:
            print "wall"
            return
        if (snake.x[0], snake.y[0]) in zip(snake.x[2:], snake.y[2:]):
                print "hit itself"
                return

        pygame.display.update()
        fpsClock.tick(FPS)

def play_game(game_width = 500, game_height = 500, FPS = 7, block_size = 20):
    pygame.init()
    nblocks_width = int(game_width/block_size)
    nblocks_height = int(game_height/block_size)
    DISPLAYSURF = pygame.display.set_mode((game_width, game_height))
    pygame.display.set_caption('Snake')
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((game_width, game_height))
    title_screen(DISPLAYSURF)
    move_snake(DISPLAYSURF, block_size, fpsClock, FPS, game_width, game_height, nblocks_width, nblocks_height)
    print "game_over"

if __name__ == '__main__':
    play_game()