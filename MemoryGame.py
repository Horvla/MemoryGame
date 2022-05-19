import pygame
import random
from pygame.locals import *

# General settings:
FPS         =  30  # Frames per second
square_size =  200 # Pentru a schimba aria de joc propriu-zisa, se schimba variabila square_size ( Max. recomandat = 250 )
game_speed  =  500 # De aici se schimba viteza in care apar patratele in mod aleator

# Calcul automat al ferestrei de joc in functie de marimea patratului ( Ratio 7:8 )
gap_size      = square_size // 10  # Distanta dintre patrate
window_height = square_size * 4    # Inaltimea ferestrei de joc
window_width  = square_size * 3.5  # Latimea ferestrei de joc

# Culori alese prin: htmlcolorcodes.com

# Color                R    G    B
background_color = (  29,  40,  89) # albastru high

color            = (  21,  95, 190) # albastru med

text_color       = ( 249, 242,  58) # galben

# Lista care contine culorile corespunzatoare fiecarui patrat
square_color     = [] 
for i in range(9):
    square_color.append(color)

# Coordonatele initiale ale primului patrat
x = int((window_width  - (3 * square_size) - 2 * gap_size))/2
y = int((window_height - (3 * square_size) - 2 * gap_size))/2 + 2 * gap_size   

S = [] # Lista care contine cele 9 patrate descrise mai jos

# Prima linie de patrate
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

# Adaugare celor 9 patrate de tip rect in lista S
S.extend([S0,S1,S2,S3,S4,S5,S6,S7,S8])

# Functie care deseneaza butoanele <=> patratele
def Buttons():
    for i in range (9):
        pygame.draw.rect(display, square_color[i], S[i])

# Functie care inchide programul in momentul apelarii    
def Close():
    pygame.quit()
    quit()

# Functie care verifica apasarea lui X/ESC pentru a iesi din program in while-ul principal   
def CheckClose():
    for event in pygame.event.get(QUIT):
        Close()
    for event in pygame.event.get(KEYUP): 
        if event.key == K_ESCAPE:
            Close() 
        pygame.event.post(event)

# Functie care primeste ca argument coordonate si returneaza patratul pe care a fost apasat
def ClickButton(x,y):
    # Collidepoint returneaza o variabila booleana, daca s-a apasat in interiorul unui patrat
    for i in range (9):
        if S[i].collidepoint( (x,y) ):
            return S[i]
    return None

# Functie care schimba culoarea unui patrat ( ca argument ) si care reda un sunet
def Flash( square, speed = 100 ):

    for i in range (9):
        if square == S[i]:
            color = square_color[i]
            sound = beep

    R = 101
    G = 145
    B = 239

    flash_color = ( R, G, B ) # culoarea flash-ului in urma apasarii/repetarii modelului
    
    CheckClose()
    
    sound.play()
    display.fill( flash_color, square )
    pygame.display.update()
    pygame.time.wait( speed )
    display.fill( color, square )
    pygame.display.update()

# Functie care afiseaza mesaj la anumite coordonate si de o anumita culoare
def Message( message, coordinates, color):
    msg = font.render( message, True, color )
    display.blit( msg, coordinates )

# Functia principala a jocului
def main():
    global FPS_clock, display, font, beep

    pygame.init()
    FPS_clock = pygame.time.Clock()
    display = pygame.display.set_mode(( window_width, window_height ))
    pygame.display.set_caption("Memory Game")

    # Font:
    font = pygame.font.SysFont(None,square_size//4)

    # Sunetul in urma apasarii patratului:
    beep = pygame.mixer.Sound("beep.ogg")

    # Secventa corecta
    correct = pygame.mixer.Sound("correct.ogg")
    correct.set_volume(0.3)

    # Sfarsitul jocului
    endgame = pygame.mixer.Sound("endgame.ogg")
    endgame.set_volume(0.6)

    # Variabile joc nou:
    model = []
    step = 0
    score = 0
    high_score = 0
    attempts = 1 
    input_await = False
    game_in_progress = True

    while game_in_progress:

        current_click = None
        display.fill(background_color)
        Buttons()

        # Display score:
        score_display = font.render("Score: " + str(score), 1, text_color) 
        score_rectangle = ( gap_size, gap_size ) # Stanga sus
        display.blit( score_display, score_rectangle ) # Afiseaza in "drepunghiul" de scor, scorul

        # Display attempts:
        attempts_display = font.render("Attempts: " + str(attempts), 1, text_color) 
        attempts_rectangle = ( gap_size, 3 * gap_size) # Stanga sus, sub scor
        display.blit( attempts_display, attempts_rectangle ) 

        # Display high score in current run:
        high_score_display = font.render("High Score: " + str(high_score), 1, text_color) 
        high_score_rectangle = ( window_width - square_size - 2 * gap_size, 2 * gap_size ) # Dreapta sus
        display.blit( high_score_display, high_score_rectangle ) 
        
        CheckClose()

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONUP:

                mouse_x, mouse_y = event.pos # pos returneaza coordonatele punctului -> (x,y)
                current_click = ClickButton( mouse_x, mouse_y ) # Stocheaza butonul pe care s-a apasat
        
        
        if not input_await:

            pygame.display.update()
            pygame.time.wait(1000)
            model.append(random.choice(S))  # Lista care stocheaza patratele generate aleator, in ordinea generarii lor

            Message("Wait", [ 1.5 * square_size, 2 * gap_size ], text_color) 

            for square in model:

                Flash(square)
                pygame.time.wait(game_speed) 
                
            input_await = True

        else:

            if current_click and current_click == model[step]:

                Flash(current_click)
                step += 1

                if step == len(model):

                    score += 1
                    input_await = False
                    step = 0

                    encouragement = ["   Nice!", "   Good!", "  Super!", " Hurray!", "    Wow!", "   Cool!", "  Great!", "Not bad!", "Perfect!", "   Fine!", "   Okay!"]

                    pygame.time.wait(500)
                    Message(random.choice(encouragement), [ 1.4 * square_size, 2 * gap_size ], text_color)
                    correct.play()
                    pygame.display.update()
                    pygame.time.wait(1000) # Delay pentru urmatoarea secventa

            elif(current_click and current_click != model[step]):

                model = []
                step = 0
                input_await = False
                attempts += 1

                if score >= high_score:
                    high_score = score

                score = 0

                Message("Try again", [ 1.5 * ( square_size - gap_size ), 2 * gap_size ], text_color)
                endgame.play()
                pygame.display.update()
                pygame.time.wait(1000) # Delay pentru urmatoarea secventa, in cazul esuarii
                

        pygame.display.update()
        FPS_clock.tick(FPS)

if __name__ == '__main__':
    main()
