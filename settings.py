# global variables for the screen setup
import sys, pygame
from platform_class import *

global scrn_height
scrn_height = 480

global scrn_width
scrn_width = 960

global scrn
scrn = pygame.display.set_mode((scrn_width, scrn_height))

global ground
ground = Platform(0, 430, 960, 50)

global middle_left
middle_left = Platform(100, 280, 300, 20)

global middle_right
middle_right = Platform(560, 280, 300, 20)

global top
top = Platform(330, 130, 300, 20)

global platforms
platforms = [ground, middle_left, middle_right, top]

def draw_platforms():
	for platform in platforms:
		platform.draw(scrn)

global gravity
gravity = 1
