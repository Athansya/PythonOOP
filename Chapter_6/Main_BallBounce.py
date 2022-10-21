'''
Titulo: Main Ball Bounce

Objetivo: Utilizar la clase Ball para hacer rebotar una pelota.
'''

# Import packages
import pygame
from pygame.locals import *
import sys
import random
from ball import *

# Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# Init world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load assets

# Initialize variables
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)

# Loop forever
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Do any per frame actions
    oBall.update()

    # Clear the window before drawing it again
    window.fill(BLACK)

    # Draw the window elements
    oBall.draw()

    # Update the window
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
