#!/usr/bin/env python
import board
import busio
import adafruit_pca9685
import rospy
from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
from geometry_msgs.msg import Twist

pin1 = 18
pin2 = 22
pin3 = 17
pin4 = 6
pin5 = 6

i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)
# kit = ServoKit(channels=16)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

GPIO.output(pin3, GPIO.LOW)
GPIO.output(pin4, GPIO.LOW)

hat.frequency = 60
RIGHT_WHEEL = hat.channels[0]
LEFT_WHEEL = hat.channels[1]


def callback(msg):
    print(msg.linear.x)
    if msg.linear.x != 0:
        if msg.linear.x >= 0:
            GPIO.output(pin1, GPIO.HIGH)
            GPIO.output(pin2, GPIO.HIGH)
            GPIO.output(pin3, GPIO.LOW)
            GPIO.output(pin4, GPIO.LOW)

        else:
            GPIO.output(pin1, GPIO.LOW)
            GPIO.output(pin2, GPIO.LOW)
            GPIO.output(pin3, GPIO.HIGH)
            GPIO.output(pin4, GPIO.HIGH)

        throttle_val = abs(msg.linear.x)

        RIGHT_WHEEL.duty_cycle = round(throttle_val * 2 * 1000)
        LEFT_WHEEL.duty_cycle = round(throttle_val * 2 * 1000)
    elif msg.angular.z != 0:
        if msg.angular.z >= 0:
            GPIO.output(pin1, GPIO.HIGH)
            GPIO.output(pin2, GPIO.LOW)
            GPIO.output(pin3, GPIO.LOW)
            GPIO.output(pin4, GPIO.HIGH)

        else:
            GPIO.output(pin1, GPIO.LOW)
            GPIO.output(pin2, GPIO.HIGH)
            GPIO.output(pin3, GPIO.HIGH)
            GPIO.output(pin4, GPIO.LOW)
        throttle_val = abs(msg.angular.z)

        RIGHT_WHEEL.duty_cycle = round(throttle_val * 2 * 1000)
        LEFT_WHEEL.duty_cycle = round(throttle_val * 2 * 1000)

    else:
        RIGHT_WHEEL.duty_cycle = 0
        LEFT_WHEEL.duty_cycle = 0



def listener():
    rospy.init_node('cmd_vel_listener', anonymous=True)
    rospy.Subscriber("/cmd_vel", Twist, callback)
    rospy.spin()


def myhook():
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.LOW)
    GPIO.output(pin3, GPIO.LOW)
    GPIO.output(pin4, GPIO.LOW)
    RIGHT_WHEEL.duty_cycle = 0
    LEFT_WHEEL.duty_cycle = 0


rospy.on_shutdown(myhook)


if __name__ == '__main__':

    try:
        listener()
    except rospy.ROSInterruptException:

        pass
