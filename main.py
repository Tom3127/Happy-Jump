import pygame
import random

pygame.init()

if __name__ == "__main__":

    screen_width = 500
    screen_height = 1000
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Happy Jump")
    window_icon = pygame.image.load("assets/window_icon.png")
    pygame.display.set_icon(window_icon)

    bg_clr = (2, 152, 219)

    # images
    platform_img = pygame.image.load("assets/platform.png").convert_alpha()
    start_surface = pygame.image.load("assets/start_surface.png").convert_alpha()
    character_img = pygame.image.load("assets/character.png").convert_alpha() # default image for the character
    character_left = pygame.image.load("assets/character_left.png").convert_alpha() # character moving left image
    character_right = pygame.image.load("assets/character_right.png").convert_alpha() # character moving right image
    character_debug = pygame.image.load("assets/debug_character.png").convert_alpha()

    #character
    char_width = character_img.get_width()
    char_height = character_img.get_height()
    char_pos_x = 215
    char_pos_y = 880
    char_bottom = char_pos_y + char_height
    character = character_img

    y_gravity = 1
    jump_height = 30
    y_velocity = jump_height
    jumping = False

    #platform generation
    platform_count = 5
    list_of_platform_dicts = []
    for i in range(platform_count):
        x_pos_of_platforms = [0, 100, 200, 300, 400] # možné pozice platforem na ose x

        platform_x = random.choice(x_pos_of_platforms)
        platform_y = random.randrange(450, 950, 50)
        platform = {'x':platform_x, 'y':platform_y}
        list_of_platform_dicts.append(platform)

    
    #start surface
    start_surface_x = 0
    start_surface_y = 950

    #main loop function
    clock = pygame.time.Clock()
    program = True

    while program:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                program = False
                pygame.quit()

        # character moving
        keys = pygame.key.get_pressed() # getting key inputs

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and char_pos_x > 0: 
            char_pos_x -= 8
            character = character_left
        

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and char_pos_x < screen_width - char_width:
            char_pos_x += 8
            character = character_right

        if keys[pygame.K_UP] or keys[pygame.K_SPACE] or keys[pygame.K_w]:
            jumping = True
        
        
        if jumping: # adding jumping to the character
            char_pos_y -= y_velocity
            y_velocity -= y_gravity
            if y_velocity < -jump_height:
                jumping = False
                y_velocity = jump_height

        screen.fill(bg_clr)
        screen.blit(start_surface, (start_surface_x, start_surface_y))

        # drawing platforem
        for dict_in_list in list_of_platform_dicts:
            platform_rect = pygame.Rect(dict_in_list['x'], dict_in_list['y'], 100, 25)
            screen.blit(platform_img, platform_rect)
            
        # drawing character
        character_rect = pygame.Rect(char_pos_x, char_pos_y, 70, 70)
        screen.blit(character, character_rect)

        #collision
        if character_rect.colliderect(platform_rect):
            print("KOLIZE!!!!!!")

        character = character_img # setting back the default image for character

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60) # FPS

# OPRAVY
# 1) Kolize hráče funguje pouze pro první vygenerovanou plošinu, pro další potom ne. 
#   ---> potřeba opravit věci s Rect a get_rect() a jejich kolize