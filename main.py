import pygame

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
    character = pygame.image.load("assets/character.png").convert_alpha()

    #character
    char_width = character.get_width()
    char_pos_x = 215
    char_pos_y = 880

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
        # ARROW inputs (moving on x axis)
        keys = pygame.key.get_pressed()

        if char_pos_x > 0:
            if keys[pygame.K_LEFT]:
                    char_pos_x -= 8
        if char_pos_x < screen_width - char_width:
            if keys[pygame.K_RIGHT]:
                    char_pos_x += 8

        screen.fill(bg_clr)
        screen.blit(start_surface, (0, 950))
        screen.blit(character, (char_pos_x, char_pos_y))
        screen.blit(platform, (100, 150))

        pygame.display.flip()
        pygame.display.update()
        clock.tick(120) #frames per second

