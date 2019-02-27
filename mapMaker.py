
from resources import *
import pygame
from time import sleep
import os
		
while 1:
	try:
		boardHeight = int(input("How tall?"))
		boardWidth = int(input("How wide?"))
		break
	except TypeError:
		continue

screen = pygame.display.set_mode((BLOCKSIZE*boardWidth, BLOCKSIZE*boardHeight+toolbarHeight))
		
board = [[0 for i in range(boardWidth)] for j in range(boardHeight)]

screen.fill(white)
pygame.display.flip()

while 1:
	
	"""
	IF THE MOUSE IS PUSHED DOWN
		GET THE CURRENT BLOCK'S STATUS
		THEN, WHILE THE MOUSE IS _HELD_ DOWN,
			TOGGLE ANY BLOCKS UNDER THE MOUSE THAT MATCH THE STATUS
	"""

	if pygame.mouse.get_pressed()[0] == True:
		
		print(getMouseLoc())

		y, x = getMouseLoc()

		if clickInToolbar(y):
			#TOOLBAR CODE HERE
			pass

		else:
			grid_y, grid_x = getMouseGridLoc(y, x)
			status = board[grid_y][grid_x]
			#I establish status here so that a single click only turns walls on or off

			while pygame.mouse.get_pressed()[0] == True:
				y, x = getMouseLoc()

				if clickInToolbar(y):
					if quitCheck(): break
					pass

				else:
					grid_y, grid_x = getMouseGridLoc(y, x)
					
					#a little unclear as to why, but these quitchecks are integral. without them, the program crashes.
					#if python hits an infinite loop thats too bare, it gets ahead of itself.
					if quitCheck(): break
					
					if board[grid_y][grid_x] == status:
						board[grid_y][grid_x] = abs(board[grid_y][grid_x] - 1) #toggler

						if board[grid_y][grid_x] == 1:
							imgPath = os.path.join('imgs', 'wall.jpg')
							wall = pygame.image.load(imgPath)
							wall = pygame.transform.scale(wall, (BLOCKSIZE, BLOCKSIZE))
							screen.blit(wall, (grid_x*BLOCKSIZE, grid_y*BLOCKSIZE+toolbarHeight))
							pygame.display.update(grid_x*BLOCKSIZE, grid_y*BLOCKSIZE+toolbarHeight, BLOCKSIZE, BLOCKSIZE)
						else:
							blank = pygame.Surface((BLOCKSIZE, BLOCKSIZE))
							blank.fill(white)
							screen.blit(blank, (grid_x*BLOCKSIZE, grid_y*BLOCKSIZE+toolbarHeight))
							pygame.display.update(grid_x*BLOCKSIZE, grid_y*BLOCKSIZE+toolbarHeight, BLOCKSIZE, BLOCKSIZE)
	
	if quitCheck(): break


with open("maps/"+input("Name The File:")+".csv", "w") as f:
	for i in board:
		line = ""
		for j in i:
			line+= str(j)+","
		f.write(line[:-1]+"\n")  