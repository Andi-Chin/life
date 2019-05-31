from square import Square
from settings import Sett
import copy
import pygame

class Matrix():
	matrix = [[Square(x, y, 0) for x in range(Sett.boardWidth)] 
                                for y in range(Sett.boardHeight)]
	def drawMatrix():
		print()
		for x in range(len(Matrix.matrix)):
			for y in range(len(Matrix.matrix)):
				print(Matrix.matrix[x][y].state, end = ' ')
				if y == len(Matrix.matrix) - 1:
					print()
		print()

	def changeState(y, x, state):
		Matrix.matrix[y][x].state = state

	def generation():
		tempMatrix = copy.deepcopy(Matrix.matrix)
		for y in range(len(Matrix.matrix)):
			for x in range(len(Matrix.matrix)):
				count = Matrix.matrix[y][x].checkArea(Matrix.matrix)
				#logic, see rules on https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
		Matrix.matrix = tempMatrix
	def drawRects(screen: pygame.Surface):
		color = None
		for row in Matrix.matrix:
			for square in row:				
				if square.state == 1:
					color = (200, 100, 0)
				elif square.state == 0:
					color = (100, 100, 100)
				pygame.draw.rect(screen, color, [square.x * Sett.gridSize, square.y * Sett.gridSize,
                                                     Sett.gridSize, Sett.gridSize], 0)
