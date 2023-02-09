import pygame
from pygame.locals import RESIZABLE, DOUBLEBUF
import sys

import PgText
import LevelMenu
import LevelPlay
import Menu
import pgmenu

import Load

FPS = 200
BGCOLOR = (0, 100, 170)

win_w = 1920
win_h = 1080

#Initiate window
pygame.init()

#Get monitor res
w = pygame.display.Info().current_w
h = pygame.display.Info().current_h

#Keep window to always be smaller than the monitor res
if w <= win_w:
    win_w = round(w / 1.5)
if h <= win_h:
    win_h = round(h / 1.5)
    
#Give the menus the window dimensions
Menu.win_w = win_w
Menu.win_h = win_h

#Set window's attributes
pygame.display.set_caption(f'Guillaumetry Dash v0.03-Beta ({win_w}x{win_h})')
flags = RESIZABLE | DOUBLEBUF
screen = pygame.display.set_mode((win_w, win_h), flags, 16)
#pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, VIDEORESIZE])
screen.fill(BGCOLOR)

#Create Pygame clock (limit fps)
clock = pygame.time.Clock()
delta_time = clock.tick(FPS)

#Load Settings in
Load.settings()

#Load Selected Level
LevelPlay.load_level(win_w, win_h)

#Create the levels using pgmenu
Menu.Menus.create()

#Run loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Bye Bye!')
            running = False
            pygame.quit()
            sys.exit()

        #When the window gets resized, resize it
        if event.type == pygame.VIDEORESIZE:
            win_w, win_h = event.w, event.h
            pygame.display.set_caption(f'Guillaumetry Dash v0.03-Beta ({win_w}x{win_h})')
            screen = pygame.display.set_mode((win_w, win_h), pygame.RESIZABLE)
            #Reload level settings and dimensions
            Load.settings()
            LevelPlay.load_level(win_w, win_h)
            #Resize all menus
            Menu.Menus.resize(win_w, win_h)
            #Redraw Pause menu if need be
            screen.fill(BGCOLOR)
            LevelMenu.show_window = True
            LevelMenu.paused(event, screen, win_w, win_h)

    screen.fill(BGCOLOR)
    
    if Menu.menu_change == 0:
        Menu.Main.draw(screen)
    elif Menu.menu_change == 1:
        #Call for eventual pause menu
        pause = LevelMenu.paused(event, screen, win_w, win_h)
        #If not in pause, play the level
        if pause == 0:
            LevelPlay.play_level(screen, event, delta_time, win_w, win_h)
    elif Menu.menu_change == 2:
        Menu.LevelSelection.draw(screen)
    elif Menu.menu_change == 3:
        Menu.Settings.draw(screen)

        #Show fps
    totalText = PgText.set_text(round(clock.get_fps()), (0, 0, 0, 128), 50, 30, 'Pusab.otf', 40)
    screen.blit(totalText[0], totalText[1])

    #update the window display
    pgmenu.update(event)
    pygame.display.update()
    delta_time = clock.tick(FPS)