import pygame
from variables import *

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.alive = True
        self.reborn = False
        self.low = False
        # Sprites
        self.stand_sprite = pygame.image.load('../graphics/dino_stand.png').convert_alpha()
        walk1_sprite = pygame.image.load('../graphics/dino_walk1.png').convert_alpha()
        walk2_sprite = pygame.image.load('../graphics/dino_walk2.png').convert_alpha()

        self.walk = [walk1_sprite, walk2_sprite]

        low1_sprite = pygame.image.load('../graphics/dino_low1.png').convert_alpha()
        low2_sprite = pygame.image.load('../graphics/dino_low2.png').convert_alpha()

        self.down = [low1_sprite, low2_sprite]
        self.dino_index = 0


        self.dead_sprite = pygame.image.load('../graphics/dino_dead.png').convert_alpha()
        # Rectangles and physics
        self.rect_up = self.stand_sprite.get_rect(topleft=(y_dino, floor_dino))
        self.rect_down = low1_sprite.get_rect(bottomleft=(y_dino, floor_low_dino))

        self.rect = self.rect_up
        self.gravity = 0

        # Dino images
        self.image = self.walk[self.dino_index]

    def player_input(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.rect.y >= floor_dino and not self.low and self.alive :
            self.gravity = -15
        if keys[pygame.K_DOWN] and self.rect.y >= floor_dino and self.alive:
            self.low = True
            self.rect = self.rect_down
        elif not keys[pygame.K_DOWN] :
            self.low = False
            self.rect = self.rect_up



    def apply_gravity(self):

        self.gravity +=1
        self.rect.y += self.gravity     #Apply gravity to dino
        if self.rect.y >= floor_dino:
            if self.low:
                self.rect.y = floor_low_dino
            else:
                self.rect.y = floor_dino

    def dino_animation(self):

        if not self.alive:

            self.image = self.dead_sprite

        elif self.low:
            self.dino_index += 0.2
            if self.dino_index >= len(self.walk):
                self.dino_index = 0
            self.image = self.down[int(self.dino_index)]

        else:
            if self.rect.y < floor_dino:
                self.image = self.stand_sprite
            else:
                self.dino_index += 0.2
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
            self.low = False
            self.reborn = True
        else:
            self.alive = True
            if self.reborn:
                self.reborn = False
                self.rect.y = floor_dino

        self.player_input()
        self.apply_gravity()
        self.dino_animation()