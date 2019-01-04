# global variables for the screen setup
import sys, pygame

global scrn_height
scrn_height = 480

global scrn_width
scrn_width = 640

global scrn
scrn = pygame.display.set_mode((scrn_width, scrn_height))
