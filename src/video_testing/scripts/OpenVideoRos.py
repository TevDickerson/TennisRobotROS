#!/usr/bin/env python3

import rospy
import cv2


def empty(val):
    pass


def startvideo():
    rospy.init_node('videoer', anonymous=True)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    cap.set(3, 640)
    cap.set(4, 480)
    cap.set(10, 50)

    cv2.namedWindow("TrackedBars")
    cv2.resizeWindow("TrackedBars", 640, 240)
    cv2.createTrackbar("Hue min", "TrackedBars", 0, 179, empty)
    cv2.createTrackbar("Hue max", "TrackedBars", 179, 179, empty)
    cv2.createTrackbar("Sat min", "TrackedBars", 0, 255, empty)
    cv2.createTrackbar("Sat max", "TrackedBars", 255, 255, empty)
    cv2.createTrackbar("Val min", "TrackedBars", 0, 255, empty)
    cv2.createTrackbar("Val max", "TrackedBars", 255, 255, empty)

    while not rospy.is_shutdown():
        success, img = cap.read()
        cv2.imshow("Video", img)

        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        cv2.imshow("HSV", img_hsv)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    try:
        startvideo()
    except rospy.ROSInterruptException:
        pass
