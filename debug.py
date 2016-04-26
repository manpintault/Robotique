import constant
import time
#function for check the position of the leg
def checkLeg(tab):
	constant.dxl_io.set_goal_position({tab[0] : 0})
	time.sleep(1)
	constant.dxl_io.set_goal_position({tab[1] : 0})
	time.sleep(1)
	constant.dxl_io.set_goal_position({tab[2] : 0})
	time.sleep(1)
#function for change an id by another
def changeId(old, new):
	constant.dxl_io.change_id({old: new})
	for i in found_ids:
		if(i == old):
			found_ids[found_ids.index(old)] = new
	print found_ids
#function t check ids of the robot
def checkId():
	found_id = constant.dxl_io.scan()
	print found_id

def checkMaxTorque():
	print constant.dxl_io.get_max_torque(constant.motor_ids)

def checkTorqueLimit():
	print constant.dxl_io.get_torque_limit(constant.motor_ids)
