
from resources import *
import pygame
import os
		
try:        
	f = open("maps/"+input("Which board? >>")+".csv", "r")
except FileNotFoundError:
	print("no board by that name here")
	exit()    

lines = f.readlines()
f.close()	

boardHeight = len(lines)
boardWidth = len(lines[0].split(","))

screen = pygame.display.set_mode((BLOCKSIZE*boardWidth, BLOCKSIZE*boardHeight))
screen.fill(white)
pygame.display.flip()

for row in range(boardHeight):
	vals = lines[row].split(",")
	for col in range(len(vals)):
		if int(vals[col]) == 1:
			imgPath = os.path.join('imgs', 'wall.jpg')
			wall = pygame.image.load(imgPath)
			wall = pygame.transform.scale(wall, (BLOCKSIZE, BLOCKSIZE))
			screen.blit(wall, (row*BLOCKSIZE, col*BLOCKSIZE))
			pygame.display.update(row*BLOCKSIZE, col*BLOCKSIZE, BLOCKSIZE, BLOCKSIZE)


while 1:
	if quitCheck():
		break
