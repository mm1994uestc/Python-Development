import math
import numpy as np
import cv2

cv2.namedWindow('Ori')
Ori = cv2.imread('Ori.png')
cv2.imshow('Ori', Ori)

# You have to get to know how to convert the round QRCode into the Square QRCode
Data = np.zeros((29, 29), dtype=np.uint8)  # Code Structure is 29*29 Square Code
AngleStep = 12.413793103448275862068965517241/180*math.pi
BlockWidth = 9
# Code begin is 45 pixel;Black and white block is 9 pixel;So we can choose 40 pixel to be begin
# 49 58 67 76 85 94 103 112 121 130 139 148 157 166 175 184 193 202 211 220 229 238 247 256 265 274 283 292 301
# 49 57 66 75 84 93 102 110 119 128 137 146 155 164 173 181 190 200 208 217 226 235 244 253 261 271 279 288 296
R = np.array([49, 57, 66, 75, 84, 93, 102, 110, 119, 128, 137, 146, 155, 164, 173, 181, 190, 200, 208, 217,
              226, 235, 244, 253, 261, 271, 279, 288, 296])
for i in range(29):
    Angle = i*AngleStep
    j = 0
    for r in R:
        Y = 300+int(r*math.cos(Angle-AngleStep*14))
        X = 300-int(r*math.sin(Angle-AngleStep*14))
        if Ori[X, Y, 1] < 10:
            Data[i][j] = 0
        else:
            Data[i][j] = 1
        j += 1
print Data
# We take a mask to be 10*10
Mask = np.ones(10, dtype=np.uint8)
Res_QRCode = np.zeros((290, 290), dtype=np.uint8)
for i in range(29):
    for j in range(29):
        if Data[i][j] == 1:
            Res_QRCode[i*10][j*10:j*10+10] = Mask
            Res_QRCode[i*10+1][j*10:j*10+10] = Mask
            Res_QRCode[i*10+2][j*10:j*10+10] = Mask
            Res_QRCode[i*10+3][j*10:j*10+10] = Mask
            Res_QRCode[i*10+4][j*10:j*10+10] = Mask
            Res_QRCode[i*10+5][j*10:j*10+10] = Mask
            Res_QRCode[i*10+6][j*10:j*10+10] = Mask
            Res_QRCode[i*10+7][j*10:j*10+10] = Mask
            Res_QRCode[i*10+8][j*10:j*10+10] = Mask
            Res_QRCode[i*10+9][j*10:j*10+10] = Mask
kernel = np.ones((1, 1), np.uint8)
erosion = cv2.erode(Res_QRCode, kernel, iterations=1)
cv2.namedWindow('QRCode')
cv2.imshow('QRCode', erosion*255)
cv2.imwrite('QRCode.png', erosion*255)
cv2.waitKey()
cv2.destroyAllWindows()
