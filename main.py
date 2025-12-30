import pygame
import constants
import circleshape
import sys
from logger import log_state
from logger import log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot


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
    shots = pygame.sprite.Group()
   
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
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
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid) == True:
                    log_event("asteroid_shot")
                    asteroid.kill()
                    shot.kill()
            if player.collides_with(asteroid) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        pygame.display.flip()

if __name__ == "__main__":
    main()
