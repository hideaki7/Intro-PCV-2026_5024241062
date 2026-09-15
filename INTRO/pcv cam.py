# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 09:10:22 2026

@author: Samuel
"""

import cv2

cap = cv2.VideoCapture(0)
counter = 0

while True:
    _, frame = cap.read()

    mode = (counter // 10) % 3

    if mode == 0:
        frame[:, :, 1] = 0
        frame[:, :, 2] = 0
    elif mode == 1:
        frame[:, :, 0] = 0
        frame[:, :, 2] = 0
    elif mode == 2:
        frame[:, :, 0] = 0
        frame[:, :, 1] = 0

    cv2.imshow("Webcam", frame)
    
    counter += 1

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)