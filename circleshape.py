import pygame
class CircleShape(pygame.sprite.Sprite):
	def __init__(self, x, y, radius):
		if hasattr(self, "containers"):
			super().__init__(self.containers) # Automatically add to sprite groups
		else:
			super().__init__()
		# Assign position and radius
		self.position = pygame.Vector2(x, y)
		self.velocity = pygame.Vector2(0, 0)
		self.radius = radius



	def draw(self, screen):
		#sub-classes must override
		pass

	def update(self, dt):
		#sub-classes must override
		pass


	# Handling player collisions with asteroids
	def check_collision(self, Asteroid):
		distance = self.position.distance_to(Asteroid.position)
		if distance <= (self.radius + Asteroid.radius):			
			return True
		return False
