# Midpoint Circle Algorithm

import pygame
import sys
from pygame import gfxdraw  

# Colour variables
black = (0, 0, 0)
white = (255, 255, 255)

# Program setup variables
running = True
resolution = (1024, 768)

# pygame init
pygame.init()
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Midpoint Circle Algorithm")
screen.fill(white)
pygame.display.update()

def plotCircle(x, y, centre):
    gfxdraw.pixel(screen,  x + centre[0],  y + centre[1], black)

def Circle(radius, centre):
    x, y = 0, radius
    d = float(1.25 - radius)        # Decision variable

    while x < y:
        if d < 0:
            x += 1
            d += (2*x) + 1   
        else:
            x += 1
            y -= 1
            d += 2*(x-y) + 1

        plotCircle( x,  y, centre)
        plotCircle( x, -y, centre)
        plotCircle(-x,  y, centre)
        plotCircle(-x, -y, centre)
        plotCircle( y,  x, centre)
        plotCircle(-y,  x, centre)
        plotCircle( y, -x, centre)
        plotCircle(-y, -x, centre)
        pygame.display.update()


# Circle parameters
# radius = 100
# centre = (200, 200)
Circle(100, (200, 200))

# Program loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
