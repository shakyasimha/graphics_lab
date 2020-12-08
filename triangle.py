# Code written by Sushovan Shakya (THA075BEI046)

import pygame
import sys
import math

# Basic variables
resolution = (1360, 768)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)

# Display setup
pygame.init()
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("2D Triangle Transformation")
screen.fill(black)
pygame.display.update()

# Triangle class
class Triangle:

    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def draw(self, colour):
        pygame.draw.polygon(screen, colour, (self.p1, self.p2, self.p3))

    # Method for translation
    def translate(self, colour, translate_factor):
        self.p1[0] += translate_factor[0]
        self.p2[0] += translate_factor[0]
        self.p3[0] += translate_factor[0]
        self.p1[1] += translate_factor[1]
        self.p2[1] += translate_factor[1]
        self.p3[1] += translate_factor[1]

        pygame.draw.polygon(screen, colour, (self.p1, self.p2, self.p3))

    # Method for scaling
    def scaling(self, colour, scaling_factor):
        self.p1[0] *= scaling_factor[0]
        self.p2[0] *= scaling_factor[0]
        self.p3[0] *= scaling_factor[0]
        self.p1[1] *= scaling_factor[1]
        self.p2[1] *= scaling_factor[1]
        self.p3[1] *= scaling_factor[1]

        pygame.draw.polygon(screen, colour, (self.p1, self.p2, self.p3))

    # Method for rotation
    def rotate(self, colour, center, angle, direction):

        # Direction = -1 => Clockwise direction
        # Direction = +1 => Anticlockwise direction
        if direction == -1:
            angle = float(-angle * math.pi / 180)
        else:
            angle = float(angle * math.pi / 180)

        # Assigning values, for the ease of calculation
        xc, yc = center[0], center[1]
        x1, y1 = self.p1[0], self.p1[1]
        x2, y2 = self.p2[0], self.p2[1]
        x3, y3 = self.p3[0], self.p3[1]

        # For (x1, y1):
        x = ((x1 - xc) * math.cos(angle)) - ((y1 - yc) * math.sin(angle)) + xc
        y = ((x1 - xc) * math.sin(angle)) + ((y1 - yc) * math.cos(angle)) + yc
        self.p1[0] = x      # Reassigning values
        self.p1[1] = y

        # For (x2, y2):
        x = ((x2 - xc) * math.cos(angle)) - ((y2 - yc) * math.sin(angle)) + xc
        y = ((x2 - xc) * math.sin(angle)) + ((y2 - yc) * math.cos(angle)) + yc
        self.p2[0] = x      # Reassigning values
        self.p2[1] = y

        # For (x3, y3):
        x = ((x3 - xc) * math.cos(angle)) - ((y3 - yc) * math.sin(angle)) + xc
        y = ((x3 - xc) * math.sin(angle)) + ((y3 - yc) * math.cos(angle)) + yc
        self.p3[0] = x      # Reassigning values
        self.p3[1] = y

        pygame.draw.polygon(screen, colour, (self.p1, self.p2, self.p3))

# Coordinates of the triangle
# p1 = [100, 200]
# p2 = [200, 200]
# p3 = [200, 100]

triangle = Triangle(p1=[100, 200], p2=[200, 200], p3=[200,100])
triangle.draw(blue)
triangle.translate(red, translate_factor=[200, 200])
triangle.scaling(green, scaling_factor=[1.5, 1.5])
triangle.rotate(yellow, center=[300, 300], angle=60, direction=1)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

