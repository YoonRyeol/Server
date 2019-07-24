import numpy as np
import cv2 as cv

cap1 = cv.VideoCapture(0)
cap2 = cv.VideoCapture(2)
if not cap1.isOpened() | cap2.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1:
        print("Can't receive frame (stream end?). Exiting...")
        break
    
    cv.imshow('frame1', frame1)
    cv.imshow('frame2', frame2)

    if cv.waitKey(1) == ord('q'):
        break

cap1.release()
cap2.release()
cv.destroyAllWindows()
