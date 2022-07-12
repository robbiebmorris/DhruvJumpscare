import pygame 
from settings import *
from tile import *
class Level:
	def __init__(self):

		self.display_surface = pygame.display.get_surface()
		self.visible_sprites = pygame.sprite.Group()
		self.obstacle_sprites = pygame.sprite.Group()
		self.create_map()

	def create_map(self):
		for row_index,row in enumerate(WORLD_MAP):
			for col_index, col in enumerate(row):
				x = col_index * TILESIZE
				y = row_index * TILESIZE
				if col == 'x':
					Tile((x,y),[self.visible_sprites],'game/graphics/test/waves.png')
	def run(self):
		# update and draw the game
		self.visible_sprites.draw(self.display_surface)