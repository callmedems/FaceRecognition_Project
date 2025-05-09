import cv2
import mediapipe as mp

#import image
img_path = 'img/face.jpg'
capture = cv2.imread('img/face.jpg')

#detect face in image
mp_detction = mp.solutions.face_detection

with mp_detction.FaceDetection(min_detection_confidence=0.5, model_selection=0) as face_detection:
    # converts the img to rgb format
    img_rgb = cv2.cvtColor(capture, cv2.COLOR_BGR2RGB)
    # process the image and detects faces
    results = face_detection.process(img_rgb) 
    
    for face in results.detections:
        data = face.location.data
        bbox = data.relative_bounding_box

        x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height
#extract face location

#blur face in image

#save image with blurred face