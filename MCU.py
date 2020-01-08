import time
import Lab3UploadPictureToAWSS3.s3
import Lab2AWSIoTconnectivity.connectivity
import Lab1EdgeFaceDetection.facedetection

############ step 1 Start your show!!! face detection -----------I am beauty sperator-----
def initialize_facedetection():
    global faceDetectAlgorithm, video_stream
    faceDetectAlgorithm, video_stream = Lab1EdgeFaceDetection.facedetection.initialize_facedetection()
    print("initiallize facedetection OK")
    
def facedetection_loop():
    global result, image_name
    result = False
    image_name = 'None'
    
### Your Beautyful work should be under
    result,image_name = Lab1EdgeFaceDetection.facedetection.face_detection_loop(
        'your face detection algorithm put here',
        'your video stream should be here'
    )
### Do not cross over me, thanks!!!!!!!!!!!!!!   
    print( result,image_name)  
    return result, image_name
    
############# step 1 DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


############ step 2 try to upload your detected image to S3 server
def initialize_s3():
    global s3_client
### Put your code down
   
    
### Put your code up
    print("initiallize s3 connectivity done")  
    
def TransmitImageData():
### Put your code down

### Put your code up
    print("Transmit image data done")

############# step 2 DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

############ step 3 try to upload your IoT data(your group,you name ...) to IoT core server
def initialize_connectivity():
    global iot_core_client
### Put your code down
    
### Put your code up
    print("initiallize connectivity done")
    
def TransmitIoTData():
### Put your code down

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
        

