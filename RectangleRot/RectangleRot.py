import numpy as np
import cv2
import math
import string

def rotate_about_center(src, angle, scale=1.):
    w = src.shape[1]
    h = src.shape[0]
    rangle = np.deg2rad(angle)  # angle in radians
    # now calculate new image width and height
    nw = (abs(np.sin(rangle)*h) + abs(np.cos(rangle)*w))*scale
    nh = (abs(np.cos(rangle)*h) + abs(np.sin(rangle)*w))*scale
    # ask OpenCV for the rotation matrix
    rot_mat = cv2.getRotationMatrix2D((nw*0.5, nh*0.5), angle, scale)
    # calculate the move from the old center to the new center combined
    # with the rotation
    rot_move = np.dot(rot_mat, np.array([(nw-w)*0.5, (nh-h)*0.5, 0]))
    # the move only affects the translation, so update the translation
    # part of the transform
    rot_mat[0, 2] += rot_move[0]
    rot_mat[1, 2] += rot_move[1]
    return cv2.warpAffine(src, rot_mat, (int(math.ceil(nw)), int(math.ceil(nh))), flags=cv2.INTER_LANCZOS4)

Image = cv2.imread('D:\PythonDevelopment\RectangleRot\Py_Sample\89683.jpg', cv2.IMREAD_UNCHANGED)
Size_X = np.size(Image, 0)
Size_Y = np.size(Image, 1)
T_L = Size_X/3
T_H = Size_X*2/3
X0 = 0  # Row
Y0 = 0  # Clo
X1 = 0
Y1 = 0
while Image[X0, Y0, 1] == 0:
    if X0 == Size_X-1:
        X0 = 0
        Y0 += 1
    X0 += 1
if (T_L < X0)and(X0 < T_H):
    I_Res = Image
else:
    if X0 > (Size_X/2):
        X1 = X0 - 300
    else:
        X1 = X0 + 300
    Y1 = 0
    while Image[X1, Y1, 1] == 0:
        Y1 += 1
    K = float((Y0 - Y1))/float((X0 - X1))
    Theta = -1*math.atan(K)*180/math.pi  # print 'X0=', X0, 'Y0=', Y0, 'X1=', X1, 'Y1=', Y1, 'K=', K, 'Theta=', Theta
    I_Res = rotate_about_center(Image, Theta, 0.88)
# cv2.imwrite('C:\Users\Administrator\Desktop\Test.jpg', I_Res)
cv2.namedWindow('Ori')
cv2.namedWindow('Res')
cv2.imshow('Ori', Image)
cv2.imshow('Res', I_Res)
cv2.waitKey()
cv2.destroyAllWindows()
