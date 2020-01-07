'''
Haar Cascade Face detection with OpenCV  
    Based on tutorial by pythonprogramming.net
    Visit original post: https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/  
Adapted by Marcelo Rovai - MJRoBot.org @ 7Feb2018 
'''

import numpy as np
import cv2
import datetime
import time
import boto3
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json



# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade = cv2.CascadeClassifier('/home/pi/opencv/opencv-3.4.1/data/haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
img_counter = 0
image_name = ''
while True:
    ret, img = cap.read()
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,        
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )

    for (x,y,w,h) in faces:
        #now_time = datetime.datetime.now()
        now_time = datetime.datetime.now()
        str_time = now_time.strftime("%Y%m%d%H%M%S")
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        image_name = str_time + ".png"
        cv2.imwrite(image_name, img)
        print("captured face!")


        
        s3 = boto3.client(
        's3',
        region_name='cn-north-1',
        # Hard coded strings as credentials, not recommended.
        aws_access_key_id='AKIA3NC37QVN3WCEFJGR',
        aws_secret_access_key='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'
        )
        
        bucket = 'pgiot-s3-test/'
        constant1 = 'efd/'
        group = 'group002/'
        year = now_time.strftime("%Y") + '/'
        month = now_time.strftime("%m") + '/'
        date = now_time.strftime("%d") + '/'
       
        s3_pic_url =  group + year + month + date
        #print("s3_pic_url:", s3_pic_url)

        #response = s3.upload_file('test.jpg', 'pgiot-s3-test', 'test.jpg')
        response = s3.upload_file(image_name, 'pgiot-s3-test', constant1 + s3_pic_url + image_name, ExtraArgs={'ACL': 'public-read'})
        print("response:", response)
        #response = s3.list_buckets()
        # Import SDK packages


        # For certificate based connection
        myMQTTClient = AWSIoTMQTTClient("myClientID")
        myMQTTClient.configureEndpoint("a3afq7zrw2mcf4.ats.iot.cn-north-1.amazonaws.com.cn", 8883)
        myMQTTClient.configureCredentials(r'root-CA.crt', r'private.pem.key', r'device.pem.crt')
        myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
        myMQTTClient.configureDrainingFrequency(1)  # Draining: 2 Hz
        myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
        myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

        mytopicheader = "pg/efd/d-1a2d3a2ea4f84eb6b8197a3a3e4a6ad8:2eaa3bcbce2d49f0adf7b3edc3cc4638:sn001/data"
        picurl = s3_pic_url + image_name
        now_time = datetime.datetime.utcnow()
        publish_time = now_time.strftime("%Y-%m-%dT%H:%M:%S")
        ct = time.time()
        date_ms = (ct - int(ct))*1000
        publish_time_2 = "%s.%03d" %(publish_time, date_ms)

        mypayload = {
            "groupId": "group002",
            "memberCount": "3",
            "memberNames": "Roy,Ben,Tom",
            "eventId": "1",
            "pictureId": picurl,
            "publishTime": publish_time_2,
            "blessings":"Happy new year!"
        }


        topicbody = json.dumps(mypayload)
        myMQTTClient.connect()
        myMQTTClient.publish(mytopicheader, topicbody, 0)

                
        cv2.imshow('imshow',img)

        k = cv2.waitKey(30) & 0xff
        if k == 27: # press 'ESC' to quit
            break

cap.release()
cv2.destroyAllWindows()