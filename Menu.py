import pygame

import pgmenu

win_w = 1920
win_h = 1080

menu_change = 0

def MenuPlay():
    global menu_change; menu_change = 1
    
    Menus.disable()

class Menus:
    def __init__(self):
        pass
    
    def create():
        Main.create()
        Pause.create()
        LevelSelection.create()
        CharacterSelection.create()
        Settings.create()
        
        global backBtn; backBtn = pgmenu.Button.create(((win_w / 19) - ((win_w / 16) / 2), (win_h / 15) - ((win_h / 16) / 2)), (max(win_w, win_h) / 16, max(win_w, win_h) / 16), Main.MenuChange, status = 'disabled')

    def disable():
        #Global back button
        global backBtn; backBtn = pgmenu.Button.modify(backBtn, (backBtn[0][0], backBtn[0][1]), (backBtn[0][2], backBtn[0][3]), backBtn[1], 'disabled')
        
        #Main Menu Widgets
        global playBtn; playBtn = pgmenu.Button.modify(playBtn, (playBtn[0][0], playBtn[0][1]), (playBtn[0][2], playBtn[0][3]), playBtn[1], 'disabled')
        global settingsBtn; settingsBtn = pgmenu.Button.modify(settingsBtn, (settingsBtn[0][0], settingsBtn[0][1]), (settingsBtn[0][2], settingsBtn[0][3]), settingsBtn[1], 'disabled')
        global levelsBtn; levelsBtn = pgmenu.Button.modify(levelsBtn, (levelsBtn[0][0], levelsBtn[0][1]), (levelsBtn[0][2], levelsBtn[0][3]), levelsBtn[1], 'disabled')
        
        #Level Selection Menu Widgets
        
        #Settings Menu Widgets
        global fpsCheckbox; fpsCheckbox = pgmenu.Checkbox.modify(fpsCheckbox, (fpsCheckbox[0][0], fpsCheckbox[0][1]), fpsCheckbox[0][2], fpsCheckbox[1], pgmenu.Checkbox.get(fpsCheckbox), 'disabled')
        global colCheckbox; colCheckbox = pgmenu.Checkbox.modify(colCheckbox, (colCheckbox[0][0], colCheckbox[0][1]), colCheckbox[0][2], colCheckbox[1], pgmenu.Checkbox.get(colCheckbox), 'disabled')
    
    def resize(w, h):
        global win_w; win_w = w
        global win_h; win_h = h
        
        Menus.create()
        print(menu_change, 'resized')
        if menu_change == 0:
            Main.MenuChange()
        elif menu_change == 1:
            Main.MenuChange()
        elif menu_change == 2:
            LevelSelection.MenuChange()
        elif menu_change == 3:
            Settings.MenuChange()
    
class Main:
    def __init__(self):
        pass
    
    def MenuChange():
        global menu_change; menu_change = 0
        
        Menus.disable()
        #Set own menu buttons' and checkboxs' status to enabled
        global playBtn; playBtn = pgmenu.Button.modify(playBtn, (playBtn[0][0], playBtn[0][1]), (playBtn[0][2], playBtn[0][3]), playBtn[1], 'enabled')
        global settingsBtn; settingsBtn = pgmenu.Button.modify(settingsBtn, (settingsBtn[0][0], settingsBtn[0][1]), (settingsBtn[0][2], settingsBtn[0][3]), settingsBtn[1], 'enabled')
        global levelsBtn; levelsBtn = pgmenu.Button.modify(levelsBtn, (levelsBtn[0][0], levelsBtn[0][1]), (levelsBtn[0][2], levelsBtn[0][3]), levelsBtn[1], 'enabled')
    
    def create():
        global playBtn; playBtn = pgmenu.Button.create(((win_w / 2) - ((win_w / 9) / 2), (win_h / 2) - ((win_h / 9) / 2)), (max(win_w, win_h) / 9, max(win_w, win_h) / 9), MenuPlay)
        global settingsBtn; settingsBtn = pgmenu.Button.create(((win_w / 1.5) - ((win_w / 13) / 2), (win_h / 1.95) - ((win_h / 13) / 2)), (max(win_w, win_h) / 13, max(win_w, win_h) / 13), Settings.MenuChange)
        global levelsBtn; levelsBtn = pgmenu.Button.create(((win_w / 3) - ((win_w / 13) / 2), (win_h / 1.95) - ((win_h / 13) / 2)), (max(win_w, win_h) / 13, max(win_w, win_h) / 13), LevelSelection.MenuChange)
        
    def draw(surf):
        surf.blit(pygame.transform.scale(pgmenu.image('title.png'), (1661 / (1920 / win_w), 179 / (1080 / win_h))), (win_w / 19.2, win_h / 14.4))
        
        pgmenu.Button.draw(surf, playBtn, (50, 200, 50), text = 'Play', text_color = (255, 191, 0), text_font = 'Pusab.otf', outline_width = round(((win_w + win_h) / 100)), outline_color = (170, 210, 255), border_radius = 200)
        pgmenu.Button.draw(surf, settingsBtn, (50, 200, 50), text = 'Settings', text_color = (255, 191, 0), text_font = 'Pusab.otf', font_size = 30, outline_width = round(((win_w + win_h) / 100)), outline_color = (170, 210, 255), border_radius = 200)
        pgmenu.Button.draw(surf, levelsBtn, (50, 200, 50), text = 'Levels', text_color = (255, 191, 0), text_font = 'Pusab.otf', outline_width = round(((win_w + win_h) / 100)), outline_color = (170, 210, 255), border_radius = 200)
    
    
class Pause:
    def __init__(self):
        pass
    
    def create():
        pass
    
    def draw():
        pass


class LevelSelection:
    def __init__(self):
        pass
    
    def MenuChange():
        global menu_change; menu_change = 2
        
        print(menu_change)
        
        Menus.disable()
        #Set own menu buttons' and checkboxs' status to enabled
        global backBtn; backBtn = pgmenu.Button.modify(backBtn, (backBtn[0][0], backBtn[0][1]), (backBtn[0][2], backBtn[0][3]), backBtn[1], 'enabled')
    
    def create():
        pass
    
    def draw(surf):
        pgmenu.Button.draw(surf, backBtn, (50, 200, 50), text = 'Back', text_color = (255, 191, 0), text_font = 'Pusab.otf', outline_width = round(((win_w + win_h) / 100)), outline_color = (170, 210, 255), border_radius = 200)


class CharacterSelection:
    def __init__(self):
        pass
    
    def create():
        pass
    
    def draw():
        pass


class Settings:
    def __init__(self):
        pass
    
    def MenuChange():
        global menu_change; menu_change = 3
        
        Menus.disable()
        #Set own menu buttons' and checkboxs' status to enabled
        global backBtn; backBtn = pgmenu.Button.modify(backBtn, (backBtn[0][0], backBtn[0][1]), (backBtn[0][2], backBtn[0][3]), backBtn[1], 'enabled')
        
        global fpsCheckbox; fpsCheckbox = pgmenu.Checkbox.modify(fpsCheckbox, (fpsCheckbox[0][0], fpsCheckbox[0][1]), fpsCheckbox[0][2], fpsCheckbox[1], pgmenu.Checkbox.get(fpsCheckbox), 'enabled')
        global colCheckbox; colCheckbox = pgmenu.Checkbox.modify(colCheckbox, (colCheckbox[0][0], colCheckbox[0][1]), colCheckbox[0][2], colCheckbox[1], pgmenu.Checkbox.get(colCheckbox), 'enabled')
    
    def create():
        global fpsCheckbox; fpsCheckbox = pgmenu.Checkbox.create(((win_w / 2.5) - ((win_w / 16) / 2), (win_h / 2.1) - ((win_h / 16) / 2)), round(max(win_w, win_h) / 48), state = True, status = 'disabled')
        global colCheckbox; colCheckbox = pgmenu.Checkbox.create(((win_w / 2.5) - ((win_w / 16) / 2), (win_h / 1.8) - ((win_h / 16) / 2)), round(max(win_w, win_h) / 48), state = False, status = 'disabled')
    
    def draw(surf):
        pgmenu.Button.draw(surf, backBtn, (50, 200, 50), text = 'Back', text_color = (255, 191, 0), text_font = 'Pusab.otf', outline_width = round(((win_w + win_h) / 100)), outline_color = (170, 210, 255), border_radius = 200)
        
        pgmenu.Checkbox.draw(surf, fpsCheckbox, (50, 200, 50), text = 'Show FPS Counter', text_color = (255, 191, 0), text_font = 'Pusab.otf', border_radius = round(max(win_w, win_h) / 187))
        pgmenu.Checkbox.draw(surf, colCheckbox, (50, 200, 50), text = 'Show Collisions', text_color = (255, 191, 0), text_font = 'Pusab.otf', border_radius = round(max(win_w, win_h) / 187))