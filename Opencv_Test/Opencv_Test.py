import numpy as np
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import math
import cmath

img = cv2.imread("D:\PythonDevelopment\Opencv_Test\IMG_0897.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('Window_0')
cv2.imshow('Window_0', img)

img_50X80 = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
#cv2.namedWindow('Window_1')
#cv2.imshow('Window_1', img_50X80)

Img_Array = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
    [[255, 255, 255], [128, 128, 128], [0, 0, 0]]
    ], dtype=np.int8)
cv2.imwrite('CvImag.jpg', Img_Array)

img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_HSV[:, :, 0] = (img_HSV[:, :, 0]+15) % 180
img_green = cv2.cvtColor(img_HSV, cv2.COLOR_HSV2BGR)
#cv2.namedWindow('Window2')
#cv2.imshow('Window2', img_green)

img_HSV[:, :, 2] = img_HSV[:, :, 2]*0.5
img_LowS = cv2.cvtColor(img_HSV, cv2.COLOR_HSV2BGR)
#cv2.namedWindow('Window3')
#cv2.imshow('Window3', img_LowS)

def Gamma_Trans(img, gamma):
    gamma_table = [np.power(x/255.0, gamma)*255.0 for x in range(256)]
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)
    return cv2.LUT(img, gamma_table)

img_corrected = Gamma_Trans(img, 0.5)
#cv2.namedWindow('Window4')
#cv2.imshow('Window4', img_corrected)

hist_b = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([img], [1], None, [256], [0, 256])
hist_r = cv2.calcHist([img], [2], None, [256], [0, 256])
hist_b_corrected = cv2.calcHist([img_corrected], [0], None, [256], [0, 256])
hist_g_corrected = cv2.calcHist([img_corrected], [1], None, [256], [0, 256])
hist_r_corrected = cv2.calcHist([img_corrected], [2], None, [256], [0, 256])
fig = plt.figure()
pix_hists = [
    [hist_b, hist_g, hist_r],
    [hist_b_corrected, hist_g_corrected, hist_r_corrected]
]
pix_vals = range(256)
for sub_plt, pix_hist in zip([121, 122], pix_hists):
    ax = fig.add_subplot(sub_plt, projection='3d')
    for c, z, channel_hist in zip(['b', 'g', 'r'], [20, 10, 0], pix_hist):
        cs = [c] * 256
        ax.bar(pix_vals, channel_hist, zs=z, zdir='y', color=cs, alpha=0.618, edgecolor='none', lw=0)

    ax.set_xlabel('Pixel Values')
    ax.set_xlim([0, 256])
    ax.set_ylabel('Counts')
    ax.set_zlabel('Channels')
#plt.show()

Matrix = np.array(([1.6, 0, -50], [0, 1.6, -100]), dtype=np.float32)
Theta = np.pi*90/180
Matrix_Rot = np.array(([np.cos(Theta), -np.cos(Theta), 0],
                       [np.sin(Theta), np.cos(Theta), 0]),
                      dtype=np.float32)

Size_X = np.size(img, 0)
Size_Y = np.size(img, 1)
print 'Size_X:', Size_X
print 'Size_Y:', Size_Y

img[726, 100, 0] = 1
img_Warp = cv2.warpAffine(img, Matrix_Rot, (Size_X, Size_Y))

#cv2.namedWindow('Window5')
#cv2.imshow('Window5', img_Warp)

Mask = np.zeros((720, 720, 3), dtype=np.uint8)+255
Angle = np.array([
    [(20, 20), (20, 30), (30, 20)],
    [(60, 180), (20, 237), (100, 237)]])
phi = 4 * np.pi / 5
rotations = [[[np.cos(i * phi), -np.sin(i * phi)], [i * np.sin(phi), np.cos(i * phi)]] for i in range(1, 5)]
pentagram = np.array([[[[0, -1]] + [np.dot(m, (0, -1)) for m in rotations]]], dtype=np.float)
pentagram = np.round(pentagram * 80 + np.array([160, 120])).astype(np.int)
pt_color = [int(c) for c in np.random.randint(0, 255, 3)]
cv2.line(Mask, (280, 280), (360, 360), (0, 0, 0), 2)
cv2.circle(Mask, (360, 360), 30, (255, 0, 0), 2)
cv2.rectangle(Mask, (330, 330), (390, 390), (0, 255, 0), 2)
cv2.fillPoly(Mask, Angle, (0, 0, 255))
cv2.polylines(Mask, pentagram, True, (0, 255, 255), 4)
cv2.putText(Mask, 'MM1994UESTC', (0, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 100, 100), 1)
cv2.circle(Mask, (100, 100), 20, pt_color, 5)
cv2.namedWindow('Window6')
cv2.imshow('Window6', Mask)

cv2.waitKey()
cv2.destroyAllWindows()

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
Sample_Time = 60
Num_Frames = 1000
Out_FPS = 25
Cap = cv2.VideoCapture('V70308-124409.mp4')
Pixel_Size = (int(Cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
              int(Cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
cv2.namedWindow('Windows')
while(Cap.isOpened()):
    ret, frame = Cap.read()
    frame = rotate_about_center(frame, 90, 0.8)
    cv2.imshow('Windows', frame)
    K = cv2.waitKey(20)
    if(K & 0xff == ord('q')):
        break
cv2.destroyWindow('Windows')
Cap.release()
