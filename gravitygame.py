
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
		self.obj.fill(teal)

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
		
		self.background_color = white
		
		boardHeight = len(lines)
		boardWidth = len(lines[0].split(","))

		self.screen = pygame.display.set_mode((BLOCKSIZE*boardWidth, BLOCKSIZE*boardHeight))
		
		self.board = [[0 for i in range(boardWidth)] for j in range(boardHeight)]

		for i in range(len(lines)):
			vals = lines[i].split(",")
			for j in range(len(vals)):
				if int(vals[j]) == 1:
					self.board[i][j] = 1

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
				p.Y += p.gVeloc
				
	"""
	defines the gravity of the world of the game.
	like in the real world, there is a gravitational acceleration constant.
	its called GFORCE here.
	each second that the player is in midair, their falling accelerates at that rate.
	hitting the ground stops it.
	no params, no returns. this function runs in the game loop.
	"""
	def gravity(self):
		bd = self.board
		p = self.player

		if blockUnder(bd, p) and p.gVeloc >= 0:
			p.Y = p.Y - (p.Y % BLOCKSIZE)
			p.gVeloc = 0
			
		else:
			p.gVeloc += GFORCE
			p.gVeloc = round(p.gVeloc, 5)
			p.Y += p.gVeloc

	"""
	function that sets the game in motion.
	includes the loop that pygame requires to keep the screen up.
	"""
	def run(self):
		while 1: #core game loop
			if quitCheck():
				return

			self.screen.fill(self.background_color)
			
			self.gravity()

			self.playerMove()

			playerPos = (self.player.X, self.player.Y)
			self.screen.blit(self.player.obj, playerPos)

			for row in range(len(self.board)):
				for col in range(len(self.board[row])):
					if self.board[row][col] == 1:
						w = pygame.Surface((BLOCKSIZE, BLOCKSIZE))
						w.fill(brown)
						self.screen.blit(w, (col*BLOCKSIZE, row*BLOCKSIZE))
			
			pygame.display.flip()
			sleep(0.1 / GAMESPEED)

#############################################################
### RUN BLOCK ###
#############################################################

mapFile = "maps/"+input("Which board? >>")+".csv"

Game(mapFile).run()