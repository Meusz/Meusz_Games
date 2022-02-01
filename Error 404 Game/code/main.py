import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
screen.fill("White")
pygame.display.set_caption("1º screen")

clock = pygame.time.Clock() #Variable to control time and frame rate
dino_surface = pygame.image.load('../graphics/dino_stand.png')
dino_surface = pygame.transform.scale(dino_surface, (100, 100))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Attach one surface into another
    screen.blit(dino_surface,(0,0))

    # draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(60) #60 times per second
