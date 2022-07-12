import pygame
from settings import *
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "graphics/test/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.dir = pygame.math.Vector2()
        self.speed = 5

    def input(self):
        arr = pygame.key.get_pressed()

        if (arr[pygame.K_UP] == 1):
            self.dir.y = -1
        elif (arr[pygame.K_DOWN] == 1):
            self.dir.y = 1
        else:
            self.dir.y = 0

        if (arr[pygame.K_LEFT] == 1):
            self.dir.x = -1
        elif (arr[pygame.K_RIGHT] == 1):
            self.dir.x = 1
        else:
            self.dir.x = 0

    def move(self):
        if (self.dir.x * self.dir.y != 0):
            self.dir = self.dir.normalize()
        self.rect.center += self.dir * self.speed

    def update(self):
        self.input()
        self.move()
