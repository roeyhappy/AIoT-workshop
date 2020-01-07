import time
import Lab3- Upload Picture To AWS S3/s3
import connectivity


def initialize_connectivity():
#Put your connectivity init here
    print("initiallize connectivity Not OK")

def initialize_s3():
#Put your s3 init here
    print("initiallize s3 connectivity Not OK")  
    
def TransmitImageData():
#Put your s3 transmit code here
    print("Transmit image data Not OK")
    
def TransmitIoTData():
#Put your IoT core transmit here
    print("transmit IoT Data not OK")
    
def StartMeasureImage():
#Put your Start your camera captureing work here
    print("start camera not OK")


def loop():
    while True:
        #blocking function if no image is detected
        result = StartMeasureImage()
        if result:
            TransmitImageData()
            TransmitIoTData()
        else:
            print("No image is captured")
        #at least delay for 2 seconds
        time.sleep(2)
        
initialize_s3()        
initialize_connectivity()      
loop()
        

