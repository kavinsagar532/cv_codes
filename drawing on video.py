# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 22:35:07 2024

@author: kavin
"""

import cv2
import datetime

cap = cv2.VideoCapture("C:\\Users\\kavin\\Downloads\\test2.mp4")
print('for width===',cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('for height===',cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 3 for width , 4 for height
#print('width===',cap.get(3))
#print('height===',cap.get(4))

while (cap.isOpened()):
    ret,frame = cap.read()
    frame = cv2.resize(frame,(800,600))
    if ret == True:
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        text = 'Height: ' + str(cap.get(4)) + ' Width: ' + str(cap.get(3))
        frame = cv2.putText(frame , text , (10,20) , font , 1 , (0,120,0), 1 , cv2.LINE_AA)
        date_data = "Date: " + str(datetime.datetime.now())
        frame = cv2.putText(frame , date_data,(20,50),font , 1 , (100,5,255),1,cv2.LINE_AA)
        cv2.rectangle(frame,(384,10),(510,128),(128,0,128),8)
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
