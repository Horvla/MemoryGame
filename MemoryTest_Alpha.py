import pygame
import random
import time
import sys

from pygame.locals import *

FPS = 60

window_height = 800 #24 * 40
window_width =  700 #20 * 40   # 40 = lungimea/latimea patratelului de caiet

square_size = 200
gap_size    =  20

time_out = 10

# Culori alese prin: htmlcolorcodes.com
# Color              R    G    B
background_color = (39, 139, 218) # albastru deschis

color            = (21,  95, 190) # albastru inchis

square_color     = []
for i in range(9):
    square_color.append(color)

x = int((window_width  - (3 * square_size) - 2 * gap_size))/2
y = int((window_height - (3 * square_size) - 2 * gap_size))/2 + 2 * gap_size  #am lasat spatiu sus pt nivel, vieti etc  

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

S.extend([S0,S1,S2,S3,S4,S5,S6,S7,S8])

def Buttons():
    for i in range (9):
        pygame.draw.rect(display, square_color[i], S[i])
    
def Close():
    pygame.quit()
    quit()
    
def CheckClose():
    for event in pygame.event.get(QUIT):
        Close()
    """
    for event in pygame.event.get(KEYUP): 
        if event.key == K_ESCAPE:
            Close() 
        pygame.event.post(event)
    """

def ClickButton(x,y):
    # collidepoint returneaza o variabila booleana, daca s-a apasat in interiorul unui patrat
    for i in range (9):
        if S[i].collidepoint( (x,y) ):
            return S[i]
    return None

def Flash(square,speed = 100):
    # color = (0,0,0)
    for i in range (9):
        if square == S[i]:
            color = square_color[i]
            sound = beep

    original_display = display.copy()
    flash_surface = pygame.Surface((square_size,square_size))
    flash_surface = flash_surface.convert_alpha()
    R = 21
    G = 95
    B = 250
    flash_color = (R, G, B)
    
    CheckClose()
    
    sound.play()
    display.fill(flash_color,square)
    pygame.display.update()
    pygame.time.wait(speed)
    display.fill(color,square)
    pygame.display.update()

def main():
    global FPS_clock, display, font, beep

    pygame.init()
    FPS_clock = pygame.time.Clock()
    display = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Test")

    # De scris font:
    # -------------

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

        # Display score:
        # -------------

        CheckClose()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos # pos returneaza coordonatele punctului -> (x,y)
                current_click = ClickButton(mouse_x,mouse_y) # stocheaza butonul pe care s-a apasat
        
        
        if not input_await:
            pygame.display.update()
            pygame.time.wait(1000)
            model.append(random.choice(S))  #vector care stocheaza patratele generate aleator, in ordinea generarii lor
            for square in model:
                Flash(square)
                pygame.time.wait(500)
            input_await = True
        
        else:
            if current_click and current_click == model[step]:
                Flash(current_click)
                step += 1
                last_click = time.time()

                if step == len(model):
                    score += 1
                    input_await = False
                    step = 0

            elif(current_click and current_click != model[step]) or (step != 0 and time.time() - time_out > last_click):
                model = []
                step = 0
                input_await = False
                score = 0
                pygame.time.wait(500)

        pygame.display.update()
        FPS_clock.tick(FPS)

if __name__ == '__main__':
    main()
    