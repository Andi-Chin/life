import pygame
import sys
import time
import copy

gridSize = 10
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', round(gridSize/2))
screen = pygame.display.set_mode([1200, 800])
pygame.display.set_caption("Conway's Game of Life")
class Square():
	def __init__(self, x, y, state):
		self.x = x
		self.y = y
		self.state = state

	def checkArea(self, matrix):
		count = 0
		for y in range(self.y - 1, self.y + 2):
			for x in range(self.x - 1, self.x + 2):
				#if it's urself
				if x == self.x and y == self.y: continue	
				#so it doesn't go out of bounds
				if x < 0 or y < 0: continue		
				try:	
					if matrix[y][x].state == 1:
						count += 1
				except IndexError:
					pass
		return count




class Matrix():

	matrix = [[Square(x, y, 0) for x in range(150)] for y in range(70)]
	# lis = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
	# 		[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
	# 		[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
	# 		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	# 		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	# 		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	# 		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	# 		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	# 		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	# 		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
	# for y in range(len(lis)):
	# 	for x in range(len(lis)):
	# 		matrix[y][x].state = lis[y][x]


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
				if count < 2:
					tempMatrix[y][x].state = 0
				if count == 3:
					tempMatrix[y][x].state = 1
				if count > 3:
					tempMatrix[y][x].state = 0
		Matrix.matrix = tempMatrix
	def drawRects():
		color = None
		for row in Matrix.matrix:
			for square in row:				
				if square.state == 1:
					color = (200, 100, 0)
				elif square.state == 0:
					color = (100, 100, 100)
				pygame.draw.rect(screen, color, [square.x*gridSize, square.y*gridSize, gridSize, gridSize], 0)


done = False
while not done:	
	Matrix.drawRects()
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				done = True

		if event.type == pygame.QUIT:
			sys.exit()

	if pygame.mouse.get_pressed()[0]:
		try:

			mouseX, mouseY = pygame.mouse.get_pos()
			y = round(mouseY/gridSize)
			x = round(mouseX/gridSize)

			Matrix.changeState(y, x, 1)
			
		except IndexError:
			print('dont click outside of the screen!')

	pygame.display.flip()



iteration = 0
while True:
	Matrix.drawRects()
	Matrix.generation()
	pygame.display.flip()

	print("gen: %s" % (iteration))

	iteration += 1



	time.sleep(0.5)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
