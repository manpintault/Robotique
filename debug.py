import constant
import time

def checkLeg(tab) :
	constant.dxl_io.set_goal_position({tab[0] : 0})
	time.sleep(1)
	constant.dxl_io.set_goal_position({tab[1] : 0})
	time.sleep(1)
	constant.dxl_io.set_goal_position({tab[2] : 0})
	time.sleep(1)

def changeId(old, new):
	constant.dxl_io.change_id({old: new})
	for i in found_ids:
		if(i == old):
			found_ids[found_ids.index(old)] = new
	print found_ids

def checkId():
	found_id = constant.dxl_io.scan()
	print found_id
