# import pygame
# from settings import *
# #raccoon = Enemy(game, 100, 100, 5, player, "game/graphics/monsters/raccoon/idle/0.png")
# class Enemy():
# 	def __init__(self, game, x_pos, y_pos, speed, player, path):
#             self.player = player
#             self.dir = pygame.math.Vector2()
#             self.path = path
#             self.game1 = game
#             self.characterSpeed = speed
#             self.xpos = x_pos
#             self.ypos = y_pos
#             self.image = pygame.image.load(path)
#             self.image = pygame.transform.scale(self.image, (50, 50))
#             self.rect = self.image.get_rect(topleft=(self.xpos,self.ypos))
#         def move(self):
#             if self.xpos > self.player.rect.x:
#                 self.dir.x = 1
#             else:
#                 self.dir.x = -1
#             if self.dir.magnitude() != 0:
#                 self.dir = self.dir.normalize()
#                 self.rect.x += self.dir.x * self.characterSpeed
#                 self.rect.y += self.dir.y * self.characterSpeed
#         def run(self):
#             self.game1.screen.blit(self.image, (self.xpos, self.ypos))
#             self.move()