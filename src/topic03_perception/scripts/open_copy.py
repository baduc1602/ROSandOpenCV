#!/usr/bin/env python

#import numpy: the data structure that will handle an image
import numpy as np

#import opennCV
import cv2

image_name = "tree"

print ("read an image from file")
img = cv2.imread("/home/duc/catkin_ws/src/ros_essential_cpp/src/topic03_perception/images/"+ image_name +".jpg")

print ("create a window holder for the image")
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

print("Display the image")
cv2.imshow("Image", img)

print("Press a key inside the image to make a copy")
cv2.waitKey(0)

print("image copied to folder images/copy/")
cv2.imwrite("/home/duc/catkin_ws/src/ros_essential_cpp/src/topic03_perception/images/copy/"+image_name+"-copy.jpg",img)