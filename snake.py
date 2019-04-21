'''
Authors: Kunal Dani, Shyanne Salen, Marina Morrow
Last Modified: April 18th, 2019

This file contains the code used to play a game of snake with a twist.
The goal is for the snake to eat a set of cherries (or units of something) without eating itself.
Everytime the snake eats one cherry, it will get bigger by one unit.
After it eats 10 cherries, it will change color. Users can try to see who can
eat the most cherries or who can finish the 5 levels (50 cherries total?).

Planning
The we can break this down into components:
First making the snake class and giving it the ability to move using arrow keys
Next we can set up our grid, its dimensions as well as randomize the location of the cherry
everytime the snake position overlaps with the cherry position (can use overlap from lazor)
Then we can give the snake the attribute of growing everytime it overlaps/eats the cherry.
Finally we can worry about the twist, and the different snake skins
If we would like to add extra, we can add scores or do a multiplayer game like slither.io, where
we can give another user their own snake and the ability to move using other keys (like -w,-a,-s,-d etc.)

Our board will be similar to the Lazor board where the origin starts
at the top right and moving right is moving in the +x direction while moving
downwards is corresponds to the +y direction



'''
import pygame as pg

pg.init() # Can't do much without first intializing pygame

class Snake:
    x = 10
    y = 10
    speed = 1  # Can adjust how many pixels/units the snake moves

    # Focus is on x-axis, moving left and right
    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    # Focus is on y-axis and movements up and down
    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed



# pygame.event.pump() will keep pygame in synch with our system
# Typically want to call this once per game loop
pg.event.pump()
keys = pg.key.get_pressed()

class Game:

    width = 800
    height = 600
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.player = Player()

    def on_init(self): # Upon initializing this game...


# if (keys[pg.K_RIGHT]):
#     print('Right arrow pressed.')
