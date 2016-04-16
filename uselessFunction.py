import constant

def initRobotIK():
	coords = kinematics.computeDK(0, 0, 0)
	angles = kinematics.computeIK(coords[0], coords[1], coords[2])

	pos = dict(zip(constant.legs[0], angles))
	constant.dxl_io.set_goal_position(pos)

def initPos(legs):
	for i in range(constant.NB_LEGS):
		angles = constant.dxl_io.get_present_position(legs[i])
		coord[i] = kinematics.computeDK(angles[0], angles[1], angles[2])
	return coord
