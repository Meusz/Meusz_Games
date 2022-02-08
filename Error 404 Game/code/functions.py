from variables import *
#from main import *
import pygame

def display_score(screen,score_font,high_score,start_time,game_active):
    current_time = int(pygame.time.get_ticks()/100) - start_time
    if not game_active and high_score < current_time:
        high_score = current_time
    score_surface = score_font.render(f'HI  {high_score}  {current_time}', False, 'Black')
    score_rect = score_surface.get_rect(center=(700, 50))
    screen.blit(score_surface, score_rect)

    return high_score

def obstacle_movement(screen,obstacles_rect_list):
    if obstacles_rect_list:
        for obstacle in obstacles_rect_list:
            obstacle[1].x -= 5
        obstacle_draw(screen, obstacles_rect_list)

def obstacle_draw(screen,obstacles_rect_list):
    if obstacles_rect_list:
        for obstacle in obstacles_rect_list:
            screen.blit(obstacle[0],obstacle[1])

def colision(dino_rect,obstacles_rect_list):
    if obstacles_rect_list:
        for obstacle in obstacles_rect_list:
            if dino_rect.colliderect(obstacle[1]):
                return True
    return False


