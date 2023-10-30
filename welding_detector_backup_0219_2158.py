import cv2
import cvzone
from cvzone.ColorModule import ColorFinder

### Initialize the Ball Video
#cap = cv2.VideoCapture('Files/Videos/vid (1).mp4')
### Initialize the Welding Video
cap_w = cv2.VideoCapture('welding/welding.avi')

### Create the ColorFinder object
myColorFinder = ColorFinder(False)
### HSV color of Ball
#hsvVals = {'hmin': 9, 'smin': 76, 'vmin': 124, 'hmax': 16, 'smax': 215, 'vmax': 200}
### HSV color of Welding
hsvVals_w = {'hmin': 25, 'smin': 20, 'vmin': 141, 'hmax': 33, 'smax': 255, 'vmax': 255}

### Variables
posList = []
posList_1 = []

while True:
    ### Grab the image
    #success, img = cap.read()
    success, img = cap_w.read()
    #img = cv2.imread("Files/Ball.png")
    #img = cv2.imread("welding/scene00029.png")

    ### Crop the Basketball image
    #img = img[0:900, :]
    ### Crop the Welding image
    img = img[0:520, 0:848]

    ### Find the Color Ball
    #imgColor, mask = myColorFinder.update(img, hsvVals)
    ### Find the location of the Ball
    #imgContours, contours = cvzone.findContours(img, mask, minArea=200)

    # if contours:
    #     posList.append(contours[0]['center'])
    #
    # for pos in posList:
    #     cv2.circle(imgContours, pos, 5, (0, 255, 0), cv2.FILLED)


    ### Find the Color Welding
    imgColor, mask = myColorFinder.update(img, hsvVals_w)
    ### Find the location of the Welding Sparks
    imgContours, contours = cvzone.findContours(img, mask, minArea=20)

    if contours:
        posList.append(contours[0]['center'])
        posList_1.append(contours[1]['center'])

    for pos in posList:
        cv2.circle(imgContours, pos, 5, (0, 255, 0), cv2.FILLED)
    for pos_1 in posList_1:
        cv2.circle(imgContours, pos_1, 5, (0, 255, 0), cv2.FILLED)



    ### Display
    imgContours = cv2.resize(imgContours, (0, 0), None, 0.7, 0.7)
    ### Display the mask
    #imgColor = cv2.resize(mask, (0, 0), None, 0.7, 0.7)
    #cv2.imshow('Image', img)
    #cv2.imshow('Image Color', imgColor)
    cv2.imshow('Image Contours', imgContours)

    ### waitKey for Ball
    #cv2.waitKey(50)
    ### waitKey for Welding
    cv2.waitKey(2000)