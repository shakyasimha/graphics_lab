#!/usr/bin/python

import pygame
from pygame import gfxdraw

# Bresenham Line drawing algorithm

# Basic program variables
white = (255, 255, 255)
black = (0, 0, 0)
resolution = (800, 600)

# Init
pygame.init()
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Bresenham algorithm")
screen.fill(white)
pygame.display.update()

# Plotting function
def plot(x, y):
    gfxdraw.setpixel(screen, x, y, black)

# Main algorithm
def Bresenham(P1, P2):
    # P1 = (x1, y1)
    # P2 = (x2, y2)
    x1, y1 = P1[0], P1[1]
    x2, y2 = P2[0], P2[1]

    dx = x2 - x1
    dy = y2 - y1
    i1 = 2 * dy
    i2 = 2 * (dy - dx)
    d = i1 - dx

    if dx < 0:
        x, y = x2, y2
        x_end = x1
    else:
        x, y = x1, y1
        x_end = x2

    while x >= x_end:
        plot(x, y)

        if d < 0:
            d += i1
        else:
            d += i2
            y += 1
        x += 1

Bresenham((200, 200), (600, 800))

# Main program loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
