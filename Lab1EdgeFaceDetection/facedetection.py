import numpy as np
import cv2
import datetime
import time

def initialize_facedetection():
    faceCascade = cv2.CascadeClassifier('/home/pi/opencv/opencv-3.4.1/data/haarcascades/haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)
    cap.set(3,640) # set Width
    cap.set(4,480) # set Height
    return faceCascade, cap
    
    
def face_detection_loop(faceCascade, cap):
    image_name= ''
    result = False
    while True:
        ret, img = cap.read()
        #img = cv2.flip(img, -1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,        
            scaleFactor=1.2,
            minNeighbors=5,     
            minSize=(20, 20)
        )
        
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            result = True
            

        cv2.imshow('video',img)

        k = cv2.waitKey(30) & 0xff
        if k == 27: # press 'ESC' to quit
            break
        if k == 13: # press 'Enter' to save
            print("STEP 1:save image")
            now_time = datetime.datetime.now()
            str_time = now_time.strftime("%Y%m%d%H%M%S")
            image_name = str_time + ".png"
            cv2.imwrite(image_name, img)
            return result,image_name
                
    
        
#faceCascade, cap = initialize_facedetection()
#result,image = face_detection_loop(faceCascade, cap)
#print(result)
#print(image)