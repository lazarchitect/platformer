
import pygame
import pygame.locals

#############################################################
### CONSTANTS ###
#############################################################

red =  (255,   0,   0)
teal = (  0, 128, 128)
brown =(128, 110,  98)
white =(255, 255, 255)

BLOCKSIZE = 20
BOARD_X = 50
BOARD_Y = 50
PLAYER_MVMT = 1


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

def getMouseGridLoc():
	mouse_loc = pygame.mouse.get_pos()
	mouse_grid_x = int(mouse_loc[0]/BLOCKSIZE)
	mouse_grid_y = int(mouse_loc[1]/BLOCKSIZE)
	return (mouse_grid_y, mouse_grid_x)

#these next few functions are just used as aliases because of how ugly and unreadable they are

#params: board, player
#returns if the player is blocked by a Wall under it
def blockUnder(bd, p):
	return bd[int((p.Y+21)/BLOCKSIZE)][int(p.X/BLOCKSIZE)] == 1 or bd[int((p.Y+21)/BLOCKSIZE)][int((p.X+19)/BLOCKSIZE)] == 1

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

####
if __name__ == "__main__":
	print("this is the resources file")