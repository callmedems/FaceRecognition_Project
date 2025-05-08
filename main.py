import cv2
from cvzone.FaceDetectionModule import FaceDetector

#import image
capture = cv2.VideoCapture(0) 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


#detect face in image

#extract face location

#blur face in image

#save image with blurred face