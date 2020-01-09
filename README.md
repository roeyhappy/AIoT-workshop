# AIoT-workshop

## Step 1: How to make your camera working and detect a face?

In this step, there are two functions provided to you in MCU.py
### initialize_facedetection()
This function is used for initiallize camera hardware and face detection algorithm, ***you do not have to do anything with this fucntion***
you need to aware that this fucntion return two varibles **faceDetectAlgorithm**: this is a algorithm that used to detect a human face **video_stream**: this is the video that camera captured
### facedetection_loop()
This function is used for trigger the camera shooting and pass the video into our algorithm. Do you remember the last function **initialize_facedetection()** provides you? **You need to fill in the algorithm and video captured varibles**

