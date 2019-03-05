
#############################################################
### IMPORTS ###
#############################################################

import pygame
import pygame.locals
from time import sleep
from resources import *
import os

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
		self.width = BLOCKSIZE #easily changeable variables
		self.height = BLOCKSIZE
		self.obj = pygame.transform.scale(pygame.image.load("imgs/player.jpg"), (self.width, self.height))

		self.gVeloc = 0 #gravitational downward speed
		self.midair = True #if midair, jump shouldnt work

class Enemy(Block):
	def init(self, x, y):
		Block.__init__(self, x, y)
		self.obj.fill(red)		

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
		
		self.background_color = teal
		
		boardHeight = len(lines)
		boardWidth = len(lines[0].split(","))

		self.screen = pygame.display.set_mode((BLOCKSIZE*boardWidth, BLOCKSIZE*boardHeight))
		self.screen.fill(self.background_color)
			
		self.board = [[0 for i in range(boardWidth)] for j in range(boardHeight)]
		
		#populate board doublearray with values from csv
		#and blit walls based on board values
		imgPath = os.path.join('imgs', 'wall.jpg')
		wall = pygame.image.load(imgPath)
		wall = pygame.transform.scale(wall, (BLOCKSIZE, BLOCKSIZE))
		for row in range(len(lines)):
			vals = lines[row].split(",")
			for col in range(len(vals)):
				if int(vals[col]) == 1:
					self.board[row][col] = 1
					self.screen.blit(wall, (col*BLOCKSIZE, row*BLOCKSIZE))
				#apply this code for ALL squares
				pygame.display.update(col*BLOCKSIZE, row*BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)

		self.player = Player(2*BLOCKSIZE, 2*BLOCKSIZE)

	def playerMove(self):
		bd = self.board
		p = self.player
		
		if pygame.key.get_pressed()[pygame.K_LEFT]:
			#if the pixel to the left of loc or the pixel to the left of loc and 20 down is == 1,
			if blockLeft(bd, p):
				pass
			else:
				for i in range(PLAYER_MVMT):
					p.X -= 1
					if isClippedLeft(bd, p):
						p.X += 1
						break	
					
		elif pygame.key.get_pressed()[pygame.K_RIGHT]:
			#if the pixel to the right of loc+20x is 1 or the pixel to the right of loc+20x+20y is 1
			if blockRight(bd, p):
				pass
			else:	
				for i in range(PLAYER_MVMT):
					p.X += 1
					if isClippedRight(bd, p):
						p.X -= 1
						break
		
		#you can only jump when on the ground
		if pygame.key.get_pressed()[pygame.K_UP]:
			if blockUnder(bd, p) and p.gVeloc == 0:
				p.gVeloc -= 5
				
	"""
	defines the gravity of the world of the game.
	like in the real world, there is a gravitational acceleration constant, called GFORCE.
	each second that the player is in midair, their falling accelerates at that rate.
	hitting the ground stops it.
	no params, no returns. this function runs in the game loop.
	"""
	def gravity(self):
		bd = self.board
		p = self.player

		#you are on or have fallen to the ground
		if blockUnder(bd, p) and p.gVeloc >= 0:
			p.gVeloc = 0

		#you jumped up and hit the ceiling
		elif blockAbove(bd, p):
			if blockUnder(bd, p): #if you are wedged in a 1-height tunnel
				p.Y = p.Y - (p.Y % BLOCKSIZE)
			else:
				p.gVeloc = GFORCE*3
				p.Y += p.gVeloc

		#soaring through the air, projectile qualities	
		else:
			p.gVeloc += GFORCE
			p.gVeloc = round(p.gVeloc, 5)

			#are you gonna hit the ground next frame?
			if wouldLand(bd, p):
				#place the player block on the ground
				p.Y = (p.Y - (p.Y % BLOCKSIZE)) + BLOCKSIZE

			#alternatively, are you gonna hit the ceiling next frame?
			elif wouldBonk(bd, p):
				#place the player block neatly at the ceiling w/o colliding
				p.Y = (p.Y - (p.Y % BLOCKSIZE))

			#generic projecticle movement.
			else:
				p.Y += p.gVeloc
