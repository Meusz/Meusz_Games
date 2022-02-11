import pygame
from sys import exit
from variables import *
from Dino_class import *
from Cactus_class import *
from Pterodactyl_class import *
from Foreground_class import *
from functions import *
from random import randint



pygame.init()
screen = pygame.display.set_mode((800, 400))
screen.fill("White")
pygame.display.set_caption("T-Rex Runner")


#Text Font
text_font = pygame.font.Font('../font/Pixeltype.ttf', 50)
score_font = pygame.font.Font('../font/Pixeltype.ttf', 30)

#Foreground
foreground = pygame.sprite.Group()
foreground.add(Foreground(0), Foreground(1200))


#Obstacles
obstacles_rect_list = pygame.sprite.Group()

#Dino
dino = pygame.sprite.GroupSingle()
dino.add(Dino())

#Text
restart_surface = pygame.image.load('../graphics/restart.png').convert_alpha()
restart_rect = restart_surface.get_rect(midbottom=(380, 150))

text_gameover_surface = text_font.render('GAME OVER', False, 'Grey')
text_gameover_rect = text_gameover_surface.get_rect(topleft=(300, 50))

clock = pygame.time.Clock()  # Variable to control time and frame rate

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1200)

while True:
    screen.fill("White")
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if not game_active and event.key == pygame.K_SPACE:
                game_active = True
                obstacles_rect_list.empty()
                start_time = int(pygame.time.get_ticks()/100)
        if game_active and event.type == obstacle_timer:
            #print(int(pygame.time.get_ticks()/100))
            if  int(pygame.time.get_ticks()/100) - start_time > 200:
                obstacle = randint(1, 2)
            else:
                obstacle = 1
            if obstacle ==1:
                obstacles_rect_list.add(Cactus())
            elif obstacle ==2:
                obstacles_rect_list.add(Pterodactyl())

    if game_active:
        # Attach one surface into another

        #Foreground

        foreground.draw(screen)
        foreground.update()
        if len(foreground) < 2 :
            foreground.add(Foreground(1200))

        # Collision
        game_active = colision_sprite(dino,obstacles_rect_list)


        # Dino
        dino.draw(screen)

        dino.update(game_active)

        #Obstacles
        obstacles_rect_list.draw(screen)
        obstacles_rect_list.update()

        # Score
        high_score = display_score(screen,score_font,high_score,start_time,game_active)
    else:
        foreground.draw(screen)
        screen.blit(text_gameover_surface, text_gameover_rect)
        screen.blit(restart_surface, restart_rect)
        obstacles_rect_list.draw(screen)
        dino.draw(screen)



    pygame.display.update()
    clock.tick(60)  # 60 times per second
