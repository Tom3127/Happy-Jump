import pygame
import random

pygame.init()
pygame.font.init()

if __name__ == "__main__":

    screen_width = 1920
    screen_height = 1080
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption("PyJump")
    window_icon = pygame.image.load("assets/window_icon.png")
    pygame.display.set_icon(window_icon)
    
    bg_clr = (2, 152, 219)

    # images
    coin_img = pygame.image.load("assets/coin.png").convert_alpha() # image of the coins
    start_surface = pygame.image.load("assets/start_surface.png").convert_alpha() # image of the ground
    character_img = pygame.image.load("assets/player.png").convert_alpha() # default image for the player
    character_left = pygame.image.load("assets/player_left.png").convert_alpha() # player moving left image
    character_right = pygame.image.load("assets/player_right.png").convert_alpha() # player moving right image
    character_debug = pygame.image.load("assets/player_debug.png").convert_alpha() # image of debug player

    #start surface
    start_surface_x = 0
    start_surface_y = 1030
    start_surface_height = start_surface.get_height()

    #player
    char_width = character_img.get_width()
    char_height = character_img.get_height()
    char_pos_x = 922.5
    char_pos_y_default = screen_height - char_height - start_surface_height
    char_pos_y = char_pos_y_default
    player = character_img
    player_speed = 15

    y_gravity = 1.5
    jump_height = 48
    y_velocity = jump_height
    jumping = False

    #coin generation
    coin_width = coin_img.get_width()
    coin_height = coin_img.get_height()
    coin_count = 20
    list_of_coin_dicts = []
    for i in range(coin_count):
        coin_x = random.randrange(0, 1870, 50)
        coin_y = random.randrange(200, 900, 50)
        coin = {'x':coin_x, 'y':coin_y}
        list_of_coin_dicts.append(coin)

    # score counter
    score = 0
    font = pygame.font.SysFont('Comic Sans MS', 75)
    
    # main loop 
    clock = pygame.time.Clock()
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                quit()

        # player movement
        keys = pygame.key.get_pressed() # getting key inputs
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and char_pos_x > 0: 
            char_pos_x -= player_speed
            player = character_left

        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and char_pos_x < screen_width - char_width:
            char_pos_x += player_speed
            player = character_right

        if keys[pygame.K_UP] or keys[pygame.K_SPACE] or keys[pygame.K_w]:
            jumping = True

        if jumping: 
            char_pos_y -= y_velocity
            y_velocity -= y_gravity
            if y_velocity < -jump_height:
                jumping = False
                y_velocity = jump_height
        screen.fill(bg_clr)
        screen.blit(start_surface, (start_surface_x, start_surface_y))
        # getting player rect
        character_rect = pygame.Rect(char_pos_x, char_pos_y, char_width, char_height)
        
        # drawing coins and checking collision
        for dict_in_list in list_of_coin_dicts:
            coin_rect = pygame.Rect(dict_in_list['x'], dict_in_list['y'], coin_width, coin_height)
            screen.blit(coin_img, coin_rect)

            if character_rect.colliderect(coin_rect):
                coin_index = list_of_coin_dicts.index(dict_in_list)
                score += 1
                list_of_coin_dicts.pop(coin_index)

        # displaying player
        screen.blit(player, character_rect)
        player = character_img # setting back the default image for player

        text_surface = font.render(f'Score: {score}', False, (255, 255, 255))

        screen.blit(text_surface, (30,0))
        # detecting if there are any coins left
        if not(list_of_coin_dicts):
            for i in range(coin_count):
                coin_x = random.randrange(0, 1870, 50)
                coin_y = random.randrange(200, 905, 50)
                coin = {'x':coin_x, 'y':coin_y}
                list_of_coin_dicts.append(coin)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60) # FPS

