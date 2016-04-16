import pypot.dynamixel
import time

motor_ids = [11, 12, 13, 21, 22, 23, 31, 32, 33, 41, 42, 43, 51, 52, 53, 61, 62, 63]
coords = [[120, 0, -114], [85, 85, -114], [85, -85, -114], [120, 0, -114], [85, 85, -114], [85, -85, -114]]

dxl_io = pypot.dynamixel.DxlIO('/dev/ttyUSB0', baudrate=1000000)

leg1 = [11, 12, 13]
leg2 = [21, 22, 23]
leg3 = [31, 32, 33]
leg4 = [41, 42, 43]
leg5 = [51, 52, 53]
leg6 = [61, 62, 63]
legs = [leg1, leg2, leg3, leg4, leg5, leg6]
NB_LEGS = 6

WINDOW_W = 600
WINDOW_H = 600

HEIGHT_TO_MOVE = 20
HEIGHT_TO_WRITE_ON = 50
HEIGHT_TO_WRITE_OFF = 20

LENGTH_MOUVEMENT_LEG = 10

LENGTH_ROTATE_LEG = 25

MOUSE_MOUVEMENT_MARGIN = 5

LENGTH_DANCE = 30
FREQ_DANCE = 0.3
# If the spider blocked a little, you can up this value >0.03
TIME_SLEEP_DANCE = 0.03
MID_ANGLE_MOTOR3_DANCE = 120
MID_ANGLE_MOTOR2_DANCE = -45
VAR_ANGLE_MOTOR_DANCE = 30

SCALE_PICTURE = 9

TIME_SLEEP = 0.1

# Coord for Move Gravity Center
MGCcoords = [[120, 0, -114 +HEIGHT_TO_WRITE_OFF], [85, 85, -114 +HEIGHT_TO_WRITE_OFF], [85, -85, -114 +HEIGHT_TO_WRITE_OFF], [120, 0, -114 +HEIGHT_TO_WRITE_OFF], [85, 85, -114 +HEIGHT_TO_WRITE_OFF], [85, -85, -114 +HEIGHT_TO_WRITE_OFF]]

DIAGONAL_LEG_ANGLE = 45
MOTOR_MAX_TORQUE = 50