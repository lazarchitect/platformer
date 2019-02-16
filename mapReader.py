
#from resources import *
#import pygame
		
try:        
	f = open("maps/"+input("Which board? >>")+".csv", "r")
except FileNotFoundError:
	print("no board by that name here")
	exit()    

lines = f.readlines()
f.close()


#screen = pygame.display.set_mode((BLOCKSIZE*BOARD_X, BLOCKSIZE*BOARD_Y))
#screen.fill(white)

for i in range(len(lines)):
	vals = lines[i].split(",")
	for j in range(len(vals)):
		if int(vals[j]) == 1:
			x = pygame.Surface((BLOCKSIZE, BLOCKSIZE))
			x.fill(brown)
			screen.blit(x, (j*BLOCKSIZE, i*BLOCKSIZE))


#pygame.display.flip()
		

#while 1:
#	if quitCheck():
#		break
