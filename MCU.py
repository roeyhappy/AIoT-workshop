import time
import Lab3UploadPictureToAWSS3.s3
import Lab2AWSIoTconnectivity.connectivity
import Lab1EdgeFaceDetection.facedetection

############ step 1 try to start your camera and detect a real human face
def initialize_facedetection():
#### Put your facedetection init down
    global facecade,cap
    
    facecade,cap = Lab1EdgeFaceDetection.facedetection.initialize_facedetection()
    print ('I am done ')
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

### Put your code up
    print("initiallize s3 connectivity Not OK")  
    
def TransmitImageData():
### Put your code down

### Put your code up
    print("Transmit image data Not OK")

############# step 2 DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

############ step 3 try to upload your IoT data(your group,you name ...) to IoT core server
def initialize_connectivity():
### Put your code down

### Put your code up
    print("initiallize connectivity Not OK")
    
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
        input()
        
        
        
initialize_facedetection()      
initialize_s3()        
initialize_connectivity()      
loop()
        

