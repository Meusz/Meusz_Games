import pygame
from variables import *
from random import randint

class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        type = randint(1,3)
        if type == 1:
            self.image = pygame.image.load('../graphics/cactus.png').convert_alpha()
        if type == 2:
            self.image = pygame.image.load('../graphics/cactus2.png').convert_alpha()
        if type == 3:
            self.image = pygame.image.load('../graphics/cactus3.png').convert_alpha()

        self.rect = self.image.get_rect(bottomleft=(posicion, floor_cactus))

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.rect.x -= 5
        self.destroy()

