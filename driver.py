from Game import *
from resources import *
import pygame
from time import sleep

mapFile = "maps/"+input("Which board? >>")+".csv"

g = Game(mapFile) #inits a game object with the given map

"""
function that sets the game in motion.
includes the loop that pygame requires to keep the screen up.
"""
while 1: #core game loop

	if quitCheck():
		break

	playerRect = (g.player.X, g.player.Y, g.player.width, g.player.height)
	g.screen.fill(g.background_color, rect=playerRect)
	pygame.display.update(playerRect)
	
	g.gravity()
	g.playerMove() #user input
		
	playerPos = (g.player.X, g.player.Y) #reblit player at new location
	g.screen.blit(g.player.obj, playerPos)
	pygame.display.update((g.player.X, g.player.Y, g.player.width, g.player.height))
		
	sleep(0.1 / GAMESPEED)