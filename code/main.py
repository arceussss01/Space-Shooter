import pygame

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True

# Surface
surf = pygame.Surface((100, 200))
surf.fill('orange')

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    # fill the window with a red color?
    display_surface.fill('darkgray')
    display_surface.blit(surf, (100,150))
    pygame.display.update()

pygame.quit()