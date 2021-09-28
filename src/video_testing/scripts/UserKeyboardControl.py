#!/usr/bin/env python
import board
import busio
import adafruit_pca9685
import rospy
from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
from geometry_msgs.msg import Twist


i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)
# kit = ServoKit(channels=16)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)
GPIO.output(22, GPIO.HIGH)
GPIO.setup(17, GPIO.HIGH)
GPIO.setup(27, GPIO.LOW)
hat.frequency = 60
RIGHT_WHEEL = hat.channels[0]
LEFT_WHEEL = hat.channels[1]


def callback(msg):
    print(msg.linear.x)
    if msg.linear.x >= 0:
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.setup(17, GPIO.LOW)
        GPIO.setup(27, GPIO.LOW)
    else:
        GPIO.output(18, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        GPIO.setup(17, GPIO.HIGH)
        GPIO.setup(27, GPIO.HIGH)

    throttle_val = abs(msg.linear.x)

    RIGHT_WHEEL.duty_cycle = round(throttle_val * 2 * 1000)
    LEFT_WHEEL.duty_cycle = round(throttle_val * 2 * 1000)


def listener():
    rospy.init_node('cmd_vel_listener', anonymous=True)
    rospy.Subscriber("/cmd_vel", Twist, callback)
    rospy.spin()


def myhook():
    GPIO.output(18, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.setup(17, GPIO.LOW)
    GPIO.setup(27, GPIO.LOW)
    RIGHT_WHEEL.duty_cycle = 0
    LEFT_WHEEL.duty_cycle = 0


rospy.on_shutdown(myhook)


if __name__ == '__main__':

    try:
        listener()
    except rospy.ROSInterruptException:

        pass
