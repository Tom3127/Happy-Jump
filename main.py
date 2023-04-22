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
    platform = pygame.image.load("assets/platform.png").convert_alpha()
    start_surface = pygame.image.load("assets/start_surface.png").convert_alpha()
    character_img = pygame.image.load("assets/character.png").convert_alpha() # default image for the character
    character_left = pygame.image.load("assets/character_left.png") # character moving left image
    character_right = pygame.image.load("assets/character_right.png") # character moving right image

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
    platform_count = 10
    for i in range(platform_count):
        platforms_x = [0, 100, 200, 300, 400, 500]
        platforms_y = []
        platforms = []
        platform_x = random.choice(platforms_x)
        platform_y = random.randint(0, 1000)
        
        

    #start surface
    start_surface_x = 0
    start_surface_y = 950

    #main loop function
    clock = pygame.time.Clock()
    program = True
    game = True # POZDĚJI UPRAVIT NA SWITCH (po přidání před-herního menu s tlačítky atd.)

    while program:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                program = False
                pygame.quit()

        # character moving
        keys = pygame.key.get_pressed() # getting dictionary of key inputs

        if keys[pygame.K_LEFT] and char_pos_x > 0: 
            char_pos_x -= 8
            character = character_left
        

        if keys[pygame.K_RIGHT] and char_pos_x < screen_width - char_width:
            char_pos_x += 8
            character = character_right

        if keys[pygame.K_UP]:
            jumping = True
        
        for current_platform_y in platforms_y:
            if char_bottom == current_platform_y:
                jumping = True
        
        if jumping:     # adding gravity to the character
            char_pos_y -= y_velocity
            y_velocity -= y_gravity
            if y_velocity < -jump_height:
                jumping = False
                y_velocity = jump_height

        screen.fill(bg_clr)
        screen.blit(start_surface, (start_surface_x, start_surface_y))
        screen.blit(platform, (platform_x, platform_y))
        screen.blit(character, (char_pos_x, char_pos_y))

        character = character_img # setting back the default image for character

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60) #frames per second

