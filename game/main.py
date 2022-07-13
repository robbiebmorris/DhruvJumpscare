import pygame, sys
from button import Button
from level import Level
from settings import *
from sys import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        self.background = pygame.image.load("graphics/tilemap/ground.png")
        pygame.display.set_caption('Dhruv Jumpscare')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.backpack = Button(20, 636, "graphics/test/backpack.png")
        self.map = Button(94, 636, "graphics/test/map.png")
        self.spellbook = Button(168, 636, "graphics/test/spellbook.png")
        self.settings = Button(242,636,"graphics/test/settings.png" )
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                    sys.exit()
            self.screen.blit(self.background, (0, 0))
            self.backpack.draw(self)
            self.map.draw(self)
            self.spellbook.draw(self)
            self.settings.draw(self)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
            
if __name__ == '__main__':
    game = Game()
    game.run()

