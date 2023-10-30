import cv2
import cvzone
from cvzone.ColorModule import ColorFinder



### Initialize the Welding Video

#cap_w = cv2.VideoCapture('welding/welding.avi')
#cap_w = cv2.VideoCapture('welding/Welding Sparks 120fps 4K Slo Mo with soothing music_1080p.mp4')
#cap_w = cv2.VideoCapture('welding/spark hit the ground demo.mp4')



### Create the ColorFinder object

myColorFinder = ColorFinder(False)



# 20220410 1943 mfAP test data 005

# hsvVals_w = {'hmin': 0, 'smin': 0, 'vmin': 225, 'hmax': 179, 'smax': 220, 'vmax': 255}

# 20221026

hsvVals_w = {'hmin': 0, 'smin': 0, 'vmin': 250, 'hmax': 179, 'smax': 135, 'vmax': 255}


### Average Y plot
# Y = 0



while True:

    ### Grab the image

    #success, img = cap.read()
    #success, img = cap_w.read()

    #img = cv2.imread("Files/Ball.png")

    img = cv2.imread("100_Welding_Videos_Frames_RGB/100.jpg")



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



    ### Find the Color Welding

    imgColor, mask = myColorFinder.update(img, hsvVals_w)

    # Find the contours of welding sparks

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)



    ### drawing contours

    #for cnt in contours:
    # cv2.drawContours(img, contours, -1, (0, 255, 0), 2)



    #loop every contours

    for cnt in contours:

        (x, y, w, h) = cv2.boundingRect(cnt)

        print(x, y, w, h)

        ### Average Y plot
        # Y = y + Y

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    ### Average Y plot
    # print(Y / len(contours))


    ### Display

    #imgColor = cv2.resize(imgColor, (0, 0), None, 0.7, 0.7)
    ### Display the Mask
    #imgColor = cv2.resize(mask, (0, 0), None, 0.7, 0.7)

    img = cv2.resize(img, (0, 0), None, 0.7, 0.7)
    cv2.imshow('Image', img)
    #cv2.imshow('Image Color', imgColor)
    cv2.waitKey(0)