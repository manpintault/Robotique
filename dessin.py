import funcMouv
import constant
from PIL import Image
import time

def draw():
	# init and load image
	im = Image.open("dessin.png")
	# convert on white (255) or black (0)
	im = im.convert('1')
	pix = im.load()

	right = True
	# For x and y of image :
	for y in range(constant.SIZE_IMAGE):
		for x in range(constant.SIZE_IMAGE):
			if(right):
				# Draw left to right
				if(pix[x, y] == 0):
					RightDoMoveOnX(x, y, constant.HEIGHT_TO_WRITE_ON)
				else:
					RightDoMoveOnX(x, y, constant.HEIGHT_TO_WRITE_OFF)
			else:
				# Draw right to left
				if(pix[(constant.SIZE_IMAGE -1)-x, y] == 0):
					LeftDoMoveOnX(x, y, constant.HEIGHT_TO_WRITE_ON)
				else:
					LeftDoMoveOnX(x, y, constant.HEIGHT_TO_WRITE_OFF)
			time.sleep(constant.TIME_SLEEP_DRAWING)
		right = not right

def RightDoMoveOnX(x, y, z):
	funcMouv.moveCenter(constant.coords, constant.legs, 
		-(constant.SIZE_IMAGE/2)+x, -(constant.SIZE_IMAGE/2)+y, z)

def LeftDoMoveOnX(x, y, z):
	funcMouv.moveCenter(constant.coords, constant.legs, 
		-(constant.SIZE_IMAGE/2)+((constant.SIZE_IMAGE -1)-x), 
		-(constant.SIZE_IMAGE/2)+(y), z)