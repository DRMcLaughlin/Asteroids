import pygame
from constants import * # Imports constants such as SCREEN_WIDTH & SCREEN_HEIGHT
from circleshape import CircleShape
from player import Player # Imports Player Class
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
	# Initialize pygame
	pygame.init()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	# Set up game display and clock
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	# Time delta for smooth movement
	dt = 0

	# Create groups for sprite management
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()



	#Set Player's containers to add instances to both groups
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable

	# Instantiate the Asteroid Field
	asteroid_field = AsteroidField()

	# Create the player instance (added automatically to both groups)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	# Main game loop
	while True:
		# Handle events
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # Quits the game  if requested
				return

		updatable.update(dt)
		
		for asteroid in asteroids:
			if player.check_collision(asteroid):
				print("Game over!")
				import sys
				sys.exit()		

		# Clear the screen
		screen.fill("black")


		# Draws objects
		for object in drawable:
			object.draw(screen)


		pygame.display.flip()
		dt = clock.tick(60) / 1000
if __name__ == "__main__":
	main()


