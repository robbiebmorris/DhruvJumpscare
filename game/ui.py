import pygame
import sys
from button import Button
from level import Level
from settings import *
from sys import *
from spells import *

def inventory(button, game):
    if button.external == True:
        button.counter += 1
        path = "game/graphics/test/Crossheir.png"
        if button.var1 == False:
            button.a, button.b = pygame.mouse.get_pos()
        crossheir = Button(button.a, button.b - 32, path)
        crossheir.draw(game)
    if pygame.mouse.get_pressed()[0] == 1 and button.counter > 120:
        button.var1 = True
        button.path = "game/graphics/test/dhruv_icon.png"
        button.counter = 0
