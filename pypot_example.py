import itertools
import time
import numpy
import pypot.dynamixel
import numpy
import time
import inverse_kinematics
import direct_kinematics
from contextlib import closing
import pypot.robot
found_ids = None

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
	coords = direct_kinematics.computeDK(0, 0, 0)
	angles = inverse_kinematics.computeIK(coords[0], coords[1], coords[2])

	pos = dict(zip(pates[0], angles))
	dxl_io.set_goal_position(pos)


if __name__ == '__main__':

	# with closing(pypot.robot.from_json('robotConfig.json')) as robot:
	with pypot.dynamixel.DxlIO('/dev/ttyUSB0', baudrate=1000000) as dxl_io:

		found_ids = [11, 12, 13, 21, 22, 23, 31, 32, 33, 41, 42, 43, 51, 52, 53, 61, 62, 63]
		pate1 = [11, 12, 13]
		pate2 = [21, 22, 23]
		pate3 = [31, 32, 33]
		pate4 = [41, 42, 43]
		pate5 = [51, 52, 53]
		pate6 = [61, 62, 63]

		pates = [pate1, pate2, pate3, pate4, pate5, pate6]

		dxl_io.enable_torque(found_ids)
		initRobot()
		i = pates[0]
		while 1:
			angles = dxl_io.get_present_position(i)
			#print angles
			coords = direct_kinematics.computeDK(angles[0], angles[1], angles[2])
			print coords
			newCoords = [coords[0], coords[1], coords[2]+1]
			print newCoords
			angles = inverse_kinematics.computeIK(newCoords[0], newCoords[1], newCoords[2])
			pos = dict(zip(i, angles))
			dxl_io.set_goal_position(pos)
			time.sleep(1)

		# while 1:
		# 	for i in pates:
		# 		angles = dxl_io.get_present_position(i)
		# 		coords = direct_kinematics.computeDK(angles[0], angles[1], angles[2])
		# 		newCoords = [coords[0], coords[1], coords[2]+1]
		# 		angles = inverse_kinematics.computeIK(newCoords[0], newCoords[1], newCoords[2])
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

