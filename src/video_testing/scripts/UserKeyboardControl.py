#!/usr/bin/env python

import rospy
from adafruit_servokit import ServoKit

from geometry_msgs.msg import Twist

kit = ServoKit(channels=16)


def callback(msg):
    print(msg.linear.x)
    kit.continuous_servo[0].throttle = msg.linear.x


def listener():
    rospy.init_node('cmd_vel_listener', anonymous=True)
    rospy.Subscriber("/cmd_vel", Twist, callback)
    rospy.spin()


if __name__ == '__main__':

    try:
        listener()
    except rospy.ROSInterruptException:
        pass
