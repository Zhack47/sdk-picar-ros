import rospy
from std_msgs.msg import String
from std_msgs.msg import Header
from geometry_msgs.msg import TwistStamped
import sys
sys.path.append("scripts")
import os
import sdk_picar_ros as car_sdk
from picar_4wd.__init__ import *
from sdk_picar_ros.speed_angle_control import set_speed_angle

speed=0.0
angle=0

def callback(data):
    global speed
    global angle
    rospy.loginfo(f"{rospy.get_caller_id()}\n At {data.header.stamp} I heard {data}")
    speed = float(data.twist.linear.x)
    angle = float(data.twist.angular.z)
    print(f"Speed received : {speed}\nAngle received : {angle}")
    set_speed_angle(speed, angle)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('ros4', anonymous=True)

    rospy.Subscriber('cmd_vel', TwistStamped, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    print(f"Working in the {os.getcwd()} directory")
    listener()
