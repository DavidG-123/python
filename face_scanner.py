#David George

import cv2
import os
from time import sleep
import time
import pyautogui
import numpy as np
from PIL import ImageGrab
from PIL import Image
def main():
    for i in range(204):
        print("Welcome to the attractiveness rating program!!! Your camera will open shortly; align your face in frame and give us a big smile with widely opened eyes :). When you are ready to take the picture, press Q."[i], sep='', end='', flush=True); sleep(.03)
    load()

def load():
    cascPath = "haarcascade.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    video_capture = cv2.VideoCapture(0)


    sleep(0.1)

    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # use appropriate flag based on version of OpenCV
        if int(cv2.__version__.split('.')[0]) >= 3:
            cv_flag = cv2.CASCADE_SCALE_IMAGE
        else:
            cv_flag = cv2.cv.CV_HAAR_SCALE_IMAGE


        cv2.imshow('Video', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("frame.png", frame)
            sleep(2)
            break
    
    cv2.destroyAllWindows()


def symm():
    pass

main()
