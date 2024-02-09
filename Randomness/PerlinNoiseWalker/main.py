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
SCREEN_CAPTION      = "Example Name"
TICK                = 100

""" SCREEN'S CONSTANTS """

""" PYGAME INITIALIZATION """
pygame.init()
SCREEN = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
CLOCK = pygame.time.Clock()
pygame.display.set_caption(SCREEN_CAPTION)

""" PYGAME INITIALIZATION """

""" WALKER """
currentPos = (random.uniform(0,WIDTH), random.uniform(0,HEIGHT))
x, y = WIDTH//2, HEIGHT//2
tx = random.uniform(100,1000)
ty = random.uniform(100,1000)
t = 0.1
speed = 10
def walker(t, x, y, tx, ty):
    noise = PerlinNoise(octaves = 4)
    x = ((noise([tx]) - 0.5) * speed) % WIDTH
    y = ((noise([ty]) - 0.5) * speed) % HEIGHT
    pygame.draw.circle(SCREEN, (255,255,255), (x, y), 10, 0)
    tx += t
    ty += t
    return x, y, tx, ty

""" WALKER """

""" MAIN GAME LOOP """
running = True
while running:

    SCREEN.fill(BACKGROUND_COLOR)
    CLOCK.tick(TICK)
    for _ in range(10):
        x, y, tx, ty = walker(t, x, y, tx, ty)

    # EVENT HANDLERS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            SIZE = (WIDTH, HEIGHT)
            SCREEN = pygame.display.set_mode(SIZE, pygame.RESIZABLE)

    pygame.display.update()

pygame.quit()

""" MAIN GAME LOOP """

