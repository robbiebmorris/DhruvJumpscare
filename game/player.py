from re import X
from turtle import speed
import pygame
from settings import *
from math import *
from level import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(
            "graphics/test/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.dir = pygame.math.Vector2()
        self.speed = 5
        self.obstacle_sprites = obstacle_sprites

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
        # self.rect.center += self.dir * self.speed , had to change this for collide according to tutorial, dont understand why tho
    def move(self,speed):
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
                #why does this not work? when the bottom code is in place, the game ends when the sprite collides with an error
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
