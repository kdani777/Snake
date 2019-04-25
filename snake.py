'''
Authors: Kunal Dani, Shyanne Salen, Marina Morrow
Last Modified: April 18th, 2019

'''
from pygame.locals import *
import pygame, sys

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
        self.color = (0, 0, 0)
        self.x = 20
        self.y = 20

class Snake():
    def __init__(self):
        self.x = 10
        self.y = 10
        self.speed = 10
        self.color = (0, 255, 0)

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

def move_snake(DISPLAYSURF, block_size, fpsClock, FPS):
    pygame.display.update()
    s = Snake()
    moving_right = True
    moving_left = False
    moving_up = False
    moving_down = False
    while True:
        DISPLAYSURF.fill((0,0,0))
        snake = pygame.Rect(s.x, s.y, block_size, block_size)
        pygame.draw.rect(DISPLAYSURF, s.color, snake)
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
                if moving_up or moving_down:
                    print "right"
                    moving_right = True
                    moving_up = False
                    moving_left = False
                    moving_down = False
            elif key_pressed[0].key == K_LEFT:
                if moving_up or moving_down:
                    print "left"
                    moving_left = True
                    moving_up = False
                    moving_right = False
                    moving_down = False
            elif key_pressed[0].key == K_UP:
                if moving_right or moving_left:
                    print "up"
                    moving_up = True
                    moving_right = False
                    moving_left = False
                    moving_down = False
            elif key_pressed[0].key == K_DOWN:
                if moving_right or moving_left:
                    print "down"
                    moving_down = True
                    moving_up = False
                    moving_right = False
                    moving_left = False
        if moving_right:
            s.move_right()                    
        elif moving_left:
            s.move_left()
        elif moving_up:
            s.move_up()
        elif moving_down:
            s.move_down()

        pygame.display.update()
        fpsClock.tick(FPS)

def play_game(game_width = 500, game_height = 500, FPS = 15, block_size = 20):
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((game_width, game_height))
    pygame.display.set_caption('Snake')
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((game_width, game_height))
    title_screen(DISPLAYSURF)
    move_snake(DISPLAYSURF, block_size, fpsClock, FPS)
    

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

