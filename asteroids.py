import pygame
import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(surface=screen,
                            color='orange',
                            center=self.position,
                            radius=self.radius,
                            width=2)

    def update(self,dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            random_angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            initial_velocity = self.velocity
            velocity = initial_velocity * 1.2
            velocity_pos = velocity.rotate(random_angle)
            velocity_neg = velocity.rotate(-random_angle)

            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = velocity_pos
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2.velocity = velocity_neg
            