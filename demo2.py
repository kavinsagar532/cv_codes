# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 15:14:54 2024

@author: kavin
"""
#capture video from youtube
'''
import cv2
import pafy
import youtube_dl

url = 'https://www.youtube.com/watch?v=t0Q2otsqC4I'
data = pafy.new(url)
data = data.getbest(preftype = 'mp4')

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
print('check===',cap.isOpened())
cap.open(data.url)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#It contain 4 parameter , name , codec , fps , resolution
output = cv2.VideoWriter('D:\\computer vision\\tom and jerry.mp4',fourcc,10.0,(640,480))

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


import pafy
import cv2
import youtube_dl

url = 'https://www.youtube.com/watch?v=t0Q2otsqC4I'
data = pafy.new(url)

data = data.getbest(preftype = 'mp4')
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(data.url)
print('check===',cap.isOpened())

while(cap.isOpened()):
    ret , frame = cap.read()
    if ret == True:
        cv2.imshow('colorframe')
        
        if cv2.waitkey(1) & 0xFF == ord('q'):
            break
'''

import pafy      #open anaconda prompt and type pip install pafy
import cv2
url = "https://www.youtube.com/watch?v=SLD9xzJ4oeU"
data = pafy.new(url )
data = data.getbest(preftype="mp4")
cap = cv2.VideoCapture()   #Here parameter 0 is a path of any video use for webcam
cap.open(data.url)

#it is 4 byte code which is use to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480),0)

while(cap.isOpened()):
    ret, frame = cap.read()   #here read the frame
    
    if ret==True:
        
        gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #here flip is used to lip the video at recording time
        #frame = cv2.flip(frame,0)
        #output.write(gray)
        
        #cv2.imshow("Gray Frame",gray)
        cv2.imshow('Colorframe',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #press to exit
            break
    else:
        break
 
# Release everything if job is finished
cap.release()
output.release()
cv2.destroyAllWindows()
