'''
Titulo: Pygame Image Click and Move

Objetivo: Utilizar pygame para mover una imagen.
'''

# Import packages
import pygame
from pygame.locals import *
import sys
from pathlib import Path
import random

# Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BASE_PATH = str(Path(__file__).resolve().parent)
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

# Initialize world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load assets
ballImage = pygame.image.load(BASE_PATH + '/images/ball.png')

# Initialize variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

# Loop forever
while True:

    # Check for and handle events
    for event in pygame.event.get():
        # Close button
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # See if user clicked
        if event.type == pygame.MOUSEBUTTONUP:
            #mousexX, mouseY = event.pos # Could do this if we needed it
            # Check if the click was in the rect of the ball
            # If so, choose a random new location
            if ballRect.collidepoint(event.pos):
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)
                ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

    # Do any "per frame" actions

    # Clear the window
    window.fill(BLACK)

    # Draw all window elements
    # draw ball at position 100 across (x) and 200 down (y)
    window.blit(ballImage, (ballX, ballY))

    # Update the window
    pygame.display.update()

    # Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
