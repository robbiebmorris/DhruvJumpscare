import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, path):
        super().__init__(groups)
        #path = "graphics/test/rock.png"
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

class Teleporter(Tile):
    def __init__(self):
        super(Teleporter, self).__init__
    def telport(self, game):
        game.bpos_y = -720
        