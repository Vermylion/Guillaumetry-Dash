import pygame
import math

button_collisions = []
inflate_btn = []

check_button_collisions = []
check_button_checked = []

textbox_collisions = []
textbox_selected = []
textbox_text = dict({})

mouse_down = False

class Text:
    def __init__(self):
        pass
    
    def set(string, color, coordx, coordy, font = 'freesansbold.ttf', fontSize = 30, CenterX = True, CenterY = True):
        font = pygame.font.Font(font, fontSize) 
        text = font.render(str(string), True, color)
        textRect = text.get_rect()
        textRect[0], textRect[1] = (coordx, coordy)
        
        if CenterX:
            textRect.centerx = coordx
        if CenterY:
            textRect.centery = coordy
        
        return (text, textRect)
    
    def write(surface, string, color, coordx, coordy, font = 'freesansbold.ttf', fontSize = 30, CenterX = True, CenterY = True):
        totalText = Text.set(string, color, coordx, coordy, font, fontSize, CenterX, CenterY)
        surface.blit(totalText[0], totalText[1])
        
        return totalText


class Button:
    def __init__(self, btn_rect, update):
        self.btn_rect = btn_rect
        self.update = update
        
    def __str__(self):
        return str([self.btn_rect, self.update])
    
    def default_update_func():
        print('Pressed')

    def create(coords = (0, 0), dimensions = (0, 0), update_func = default_update_func):
        btn_rect = pygame.Rect(coords[0], coords[1], dimensions[0], dimensions[1])
        global button_collisions; button_collisions.append([btn_rect, update_func])
        
        return [btn_rect, update_func]
    
    def draw(surface, button_rect, color = (0, 0, 0), image = None, text = None, text_color = (0, 0, 0), text_font = 'freesansbold.ttf', font_size = None, outline_width = 0, outline_color = (0, 0, 0), border_width = 0, border_radius = -1, border_top_left_radius = -1, border_top_right_radius = -1, border_bottom_left_radius = -1, border_bottom_right_radius = -1):
        if button_rect in inflate_btn:
            draw_rect = button_rect[0].inflate(button_rect[0][2] / 15, button_rect[0][3] / 15)
        else:
            draw_rect = button_rect[0]
        
        if image != None:
            btn_img = pygame.image.load(image).convert_alpha()
            btn_img = pygame.transform.scale(btn_img, (draw_rect[2], draw_rect[3]))
            
            surface.blit(btn_img, (draw_rect[0], draw_rect[1]))
        else:
            if outline_width > 0:
                outline_rect = pygame.Rect(round(draw_rect[0] - (outline_width / 2)), round(draw_rect[1] - (outline_width / 2)), draw_rect[2] + outline_width, draw_rect[3] + outline_width)
                pygame.draw.rect(surface, outline_color, outline_rect, border_width, border_radius, border_top_left_radius, border_top_right_radius, border_bottom_left_radius, border_bottom_right_radius)
            pygame.draw.rect(surface, color, draw_rect, border_width, border_radius, border_top_left_radius, border_top_right_radius, border_bottom_left_radius, border_bottom_right_radius)
            
        if text != None:
            if font_size == None:
                font_size = min(draw_rect[2], draw_rect[3])
                if font_size * len(text) > max(draw_rect[2], draw_rect[3]):
                    font_size = round(round(max(draw_rect[2], draw_rect[3]) / len(text)) - (0.05 * draw_rect[2])) * 2
            
            totalText = Text.set(text, text_color, (draw_rect[0] + round(draw_rect[2] / 2)), (draw_rect[1] + round(draw_rect[3] / 2)), text_font, font_size)
            surface.blit(totalText[0], totalText[1])
    
    def update(event):
        global button_collisions, inflate_btn, mouse_down
        
        for btn_props in button_collisions:
            x, y = pygame.mouse.get_pos()
            if btn_props[0].collidepoint(x, y):
                inflate_btn.append(btn_props)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT and not mouse_down:
                        mouse_down = True
                        btn_props[1]()
                
            elif len(inflate_btn) != 0 and btn_props in inflate_btn:
                del inflate_btn[inflate_btn.index(btn_props)]
                
            if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == pygame.BUTTON_LEFT and mouse_down:
                        mouse_down = False
                
                
class Checkbox:
    def __init__(self):
        pass
    
    def default_update_func():
        print('Clicked')
    
    def create(coords = (0, 0), size = 20, update_func = default_update_func, state = 'not_checked'):
        check_btn_rect = pygame.Rect(coords[0], coords[1], size, size)
        global check_button_collisions; check_button_collisions.append([check_btn_rect, update_func])
        
        if state == 'checked':
            check_button_checked.append([check_btn_rect, update_func])
        
        return [check_btn_rect, update_func]
    
    def draw(surface, check_button_rect, foreground = (0, 0, 0), background = (255, 255, 255), background_image = None, foreground_image = None, text = None, text_color = (0, 0, 0), text_font = 'freesansbold.ttf', font_size = None, outline_width = 0, outline_color = (0, 0, 0), border_width = 0, border_radius = -1, border_top_left_radius = -1, border_top_right_radius = -1, border_bottom_left_radius = -1, border_bottom_right_radius = -1):
        Button.draw(surface, check_button_rect, background, background_image, text = None, text_color = (0, 0, 0), text_font = 'freesansbold.ttf', font_size = None, outline_width = outline_width, outline_color = outline_color, border_width = border_width, border_radius = border_radius, border_top_left_radius = border_top_left_radius, border_top_right_radius = border_top_right_radius, border_bottom_left_radius = border_bottom_left_radius, border_bottom_right_radius = border_bottom_right_radius)
        
        if check_button_rect in check_button_checked:
            checked_rect = pygame.Rect(round(check_button_rect[0][0] + (0.15 * check_button_rect[0][2])), round(check_button_rect[0][1] + (0.15 * check_button_rect[0][3])), round(check_button_rect[0][2] - ((0.15 * check_button_rect[0][2]) * 2)), round(check_button_rect[0][3] - ((0.15 * check_button_rect[0][3]) * 2)))
            if foreground_image != None:
                check_btn_img = pygame.image.load(foreground_image).convert_alpha()
                check_btn_img = pygame.transform.scale(check_btn_img, (checked_rect[2], checked_rect[3]))
            
                surface.blit(check_btn_img, (checked_rect[0], checked_rect[1]))
            else:
                pygame.draw.rect(surface, foreground, checked_rect, border_radius = border_radius, border_top_left_radius = border_top_left_radius, border_top_right_radius = border_top_right_radius, border_bottom_left_radius = border_bottom_left_radius, border_bottom_right_radius = border_bottom_right_radius)
                
        if text != None:
            if font_size == None:
                font_size = check_button_rect[0][2]
            
            totalText = Text.set(text, text_color, check_button_rect[0][0] + check_button_rect[0][2] + (check_button_rect[0][2] / 2) + outline_width, check_button_rect[0][1] + (check_button_rect[0][2] / 2), text_font, font_size, False, True)
            surface.blit(totalText[0], totalText[1])
    
    def update(event):
        global check_button_collisions, check_button_checked, mouse_down
        
        for check_btn_props in check_button_collisions:
            x, y = pygame.mouse.get_pos()
            if check_btn_props[0].collidepoint(x, y):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT and not mouse_down:
                        mouse_down = True
                        
                        if check_btn_props not in check_button_checked:
                            check_button_checked.append(check_btn_props)
                        else:
                            del check_button_checked[check_button_checked.index(check_btn_props)]
                            
                        check_btn_props[1]()
                            
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == pygame.BUTTON_LEFT and mouse_down:
                        mouse_down = False
                        
    def get(checkbox_element):
        return checkbox_element in check_button_checked


class Textbox:
    def __init__(self):
        pass

    def create(coords = (0, 0), dimensions = (0, 0), text = ''):
        textbox_rect = pygame.Rect(coords[0], coords[1], dimensions[0], dimensions[1])
        global textbox_collisions; textbox_collisions.append([textbox_rect])

        global textbox_text; textbox_text[str(textbox_rect)] = text
        
        return [textbox_rect]

    def draw(surface, textbox_rect, color = (0, 0, 0), image = None, text_color = (0, 0, 0), text_font = 'freesansbold.ttf', font_size = 20, outline_width = 0, outline_color = (0, 0, 0), border_width = 0, border_radius = -1, border_top_left_radius = -1, border_top_right_radius = -1, border_bottom_left_radius = -1, border_bottom_right_radius = -1):
        Button.draw(surface, textbox_rect, color, image, text = None, text_color = (0, 0, 0), text_font = 'freesansbold.ttf', font_size = None, outline_width = outline_width, outline_color = outline_color, border_width = border_width, border_radius = border_radius, border_top_left_radius = border_top_left_radius, border_top_right_radius = border_top_right_radius, border_bottom_left_radius = border_bottom_left_radius, border_bottom_right_radius = border_bottom_right_radius)

        Text.write(surface, textbox_text[str(textbox_rect[0])], text_color, textbox_rect[0][0], textbox_rect[0][1] + (textbox_rect[0][3] / 2), text_font, font_size, False)
        
    
class BaseMenu(object):
    def __init__(self, BgColor, title, mainEvents):
        self.BgColor = BgColor
        self.title = title
        self.Widgets = mainEvents
        
    def __repr__(self):
        template = 'BaseMenu(BgColor={color}, Title={title}, Widgets={events})'
        return template.format(
            color = self.BgColor,
            title = self.title,
            events = self.Widgets
        )
            
    def create(bgColor, title, widgets, **kwargs):
        w = pygame.display.Info().current_w
        h = pygame.display.Info().current_h
        
        bgColor = bgColor
        titleSurf = title
        mainEvents = widgets
        
        titleOffsetX = kwargs.get('titleOffsetX', 0)
        titleOffsetY = kwargs.get('titleOffsetY', 0)
        
        list_of_vars = dict({})
        for i in mainEvents:
            options = ['button', (w / len(mainEvents) * (list(mainEvents).index(i) + 1) - 300, h / 2), (150, 75)]
            if len(mainEvents[i]) >= len(options):
                options = mainEvents[i]
                
            if options[0] == 'button':
                locals()[f'{i}'] = Button.create(*options)
            elif options[0] == 'checkbox':
                locals()[f'{i}'] = Checkbox.create(*options)
            list_of_vars[f'{i}'] = locals()[f'{i}']
            #print(locals()[f'{i}'])
        
        return BaseMenu(bgColor, title, list_of_vars)
    
    def draw():
        pass
        
    
def return_var(var):
    print(var)
    return list(var)

def text(txt):
    return Text.set(txt, (0, 0, 0), 0, 0)[0]

def image(img):
    img_surf = pygame.image.load(img).convert_alpha()
    return img_surf
    
def update(event):
    Button.update(event)
    
    Checkbox.update(event)
    
    
#menu = BaseMenu(
#    bgColor = (0, 0, 0, 128),
#    title = image('player.png'),
#    mainEvents = ['btn1', 'btn2', 'btn3']
#          )
#
#menu.btn1.widget('button')
#
#btn1_menu = menu.btn1.BaseMenu(
#    bg_color = (0, 0, 0, 128),
#    title = text('Hello'),
#    main_events = ['btn1', 'btn2', 'btn3']
#            )
