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

x = 0

class player(object):
    def __init__(self, x, y, megaman, jmp):
        self.x = x
        self.y = y
        self.megaman = megaman
        self.jmp = jmp
        self.hitbox = (self.x, self.y+60, 100, 80)

    def run(self):

        if (self.megaman == 1):
            window.blit(run[0], (20, 150))

        if (self.megaman == 2):
            window.blit(run[1], (20, 150))

        if (self.megaman == 3):
            window.blit(run[2], (20, 150))

    def jump(self):

        if (self.jmp == 0):
            self.hitbox = (self.x, self.y - 60, 100, 80)

            self.jmp += 1
            window.blit(jump[0], (20, 30))

        if (self.jmp == 1):
            self.hitbox = (self.x, self.y - 60, 100, 80)

            window.blit(jump[1], (20, 30))

        if (self.jmp == 2):
            self.hitbox = (self.x, self.y - 60, 100, 80)

            window.blit(jump[2], (20, 30))
            self.jmp = 0
        else:
            self.jmp += 1
        self.hitbox = (self.x, self.y, 100, 80)

class enemy(object):
    def __init__(self, x, y, anim):
        self.x = x
        self.y = y
        self.anim = anim
        self.hitbox = (self.x, self.y+30, 100, 100)

    def update(self):

        if self.anim == 0:
            window.blit(enemy_bat[0], (self.x, self.y))
        if self.anim == 1:
            window.blit(enemy_bat[1], (self.x-20, self.y))
        if self.anim == 2:
            window.blit(enemy_bat[2], (self.x-20, self.y))

megaman = 1
e = 0
y = 250
x_enemy=160
score = 0
black=(0,0,0)
end_it=False
while (end_it==False):

    window.fill(Color.Beige)
    myfont=pygame.font.SysFont("Britannic Bold", 40)
    nlabel=myfont.render("Welcome,", 1, (255, 0, 0))
    nlabel2=myfont.render("Mouse Click to begin", 1, (255, 0, 0))

    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN:
            pygame.time.wait(500)
            y = 1000
            end_it=True
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    window.blit(nlabel,(70, 50))
    window.blit(nlabel2,(70, 90))

    pygame.display.flip()
gameover = False

while isRunning:

    # print(score)
    for event in pygame.event.get():
        if event.type == QUIT:
            isRunning = False

    rel_x = x % bg.get_rect().width
    window.blit(bg, (rel_x - bg.get_rect().width, 0))
    if rel_x < window_width + 200:
        window.blit(bg, (rel_x, 0))
    x-=10

    window.blit(bg, (x, 0))
    jmp = 0
    Hero = player(20, 150, megaman, jmp)
    window.blit(bg, (x, 0))
    Hero.run()
    if megaman > 3:
        megaman = 1
    else:
        megaman += 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        window.blit(bg, (rel_x - bg.get_rect().width, 0))
        if rel_x < window_width + 200:
            window.blit(bg, (rel_x, 0))
        Hero.jump()

    a = enemy(y, x_enemy, e)
    a.update()

    if e > 2:
        e = 0
    else:
        e += 1
    y -= 20
    if y<=0:

        y = random.randint(600, 1000)
        # x_enemy = random.randint(160, 250)
        # a = enemy(y, x_enemy, e)
    score += 1
    font = pygame.font.Font("C:\\Windows\\Fonts\\Arial.ttf", 50)
    text = font.render("Score: "+str(score), True, (Color.White))
    # textpos = text.get_rect(centerx=window.get_width() / 2)
    window.blit(text, (0, 0))

    pygame.display.update()
    if Hero.hitbox[0] >= a.hitbox[0] and Hero.hitbox[1]+Hero.hitbox[3] >= a.hitbox[1]+a.hitbox[3]:
        window.fill((255,0,0))
        isRunning = False
        gameover = True
        # score = 0
        pygame.display.update()

    clock.tick(27)


while gameover:
    window.fill(Color.Beige)
    myfont = pygame.font.SysFont("Britannic Bold", 40)
    nlabel = myfont.render("Score:  "+ str(score), 1, (255, 0, 0))
    # nlabel2 = myfont.render("Mouse Click to Play Again", 1, (255, 0, 0))

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            pygame.time.wait(500)
            y = 1000
            gameover = False
            end_it = True
            isRunning = True
            pygame.display.flip()

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    window.blit(nlabel, (70, 50))
    # window.blit(nlabel2, (70, 90))
    pygame.display.flip()



pygame.quit()
sys.exit()