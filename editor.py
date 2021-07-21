import cv2
import numpy as np
import sys

try:
    path =  sys.argv[1]
except:
    path="assets/images/image.jpg" 
try:    
    height = (int(sys.argv[2]),int(sys.argv[3]))
except:     
    height=(1280,720)

img = cv2.imread(path)

if img is None:
    img = np.zeros([512,512,3],dtype=np.uint8)
    img.fill(255)
    img = cv2.resize(img, (height))


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,color,-1)

def drawRectangleOnImage(image, coordinates, rectColor=(0, 255, 0), rectThickness=2):
    x = coordinates[0]
    y = coordinates[1]
    w = coordinates[2]
    h = coordinates[3]
    return cv2.rectangle(image, (x, y), (x+w, y+h), rectColor, rectThickness)

cv2.namedWindow(winname= "Image Editor")
cv2.setMouseCallback("Image Editor", draw_circle)
color = (0,0,256)
message = 'Press r/g/b to choose color pallette (Default : RED)'
messageCoords = [10, 700]
while True:

    cv2.imshow("Image Editor", img)  
    k = cv2.waitKey(1) & 0xFF
    if k == 82:
        message = 'Color pallette : RED'
        color = (0,0,256)
    elif k == 66:
        message = 'Color pallette : BLUE'
        color = (256,0,0)
    elif k == 71:
        message = 'Color pallette : GREEN'
        color = (0,256,0)

    img = drawRectangleOnImage(
        img, (10,680,1000,30), (0, 0, 0), -1
    )
    img = cv2.putText(
        img, message, (50,700),
        cv2.FONT_HERSHEY_COMPLEX_SMALL,
        1, (255, 255, 255), 1, cv2.LINE_AA
    )

    if k == 81:
        cv2.imwrite("assets/images/tiger.jpg", img)
        break
cv2.destroyAllWindows()