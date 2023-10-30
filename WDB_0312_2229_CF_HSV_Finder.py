import cv2
import cvzone
from cvzone.ColorModule import ColorFinder

### Initialize the Ball Video
# cap = cv2.VideoCapture('Files/Videos/vid (1).mp4')
### Initialize the Welding Video
#cap_w = cv2.VideoCapture('welding/welding.avi')

### Create the ColorFinder object
myColorFinder = ColorFinder(True)
### HSV color of Ball
hsvVals = {'hmin': 9, 'smin': 76, 'vmin': 124, 'hmax': 16, 'smax': 215, 'vmax': 200}
### HSV color of Welding
#hsvVals_w = {'hmin': 25, 'smin': 20, 'vmin': 141, 'hmax': 33, 'smax': 255, 'vmax': 255}



while True:
    ### Grab the image
    #success, img = cap_w.read()
    #img = cv2.imread("Files/Ball.png")
    img = cv2.imread("Final_Fire_Test/Welder00538.jpg")

    ### Crop the Basketball image
    #img = img[0:900, :]
    ### Crop the Welding image
    # img = img[0:520, 0:848]

    ### Find the Color Ball
    imgColor, mask = myColorFinder.update(img, hsvVals)
    ### Find the Color Welding
    #imgColor, mask = myColorFinder.update(img, hsvVals_w)



    ### Display
    img = cv2.resize(img, (0, 0), None, 0.7, 0.7)
    cv2.imshow('Image', img)
    cv2.imshow('Image Color', imgColor)
    cv2.waitKey(50)