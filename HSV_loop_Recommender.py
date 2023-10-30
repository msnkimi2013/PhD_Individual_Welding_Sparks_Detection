import cv2
import cvzone
from cvzone.ColorModule import ColorFinder

### Create the ColorFinder object
myColorFinder = ColorFinder(False)
### initial the welding image
img = cv2.imread("100_Welding_Videos_Frames_RGB/100.jpg")

### Variables

# fixed
hmin = 0
hmax = 179
smin = 0
vmax = 255

# changable
smax = 0
vmin = 0

# looper
s2 = 0
v1 = 0

# counter
cnt = 0

# hsv list
list = []
# hsv dictionary
hsvVals = {}

for s2 in range(51):
    for v1 in range(51):
        smax = s2 * 5
        vmin = v1 * 5

        # print(s2)
        # print(v1)
        cnt = cnt + 1
        print(cnt)

        #hsv list append
        list.append(hmin)
        list.append(hmax)
        list.append(smin)
        list.append(smax)
        list.append(vmin)
        list.append(vmax)
        #print(list)


        ### hsv dictionary append
        hsvVals.update({'hmin':list[0]})
        hsvVals.update({'smin':list[2]})
        hsvVals.update({'vmin':list[4]})
        hsvVals.update({'hmax':list[1]})
        hsvVals.update({'smax':list[3]})
        hsvVals.update({'vmax':list[5]})
        print(hsvVals)

        ### color mask
        imgColor, mask = myColorFinder.update(img, hsvVals)

        ### color mask save to image
        #cv2.imwrite("/home/jinxi/PycharmProjects/opencv_basketball_spark/welding/hsv_loop_output/{0}.jpg".format(cnt), mask)
        cv2.imwrite("100_Welding_Videos_Frames_RGB/100/{0}.jpg".format(cnt), mask)

        ### Display
        # mask = cv2.resize(mask, (0, 0), None, 0.7, 0.7)
        # img = cv2.resize(img, (0, 0), None, 0.7, 0.7)
        cv2.imshow('Image Color Mask', mask)
        cv2.imshow('Image', img)
        cv2.waitKey(3)

        ### list and dictionary re-initialize
        list = []
        hsvVals = {}
