import pygame
from random import choice
from variables import *

class Alien(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        super().__init__()
        file_path= '../graphics/' + color + '.png'
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = (x,y))

    def update(self,direction,down):
        self.rect.x += direction
        self.rect.y += down

class Extra(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../graphics/extra.png')
        self.direction = choice((-1,1))
        if self.direction == -1:
            self.rect = self.image.get_rect(center = (screen_width +50 ,50 ))
        else:
            self.rect = self.image.get_rect(center=(-50, 50))

    def update(self):
        self.rect.x += 3 * self.direction