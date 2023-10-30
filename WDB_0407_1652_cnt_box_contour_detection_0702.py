import cv2
import cvzone
from cvzone.ColorModule import ColorFinder

### Initialize the Ball Video
#cap = cv2.VideoCapture('Files/Videos/vid (1).mp4')
### Initialize the Welding Video
#cap_w = cv2.VideoCapture('welding/welding.avi')
#cap_w = cv2.VideoCapture('welding/Welding Sparks 120fps 4K Slo Mo with soothing music_1080p.mp4')
#cap_w = cv2.VideoCapture('welding/spark hit the ground demo.mp4')

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
# 20220408
# hsvVals_w = {'hmin': 0, 'smin': 37, 'vmin': 209, 'hmax': 70, 'smax': 140, 'vmax': 255}
# 20220410 mfAP_test_data_145_very bad hsvVals
# hsvVals_w = {'hmin': 0, 'smin': 0, 'vmin': 143, 'hmax': 179, 'smax': 239, 'vmax': 255}
# 20220410 1943 mfAP test data 005
hsvVals_w = {'hmin': 0, 'smin': 0, 'vmin': 225, 'hmax': 179, 'smax': 137, 'vmax': 255}

# Y = 0

while True:
    ### Grab the image
    #success, img = cap.read()
    #success, img = cap_w.read()
    #img = cv2.imread("Files/Ball.png")
    #img = cv2.imread("welding/scene00029.png")
    ### mfAP test data
    img = cv2.imread("welding/mfAP_test_data/welding00005.jpg")

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
    # Find the contours of welding sparks
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    ### drawing contours
    #for cnt in contours:
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

    #loop every contours
    # for cnt in contours:
    #     (x, y, w, h) = cv2.boundingRect(cnt)
    #     #print(x, y, w, h)
    #     Y = y + Y
    #
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # print(Y / len(contours))


    ### Display
    #imgColor = cv2.resize(imgColor, (0, 0), None, 0.7, 0.7)
    ### Display the Mask
    #imgColor = cv2.resize(mask, (0, 0), None, 0.7, 0.7)
    img = cv2.resize(img, (0, 0), None, 0.7, 0.7)
    cv2.imshow('Image', img)
    #cv2.imshow('Image Color', imgColor)
    cv2.waitKey(0)