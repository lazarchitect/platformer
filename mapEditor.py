
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
boardWidth = len(lines[0])

screen = pygame.display.set_mode((BLOCKSIZE*boardWidth, BLOCKSIZE*boardHeight))
		
board = [[0 for i in range(boardWidth)] for j in range(boardHeight)]

screen.fill(white)
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
	
	if pygame.mouse.get_pressed()[0] == True:
		y, x = getMouseGridLoc()
		board[y][x] = abs(board[y][x] - 1)
	
		screen.fill(white)
		blitWalls()
		pygame.display.flip()

		while pygame.mouse.get_pressed()[0] == True and (y, x) == getMouseGridLoc():
			if quitCheck():
				break
	
	if quitCheck(): break
		

with open("maps/"+mapFile+".csv", "w") as f:
	for i in board:
		line = ""
		for j in i:
			line+= str(j)+","
		f.write(line[:-1]+"\n")