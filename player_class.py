import sys, pygame
from settings import *
from projectile_class import *

"""
The player, or the character, has the following instance variables:
x - denotes the x position of the player
y - denotes the y position of the player
width - denotes the width of the player
height - denotes the height of the player
speed - denotes the speed of the plaer

facing - sees if the player is facing left or right; 1 if facing right, -1 if facing left
isJump - boolean value that is true when the player is jumping, false otherwise
jumpcount - denotes how high and fast the player can jump

vulnerability - true when the player can take damage, false when the player cannot like when blocking

bullets - an array containing projectile class
"""

class Player():
	def __init__(self, x, y, width, height, speed):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.speed = speed

		self.facing = 1
		self.isJump = False
		self.jumpcount = 5
		#checks if a character can be damaged or not
		self.vulnerability = True

		self.bullets = []

	def draw(self):
		pygame.draw.rect(scrn, (255, 0, 0), (self.x, self.y, self.width, self.height))

	def move_left(self):
		if self.x > self.speed:
			self.x -= self.speed
		self.facing = -1

	def move_right(self):
		if self.x < scrn_width - self.width - self.speed:
			self.x += self.speed
		self.facing = 1

	def jump(self):
		if self.jumpcount >= -5:
			if self.jumpcount >= 0:
				self.y -= self.jumpcount ** 2
			else:
				self.y += self.jumpcount ** 2
			self.jumpcount -= 1

		else:
			#jumping has concluded
			self.isJump = False
			self.jumpcount = 5

	def throw(self):
		if len(self.bullets) < 5:
			self.bullets.append(Projectile(int(self.x + self.width / 2), int(self.y + self.height / 2), 6, (100, 100, 100), self.facing))

	def melee(self):
		pass

	def defense(self):
		self.vulnearability = False

class Football_player(Player):
	pass

class Basketball_player(Player):
	pass

class Wrestler(Player):
	pass

class Baseball_player(Player):
	pass