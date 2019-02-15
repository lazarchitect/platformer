
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
PLAYER_MVMT = BLOCKSIZE/10


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




####
if __name__ == "__main__":
	print("Dont run the resources file ya dimbis")