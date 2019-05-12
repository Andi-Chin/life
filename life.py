import pygame
import sys
import time
import copy
from matrix import Matrix
from settings import Sett
from gameFunctions import *

pygame.init()

pygame.font.init()
myfont: pygame.font.Font = pygame.font.SysFont('Comic Sans MS', round(Sett.gridSize/2))
screen = pygame.display.set_mode([Sett.screenWidth, Sett.screenHeight])
pygame.display.set_caption("Conway's Game of Life")

# this is the manual population phase

starting(screen)

iteration = 0
while True:
	Matrix.drawRects(screen)
	Matrix.generation()
	pygame.display.flip()

	print("gen: %s" % (iteration))
	iteration += 1
	time.sleep(0.5)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
