#!/usr/bin/env python3

import rospy
import cv2
import numpy as np


def empty(val):
    pass

def getContours(img, imgcontors):
    contours, heirarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 50:
            cv2.drawContours(imgcontors, cnt, -1, (255, 0, 0), 3)

def startvideo():
    rospy.init_node('videoer', anonymous=True)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    cap.set(3, 640)
    cap.set(4, 480)
    cap.set(10, 50)

    cv2.namedWindow("TrackedBars")
    cv2.resizeWindow("TrackedBars", 640, 240)
    cv2.createTrackbar("Hue min", "TrackedBars", 23, 179, empty)
    cv2.createTrackbar("Hue max", "TrackedBars", 50, 179, empty)
    cv2.createTrackbar("Sat min", "TrackedBars", 29, 255, empty)
    cv2.createTrackbar("Sat max", "TrackedBars", 199, 255, empty)
    cv2.createTrackbar("Val min", "TrackedBars", 21, 255, empty)
    cv2.createTrackbar("Val max", "TrackedBars", 255, 255, empty)

    while not rospy.is_shutdown():
        success, img = cap.read()
        cv2.imshow("Video", img)

        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        cv2.imshow("HSV", img_hsv)

        h_min = cv2.getTrackbarPos("Hue min", "TrackedBars")
        h_max = cv2.getTrackbarPos("Hue max", "TrackedBars")
        s_min = cv2.getTrackbarPos("Sat min", "TrackedBars")
        s_max = cv2.getTrackbarPos("Sat max", "TrackedBars")
        v_min = cv2.getTrackbarPos("Val min", "TrackedBars")
        v_max = cv2.getTrackbarPos("Val max", "TrackedBars")

        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        mask = cv2.inRange(img_hsv, lower, upper)

        cv2.imshow("Mask", mask)

        imgcanny = cv2.Canny(mask, 50, 50)

        cv2.imshow("Canny", imgcanny)

        imgcontors = img.copy()
        getContours(mask, imgcontors)

        cv2.imshow("Contors", imgcontors)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    try:
        startvideo()
    except rospy.ROSInterruptException:
        pass
