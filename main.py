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

    #Converts image into grayscale  
    img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Detects faces on image
    face_frontal=frontal_cascade.detectMultiScale(img_gray, scaleFactor=1.3, minNeighbors=4)

    face_profile=profile_cascade.detectMultiScale(img_gray, scaleFactor=1.3, minNeighbors=4)

    #Join both classifiers
    merge_faces=list(face_frontal) + list (face_profile)

    # Aplied gaussian blurr for every face detected
    for (x, y, w, h) in merge_faces:
        ROI = img[y:y+h, x:x+w]
        blur = cv2.GaussianBlur(ROI, (99, 99), 0)
        img[y:y+h, x:x+w] = blur

    #Open camera
    cv2.imshow("Face blurring", img) #Pass image frame 

    #Standart quote to close de camera
    if cv2.waitKey(1) & 0xFF==ord('q'): #Press q from the key board to close the program 
        break

#Release the window resources at close
video.release()
cv2.destroyAllWindows()

