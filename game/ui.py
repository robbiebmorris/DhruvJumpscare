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
        path = "game/graphics/test/Inventory.png"
        crossheir = Button(0, 0, path)
        crossheir.draw(game)
    if pygame.mouse.get_pressed()[0] == 1 and button.counter > 120:
        button.var1 = True
        button.counter = 0
