import pygame
from level import *
from settings import *
from tile import *
from player import *


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.w, self.h = self.surface.get_size()
        print(self.w)
        print(self.h)

    def camera_draw(self, player):

        player_x = player.rect.centerx - (self.w / 2)
        player_y = player.rect.centery - (self.h / 2)

        for sprite in self.sprites():
            objectx = sprite.rect.centerx - player_x
            objecty = sprite.rect.centery - player_y
            self.surface.blit(sprite.image, (objectx, objecty))
