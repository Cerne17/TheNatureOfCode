import pygame
from colorConstants import *
import numpy as np
import random
from functionalities import *

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

""" MAIN GAME LOOP """
running = True
while running:

    CLOCK.tick(TICK)
    SCREEN.fill(BACKGROUND_COLOR)

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
