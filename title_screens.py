from pygame.locals import *
import pygame, sys
from snake_game_modes import get_colors

def title_screen(DISPLAYSURF, game_width, game_height):
    colors = get_colors()
    while True:
        font = pygame.font.SysFont('berlinsansfb', 150) 
        font2 = pygame.font.SysFont('cambria', 20)  
        title = font.render('Snake', True, colors[1])
        title_rect = title.get_rect(center=(game_width/2, 200))
        DISPLAYSURF.blit(title, title_rect)
        subtitle_1 = font2.render('Press any key to contine', True, colors[15])
        subtitle_2 = font2.render('Press escape or close to quit', True, colors[15])
        subtitle_1_rect = subtitle_1.get_rect(center=(game_width/2, 275))
        DISPLAYSURF.blit(subtitle_1, subtitle_1_rect)
        subtitle_2_rect = subtitle_2.get_rect(center=(game_width/2, 300))
        DISPLAYSURF.blit(subtitle_2, subtitle_2_rect)
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

def mode_screen(DISPLAYSURF, game_width, game_height):
    colors = get_colors()
    while True:
        DISPLAYSURF.fill((0,0,0))
        # print pygame.font.get_fonts()
        font = pygame.font.SysFont('maiandragd', 20)
        rect = pygame.draw.rect(DISPLAYSURF, colors[16], (game_width/2-60, 100, 120, 25))
        text = font.render("Classic Mode", True, colors[10])
        DISPLAYSURF.subsurface(rect)
        DISPLAYSURF.subsurface(rect).blit(text, (3, 0))
        rect2 = pygame.draw.rect(DISPLAYSURF, colors[16], (game_width/2-100, 200, 200, 25))
        text2 = font.render("Color Changing Mode", True, colors[10])
        DISPLAYSURF.subsurface(rect2)
        DISPLAYSURF.subsurface(rect2).blit(text2, (3, 0))
        rect3 = pygame.draw.rect(DISPLAYSURF, colors[16], (game_width/2-(190/2), 300, 190, 25))
        text3 = font.render("Rotten Apples Mode", True, colors[10])
        DISPLAYSURF.subsurface(rect3)
        DISPLAYSURF.subsurface(rect3).blit(text3, (3, 0))
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if game_width/2+60 > mouse[0] > game_width/2-60 and 100+25 > mouse[1] > 100:
            if click[0] == 1:
                game_mode = "Classic"
                return game_mode
        elif game_width/2+100 > mouse[0] > game_width/2-100 and 200+25 > mouse[1] > 200:
            if click[0] == 1:
                game_mode = "Color Changing Mode"
                return game_mode
        elif game_width/2+(190/2) > mouse[0] > game_width/2-(190/2) and 300+25 > mouse[1] > 300:
            if click[0] == 1:
                game_mode = "Rotten Apples Mode"
                return game_mode
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

def game_over_screen(DISPLAYSURF, block_size, fpsClock, FPS, game_height, game_width, nblocks_width, nblocks_height):
    colors = get_colors()
    while True:
        DISPLAYSURF.fill((0,0,0))
        play_again = False
        # print pygame.font.get_fonts()
        font = pygame.font.SysFont('broadway', 70)
        font2 = pygame.font.SysFont('cambria', 20)
        title = font.render('GAME OVER', True, (255,255,255))
        title_rect = title.get_rect(center=(game_width/2, 200))
        DISPLAYSURF.blit(title, title_rect)
        subtitle_1 = font2.render('Press any key to play again', True, (155, 155, 0))
        subtitle_2 = font2.render('Press escape or close to quit', True, (155, 155, 0))
        subtitle_1_rect = subtitle_1.get_rect(center=(game_width/2, 400))
        DISPLAYSURF.blit(subtitle_1, subtitle_1_rect)
        subtitle_2_rect = subtitle_2.get_rect(center=(game_width/2, 425))
        DISPLAYSURF.blit(subtitle_2, subtitle_2_rect)
        pygame.display.update()
        key_pressed = pygame.event.get(KEYUP)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                return play_again
        if len(key_pressed) > 0:
            print key_pressed
            if key_pressed[0].key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                return play_again
            else:
                pygame.event.get()
                play_again = True
                return play_again