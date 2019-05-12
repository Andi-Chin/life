
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