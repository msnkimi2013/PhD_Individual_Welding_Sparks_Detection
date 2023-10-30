import cv2
import cvzone
from cvzone.ColorModule import ColorFinder



### Initialize the Welding Video
cap_w = cv2.VideoCapture('Final_Fire_Test/AAA_Fire_MVI_0188_Clip.mp4')

### Create the ColorFinder object
myColorFinder = ColorFinder(False)



# 20221110
hsvVals_w = {'hmin': 0, 'smin': 0, 'vmin': 250, 'hmax': 179, 'smax': 250, 'vmax': 255}



### welding zone filter
Img_width = 1920
Img_height = 1088

# welding zone filter relative coordinates
center_x = 0.5
center_y = 0.6
width = 1
height = 0.8

# welding zone filter left_x top_y w h coordinates
WZF_x = center_x * Img_width - width * Img_width * 0.5
WZF_y = center_y * Img_height - height * Img_height * 0.5
WZF_w = width * Img_width
WZF_h = height * Img_height


### loop counter
i = 0

### loop conter list
i_list = []

### x coordinate compare

# former_x = 0

# list_bbox_num = []

# print each area in one single frame
area_list = []





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

        # area list
        area_list.append(area)

        if 1 < area < 20000 :

            (x, y, w, h) = cv2.boundingRect(cnt)

            # print(x, y, w, h)

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)



            # cnt area filter the fire
            if 2500 < area < 18000 :

                ### Welding Zone Filter Start
                if x > WZF_x :
                    if (x + w) < (WZF_x + WZF_w) :
                        if y > WZF_y :
                            if (y + h) < (WZF_y + WZF_h):


                                # how many cnt or bbox match 3 filter pre-requirements in each frame
                                i = i + 1
    print(i)

    # continuous 10 frame judgement
    i_list.append(i)
    Sum = sum(i_list)

    # list_bbox_num.append(i)
    if len(i_list) > 10:
        i_list=[]
        # reset i loop counter

        if Sum > 10:

            # Fire Message
            img = cv2.putText(img, 'FIRE', (200, 200), cv2.FONT_ITALIC,
                           8, (0,0,255), 10, cv2.LINE_AA)

    i = 0
    # print(list_bbox_num)



    # area list
    # sorted_area_list = sorted(area_list, reverse= True)
    # print(sorted_area_list)
    #
    # area_list = []



    ### Display
    #imgColor = cv2.resize(imgColor, (0, 0), None, 0.7, 0.7)

    ### Display the Mask
    imgColor = cv2.resize(mask, (0, 0), None, 0.7, 0.7)
    img = cv2.resize(img, (0, 0), None, 0.7, 0.7)
    cv2.imshow('Image', img)
    cv2.imshow('Image Color', imgColor)
    cv2.waitKey(0)