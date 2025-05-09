import cv2

#import image

video = cv2.VideoCapture(0) #Sets 0 at camera ID
video.set (3, 640) #set width
video.set (4, 480) #set height

#Add haar cascade classifiers
frontal_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
profile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')


#Loop that initiates the camera
while True:

    capture, img=video.read()

    #Detects faces on image
    face_frontal=cv2.CascadeClassifier(frontal_cascade)

    face_profile=cv2.CascadeClassifier(profile_cascade)

    cv2.imshow("Image", img)

    cv2.waitKey(1) #delay time

