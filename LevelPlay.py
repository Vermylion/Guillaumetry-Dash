import pygame

import Physics
import LevelCreate
import Physics

BGCOLOR = (0, 100, 170)

gravity_offset = 0
player_pos = gravity_offset
level_move_speed = 0
orb_save = 0

key_down = False
not_touching_ground = False

angle = 0

def load_level(win_w, win_h):
    global level, player, player_rect_bottom, player_rect_right, player_rect_top, level_height, level_length, list_of_collisions, list_of_collisions_enemy,  list_of_collisions_jump_pad, list_of_collisions_jump_orb, list_of_collisions_jump_orb_gravity
    
    #Import level, player and collisions from
    level, player, player_rect_bottom, player_rect_right, player_rect_top, level_height, level_length, list_of_collisions, list_of_collisions_enemy,  list_of_collisions_jump_pad, list_of_collisions_jump_pad_gravity, list_of_collisions_jump_orb, list_of_collisions_jump_orb_gravity = LevelCreate.load_level(win_w, win_h)
    player.convert_alpha()
    level_length = 100 * level_length + 1000 

    #Give Physics all current collision lists
    Physics.set_collisions_lists(list_of_collisions, list_of_collisions_enemy, list_of_collisions_jump_pad, list_of_collisions_jump_pad_gravity, list_of_collisions_jump_orb, list_of_collisions_jump_orb_gravity, level_height)

#Main function to run all code based on the level
def play_level(screen, event, delta_time, win_w, win_h):
    global not_touching_ground, orb_save, gravity_offset, player_pos, level, player, level_move_speed, level_height, level_length, key_down, angle

    #Detect key presses, so we can keep pressing down and sending jump inputs
    if event.type == 771:
        if event.text == ' ':
            if not not_touching_ground:
                Physics.gravity_set_vars(6.5, True)

    if event.type == 768:
        if event.key == pygame.K_UP:
            if not not_touching_ground:
                Physics.gravity_set_vars(6.5, True)
                
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == pygame.BUTTON_LEFT:
            if not not_touching_ground:
                Physics.gravity_set_vars(6.5, True)
                
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == pygame.BUTTON_LEFT:
            orb_save = 0  

    #Check phyics; import modified vars from Physics
    gravity_offset, player_pos, not_touching_ground, orb_save, reset, angle = Physics.cube_physics(delta_time, level_move_speed, orb_save)

    #Winning; if past the end of the level (length of level)
    if abs(level_move_speed) > level_length - 100:
        print('win')
        Physics.reset_attempt()
        reset = True

    if reset:
        level_move_speed = 0

    #Move level at set speed
    level_move_speed -= 0.8 * delta_time

    #Reset screen visuals
    #screen.fill(BGCOLOR)

    #Draw Player and Level on screen. If player's position is above -320, the level moves on the y axis instead of him
    if gravity_offset < -320:
        screen.blit(level, (level_move_speed, (win_h - (level_height - 5) - 290) - (gravity_offset + 320)))
        player_pos = player_pos
    else:
        screen.blit(level, (level_move_speed, (win_h - (level_height - 5) - 290)))
    
    #Rotate Player
    rotated_player = pygame.transform.rotate(player, Physics.angle)
    rect = rotated_player.get_rect(center = (300, (win_h - 385) + player_pos))
    
    screen.blit(rotated_player, (rect.x, rect.y + 50))