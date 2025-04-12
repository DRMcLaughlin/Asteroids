import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	# Overriding draw method from CircleShape to draw the Asteroids
	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)

	# Overriding update method from CircleShape to handle movement of Asteroids
	def update(self, dt):
		self.position += self.velocity * dt
