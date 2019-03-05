
import pygame
import pygame.locals

#############################################################
### CONSTANTS ###
#############################################################

red =  (255,   0,   0)
teal = (  0, 128, 128)
brown =(128, 110,  98)
white =(255, 255, 255)

GFORCE = 0.2
BLOCKSIZE = 20
PLAYER_MVMT = 6
PLAYER_JUMP = 6
GAMESPEED = 2

toolbarHeight = 40


#############################################################
### HELPER METHODS ###
#############################################################

def quitCheck():
	if pygame.key.get_pressed()[pygame.K_q]:
		pygame.quit()
		return True
	for event in pygame.event.get():
		if event.type == pygame.locals.QUIT: 
			pygame.quit()
			return True

#finds the mouse position in the pygame screen
#returns: a tuple containing the y, x coords
def getMouseLoc():
	coords = pygame.mouse.get_pos()
	return (coords[1], coords[0])

def getMouseGridLoc(mouse_y, mouse_x):
	mouse_grid_x = int(mouse_x/BLOCKSIZE)
	mouse_grid_y = int((mouse_y-toolbarHeight)/BLOCKSIZE)
	return (mouse_grid_y, mouse_grid_x)

#given the mouse location Y value,
#determines if the user's click was in the toolbar or the grid area.
def clickInToolbar(y):
	return y < toolbarHeight

def borderWall(row, col, boardWidth, boardHeight):
	return row == 0 or col == 0 or row+1 == boardHeight or col+1 == boardWidth

#these next few functions are just used as aliases for blocks of code in the game file because of how ugly and unreadable they are

#params: board, player
#returns if the pixel underneath the player block is a wall.
def blockUnder(bd, p):
	return bd[int((p.Y+20)/BLOCKSIZE)][int((p.X+1)/BLOCKSIZE)] == 1 or bd[int((p.Y+20)/BLOCKSIZE)][int((p.X+19)/BLOCKSIZE)] == 1

#params: board, player
#returns if the player is blocked by a Wall above it
def blockAbove(bd, p):
	return bd[int((p.Y-1)/BLOCKSIZE)][int(p.X/BLOCKSIZE)] == 1 or bd[int((p.Y-1)/BLOCKSIZE)][int((p.X+19)/BLOCKSIZE)] == 1

#params: board, player
#returns if the player is blocked by a Wall to the right
def blockRight(bd, p):
	return bd[int(p.Y/BLOCKSIZE)][int((p.X+20)/BLOCKSIZE)] == 1 or bd[int((p.Y+19)/BLOCKSIZE)][int((p.X+20)/BLOCKSIZE)] == 1

#params: board, player
#returns if the player is blocked by a Wall to the left
def blockLeft(bd, p):
	return bd[int(p.Y/BLOCKSIZE)][int((p.X-1)/BLOCKSIZE)] == 1 or bd[int((p.Y+19)/BLOCKSIZE)][int((p.X-1)/BLOCKSIZE)] == 1

################
#these next functions determine if the player block hits a wall

def isClippedRight(bd, p):
	return bd[int(p.Y/BLOCKSIZE)][int((p.X+19)/BLOCKSIZE)] == 1 or bd[int((p.Y+19)/BLOCKSIZE)][int((p.X+19)/BLOCKSIZE)] == 1

def isClippedLeft(bd, p):
	return bd[int(p.Y/BLOCKSIZE)][int(p.X/BLOCKSIZE)] == 1 or bd[int((p.Y+19)/BLOCKSIZE)][int((p.X)/BLOCKSIZE)] == 1

#its understood that the player is falling DOWN
#return true if the next frame would clip the bottom of the player (hence the +19) into the floor
def wouldLand(bd, p):
	next_Y = p.Y + 19 + p.gVeloc #where the bottom of the player block will be after 1 frame
	return bd[int(next_Y/BLOCKSIZE)][int(p.X/BLOCKSIZE)] == 1 or bd[int(next_Y/BLOCKSIZE)][int((p.X+19)/BLOCKSIZE)] == 1

#its understood that the player is flying UP
#return true if the next frame would clip the top of the player into the ceiling
def wouldBonk(bd, p):
	next_Y = p.Y + 0 + p.gVeloc #where the top of the player block will be after 1 frame
	return bd[int(next_Y/BLOCKSIZE)][int(p.X/BLOCKSIZE)] == 1 or bd[int(next_Y/BLOCKSIZE)][int((p.X+19)/BLOCKSIZE)] == 1

#############################################################
### CLASSES ###
#############################################################

class toolBarButton():
	def __init__(self):
		r = pygame.Rect()

#############################################################
### RUNNING CODE ###
#############################################################

if __name__ == "__main__":
	print("this is the resources file")