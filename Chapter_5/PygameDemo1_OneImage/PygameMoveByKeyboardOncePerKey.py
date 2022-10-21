'''
Titulo: Pygame Move by Keyboard Once per Key

Objetivo: Detectar input de teclas en pygame
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

TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 3

# Initialize world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load assets
ballImage = pygame.image.load(BASE_PATH + '/images/ball.png')
targetImage = pygame.image.load(BASE_PATH + '/images/target.jpg')

# Initialize variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
targetRect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)

# Loop forever
while True:
    # Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ballX -= N_PIXELS_TO_MOVE
            elif event.key == pygame.K_RIGHT:
                ballX  += N_PIXELS_TO_MOVE
            elif event.key == pygame.K_UP:
                ballY -= N_PIXELS_TO_MOVE
            elif event.key == pygame.K_DOWN:
                ballY += N_PIXELS_TO_MOVE

    # Do any "per frame" actions
    # Check if the ball is colliding with the target
    ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
    if ballRect.colliderect(targetRect):
        print('Ball is touching the target')

        # Clear the window
        window.fill(BLACK)

        # Draw all window elements
        window.blit(targetImage, (TARGET_X, TARGET_Y))
        window.blit(ballImage, (ballX, ballY))

        # Update the window
        pygame.display.update()

        # Slow things down
        clock.tick(FRAMES_PER_SECOND)
