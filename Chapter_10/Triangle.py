'''
UID: 202203161023
Autor: Alfonso toriz V.

Objetivo: Crear una clase trinagle un la base class Shape.
'''

# Triangel class
import pygame
import Shape
import random


class Triangle(Shape):

    def __init__(self, window, maxWidth, maxHeight):
        super().__init__(window, 'Triangle', maxWidth, maxHeight)
        self.width = random.randrange(10, 100)
        self.height = random.randrange(10, 100)
        self.triangleSlope = -1 * (self.height / self.width)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def clickedInside(self, mousePoint):
        inRect = self.rect.collidepoint(mousePoint)
        if not inRect:
            return False

        # Do some math to see if hte point is inside the triangle
        xOffset = mousePoint[0] - self.x
        yOffset = mousePoint[1] - self.y
        if xOffset == 0:
            return True

        pointSlopeFromYIntercept = (yOffset - self.height) / xOffset  # rise over run
        if pointSlopeFromYIntercept < 1:
            return True
        else:
            return False

    def getArea(self):
        theArea = .5 * self.width * self.height
        return theArea

    def draw(self):
        pygame.draw.polygon(
            self.window, self.color,
            (
                (self.x, self.y + self.height),
                (self.x, self.y),
                (self.x + self.width, self.y)
            )
        )
