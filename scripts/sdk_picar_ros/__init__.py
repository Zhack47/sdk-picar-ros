#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from picar_4wd.pwm import PWM
from picar_4wd.pin import Pin
from picar_4wd.motor import Motor
from picar_4wd.speed import Speed
from picar_4wd.filedb import FileDB
from picar_4wd.utils import *
import time
import math


# Init constants
wheel_radius = 0.033  # Meters
# angular_speed_per_percent_of_power  = 1  # In degrees per second, TBD by Khalil
a = 0.00387
b = 0.2944

def power_to_ms(power):
    #global angular_speed_per_percent_of_power
    global wheel_radius
    global a
    global b
    # multiplicator = angular_speed_per_percent_of_power
    # wheel_radius = wheel_radius
    if power >= 0:
        speed = a * power + b # power * (multiplicator * 2 * math.pi * wheel_radius)
    else:
        speed = a * power - b
    print(f"Speed : {speed}")
    return speed


def ms_to_power(speed):
    global wheel_radius
    #global angular_speed_per_percent_of_power
    global a
    global b
    #multiplicator = angular_speed_per_percent_of_power
    #wheel_radius = wheel_radius
    #power = speed / (multiplicator * 2 * math.pi * wheel_radius)
    print(f"Speed : {speed}")
    if -b < speed and b > speed:
        power = 0
    else:
        if speed >=b:
            power = math.ceil((speed - b) / a)
        elif speed <= -b:
            power = math.ceil((speed + b) / a)
    print(f"Power : {power}")
    return power


# Config File:
config = FileDB("~/.picar-4wd-config")
left_front_reverse = config.get('left_front_reverse', default_value = False)
right_front_reverse = config.get('right_front_reverse', default_value = False)
left_rear_reverse = config.get('left_rear_reverse', default_value = False)
right_rear_reverse = config.get('right_rear_reverse', default_value = False)    


# Init motors

left_front_motor = Motor(PWM("P13"), Pin("D4"), is_reversed=left_front_reverse) # motor 1
right_front_motor = Motor(PWM("P12"), Pin("D5"), is_reversed=right_front_reverse) # motor 2
left_rear_motor = Motor(PWM("P8"), Pin("D11"), is_reversed=left_rear_reverse) # motor 3
right_rear_motor = Motor(PWM("P9"), Pin("D15"), is_reversed=right_rear_reverse) # motor 4 


left_rear_speed = Speed(25)
right_rear_speed = Speed(4)

space_between_wheels=0.14  # Meters TBD by Khalil
#max_speed = power_to_ms(100)
