# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:02:15 2024

@author: kavin
"""

#screen recorder

import cv2 as c
import pyautogui as p
import numpy as np

rs = p.size()

fn = input('please enter any file name and path')

fps = 10.0

fourcc = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter(fn,fourcc,fps,rs)

c.namedWindow('Live_Recording',c.WINDOW_NORMAL)
c.resizeWindow('Live_Recording',(600,400))

while True:
    img = p.screenshot()
    f = np.array(img)
    f = c.cvtColor(f,c.COLOR_BGR2RGB)
    output.write(f)
    c.imshow('Live_Recording',f)
    if c.waitKey(1) == ord('q'):
        break

output.release()
c.destroyAllWindows()