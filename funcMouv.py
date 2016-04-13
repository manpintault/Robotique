import constant
import time
import numpy
import kinematics
import itertools

def faitUnPasAvant(coords, pates, x, y):
	moveCenter(coords, pates, x, y, 0)
	time.sleep(0.)
	for i in range(constant.NB_PATES/2):
		moveLigneDroite(coords[i], pates[i], 0, 0, constant.HEIGHT_TO_MOVE)
		moveLigneDroite(coords[i+(constant.NB_PATES/2)], pates[i+(constant.NB_PATES/2)], 0, 0, constant.HEIGHT_TO_MOVE)
		time.sleep(0.1)
		moveLeg(pates, i, coords[i][0], coords[i][1], coords[i][2] + constant.HEIGHT_TO_MOVE)
		moveLeg(pates, i+(constant.NB_PATES/2), coords[i+(constant.NB_PATES/2)][0], coords[i+(constant.NB_PATES/2)][1], coords[i+(constant.NB_PATES/2)][2] + constant.HEIGHT_TO_MOVE)
		time.sleep(0.1)
		moveLeg(pates, i, coords[i][0], coords[i][1], coords[i][2])
		moveLeg(pates, i+(constant.NB_PATES/2), coords[i+(constant.NB_PATES/2)][0], coords[i+(constant.NB_PATES/2)][1], coords[i+(constant.NB_PATES/2)][2])
		time.sleep(0.1)


def tournerLesPates(coords, pates, x):
	time.sleep(0.3)
	#Pour chaque paire de pates
	for i in range(constant.NB_PATES/2):
		#On leve la pate
		moveLeg(pates, i, coords[i][0], coords[i][1], coords[i][2] + constant.HEIGHT_TO_MOVE)
		moveLeg(pates, i+(constant.NB_PATES/2), coords[i+(constant.NB_PATES/2)][0], coords[i+(constant.NB_PATES/2)][1], coords[i+(constant.NB_PATES/2)][2] + constant.HEIGHT_TO_MOVE)
		time.sleep(0.1)

		#On fait une rotation de x degre
		angles1 = kinematics.computeIK(coords[i][0], coords[i][1], coords[i][2])
		angles1[0] = angles1[0] + x
		newCoords1 = kinematics.computeDK(angles1[0], angles1[1], angles1[2])

		angles2 = kinematics.computeIK(coords[i+(constant.NB_PATES/2)][0], coords[i+(constant.NB_PATES/2)][1], coords[i+(constant.NB_PATES/2)][2])
		angles2[0] = angles2[0] + x
		newCoords2 = kinematics.computeDK(angles2[0], angles2[1], angles2[2])

		moveLeg(pates, i, newCoords1[0], newCoords1[1], newCoords1[2] + constant.HEIGHT_TO_MOVE)
		moveLeg(pates, i+(constant.NB_PATES/2), newCoords2[0], newCoords2[1], newCoords2[2] + constant.HEIGHT_TO_MOVE)
		time.sleep(0.1)

		#on rabaisse la pate
		moveLeg(pates, i, newCoords1[0], newCoords1[1], newCoords1[2])
		moveLeg(pates, i+(constant.NB_PATES/2), newCoords2[0], newCoords2[1], newCoords2[2])
		time.sleep(0.1)

	for i in range(constant.NB_PATES/2):
		moveLeg(pates, i, coords[i][0], coords[i][1], coords[i][2])
		moveLeg(pates, i+ (constant.NB_PATES/2), coords[i+(constant.NB_PATES/2)][0], coords[i+(constant.NB_PATES/2)][1], coords[i+(constant.NB_PATES/2)][2])


def moveLeg(pates, numPate, x, y, z):
	angles = kinematics.computeIK(x, y, z)
	pos = dict(zip(pates[numPate], angles))
	constant.dxl_io.set_goal_position(pos)


def moveTestRotate(maxx, freq):
	moveCenter(constant.coords, constant.pates, maxx*numpy.sin(freq*time.time()*2*numpy.pi), maxx*numpy.cos(freq*time.time()*2*numpy.pi), maxx*numpy.cos(freq*time.time()*2*numpy.pi))
	moveCenter(constant.coords, constant.pates, -maxx*numpy.sin(freq*time.time()*2*numpy.pi), -maxx*numpy.cos(freq*time.time()*2*numpy.pi), -maxx*numpy.cos(freq*time.time()*2*numpy.pi))



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
	time.sleep(0.1)

def moveLigneDroite(coord, numPate, x, y, z):
		newCoords = [coord[0]+x, coord[1]+y, coord[2]+z]
		angles = kinematics.computeIK(newCoords[0], newCoords[1], newCoords[2])
		pos = dict(zip(numPate, angles))
		constant.dxl_io.set_goal_position(pos)

