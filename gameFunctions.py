import pygame
from matrix import Matrix
import sys
from settings import Sett


def starting(screen: pygame.Surface):
	done = False
	while not done:	
		Matrix.drawRects(screen)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					done = True

			if event.type == pygame.QUIT:
				sys.exit()

		if pygame.mouse.get_pressed()[0]:
			try:
				mouseX, mouseY = pygame.mouse.get_pos()
				y = round(mouseY / Sett.gridSize)
				x = round(mouseX / Sett.gridSize)
				Matrix.changeState(y, x, 1)
			except IndexError:
				print('dont click outside of the screen!')
		pygame.display.flip()