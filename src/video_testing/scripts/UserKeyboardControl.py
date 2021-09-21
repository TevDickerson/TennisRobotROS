#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist


def callback(msg):
    print(msg)


def listener():
    rospy.init_node('cmd_vel_listener', anonymous=True)
    rospy.Subscriber("/cmd_vel", Twist, callback)
    rospy.spin()


if __name__ == '__main__':

    try:
        listener()
    except rospy.ROSInterruptException:
        pass
