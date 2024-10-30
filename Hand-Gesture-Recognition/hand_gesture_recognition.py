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

def call_me(lmList):
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute+1
    pywhatkit.sendwhatmsg("+91_phone_number_", "Hello, How are you today", current_hour, current_minute,0)


#################################
wCam,hCam=640,480
#################################

myScreenshot = pyautogui.screenshot()

cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime=0

detector=htm.handDetector(detectionCon=0.7)
opened_1=False
opened_2=False

while True:
    success,img=cap.read()
    img=cv2.flip(img, 1)
    img=detector.findHands(img)
    lmList=detector.findPosiiton(img,draw=True)
    if len(lmList)!=0:
        print(lmList)
        tind=[8,12,16,20]
        tg=[]
################################################################################################3
        for i in tind:
            if lmList[i][2]<lmList[i-2][2]:
                tg.append(1)
            else:
                tg.append(0)
        #print(tg)
####################################################################################################
        if tg[2]==0 and tg[3]==0 and tg[0]==1 and tg[1]==1 and not opened_1:
            # opened_1=True
            print("selfie working")
#########################################################################################################3
        if tg[2] == 0 and tg[3] == 0 and tg[0] == 0 and tg[1] == 1 and not opened_1:
            # opened_1=True
            print("Middle Finger Raised")

            #subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
            #cv2.imwrite(r'C:\Users\Aakash\Downloads\my_face.png', img)
############################################################################################################33

        if lmList[4][2]<lmList[8][2] and lmList[8][2]<lmList[20][2]:
            if lmList[8][1] > lmList[6][2] and lmList[12][1] > lmList[10][1] and lmList[16][1] > lmList[14][1] and not opened_2:
                print("call me")
                #opened_2 = True
                # call_me(lmList)

##########################################################################



    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img, f'FPS: {int(fps)}',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,
                (255,0,0),3)
    cv2.imshow("Img",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




