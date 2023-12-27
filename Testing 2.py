import pygame
import sys

import pgmenu
import Menu

BGCOLOR = (0, 100, 100)

pygame.init()
screen = pygame.display.set_mode((1000, 1000))

Menu.win_w = pygame.display.Info().current_w
Menu.win_h = pygame.display.Info().current_h

Menu.Menus.create()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Bye bye!')
            pygame.quit()
            sys.exit()

    screen.fill(BGCOLOR)
    
    if Menu.menu_change == 0:
        Menu.Main.draw(screen)
    elif Menu.menu_change == 1:
        Menu.Main.draw(screen)
    elif Menu.menu_change == 2:
        Menu.LevelSelection.draw(screen)
    elif Menu.menu_change == 3:
        Menu.Settings.draw(screen)

    pgmenu.update(event)
    pygame.display.update()
