import pygame
pygame.init()

WIDTH, HEIGHT = 256, 512
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

FPS   = 60
CLOCK = pygame.time.Clock()

tickSpeed = 1
timer     = 0

pygame.key.set_repeat(200)

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
    def update(self):
        pass
    def draw(self):
        pygame.draw.rect(SCREEN, self.colour, pygame.Rect(self.x, self.y, self.width, self.height))

hotBlock = Block(25.6 * 4, 25.6 * 2, 25.6, 25.6, (255, 255, 255))
blockMovable = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_a and blockMovable == True:
                hotBlock.x -= 25.6
            if event.key == pygame.K_d and blockMovable == True:
                hotBlock.x += 25.6

    SCREEN.fill((0, 0, 0))

    # Block Updating

    hotBlock.update()
    hotBlock.draw()

    timer += 1
    if timer >= 50:
        timer = 0
        if hotBlock.y <= HEIGHT - hotBlock.height:
            hotBlock.y += 25.6
        else:
            blockMovable = False

    # Updating

    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()
