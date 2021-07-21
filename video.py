import numpy as np
import cv2 as cv
import argparse
import sys

try:
    path =  sys.argv[1]
except:
    path="assets/videos/video.mp4" 
try:    
    height = (int(sys.argv[2]),int(sys.argv[3]))
except:     
    height=(1280,720)

cap = cv.VideoCapture(path)
cap_webcam = cv.VideoCapture(0)
frame_counter = 0
r = 0
def drawRectangleOnImage(image, coordinates, rectColor=(0, 255, 0), rectThickness=2):
    x = coordinates[0]
    y = coordinates[1]
    w = coordinates[2]
    h = coordinates[3]
    return cv.rectangle(image, (x, y), (x+w, y+h), rectColor, rectThickness)


while True:
    k = cv.waitKey(1) & 0xFF
    ret, frame = cap.read()
    ret_webcam, frame_webcam = cap_webcam.read()

    frame = cv.resize(frame, (height))
    frame_webcam = cv.resize(frame_webcam, (300,200))

    frame_counter += 1
    if frame_counter == cap.get(cv.CAP_PROP_FRAME_COUNT):
        frame_counter = 0 
        cap.set(cv.CAP_PROP_POS_FRAMES, 0)

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    if k==49:      
        r = 1

    if k==50 or r==2:
        frame_webcam = cv.cvtColor(frame_webcam, cv.COLOR_BGR2GRAY)
        frame_webcam = np.stack((frame_webcam,) * 3, axis=-1)
        r = 2

    if k==51 or r==3:
        id_kernel = np.ones((5, 5), np.float32) / 25.0
        frame_webcam = cv.filter2D(frame_webcam, -1, id_kernel)
        r = 3

    frame[:200,:300] = frame_webcam   
    frame = drawRectangleOnImage(
        frame, (0,0,300,200), (0, 0, 256), 3
    )

    cv.imshow('frame', frame)
    if k == 81:
        break
cap.release()
cv.destroyAllWindows()
