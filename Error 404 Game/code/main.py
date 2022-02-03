import pygame
from sys import exit
from variables import *
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
foreground = pygame.image.load('../graphics/foreground.png').convert_alpha()

#Obstacles
cactus = pygame.image.load('../graphics/cactus.png').convert_alpha()
cactus_rect = cactus.get_rect(bottomleft=(800, floor_cactus))
cactus2 = pygame.image.load('../graphics/cactus2.png').convert_alpha()
cactus2_rect = cactus2.get_rect(bottomleft=(800, floor_cactus))
cactus3 = pygame.image.load('../graphics/cactus3.png').convert_alpha()
cactus3_rect = cactus3.get_rect(bottomleft=(800, floor_cactus))

obstacles_rect_list = []

#Dino
dino_surface = pygame.image.load('../graphics/dino_stand.png').convert_alpha()
dino_rect = dino_surface.get_rect(topleft=(y_dino, floor_dino))


dino_dead_surface = pygame.image.load('../graphics/dino_dead.png').convert_alpha()
dino_dead_rect = dino_surface.get_rect(topleft=(y_dino, floor_dino))

restart_surface = pygame.image.load('../graphics/restart.png').convert_alpha()
restart_rect = restart_surface.get_rect(midbottom=(380, 150))

text_gameover_surface = text_font.render('GAME OVER', False, 'Grey')
text_gameover_rect = text_gameover_surface.get_rect(topleft=(300, 50))
# score_surface = text_font.render('Mygame',False,'Grey')
# score_rect = score_surface.get_rect(center=(700,50))

clock = pygame.time.Clock()  # Variable to control time and frame rate

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,900)

while True:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if game_active and dino_rect.y == floor_dino and event.key == pygame.K_SPACE:
                dino_gravity = -15
            if not game_active and event.key == pygame.K_SPACE:
                game_active = True
                obstacles_rect_list = []
                start_time = int(pygame.time.get_ticks()/100)
        if game_active and event.type == obstacle_timer:
            obstacle = randint(1,3)
            position = randint(900,1100)
            if obstacle ==1:
                obstacles_rect_list.append( (cactus, cactus.get_rect(bottomleft=(position, floor_cactus))) )
            elif obstacle ==2:
                obstacles_rect_list.append( (cactus2,cactus2.get_rect(bottomleft=(position, floor_cactus))) )
            else:
                obstacles_rect_list.append( (cactus3,cactus3.get_rect(bottomleft=(position, floor_cactus))) )

    if game_active:
        # Attach one surface into another
        screen.blit(foreground, (0, 0))

        #Obstacle Movement
        obstacle_movement(screen, obstacles_rect_list)

        # Dino
        dino_rect.y += dino_gravity
        screen.blit(dino_surface, dino_rect)

        if (dino_rect.y < floor_dino):
            dino_gravity += 1
        else:
            dino_gravity = 0

        # Collision
        if colision(dino_rect,obstacles_rect_list):
            game_active = False
        high_score = display_score(screen,score_font,high_score,start_time,game_active)
    else:

        dino_dead_rect.y = dino_rect.y
        screen.blit(foreground, (0, 0))
        screen.blit(text_gameover_surface, text_gameover_rect)
        screen.blit(restart_surface, restart_rect)
        obstacle_draw(screen,obstacles_rect_list)
        screen.blit(dino_dead_surface, dino_dead_rect)


    pygame.display.update()
    clock.tick(60)  # 60 times per second
