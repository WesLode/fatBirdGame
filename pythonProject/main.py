import pygame
import configs
import assets
from pythonProject.object.background import Background

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()

Background(sprites)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    sprites.draw(screen)

    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()