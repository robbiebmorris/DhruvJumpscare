import pygame, sys
from level import Level
from settings import *
from tile import *
from player import *
from sys import *

class Button(pygame.sprite.Group):
    def __init__(self, x, y, path):
        self.a = 0
        self.b = 0
        self.x = x
        self.y = y
        self.path = path
        self.var1 = False
        self.counter = 0
        self.external = False
        #ex. path = "graphics/test/rock.png"
        self.image = pygame.image.load(self.path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)

        # self.width = self.image.get_width()
        # self.height = self.image.get_height()
        self.clicked = False
    def draw(self, game):
        self.pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(self.pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked ==False:
                print("clicked")
                self.clicked = True
                self.external = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        game.screen.blit(self.image,(self.rect.x,self.rect.y))

