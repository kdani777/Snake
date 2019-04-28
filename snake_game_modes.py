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
        16: (0, 120, 0)
    }

class Apple(object):
    def __init__(self):
        self.color = 2
        self.x = 20
        self.y = 20

class Snake():
    def __init__(self):
        self.x = 10
        self.y = 10
        self.speed = 1
        self.color = 3
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
    x = random.randint(2+snake_size, nblocks_width/2)
    y = random.randint(2+snake_size, nblocks_height/2)
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

def show_score(score, game_width, DISPLAYSURF, score_color):
    colors = get_colors()
    font = pygame.font.SysFont('lucidabright', 20)
    score = font.render('Score: %s' % (score), True, colors[score_color])
    score_rect = score.get_rect()
    score_rect.topleft = (game_width - 120, 10)
    DISPLAYSURF.blit(score, score_rect)

def move_snake(DISPLAYSURF, block_size, fpsClock, FPS, game_height, game_width, nblocks_width, nblocks_height, game_mode):
    colors = get_colors()
    print type(color)
    pygame.display.update()
    hit_apple = False
    snake = initial_snake(3, block_size, nblocks_width, nblocks_height)
    snake_turns = {}
    apple = spawn_apple(nblocks_width, nblocks_height, block_size)
    background = 0
    score_color = 1
    while True:
        DISPLAYSURF.fill(colors[background])
        apple2 = pygame.Rect(apple.x*block_size, apple.y*block_size, block_size, block_size)
        pygame.draw.rect(DISPLAYSURF, colors[apple.color], apple2)  
        for i in range(len(snake.x)):
            y = snake.y[i]*block_size
            x = snake.x[i]*block_size
            s = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(DISPLAYSURF, colors[snake.color], s)
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
            if game_mode == "Color Changing Mode":
                apple.color, snake.color = random.sample(range(2,15),2)
                print apple.color, snake.color
                background = random.randint(0,1)
                if background == 1:
                    score_color = 0
                else:
                    score_color = 1
        elif snake.x[0] == -2 or snake.y[0] == -2:
            print "wall"
            return
        elif snake.x[0] == nblocks_width+1 or snake.y[0] == nblocks_height+1:
            print "wall"
            return
        if (snake.x[0], snake.y[0]) in zip(snake.x[2:], snake.y[2:]):
            print "hit itself"
            return

        show_score(len(snake.x)-4, game_width, DISPLAYSURF, score_color)
        pygame.display.update()
        fpsClock.tick(FPS)