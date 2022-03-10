import rospy
import picar_4wd as car
import math
import sys
import time
sys.path.append("scripts/")
import sdk_picar_ros as car_sdk
from picar_4wd.__init__ import *
import traceback


def set_speed_angle(speed, theta_):
    """
    Sets the linear speed for the car

    Args:
        speed (float): Speed in meter per second
    """

    theta = math.radians(theta_)
    print(f"Angle in radians {theta}")
    try:
        if speed == 0:
            car.left_front.set_power(int(0))
            car.right_front.set_power(int(0))
            car.left_rear.set_power(int(0))
            car.right_rear.set_power(int(0))
            return 0
        
        ## If the angle passed to the function is equal to 0,
        ## we set the speed to the one passed to the function and exit the function with the exit code 0
        if int(theta_) == 0: 
            computed_power = car_sdk.ms_to_power(speed)
            car.left_front.set_power(int(computed_power))
            car.right_front.set_power(int(computed_power))
            car.left_rear.set_power(int(computed_power))
            car.right_rear.set_power(int(computed_power))
            return 0
        
        ## If the angle passed to the function is different from 0,
        ## we set the speed to the one passed to the function but we have to handle the angle as well
        ## before we exit the function. We use te differential of speed between 
        ## the left and right wheels to get the car to turn.
        elif theta >0 or theta <0 :
            right_speed = 1.0 * speed + (theta * car_sdk.space_between_wheels / 2)
            left_speed = 1.0 * speed - (theta * car_sdk.space_between_wheels / 2)

            # We have to handle some edge cases, due to the non linearity of the power to speed function.
            if -car_sdk.b < left_speed < car_sdk.b:
                if right_speed-car_sdk.b > car_sdk.b + left_speed:
                    modifier = min(right_speed-car_sdk.b, car_sdk.b + left_speed)+0.01
                    right_speed -= modifier 
                    left_speed -= modifier 
                if car_sdk.a * 100 +car_sdk.b - right_speed > car_sdk.b - left_speed:
                    right_speed += min(car_sdk.b+0.01 - left_speed, car_sdk.a * 100 +car_sdk.b-right_speed)
                    left_speed += min(car_sdk.b+0.01 - left_speed, car_sdk.a * 100 +car_sdk.b-right_speed)

            computed_right_power = car_sdk.ms_to_power(right_speed)
            computed_left_power = car_sdk.ms_to_power(left_speed)

            ## We also try to keep the power values in the bounds [1, 100]..
            if computed_right_power > 100 and 1 < computed_left_power:
                power_modifier= min(computed_right_power-100, computed_left_power-1)
                computed_right_power-=power_modifier
                computed_left_power-=power_modifier
                
            ## ..and to avoid having an immobile wheel as much as possible
            if computed_left_power*computed_right_power<0:
                offset_center = computed_left_power + (computed_right_power - computed_left_power)/2
                computed_left_power -= offset_center
                computed_right_power -= offset_center

            print(computed_right_power)
            print(computed_left_power)
            car.left_front.set_power(int(computed_left_power))
            car.right_front.set_power(int(computed_right_power))
            car.left_rear.set_power(int(computed_left_power))
            car.right_rear.set_power(int(computed_right_power))
            
    except Exception as e:
        print("Could not set speed: failed to set power for motors")
        print(e)
        traceback.print_tb(e.__traceback__)
        return -1


print(__name__)
if __name__ == "__main__":
    set_speed_angle(1,10)

    

