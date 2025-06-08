import pygame
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self, 2)
        
#    def circle(self):
#        forward = pygame.Vector2(0, 1).rotate(self.rotation)
#        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
#        a = self.position + forward * self.radius
#        b = self.position - forward * self.radius - right
#        c = self.position - forward * self.radius + right
#        return [a, b, c]

    def update(self, dt):
        self.position += self.velocity * dt
    

