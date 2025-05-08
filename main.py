import cv2
from cvzone.FaceDetectionModule import FaceDetector

#import image
capture = cv2.VideoCapture(0) 

while True:
    value,frame = capture.read()
    cv2.imshow("Video", frame)
    cv2.waitKey(1)

#detect face in image

#extract face location

#blur face in image

#save image with blurred face