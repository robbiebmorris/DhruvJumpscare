import pygame
import sys
from button import Button
from level import Level
from settings import *
from sys import *
from spells import *

def inventory(button, game):
    game.screen.blit(pygame.image.load("graphics/test/settings.png"),(242, 636))
    game.screen.blit(pygame.image.load("graphics/test/spellbook.png"), (168, 636))
    game.screen.blit(pygame.image.load("graphics/test/map.png"),(94, 636))
    game.screen.blit(pygame.image.load("graphics/test/backpack.png"),(20, 636))
    path = "graphics/test/Inventory.png"
    if button.external == True:
        button.counter += 1
        inventory = Button(0, 0, path)
        inventory.draw(game)
    if button.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1 and button.counter > 30:
        button.external = False
        button.counter = 0
