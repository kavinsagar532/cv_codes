# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 14:26:31 2024

@author: kavin
"""

'''import cv2
cap = cv2.VideoCapture("C:\\Users\\kavin\\Downloads\\test2.mp4")
print('cap',cap)

while True:
    ret , frame = cap.read()
    frame = cv2.resize(frame,(700,450))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    k = cv2.waitKey(25)
    if k == ord('q') & 0xFF:
        break
cap.release()
cv2.destroyAllWindows()'''

#Now capture video from webcam and save into memory
'''
import cv2

cap = cv2.VideoCapture(0)

print('cap',cap)

while cap.isOpened():
    ret , frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(700,450))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',frame)
        cv2.imshow('gray',gray)
        k = cv2.waitKey(25)
        if k == ord('q') & 0xFF:
            break
cap.release()
cv2.destroyAllWindows()
'''

import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
#It contain 4 parameter , name , codec , fps , resolution
output = cv2.VideoWriter('D:\\computer vision\\output_.avi',fourcc,10.0,(640,480))

print('cap',cap)

while cap.isOpened():
    ret , frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',frame)
        cv2.imshow('gray',gray)
        output.write(frame)
        k = cv2.waitKey(25)
        if k == ord('q') & 0xFF:
            break
cap.release()
output.release()
cv2.destroyAllWindows()

