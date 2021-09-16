#!/usr/bin/env python3

import rospy
import cv2

#Hi to myself this worked.

def startvideo():
    rospy.init_node('videoer', anonymous=True)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    
    cap.set(3, 640)
    cap.set(4, 480)
    cap.set(10, 50)
    
    #cv2.namedWindow("Video",cv2.WINDOW_NORMAL)

    while not rospy.is_shutdown():
        success, img = cap.read()
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        

if __name__ == '__main__':
    try:
        startvideo()
    except rospy.ROSInterruptException:
        pass
