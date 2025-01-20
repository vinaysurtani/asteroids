import os
import sys

from asteroidfield import AsteroidField
from shot import Shot
os.environ["SDL_AUDIODRIVER"] = "dummy"
from asteroid import Asteroid
from player import Player, shots_group
import pygame 
from constants import *

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()
	Shot.containers = (updatable, drawable, shots_group)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		for update in updatable:
			update.update(dt)
		for asteroid in asteroids:
			if asteroid.collides(player) == True:
				print("Game over!")
				sys.exit(0)
			for shot in shots_group:
				if shot.collides(asteroid) == True:
					shot.kill()
					asteroid.split()
		# for shot in shots_group:
		# 	shot.update(dt)
		# 	shot.draw(screen)
		for draw in drawable:
			draw.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60)/1000

if __name__ == "__main__":
	main()
