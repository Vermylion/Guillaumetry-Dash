import pygame

import PgText
import Load
import LevelPlay

pause = 0
pressed = False
show_window = True

#Function gets called every frame to detect if pause button (escape) has been pressed
#When true, will create a pause menu screen
def paused(event, screen, win_w, win_h):
    global pause, pressed, show_window

    #Detect key press (esc)
    if pressed == False:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                #Allow to press only once, and show menu only once (until key pressed again)
                pressed = True
                show_window = True

                pause = (pause + 1) % 2

    #Detect release of key (set pressed to false, ward of multiple key calls)
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_ESCAPE:
            pressed = False

    #If is paused and it's the first time to show the pause menu
    if pause == 1 and show_window:
        #Create semi_transparent 'menu'
        paused_bg_surf = pygame.Surface((win_w, win_h), pygame.SRCALPHA)
        paused_bg_surf.fill((0, 0, 0, 128))

        #Write text to it ('Game Paused')
        totalText = PgText.set_text('Game Paused', (255, 255, 255, 128), win_w / 2, win_h / 2, 'Pusab.otf', 70)
        paused_bg_surf.blit(totalText[0], totalText[1])

        #Draw or 'blit' pause menu to given surface
        screen.blit(paused_bg_surf, (0, 0))

        show_window = False
        
    #if pause == 0:
    #    Load.settings()
    #    LevelPlay.load_level(win_w, win_h)

    return pause

def win(screen, win_w, win_h):
    global pause, pressed, show_window
    
    print('win')