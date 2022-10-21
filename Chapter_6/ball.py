'''
Titulo: Ball

Objetivo: Crear una clase para manipular un objeto Ball con
diferentes metodos.
'''

# import statements
import pygame
from pygame.locals import *
import random
from pathlib import Path

# Define
BASE_PATH = str(Path(__file__).resolve().parent)

# Ball class
class Ball():
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window # Remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.image = pygame.image.load(BASE_PATH + '/images/ball.png')
        ballRect = self.image.get_rect()
        self.height = ballRect.height
        self.width = ballRect.width
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height

        # Pick a random starting position
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)

        # Choose a random speed between -4 and 4, but not 0
        # in both the x and y directions
        speedsList = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)

    def update(self):
        # Check for hitting a wall. If so, change the direction
        if (self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed

        if (self.y < 0) or (self.y >= self.maxHeight):
            self.ySpeed = -self.ySpeed

        # Update the Ball's x and y, using the speed in two directions
        self.x += self.xSpeed
        self.y += self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))
