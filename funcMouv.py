import constant
import time
import numpy
import kinematics
import itertools
import math

def doABetterStepForward(coords, legs, x, y, freq_speed_robot):

	# Calculation of sinusoid function for all motor
	sinusoide = numpy.sin(freq_speed_robot*time.time()*2*numpy.pi)
	cosinoide = numpy.cos(freq_speed_robot*time.time()*2*numpy.pi)

	# Added some variables for differents functionings of some motors
	moveBodySinX = -x*sinusoide
	moveBodySinY = -y*sinusoide
	moveBodyCosZ = constant.HEIGHT_TO_MOVE*cosinoide

	moveCenter1(constant.MGCcoords, constant.legs, moveBodySinX, moveBodySinY, moveBodyCosZ)
	moveCenter2(constant.MGCcoords, constant.legs, -moveBodySinX, -moveBodySinY, -moveBodyCosZ)
	time.sleep(constant.TIME_SLEEP_DANCE)	


def moveCenter1(coords, legs, x, y, z):
	for i in range(constant.NB_LEGS):
		if i == 1 :
			moveStraightOn(coords[i], legs[i], y, x, z)
		if i == 3:
			moveStraightOn(coords[i], legs[i], -x, y, z)
		if i == 5:
			moveStraightOn(coords[i], legs[i], -y, -x, z)

def moveCenter2(coords, legs, x, y, z):
	for i in range(constant.NB_LEGS):
		if i == 0:
			moveStraightOn(coords[i], legs[i], x, -y, z)
		if i == 2:
			moveStraightOn(coords[i], legs[i], y, x, z)
		if i == 4 :
			moveStraightOn(coords[i], legs[i], -y, -x, z)

def goUpOneLeg(legs, i):
	newAngles = constant.dxl_io.get_present_position(legs[i])
	newCoords = kinematics.computeDK(newAngles[0], newAngles[1], newAngles[2])
	moveStraightOn(newCoords, legs[i], 0, 0, constant.HEIGHT_TO_MOVE)

def doAStepForward(coords, legs, x, y):
	# First step : only move the body
	moveCenter(coords, legs, x, y, 0)
	time.sleep(constant.TIME_SLEEP)
	# Second step : move all legs
	# So for each opposites legs
	for i in range(constant.NB_LEGS/2):
		# Go up the leg
		goUpOneLeg(legs, i)
		goUpOneLeg(legs, i+(constant.NB_LEGS/2))
		time.sleep(constant.TIME_SLEEP)

		# Go move the leg to his initial position
		moveLeg(legs, i, coords[i][0], coords[i][1], coords[i][2] + constant.HEIGHT_TO_MOVE)
		moveLeg(legs, i+(constant.NB_LEGS/2), coords[i+(constant.NB_LEGS/2)][0], coords[i+(constant.NB_LEGS/2)][1], coords[i+(constant.NB_LEGS/2)][2] + constant.HEIGHT_TO_MOVE)
		time.sleep(constant.TIME_SLEEP)

		# Go down the leg
		moveLeg(legs, i, coords[i][0], coords[i][1], coords[i][2])
		moveLeg(legs, i+(constant.NB_LEGS/2), coords[i+(constant.NB_LEGS/2)][0], coords[i+(constant.NB_LEGS/2)][1], coords[i+(constant.NB_LEGS/2)][2])
		time.sleep(constant.TIME_SLEEP)

def getCoordsToRotateOneLeg(coords, x, i):
	angles = kinematics.computeIK(coords[i][0], coords[i][1], coords[i][2])
	angles[0] = angles[0] + x
	return kinematics.computeDK(angles[0], angles[1], angles[2])

# Turn around with "x" degrees
def turnAround(coords, legs, x):
	# For each legs
	for i in range(constant.NB_LEGS/2):
		# Go up the leg
		moveLeg(legs, i, coords[i][0], coords[i][1], coords[i][2] + constant.HEIGHT_TO_MOVE)
		moveLeg(legs, i+(constant.NB_LEGS/2), coords[i+(constant.NB_LEGS/2)][0], coords[i+(constant.NB_LEGS/2)][1], coords[i+(constant.NB_LEGS/2)][2] + constant.HEIGHT_TO_MOVE)
		time.sleep(constant.TIME_SLEEP)

		# Do rotation of leg
		newCoords1 = getCoordsToRotateOneLeg(coords, x, i)
		newCoords2 = getCoordsToRotateOneLeg(coords, x, i+(constant.NB_LEGS/2))

		moveLeg(legs, i, newCoords1[0], newCoords1[1], newCoords1[2] + constant.HEIGHT_TO_MOVE)
		moveLeg(legs, i+(constant.NB_LEGS/2), newCoords2[0], newCoords2[1], newCoords2[2] + constant.HEIGHT_TO_MOVE)
		time.sleep(constant.TIME_SLEEP)

		# Go down the leg
		moveLeg(legs, i, newCoords1[0], newCoords1[1], newCoords1[2])
		moveLeg(legs, i+(constant.NB_LEGS/2), newCoords2[0], newCoords2[1], newCoords2[2])
		time.sleep(constant.TIME_SLEEP)

	for i in range(constant.NB_LEGS/2):
		moveLeg(legs, i, coords[i][0], coords[i][1], coords[i][2])
		moveLeg(legs, i+ (constant.NB_LEGS/2), coords[i+(constant.NB_LEGS/2)][0], coords[i+(constant.NB_LEGS/2)][1], coords[i+(constant.NB_LEGS/2)][2])

def moveLeg(legs, numleg, x, y, z):
	angles = kinematics.computeIK(x, y, z)
	pos = dict(zip(legs[numleg], angles))
	constant.dxl_io.set_goal_position(pos)


def goToDance(maxx, freq):
	# Calculation of sinusoid function for all motor
	sinusoide = numpy.sin(freq*time.time()*2*numpy.pi)
	cosinoide = numpy.cos(freq*time.time()*2*numpy.pi)
	# Added some variables for differents functionings of some motors
	moveBodySin = -maxx*sinusoide
	moveBodyCos = -maxx*cosinoide
	moveLegCos = constant.VAR_ANGLE_MOTOR_DANCE*cosinoide
	moveLegSin = constant.VAR_ANGLE_MOTOR_DANCE*sinusoide
	# Do the mouvement
	moveCenterToDance(constant.MGCcoords, constant.legs, moveBodySin, moveBodyCos, moveBodyCos)
	moveAngleLeg(constant.legs, moveLegCos, moveLegSin)
	time.sleep(constant.TIME_SLEEP_DANCE)

def moveAngleLeg(legs, cosLeg1, sinLeg4):
	for i in range(constant.NB_LEGS):
		if i == 0:
			angles = [0, constant.MID_ANGLE_MOTOR2_DANCE - cosLeg1, constant.MID_ANGLE_MOTOR3_DANCE + cosLeg1]
			pos = dict(zip(legs[i], angles))
			constant.dxl_io.set_goal_position(pos)
		if i == 3:
			angles = [0, constant.MID_ANGLE_MOTOR2_DANCE - sinLeg4, constant.MID_ANGLE_MOTOR3_DANCE + sinLeg4]
			pos = dict(zip(legs[i], angles))
			constant.dxl_io.set_goal_position(pos)
	
def moveCenterToDance(coords, legs, x, y, z):
	for i in range(constant.NB_LEGS):
		if i == 1 or i == 2 :
			moveStraightOn(coords[i], legs[i], y, x, z)
		if i == 4 or i == 5:
			moveStraightOn(coords[i], legs[i], -y, -x, z)

def moveCenter(coords, legs, x, y, z):
	for i in range(constant.NB_LEGS):
		if i == 0:
			moveStraightOn(coords[i], legs[i], x, -y, z)
		if i == 1 or i == 2:
			moveStraightOn(coords[i], legs[i], y, x, z)
		if i == 3:
			moveStraightOn(coords[i], legs[i], -x, y, z)
		if i == 4 or i == 5:
			moveStraightOn(coords[i], legs[i], -y, -x, z)
	time.sleep(constant.TIME_SLEEP_DANCE)

def moveStraightOn(coords, numleg, x, y, z):
		angles = kinematics.computeIK(coords[0]+x, coords[1]+y, coords[2]+z)
		pos = dict(zip(numleg, angles))
		constant.dxl_io.set_goal_position(pos)

def moveOnZ(coords, numleg, z):
		angles = kinematics.computeIK(coords[0], coords[1], coords[2]-z)
		pos = dict(zip(numleg, angles))
		constant.dxl_io.set_goal_position(pos)

def moveGravityCenter(coords, legs, x, y):
	varX = x*math.cos(constant.DIAGONAL_LEG_ANGLE)
	for i in range(constant.NB_LEGS):
		if i == 0:
			moveOnZ(coords[i], legs[i], x)
		if i == 1:
			moveOnZ(coords[i], legs[i], y + varX)
		if i == 2:
			moveOnZ(coords[i], legs[i], y - varX)
		if i == 3:
			moveOnZ(coords[i], legs[i], -x)
		if i == 4:
			moveOnZ(coords[i], legs[i], -y - varX)
		if i == 5:
			moveOnZ(coords[i], legs[i], -y + varX)
#	time.sleep(constant.TIME_SLEEP_FOR_GRAVITY_CENTER)

def standUp():
	for i in range(constant.NB_LEGS):
		moveLeg(constant.legs, i, constant.coords[i][0], constant.coords[i][1], constant.coords[i][2])