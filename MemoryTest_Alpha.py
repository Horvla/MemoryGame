import pygame
import random
import time

pygame.init()

window_height = 24 * 40
window_width = 20 * 40   # 40 = lungimea/latimea patratelului de caiet

window = pygame.display.set_mode((window_width, window_height)) # Window Size
pygame.display.update()
pygame.display.set_caption("Memory Game Test") # Title

game_in_progress = True # Game in progress

square_dimension = 220
square_x_position = 0
square_y_position = 0


COLOR_TEST = (124, 124, 124)

while game_in_progress:
    for event in pygame.event.get():

        if event.type == pygame.QUIT: # In momentul apasarii "X" din
            game_in_progress = False               # fereastra, se iese din joc

        else:
            pygame.draw.rect(window, COLOR_TEST, [50, 160, square_dimension, square_dimension])
            pygame.draw.rect(window, COLOR_TEST, [290, 160, square_dimension, square_dimension])
            pygame.draw.rect(window, COLOR_TEST, [530, 160, square_dimension, square_dimension])
            # ^ primele 3 patrate ^

            pygame.draw.rect(window, COLOR_TEST, [50, 400, square_dimension, square_dimension])
            pygame.draw.rect(window, COLOR_TEST, [290, 400, square_dimension, square_dimension])
            pygame.draw.rect(window, COLOR_TEST, [530, 400, square_dimension, square_dimension])
            # ^ urmatoarele 3 patrate ^

            pygame.draw.rect(window, COLOR_TEST, [50, 640, square_dimension, square_dimension])
            pygame.draw.rect(window, COLOR_TEST, [290, 640, square_dimension, square_dimension])
            pygame.draw.rect(window, COLOR_TEST, [530, 640, square_dimension, square_dimension])
            # ^ ultimele 3 patrate ^

            pygame.display.update()   

            

"""
pygame.quit()
quit()
"""