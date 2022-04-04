import cv2
from time import sleep
import time

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
        break

video_capture.release()
cv2.destroyAllWindows()

def main():
    pass
def load():
    pass
