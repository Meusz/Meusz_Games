from variables import *
import pygame

def display_score(screen,score_font,high_score,start_time,game_active):
    current_time = int(pygame.time.get_ticks()/100) - start_time
    if not game_active and high_score < current_time:
        high_score = current_time
    score_surface = score_font.render(f'HI  {high_score}  {current_time}', False, 'Black')
    score_rect = score_surface.get_rect(center=(700, 50))
    screen.blit(score_surface, score_rect)

    return high_score



def colision_sprite(dino,obstacles_rect_list):
    if pygame.sprite.spritecollide(dino.sprite,obstacles_rect_list,False):
        return False
    else:
        return True


