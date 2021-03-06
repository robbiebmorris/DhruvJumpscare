import pygame
from settings import *
from tile import *
from player import *
from camera import *


class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = CameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == "b":
                    Tile((x, y), [self.obstacle_sprites],
                         "game/graphics/test/Blank.png")
                if col == 'x':
                    Tile((x, y), [self.visible_sprites,
                         self.obstacle_sprites], "game/graphics/test/rock.png")
                if col == 'p':
                    self.player = Player(
                        (x, y), [self.visible_sprites], self.obstacle_sprites)
                if col == "t":
                    Tile((x, y), [self.obstacle_sprites],
                         "game/graphics/test/Blank.png")

    def run(self, game):
        # update and draw the game
        self.visible_sprites.camera_draw(self.player, game)
        self.visible_sprites.update()
