
#############################################################
### IMPORTS ###
#############################################################

import pygame
import pygame.locals
from time import sleep
from resources import *

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
		#walls dont *do* much

class Player(Block):
	def __init__(self, x, y):
		Block.__init__(self, x, y)
		self.obj.fill(red)

		self.gVeloc = 0 #gravitational downward speed

#############################################################
### MAIN CLASS ###
#############################################################

class Game:

	def __init__(self, mapFile):

		try:        
			f = open(mapFile, "r")
		except FileNotFoundError:
			print("no board by that name here")
			exit()    

		lines = f.readlines()
		f.close()
		
		self.background_color = white
		
		self.screen = pygame.display.set_mode((BLOCKSIZE*BOARD_X, BLOCKSIZE*BOARD_Y))
		
		self.board = [[0 for i in range(BOARD_X)] for j in range(BOARD_Y)]

		for i in range(len(lines)):
			vals = lines[i].split(",")
			for j in range(len(vals)):
				if int(vals[j]) == 1:
					self.board[i][j] = 1

		self.player = Player(2*BLOCKSIZE, 2*BLOCKSIZE)

	def playerMove(self):
		sleep(0.01)
		p = self.player
		bd = self.board
		# loc = (p.Y, p.X)
		#loc is upper left pixel
		# grid_loc = (int(p.Y/BLOCKSIZE), int(p.X/BLOCKSIZE))
		# print("loc:",loc)
		# print("grid_loc:",grid_loc)

		if pygame.key.get_pressed()[pygame.K_LEFT]:
			#if the pixel to the left of loc or the pixel to the left of loc and 20 down is == 1,
			if blockLeft(bd, p):
				pass
			else:
				p.X-=PLAYER_MVMT
			
		elif pygame.key.get_pressed()[pygame.K_RIGHT]:
			#if the pixel to the right of loc+20x is 1 or the pixel to the right of loc+20x+20y is 1
			if blockRight(bd, p):
				pass
			else:	
				p.X+=PLAYER_MVMT
		
		if pygame.key.get_pressed()[pygame.K_UP]:
			pass
            #TODO: define jump movement
		
		elif pygame.key.get_pressed()[pygame.K_DOWN]:
			# if blockUnder(bd, p):
			# 	pass
			# else:
			# 	p.Y += PLAYER_MVMT	
			pass
            #TODO: should there even be anything here? ('fast fall')

	def gravity(self):
		if blockUnder(self.board, self.player) == False:
			self.player.gVeloc += GFORCE
		else:
			self.player.gVeloc = 0
			self.player.Y = self.player.Y - (self.player.Y % 20)
	
		self.player.Y += self.player.gVeloc

	def run(self):
		while 1: #core game loop
			if quitCheck():
				return

			self.screen.fill(self.background_color)

			self.playerMove()

			self.gravity()

			playerPos = (self.player.X, self.player.Y)
			self.screen.blit(self.player.obj, playerPos)

			for row in range(len(self.board)):
				for col in range(len(self.board[row])):
					if self.board[row][col] == 1:
						w = pygame.Surface((BLOCKSIZE, BLOCKSIZE))
						w.fill(brown)
						self.screen.blit(w, (col*BLOCKSIZE, row*BLOCKSIZE))
			
			pygame.display.flip()
			sleep(0.02)

#############################################################
### RUN BLOCK ###
#############################################################

mapFile = "maps/"+input("Which board? >>")+".csv"

Game(mapFile).run()