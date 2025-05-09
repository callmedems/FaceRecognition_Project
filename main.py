import cv2

#Camera set up
capture = cv2.VideoCapture(0) #Sets 0 at camera ID
capture.set (3, 640) #set width
capture.set (4, 480) #set height

#Loop that initiates the camera
while True:
    cap, img=capture.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1) #delay time



#detect face in image



#process and blur face in image

#save image with blurred face


#detect face in image

#process and blur face in image

#save image with blurred face