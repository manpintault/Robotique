import itertools
import time
import kinematics
import pygame
from pygame.locals import *
from contextlib import closing
import pypot.robot
import constant
import init
import debug
import funcMouv

if __name__ == '__main__':

	# Activate robot motors
	constant.dxl_io.enable_torque(constant.motor_ids)

	# Initialization of the robot
	init.initLimitAngles()
	init.initMaxTorque()
	init.initRobot()

	# Initialization of interface controler
	pygame.init()
	screen = pygame.display.set_mode((constant.WINDOW_W, constant.WINDOW_H))
	fond = pygame.image.load("Array.png").convert()
	screen.blit(fond, (0, 0))
	pygame.display.flip()
	
	# Variable mouvement z for leg num 0
	zleg=constant.coords[0][2] + constant.LENGTH_MOUVEMENT_LEG

	# Statment variable to do action
	dancing = False
	move_leg = False
	avance = False
	writing = False
	writingON = False
	rotate = False
	gravityCenter = False
	standUp = False
	run=1
	print "ready"

	runing = False

	# Main of program
	while run:
		for event in pygame.event.get():
			# Catch the mouvment of mouse
			if event.type == MOUSEMOTION: 
				x = (event.pos[0] - constant.WINDOW_W/2) / constant.SCALE_PICTURE
				y = (event.pos[1] - constant.WINDOW_H/2) / constant.SCALE_PICTURE
			# Catch the button click of mouse
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					standUp = not standUp
					dancing = not dancing
			# Catch all key of keyboard
			if event.type == KEYDOWN:
				# "escape" to go out
				if event.key == pygame.K_ESCAPE:
					run=0
				# "w" to begin write step
				if event.key == pygame.K_w:
					standUp = not standUp
					writing = not writing
					writingON = False
				# "k" to begin writing
				if event.key == pygame.K_k:
					writingON = not writingON
				# "l" to move leg
				if event.key == pygame.K_l:
					standUp = not standUp
					move_leg = not move_leg
					zleg=constant.coords[0][2] + constant.LENGTH_MOUVEMENT_LEG
				# and "up" to go up leg
				if move_leg and event.key == pygame.K_UP:
					zleg = zleg + constant.LENGTH_MOUVEMENT_LEG
				# and "down" to go down leg
				if move_leg and event.key == pygame.K_DOWN:
					zleg = zleg - constant.LENGTH_MOUVEMENT_LEG
				# "a" to step Forward
				if event.key == pygame.K_a:
					avance = not avance
				# "d" to stand up
				if event.key == pygame.K_d:
					standUp = not standUp
				# "r" to rotate
				if event.key == pygame.K_r:
					rotate = not rotate
				# and "left" to rotate on left
				if rotate and event.key == pygame.K_LEFT:
					funcMouv.turnAround(constant.coords, constant.legs, constant.LENGTH_ROTATE_LEG)
				# and "right" to rotate on right
				if rotate and event.key == pygame.K_RIGHT:
					funcMouv.turnAround(constant.coords, constant.legs, -constant.LENGTH_ROTATE_LEG)
				# "g" to move gravity center
				if event.key == pygame.K_g:
					standUp = not standUp
					gravityCenter = not gravityCenter

				if event.key == pygame.K_c:
					runing = not runing

		# Condition to Stand up
		if standUp :
			funcMouv.standUp()
			standUp = not standUp

		# Condition to writing
		if writing :
			if writingON :
				funcMouv.moveCenter(constant.coords, constant.legs, x, y, constant.HEIGHT_TO_WRITE_ON)
			if not writingON :
				funcMouv.moveCenter(constant.coords, constant.legs, x, y, constant.HEIGHT_TO_WRITE_OFF)

		# Condition to move one leg
		if move_leg :
			funcMouv.moveLeg(constant.legs, 0, constant.coords[0][0]-y, constant.coords[0][1]-x, zleg)

		# Condition to dancing
		if dancing :
			funcMouv.goToDance(constant.LENGTH_DANCE, constant.FREQ_DANCE)

		# Condition to step Forward
		if(avance and (x<-constant.MOUSE_MOUVEMENT_MARGIN or x > constant.MOUSE_MOUVEMENT_MARGIN or y < -constant.MOUSE_MOUVEMENT_MARGIN or y > constant.MOUSE_MOUVEMENT_MARGIN)):
			funcMouv.doAStepForward(constant.coords, constant.legs, x, y)

		# Condition to move his gravity center
		if gravityCenter :
			funcMouv.moveGravityCenter(constant.MGCcoords, constant.legs, x, y)




		# Condition to runing
		if(runing and (x<-constant.MOUSE_MOUVEMENT_MARGIN or x > constant.MOUSE_MOUVEMENT_MARGIN or y < -constant.MOUSE_MOUVEMENT_MARGIN or y > constant.MOUSE_MOUVEMENT_MARGIN)):
			funcMouv.doABetterStepForward(constant.coords, constant.legs, x, y)

	# Deactivate robot motors
	constant.dxl_io.disable_torque(constant.motor_ids)