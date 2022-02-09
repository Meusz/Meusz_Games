import pygame
from variables import *
from random import randint

class Pterodactyl(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


        pterodactyl1 = pygame.image.load('../graphics/pterodactyl1.png').convert_alpha()
        pterodactyl2 = pygame.image.load('../graphics/pterodactyl2.png').convert_alpha()
        self.pterodactyl_index = 0
        self.pterodactyl = [pterodactyl1, pterodactyl2]

        # variables
        self.image = self.pterodactyl[self.pterodactyl_index]
        self.rect = self.image.get_rect(bottomleft=(posicion, floor_pterodactyl) )

    def pterodactyl_animation(self):
        self.pterodactyl_index += 0.1
        if self.pterodactyl_index >= len(self.pterodactyl):
            self.pterodactyl_index = 0
        self.image = self.pterodactyl[int(self.pterodactyl_index)]

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.rect.x -= 5
        self.pterodactyl_animation()
        self.destroy()

