import funcMouv
import constant
from PIL import Image
import time

def draw():
	print "coucou"
	im = Image.open("dessin.png")
	im = im.convert('1')
	pix = im.load()

	right = True
	x = 0
	y = 0

	out  = False

HEIGHT_TO_WRITE_ON = 53
HEIGHT_TO_WRITE_OFF = 50

	for y in range(50):
		for x in range(50):
			if(right):
				print "", x, " et ", y, " = ",pix[x, y]
				if(pix[x, y] == 0):
					funcMouv.moveCenter(constant.coords, constant.legs, 
						-25+(x), -25+(y), 
						constant.HEIGHT_TO_WRITE_ON)
				else:
					funcMouv.moveCenter(constant.coords, constant.legs, 
						-25+(x), -25+(y), 
						constant.HEIGHT_TO_WRITE_OFF)

			else:
				print "", 49-x, " et ", y, " = ",pix[49-x, y]
				if(pix[49-x, y] == 0):
					funcMouv.moveCenter(constant.coords, constant.legs, 
						-25+(49-x), -25+(y), 
						constant.HEIGHT_TO_WRITE_ON)
				else:
					funcMouv.moveCenter(constant.coords, constant.legs, 
						-25+(49-x), -25+(y), 
						constant.HEIGHT_TO_WRITE_OFF)

			time.sleep(0.00005)
		right = not right