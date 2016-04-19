import constant
import time

def initLimitAngles():
	for i in constant.motor_ids:
		if(i == 11 or i == 41):
			constant.dxl_io.set_angle_limit({i : [-101, 101]})
		if(i == 21 or i == 51):
			constant.dxl_io.set_angle_limit({i : [-35, 101]})
		if(i == 12 or i == 22 or i == 32 or i == 42 or i == 52 or i == 62):
			constant.dxl_io.set_angle_limit({i : [-92 , 101]})
		if(i == 13 or i == 23 or i == 33 or i == 43 or i == 53 or i == 63):
			constant.dxl_io.set_angle_limit({i : [-77 , 150]})
		if(i == 31 or i == 61):
			constant.dxl_io.set_angle_limit({i : [-101 , 33]})

def initRobot() :
	for i in constant.motor_ids :
		if(i in [21, 51]):
			constant.dxl_io.set_goal_position({i : constant.DIAGONAL_LEG_ANGLE})
		elif(i in [31, 61]):
			constant.dxl_io.set_goal_position({i : -constant.DIAGONAL_LEG_ANGLE})
		else:
			constant.dxl_io.set_goal_position({i : 0})
		time.sleep(constant.TIME_SLEEP)

def initMaxTorque():
	for i in constant.motor_ids:
		constant.dxl_io.set_max_torque({i : constant.MOTOR_MAX_TORQUE})

def initTorqueLimit():
	for i in constant.motor_ids:
		constant.dxl_io.set_max_torque({i : constant.MOTOR_TORQUE_LIMIT})