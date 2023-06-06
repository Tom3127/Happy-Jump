import pygame
import random

pygame.init()
pygame.font.init()

if __name__ == "__main__":
# IMAGES

    # window
    window_icon = pygame.image.load("assets/window_icon.png")

    # game images
    coin_img = pygame.image.load("assets/coin.png") # image of the coins
    ground = pygame.image.load("assets/ground.png") # image of the ground
    player = pygame.image.load("assets/player.png") # default image for the player
    player_left = pygame.image.load("assets/player_left.png") # player moving left image
    player_right = pygame.image.load("assets/player_right.png") # player moving right image
    player_debug = pygame.image.load("assets/player_debug.png") # image of debug player

# WINDOW SETUP
    # window properties
    screen_width = 1920
    screen_height = 1080
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption("PyJump")
    pygame.display.set_icon(window_icon)

# INGAME FEATURES
    # background color
    bg_clr = (2, 152, 219)

    # ground
    ground_x = 0
    ground_y = 1030
    ground_height = ground.get_height()

    #player
    player_width = player.get_width()
    player_height = player.get_height()
    player_x = screen_width / 2 - player_width / 2
    player_y = screen_height - player_height - ground_height
    player_img = player
    player_speed = 15
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    y_gravity = 1.5
    jump_height = 48
    y_velocity = jump_height
    jumping = False

    #coin generation
    coin_width = coin_img.get_width()
    coin_height = coin_img.get_height()
    coin_count = 20
    coins = []
    def coin_gen():
        for i in range(coin_count):
            coin_x = random.randrange(0, 1870, 62)
            coin_y = random.randrange(200, 900, 62)
            coin = {'x':coin_x, 'y':coin_y}
            coins.append(coin)

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

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_x > 0: 
            player_x -= player_speed
            player = player_left

        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_x < screen_width - player_width:
            player_x += player_speed
            player = player_right

        if keys[pygame.K_UP] or keys[pygame.K_SPACE] or keys[pygame.K_w]:
            jumping = True

        if jumping: 
            player_y -= y_velocity
            y_velocity -= y_gravity
            if y_velocity < -jump_height:
                jumping = False
                y_velocity = jump_height

        screen.fill(bg_clr)
        screen.blit(ground, (ground_x, ground_y))
        # getting player rect
        character_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        
        # drawing coins and checking collision
        for dict_in_list in coins:
            coin_rect = pygame.Rect(dict_in_list['x'], dict_in_list['y'], coin_width, coin_height)
            screen.blit(coin_img, coin_rect)

            if character_rect.colliderect(coin_rect):
                coin_index = coins.index(dict_in_list)
                score += 1
                coins.pop(coin_index)

        # displaying player
        screen.blit(player, character_rect)
        player = player # setting back the default image for player

        text_surface = font.render(f'Score: {score}', False, (255, 255, 255))

        screen.blit(text_surface, (30,0))
        # detecting if there are any coins left
        if not(coins):
            for i in range(coin_count):
                coin_x = random.randrange(0, 1870, 50)
                coin_y = random.randrange(200, 905, 50)
                coin = {'x':coin_x, 'y':coin_y}
                coins.append(coin)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60) # FPS
