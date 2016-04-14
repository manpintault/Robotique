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

	init.initLimitAngles()
	constant.dxl_io.enable_torque(constant.motor_ids)
	init.initRobot()
	pygame.init()
	fenetre = pygame.display.set_mode((constant.WINDOW_W, constant.WINDOW_H))
	fond = pygame.image.load("Array.png").convert()
	fenetre.blit(fond, (0, 0))
	pygame.display.flip()
	print "ready"
	run=1

	# Variable mouvement z for pate num 0
	zleg=constant.coords[0][2] + constant.LENGTH_MOUVEMENT_LEG

	dancing = False
	move_leg = False
	avance = False
	writing = False
	writingON = False
	rotate = False
	gravityCenter = False
	standUp = False

	while run:
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == MOUSEMOTION: #Si mouvement de souris
				x = (event.pos[0] - constant.WINDOW_W/2) / constant.SCALE_PICTURE
				y = (event.pos[1] - constant.WINDOW_H/2) / constant.SCALE_PICTURE
				print x
				print y
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					standUp = not standUp
					dancing = not dancing
			if event.type == KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					run=0
				if event.key == pygame.K_w:
					standUp = not standUp
					writing = not writing
					writingON = False
				if event.key == pygame.K_k:
					writingON = not writingON
				if event.key == pygame.K_l:
					standUp = not standUp
					move_leg = not move_leg
					zleg=constant.coords[0][2] + constant.LENGTH_MOUVEMENT_LEG
				if event.key == pygame.K_a:
					avance = not avance
				if move_leg and event.key == pygame.K_UP:
					zleg = zleg + constant.LENGTH_MOUVEMENT_LEG
				if move_leg and event.key == pygame.K_DOWN:
					zleg = zleg - constant.LENGTH_MOUVEMENT_LEG
				if event.key == pygame.K_d:
					standUp = not standUp
				if event.key == pygame.K_r:
					rotate = not rotate
				if rotate and event.key == pygame.K_LEFT:
					funcMouv.tournerLesPates(constant.coords, constant.pates, constant.LENGTH_MOUVEMENT_LEG)
				if rotate and event.key == pygame.K_RIGHT:
					funcMouv.tournerLesPates(constant.coords, constant.pates, -constant.LENGTH_MOUVEMENT_LEG)
				if event.key == pygame.K_g:
					standUp = not standUp
					gravityCenter = not gravityCenter

		if standUp :
			funcMouv.standUp()
			standUp = not standUp

		if writing :
			if writingON :
				funcMouv.moveCenter(constant.coords, constant.pates, x, y, constant.HEIGHT_TO_WRITE_ON)
			if not writingON :
				funcMouv.moveCenter(constant.coords, constant.pates, x, y, constant.HEIGHT_TO_WRITE_OFF)

		if move_leg :
			funcMouv.moveLeg(constant.pates, 0, constant.coords[0][0]-y, constant.coords[0][1]-x, zleg)

		if dancing :
			funcMouv.moveTestRotate(constant.LENGTH_DANCE, constant.FREQ_DANCE)

		if(avance and (x<-constant.MOUSE_MOUVEMENT_MARGIN or x > constant.MOUSE_MOUVEMENT_MARGIN or y < -constant.MOUSE_MOUVEMENT_MARGIN or y > constant.MOUSE_MOUVEMENT_MARGIN)):
			funcMouv.faitUnPasAvant(constant.coords, constant.pates, x, y)

		if gravityCenter :
			funcMouv.moveGravityCenter(constant.MGCcoords, constant.pates, x, y)




	constant.dxl_io.disable_torque(constant.motor_ids)







#			faitUnPasAvant(coord, pates, 20, 20)
#			faitUnPasAvant(coord, pates, -20, -20)
#			faitUnPasAvant(coord, pates, -20, -20)
#			faitUnPasAvant(coord, pates, 30, 0)
#			faitUnPasAvant(coord, pates, 0, -30)
#			faitUnPasAvant(coord, pates, -30, 0)

#			moveCenter(coord, pates, 10, 10, -10)

#			moveLeg(pates, 0, 100, 20, -140)

			# maxx = 10
			# freq = 4.5
			# moveTestRotate(maxx, freq)



#			moveTestLigneCote(coord, pates, 20)
#			moveTestLigneCote(coord, pates, -20)

#			time.sleep(0.1)

#			moveTestLigneDroite(coord, pates, 20)
#			moveTestLigneDroite(coord, pates, -20)



#		while 1:
#				angles = constant.dxl_io.get_present_position(j)
#				coords = kinematics.computeDK(angles[0], angles[1], angles[2])
#				newCoords = [coords[0]+30, coords[1], coords[2]]
#				angles = kinematics.computeIK(newCoords[0], newCoords[1], newCoords[2])
#				pos = dict(zip(j, angles))
#				constant.dxl_io.set_goal_position(pos)
#				time.sleep(3)

		# while 1:
		# 	for i in pates:
		# 		angles = constant.dxl_io.get_present_position(i)
		# 		coords = kinematics.computeDK(angles[0], angles[1], angles[2])
		# 		newCoords = [coords[0], coords[1], coords[2]+1]
		# 		angles = kinematics.computeIK(newCoords[0], newCoords[1], newCoords[2])
		# 		pos = dict(zip(i, angles))
		# 		constant.dxl_io.set_goal_position(pos)
		# 	time.sleep(1)



#		print 'Current pos:', constant.dxl_io.get_present_position(found_ids)

		# time.sleep(1)  # we wait for 1s





 #a = 10
  #      freq = 0.5
   #     while 1:
    #    	
     #   	angle = a*numpy.sin(freq*time.time()*2*numpy.pi)
	        # we create a python dictionnary: {id0 : position0, id1 : position1...}
	#        pos = dict(zip(found_ids, [angle, angle, angle]))
	        #print 'Cmd:', pos

	        # we send these new positions
	 #       constant.dxl_io.set_goal_position(pos)
	        #time.sleep(0.01)  # we wait for 1s

