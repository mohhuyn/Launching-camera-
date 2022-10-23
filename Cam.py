import cv2
from time import sleep

cam=cv2.VideoCapture(0)

while True:
    ignore, frame=cam.read()
       
    cv2.imshow('My webCam',frame)
    cv2.moveWindow('My webCam',250,20)

    if cv2.waitKey(1) == ord('q'):

        break
    
cam.release()
