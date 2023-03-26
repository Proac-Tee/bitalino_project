# import the necessary libraries
import pygame

from data_acq import data_acquisition

pygame.init()

# Set up the game window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Jumping Game")

# Load the player image
player_img = pygame.image.load("test_group\DinoStart.png").convert_alpha()

# Set up the player position and velocity
player_x = WINDOW_WIDTH / 2
player_y = WINDOW_HEIGHT - player_img.get_height()
player_vel_y = 0
GRAVITY = 0.5
JUMP_VELOCITY = -10

# Run the data acquisition function in a separate thread
import threading

acquisition_thread = threading.Thread(target=data_acquisition)
acquisition_thread.start()