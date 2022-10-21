'''
Titulo: Main Simple Button

Objetivo: Utilizar la clase SimpleButton para hacer un boton.
'''

# Import packages
import pygame
from pygame.locals import *
import sys
import random
from SimpleButton import *

# Define constants
GRAY = (128, 128, 128)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# Init world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load assets

# Initialize variables
oButton = SimpleButton(window, (150, 30), '/images/buttonUp.png', '/images/buttonDown.png')

# loop forever
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oButton.handleEvent(event):
            print('User has clicked the button')

    # Do any per frame actions

    # Clear the window
    window.fill(GRAY)

    # Draw all window elements
    oButton.draw()

    # Update the window
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
