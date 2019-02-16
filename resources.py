
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
PLAYER_MVMT = int(BLOCKSIZE/8)


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


####
if __name__ == "__main__":
	import game
	game.Game().run()