import pygame
import sys
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from shot import *

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt=0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots,updatable, drawable)
    
    asteroid_field = AsteroidField()
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)

    running = True
    while running:

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            
        # fill the screen with a color to wipe away anything from last frame
        screen.fill('black')


        updatable.update(dt)

        for i in asteroids:
            for bullet in shots:
                if i.collide(bullet):
                    i.split()
                    bullet.kill()

        for i in asteroids:
            if i.collide(player):
                print("Game over!")
                sys.exit()

        for i in drawable:
            i.draw(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()
        
        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60)/1000
    
    pygame.quit()

if __name__ == "__main__":
    main()