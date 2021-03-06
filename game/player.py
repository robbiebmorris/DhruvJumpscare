from re import X
from turtle import speed
import pygame
from settings import *
from math import *
from level import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        self.leftward = True
        self.counter = 8
        self.walking = False
        super().__init__(groups)
        self.image = pygame.image.load(
            "game/graphics/test/TheWizard.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.dir = pygame.math.Vector2()
        self.speed = 7
        self.obstacle_sprites = obstacle_sprites

    def input(self):
        arr = pygame.key.get_pressed()

        if ((arr[pygame.K_UP] == 1) or (arr[pygame.K_w] == 1)):
            self.dir.y = -1
            self.counter += 1
            if self.counter > 8:
                if self.walking == False:
                    if self.leftward == True:
                        self.image = pygame.image.load("game/graphics/test/wizard-down.png").convert_alpha()
                        self.walking = True
                        self.counter = 0
                    if self.leftward == False:
                        self.image = pygame.image.load("game/graphics/test/wizard-downRight.png").convert_alpha()
                        self.walking = True
                        self.counter = 0
                else:
                    if self.leftward == True:
                        self.image = pygame.image.load("game/graphics/test/TheWizard.png").convert_alpha()
                        self.walking = False
                        self.counter = 0
                    if self.leftward == False:
                        self.image = pygame.image.load("game/graphics/test/WizardRight.png").convert_alpha()
                        self.walking = False
                        self.counter = 0
        elif ((arr[pygame.K_DOWN] == 1) or (arr[pygame.K_s] == 1)):
            self.dir.y = 1
            self.counter += 1
            if self.counter > 8:
                if self.walking == False:
                    if self.leftward == True:
                        self.image = pygame.image.load("game/graphics/test/wizard-down.png").convert_alpha()
                        self.walking = True
                        self.counter = 0
                    if self.leftward == False:
                        self.image = pygame.image.load("game/graphics/test/wizard-downRight.png").convert_alpha()
                        self.walking = True
                        self.counter = 0
                else:
                    if self.leftward == True:
                        self.image = pygame.image.load("game/graphics/test/TheWizard.png").convert_alpha()
                        self.walking = False
                        self.counter = 0
                    if self.leftward == False:
                        self.image = pygame.image.load("game/graphics/test/WizardRight.png").convert_alpha()
                        self.walking = False
                        self.counter = 0
        else:
            self.dir.y = 0

        if (arr[pygame.K_LEFT] == 1 or arr[pygame.K_a] == 1):
            self.dir.x = -1
            self.leftward = True
            if (arr[pygame.K_UP] == 0) and (arr[pygame.K_w] == 0) and (arr[pygame.K_DOWN] == 0) and (arr[pygame.K_s] == 0):
                self.counter += 1
                if self.counter > 8:
                    if self.walking == False:
                        self.image = pygame.image.load("game/graphics/test/wizard-down.png").convert_alpha()
                        self.walking = True
                        self.counter = 0
                    else: 
                        self.image = pygame.image.load("game/graphics/test/TheWizard.png").convert_alpha()
                        self.walking = False
                        self.counter = 0
        elif ((arr[pygame.K_RIGHT] == 1) or (arr[pygame.K_d])):
            self.dir.x = 1
            self.leftward = False
            if (arr[pygame.K_UP] == 0) and (arr[pygame.K_w] == 0) and (arr[pygame.K_DOWN] == 0) and (arr[pygame.K_s] == 0):
                self.counter += 1
                if self.counter > 8:
                    if self.walking == False:
                            self.image = pygame.image.load("game/graphics/test/wizard-downRight.png").convert_alpha()
                            self.walking = True
                            self.counter = 0
                    else: 
                            self.image = pygame.image.load("game/graphics/test/WizardRight.png").convert_alpha()
                            self.walking = False
                            self.counter = 0
        else:
            self.dir.x = 0
        # self.rect.center += self.dir * self.speed , had to change this for collide according to tutorial, dont understand why tho

    def move(self, speed):
        if self.dir.magnitude() != 0:
            self.dir = self.dir.normalize()
        self.rect.x += self.dir.x * speed
        self.collide("h")
        self.rect.y += self.dir.y * speed
        self.collide("v")

    def collide(self, dir):
        for sprite in self.obstacle_sprites:
            if dir == "h":
                if sprite.rect.colliderect(self.rect):
                    if self.dir.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.dir.x < 0:
                        self.rect.left = sprite.rect.right
            if dir == "v":
                if sprite.rect.colliderect(self.rect):
                    if self.dir.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.dir.y < 0:
                        self.rect.top = sprite.rect.bottom
                # why does this not work? when the bottom code is in place, the game ends when the sprite collides with an error
                # if self.dir.x > 0:
                #     self.rect = sprite.rect.left
                # if self.dir.x < 0:
                #     self.rect = sprite.rect.right
                # if self.dir.y > 0:
                #     self.rect = sprite.rect.top
                # if self.dir.y < 0:
                #     self.rect = sprite.rect.bottom

    def update(self):
        self.input()
        self.move(self.speed)
