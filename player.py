import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot
class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS) # Initialize CircleShape with position and radius
		self.rotation = 0 # Initial rotation state
		self.position = pygame.Vector2(x, y)



	def triangle(self):
		# Define the three points of the triangle based on rotation and position
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

		# Position the triangle points relative to the 'rect.center'
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def update(self, dt):
		keys = pygame.key.get_pressed()
		
		Shot.shot_cooldown = max(0, Shot.shot_cooldown - dt)

		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(dt)
		if keys[pygame.K_SPACE]:
			self.shoot()

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt


	def shoot(self):
		if Shot.shot_cooldown == 0:
			new_shot = Shot(self.position.x, self.position.y)
			velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
			new_shot.velocity = velocity
			Shot.shot_cooldown += 0.3
			return new_shot
			
			
	
