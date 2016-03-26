import itertools
import time
import numpy
import pypot.dynamixel
import numpy
import time
import kinematics
from contextlib import closing
import pypot.robot
found_ids = None
coord = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
pates = None

def changeId(old, new):
	dxl_io.change_id({old: new})
	for i in found_ids:
		if(i == old):
			found_ids[found_ids.index(old)] = new

	print found_ids

def checkLeg(tab) :
	dxl_io.set_goal_position({tab[0] : 0})
	time.sleep(1)
	dxl_io.set_goal_position({tab[1] : 0})
	time.sleep(1)
	dxl_io.set_goal_position({tab[2] : 0})
	time.sleep(2)

def initRobot() :
	for i in found_ids :
		if(i in [21, 51]):
			dxl_io.set_goal_position({i : 45})
		elif(i in [31, 61]):
			dxl_io.set_goal_position({i : -45})
		else:
			dxl_io.set_goal_position({i : 0})
		time.sleep(0.2)

def initRobotIK():
	coords = kinematics.computeDK(0, 0, 0)
	angles = kinematics.computeIK(coords[0], coords[1], coords[2])

	pos = dict(zip(pates[0], angles))
	dxl_io.set_goal_position(pos)

def initPates():
	pate1 = [11, 12, 13]
	pate2 = [21, 22, 23]
	pate3 = [31, 32, 33]
	pate4 = [41, 42, 43]
	pate5 = [51, 52, 53]
	pate6 = [61, 62, 63]
	pates = [pate1, pate2, pate3, pate4, pate5, pate6]
	return pates

def initPos(pates):
	for i in range(6):
		angles = dxl_io.get_present_position(pates[i])
		coord[i] = kinematics.computeDK(angles[0], angles[1], angles[2])
	return coord


#!!!!!! DEBUT DE LA MARCHE !!!!!!!!
def faitUnPasAvant(coords, pates, x, y):
	moveCenter(coords, pates, x, y, 0)
	time.sleep(0.3)
	for i in range(3):
		moveLigneDroite(coords[i], pates[i], 0, 0, 20)
		moveLigneDroite(coords[i+3], pates[i+3], 0, 0, 20)
		time.sleep(0.1)
		moveLeg(pates, i, coords[i][0], coords[i][1], coords[i][2] + 20)
		moveLeg(pates, i+3, coords[i+3][0], coords[i+3][1], coords[i+3][2] + 20)
		time.sleep(0.1)
		moveLeg(pates, i, coords[i][0], coords[i][1], coords[i][2])
		moveLeg(pates, i+3, coords[i+3][0], coords[i+3][1], coords[i+3][2])
		time.sleep(0.1)


#!!!!!! Question 1 du projet !!!!!!!!
def moveLeg(pates, numPate, x, y, z):
	newCoords = [x, y, z]
	angles = kinematics.computeIK(newCoords[0], newCoords[1], newCoords[2])
	pos = dict(zip(pates[numPate], angles))
	dxl_io.set_goal_position(pos)


#!!!!!! FUN ROTATION !!!!!!!!
#test nice with maxx = 10 and freq = 4.5
def moveTestRotate(maxx, freq):
	moveCenter(coord, pates, maxx*numpy.sin(freq*time.time()*2*numpy.pi), maxx*numpy.cos(freq*time.time()*2*numpy.pi), maxx*numpy.cos(freq*time.time()*2*numpy.pi))
	moveCenter(coord, pates, -maxx*numpy.sin(freq*time.time()*2*numpy.pi), -maxx*numpy.cos(freq*time.time()*2*numpy.pi), -maxx*numpy.cos(freq*time.time()*2*numpy.pi))


def moveTestLigneDroite(coords, pates, x):
	for i in range(6):
		if i == 0:
			moveLigneDroite(coords[i], pates[i], x, 0, 0)
		if i in [1,2]:
			moveLigneDroite(coords[i], pates[i], 0, x, 0)
		if i == 3:
			moveLigneDroite(coords[i], pates[i], -x, 0, 0)
		if i in [4,5]:
			moveLigneDroite(coords[i], pates[i], 0, -x, 0)
	time.sleep(0.5)

def moveTestLigneCote(coords, pates, y):
	for i in range(6):
		if i == 0:
			moveLigneDroite(coords[i], pates[i], 0, -y, 0)
		if i in [1,2]:
			moveLigneDroite(coords[i], pates[i], y, 0, 0)
		if i == 3:
			moveLigneDroite(coords[i], pates[i], 0, y, 0)
		if i in [4,5]:
			moveLigneDroite(coords[i], pates[i], -y, 0, 0)
	time.sleep(0.5)


#!!!!!! Question 2 du projet !!!!!!!!
def moveCenter(coords, pates, x, y, z):
	for i in range(6):
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
		#angles = dxl_io.get_present_position(numPate)
		#coords = kinematics.computeDK(angles[0], angles[1], angles[2])
		newCoords = [coord[0]+x, coord[1]+y, coord[2]+z]
		angles = kinematics.computeIK(newCoords[0], newCoords[1], newCoords[2])
		pos = dict(zip(numPate, angles))
		dxl_io.set_goal_position(pos)

if __name__ == '__main__':

	# with closing(pypot.robot.from_json('robotConfig.json')) as robot:
	with pypot.dynamixel.DxlIO('/dev/ttyUSB0', baudrate=1000000) as dxl_io:

		found_ids = [11, 12, 13, 21, 22, 23, 31, 32, 33, 41, 42, 43, 51, 52, 53, 61, 62, 63]
#		found_ids = dxl_io.scan()
#		print found_ids

		dxl_io.enable_torque(found_ids)
		initRobot()

		pates = initPates()
		coord = initPos(pates)


		print "ready"
		time.sleep(0.5)
		while 1:

			faitUnPasAvant(coord, pates, 0, 30)
			faitUnPasAvant(coord, pates, 30, 0)
			faitUnPasAvant(coord, pates, 0, -30)
			faitUnPasAvant(coord, pates, -30, 0)

#			moveCenter(coord, pates, 10, 10, -10)

#			moveLeg(pates, 0, 100, 20, -140)

#			maxx = 10
#			freq = 4.5
#			moveTestRotate(maxx, freq)



#			moveTestLigneCote(coord, pates, 20)
#			moveTestLigneCote(coord, pates, -20)

#			time.sleep(0.1)

#			moveTestLigneDroite(coord, pates, 20)
#			moveTestLigneDroite(coord, pates, -20)



#		while 1:
#				angles = dxl_io.get_present_position(j)
#				coords = kinematics.computeDK(angles[0], angles[1], angles[2])
#				newCoords = [coords[0]+30, coords[1], coords[2]]
#				angles = kinematics.computeIK(newCoords[0], newCoords[1], newCoords[2])
#				pos = dict(zip(j, angles))
#				dxl_io.set_goal_position(pos)
#				time.sleep(3)

		# while 1:
		# 	for i in pates:
		# 		angles = dxl_io.get_present_position(i)
		# 		coords = kinematics.computeDK(angles[0], angles[1], angles[2])
		# 		newCoords = [coords[0], coords[1], coords[2]+1]
		# 		angles = kinematics.computeIK(newCoords[0], newCoords[1], newCoords[2])
		# 		pos = dict(zip(i, angles))
		# 		dxl_io.set_goal_position(pos)
		# 	time.sleep(1)



		print 'Current pos:', dxl_io.get_present_position(found_ids)

		time.sleep(1)  # we wait for 1s



		dxl_io.disable_torque(found_ids)
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
	 #       dxl_io.set_goal_position(pos)
	        #time.sleep(0.01)  # we wait for 1s

