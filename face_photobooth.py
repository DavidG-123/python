#David George

import cv2
import os
from time import sleep
import time
from datetime import datetime
import pyautogui
import numpy as np
from PIL import ImageGrab
from PIL import Image
red = "\033[1;31;40m"; white = "\033[1;37;40m"; green = "\033[1;32;40m"; blue = "\033[1;36;40m"; yellow = "\033[1;33;40m"

def main():
    print(red, end='')
    for i in range(83):
       print("Welcome to the Photobooth program. When you are ready to take the picture, press Q."[i], sep='', end='', flush=True); sleep(.03)
    print()
    cascPath = "haarcascade.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    video_capture = cv2.VideoCapture(0)


    sleep(0.1)

    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
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
    loadIt(641, 0)
    
    
def preset(beach_one, beach_two, beach_three, cabana, desert, solar_system, volcano):
    for a in range(38):
        print("Which background template do you want?"[a], end='', sep='', flush=True); sleep(.05)
    print(); choice = str.upper(input("Beach, Beach 2, Beach 3, Cabana, Desert, Outer Space, or Volcano: " + f"{chr(10)}"))
    if choice == "BEACH" or choice == "BEACH 2" or choice == "BEACH 3" or choice == "CABANA" or choice == "DESERT" or choice == "OUTER SPACE" or choice == "VOLCANO":
        if choice == "BEACH": return beach_one
        elif choice == "BEACH 2": return beach_two
        elif choice == "BEACH 3": return beach_three
        elif choice == "CABANA": return cabana
        elif choice == "DESERT": return desert
        elif choice == "OUTER SPACE": return solar_system
        elif choice == "VOLCANO": return volcano
        loadIt(0, 0)
    else:
        def loopChoice():
            choice = str.upper(input("Beach, Beach 2, Beach 3, Cabana, Desert, Outer Space, or Volcano: " + f"{chr(10)}"))
            if choice == "BEACH" or choice == "BEACH 2" or choice == "BEACH 3" or choice == "CABANA" or choice == "DESERT" or choice == "OUTER SPACE" or choice == "VOLCANO":
                return choice
            else:
                loopChoice()
        choice = loopChoice()
        if choice == "BEACH": return beach_one
        elif choice == "BEACH 2": return beach_two
        elif choice == "BEACH 3": return beach_three
        elif choice == "CABANA": return cabana
        elif choice == "DESERT": return desert
        elif choice == "OUTER SPACE": return solar_system
        elif choice == "VOLCANO": return volcano
        print(white, end='')
        loadIt(0, 0)

def loadIt(x, y):
    if x == 641:
        presetImg = preset(Image.open('vanilla_pics/beach.png'), Image.open('vanilla_pics/beach2.png'), Image.open('vanilla_pics/beach3.png'), Image.open('vanilla_pics/cabana.png'), Image.open('vanilla_pics/desert.png'), Image.open('vanilla_pics/solar-system.png'), Image.open('vanilla_pics/volcano.png')).load()
    x = 0
    image_og = Image.open('frame.png')

    width, height = image_og.size

    pixels_original = image_og.load()

    r, g, b = pixels_original[x, y]
    while y < 480:
                    
        for z in range(0, 640):
            color = pixels_original[z, y]
            rr, gg, bb = color


            if rr <= 157 and rr >= 137 and gg >= 201 and bb <= 131 and bb >= 111:
                pixels_original[z, y] = presetImg[z, y]
        y += 1
    image_og.show()
    now = datetime.now()
    theTime = str(now.strftime("%Y-%B-%d %H-%M-%S"))
    filename = str("gallery/" + f"{theTime}" + ".png")
    image_og.save(filename)

if __name__ == "__main__":
    main()
print(red, end='')
for a in range(42):
    print("Thank you for using my Photobooth program!"[a], end='', sep='', flush=True); sleep(.03)
print(white)
