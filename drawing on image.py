# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 21:40:47 2024

@author: kavin
"""

import numpy as np
import cv2

#img = cv2.imread("C:\\Users\\kavin\\Downloads\\download (3).jpeg")
#img = cv2.resize(img,(600,700))


#zeros - black , ones - white
img = np.zeros([512,512,3] , np.uint8) * 255 


#simple line , img,start,end,color,thickness
img = cv2.line(img,(0,0),(200,200),(154,92,424),8)

#arrowed line 
img = cv2.arrowedLine(img,(0,125),(255,255),(255,0,255),10)

#rectangle
img = cv2.rectangle(img,(384,10),(510,128),(128,0,128),10)

#circle img,start,radius,color,thickness
img = cv2.circle(img,(447,125),63,(214,255,0),5)

#puttext img,text,start,font,fontsize,color,thickness,linetype
img = cv2.putText(img,'Bear',(20,500),cv2.FONT_ITALIC,4,(0,125,255),10,cv2.LINE_AA)

#ellipse img,start,(length,height),rotation point x and y,angle,color,thickness
img = cv2.ellipse(img,(400,600),(100,50),0,0,180,155,5)




cv2.imshow("res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()