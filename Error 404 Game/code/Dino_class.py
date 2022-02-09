import pygame
from variables import *

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.alive = True
        self.reborn = False
        # Sprites
        self.stand_sprite = pygame.image.load('../graphics/dino_stand.png').convert_alpha()
        walk1_sprite = pygame.image.load('../graphics/dino_walk1.png').convert_alpha()
        walk2_sprite = pygame.image.load('../graphics/dino_walk2.png').convert_alpha()

        self.walk = [walk1_sprite, walk2_sprite]
        self.dino_index = 0

        self.dead_sprite = pygame.image.load('../graphics/dino_dead.png').convert_alpha()
        # Rectangles and physics
        self.rect = self.stand_sprite.get_rect(topleft=(y_dino, floor_dino))
        self.gravity = 0
        # Dino images
        self.image = self.walk[self.dino_index]

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.y >= floor_dino:
            self.gravity = -15

    def apply_gravity(self):
        self.gravity +=1
        self.rect.y += self.gravity
        if self.rect.y >= floor_dino:
            self.rect.y = floor_dino

    def dino_animation(self):

        if not self.alive:
            self.image = self.dead_sprite

        else:
            if self.rect.y < floor_dino:
                self.image = self.stand_sprite
            else:
                self.dino_index += 0.1
                if self.dino_index >= len(self.walk):
                    self.dino_index = 0
                self.image = self.walk[int(self.dino_index)]

    def dino_dead(self):
        self.alive = False

    def dino_alive(self):
        self.alive = True

    def update(self, game_active):
        if not game_active:
            self.alive = False
            self.reborn = True
        else:
            self.alive = True
            if self.reborn:
                self.reborn = False
                self.rect.y = floor_dino

        self.player_input()
        self.apply_gravity()
        self.dino_animation()