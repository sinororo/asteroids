import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self,x,y,radius,velocity):
        super().__init__(x,y,radius)
        self.velocity = velocity

    def draw(self,screen):
        pygame.draw.circle(surface=screen,
                            color='yellow',
                            center=self.position,
                            radius=self.radius,
                            width=2)

    def update(self,dt):
        self.position += self.velocity * dt