import cv2
import cvzone
from cvzone.ColorModule import ColorFinder

### Initialize the Ball Video
#cap = cv2.VideoCapture('Files/Videos/vid (1).mp4')
### Initialize the Welding Video
#cap_w = cv2.VideoCapture('welding/welding.avi')
#cap_w = cv2.VideoCapture('welding/Welding Sparks 120fps 4K Slo Mo with soothing music_1080p.mp4')
cap_w = cv2.VideoCapture('welding/7346.mp4')

### Create the ColorFinder object
myColorFinder = ColorFinder(False)
### HSV color of Ball
#hsvVals = {'hmin': 9, 'smin': 76, 'vmin': 124, 'hmax': 16, 'smax': 215, 'vmax': 200}
### HSV color of Welding
#hsvVals_w = {'hmin': 25, 'smin': 20, 'vmin': 141, 'hmax': 33, 'smax': 255, 'vmax': 255}
#site data
#hsvVals_w = {'hmin': 9, 'smin': 13, 'vmin': 225, 'hmax': 15, 'smax': 125, 'vmax': 255}
#welding spark hitting the floor
#hsvVals_w = {'hmin': 18, 'smin': 0, 'vmin': 252, 'hmax': 51, 'smax': 52, 'vmax': 255}

###color group red hsv
#hsvVals_w = {'hmin': 0, 'smin': 0, 'vmin': 213, 'hmax': 179, 'smax': 143, 'vmax': 255}
###color group yellow hsv
#hsvVals_w = {'hmin': 25, 'smin': 138, 'vmin': 155, 'hmax': 179, 'smax': 229, 'vmax': 255}
### 20220427
hsvVals_w = {'hmin': 0, 'smin': 0, 'vmin': 159, 'hmax': 179, 'smax': 171, 'vmax': 255}

while True:
    ### Grab the image
    #success, img = cap.read()
    success, img = cap_w.read()
    #img = cv2.imread("Files/Ball.png")
    #img = cv2.imread("welding/scene00029.png")
    # color group HSV
    #img = cv2.imread("welding/Red/J00002.jpg")

    ### Crop the Basketball image
    #img = img[0:900, :]
    ### Crop the Welding image
    #img = img[0:520, 0:848]
    #1
    #img = img[177:448, 1054:1480]
    #2
    #img = img[0:415, 0:837]
    #4
    #img = img[0:447, 0:721]


    ### Find the Color Ball
    #imgColor, mask = myColorFinder.update(img, hsvVals)
    ### Find the Color Welding
    imgColor, mask = myColorFinder.update(img, hsvVals_w)


    ### Display
    #imgColor = cv2.resize(imgColor, (0, 0), None, 0.7, 0.7)
    ### Display the Mask
    imgColor = cv2.resize(mask, (0, 0), None, 0.7, 0.7)
    img = cv2.resize(img, (0, 0), None, 0.7, 0.7)
    cv2.imshow('Image', img)
    cv2.imshow('Image Color', imgColor)
    cv2.waitKey(0)