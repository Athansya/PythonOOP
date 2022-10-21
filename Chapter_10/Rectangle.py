'''
UID: 202203161100
Autor: Alfonso Toriz V.

Objetivo: Crear una subclase Rectangle utilizando una
clase abstracta base.
'''

# Rectangle class
import pygame
import random
import ShapeABC


class Rectangle(ShapeABC):

    def __init__(self, window, maxWidth, maxHeight):
        super().__init__(window, 'Rectangle', maxWidth, maxHeight)
        self.width = random.randrange(10, 100)
        self.height = random.randrange(10, 100)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def clickedInside(self, mousePoint):
        clicked = self.rect.collidepoint(mousePoint)
        return clicked

    def getArea(self):
        theArea = self.width * self.height
        return theArea

    # No se incluye el metodo draw() para provocar un error
    # de la clase abstracta
