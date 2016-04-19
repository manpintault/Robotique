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
import dessin

if __name__ == '__main__':

	# Activate robot motors
	constant.dxl_io.enable_torque(constant.motor_ids)

	# Initialization of the robot
	init.initLimitAngles()
	init.initTorqueLimit()
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
	# Variable of robot speed when he's running
	freq_speed_robot = constant.ROBOT_SPEED

	# Statment variable to do action
	dancing = False
	move_leg = False
	avance = False
	onPosition = False
	writing = False
	writingON = False
	rotate = False
	gravityCenter = False
	standUp = False
	runing = False
	run=1
	print "ready"

	# Main of program
	while run:
		for event in pygame.event.get():
			# Catch the mouvment of mouse
			if event.type == MOUSEMOTION: 
				x = (event.pos[0] - constant.WINDOW_W/2)
				y = (event.pos[1] - constant.WINDOW_H/2)
			# Catch the button click of mouse
			if event.type == MOUSEBUTTONDOWN and move_leg == False and avance == False and writing == False and rotate == False and gravityCenter == False and runing == False:
				if event.button == 1:
					standUp = not standUp
					dancing = not dancing
			# Catch all key of keyboard
			if event.type == KEYDOWN:
				# "escape" to go out
				if event.key == pygame.K_ESCAPE:
					run=0
				# "w" to begin write step
				if event.key == pygame.K_w and move_leg == False and avance == False and dancing == False and rotate == False and gravityCenter == False and runing == False:
					standUp = not standUp
					writing = not writing
					onPosition = False
					writingON = False
				# "k" to begin writing
				if event.key == pygame.K_k:
					writingON = not writingON
				# "p" to draw Image of "dessin.png"
				if event.key == pygame.K_p and writingON == False:
					dessin.draw()
				# "l" to move leg
				if event.key == pygame.K_l and dancing == False and avance == False and writing == False and rotate == False and gravityCenter == False and runing == False:
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
				if event.key == pygame.K_a and move_leg == False and dancing == False and writing == False and rotate == False and gravityCenter == False and runing == False:
					avance = not avance
				# "d" to stand up
				if event.key == pygame.K_d:
					standUp = not standUp
				# "r" to rotate
				if event.key == pygame.K_r and move_leg == False and avance == False and writing == False and dancing == False and gravityCenter == False and runing == False:
					rotate = not rotate
				# and "left" to rotate on left
				if rotate and event.key == pygame.K_LEFT:
					funcMouv.turnAround(constant.coords, constant.legs, constant.LENGTH_ROTATE_LEG)
				# and "right" to rotate on right
				if rotate and event.key == pygame.K_RIGHT:
					funcMouv.turnAround(constant.coords, constant.legs, -constant.LENGTH_ROTATE_LEG)
				# "g" to move gravity center
				if event.key == pygame.K_g and move_leg == False and avance == False and writing == False and rotate == False and dancing == False and runing == False:
					standUp = not standUp
					gravityCenter = not gravityCenter
				# "c" to step Forward faster
				if event.key == pygame.K_c and move_leg == False and avance == False and writing == False and gravityCenter == False and dancing == False and rotate == False:
					freq_speed_robot = constant.ROBOT_SPEED
					standUp = not standUp
					runing = not runing
				# and "+" to move fastly
				if runing and event.key == pygame.K_KP_PLUS :
					if freq_speed_robot < constant.MAX_ROBOT_SPEED :
						freq_speed_robot = freq_speed_robot + constant.VARIATION_ROBOT_SPEED
					else :
						print "You can't move faster."
				# and "-" to move slowly
				if runing and event.key == pygame.K_KP_MINUS :
					if freq_speed_robot > constant.MIN_ROBOT_SPEED :
						freq_speed_robot = freq_speed_robot - constant.VARIATION_ROBOT_SPEED
					else :
						print "You can't move slower."

		# Condition to Stand up
		if standUp :
			funcMouv.standUp()
			time.sleep(constant.TIME_SLEEP_STAND_UP)
			funcMouv.standUp()
			standUp = not standUp

		# Condition to writing
		if writing :
			if (not onPosition):
				for i in range(4):
					funcMouv.moveCenter(constant.coords, constant.legs, 0, 0, i*10)
					time.sleep(constant.TIME_SLEEP_WRITING)
				onPosition = True

			if writingON :
				funcMouv.moveCenter(constant.coords, constant.legs, (x/constant.SCALE_PICTURE_OTHER), (y/constant.SCALE_PICTURE_OTHER), constant.HEIGHT_TO_WRITE_ON)
			if not writingON :
				funcMouv.moveCenter(constant.coords, constant.legs, (x/constant.SCALE_PICTURE_OTHER), (y/constant.SCALE_PICTURE_OTHER), constant.HEIGHT_TO_WRITE_OFF)

		# Condition to move one leg
		if move_leg :
			funcMouv.moveLeg(constant.legs, 0, constant.coords[0][0]-(y/constant.SCALE_PICTURE_OTHER), constant.coords[0][1]-(x/constant.SCALE_PICTURE_OTHER), zleg)

		# Condition to dancing
		if dancing :
			funcMouv.goToDance(constant.LENGTH_DANCE, constant.FREQ_DANCE)

		# Condition to step Forward
		if (avance and (x<-constant.MOUSE_MOUVEMENT_MARGIN or x > constant.MOUSE_MOUVEMENT_MARGIN or y < -constant.MOUSE_MOUVEMENT_MARGIN or y > constant.MOUSE_MOUVEMENT_MARGIN)):
			funcMouv.doAStepForward(constant.coords, constant.legs, (x/constant.SCALE_PICTURE_WALK), (y/constant.SCALE_PICTURE_WALK))

		# Condition to move his gravity center
		if gravityCenter :
			funcMouv.moveGravityCenter(constant.MGCcoords, constant.legs, (x/constant.SCALE_PICTURE_GRAVITY), (y/constant.SCALE_PICTURE_GRAVITY))

		# Condition to runing
		if runing :
			if (x<-constant.MOUSE_MOUVEMENT_MARGIN or x > constant.MOUSE_MOUVEMENT_MARGIN or y < -constant.MOUSE_MOUVEMENT_MARGIN or y > constant.MOUSE_MOUVEMENT_MARGIN) :
				funcMouv.doABetterStepForward(constant.coords, constant.legs, (x/constant.SCALE_PICTURE_RUN), (y/constant.SCALE_PICTURE_RUN), freq_speed_robot)
			else :
				funcMouv.standUp();

	# Deactivate robot motors
	constant.dxl_io.disable_torque(constant.motor_ids)