import constant
import time
import numpy
import kinematics
import itertools
import math

def faitUnPasAvant(coords, pates, x, y):
	moveCenter(coords, pates, x, y, 0)
	time.sleep(constant.TIME_SLEEP)
	for i in range(constant.NB_PATES/2):
		newAngles = constant.dxl_io.get_present_position(pates[i])
		newCoords = kinematics.computeDK(newAngles[0], newAngles[1], newAngles[2])
		moveLigneDroite(newCoords, pates[i], 0, 0, constant.HEIGHT_TO_MOVE)
		newAngles = constant.dxl_io.get_present_position(pates[i+(constant.NB_PATES/2)])
		newCoords = kinematics.computeDK(newAngles[0], newAngles[1], newAngles[2])
		moveLigneDroite(newCoords, pates[i+(constant.NB_PATES/2)], 0, 0, constant.HEIGHT_TO_MOVE)
		time.sleep(constant.TIME_SLEEP)
		moveLeg(pates, i, coords[i][0], coords[i][1], coords[i][2] + constant.HEIGHT_TO_MOVE)
		moveLeg(pates, i+(constant.NB_PATES/2), coords[i+(constant.NB_PATES/2)][0], coords[i+(constant.NB_PATES/2)][1], coords[i+(constant.NB_PATES/2)][2] + constant.HEIGHT_TO_MOVE)
		time.sleep(constant.TIME_SLEEP)
		moveLeg(pates, i, coords[i][0], coords[i][1], coords[i][2])
		moveLeg(pates, i+(constant.NB_PATES/2), coords[i+(constant.NB_PATES/2)][0], coords[i+(constant.NB_PATES/2)][1], coords[i+(constant.NB_PATES/2)][2])
		time.sleep(constant.TIME_SLEEP)


def tournerLesPates(coords, pates, x):
	#Pour chaque paire de pates
	for i in range(constant.NB_PATES/2):
		#On leve la pate
		moveLeg(pates, i, coords[i][0], coords[i][1], coords[i][2] + constant.HEIGHT_TO_MOVE)
		moveLeg(pates, i+(constant.NB_PATES/2), coords[i+(constant.NB_PATES/2)][0], coords[i+(constant.NB_PATES/2)][1], coords[i+(constant.NB_PATES/2)][2] + constant.HEIGHT_TO_MOVE)
		time.sleep(constant.TIME_SLEEP)

		#On fait une rotation de x degre
		angles1 = kinematics.computeIK(coords[i][0], coords[i][1], coords[i][2])
		angles1[0] = angles1[0] + x
		newCoords1 = kinematics.computeDK(angles1[0], angles1[1], angles1[2])

		angles2 = kinematics.computeIK(coords[i+(constant.NB_PATES/2)][0], coords[i+(constant.NB_PATES/2)][1], coords[i+(constant.NB_PATES/2)][2])
		angles2[0] = angles2[0] + x
		newCoords2 = kinematics.computeDK(angles2[0], angles2[1], angles2[2])

		moveLeg(pates, i, newCoords1[0], newCoords1[1], newCoords1[2] + constant.HEIGHT_TO_MOVE)
		moveLeg(pates, i+(constant.NB_PATES/2), newCoords2[0], newCoords2[1], newCoords2[2] + constant.HEIGHT_TO_MOVE)
		time.sleep(constant.TIME_SLEEP)

		#on rabaisse la pate
		moveLeg(pates, i, newCoords1[0], newCoords1[1], newCoords1[2])
		moveLeg(pates, i+(constant.NB_PATES/2), newCoords2[0], newCoords2[1], newCoords2[2])
		time.sleep(constant.TIME_SLEEP)

	for i in range(constant.NB_PATES/2):
		moveLeg(pates, i, coords[i][0], coords[i][1], coords[i][2])
		moveLeg(pates, i+ (constant.NB_PATES/2), coords[i+(constant.NB_PATES/2)][0], coords[i+(constant.NB_PATES/2)][1], coords[i+(constant.NB_PATES/2)][2])


def moveLeg(pates, numPate, x, y, z):
	angles = kinematics.computeIK(x, y, z)
	pos = dict(zip(pates[numPate], angles))
	constant.dxl_io.set_goal_position(pos)


def moveTestRotate(maxx, freq):
	moveCenter(constant.MGCcoords, constant.pates, -maxx*numpy.sin(freq*time.time()*2*numpy.pi), -maxx*numpy.cos(freq*time.time()*2*numpy.pi), -maxx*numpy.cos(freq*time.time()*2*numpy.pi))

	"""
CECI EST EN TEST J'ESSAIE DE LUI FAIRE LEVER 2 PATTES EN SINUSOIDE PENDANT QU'IL FAIT SA DANCE :)

	for i in range(constant.NB_PATES):
		if i == 0:
			moveLigneDroite(constant.coords[i], constant.pates[i], 0, 0, 20 + varSin)
		if i == 3:
			moveLigneDroite(constant.coords[i], constant.pates[i], 0, 0, 20 + varSin)
	print 20 + varSin*10
	time.sleep(0.1)

def moveTestCenter(coords, pates, x, y, z):
	for i in range(constant.NB_PATES):
		if i == 1:
			moveLigneDroite(coords[i], pates[i], y, x, z)
		if i == 2:
			moveLigneDroite(coords[i], pates[i], y, x, z)
		if i == 4:
			moveLigneDroite(coords[i], pates[i], -y, -x, z)
		if i == 5:
			moveLigneDroite(coords[i], pates[i], -y, -x, z)

"""

def moveCenter(coords, pates, x, y, z):
	for i in range(constant.NB_PATES):
		if i == 0:
			moveLigneDroite(coords[i], pates[i], x, -y, z)
		if i == 1:
			moveLigneDroite(coords[i], pates[i], y, x, z)
		if i == 2:
			moveLigneDroite(coords[i], pates[i], y, x, z)
		if i == 3:
			moveLigneDroite(coords[i], pates[i], -x, y, z)
		if i == 4:
			moveLigneDroite(coords[i], pates[i], -y, -x, z)
		if i == 5:
			moveLigneDroite(coords[i], pates[i], -y, -x, z)
	time.sleep(constant.TIME_SLEEP_DANCE)

def moveLigneDroite(coords, numPate, x, y, z):
		angles = kinematics.computeIK(coords[0]+x, coords[1]+y, coords[2]+z)
		pos = dict(zip(numPate, angles))
		constant.dxl_io.set_goal_position(pos)

def moveOnZ(coords, numPate, z):
		angles = kinematics.computeIK(coords[0], coords[1], coords[2]-z)
		pos = dict(zip(numPate, angles))
		constant.dxl_io.set_goal_position(pos)

def moveGravityCenter(coords, pates, x, y):
	varX = x*math.cos(constant.DIAGONAL_LEG_ANGLE)
	for i in range(constant.NB_PATES):
		if i == 0:
			moveOnZ(coords[i], pates[i], x)
		if i == 1:
			moveOnZ(coords[i], pates[i], y + varX)
		if i == 2:
			moveOnZ(coords[i], pates[i], y - varX)
		if i == 3:
			moveOnZ(coords[i], pates[i], -x)
		if i == 4:
			moveOnZ(coords[i], pates[i], -y - varX)
		if i == 5:
			moveOnZ(coords[i], pates[i], -y + varX)
	time.sleep(constant.TIME_SLEEP)

def standUp():
	for i in range(constant.NB_PATES):
		moveLeg(constant.pates, i, constant.coords[i][0], constant.coords[i][1], constant.coords[i][2])