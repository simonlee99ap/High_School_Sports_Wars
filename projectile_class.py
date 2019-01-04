import sys, pygame
from settings import *

class Projectile():
	def __init__(self, x, y, radius, color, facing):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.facing = facing
		self.speed = 20 * facing

	def draw(self):
		pygame.draw.circle(scrn, self.color, (self.x, self.y), self.radius)