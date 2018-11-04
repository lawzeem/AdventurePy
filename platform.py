import pygame, sys, time

from pygame.locals import *
from Scripts.UltraColor import *
from Scripts.textures import *

pygame.init()

def set_window():
    global window, window_height, window_width, window_title
    window_height = 600
    window_width = 400
    window_title = "AdventurePy"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_height, window_width), pygame.HWSURFACE | pygame.DOUBLEBUF)



def redrawGameWindow():
    pygame.display.update()

set_window()

clock = pygame.time.Clock()
# RUN
isRunning = True

run = [pygame.transform.scale(pygame.image.load('graphics\\megaman\\tile003.png'), (200, 200)), pygame.transform.scale(pygame.image.load('graphics\\megaman\\tile004.png'), (200, 200)), pygame.transform.scale(pygame.image.load('graphics\\megaman\\tile005.png'), (200, 200)) ]
jump = [pygame.transform.scale(pygame.image.load('graphics\\megaman\\tile006.png'), (200, 200)), pygame.transform.scale(pygame.image.load('graphics\\megaman\\tile006.png'), (200, 200)), pygame.transform.scale(pygame.image.load('graphics\\megaman\\tile010.png'), (200, 200))]
enemy_bat = [pygame.transform.scale(pygame.image.load('graphics\\enemy_bat\\tile013.png'), (150, 150)), pygame.transform.scale(pygame.image.load('graphics\\enemy_bat\\tile014.png'), (150, 200)), pygame.transform.scale(pygame.image.load('graphics\\enemy_bat\\tile015.png'), (150, 150))]
bg = pygame.image.load('graphics\\pethero-bg1.gif')
bg = pygame.transform.scale(bg, (600,400))
e = 0
y = 250
# def enemy(e):

megaman = 1
x = 0

def Hero(megamane):
    if (megamane == 1):
        window.blit(bg, (x, 0))

        window.blit(run[0], (20, 150))
        megamane+=1

    if (megamane == 2):
        window.blit(bg, (x, 0))

        window.blit(run[1], (20, 150))
        megamane += 1

    if (megamane == 3):
        window.blit(bg, (x, 0))

        window.blit(run[2], (20, 150))
        megamane = 1
    else:
        megamane += 1


while isRunning:
    for event in pygame.event.get():
        if event.type == QUIT:
            isRunning = False

    rel_x = x % bg.get_rect().width
    window.blit(bg, (rel_x - bg.get_rect().width, 0))
    if rel_x < window_width + 200:
        window.blit(bg, (rel_x, 0))
    x-=10
    # megaman = 1
    # Hero(megaman)
    if (megaman == 1):
        window.blit(bg, (x, 0))

        window.blit(run[0], (20, 150))

    if (megaman == 2):
        window.blit(bg, (x, 0))

        window.blit(run[1], (20, 150))

    if (megaman == 3):
        window.blit(bg, (x, 0))

        window.blit(run[2], (20, 150))
        megaman = 1
    else:
        megaman += 1


    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        window.blit(bg, (rel_x - bg.get_rect().width, 0))
        if rel_x < window_width + 200:
            window.blit(bg, (rel_x, 0))

        jmp = 0
        # x-=4
        if (jmp == 0):
            # window.blit(bg, (0, 0))
            jmp += 1
            window.blit(jump[0], (20, 30))


        if (jmp == 1):
            # window.fill(Color.Azure)
            window.blit(jump[1], (20, 30))

        if (jmp == 2):
            # window.fill(Color.Azure)
            window.blit(jump[2], (20, 30))
            jmp = 0
        else:
            jmp += 1
    # enemy(e)
    if e == 0:
        window.blit(enemy_bat[0], (y, 160))
    if e == 1:
        window.blit(enemy_bat[1], (y, 160))
    if e == 2:
        window.blit(enemy_bat[2], (y, 160))
        e = 0
    else:
        e+=1
        y-=20

    pygame.display.update()

    clock.tick(27)
    # redrawGameWindow()

pygame.quit()
sys.exit()

