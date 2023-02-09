import pygame

list_of_collisions = []
list_of_collisions_enemy = []
list_of_collisions_jump_pad = []
list_of_collisions_jump_orb = []

level_height = 0

gravity_offset = 0
player_pos = gravity_offset
level_move_speed = 0
orb_save = 0

Y_SPEED = 0

not_touching_ground = False

#When death or win occurs, will reset all physics and level pos to 0, to get updated later by LevelPlay and cube_physics
def reset_attempt():
    global gravity_offset, player_pos, level_move_speed, Y_SPEED, not_touching_ground

    level_move_speed = 0
    gravity_offset = -5
    player_pos = -5
    Y_SPEED = 0
    not_touching_ground = False

#Set collision lists to the ones given by LevelCreate (passed down by LevelPlay)
def set_collisions_lists(*col_lists):
    global list_of_collisions, list_of_collisions_enemy, list_of_collisions_jump_pad, list_of_collisions_jump_orb, level_height
    
    list_of_collisions = col_lists[0]
    list_of_collisions_enemy = col_lists[1]
    list_of_collisions_jump_pad = col_lists[2]
    list_of_collisions_jump_orb = col_lists[3]
    #Get level height (based on the given number being the lowest bloc)
    level_height = col_lists[-1]

#Set given vars to given input; used by LevelPlay to signify a jump, or a fall
def gravity_set_vars(yspeed, falling_bool):
        global gravity_offset, player_pos, level_move_speed, orb_save, Y_SPEED, not_touching_ground

        Y_SPEED = yspeed
        not_touching_ground = falling_bool

#Main physics system
def cube_physics(delta_time, level_move, orb):
    global gravity_offset, player_pos, level_move_speed, orb_save, Y_SPEED, not_touching_ground, list_of_collisions, list_of_collisions_enemy, list_of_collisions_jump_pad, list_of_collisions_jump_orb, level_height
    
    reset = False
    level_move_speed = level_move
    orb_save = orb

    #Gravity 'function', calculates player position on the y axis
    if not_touching_ground:
        #As it gets called every frame, will slowly change player y by current Y_SPEED
        gravity_offset -= round(Y_SPEED * (delta_time / 5), 3)
        #Change Y_SPEED by a negative number, making the player go in a curve (e.g. 6.5 to -9)
        if Y_SPEED != -(round(9 * (delta_time / 5), 3)): #or -9
            Y_SPEED = round(Y_SPEED - 0.02 * delta_time, 3)

    #Keep player from going too high (off the screen), by changing the level pos, but not the players
        if not gravity_offset < -320:
            player_pos = gravity_offset

        if not orb_save == 50:
            orb_save += 1

    #Hitbox collision detection
    #Set each hitbox (player's sides) to new player pos (x and y axis)
    player_rect_bottom = pygame.Rect(300 + 5 - level_move_speed, (level_height - 100) + gravity_offset + 80, 90, 20)
    player_rect_right = pygame.Rect(300 + 90 - level_move_speed, (level_height - 100) + gravity_offset, 10, 70)
    player_rect_top = pygame.Rect(300 + 5 - level_move_speed, (level_height - 100) + gravity_offset, 90, 10)

    #Detect if the player's bottom is touching platforms => stop falling
    if player_rect_bottom.collidelist(list_of_collisions) != -1:
        not_touching_ground = False
    else:
        if not not_touching_ground:
            gravity_set_vars(0, True)

    #Detect if the player's right side is touching platforms => reset (kill)
    if player_rect_right.collidelist(list_of_collisions) != -1:
        reset_attempt()
        reset = True
    #Detect if the player's top side is touching platforms => reset (kill)
    if player_rect_top.collidelist(list_of_collisions) != -1:
        reset_attempt()
        reset = True

    #Detect if the player's bottom side is touching enemies (spikes) => reset (kill)
    if player_rect_bottom.collidelist(list_of_collisions_enemy) != -1:
        reset_attempt()
        reset = True
    #Detect if the player's right side is touching enemies (spikes) => reset (kill)
    if player_rect_right.collidelist(list_of_collisions_enemy) != -1:
        reset_attempt()
        reset = True
    #Detect if the player's top side is touching enemies (spikes) => reset (kill)
    if player_rect_top.collidelist(list_of_collisions_enemy) != -1:
        reset_attempt()
        reset = True

    #Detect if the player's bottom side is touching jump pad => jump
    if player_rect_bottom.collidelist(list_of_collisions_jump_pad) != -1:
        gravity_set_vars(10, True)
    #Detect if the player's bottom side is touching jumb orb => jump
    if player_rect_bottom.collidelist(list_of_collisions_jump_orb) != -1:
        if orb_save % 50 != 0:
            gravity_set_vars(6.5, True)

    return gravity_offset, player_pos, not_touching_ground, orb_save, reset