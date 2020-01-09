import time
import Lab2UploadPictureToAWSS3.s3 as s3server
import Lab3AWSIoTconnectivity.connectivity as IoTcore
import Lab1EdgeFaceDetection.facedetection as faceDetect

############ step 1 Start your show!!! face detection -----------I am beauty sperator-----
def initialize_facedetection():
    global faceDetectAlgorithm, video_stream
    faceDetectAlgorithm, video_stream = faceDetect.initialize_facedetection()
    print("initiallize facedetection OK")
    
def facedetection_loop():
    global result, image_name
    result = False
    image_name = 'None'
    
### Your Beautyful work should be under!!!!!!!
    faceAlgorithm = 'your face detection algorithm put here'
    face_video_stream = 'your face pictures should be here'

### Do not cross over me, thanks!!!!!!!!!!!!!! 
    result,image_name = faceDetect.face_detection_loop(
        faceAlgorithm,
        face_video_stream
    )  
    print( result,image_name)  
    return result, image_name
    
############# step 1 DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


############ step 2 try to upload your detected image to S3 server
def initialize_s3():
    global s3_client
     
### Your Beautyful work should be under!!!!!!!
    region = 'put your region name here'
    access_key = 'put your access_key here'
    secret_key = 'put your secret_key here'
    
### Do not cross over me, thanks!!!!!!!!!!!!!! 
    s3_client = s3server.s3_init(region, access_key, secret_key)
    print("initiallize s3 connectivity done")  
    
def TransmitImageData():
### Your Beautyful work should be under!!!!!!!
    imageName = 'the image you captured in step 1'
    groupid = 'which group you are in??'
    
### Do not cross over me, thanks!!!!!!!!!!!!!!
    s3server.s3_upload(imageName, group, s3_client)
    print("Transmit image data done")

############# step 2 DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

############ step 3 try to upload your IoT data(your group,you name ...) to IoT core server
def initialize_connectivity():
    global iot_core_client
    
### Your Beautyful work should be under!!!!!!!
    endpoint = 'put your endpoint here'
    port = 'put your port number here'
    root_cert= 'put your root certification location here'
    private_key= 'put your private key here'
    device_cert= 'put your device certification here'
### Do not cross over me, thanks!!!!!!!!!!!!!!
    iot_core_client = IoTcore.IoT_core_init(endpoint,
        port,
        root_cert,
        private_key,
        device_cert
    )
    print("initiallize connectivity done")
    
def TransmitIoTData():
    mytopicheader = "pg/efd/d-1a2d3a2ea4f84eb6b8197a3a3e4a6ad8:2eaa3bcbce2d49f0adf7b3edc3cc4638:sn001/data"

### Your Beautyful work should be under!!!!!!!
    groupid = 'which group you are in??'
    group_member_count = 'How many members in your group'
    member_names = 'you name, you team member 1 name, ...'
    blessing = 'what do you want to say, be careful, everyone can see ^_^'
### Do not cross over me, thanks!!!!!!!!!!!!!!
    transmit_message_to_cloud(mytopicheader, 
        image_name, 
        groupid, 
        group_member_count, 
        member_names,
        blessing, 
        iot_core_client
    )
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
        

