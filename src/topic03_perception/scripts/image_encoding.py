#!/usr/bin/env python

import numpy as np
import cv2

image_name = "tree"

print("Read an image from file")
color_image = cv2.imread("/home/duc/catkin_ws/src/ros_essential_cpp/src/topic03_perception/images/tree.jpg", cv2.IMREAD_COLOR)

print ("Display image in native color")
cv2.imshow("Original Image", color_image)
cv2.moveWindow("Original Image",0,0)
print(color_image.shape)


height, width, channels = color_image.shape

print("Split the image into three channels")
blue, green, red = cv2.split(color_image)

cv2.imshow("Blue Channel", blue)
cv2.moveWindow("Blue Channel",0, height)

cv2.imshow("Red Channel", red)
cv2.moveWindow("Red Channel",0, height)

cv2.imshow("Green Channel", green)
cv2.moveWindow("Green Channel",0, height)


print ("Split the image into Hue, Saturation, Value channels")
hsv = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_image = np.concatenate((h,s,v),axis=1)
cv2.imshow("Hue, Saturation, Value Image", hsv_image)

print("Converts an image to a grayscale")
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray_image)
print(gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()