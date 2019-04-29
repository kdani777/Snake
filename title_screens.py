'''
Authors: Kunal Dani, Shyanne Salen, Marina Morrow
Last Modified: April 29th, 2019
Snake Project
Software Carpentry
Title Screens

This file contains the code corresponding to the formatting and
functionalization of the title screen that appears upon start up of
the Snake game. Upon startup the user will be given instruction on how
to proceed or exit the game. If the user proceeds, they will be 
instructed to pick one of the four game modes. From there, they will 
navigated to the game of their choosing until they lose. Upon losing
the user will be given directions for if they want to either play 
again or exit the game. This function relies on the snake_game_modes.py
file for the colors.

***FILES***
    snake_game_modes.py
        This file contains the function to operate snake with the three
        other game modes. This file contains the get_colors function
        which returns a dictionary and is used to pick colors for the
        title, game mode, and game over screens.

***FUNCTIONS***
    title_screen
        This function formats the title screen such that the user will
        be given instructions upon start up the game.
    mode_screen
        This function formats and functionalizes the mode screen so 
        the user will be able to navigate between different game modes
        and play the one of their choosing.
    game_over_screen
        This function formats and functionalizes the game over screen 
        that appears upon the user losing the game and instructs the 
        user on how to play again.
'''

from pygame.locals import *
import pygame
import sys
from snake_game_modes import get_colors

def title_screen(DISPLAYSURF, game_width):
    '''
    This function formats and functionalizes the title screen. On the
    title screen the user will see instructions on how to either
    proceed to gameplay or exit the game.

    **Parameter**
        DISPLAYSURF: *class*
            This is the pygame.Surface class taken from the pygame 
            module.
        game_width: *int*
            An integer corresponding to the width of the game grid.

    **Return**
        Function will return itself upon being called, and all 
        parameters and formatting associated with the title screen 
        will be displayed.
    '''
    colors = get_colors()
    while True:
        font = pygame.font.SysFont('berlinsansfb', 150)
        font2 = pygame.font.SysFont('cambria', 20)
        title = font.render('Snake', True, colors[1])
        title_rect = title.get_rect(center=(game_width / 2, 200))
        DISPLAYSURF.blit(title, title_rect)

        subtitle_1 = font2.render('Press any key to contine', True, colors[15])
        subtitle_2 = font2.render('Press escape or close to quit', True, \
            colors[15])
        subtitle_1_rect = subtitle_1.get_rect(center=(game_width / 2, 275))
        DISPLAYSURF.blit(subtitle_1, subtitle_1_rect)
        subtitle_2_rect = subtitle_2.get_rect(center=(game_width / 2, 300))
        DISPLAYSURF.blit(subtitle_2, subtitle_2_rect)
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
            else:
                pygame.event.get()
                return


def mode_screen(DISPLAYSURF, game_width):
    '''
    This function formats and functionalizes the mode screen.
    On the mode screen the user will see directed to one of the
    four game modes and may click on the one of their choosing using
    their cursor. Upon clicking they will be redirected to the game 
     mode
    and the game will initiate.

    **Parameter**
        DISPLAYSURF: *class*
            This is the pygame.Surface class taken from the pygame 
            module.
        game_width: *int*
            An integer corresponding to the width of the game grid.

    **Return**
        Function will return itself upon being called, and all 
        parameters and formatting associated with the mode screen
        will be displayed.
    '''
    colors = get_colors()
    while True:
        DISPLAYSURF.fill((0, 0, 0))
        font = pygame.font.SysFont('maiandragd', 25)
        font2 = pygame.font.SysFont('cambria', 20)
        rect_height = 30
        rect = pygame.draw.rect(DISPLAYSURF, colors[16], (game_width / 2 - \
            (150 / 2), 50, 150, rect_height))
        text = font.render("Classic Mode", True, colors[10])
        DISPLAYSURF.subsurface(rect)
        DISPLAYSURF.subsurface(rect).blit(text, (4, 0))

        rect2 = pygame.draw.rect(DISPLAYSURF, colors[16], (game_width / 2 - \
            (250 / 2), 160, 250, rect_height))
        text2 = font.render("Color Changing Mode", True, colors[10])
        DISPLAYSURF.subsurface(rect2)
        DISPLAYSURF.subsurface(rect2).blit(text2, (4, -3))

        rect3 = pygame.draw.rect(DISPLAYSURF, colors[16], (game_width / 2 - \
            (230 / 2), 270, 230, rect_height))
        text3 = font.render("Rotten Apples Mode", True, colors[10])
        DISPLAYSURF.subsurface(rect3)
        DISPLAYSURF.subsurface(rect3).blit(text3, (2, -3))

        rect4 = pygame.draw.rect(DISPLAYSURF, colors[16], (game_width / 2 - \
            (250 / 2), 380, 250, rect_height))
        text4 = font.render("Random Snakes Mode", True, colors[10])
        DISPLAYSURF.subsurface(rect4)
        DISPLAYSURF.subsurface(rect4).blit(text4, (4, 0))

        subtitle_1 = font2.render('This is the classic snake game. Use the'\
        'arrow keys to', True, colors[9])
        subtitle_2 = font2.render('move the snake around the screen to eat'\
            'the apples.', True, colors[9])
        subtitle_3 = font2.render('Avoid hitting the wall or trying to eat'\
            ' yourself.', True, colors[9])
        subtitle_1_rect = subtitle_1.get_rect(center=(game_width / 2, 90))
        DISPLAYSURF.blit(subtitle_1, subtitle_1_rect)
        subtitle_2_rect = subtitle_2.get_rect(center=(game_width / 2, 110))
        DISPLAYSURF.blit(subtitle_2, subtitle_2_rect)
        subtitle_3_rect = subtitle_3.get_rect(center=(game_width / 2, 130))
        DISPLAYSURF.blit(subtitle_3, subtitle_3_rect)

        subtitle_4 = font2.render('This is like the classic snake game. Use '\
            'the arrow keys', True, colors[9])
        subtitle_5 = font2.render('to move the snake. The snake, apple, and'\
            ' background will', True, colors[9])
        subtitle_6 = font2.render('change color when the snake eats an apple.', \
         True, colors[9])
        subtitle_4_rect = subtitle_4.get_rect(center=(game_width / 2, 200))
        DISPLAYSURF.blit(subtitle_4, subtitle_4_rect)
        subtitle_5_rect = subtitle_5.get_rect(center=(game_width / 2, 220))
        DISPLAYSURF.blit(subtitle_5, subtitle_5_rect)
        subtitle_6_rect = subtitle_6.get_rect(center=(game_width / 2, 240))
        DISPLAYSURF.blit(subtitle_6, subtitle_6_rect)

        subtitle_7 = font2.render('Use the arrow keys to move the snake to' \
            ' eat the apples.', True, colors[9])
        subtitle_8 = font2.render('Do not eat the brown rotten apples. Avoid'\
            ' the wall and', True, colors[9])
        subtitle_9 = font2.render('trying to eat yourself.', True, colors[9])
        subtitle_7_rect = subtitle_7.get_rect(center=(game_width / 2, 310))
        DISPLAYSURF.blit(subtitle_7, subtitle_7_rect)
        subtitle_8_rect = subtitle_8.get_rect(center=(game_width / 2, 330))
        DISPLAYSURF.blit(subtitle_8, subtitle_8_rect)
        subtitle_9_rect = subtitle_9.get_rect(center=(game_width / 2, 350))
        DISPLAYSURF.blit(subtitle_9, subtitle_9_rect)

        subtitle_10 = font2.render('Use the arrow keys to move the snake to eat'\
            ' the apples.', True, colors[9])
        subtitle_11 = font2.render('Avoid trying to eat the dark green snakes.'\
            ' Avoid the wall', True, colors[9])
        subtitle_12 = font2.render('and trying to eat yourself.', True, \
            colors[9])
        subtitle_10_rect = subtitle_10.get_rect(center=(game_width / 2, 420))
        DISPLAYSURF.blit(subtitle_10, subtitle_10_rect)
        subtitle_11_rect = subtitle_11.get_rect(center=(game_width / 2, 440))
        DISPLAYSURF.blit(subtitle_11, subtitle_11_rect)
        subtitle_12_rect = subtitle_12.get_rect(center=(game_width / 2, 460))
        DISPLAYSURF.blit(subtitle_12, subtitle_12_rect)

        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if game_width / 2 + (150 / 2) > mouse[0] > game_width / 2 - (150 / 2) \
         and 50 + 30 > mouse[1] > 50:
            if click[0] == 1:
                game_mode = "Classic Mode"
                return game_mode
        elif game_width / 2 + (250 / 2) > mouse[0] > game_width / 2 - (250 / 2) \
         and 160 + 30 > mouse[1] > 160:
            if click[0] == 1:
                game_mode = "Color Changing Mode"
                return game_mode
        elif game_width / 2 + (230 / 2) > mouse[0] > game_width / 2 - (230 / 2) \
         and 270 + 30 > mouse[1] > 270:
            if click[0] == 1:
                game_mode = "Rotten Apples Mode"
                return game_mode
                game_width / 2 - (250 / 2), 380, 250,
        elif game_width / 2 + (250 / 2) > mouse[0] > game_width / 2-(250 / 2) \
         and 380 + 30 > mouse[1] > 380:
            if click[0] == 1:
                game_mode = "Random Snakes Mode"
                return game_mode
        key_pressed = pygame.event.get(KEYUP)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if len(key_pressed) > 0:
            if key_pressed[0].key == K_ESCAPE:
                pygame.quit()
                sys.exit()


def game_over_screen(DISPLAYSURF, game_width, score):
    '''
    This function formats and functionalizes the game over screen.
    Upon completion of the game the user will see this screen, which
    consists of a 'Game Over' sign and the users score. They will 
    also be instructed on how to play a new game or exit the entire 
    game. All actions will be conducted via keyboard keys.

    **Parameter**
        DISPLAYSURF: *class*
            This is the pygame.Surface class taken from the pygame
            module.
        game_width: *int*
            An integer corresponding to the width of the game grid.
        score: *int*
            An integer corresponding to the users final score.

    **Return**
        Function will return itself upon being called, and all 
        parameters and formatting associated with the game over screen 
        will be displayed in addition to the users score and 
        instructions on how to exit the game or continue playing.

        play_again: *Boolean*
            This is a boolean that will either be true if user presses
            any key to play again or will return false if user opts to
            exit the game.
    '''
    colors = get_colors()
    while True:
        DISPLAYSURF.fill((0, 0, 0))
        play_again = False
        font = pygame.font.SysFont('broadway', 70)
        font2 = pygame.font.SysFont('cambria', 20)
        title = font.render('GAME OVER', True, (255, 255, 255))
        title_rect = title.get_rect(center=(game_width / 2, 200))
        DISPLAYSURF.blit(title, title_rect)

        subtitle_1 = font2.render('Press any key to play again', True, (155, \
            155, 0))
        subtitle_2 = font2.render('Press escape or close to quit', True, (155, \
         155, 0))
        subtitle_1_rect = subtitle_1.get_rect(center=(game_width / 2, 400))
        DISPLAYSURF.blit(subtitle_1, subtitle_1_rect)
        subtitle_2_rect = subtitle_2.get_rect(center=(game_width / 2, 425))
        DISPLAYSURF.blit(subtitle_2, subtitle_2_rect)

        font3 = pygame.font.SysFont('lucidabright', 20)
        final_score = font3.render('Final Score: %s' % (score), True, \
            colors[1])
        score_rect = final_score.get_rect(center=(game_width / 2, 300))
        DISPLAYSURF.blit(final_score, score_rect)
        pygame.display.update()

        key_pressed = pygame.event.get(KEYUP)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                return play_again
        if len(key_pressed) > 0:
            if key_pressed[0].key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                return play_again
            else:
                pygame.event.get()
                play_again = True
                return play_again
