from pygame.locals import *
import pygame, sys
import random

class Apple(object):
    '''
    '''
    def __init__(self):
        '''
        '''
        self.color = 2
        self.x = 20
        self.y = 20

class Snake():
    '''
    '''
    def __init__(self):
        '''
        '''
        self.x = 10
        self.y = 10
        self.speed = 1
        self.color = 3
        self.direction = "right"

    def move(self):
        '''
        '''
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

    def add_snake_pieces(self):
        '''
        '''
        if self.x[-1] == self.x[-2]:
            self.x.append(self.x[-1])
            self.y.append(self.y[-1]-1)
        elif self.y[-1] == self.y[-2]:
            self.x.append(self.x[-1]-1)
            self.y.append(self.y[-1])

def initial_snake(snake_size, nblocks_width, nblocks_height):
    '''
    '''
    snake = Snake()
    x = random.randint(2+snake_size, nblocks_width/2)
    y = random.randint(2+snake_size, nblocks_height/2)
    snake.x = [x]
    snake.y = [y]
    for i in range(snake_size):
        snake.x.append(snake.x[0] - i)
        snake.y.append(snake.y[0])
    return snake

def spawn_apple(nblocks_width, nblocks_height, snake, game_mode):
    '''
    '''
    apple = Apple()
    apple.x = random.randint(2, nblocks_width-2)
    apple.y = random.randint(2, nblocks_height-2)
    while (apple.x, apple.y) in zip(snake.x, snake.y):
        apple.x = random.randint(2, nblocks_width-2)
        apple.y = random.randint(2, nblocks_height-2)
    if game_mode == "Rotten Apples Mode":
        while snake.x[0] < apple.x < snake.x[0] + 10 and snake.y[0] < apple.y < snake.y[0] + 10:
            apple.x = random.randint(2, nblocks_width-2)
            apple.y = random.randint(2, nblocks_height-2)
    return apple

def show_score(current_score, game_width, DISPLAYSURF, score_color, colors):
    '''
    '''
    font = pygame.font.SysFont('lucidabright', 20)
    score = font.render('Score: %s' % (current_score), True, colors[score_color])
    score_rect = score.get_rect()
    score_rect.topleft = (game_width - 120, 10)
    DISPLAYSURF.blit(score, score_rect)

def get_key_pressed(snake):
    '''
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