import cv2
import numpy as np
import time
import os
import handtracker as htm
import pyscreenshot as ImageGrab
import sys


def paint():
    brushThickness = 10
    eraserThickness = 50


    folderPath = "guide"
    myList = os.listdir(folderPath)
    # print(myList)
    overlayList = []
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        overlayList.append(image)
    # print(len(overlayList))
    header = overlayList[0]
    drawColour = (0, 255, 0)


    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    detector = htm.handDetector(detectionCon=0.85)

    xp, yp = 0, 0

    imgCanvas = np.zeros((720, 1280, 3), np.uint8)

    i = 0

    while True:
        i += 1
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)

        if len(lmList) != 0:
            # print(lmList)

            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]
            fingers = detector.fingersUp()
            # print(fingers)

            if(fingers[1] and fingers[2]):
                # print("selectionMode")
                xp, yp = x1, y1
                if y1 < 125:
                    if 200 < x1 < 400:
                        header = overlayList[0]
                        drawColour = (0, 255, 0)
                    elif 500 < x1 < 700:
                        header = overlayList[1]
                        drawColour = (0, 0, 255)

                    # elif 0 < x1 < 200:
                    #     im = ImageGrab.grab()
                    #     im.save("screenshots/ssimg.png")
                    elif 800 < x1 < 1000:
                        header = overlayList[2]
                        drawColour = (0, 255, 255)
                    elif 1050 < x1 < 1200:
                        header = overlayList[3]
                        drawColour = (0, 0, 0)
                cv2.rectangle(img, (x1, y1-15), (x2, y2+15),
                            drawColour, cv2.FILLED)

            if(fingers[1] and fingers[2] == False):
                cv2.circle(img, (x1, y1), 10, drawColour, cv2.FILLED)
                # print("Draw Mode")
                if xp == 0 and yp == 0:
                    xp, yp = x1, y1
                if drawColour == (0, 0, 0):
                    cv2.line(img, (xp, yp), (x1, y1), drawColour, eraserThickness)
                    cv2.line(imgCanvas, (xp, yp), (x1, y1),
                            drawColour, eraserThickness)
                else:
                    cv2.line(img, (xp, yp), (x1, y1), drawColour, brushThickness)
                    cv2.line(imgCanvas, (xp, yp), (x1, y1),
                            drawColour, brushThickness)
                    xp, yp = x1, y1

            if(fingers[1] and fingers[2] and fingers[3] and fingers[4]):
                imgCanvas = np.zeros((720, 1280, 3), np.uint8)
            if(fingers[1] and fingers[2] and fingers[3] and fingers[4] == False):

                ab = str(i)
                x = "screenshots/ssimg"+ab
                x = x+".png"
                im = ImageGrab.grab()
                im.save(x)
                print(x)
            # if(fingers[1] and fingers[4] and fingers[2] == False and fingers[3] == False):
            #     sys. exit()

        img[0:125, 0:1280] = header
        img = cv2.addWeighted(img, 0.5, imgCanvas, 0.5, 0)
        cv2.imshow('Image', img)
        # cv2.imshow('Board', imgCanvas)
        cv2.waitKey(1)
