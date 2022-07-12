import pygame, sys
from level import Level
from settings import *
from sys import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700,700))
        pygame.display.set_caption('Dhruv Jumpscare')
        self.clock = pygame.time.Clock()
        self.level = Level()
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                    sys.exit()
            self.screen.fill("black")
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
            
if __name__ == '__main__':
    game = Game()
    game.run()