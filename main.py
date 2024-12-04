import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Shot.containers = (bullets, updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))
        for draw in drawable:
            draw.draw(screen)
        for update in updatable:
            update.update(dt)
        for asteroid in asteroids:
            if asteroid.collide(player):
                raise SystemExit("Game Over!")
            for bullet in bullets:
                if bullet.collide(asteroid):
                    bullet.kill()
                    asteroid.split()

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
    



if __name__ == "__main__":
    main()