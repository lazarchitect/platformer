
from resources import *
import pygame

mapFile = input("Which board? >>")

try:        
	f = open("maps/"+mapFile+".csv", "r")
except FileNotFoundError:
	print("no board by that name here")
	exit()    

lines = f.readlines()
f.close()

boardHeight = len(lines)
boardWidth = len(lines[0].split(","))

screen = pygame.display.set_mode((BLOCKSIZE*boardWidth, BLOCKSIZE*boardHeight))
		
board = [[0 for i in range(boardWidth)] for j in range(boardHeight)]

screen.fill(white)
#TODO: add buttons for modifying screen dimensions
pygame.display.flip()

for i in range(len(lines)):
	vals = lines[i].split(",")
	for j in range(len(vals)):
		if int(vals[j]) == 1:
			board[i][j] = 1
			x = pygame.Surface((BLOCKSIZE, BLOCKSIZE))
			x.fill(brown)
			screen.blit(x, (j*BLOCKSIZE, i*BLOCKSIZE))

def blitWalls():
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 1:
				x = pygame.Surface((BLOCKSIZE, BLOCKSIZE))
				x.fill(brown)
				screen.blit(x, (j*BLOCKSIZE, i*BLOCKSIZE))

pygame.display.flip()

while 1:
	
	"""
	IF THE MOUSE IS PUSHED DOWN
		GET THE CURRENT BLOCK'S STATUS
		THEN, WHILE THE MOUSE IS _HELD_ DOWN,
			TOGGLE ANY BLOCKS UNDER THE MOUSE THAT MATCH THE STATUS
	"""

	if pygame.mouse.get_pressed()[0] == True:
		y, x = getMouseGridLoc()
		status = board[y][x]
		while pygame.mouse.get_pressed()[0] == True:
			y, x = getMouseGridLoc()
			
			#a little unclear as to why, but these quitchecks are integral. without them, the program crashes.
			#if python hits an infinite loop thats too bare, it gets ahead of itself.
			if quitCheck(): break
			
			if board[y][x] == status:
				board[y][x] = abs(board[y][x] - 1) #toggler
				screen.fill(white)
				blitWalls()
				pygame.display.flip()
	
	if quitCheck(): break

with open("maps/"+mapFile+".csv", "w") as f:
	for i in board:
		line = ""
		for j in i:
			line+= str(j)+","
		f.write(line[:-1]+"\n")