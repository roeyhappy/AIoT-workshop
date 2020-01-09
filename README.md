# AIoT-workshop

## Step 1: How to make your camera working and detect a face?

In this step, there are two functions provided to you in **MCU.py**
### initialize_facedetection()
This function is used for initiallize camera hardware and face detection algorithm, ***you do not have to do anything with this fucntion***
you need to aware that this fucntion return two varibles:
+ **faceDetectAlgorithm**: this is a algorithm that used to detect a human face 
+ **video_stream**: this is the video that camera captured
### facedetection_loop()
This function is used for trigger the camera shooting and pass the video into our algorithm. Do you remember the last function **initialize_facedetection()** provides you? **You need to fill in the algorithm and video captured varibles**, for example, your working zone looks like this: 
+  Your Beautyful work should be under!!!!!!!
    + faceAlgorithm = 'your face detection algorithm put here' 
    + face_video_stream = 'your face pictures should be here' 
+ Do not cross over me, thanks!!!!!!!!!!!!!! 

After you finish your work, you can run MCU.py by press Run button in IDE or python3 MCU.py in command line. You can see a windows pop up, and if you show your face in the camera, a blue squre will capture your face,you can checkout ![example](https://github.com/roeyhappy/AIoT-workshop/blob/master/20200109105148.jpg)

After you set up your most beautyful face, you press **Enter**, and the picture will captured and saved in local folder. Your step 1 is done!!!

## Step 2: Transfer your face image to S3 server in AWS
In this step, there are two functions provided to you **MCU.py**
### initialize_s3()
This function is used to initialize the s3 server, there are three varibles you need to work with:

+  Your Beautyful work should be under!!!!!!!
    + region = 'put your region name here'
    + access_key = 'put your access_key here'
    + secret_key = 'put your secret_key here'
+ Do not cross over me, thanks!!!!!!!!!!!!!! 

1. region is the location of s3 server, for now it should be 'cn-north-1'
2. access_key is the id key that access the aws S3
3. secret key is the password key that access the aws S3

All of them, should not expose to public, and it will not provided in this document, you will receive a secure source that store these.
### TransmitImageData()
This function is used to transmit captured image (do you remember what you did in step 1 when you press Enter key ??), there are two varibles you need to work with:

+  Your Beautyful work should be under!!!!!!!
    + imageName = 'the image you captured in step 1'
    + groupid = 'which group you are in??'    
+ Do not cross over me, thanks!!!!!!!!!!!!!!

1. imageName is the image that you captured in step 1 when you press Enter key, it is stored in your local folder named as "202001XXXXXXXXXX.jpg", you can either put imageName = "202001XXXXXXXXXX.jpg" or imageName = image_name
2. groupid is the group number that you are in, for example, you are in group 1, you should write your code as groupid = 'group001'

Then your step 2 is done!!!!!!!!!!!!!!!!!!!!!!!!

## Step 3: Transfer your IoT Data to IoT core in AWS
An face image is not enough to identify youself, you need extra information to show youself. And the information will trigger the publich to GCIT Family in Golden Pocket. There are two function you need to work with.
### initialize_connectivity()
There are 5 varibles that you need to work with:

+  Your Beautyful work should be under!!!!!!!
    + endpoint = 'put your endpoint here'
    + port = 'put your port number here'
    + root_cert= 'put your root certification location here'
    + private_key= 'put your private key here'
    + device_cert= 'put your device certification here'   
+ Do not cross over me, thanks!!!!!!!!!!!!!!

1. endpoint is the address of IoT core, this information is important, it will be in a seperate document.
2. port is a number that you need to connect to IoT core, it will be in a seperate document.
3. root_cert is used to identify the server is the real server.
4. private_key is used to unlock the message that received from servers.
5. device_cert is used to let server identify the device is the real device.

