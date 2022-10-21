'''
Titulo: Pygame Window Only

Objetivo: Desplegar una pantall en negro
utilizando pygame.
'''

# Import packages
import pygame
from pygame.locals import *
import sys

# Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# Initialize world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load assets: image(s), sound(s), etc.

# Initialize variables

# Loop forever
while True:

    # Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Do any "per frame" actions

    # Clear the window
    window.fill(BLACK)

    # Draw all window elements

    # Update the window
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
