import time
import s3
import connectivity
import userapp

def initialize_connectivity():
#Put your connectivity init here
    print("initiallize connectivity OK")

def initialize_s3():
#Put your s3 init here
    print("initiallize s3 connectivity OK")    

def loop():
    while True:
        #blocking function if no image is detected
        result = userapp.StartMeasureImage()
        if result:
            userapp.TransmitIoTData()
            userapp.TransmitImageData()
        #at least delay for 2 seconds
        time.sleep(2)
        
        
        
loop()
        

