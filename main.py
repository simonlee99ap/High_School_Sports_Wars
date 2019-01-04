import sys, pygame
from player_class import *
from projectile_class import *
import settings

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

	if keys[pygame.K_RIGHT]:
		player1.move_right()

	if keys[pygame.K_UP]:
		player1.isJump = True

	if player1.isJump:
		player1.jump()


	#prevents the tracing of the character as it moves
	scrn.fill((0,0,0))

	for bullet in player1.bullets:
		bullet.draw()

	player1.draw()
	pygame.display.update()