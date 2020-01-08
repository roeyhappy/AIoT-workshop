import time
import Lab3UploadPictureToAWSS3.s3
import Lab2AWSIoTconnectivity.connectivity
import Lab1EdgeFaceDetection.facedetection

############ step 1 try to start your camera and detect a real human face
def initialize_facedetection():
#### Put your facedetection init down
    global facecade,cap
    
    facecade,cap = Lab1EdgeFaceDetection.facedetection.initialize_facedetection()
    print ('initialize face detection is done ')
    return
#### Put your facedetection init up 
    print("initiallize facedetection Not OK")
    
def facedetection_loop():
    global result, image_name
    result = False
    image_name = 'None'
### Put your facedetection loop down
    #facecade,cap = Lab1EdgeFaceDetection.facedetection.initialize_facedetection()
    result,image_name = Lab1EdgeFaceDetection.facedetection.face_detection_loop(facecade,cap)
### Put your facedetection loop up    
    print( result,image_name)  
    return result, image_name
    
############# step 1 DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


############ step 2 try to upload your detected image to S3 server
def initialize_s3():
### Put your code down
    global s3_client
    s3_client = Lab3UploadPictureToAWSS3.s3.s3_init('cn-north-1','AKIA3NC37QVN3WCEFJGR','Py4M+cjldIdqaQCAGeiernuBaOXdgOO1thREuRFp')
### Put your code up
    print("initiallize s3 connectivity done")  
    
def TransmitImageData():
### Put your code down
    Lab3UploadPictureToAWSS3.s3.s3_upload(image_name, 'group003', image_name, s3_client)
### Put your code up
    print("Transmit image data done")

############# step 2 DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

############ step 3 try to upload your IoT data(your group,you name ...) to IoT core server
def initialize_connectivity():
### Put your code down
    global iot_core_client
    iot_core_client = Lab2AWSIoTconnectivity.connectivity.IoT_core_init("a3afq7zrw2mcf4.ats.iot.cn-north-1.amazonaws.com.cn", 8883, r'root-CA.crt', r'private.pem.key', r'device.pem.crt')
### Put your code up
    print("initiallize connectivity done")
    
def TransmitIoTData():
### Put your code down
    mytopicheader = "pg/efd/d-1a2d3a2ea4f84eb6b8197a3a3e4a6ad8:2eaa3bcbce2d49f0adf7b3edc3cc4638:sn001/data"
    Lab2AWSIoTconnectivity.connectivity.transmit_message_to_cloud(mytopicheader, image_name, "group003", '3', "roy,ben,tom",'everything is good', iot_core_client)
### Put your code up
    print("transmit IoT Data not OK")

############# step 3 DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
def loop():
    while True:
        #blocking function if no image is detected
        result, image_name = facedetection_loop()
        if result:
            TransmitImageData()
            TransmitIoTData()
        else:
            print("No image is captured")
        #get Enter keep contingue
        #input()
        
        
        
initialize_facedetection()      
initialize_s3()        
initialize_connectivity()      
loop()
        

