import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("1º screen")

clock = pygame.time.Clock() #Variable to control time and frame rate
test_surface = pygame.Surface((100,200)) #Display an image on the screen
test_surface.fill("Red")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Attach one surface into another
    screen.blit(test_surface,(0,0))

    # draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(60) #60 times per second
