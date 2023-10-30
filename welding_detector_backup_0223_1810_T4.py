import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np

### Initialize the Ball Video
#cap = cv2.VideoCapture('Files/Videos/vid (1).mp4')
### Initialize the Welding Video
cap_w = cv2.VideoCapture('welding/T4.mp4')

### Create the ColorFinder object
myColorFinder = ColorFinder(False)
### HSV color of Ball
#hsvVals = {'hmin': 9, 'smin': 76, 'vmin': 124, 'hmax': 16, 'smax': 215, 'vmax': 200}
### HSV color of Welding
#hsvVals_w = {'hmin': 25, 'smin': 20, 'vmin': 141, 'hmax': 33, 'smax': 255, 'vmax': 255}
hsvVals_w = {'hmin': 0, 'smin': 9, 'vmin': 199, 'hmax': 179, 'smax': 65, 'vmax': 234}

### Variables
posList_X = []
posList_Y = []
posList_1_X = []
posList_1_Y = []


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
        posList_X.append(contours[0]['center'][0])
        posList_Y.append(contours[0]['center'][1])
        posList_1_X.append(contours[1]['center'][0])
        posList_1_Y.append(contours[1]['center'][1])

    if posList_X:

        ### Polynomial Regression y = Ax^2 + Bx + C
        ### Find the Coefficients
        A, B, C = np.polyfit(posList_X, posList_Y, 2)
        A1, B1, C1 = np.polyfit(posList_1_X, posList_1_Y, 2)

        for i, (pos_x, pos_y) in enumerate(zip(posList_X, posList_Y)):
            pos = (pos_x, pos_y)
            cv2.circle(imgContours, pos, 5, (0, 255, 0), cv2.FILLED)
            if i == 0:
                cv2.line(imgContours, pos, pos, (0, 255, 0), 2)
            else:
                cv2.line(imgContours, pos, (posList_X[i - 1],posList_Y[i - 1]), (0, 255, 0), 2)

        for k, (pos_1_x, pos_1_y) in enumerate(zip(posList_1_X, posList_1_Y)):
            pos_1 = (pos_1_x, pos_1_y)
            cv2.circle(imgContours, pos_1, 5, (0, 255, 0), cv2.FILLED)
            if k == 0:
                cv2.line(imgContours, pos_1, pos_1, (0, 255, 0), 2)
            else:
                cv2.line(imgContours, pos_1, (posList_1_X[k - 1], posList_1_Y[k - 1]), (0, 255, 0), 2)



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