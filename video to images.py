# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:35:55 2024

@author: kavin
"""
'''
# Break Video into Multiple Images and store in a folder

import cv2

vidcap = cv2.VideoCapture("D:\\D DRIVE\\movie\\www.1TamilMV.yt - Romeo (2024) Tamil TRUE WEB-DL - 1080p - AVC - (DD5.1 - 640Kbps  AAC) - 2.8GB - ESub.mkv")

ret,image = vidcap.read()
count = 0
while True:
    if ret == True:
        cv2.imwrite('D:\\computer vision\\frames\\imgN%d.jpg'%count,image)
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count ** 100))
        ret , image  = vidcap.read()
        cv2.imshow('res',image)
        print(count)
        count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            cv2.destroyAllWindows()
            
vidcap.release()
cv2.destroyAllWindows()
'''
import cv2

# Path to the video file
video_path = "D:\\D DRIVE\\movie\\www.1TamilMV.yt - Romeo (2024) Tamil TRUE WEB-DL - 1080p - AVC - (DD5.1 - 640Kbps  AAC) - 2.8GB - ESub.mkv"

# Open the video file
vidcap = cv2.VideoCapture(video_path)

# Check if the video was opened successfully
if not vidcap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get the frames per second (fps) of the video
fps = int(vidcap.get(cv2.CAP_PROP_FPS))
print(f"FPS: {fps}")

# Frame counter
count = 0

while True:
    # Read the next frame from the video
    ret, image = vidcap.read()
    
    if not ret:
        break  # Break the loop if no frame is returned

    # Save the frame as an image file
    cv2.imwrite(f'D:\\computer vision\\frames\\imgN{count}.jpg', image)
    
    # Print the frame count
    print(f"Saved frame {count}")
    
    # Move to the next frame at 1 second intervals
    vidcap.set(cv2.CAP_PROP_POS_FRAMES, (count) * fps)
    
    # Display the frame
    cv2.imshow('Frame', image)
    
    count += 1
    
    # Exit if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
vidcap.release()
cv2.destroyAllWindows()
