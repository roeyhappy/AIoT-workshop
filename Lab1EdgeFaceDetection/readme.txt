Lab 1: face detection
Introduction
In this lab, we will introduce our workshop case study and setup tools on your local Raspberry Pi 4 enable you to detect face

Workshop Case Study
Every team have been assigned a set of hardware, including a 4G Wi-Fi, a raspberry pi 4, a usb camera, a led light and a micro usb cable.

Step 1 
You must initialize the face detection module by calling initialize_facedetection() in fucntion initialize_facedetection() in MCU.py
it will return faceCascade, cap two varible for next step use

Step 2 
Now you can start to capture your image and capture your face by calling 
	face_detection_loop(faceCascade, cap) in facedetection_loop() in MCU.py
	This fucntion use two parameters from step 1!!!!
	
	This function will return two varibles that you are going to use:
		image_name: your captured image name
		result: if you camera captured a image



Step 4 in MCU.py click run