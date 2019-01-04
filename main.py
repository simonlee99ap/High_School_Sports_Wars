import sys, pygame
from player_class import *
from projectile_class import *
from platform_class import *
from settings import *

pygame.init()

#screen setup
pygame.display.set_caption("High School Sports Wars")

clock = pygame.time.Clock()

#player creation
player1 = Player(100, 350, 20, 80, 8)


#main loop
while True:
	clock.tick(60)

	#exit condition
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	#eliminate the bullet when it's off the map
	for bullet in player1.bullets:
		if bullet.x < scrn_width and bullet.x > 0:
			bullet.x += bullet.speed
		else:
			player1.bullets.pop(player1.bullets.index(bullet))

	keys = pygame.key.get_pressed()

	if keys[pygame.K_SPACE]:
		player1.throw()

	if keys[pygame.K_LEFT]:
		player1.move_left()
	elif keys[pygame.K_RIGHT]:
		player1.move_right()

	if keys[pygame.K_UP]:
		player1.isJump = True

	if player1.isJump:
		player1.jump()

	#FIXME: must be a better way using OOP to optimize this process
	#       and clean up the code
	for platform in platforms:
		player1.prevent_fallthrough(platform)

	#checks if the player needs to fall
	falling = True
	for platform in platforms:
		falling = falling and not player1.on_platform(platform)

	if falling and not player1.isJump:
		player1.fall()

	else:
		#if not falling reset the fall counter
		player1.fallcount = 1

	#prevents the tracing of the character as it moves
	scrn.fill((0,0,0))

	for bullet in player1.bullets:
		bullet.draw(scrn)

	draw_platforms()
	player1.draw()
	pygame.display.update()