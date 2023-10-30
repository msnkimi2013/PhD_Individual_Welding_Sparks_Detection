import cv2
import cvzone
from cvzone.ColorModule import ColorFinder



### Initialize the Welding Video
cap_w = cv2.VideoCapture('100_Welding_Video_Clip_Grouped_for_비산불티/23/104.mp4')

### Create the ColorFinder object
myColorFinder = ColorFinder(False)



# 20221110
hsvVals_w = {'hmin': 0, 'smin': 0, 'vmin': 250, 'hmax': 179, 'smax': 250, 'vmax': 255}



### welding zone filter
Img_width = 1920
Img_height = 1088

# welding zone filter relative coordinates
center_x = 0.5
center_y = 0.5
width = 1
height = 1

# welding zone filter left_x top_y w h coordinates
WZF_x = center_x * Img_width - width * Img_width * 0.5
WZF_y = center_y * Img_height - height * Img_height * 0.5
WZF_w = width * Img_width
WZF_h = height * Img_height


### loop counter
i = 0

list_bbox_num = []


while True:
    ### Grab the image
    #success, img = cap.read()
    success, img = cap_w.read()



    #img = cv2.imread("Files/Ball.png")
    #img = cv2.imread("welding/scene00029.png")



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



    #loop every contours
    for cnt in contours:


        area = cv2.contourArea(cnt)

        if 1 < area:

            (x, y, w, h) = cv2.boundingRect(cnt)


            ### Welding Zone Filter Start
            if x > WZF_x :
                if (x + w) < (WZF_x + WZF_w) :
                    if y > WZF_y :
                        if (y + h) < (WZF_y + WZF_h):

                            # print(x, y, w, h)

                            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

                            # how many cnt or bbox match 3 filter pre-requirements in each frame
                            i = i + 1
    print(i)

    list_bbox_num.append(i)

    # reset i loop counter
    i = 0

    print(list_bbox_num)



    ### Display
    #imgColor = cv2.resize(imgColor, (0, 0), None, 0.7, 0.7)

    ### Display the Mask
    imgColor = cv2.resize(mask, (0, 0), None, 0.7, 0.7)
    img = cv2.resize(img, (0, 0), None, 0.7, 0.7)
    cv2.imshow('Image', img)
    cv2.imshow('Image Color', imgColor)
    cv2.waitKey(0)