import pygame
import sys
from button import Button
from level import Level
from settings import *
from sys import *
from spells import *
from ui import *
# from enemy import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.bpos_x = 0
        self.bpos_y = 0
        self.slot1 = Button(256, 0, "game/graphics/test/slot.png")
        self.background = pygame.image.load("game/graphics/tilemap/ground.png")
        self.screen.blit(self.background,(0,0))
        self.backpack = Button(20, 636, "game/graphics/test/backpack.png")
        self.map = Button(94, 636, "game/graphics/test/map.png")
        self.spellbook = Button(168, 636, "game/graphics/test/spellbook.png")
        self.settings = Button(242, 636, "game/graphics/test/settings.png")
        pygame.display.set_caption('Dhruv Jumpscare')
        # self.raccoon = Enemy(game, 100, 100, 5, player, "game/graphics/monsters/raccoon/idle/0.png")
        self.clock = pygame.time.Clock()
        self.level = Level()
        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.backpack.draw(self)
            self.map.draw(self)
            self.spellbook.draw(self)
            self.settings.draw(self)
            self.slot1.draw(self)
            self.level.run(self)
            checkSpell(self.spellbook, self)
            inventory(self.backpack, self)
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
