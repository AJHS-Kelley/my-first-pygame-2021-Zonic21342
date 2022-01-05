#Pygame Collision Detection Pratice, Brunswick Kyomari, Jan-05-22, 9:32am, 0.4

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

#Setup colors
BLACK = (0,0,0)
GREEN = (0,255,0)
WHITE = (255, 255, 255)

#Setup the player and food data structures.
foodcounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50)
foods = []

for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWEIGHT = FOODSIZE), random.randit(0, WINDOWHEIGHT = FOODSIZE), FOODSIZE, FOODSIZE))


