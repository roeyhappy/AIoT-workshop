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

region is the location of s3 server, for now it should be 'cn-north-1'
access_key is the 


