import pygame
import random
import time
import sys

from pygame.locals import *

FPS = 60

window_height = 24 * 40
window_width = 20 * 40   # 40 = lungimea/latimea patratelului de caiet

square_size = 220
gap_size    =  20

# Culori alese prin: htmlcolorcodes.com
# Color              R    G    B
background_color = (39, 139, 218) # albastru deschis

color            = (21,  95, 190) # albastru inchis
square_color     = []
for i in range(9):
    square_color.append(color)

x = int((window_width  - (2 * square_size) - gap_size))
y = int((window_height - (2 * square_size) - gap_size))

S = [] #vector care contine cele 9 patrate

# Prima linie de patrate - se pastreaza y
S0 = pygame.Rect(x                               , y, square_size, square_size)
S1 = pygame.Rect(x + square_size + gap_size      , y, square_size, square_size)
S2 = pygame.Rect(x + 2 * (square_size + gap_size), y, square_size, square_size)

# A doua linie de patrate 
S3 = pygame.Rect(x                               , y + square_size + gap_size, square_size, square_size)
S4 = pygame.Rect(x + square_size + gap_size      , y + square_size + gap_size, square_size, square_size)
S5 = pygame.Rect(x + 2 * (square_size + gap_size), y + square_size + gap_size, square_size, square_size)

# A treia linie de patrate
S6 = pygame.Rect(x                               , y + 2 * (square_size + gap_size), square_size, square_size)
S7 = pygame.Rect(x + square_size + gap_size      , y + 2 * (square_size + gap_size), square_size, square_size)
S8 = pygame.Rect(x + 2 * (square_size + gap_size), y + 2 * (square_size + gap_size), square_size, square_size)

S.append(S0)
S.append(S1)
S.append(S2)
S.append(S3)
S.append(S4)
S.append(S5)
S.append(S6)
S.append(S7)
S.append(S8)

def Buttons():
    pygame.draw.rect(display, square_color[0], S0)
    pygame.draw.rect(display, square_color[1], S1)
    pygame.draw.rect(display, square_color[2], S2)
    pygame.draw.rect(display, square_color[3], S3)
    pygame.draw.rect(display, square_color[4], S4)
    pygame.draw.rect(display, square_color[5], S5)
    pygame.draw.rect(display, square_color[6], S6)
    pygame.draw.rect(display, square_color[7], S7)
    pygame.draw.rect(display, square_color[8], S8)

def Close():
    pygame.quit()
    sys.exit()

def ClickButton(x,y):
    # collidepoint returneaza o variabila booleana, daca s-a apasat in interiorul unui patrat
    if   S0.collidepoint( (x,y) ):
        return square_color[0]
    elif S1.collidepoint( (x,y) ):
        return square_color[1]
    elif S2.collidepoint( (x,y) ):
        return square_color[2]
    elif S3.collidepoint( (x,y) ):
        return square_color[3]
    elif S4.collidepoint( (x,y) ):
        return square_color[4]
    elif S5.collidepoint( (x,y) ):
        return square_color[5]
    elif S6.collidepoint( (x,y) ):
        return square_color[6]
    elif S7.collidepoint( (x,y) ):
        return square_color[7]
    elif S8.collidepoint( (x,y) ):
        return square_color[8]    

def Flash(a):
    for i in range(9):
        if a == square_color[i]:
            square = S[i]

    original_display = display.copy()

    flash_color      = (163,182, 206)
    R, G, B          = flash_color


def main():
    global FPS_clock, display, font, beep

    pygame.init()
    FPS_clock = pygame.time.Clock()
    display = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Test")

    # De scris font
    # -----------

    beep = pygame.mixer.Sound("beep.ogg")

    # Variabile joc nou:
    model = []
    step = 0
    last_click = 0
    score = 0
    input_await = False

    game_in_progress = True

    while game_in_progress:

        current_click = None
        display.fill(background_color)
        Buttons()
        pygame.display.update()

        # Display score:
        # -------------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_in_progress = False
            elif event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos # pos returneaza coordonatele punctului -> (x,y)
                current_click = ClickButton(mouse_x,mouse_y) # stocheaza butonul pe care s-a apasat
        """
        if not input_await:
            pygame.display.update()
            pygame.time.wait(1000)
            model.append(random.choice(square_color))
            for button in model:
                # !!!
        else:
            if not current_click:
                continue
            elif current_click == model[step]:
                return 0
                # !!!
        return
        """

if __name__ == "__main__":
    main()