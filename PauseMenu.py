import pygame

import PgText

pause = 0
pressed = False
show_window = True

def paused(event, screen, win_w, win_h):
    global pause, pressed, show_window

    if pressed == False:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pressed = True
                show_window = True

                pause = (pause + 1) % 2

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_ESCAPE:
            pressed = False

    if pause == 1 and show_window:
        paused_bg_surf = pygame.Surface((win_w, win_h), pygame.SRCALPHA)
        paused_bg_surf.fill((0, 0, 0, 128))

        totalText = PgText.set_text('Game Paused', (255, 255, 255, 128), win_w / 2, win_h / 2, 'Pusab.otf', 70)
        screen.blit(totalText[0], totalText[1])

        screen.blit(paused_bg_surf, (0, 0))

        show_window = False

    return pause