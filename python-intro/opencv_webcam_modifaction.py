# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 23:29:04 2015

@author: patrickchrist
"""

import cv2
cam = cv2.VideoCapture(0) # Get the stream of your webcam
running = True
while running:    # get current frame of video    
    running, frame = cam.read()    
    if running:    
        cv2.rectangle(frame, (100, 100), (200, 200), (255,0,0), 2)    
        cv2.imshow('frame', frame)        
        if cv2.waitKey(1) & 0xFF == 27:             # escape key pressed            
            running = False    
        else:        # error reading frame        
		print 'error reading video feed'
cam.release()
cv2.destroyAllWindows()
