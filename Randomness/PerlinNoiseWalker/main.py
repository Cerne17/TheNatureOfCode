import pygame
from colorConstants import *
import numpy as np
import random
from functionalities import *
from perlin_noise import PerlinNoise

""" SCREEN'S CONSTANTS """
WIDTH, HEIGHT       = 1200, 800
SIZE                = (WIDTH, HEIGHT)
BACKGROUND_COLOR    = DARK_GRAY
SCREEN_CAPTION      = "Perlin Walker"
TICK                = 100

""" SCREEN'S CONSTANTS """

""" PYGAME INITIALIZATION """
pygame.init()
SCREEN = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
CLOCK = pygame.time.Clock()
pygame.display.set_caption(SCREEN_CAPTION)

MINTICK         = 30
MAXTICK         = 200
MINCOLORTICK    = 0.000001
MAXCOLORTICK    = 0.00001
MINWALKERSIZE   = 20
MAXWALKERSIZE   = 200
MINFLIGHTCHANCE = 0.001
MAXFLIGHTCHANCE = 0.01


""" PYGAME INITIALIZATION """

""" PERLIN COLOR PICKER"""
COLORCHANGETICK = 0.000005
r,g,b = 255, 255, 255
dr = random.uniform(0,1000)
dg = random.uniform(0,1000)
db = random.uniform(0,1000)
noise = PerlinNoise()
def pickColor(r,g,b,dr,dg,db):
    global noise, COLORCHANGETICK
    r = (r + noise(dr)) % 256
    g = (g + noise(dg)) % 256
    b = (b + noise(db)) % 256
    dr += random.uniform(0,COLORCHANGETICK)
    dg += random.uniform(0,COLORCHANGETICK)
    db += random.uniform(0,COLORCHANGETICK)
    return r,g,b,dr,dg,db

""" PERLIN COLOR PICKER"""

""" SLIDER """
def slider(name, currentValue, minValue, maxValue, position, forwardColor, backColor):
    """
    Name - String
    currentValue - float
    minValue - int
    maxValue - int
    position - tuple
    forwardColor - tuple
    backColor - tuple
    """
    width = 250
    height = 30
    margin = 10
    filledPart = (currentValue - minValue) * width / (maxValue - minValue)

    background = pygame.Rect(position[0], position[1], width, height)
    pygame.draw.rect(SCREEN, backColor, background)
    forward = pygame.Rect(position[0], position[1], filledPart, height)
    pygame.draw.rect(SCREEN, forwardColor, forward)

    Font=pygame.font.SysFont('Arial',  30)
    text = Font.render(name, True, (255, 255, 255))
    SCREEN.blit(text, (position[0]+width+margin, position[1]))

""" SLIDER """

""" WALKER """
x, y = WIDTH//2, HEIGHT//2
OUTERSIZE = 100
INNERSIZE = int(3*OUTERSIZE/4)
FLIGHTCHANCE = 0.005
tx = 0
ty = 1000
def walker(tx, ty, x, y):
    global noise, index, OUTERSIZE, FLIGHTCHANCE
    chance = random.uniform(0,1)
    if chance >= FLIGHTCHANCE:
        x = (x + noise(tx)) % WIDTH
        y = (y + noise(ty)) % HEIGHT
    elif chance < FLIGHTCHANCE:
        flightSize = 3*OUTERSIZE/2
        x = (x + random.uniform(-flightSize, flightSize)) % WIDTH
        y = (y + random.uniform(-flightSize, flightSize)) % HEIGHT
    tx += 0.01
    ty += 0.01
    return tx, ty, x, y

""" WALKER """

""" KEY MAPPER """
dColor = 0.000001
dTick  = 5
dSize  = 10
dFlight = 0.001
mapper = {
        "w": dColor, 
        "s": -1*dColor, 
        "d": dTick,            
        "a": -1*dTick,            
        "l": dSize,       
        "j": -1*dSize,       
        "k": -1*dFlight,
        "i": dFlight,
        }
translator = {
        119: "w",
        115: "s",
        100: "d",
        97:  "a",
        108: "l",
        106: "j",
        105: "i",
        107: "k",
        }

""" KEY MAPPER """

SCREEN.fill(BACKGROUND_COLOR)
""" MAIN GAME LOOP """
running = True
walking = True
while running:

    CLOCK.tick(TICK)
    if walking:
        for _ in range(10):
            r,g,b,dr,dg,db = pickColor(r,g,b,dr,dg,db)
            INNERSIZE = int(3*OUTERSIZE/4)
            pygame.draw.circle(SCREEN, (r,g,b), (x, y), OUTERSIZE, INNERSIZE)
            tx, ty, x, y = walker(tx, ty, x, y)

    slider("Tick Speed (a-d)", TICK, MINTICK, MAXTICK, (30,30), (80,80,80), (30,30,30))
    slider("Color Change (s-w)", COLORCHANGETICK, MINCOLORTICK, MAXCOLORTICK, (30,70), (120,20,20), (50,20,20))
    slider("Walker Size (j-l)", OUTERSIZE, MINWALKERSIZE, MAXWALKERSIZE, (30,110), (10,120,10), (20,50,20))
    slider("Flight Chance (k-i)", FLIGHTCHANCE, MINFLIGHTCHANCE, MAXFLIGHTCHANCE, (30,150), (10,10,120), (20,20,50))

    # EVENT HANDLERS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            SIZE = (WIDTH, HEIGHT)
            SCREEN = pygame.display.set_mode(SIZE, pygame.RESIZABLE)

        if event.type == pygame.KEYDOWN:
            key = event.key
            if key in translator.keys():
                trueKey = translator[key]
                if trueKey in ["w", "s"]:
                    COLORCHANGETICK += mapper[trueKey]
                if trueKey in ["d", "a"]:
                    TICK += mapper[trueKey]
                if trueKey in ["l", "j"]:
                    OUTERSIZE += mapper[trueKey]
                if trueKey in ["k", "i"]:
                    FLIGHTCHANCE += mapper[trueKey]
            if key == pygame.K_SPACE:
                walking = not walking
            if key == pygame.K_r:
                SCREEN.fill(BACKGROUND_COLOR)

    Font=pygame.font.SysFont('Arial',  30)
    text = Font.render("Pause: SPACE", True, (255, 255, 255))
    SCREEN.blit(text, (30, HEIGHT - 90))
    text = Font.render("Clear Screen: r", True, (255, 255, 255))
    SCREEN.blit(text, (30, HEIGHT - 50))

    pygame.display.update()

pygame.quit()

""" MAIN GAME LOOP """
