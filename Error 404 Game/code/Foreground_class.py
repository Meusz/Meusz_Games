import pygame
from variables import *
from random import randint

class Foreground(pygame.sprite.Sprite):
    def __init__(self,posicion):
        super().__init__()


        foreground_surface = pygame.image.load('../graphics/foreground.png').convert_alpha()
        self.foreground_index = 0

        # variables
        self.image = foreground_surface
        self.rect = self.image.get_rect(topleft=(posicion, 0))


    def destroy(self):
        if self.rect.topleft <= (-1200, 0):
            self.kill()

    def update(self):
        self.rect.x -= 5
        self.destroy()
