# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 08:20:18 2026

@author: Samuel
"""

import cv2

image = cv2.imread("TiMe To LoCk In.jpeg")

biru = image.copy()
biru[:, :, 1] = 0
biru[:, :, 2] = 0

hijau = image.copy()
hijau[:, :, 0] = 0
hijau[:, :, 2] = 0

merah = image.copy()
merah[:, :, 0] = 0
merah[:, :, 1] = 0

cv2.imshow("Biru", biru)
cv2.imshow("Hijau", hijau)
cv2.imshow("Merah", merah)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)