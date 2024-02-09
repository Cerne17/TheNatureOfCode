import pygame
from colorConstants import *
import random

""" SCREEN'S CONSTANTS """
WIDTH, HEIGHT                = 1200, 800
SIZE                         = (WIDTH, HEIGHT)
BACKGROUND_COLOR             = DARK_GRAY
WALKER_COLOR                 = (0, 255, 255)
SCREEN_CAPTION               = "Random Walker"
CLOCK_TICK                   = 100
CLOCK_INCREASE_MULTIPLIER    = 1

""" SCREEN'S CONSTANTS """

""" PYGAME INITIALIZATION """
pygame.init()
SCREEN = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
CLOCK = pygame.time.Clock()
pygame.display.set_caption(SCREEN_CAPTION)
SCREEN.fill(BACKGROUND_COLOR)

""" PYGAME INITIALIZATION """

""" RANDOM WALKER """

WALKER_SIZE = 1
WALKS_PER_CYCLE = 4

currentPos = (random.uniform(0,WIDTH), random.uniform(0,HEIGHT))
def randomWalk(currentPos):
    nextPos = ((currentPos[0] + random.uniform(-1, 1))%WIDTH, (currentPos[1] + random.uniform(-1, 1))%HEIGHT)
    pygame.draw.circle(SCREEN, WALKER_COLOR, nextPos, WALKER_SIZE, 0)
    
    return nextPos

walking = True


""" MAIN GAME LOOP """
running = True
while running:

    CLOCK.tick(CLOCK_TICK)

    if walking:
        for i in range(WALKS_PER_CYCLE):
             currentPos = randomWalk(currentPos)

    # EVENT HANDLERS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            SIZE = (WIDTH, HEIGHT)
            SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            SCREEN.fill(BACKGROUND_COLOR)
            currentPos = (random.uniform(0,WIDTH), random.uniform(0,HEIGHT))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                walking = not walking
            if event.key == pygame.K_w:
                WALKS_PER_CYCLE += 5*CLOCK_INCREASE_MULTIPLIER
            if event.key == pygame.K_s:
                WALKS_PER_CYCLE -= 5*CLOCK_INCREASE_MULTIPLIER
            if event.key == pygame.K_a:
                CLOCK_INCREASE_MULTIPLIER -= 1
            if event.key == pygame.K_d:
                CLOCK_INCREASE_MULTIPLIER += 1
            if event.key == pygame.K_r:
                SCREEN.fill(BACKGROUND_COLOR)
                currentPos = (random.uniform(0,WIDTH), random.uniform(0,HEIGHT))

        if event.type == pygame.MOUSEBUTTONDOWN:
            currentPos = pygame.mouse.get_pos()


    pygame.display.update()

pygame.quit()

""" MAIN GAME LOOP """
