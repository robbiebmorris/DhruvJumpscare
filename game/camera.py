import pygame
from level import *
from settings import *
from tile import *
from player import *
from button import *



class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.w, self.h = self.surface.get_size()
        print(self.w)
        print(self.h)

    def camera_draw(self, player, game):        
        player_x = player.rect.centerx - (self.w / 2)
        player_y = player.rect.centery - (self.h / 2)
        game.screen.blit(game.background, (game.bpos_x - player_x, game.bpos_y - player_y))
        pygame.image.load(game.backpack.path).convert_alpha()
        # game.screen.blit(game.backpack, ((20- player_x), (636- player_y)))
        # game.backpack = Button((20- player_x), (636- player_y), "game/graphics/test/backpack.png")
        # game.map = Button((94- player_x), (636- player_y), "game/graphics/test/map.png")
        # game.spellbook = Button((168- player_x) , (636- player_y), "game/graphics/test/spellbook.png")
        # game.settings = Button((636- player_y), (636- player_y), "game/graphics/test/settings.png")
        for sprite in self.sprites():
            objectx = sprite.rect.centerx - player_x
            objecty = sprite.rect.centery - player_y
            self.surface.blit(sprite.image, (objectx, objecty))
