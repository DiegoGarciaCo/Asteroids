import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            vector_one = self.velocity.rotate(angle)
            vector_two = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            first_asteroid.velocity = vector_one * 1.2
            second_asteroid.velocity = vector_two * 1.2

    def update(self, dt):
        self.position += self.velocity * dt 

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)