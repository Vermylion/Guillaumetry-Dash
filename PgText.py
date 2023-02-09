import pygame

def set_text(string, color, coordx, coordy, font, fontSize):
    font = pygame.font.Font(font, fontSize) 
    text = font.render(str(string), True, color)
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)

    return (text, textRect)