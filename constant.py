import pypot.dynamixel
import time

motor_ids = [11, 12, 13, 21, 22, 23, 31, 32, 33, 41, 42, 43, 51, 52, 53, 61, 62, 63]
coords = [[120, 0, -114], [85, 85, -114], [85, -85, -114], [120, 0, -114], [85, 85, -114], [85, -85, -114]]

dxl_io = pypot.dynamixel.DxlIO('/dev/ttyUSB0', baudrate=1000000)

pate1 = [11, 12, 13]
pate2 = [21, 22, 23]
pate3 = [31, 32, 33]
pate4 = [41, 42, 43]
pate5 = [51, 52, 53]
pate6 = [61, 62, 63]
pates = [pate1, pate2, pate3, pate4, pate5, pate6]

NB_PATES = 6

WINDOW_W = 600
WINDOW_H = 600

HEIGHT_TO_MOVE = 20
HEIGHT_TO_WRITE_ON = 50
HEIGHT_TO_WRITE_OFF = 20

LENGTH_MOUVEMENT_LEG = 10

MOUSE_MOUVEMENT_MARGIN = 5

LENGTH_DANCE = 30
FREQ_DANCE = 0.3
# If the spider blocked a little, you can up this value >0.03
TIME_SLEEP_DANCE = 0.03

SCALE_PICTURE = 9

TIME_SLEEP = 0.1

#Coord for Move Gravity Center
MGCcoords = [[120, 0, -114 +HEIGHT_TO_WRITE_OFF], [85, 85, -114 +HEIGHT_TO_WRITE_OFF], [85, -85, -114 +HEIGHT_TO_WRITE_OFF], [120, 0, -114 +HEIGHT_TO_WRITE_OFF], [85, 85, -114 +HEIGHT_TO_WRITE_OFF], [85, -85, -114 +HEIGHT_TO_WRITE_OFF]]

DIAGONAL_LEG_ANGLE = 45