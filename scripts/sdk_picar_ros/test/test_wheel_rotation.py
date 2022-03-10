## Calibration script for the PiCar.
## Using this scrit and a linear regression, you should be able
## to find the variables a and d, defining the relation between
## real world speed and the power arbitrary unit


import rospy
from std_msgs.msg import Float32
from picar_4wd.motor import Motor
from picar_4wd.pwm import PWM
from picar_4wd.pin import Pin
import time

left_front = Motor(PWM("P13"), Pin("D4")) # motor 1
right_front = Motor(PWM("P12"), Pin("D5")) # motor 2
left_rear = Motor(PWM("P8"), Pin("D11")) # motor 3
right_rear = Motor(PWM("P9"), Pin("D15")) # motor 4

for i in range(0, 101, 10):
    left_front.set_power(i)
    right_front.set_power(i)
    left_rear.set_power(i)
    right_rear.set_power(i)
    time.sleep(6)
    left_front.set_power(0)
    right_front.set_power(0)
    left_rear.set_power(0)
    right_rear.set_power(0)
    time.sleep(20)
