#Pygame Collision Detection Pratice, Brunswick Kyomari, Jan-05-22, 9:16am, 0.2

import pygame, sys, random
from pygame.locals import

# Setup Pygame
pygame,init()
mainClock = pygame.time.Clock()

#Setup the Pygame window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = Pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0,32)
pygame.display.set_caption('Collision Detection 2022')