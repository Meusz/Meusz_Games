import pygame
from sys import exit
floor_dino = 250
floor_cactus = 300
pygame.init()
screen = pygame.display.set_mode((800,400))
text_font = pygame.font.Font('../font/Pixeltype.ttf', 50)
screen.fill("White")
pygame.display.set_caption("T-Rex Runner")

clock = pygame.time.Clock() #Variable to control time and frame rate
foreground = pygame.image.load('../graphics/foreground.png').convert_alpha()
cactus = pygame.image.load('../graphics/cactus.png').convert_alpha()
cactus_rect = cactus.get_rect(bottomleft = (800,floor_cactus))

dino_surface = pygame.image.load('../graphics/dino_stand.png').convert_alpha()
dino_rect = dino_surface.get_rect(topleft =(0,floor_dino))
dino_gravity = 0


text_surface = text_font.render('GAME OVER',False,'Grey')
text_rect = text_surface.get_rect(topleft= (300,50))
score_surface = text_font.render('Mygame',False,'Grey')
score_rect = score_surface.get_rect(center=(700,50))

while True:
    print(dino_rect.y)
    #Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and dino_rect.y == floor_dino:
                dino_gravity = -15





    #Attach one surface into another
    screen.blit(foreground, (0, 0))

    screen.blit(cactus, cactus_rect)
    cactus_rect.x -=5
    if (cactus_rect.right <= 0):
        cactus_rect.x = 800


    screen.blit(score_surface, score_rect)

    #Dino
    dino_rect.y += dino_gravity
    screen.blit(dino_surface, dino_rect)

    if (dino_rect.y < floor_dino):
        dino_gravity += 1
    else:
        dino_gravity = 0

    # draw all our elements
    # update everything
    if dino_rect.colliderect(cactus_rect):
        screen.blit(text_surface,text_rect)


    pygame.display.update()
    clock.tick(60) #60 times per second
