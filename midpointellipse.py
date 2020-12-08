# Midpoint Ellipse Algorithm

import pygame
import sys
import math
from pygame import gfxdraw

# Colour variables
black = (0, 0, 0)
white = (255, 255, 255)

# Program setup variables
running = True
resolution = (1024, 768)

# Init
pygame.init()
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Mmidpoint Ellipse Algorithm")
screen.fill(white)
pygame.display.update()

# Plotting function
def plot(x, y):
    gfxdraw.pixel(screen, x, y, black)

# Algorithm 
def Ellipse(centre, a, b):

    # center = (x, y) => center of ellipse (tuple)
    # a => semi-major axis
    # b => semi-minor axis

    x, y = 0, b
    xc, yc = centre[0], centre[1]       # Centre variables

    # Initial parameters for the 1st region
    d1 = pow(b, 2) - (pow(a, 2) * b) + (0.25 * pow(a, 2))
    dx = 2 * pow(b, 2) * x
    dy = 2 * pow(a, 2) * y

    # Plotting for 1st region
    while dy > dx:
        plot(xc + x, yc + y)
        plot(xc - x, yc + y)
        plot(xc - x, yc - y)
        plot(xc + x, yc - y)
        pygame.display.update()

        if d1 < 0:
            x += 1
            dx += (2 * pow(b, 2))
            dy += dx + pow(a, 2)
        else:
            x += 1
            y -= 1
            dx += (2 * pow(b, 2))
            dy -= (2 * pow(a, 2))
            d1 += dx - dy + pow(b, 2)

    # Initial parameters for the 2nd region
    d2 = (pow(b, 2) * pow((x + 0.5), 2)) + (pow(a, 2) * pow((y - 1), 2)) - (pow(a, 2) * pow(b, 2))

    # Plotting for 2nd region
    while y > 0:
        plot(xc + x, yc + y)
        plot(xc - x, yc + y)
        plot(xc - x, yc - y)
        plot(xc + x, yc - y)
        pygame.display.update()

        if d1 < 0:
            x += 1
            dx += (2 * pow(b, 2))
            dy += dx + pow(b, 2)
        else:
            x += 1
            y -= 1
            dx += (2 * pow(b, 2))
            dy -= (2 * pow(a, 2))
            d2 += dx - dy + pow(a, 2)


# Ellipse parameters:
# Center = (100, 100)
# Major axis = 288
# Minor axis = 250
Ellipse((100, 100), 288, 250)

# Program loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()