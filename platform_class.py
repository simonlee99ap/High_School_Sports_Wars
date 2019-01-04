import sys, pygame

class Platform:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def draw(self, scrn):
		pygame.draw.rect(scrn, (0, 255, 0), (self.x, self.y, self.width, self.height))