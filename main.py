import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
    clock = pygame.time.Clock()
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteriods = pygame.sprite.Group()
    

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteriods, updateable, drawable)
    AsteroidField.containers = (updateable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteriod_field = AsteroidField()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)

        for asteroid in asteriods:
            if asteroid.has_collided(player):
                sys.exit("Game over!")

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
       

        pygame.display.flip() 
        #limit the framerate
        dt = clock.tick(60)/1000
        


if __name__ == "__main__":
    main()
