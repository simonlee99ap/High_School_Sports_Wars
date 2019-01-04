import sys, pygame
from settings import *
from projectile_class import *
from platform_class import *

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
fallcount - denotes how long the player has been falling
"""
def on_platform(player, platform):
	if (player.y == platform.y - player.height) and (player.x < platform.x + platform.width) and (player.x > platform.x - player.width):
		return True
	return False

class Player():
	def __init__(self, x, y, width, height, speed):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.speed = speed

		self.facing = 1
		self.isJump = False
		self.jumpcount = 8
		self.vulnerability = True
		self.bullets = []
		self.fallcount = 1

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
		if self.jumpcount > 0:
			self.y -= self.jumpcount ** 2
			self.jumpcount -= 1

		else:
			#jumping has concluded
			self.isJump = False
			self.jumpcount = 8

	def throw(self):
		if len(self.bullets) < 5:
			self.bullets.append(Projectile(int(self.x + self.width / 2), int(self.y + self.height / 2), 6, (100, 100, 100), self.facing))

	def melee(self):
		pass

	def defense(self):
		self.vulnearability = False

	def fall(self):
		self.y += gravity * self.fallcount ** 2
		self.fallcount += 1

	def on_platform(self, platform):
		if (self.y == platform.y - self.height) and (self.x < platform.x + platform.width) and (self.x > platform.x - self.width):
			return True
		return False

	def prevent_fallthrough(self, platform):
		if (self.x < platform.x + platform.width) and (self.x > platform.x - self.width):
			if platform.y - self.y - self.height > 0 and platform.y - self.y - self.height < gravity * self.fallcount ** 2:
				self.y = platform.y - self.height


class Football_player(Player):
	pass

class Basketball_player(Player):
	pass

class Wrestler(Player):
	pass

class Baseball_player(Player):
	pass