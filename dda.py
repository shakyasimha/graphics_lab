# Digital Differential Analyzer Algorithm

import pygame
import sys
from pygame import gfxdraw

# Colour variables
black = (0, 0, 0)
white = (255, 255, 255)

# Display variables
resolution = (800, 600)
running = True

# Pygame init
pygame.init()
screen = pygame.display.set_mode(resolution)
screen.fill(white)
pygame.display.set_caption("Digital Differential Analyzer Algorithm")

def DDA(P1, P2):
    x1, y1 = P1[0], P1[1]
    x2, y2 = P2[0], P2[1]

    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):
        step = abs(dx)
    else:
        step = abs(dy)

    x, y = x1, y1
    x_inc = dx / step
    y_inc = dy / step

    gfxdraw.pixel(screen, round(x), round(y), black)

    for i in range(step):
        x += x_inc
        y += y_inc 
        gfxdraw.pixel(screen, round(x), round(y), black)

# Line parameters:
# Point 1, P1 = (200, 200)
# Point 2, P2 = (600, 800)
DDA((200, 200), (600, 800))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()