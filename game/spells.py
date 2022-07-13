import pygame
import sys
from level import Level
from settings import *
from tile import *
from player import *
from sys import *
from button import *


def checkSpell(button, game):
    if button.external == True:
        button.counter += 1
        path = "game/graphics/test/Crossheir.png"
        if button.var1 == False:
            button.x, button.y = pygame.mouse.get_pos()
        crossheir = Button(button.x-32, button.y - 32, path)
        crossheir.draw(game)
    if pygame.mouse.get_pressed()[0] == 1 and button.counter > 120:
        button.var1 = True
        button.counter = 0
