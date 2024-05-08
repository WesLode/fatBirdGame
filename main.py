import pygame
import configs
import assets
from object.background import Background
from object.bird import Bird
from object.column import Column
from object.floor import Floor
from object.game_over_message import GameOverMessage
from object.game_start_message import GameStartMessage
from object.score import Score

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
column_create_event = pygame.USEREVENT
running = True
game_over = False
game_started = False

assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()


def create_sprites():
    Background(0, sprites)
    Background(1, sprites)
    Floor(0, sprites)
    Floor(1, sprites)
    return Bird(sprites), GameStartMessage(sprites), Score(sprites)


bird, game_start_message, score = create_sprites()


Column(sprites)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == column_create_event:
            Column(sprites)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_started and not game_over:
                game_started = True
                game_start_message.kill()
                pygame.time.set_timer(column_create_event, 1500)
            if event.key == pygame.K_ESCAPE and game_over:
                game_over = False
                game_started = False
                sprites.empty()
                bird, game_start_message, score = create_sprites()
            if not game_over:
                bird.handle_event(event)

        bird.handle_event(event)

    screen.fill("purple")

    sprites.draw(screen)

    if game_started and not game_over:
        sprites.update()

    if bird.check_collision(sprites):
        game_started = False
        game_over = True
        GameOverMessage(sprites)
        pygame.time.set_timer(column_create_event, 0)

    for sprite in sprites:
        if type(sprite) is Column and sprite.is_passed():
            score.value += 1

    print(score.value)

    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit()
