import pygame, sys
from variables import *
from Laser_class import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('../graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 400
        self.speed = 5
        self.lasers = pygame.sprite.Group()
        self.life = 3

    def player_input(self):
        keys = pygame.key.get_pressed()
        #if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.rect.y >= floor_dino and not self.low and self.alive :
        #    self.gravity = -15
        if keys[pygame.K_LEFT] and self.rect.left > 20:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT] and self.rect.x < screen_width -80:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()



    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True


    def shoot(self):
        self.lasers.add(Laser(self.rect.center,1))

    def damaged(self):
        self.life -=1

    def alive(self):
        return self.life > 0

    def update(self):
        self.player_input()
        self.recharge()
        self.lasers.update()