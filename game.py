import pygame
import sys
import random

pygame.init()

#---------------
WIDTH = 800
HEIGHT = 600

RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOUR = (0, 0, 0)

player_size = 50
player_position = [WIDTH/2, HEIGHT - 1.5*player_size]

enemy_size = 30
enemy_position = [random.randint(0, WIDTH - enemy_size), 0]

SPEED = 10
#----------------

#display settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
GAME_OVER = False

# frame rate
clock = pygame.time.Clock()


# Collision of the red and blue blocks
def detect_collision (player_position, enemy_position):
	p_x = player_position[0]
	p_y = player_position[1]

	e_x = enemy_position[0]
	e_y = enemy_position[1]

	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
		if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
			return True
	return False

while not GAME_OVER:
	for event in pygame.event.get() : 
		
		if event.type == pygame.QUIT:
			sys.exit()

#moving the  red block
		if event.type == pygame.KEYDOWN:

			x = player_position[0]
			y = player_position[1]

			if event.key == pygame.K_LEFT:
				x -= player_size
			elif event.key == pygame.K_RIGHT:
				x += player_size

			player_position = [x,y]

	screen.fill(BACKGROUND_COLOUR)

# Update the positions of the blue blocks AKA enemy
	if enemy_position[1] >= 0 and enemy_position[1] < HEIGHT:
		enemy_position[1] += SPEED
	else: 
		enemy_position[0] = random.randint(0, WIDTH - enemy_size)
		enemy_position[1] = 0

#the blue blocks
	pygame.draw.rect(screen, RED, (player_position[0], player_position[1], player_size, player_size))


#the red block
	pygame.draw.rect(screen, BLUE, (enemy_position[0], enemy_position[1], enemy_size, enemy_size))

	clock.tick(30)
	pygame.display.update()

# need to do the collision bit for the next time (when the two blocks meet)