import pygame
import constants

pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 32)

def display_score(screen, x, y):
    score_img = font.render(f"Total Score: {str(constants.SCORE)}", True, [255, 255, 255])
    screen.blit(score_img, (x, y))