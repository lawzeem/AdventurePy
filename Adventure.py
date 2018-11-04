import pygame, sys, time

from pygame.locals import *
from Scripts.UltraColor import *
from Scripts.textures import *

pygame.init()

cSec = 0
cFrame = 0
FPS = 0

left = False
right = False
up = False
down = False

walkLeft = [pygame.image.load('graphics\\tile009.png'), pygame.image.load('graphics\\tile010.png'), pygame.image.load('graphics\\tile011.png')]
walkUp = [pygame.image.load('graphics\\tile000.png'), pygame.image.load('graphics\\tile001.png'), pygame.image.load('graphics\\tile002.png')]
walkDown = [pygame.image.load('graphics\\tile006.png'), pygame.image.load('graphics\\tile007.png'), pygame.image.load('graphics\\tile008.png')]
walkRight = [pygame.image.load('graphics\\tile003.png'), pygame.image.load('graphics\\tile004.png'), pygame.image.load('graphics\\tile005.png')]
bg = pygame.image.load('graphics\\grass-tile.png')
char = pygame.image.load('graphics\\tile007.png')
clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0

    def draw(self, window):
        if self.walkCount + 1 >= 9:
            self.walkCount = 0
        if self.left:
            window.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            window.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.up:
            window.blit(walkUp[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.down:
            window.blit(walkDown[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            window.blit(char, (self.x, self.y))

# x_char = 0
# y_char = 0
# width_char = 16
# height_char = 64
# vel = 5
# walkCount = 0

tile_size = 32

fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Arial.ttf", 20)

# Showing FPS
def show_fps():
    fps_overlay = fps_font.render(str(FPS), True, Color.Azure)
    window.blit(fps_overlay, (0, 0))

# Window
def set_window():
    global window, window_height, window_width, window_title
    window_height = 500
    window_width = 480
    window_title = "AdventurePy"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_height, window_width), pygame.HWSURFACE | pygame.DOUBLEBUF)

# Displaying FPS / Not really necessary
def fps():
    global cSec, cFrame, FPS
    if cSec == time.strftime("%S"):
        cFrame+=1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")

def redrawGameWindow():
    global walkCount
    # for x in range(0, 500, tile_size):
    #     for y in range(0, 480, tile_size):
    #         window.blit(bg, (x,y))
    # pygame.draw.rect(window, (255, 0, 0), (x_char, y_char, width_char, height_char))

    Hero.draw(window)
    pygame.display.update()

set_window()

# RUN
isRunning = True
Hero = player(50, 425, 16, 64)
while isRunning:
    clock.tick(27)
    # pygame.time.delay(15)
    for event in pygame.event.get():
        if event.type == QUIT:
            isRunning = False
    fps()

    window.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and Hero.x > Hero.vel:
        Hero.x-=Hero.vel
        Hero.left = True
        Hero.right = False
        Hero.up = False
        Hero.down = False
    elif keys[pygame.K_RIGHT] and Hero.x < window_width - Hero.width - Hero.vel:
        Hero.x+=Hero.vel
        Hero.left = False
        Hero.right = True
        Hero.up = False
        Hero.down = False
    elif keys[pygame.K_UP] and Hero.y > Hero.vel:
        Hero.y-=Hero.vel
        Hero.left = False
        Hero.right = False
        Hero.up = True
        Hero.down = False
    elif keys[pygame.K_DOWN] and Hero.y < window_height - Hero.height - Hero.vel:
        Hero.y+=Hero.vel
        Hero.left = False
        Hero.right = False
        Hero.up = False
        Hero.down = True
    else:
        Hero.left = False
        Hero.right = False
        Hero.up = False
        Hero.down = False
        Hero.walkCount = 0
    redrawGameWindow()
    show_fps()

pygame.quit()
sys.exit()

