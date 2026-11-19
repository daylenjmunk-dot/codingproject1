import pygame
pygame.init()

WIDTH, HEIGHT = 512, 512
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test 1")

FPS = 60
CLOCK = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    SCREEN.fill((0, 0, 0))
    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()
