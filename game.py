
#############################################################
### IMPORTS ###
#############################################################

import pygame
import pygame.locals
from time import sleep

#############################################################
### CONSTANTS ###
#############################################################

red =  (255,   0,   0)
teal = (  0, 128, 128)


#############################################################
### HELPER METHODS ###
#############################################################

def quitCheck():
	for event in pygame.event.get():
		if event.type == pygame.locals.QUIT: exit()

#############################################################
### SUB-CLASSES ###
#############################################################

class Block:
	def __init__(self, x, y):
		
		#static fields
		self.block_size = 20
		self.dimensions = (self.block_size, self.block_size)
		self.obj = pygame.Surface(self.dimensions)
		
		#instance fields
		self.X = x
		self.Y = y

class Player(Block):
	def __init__(self, x, y):
		Block.__init__(self, x, y)

#############################################################
### MAIN CLASS ###
#############################################################

class Game:

	def __init__(self):
		
		self.background_color = teal
		
		self.screen = pygame.display.set_mode((1000, 600))
		
		self.board = None
		
		self.makeWalls("wallfile.csv")
		
		self.player = Player(10, 10)

	def makeWalls(self, wallFile):
		print(self)

	def playerMove(self):
		if pygame.key.get_pressed()[pygame.K_LEFT]:
			self.player.X -= 2
			
		elif pygame.key.get_pressed()[pygame.K_RIGHT]:
			self.player.X += 2
			
		if pygame.key.get_pressed()[pygame.K_UP]:
			self.player.Y -= 2
			self.background_color = red
			
		elif pygame.key.get_pressed()[pygame.K_DOWN]:
			self.player.Y += 2
			self.background_color = teal
			
	def run(self):
		while 1: #core game loop
			quitCheck()

			self.screen.fill(self.background_color)

			self.playerMove()

			playerPos = (self.player.X, self.player.Y)

			self.screen.blit(self.player.obj, playerPos)
			
			pygame.display.flip()
			sleep(0.02)

#############################################################
### RUN BLOCK ###
#############################################################


pygame.init()

Game().run()