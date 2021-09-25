#!/usr/bin/env python

import rospy
from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
from geometry_msgs.msg import Twist

kit = ServoKit(channels=16)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)
GPIO.output(27, GPIO.HIGH)

def callback(msg):
    print(msg.linear.x)
    kit.continuous_servo[0].throttle = msg.linear.x * 2
    kit.continuous_servo[1].throttle = msg.linear.x * 2


def listener():
    rospy.init_node('cmd_vel_listener', anonymous=True)
    rospy.Subscriber("/cmd_vel", Twist, callback)
    rospy.spin()


def myhook():
    GPIO.output(18, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)

rospy.on_shutdown(myhook)

if __name__ == '__main__':

    try:
        listener()
    except rospy.ROSInterruptException:
        GPIO.output(4, GPIO.LOW)
        pass
