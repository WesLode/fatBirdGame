import pygame.sprite

import configs
from layer import Layer
import assets
import configs
from object.background import Background
from object.floor import Floor
from object.column import Column


class Bird(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.PLAYER
        self.images = [
            assets.get_sprite("redbird-upflap"),
            assets.get_sprite("redbird-midflap"),
            assets.get_sprite("redbird-downflap"),
        ]
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(-50, 50))
        self.mask = pygame.mask.from_surface(self.image)
        self.flap = 0

        super().__init__(*groups)

    def update(self):
        # self.images.insert(0, self.images.pop())
        self.images.append(self.images.pop(0))
        self.image = self.images[0]

        self.flap += configs.GRAVITY
        self.rect.y += self.flap

        if self.rect.x < 50:
            self.rect.x += 3

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.flap = 0
            self.flap -= 6

    def check_collision(self, sprites):
        for sprite in sprites:
            if (
                    (type(sprite) is Column or type(sprite) is Floor)
                    # type(sprite) is Background
                    and
                    sprite.mask.overlap(self.mask, (self.rect.x - sprite.rect.x, self.rect.y - sprite.rect.y))
                    or
                    self.rect.bottom < 0
            ):
                return True
        return False


