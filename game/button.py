import pygame, sys
from level import Level
from settings import *
from tile import *
from player import *
from sys import *

class Button():
    def __init__(self, x, y, path):
        self.image = path
        #ex. path = "graphics/test/rock.png"
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        # self.width = self.image.get_width()
        # self.height = self.image.get_height()
        self.clicked = False
    def draw(self, game):

        self.pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(self.pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked ==False:
                print("clicked")
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        game.screen.blit(self.image,(self.rect.x,self.rect.y))

