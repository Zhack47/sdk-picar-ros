import sys
sys.path.append("scripts")
import sdk_picar_ros as car_sdk
from picar_4wd.__init__ import *
from sdk_picar_ros.speed_angle_control import set_speed_angle

set_speed_angle(0.0, 0)
