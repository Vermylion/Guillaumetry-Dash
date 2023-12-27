import pygame

list_of_collisions = []
list_of_collisions_enemy = []
list_of_collisions_jump_pad = []
list_of_collisions_jump_pad_gravity = []
list_of_collisions_jump_orb = []
list_of_collisions_jump_orb_gravity = []
draw_collisions = False

#Function to draw main platform
def draw_platform(surf, xpos, ypos):
    #Create new surface (100x100, transparent)
    platform_surf = pygame.Surface((100, 100), pygame.SRCALPHA)

    #Draw platform to it (border and inside)
    square_rect = pygame.Rect(5, 5, 90, 90)
    border_rect = pygame.Rect(0, 0, 100, 100)

    pygame.draw.rect(platform_surf, (255, 255, 255), border_rect)
    pygame.draw.rect(platform_surf, (0, 0, 0), square_rect)

    #Create collision (rectangle)
    collision_rect = pygame.Rect(xpos, ypos, 100, 100)
    global list_of_collisions
    list_of_collisions.append(collision_rect)

    #Draw or 'blit' platform to given surface
    surf.blit(platform_surf, (xpos, ypos))
    #Also draw collision's contour if prompt is true
    if draw_collisions:
        pygame.draw.rect(surf, (255, 0, 0), collision_rect, 2)

#Function to draw small platform
def draw_small_platform(surf, xpos, ypos):
    #Create new surface (100x100, transparent)
    small_platform_surf = pygame.Surface((100, 100), pygame.SRCALPHA)

    #Draw the small platform to it (border and inside)
    rectangle_rect = pygame.Rect(5, 30, 90, 40)
    border_rect = pygame.Rect(0, 25, 100, 50)

    pygame.draw.rect(small_platform_surf, (255, 255, 255), border_rect)
    pygame.draw.rect(small_platform_surf, (0, 0, 0), rectangle_rect)
    
    #Create collision (rectangle)
    collision_rect = pygame.Rect(xpos, ypos + 25, 100, 50)
    global list_of_collisions
    list_of_collisions.append(collision_rect)

    #Draw or 'blit' small platform to given surface
    surf.blit(small_platform_surf, (xpos, ypos))
    #Also draw collision's contour if prompt is true
    if draw_collisions:
        pygame.draw.rect(surf, (255, 0, 0), collision_rect, 2)

#Function to draw the spikes
def draw_spike(surf, xpos, ypos, rotation = 0, size = 'normal'):
    #Set spike size based on given input (small or normal)
    if size == 'small':
        height = 70
        col_x, col_y = 70, 30
    if size == 'normal':
        height = 15
        col_x, col_y = 30, 70

    #Create new surface (100x100, transparent)
    rotatable_surf = pygame.Surface((100, 100), pygame.SRCALPHA)

    #Draw the spike (inside and border) using polygon function (add points)
    pygame.draw.polygon(surface = rotatable_surf, color = (255, 170, 170), points = [(0, 100), (50, height - 10), (100, 100)])
    pygame.draw.polygon(surface = rotatable_surf, color = (0, 0, 0), points = [(10, 95), (50, height), (90, 95)])
    #Rotate the spike to given degree (0 or 90 or 180 or 270)
    rotatable_surf = pygame.transform.rotate(rotatable_surf, rotation)

    #Create collision based on size and rotation
    if rotation == 0:
        collision_rect = pygame.Rect(xpos + 30, ypos + col_x, 40, col_y)
    elif rotation == 90:
        collision_rect = pygame.Rect(xpos + col_x, ypos + 30, col_y, 40)
    elif rotation == 180:
        collision_rect = pygame.Rect(xpos + 30, ypos, 40, col_y)
    elif rotation == 270:
        collision_rect = pygame.Rect(xpos, ypos + 30, col_y, 40)
    global list_of_collisions_enemy
    list_of_collisions_enemy.append(collision_rect)

    #Draw or 'blit' spike to given surface
    surf.blit(rotatable_surf, (xpos, ypos))
    #Also draw collision's contour if prompt is true
    if draw_collisions:
        pygame.draw.rect(surf, (255, 0, 0), collision_rect, 2)

#Function to draw the jump orbs
def draw_orb(surf, xpos, ypos):
    #Create new surface (100x100, transparent)
    orb_surf = pygame.Surface((100, 100), pygame.SRCALPHA)

    #Draw the orb to it (outer ring and inside circle)
    pygame.draw.circle(orb_surf, (255, 220, 0), (50, 50), 45, 5)
    pygame.draw.circle(orb_surf, (255, 220, 0), (50, 50), 30)

    #Create collision (rectangle)
    collision_rect = pygame.Rect(xpos+ 10, ypos + 10, 80, 80)
    global list_of_collisions_jump_orb
    list_of_collisions_jump_orb.append(collision_rect)

    #Draw or 'blit' jump orb to given surface
    surf.blit(orb_surf, (xpos, ypos))
    #Also draw collision's contour if prompt is true
    if draw_collisions:
        pygame.draw.rect(surf, (255, 0, 0), collision_rect, 2)
        
def draw_gravity_orb(surf, xpos, ypos):
    #Create new surface (100x100, transparent)
    orb_surf = pygame.Surface((100, 100), pygame.SRCALPHA)

    #Draw the orb to it (outer ring and inside circle)
    pygame.draw.circle(orb_surf, (0, 220, 255), (50, 50), 45, 5)
    pygame.draw.circle(orb_surf, (0, 220, 255), (50, 50), 30)

    #Create collision (rectangle)
    collision_rect = pygame.Rect(xpos+ 10, ypos + 10, 80, 80)
    global list_of_collisions_jump_orb_gravity
    list_of_collisions_jump_orb_gravity.append(collision_rect)

    #Draw or 'blit' jump orb to given surface
    surf.blit(orb_surf, (xpos, ypos))
    #Also draw collision's contour if prompt is true
    if draw_collisions:
        pygame.draw.rect(surf, (255, 0, 0), collision_rect, 2)

#Function to draw jump pads
def draw_pad(surf, xpos, ypos, rotation = 0):
    #Create new surface (100x100, transparent)
    pad_surf = pygame.Surface((100, 100), pygame.SRCALPHA)

    #Draw an oval (cut in  half) to it
    pygame.draw.ellipse(pad_surf, (255, 150, 0), (0, 75, 100, 50))

    #Create collision (rectangle)
    if rotation == 0:
        collision_rect = pygame.Rect(xpos, ypos + 70, 100, 30)
    elif rotation == 90:
        collision_rect = pygame.Rect(xpos + 70, ypos, 30, 100)
    elif rotation == 180:
        collision_rect = pygame.Rect(xpos, ypos, 100, 30)
    elif rotation == 270:
        collision_rect = pygame.Rect(xpos, ypos, 30, 100)
    
    global list_of_collisions_jump_pad
    list_of_collisions_jump_pad.append(collision_rect)

    rotated_pad_surf = pygame.transform.rotate(pad_surf, rotation)
    #Draw or 'blit' jump pad to given surface
    surf.blit(rotated_pad_surf, (xpos, ypos))
    #Also draw collision's contour if prompt is true
    if draw_collisions:
        pygame.draw.rect(surf, (255, 0, 0), collision_rect, 2)
        
def draw_gravity_pad(surf, xpos, ypos, rotation = 0):
    #Create new surface (100x100, transparent)
    pad_surf = pygame.Surface((100, 100), pygame.SRCALPHA)

    #Draw an oval (cut in  half) to it
    pygame.draw.ellipse(pad_surf, (0, 220, 255), (0, 75, 100, 50))

    #Create collision (rectangle)
    if rotation == 0:
        collision_rect = pygame.Rect(xpos, ypos + 70, 100, 30)
    elif rotation == 90:
        collision_rect = pygame.Rect(xpos + 70, ypos, 30, 100)
    elif rotation == 180:
        collision_rect = pygame.Rect(xpos, ypos, 100, 30)
    elif rotation == 270:
        collision_rect = pygame.Rect(xpos, ypos, 30, 100)
    global list_of_collisions_jump_pad_gravity
    list_of_collisions_jump_pad_gravity.append(collision_rect)

    rotated_pad_surf = pygame.transform.rotate(pad_surf, rotation)
    #Draw or 'blit' jump pad to given surface
    surf.blit(rotated_pad_surf, (xpos, ypos))
    #Also draw collision's contour if prompt is true
    if draw_collisions:
        pygame.draw.rect(surf, (255, 0, 0), collision_rect, 2)

def draw_saw(surf, xpos, ypos):
    #Create new surface (100x100, transparent)
    saw_surf = pygame.Surface((100, 100), pygame.SRCALPHA)
    
    #Draw a circle to it (border and inside)
    pygame.draw.circle(saw_surf, (255, 170, 170), (50, 50), 50)
    pygame.draw.circle(saw_surf, (0, 0, 0), (50, 50), 45)

    #Create collision (rectangle)
    collision_rect = pygame.Rect(xpos + 10, ypos + 60, 80, 80)
    global list_of_collisions_enemy
    list_of_collisions_enemy.append(collision_rect)
    
    #Draw or 'blit' jump orb to given surface
    surf.blit(saw_surf, (xpos, ypos + 50))

    #Also draw collision's contour if prompt is true
    if draw_collisions:
        pygame.draw.rect(surf, (255, 0, 0), collision_rect, 2)

#Main function that reads level off of .txt, and calls each drawing function
def load_level(win_width, win_height):
    #Load level text doc, read the content, get total number of lines
    level_file = open('level.txt', 'r')
    lines = level_file.readlines()
    lvl_height = len(lines)
    lvl_length = len(max(lines, key=len))
    level_file.close()
    
    level_file = open('level.txt', 'r')
    level_layers = dict({})
    for x in range(lvl_height):
            level_layers[len(level_layers)] = level_file.readline().replace('\n', '')
    level_file.close()
    
    #Create level surface
    level = pygame.Surface((100 * lvl_length + 1000 + win_width, 100 * lvl_height + 310), pygame.SRCALPHA)
    xoffset = 1000
    yoffset = 10

    #Open level .txt, read it line by line
    for layer_nbr in level_layers:
        layer = level_layers[layer_nbr]
        #Depending on character, call of according function
        for tile in layer:
            if tile == '#':
                draw_platform(level, xoffset, yoffset)
            if tile == '-':
                draw_small_platform(level, xoffset, yoffset)
                
            if tile == 'S' or tile == 's':
                if tile == 'S': 
                    size = 'normal' 
                else: 
                    size = 'small'
                if len(layer) != 0:
                    print(layer, tile, layer.index(tile), layer_nbr, layer[layer.index(tile) - 1])
                              
                if len(layer) != 0 and layer[layer.index(tile) - 1] == '#':
                    draw_spike(level, xoffset, yoffset, 270, size)
                elif len(layer) >= layer.index(tile) + 2 and layer[layer.index(tile) + 1] == '#':
                    draw_spike(level, xoffset, yoffset, 90, size)
                elif layer_nbr != 0 and len(level_layers[layer_nbr - 1]) >= layer.index(tile) and (level_layers[layer_nbr - 1][layer.index(tile)] == '#' or level_layers[layer_nbr - 1][layer.index(tile)] == '-'):
                    draw_spike(level, xoffset, yoffset, 180, size)
                else:
                    draw_spike(level, xoffset, yoffset, 0, size)
                    
            if tile == 'o':
                draw_saw(level, xoffset, yoffset)
            if tile == 'O':
                draw_orb(level, xoffset, yoffset)
            if tile == '0':
                draw_gravity_orb(level, xoffset, yoffset)
            if tile == '_':
                if len(layer) != 0 and layer[layer.index(tile) - 1] == '#':
                    draw_pad(level, xoffset, yoffset, 270)
                elif len(layer) >= layer.index(tile) + 2 and layer[layer.index(tile) + 1] == '#':
                    draw_pad(level, xoffset, yoffset, 90)
                elif layer_nbr != 0 and len(level_layers[layer_nbr - 1]) >= layer.index(tile) and (level_layers[layer_nbr - 1][layer.index(tile)] == '#' or level_layers[layer_nbr - 1][layer.index(tile)] == '-'):
                    draw_pad(level, xoffset, yoffset, 180)
                else:
                    draw_pad(level, xoffset, yoffset, 0)
                    
            if tile == '=':
                print(len(layer), layer.index(tile) + 2)
                if len(layer) != 0 and layer[layer.index(tile) - 1] == '#':
                    draw_gravity_pad(level, xoffset, yoffset, 270)
                elif len(layer) >= layer.index(tile) + 2 and layer[layer.index(tile) + 1] == '#':
                    draw_gravity_pad(level, xoffset, yoffset, 90)
                elif layer_nbr != 0 and len(level_layers[layer_nbr - 1]) >= layer.index(tile) and (level_layers[layer_nbr - 1][layer.index(tile)] == '#' or level_layers[layer_nbr - 1][layer.index(tile)] == '-'):
                    draw_gravity_pad(level, xoffset, yoffset, 180)
                else:
                    draw_gravity_pad(level, xoffset, yoffset, 0)
                    
            if tile == ' ':
                pass
                
                #Change length by 100
            xoffset += 100

            #reset xoffset and add 100 to yoffset when changing lines
        yoffset += 100
        xoffset = 1000

    #Create floor of level (draw rect and collision rect)
    floorrect = pygame.Rect(0, 100 * lvl_height + 10, 100 * lvl_length + 1000 + win_width, 300)
    floor_rect = pygame.Rect(0, 100 * lvl_height + 10 - 1, 100 * lvl_length + 1000 + win_width, 300)
    list_of_collisions.append(floor_rect)

    #Draw floor rect along with white line
    pygame.draw.rect(level, (0, 0, 0, 128), floorrect)
    pygame.draw.line(level, (255, 255, 255), (0, 100 * lvl_height + 12), (100 * lvl_length + 1000 + win_width, 100 * lvl_height + 12), 5)
    #Also draw collision's contour if prompt is true
    if draw_collisions:
        pygame.draw.rect(level, (255, 0, 0), floor_rect, 1)

    #Import player image and scale it to 100x100
    player = pygame.image.load('player.png')
    player = pygame.transform.scale(player, (100, 100))

    #Create player's collision boxes for all 4 sides
    player_rect_bottom = pygame.Rect(300 + 5, (yoffset - 100) + 80, 90, 20)
    player_rect_right = pygame.Rect(300 + 90, (yoffset - 100) + 20, 10, 60)
    player_rect_left = pygame.Rect(300, (yoffset - 100) + 5, 10, 90) #Not using it
    player_rect_top = pygame.Rect(300 + 5, (yoffset - 100), 90, 20)

    #Function to draw player's collisions
    def draw_player_collisions():
        player_rect_bottom_draw = pygame.Rect(5, 80, 90, 20)
        player_rect_right_draw = pygame.Rect(90, 20, 10, 60)
        player_rect_left_draw = pygame.Rect(0, 5, 10, 90)
        player_rect_top_draw = pygame.Rect(5, 0, 90, 20)

        pygame.draw.rect(player, (0, 255, 0), player_rect_bottom_draw, 5)
        pygame.draw.rect(player, (0, 0, 255), player_rect_right_draw, 5)
        #pygame.draw.rect(player, (0, 0, 255), player_rect_left_draw, 5)
        pygame.draw.rect(player, (255, 0, 0), player_rect_top_draw, 5)
    
    #Also draw collision's contour if prompt is true
    if draw_collisions:
        draw_player_collisions()

    return level, player, player_rect_bottom, player_rect_right, player_rect_top, yoffset, lvl_length, list_of_collisions, list_of_collisions_enemy, list_of_collisions_jump_pad, list_of_collisions_jump_pad_gravity, list_of_collisions_jump_orb, list_of_collisions_jump_orb_gravity
