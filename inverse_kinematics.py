#!/usr/bin/python
import math
#import pygame
#from pygame.locals import *

#pygame.init()
#fenetre = pygame.display.set_mode((640,480))
#continuer = 1

#while continuer :

constL1 = 51
constL2 = 63.7
constL3 = 93

theta2c  = -20.69
theta3c  = 90 + theta2c - 5.06

def modulo180(angle):
	if(-180 < angle < 180):
		return angle

	angle = angle%360
	if(angle>180):
		return -360 + angle

	return angle

def alKashi(a, b, c):
	value = (((a*a)+(b*b)-(c*c))/(2*a*b))
	
	return -math.acos(value)

def computeIK(x, y, z, l1=constL1, l2=constL2, l3=constL3):
	theta1 = math.atan2(y, x)

	xp = math.sqrt(x*x+y*y) - l1
	if(xp < 0):
		print("dest too colse")
		xp = 0
	
	d = math.sqrt(math.pow(xp, 2) + math.pow(z, 2))
	if(d > l2+l3):
		print("Dest too far");
		d = l2+l3

	theta2 = alKashi(l2, d, l3) - math.atan2(z, xp)
	theta3 = math.pi - alKashi(l2, l3, d)

	return [modulo180(math.degrees(theta1)), modulo180(math.degrees(theta2) + theta2c), modulo180(math.degrees(theta3) + theta3c)]

