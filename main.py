import cv2
import mediapipe as mp

#import image
img_path = 'miagoth.jpeg'
capture = cv2.imread('img_path')

H, W, _ = capture.shape

#detect face in image
mp_detction = mp.solutions.face_detection

with mp_detction.FaceDetection(min_detection_confidence=0.5, model_selection=0) as face_detection:
    # converts the img to rgb format
    img_rgb = cv2.cvtColor(capture, cv2.COLOR_BGR2RGB)
    # process the image and detects faces
    results = face_detection.process(img_rgb) 

    #print results.detections
    
    if results.detections is not None: 
        for face in results.detections:
            data = face.location.data
            bbox = data.relative_bounding_box

            x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

            x1 = int(x1 * W)
            y1 = int(y1 * W)
            w = int(w * W)
            h = int(h * W)

            capture = cv2.rectangle(capture, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 10)

cv2.imshow('Face Detection', capture)
cv2.waitKey(0)

#extract face location

#blur face in image

#save image with blurred face