import cv2
import time
# import numpy as np
import HandTrackingModule as htm
# import math
# import subprocess
# from AppOpener import open
import pyautogui
import pywhatkit
import datetime

#################################
wCam, hCam = 640, 480
#################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)
opened_1 = False
opened_2 = False

while True:
    success,img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList = detector.findPosiiton(img,draw=True)
    if len(lmList) != 0:
        # print(lmList)
        tind=[8, 12, 16, 20]
        tg = []

        for i in tind:
            if lmList[i][2] < lmList[i-2][2]:
                tg.append(1)
            else:
                tg.append(0)

        print(tg)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1,
                (255, 0, 0), 3)
    cv2.imshow("Img", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

