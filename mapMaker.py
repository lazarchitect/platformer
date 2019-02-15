
from resources import *
import pygame
from time import sleep
		
screen = pygame.display.set_mode((BLOCKSIZE*BOARD_X, BLOCKSIZE*BOARD_Y))

screen.fill(white)
pygame.display.flip()

board = [[0 for i in range(BOARD_X)] for j in range(BOARD_Y)]

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