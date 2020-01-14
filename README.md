# AIoT-workshop

## Step 1: How to make your camera working and detect a face?

In this step, there are two functions provided to you in **MCU.py**
### initialize_facedetection()
This function is used for initialize camera hardware and face detection algorithm, ***you do not have to do anything with this function***
you need to aware that this function return two variables:
+ **faceDetectAlgorithm**: this is a algorithm that used to detect a human face 
+ **video_stream**: this is the video that camera captured
### facedetection_loop()
This function is used for trigger the camera shooting and pass the video into our algorithm. Do you remember the last function **initialize_facedetection()** provides you? **You need to fill in the algorithm and video captured variables**, for example, your working zone looks like this: ***you do not have to do anything with this function*** 
+  Your Beautiful work example!!!!!!!
    + faceAlgorithm = faceDetectAlgorithm 
    + face_video_stream = video_stream
+ Do not cross over me, thanks!!!!!!!!!!!!!! 

After you finish your work, you can run MCU.py by press Run button in IDE or python3 MCU.py in command line. You can see a windows pop up, and if you show your face in the camera, a blue square will capture your face, you can checkout ![example](https://github.com/roeyhappy/AIoT-workshop/blob/master/20200109105148.jpg)

After you set up your beautiful face, you press **Enter**, and the picture will captured and saved in local folder. Your step 1 is done!!!

## Step 2: Transfer your face image to S3 server in AWS
In this step, there are two functions provided to you **MCU.py**
### initialize_s3()
This function is used to initialize the s3 server, there are three variables you need to work with:

+  Your Beautiful work should be under!!!!!!!
    + region = 'put your region name here'
    + access_key = 'put your access_key here'
    + secret_key = 'put your secret_key here'
+ Do not cross over me, thanks!!!!!!!!!!!!!! 

1. region is the location of s3 server, for now it should be 'cn-north-1'
2. access_key is the id key that access the aws S3
3. secret key is the password key that access the aws S3

All of them, should not expose to public, and it will not be provided in this document, you can find this information in Raspberry /home/pi/AIoTlab/paramters.txt.

Then you need to go into **\AIoT-workshop\Lab2UploadPictureToAWSS3\s3.py** locate function  **s3_init(region, access_key, secret_key)** you need to fix the secret key parameter.
### TransmitImageData()
This function is used to transmit captured image (do you remember what you did in step 1 when you press Enter key ??), there are two variables you need to work with:

+  Your Beautiful work should be under!!!!!!!
    + imageName = 'the image you captured in step 1'
    + groupid = 'which group you are in??'    
+ Do not cross over me, thanks!!!!!!!!!!!!!!

1. imageName is the image that you captured in step 1 when you press Enter key, it is stored in your local folder named as "202001XXXXXXXXXX.jpg", you can either put imageName = "202001XXXXXXXXXX.jpg" or imageName = image_name
2. groupid is the group number that you are in, for example, you are in group 1, you should write your code as groupid = 'group001'

Then your step 2 is done!!!!!!!!!!!!!!!!!!!!!!!!

## Step 3: Transfer your IoT Data to IoT core in AWS
An face image is not enough to identify yourself, you need extra information to show youself. And the information will trigger the publish to GCIT Family in Golden Pocket. There are two function you need to work with.
### initialize_connectivity()
This function is used to initialize the IoT core connection. There are 5 variables that you need to work with:

+  Your Beautiful work should be under!!!!!!!
    + endpoint = 'put your endpoint here'
    + port = 'put your port number here'
    + root_cert= 'put your root certification location here'
    + private_key= 'put your private key here'
    + device_cert= 'put your device certification here'   
+ Do not cross over me, thanks!!!!!!!!!!!!!!

1. endpoint is the address of IoT core, this information is important, it will be in a separate document.
2. port is a number that you need to connect to IoT core, it will be in a separate document.
3. root_cert is used to identify the server is the real server.
4. private_key is used to unlock the message that received from servers.
5. device_cert is used to let server identify the device is the real device.
you can find all this information in Raspberry /home/pi/AIoTlab/

### TransmitIoTData()
This function is used to transmit message to IoT core. There are four variables you need to work with:

+  Your Beautiful work should be under!!!!!!!
    + thingname = 'your thing name should be here'
    + groupid = 'which group you are in??'
    + group_member_count = 'How many members in your group'
    + member_names = 'you name, you team member 1 name, ...'
    + blessing = 'what do you want to say, be careful, everyone can see ^_^'   
+ Do not cross over me, thanks!!!!!!!!!!!!!!

+ Your Beautiful work should be under!!!!!!!
    + You need to call Lab3AWSIoTconnectivity transmit_message_to_cloud() function to transmit your data
+ Do not cross over me, thanks!!!!!!!!!!!!!!

1. groupid is the group number that you are in, for example, you are in group 1, you should write your code as **groupid = 'group001'**
2. group_member_count is the information that you want to tell IoT core how many group members in your group, for example, **group_member_count = '3'**
3. member_names is the names in your group, for example, **member_names = 'roy, tom, ben'**
4. blessing is your imagination.
5. the last step is you need to go into Lab3AWSIoTconnectivity and use transmit_message_to_cloud() function to transmit your data

**Step 3 is done !!!!**

## Step 4: How to push a notification to Goldpocket from Lambda
In this step, there is no hands-on work to do.


