
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
brown =(128, 110,  98)
white =(255, 255, 255)

BLOCKSIZE = 20
BOARD_X = 50
BOARD_Y = 50
PLAYER_MVMT = BLOCKSIZE/10

#############################################################
### HELPER METHODS ###
#############################################################

def quitCheck():
	if pygame.key.get_pressed()[pygame.K_q]:
		exit()
	for event in pygame.event.get():
		if event.type == pygame.locals.QUIT: exit()

#############################################################
### SUB-CLASSES ###
#############################################################


"""
represents the basic building block of the game world.
All items are made of blocks, giving them the same hitbox.
All Blocks are 20x20 pixels.

X and Y are its locations in the board.
"""
class Block:
	def __init__(self, x, y):
		
		#static fields
		self.block_size = BLOCKSIZE
		self.dimensions = (self.block_size, self.block_size)
		self.obj = pygame.Surface(self.dimensions)
		
		#instance fields
		self.X = x
		self.Y = y

class Wall(Block):
	def __init__(self, x, y):
		Block.__init__(self, x, y)
		self.obj.fill(brown)

class Player(Block):
	def __init__(self, x, y):
		Block.__init__(self, x, y)
		self.obj.fill(red)

#############################################################
### MAIN CLASS ###
#############################################################

class Game:

	def __init__(self):
		
		self.background_color = white
		
		self.screen = pygame.display.set_mode((BLOCKSIZE*BOARD_X, BLOCKSIZE*BOARD_Y))
		
		self.board = [[0 for i in range(BOARD_X)] for j in range(BOARD_Y)]

		#create sample wall
		self.testWall = Wall(4, 4) #position. these coords are the top left pixel probably
		self.board[4][4] = 1 #y, x

		self.player = Player(2, 2)

	def playerMove(self):
		sleep(0.01)
		p = self.player

		loc = (p.Y, p.X)
		#loc is upper left pixel
		grid_loc = (int(p.Y/BLOCKSIZE), int(p.X/BLOCKSIZE))
		print("loc:",loc)
		print("grid_loc:",grid_loc)

		if pygame.key.get_pressed()[pygame.K_LEFT]:
			#if the pixel to the left of loc or the pixel to the left of loc and 20 down is == 1,
			if self.board[int(p.Y/BLOCKSIZE)][int((p.X-1)/BLOCKSIZE)] == 1 or self.board[int((p.Y+19)/BLOCKSIZE)][int((p.X-1)/BLOCKSIZE)] == 1:
				pass
			else:
				p.X-=PLAYER_MVMT
			
		elif pygame.key.get_pressed()[pygame.K_RIGHT]:
			#if the pixel to the right of loc+20x is 1 or the pixel to the right of loc+20x+20y is 1
			if self.board[int(p.Y/BLOCKSIZE)][int((p.X+20)/BLOCKSIZE)] == 1 or self.board[int((p.Y+19)/BLOCKSIZE)][int((p.X+20)/BLOCKSIZE)] == 1:
				pass
			else:	
				p.X+=PLAYER_MVMT
		
		if pygame.key.get_pressed()[pygame.K_UP]:
			if self.board[int((p.Y-1)/BLOCKSIZE)][int(p.X/BLOCKSIZE)] == 1 or self.board[int((p.Y-1)/BLOCKSIZE)][int((p.X+19)/BLOCKSIZE)] == 1:
				pass
			else:
				p.Y-=PLAYER_MVMT
		
		elif pygame.key.get_pressed()[pygame.K_DOWN]:
			if self.board[int((p.Y+21)/BLOCKSIZE)][int(p.X/BLOCKSIZE)] == 1 or self.board[int((p.Y+21)/BLOCKSIZE)][int((p.X+19)/BLOCKSIZE)] == 1:
				pass
			else:
				p.Y+=PLAYER_MVMT

			
	def run(self):
		while 1: #core game loop
			quitCheck()

			self.screen.fill(self.background_color)

			self.playerMove()

			playerPos = (self.player.X, self.player.Y)
			self.screen.blit(self.player.obj, playerPos)

			w = self.testWall #just for shorthand/readability purposes
			wallPos = (w.X*BLOCKSIZE, w.Y*BLOCKSIZE)
			self.screen.blit(w.obj, wallPos)
			
			pygame.display.flip()
			sleep(0.02)

#############################################################
### RUN BLOCK ###
#############################################################


pygame.init()

Game().run()