import pygame
from colorConstants import *
import numpy as np
import random

""" TODOS """
#TODO: Create a slider to adjust the Standard Deviation

""" TODOS """

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
SCREEN.fill(BACKGROUND_COLOR)

""" PYGAME INITIALIZATION """

""" COLOR PICKER """
COLOR_STD_DEVIATION = 60
redCenter = random.uniform(0,255)%255
greenCenter = random.uniform(0,255)%255
blueCenter = random.uniform(0,255)%255

print(f"red center: {redCenter} | green center: {greenCenter} | blue center: {blueCenter}")

def pickColor():

    red = random.gauss(redCenter, COLOR_STD_DEVIATION)%255
    green = random.gauss(greenCenter, COLOR_STD_DEVIATION)%255
    blue = random.gauss(blueCenter, COLOR_STD_DEVIATION)%255

    return (red, green, blue)

""" COLOR PICKER """

""" PAINT SPLATTER """
paint = True
STD_DEVIATION = 100
PAINT_SIZE = 2
def drawPaint():
    xPos = random.gauss(WIDTH/2, STD_DEVIATION)
    yPos = random.gauss(HEIGHT/2, STD_DEVIATION)

    pygame.draw.circle(SCREEN, pickColor(), (xPos, yPos), PAINT_SIZE, 0)

""" PAINT SPLATTER """

""" SLIDER """
MINSLIDERVALUE         = 0
MAXSLIDERVALUE         = 200
SLIDEVARIATIONPERCLICK = 5
currentStdDeviation    = 50
def slider(currentStdDeviation):
    sliderWidth  = 250
    sliderHeight = 30
    sliderPosX   = 20
    sliderPosY   = 20

    sliderBorder = pygame.Rect(sliderPosX, sliderPosY, sliderWidth, sliderHeight)
    pygame.draw.rect(SCREEN, (50, 50, 50), sliderBorder)
    sliderValue  = pygame.Rect(sliderPosX, sliderPosY, currentStdDeviation*sliderWidth/MAXSLIDERVALUE, sliderHeight)
    pygame.draw.rect(SCREEN, (80, 80, 80), sliderValue)

    global STD_DEVIATION
    STD_DEVIATION = currentStdDeviation

""" SLIDER """

""" MAIN GAME LOOP """
running = True
while running:

    CLOCK.tick(TICK)

    if paint:
        for _ in range(10):
            drawPaint()
    
    slider(currentStdDeviation)

    # EVENT HANDLERS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            SIZE = (WIDTH, HEIGHT)
            SCREEN = pygame.display.set_mode(SIZE, pygame.RESIZABLE)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paint = not paint
            if event.key == pygame.K_r:
                SCREEN.fill(BACKGROUND_COLOR)
                redCenter = random.uniform(0,255)%255
                greenCenter = random.uniform(0,255)%255
                blueCenter = random.uniform(0,255)%255
            if event.key == pygame.K_LEFT:
                currentStdDeviation = currentStdDeviation - SLIDEVARIATIONPERCLICK if currentStdDeviation >= MINSLIDERVALUE + SLIDEVARIATIONPERCLICK else MINSLIDERVALUE
            if event.key == pygame.K_RIGHT:
                currentStdDeviation = currentStdDeviation + SLIDEVARIATIONPERCLICK if currentStdDeviation <= MAXSLIDERVALUE - SLIDEVARIATIONPERCLICK else MAXSLIDERVALUE

    pygame.display.update()

pygame.quit()

""" MAIN GAME LOOP """
