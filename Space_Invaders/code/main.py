import random

import pygame, sys
from variables import *
from Player_class import *
from Block_class import *
from Alien_class import *
from random import choice
from Laser_class import *

class Game:
    def __init__(self,high_score):

        self.win = False
        self.loose = False
        # Set up a player in the game
        player_sprite = Player((screen_width/2,screen_height-10))
        self.player  = pygame.sprite.GroupSingle(player_sprite)

        #Health bar and score
        self.live_surface = pygame.image.load("../graphics/player.png").convert_alpha()
        self.live_x_start_pos = screen_width - ( self.live_surface.get_size()[0] * 2 +20)
        self.score = 0
        self.high_score = high_score
        self.font = pygame.font.Font("../font/Pixeltype.ttf",20)

        #Win Loose text
        self.font2 = pygame.font.Font("../font/Pixeltype.ttf", 50)


        # Set up a obstacle in the game
        self.shape = shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.block_amount = 4
        self.obstacle_x_positions = [ num *(screen_width)/self.block_amount for num in range(self.block_amount)]
        self.create_multiple_obstacles(*self.obstacle_x_positions, x_start= 40,y_start = 480)

        # Set up the aliens
        self.aliens = pygame.sprite.Group()
        self.alien_setup(rows = 6, cols = 8)
        self.alien_lasers = pygame.sprite.Group()
        self.direction = 1
        self.down = 0

        # Set up the extra
        self.extra = pygame.sprite.Group()

    def create_obstacle(self, x_start,y_start,offset_x):
        for row_index,row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = Block(self.block_size,(241,79,80),x,y)

                    self.blocks.add(block)
    def create_multiple_obstacles(self,*offset,x_start,y_start):
        for offset_x in offset:
            self.create_obstacle(x_start,y_start,offset_x)

    def alien_setup(self,rows,cols,x_distance = 60,y_distance=48, x_offset = 70 , y_offset = 100):
        for row_index, row in enumerate(range(rows)):
            for col_index,col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset
                if row_index == 0 or row_index == 1:
                    alien_sprite = Alien('green', x, y)
                elif row_index == 2 or row_index == 3:
                    alien_sprite = Alien('yellow', x, y)
                else:
                    alien_sprite = Alien('red', x, y)

                self.aliens.add(alien_sprite)

    def alien_position_checker(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.left < 0:
                self.direction = 1
                self.down = down
            elif alien.rect.right >= screen_width:
                self.direction = -1
                self.down = down


    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center,-1)
            self.alien_lasers.add(laser_sprite)

    # Laser Collisions
    def collision_checks(self):
        # Player Lasers
        if self.player.sprite.lasers:
            # Check if collides
            for laser in self.player.sprite.lasers:
                # Check if collides with a block
                if pygame.sprite.spritecollide(laser,self.blocks,True):
                    laser.kill()
                # Check if collides with an alien
                aliens_hit = pygame.sprite.spritecollide(laser,self.aliens,True)
                if aliens_hit:
                    laser.kill()
                    for alien in aliens_hit:
                        self.score += alien.value

                # Check if collides with an extra alien
                extra_hit = pygame.sprite.spritecollide(laser, self.extra, True)
                if extra_hit:
                    laser.kill()
                    for extra in extra_hit:
                        self.score += extra.value
        if self.alien_lasers:
            # Check if collides
            for laser in self.alien_lasers:
                if pygame.sprite.spritecollide(laser,self.blocks,True):
                    laser.kill()
                if pygame.sprite.spritecollide(laser,self.player,False):
                    laser.kill()
                    self.player.sprite.damaged()
        if self.aliens:
            # Check if collides
            for alien in self.aliens:
                pygame.sprite.spritecollide(alien, self.blocks, False)

                if pygame.sprite.spritecollide(alien, self.player, False):
                    alien.kill()
                    self.player.sprite.damaged()
        else:
            self.win = True
        if self.player.sprite.life <= 0:
            self.loose = True

    def display_lives(self):
        for live in range(self.player.sprite.life -1):
            x = self.live_x_start_pos + (live * (self.live_surface.get_size()[0] +10))
            screen.blit(self.live_surface,(x,1))

    def display_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

        score_surface = self.font.render(f'HI  {self.high_score}  {self.score}', False, 'white')
        score_rect = score_surface.get_rect(center=(60, 20))
        screen.blit(score_surface, score_rect)

    def display_win(self):
        win_surface = self.font2.render(f'You Win! Press enter to Restart', False, 'white')
        win_rect = win_surface.get_rect(center=(screen_width/2, screen_height/2))
        screen.blit(win_surface, win_rect)

    def display_loose(self):
        loose_surface = self.font2.render(f'You Loose! Press enter to Restart', False, 'white')
        loose_rect = loose_surface.get_rect(center=(screen_width/2, screen_height/2))
        screen.blit(loose_surface, loose_rect)


    def run(self):
        self.player.sprite.lasers.draw(screen)
        self.alien_position_checker()
        self.player.update()
        self.aliens.update(self.direction,self.down)
        self.alien_lasers.update()
        self.down = 0
        self.extra.update()
        self.collision_checks()
        self.player.draw(screen)
        self.blocks.draw(screen)
        self.aliens.draw(screen)
        self.alien_lasers.draw(screen)
        self.extra.draw(screen)
        self.display_lives()
        self.display_score()
        # update all sprite groups
        # draw all sprite groups

if __name__ == '__main__':
    pygame.init()
    higher_score = 0
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    game = Game(0)

    ALIENEXTRA = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIENEXTRA, random.randint(4000, 10000))
    ALIENLASER = pygame.USEREVENT + 2
    pygame.time.set_timer(ALIENLASER, 700)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ALIENLASER:
                game.alien_shoot()
            if event.type == ALIENEXTRA:
                game.extra.add(Extra())
            if event.type == pygame.KEYDOWN:
                if(game.loose or game.win) and event.key == pygame.K_SPACE:
                    game = Game(higher_score)

        if game.loose:
            game.display_loose()
        elif game.win:
            game.display_win()
        else:
            screen.fill((30,30,30))
            game.run()

        higher_score = game.high_score


        pygame.display.flip()
        clock.tick(60)
