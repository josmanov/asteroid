import pygame
import constants 
from logger import log_state
from player import Player
import circleshape
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print("Screen width:", constants.SCREEN_WIDTH)
    print("Screen height:", constants.SCREEN_HEIGHT)

    pygame.init()

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
   
    Asteroid.containers = (asteroids, updatable, drawable)

    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    # asteroids = Asteroid(
    #    constants.SCREEN_WIDTH / 2,
    #    constants.SCREEN_HEIGHT / 2,
    #    constants.ASTEROID_MIN_RADIUS
    #    )
    asteroid_field = AsteroidField()

    while (1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting game...")
                return
        log_state()
        dt = clock.tick(60) / 1000
        player.update(dt)
        screen.fill("black", None, 0)
        for item in drawable:
            item.draw(screen)
        for item in updatable:
            item.update(dt)
        pygame.display.flip()

if __name__ == "__main__":
    main()
