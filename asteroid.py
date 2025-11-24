import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        random_angle = random.uniform(20, 50)

        child_1_velocity = self.velocity.rotate(random_angle)
        child_2_velocity = self.velocity.rotate(-random_angle)
        children_radius = self.radius - ASTEROID_MIN_RADIUS

        child_1 = Asteroid(self.position.x, self.position.y, children_radius)
        child_1.velocity = child_1_velocity * 1.2
        child_2 = Asteroid(self.position.x, self.position.y, children_radius)
        child_2.velocity = child_2_velocity * 1.2