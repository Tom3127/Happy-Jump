import pygame
import os

pygame.init()

screen_width = 500
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Happy Jump")
window_icon = pygame.image.load("assets/window_icon.png")
pygame.display.set_icon(window_icon)

bg_clr = (2, 152, 219)

fps = 60

# images
platform_img = pygame.image.load("assets/platform.png").convert_alpha()

# platforms


def draw_window():
    screen.fill(bg_clr)
    pygame.display.flip()
    pygame.display.update()

def platform_generate():
    screen.blit(platform_img, (200, 500))

#main loop
def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    platform_generate()

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()