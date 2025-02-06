from constants import *
from player import Player
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create a clock object to control the frame rate
    clock = pygame.time.Clock()
    dt = 0
    
    # instantiate player obj
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        
        # update player draw
        player.draw(screen)
        
        dt = clock.tick(60) / 1000
        
        # flip
        pygame.display.flip()

if __name__ == "__main__":
    main()