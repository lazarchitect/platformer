
from resources import *
import pygame
from time import sleep
		
while 1:
    try:
        boardHeight = int(input("How tall?"))
        boardWidth = int(input("How wide?"))
        break
    except TypeError:
        continue

screen = pygame.display.set_mode((BLOCKSIZE*boardWidth, BLOCKSIZE*boardHeight))

screen.fill(white)
pygame.display.flip()

board = [[0 for i in range(boardWidth)] for j in range(boardHeight)]

def blitWalls():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                x = pygame.Surface((BLOCKSIZE, BLOCKSIZE))
                x.fill(brown)
                screen.blit(x, (j*BLOCKSIZE, i*BLOCKSIZE))

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

    if quitCheck():
        break

with open("maps/"+input("Name The File:")+".csv", "w") as f:
    for i in board:
        line = ""
        for j in i:
            line+= str(j)+","
        f.write(line[:-1]+"\n")  