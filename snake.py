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

    # Focus is on x-axis, moving left and right
    def move_right(self):
        self.x = self.x + self.speed

    def move_left(self):
        self.x = self.x - self.speed

    # Focus is on y-axis and movements up and down
    def move_up(self):
        self.y = self.y - self.speed

    def move_down(self):
        self.y = self.y + self.speed

def initial_snake(snake_size, block_size, nblocks_width, nblocks_height):
    s = Snake()
    s.x = random.randint(snake_size, nblocks_width)
    s.y = random.randint(snake_size, nblocks_height)
    snakes = []
    for i in range(snake_size):
        new_snake = Snake()
        new_snake.x = s.x - i
        new_snake.y = s.y
        snakes.append(new_snake)
    return snakes

def add_snake_pieces(snakes):
    new_snake = Snake()
    if snakes[-1].x == snakes[-2].x:
        new_snake.x = snakes[-1].x
        new_snake.y = snakes[-1].y - 1
        new_snake.direction = snakes[-1].direction
        snakes.append(new_snake)
    elif snakes[-1].y == snakes[-2].y:
        new_snake.x = snakes[-1].x - 1
        new_snake.y = snakes[-1].y
        new_snake.direction = snakes[-1].direction
        snakes.append(new_snake)
    return snakes

def spawn_apple(nblocks_width, nblocks_height, block_size):
    apple = Apple()
    apple.x = random.randint(1, nblocks_width-1)
    apple.y = random.randint(1, nblocks_height-1)
    return apple

def move_snake(DISPLAYSURF, block_size, fpsClock, FPS, game_height, game_width, nblocks_width, nblocks_height):
    pygame.display.update()
    hit_apple = False
    snakes = initial_snake(5, block_size, nblocks_width, nblocks_height)
    snake_turns = {}
    apple = spawn_apple(nblocks_width, nblocks_height, block_size)
    while True:
        DISPLAYSURF.fill((0,0,0))
        apple2 = pygame.Rect(apple.x*block_size, apple.y*block_size, block_size, block_size)
        pygame.draw.rect(DISPLAYSURF, apple.color, apple2)  
        for s in snakes:
            y = s.y*block_size
            x = s.x*block_size
            snake = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(DISPLAYSURF, s.color, snake)
            pygame.display.update()
        if hit_apple == True:
            print snakes[-1].direction
            break
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
                if snakes[0].direction == "up" or snakes[0].direction == "down":
                    print "right"
                    snakes[0].direction = "right"
                    snake_turns.update({(snakes[0].x, snakes[0].y): "right"})
            elif key_pressed[0].key == K_LEFT:
                if snakes[0].direction == "up" or snakes[0].direction == "down":
                    snakes[0].direction = "left"
                    snake_turns.update({(snakes[0].x, snakes[0].y): "left"})
                    print snake_turns
                    print "left"
            elif key_pressed[0].key == K_UP:
                if snakes[0].direction == "right" or snakes[0].direction == "left":
                    snakes[0].direction = "up"
                    snake_turns.update({(snakes[0].x, snakes[0].y): "up"})
                    print "up"
            elif key_pressed[0].key == K_DOWN:
                if snakes[0].direction == "right" or snakes[0].direction == "left":
                    snakes[0].direction = "down"
                    snake_turns.update({(snakes[0].x, snakes[0].y): "down"})
                    print "down"
        if snakes[0].direction == "right":
            snakes[0].move_right()
        elif snakes[0].direction == "left":
            snakes[0].move_left()
        elif snakes[0].direction == "up":
            snakes[0].move_up()  
        elif snakes[0].direction == "down":
            snakes[0].move_down()

        for i in range(1, len(snakes)): # gets stuck here somehow
            if snakes[i].direction == "right":
                snakes[i].move_right()
            elif snakes[i].direction == "left":
                snakes[i].move_left()
            elif snakes[i].direction == "up":
                snakes[i].move_up()  
            elif snakes[i].direction == "down":
                snakes[i].move_down()
            if (snakes[i].x, snakes[i].y) in snake_turns:
                snakes[i].direction = snake_turns[(snakes[i].x, snakes[i].y)]
                print len(snakes)
                if i == len(snakes)-1:
                    print snake_turns
                    del snake_turns[(snakes[i].x, snakes[i].y)] # DELETING BEFORE GETS TO THE END OF NEW SNAKE
                    print snake_turns
                    print "i"
                    print i
 
        if (snakes[0].x, snakes[0].y) == (apple.x, apple.y):
            print "hit apple"
            apple = spawn_apple(nblocks_width, nblocks_height, block_size)
            snakes = add_snake_pieces(snakes)
            print len(snakes)

        pygame.display.update()
        fpsClock.tick(FPS)

def play_game(game_width = 500, game_height = 500, FPS = 5, block_size = 20):
    pygame.init()
    nblocks_width = int(game_width/block_size)
    nblocks_height = int(game_height/block_size)
    DISPLAYSURF = pygame.display.set_mode((game_width, game_height))
    pygame.display.set_caption('Snake')
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((game_width, game_height))
    title_screen(DISPLAYSURF)
    move_snake(DISPLAYSURF, block_size, fpsClock, FPS, game_width, game_height, nblocks_width, nblocks_height)
    

play_game()

# class Game:

#     width = 800
#     height = 600
#     player = 0

#     def __init__(self):
#         self._running = True
#         self._display_surf = None
#         self._image_surf = None
#         self.player = Snake()

#     def on_init(self): # Upon initializing this game...
#         pg.init()
#         self._display_surf = pg.display.set_mode((self.width, self.height), pg.HWSURFACE)

#         pg.display.set_caption('Snake')
#         self._running = True
#         self._image_surf = pg.image.load('background.png').convert()

#     def on_event(self, event):
#         if event.type == QUIT:
#             self._running = False

#     def on_loop(self):
#         pass

#     def on_render(self):
#         self.__display_surf.fill((0,0,0))
#         self._display_surf.blit(self._image_surf,(self.snake.x, self.snake.y))
#         pg.display.flip()

#     def on_cleanup(self):
#         pg.quit()

#     def on_execute(self):
#         if self.on_init() == False:
#             self._running = False

#         while not self._running:
#             pg.event.pump()
#             keys = pg.key.get_pressed()
#         # pygame.event.pump() will keep pygame in synch with our system
#         # Typically want to call this once per game loop

#             if (keys[pg.K_RIGHT]):
#                 self.snake.moveRight()

#             if(keys[pg.K_LEFT]):
#                 self.snake.moveLeft()

#             if(keys[pg.K_UP]):
#                 self.snake.moveUp()

#             if(keys[pg.K_DOWN]):
#                 self.snake.moveDown()

#             if(keys[pg.K_ESCAPE]):
#                 self._running = False

#             self.on_loop
#             self.on_render()
#         self.on_cleanup()

# if __name__ == '__main__':
#     play = Game()
#     play.on_execute()

