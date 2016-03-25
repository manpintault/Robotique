#!/usr/bin/python
import math

constL1 = 51
constL2 = 63.7
constL3 = 93

alpha = (20.60*math.pi)/180
beta= (5.06*math.pi)/180

def computeDK(theta1, theta2, theta3, l1=constL1, l2=constL2, l3=constL3):
    "returns the end effector's position [x, y, z] according to the parameters"
    #no offset for theta1 because the joint is aligned with the origin
    theta2C = -alpha
    theta3C =(math.pi/2)+theta2C - beta
    theta2 = theta2 - theta2C
    theta3 = -(theta3-theta3C)
    x=(l1 + l2*math.cos(theta2) + l3*math.cos(theta2+theta3))*math.cos(theta1)
    y=(l1 + l2*math.cos(theta2) + l3*math.cos(theta2+theta3))*math.sin(theta1)
    z=-(l2*math.sin(theta2)+l3*math.sin(theta2 + theta3))
    return [round(x, 2), round(y, 2), round(z, 2)]

