#!/usr/bin/env python

import rospy


from geometry_msgs.msg import Twist


def listener():
    rospy.init_node('cmd_vel_listener', anonymous=True)
    rospy.Subscriber("/cmd_vel", Twist)
    while not rospy.is_shutdown():
        print(msg.linear.x)
        print(msg.linear.y)
        print(msg.linear.z)

if __name__ == '__main__':

    try:
        listener()
    except rospy.ROSInterruptException:
        pass
