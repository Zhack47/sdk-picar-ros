#Script keyboard publisher.   Toute voiture abonnée à ce topic recevront les informations du clavier pour avancer, reculer, tourner et s'arrêter


#import 
import rospy
from std_msgs.msg import String
from std_msgs.msg import Header
from geometry_msgs.msg import Twist
from geometry_msgs.msg import TwistStamped
import sys
sys.path.append("scripts")
import sdk_picar_ros as car_sdk
import tty
import termios
import asyncio
from sdk_picar_ros.speed_angle_control import set_speed_angle


power_val = 50
key = 'status'
normalize_speed =100
print("If you want to quit.Please press q")
def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return chr(0x10 + ord(c3) - 65)

def Keyborad_control():

    pub = rospy.Publisher("cmd_vel",TwistStamped, queue_size=10)

    rospy.init_node("Keyboard_publisher")

    vel_msg = TwistStamped()
    vel_msg.header = Header()
    power_temp = 0
    angle_temp = 0
    vel_msg.header.stamp = rospy.Time.now()
    while True:
        global power_val
        key=readkey()
        if key=='6':
            if power_val <=90:
                power_val += 10
                power_temp = power_val
                print("power_val:",power_val)
               
        elif key=='4':
            if power_val >=10:
                power_val -= 10
                power_temp = power_val
                print("power_val:",power_val)

        
        elif key=='w':
            power_temp = power_val 
            vel_msg.twist.angular.z = 0
        elif key=='a':
            # pass
            vel_msg.twist.angular.z = 150
        elif key=='s':
            # pass
            vel_msg.twist.angular.z = 0
            power_temp= -power_val
        elif key=='d':
            # pass
            vel_msg.twist.angular.z = -150
        else:
            power_temp = 0
            print("Arrêt de la voiture")
        if key=='q':
            print("quit")  
            break
        print(f"power:{power_temp}")  
        vel_msg.twist.linear.x = car_sdk.power_to_ms(power_temp)
        print(f"speed:{vel_msg.twist.linear.x}")
        print(f"angle: {vel_msg.twist.angular.z}")
        print("//")
        pub.publish(vel_msg)
        set_speed_angle(vel_msg.twist.linear.x, vel_msg.twist.angular.z)
if __name__ == '__main__':
    Keyborad_control()
