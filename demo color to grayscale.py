# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 13:54:56 2024

@author: kavin
"""
import cv2
'''
img1 = cv2.imread("C:\\Users\\kavin\\Downloads\\download (3).jpeg",1)
img1 = cv2.resize(img1,(1280,700))
print(img1)
cv2.imshow('original',img1)

img2 = cv2.imread("C:\\Users\\kavin\\Downloads\\download (3).jpeg",0)
img2 = cv2.resize(img1,(1280,700))
print(img1)
cv2.imshow('black and white',img1)

img3 = cv2.imread("C:\\Users\\kavin\\Downloads\\download (3).jpeg",-1)
img3 = cv2.resize(img1,(1280,700))
print(img1)
cv2.imshow('high saturation',img1)

img3 = cv2.flip(img1,0) # it accepts 3 parameters 0,-1,1

cv2.waitKey()
cv2.destroyAllWindows()
'''

# Image conversion project colored image into grayscale

path = input("Enter the path and name of an image === ")
print('You enter this ===',path)

img = cv2.imread(path,0)
cv2.imshow('converted images==',img)

k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite('D:\\computer vision\\output.png',img)
else:
    cv2.destroyAllWindows()



