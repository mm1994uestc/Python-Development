"""
.*. coding:utf-8 .*.
Author: MM1994UESTC
History: 20170329
Edition: 1.0
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import math
import cmath
# img = cv2.imread("D:\PythonDevelopment\Opencv_Test\IMG_0897.jpg", cv2.IMREAD_COLOR)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.namedWindow('image')
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyWindow('image')
# img_50X80 = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# cv2.namedWindow('image')
# cv2.imshow('image', img_50X80)
# cv2.waitKey(0)
# cv2.destroyWindow('image')
# Img_Array = np.array([
#     [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
#     [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
#     [[255, 255, 255], [128, 128, 128], [0, 0, 0]]
#     ], dtype=np.int8)
# cv2.imwrite('CvImag.jpg', Img_Array)
# img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# img_HSV[:, :, 0] = (img_HSV[:, :, 0]+15) % 180
# img_green = cv2.cvtColor(img_HSV, cv2.COLOR_HSV2BGR)
# cv2.namedWindow('image')
# cv2.imshow('image', img_green)
# cv2.waitKey(0)
# cv2.destroyWindow('image')
# img_HSV[:, :, 2] = img_HSV[:, :, 2]*0.5
# img_LowS = cv2.cvtColor(img_HSV, cv2.COLOR_HSV2BGR)
# cv2.namedWindow('image')
# cv2.imshow('image', img_LowS)
# cv2.waitKey(0)
# cv2.destroyWindow('image')
# def Gamma_Trans(img, gamma):
#     gamma_table = [np.power(x/255.0, gamma)*255.0 for x in range(256)]
#     gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)
#     return cv2.LUT(img, gamma_table)
# img_corrected = Gamma_Trans(img, 0.5)
# cv2.namedWindow('image')
# cv2.imshow('image', img_corrected)
# cv2.waitKey(0)
# cv2.destroyWindow('image')
# hist_b = cv2.calcHist([img], [0], None, [256], [0, 256])
# hist_g = cv2.calcHist([img], [1], None, [256], [0, 256])
# hist_r = cv2.calcHist([img], [2], None, [256], [0, 256])
# hist_b_corrected = cv2.calcHist([img_corrected], [0], None, [256], [0, 256])
# hist_g_corrected = cv2.calcHist([img_corrected], [1], None, [256], [0, 256])
# hist_r_corrected = cv2.calcHist([img_corrected], [2], None, [256], [0, 256])
# fig = plt.figure()
# pix_hists = [
#     [hist_b, hist_g, hist_r],
#     [hist_b_corrected, hist_g_corrected, hist_r_corrected]
# ]
# pix_vals = range(256)
# for sub_plt, pix_hist in zip([121, 122], pix_hists):
#     ax = fig.add_subplot(sub_plt, projection='3d')
#     for c, z, channel_hist in zip(['b', 'g', 'r'], [20, 10, 0], pix_hist):
#         cs = [c] * 256
#         ax.bar(pix_vals, channel_hist, zs=z, zdir='y', color=cs, alpha=0.618, edgecolor='none', lw=0)
#     ax.set_xlabel('Pixel Values')
#     ax.set_xlim([0, 256])
#     ax.set_ylabel('Counts')
#     ax.set_zlabel('Channels')
# plt.show()
# cv2.waitKey(0)
# Matrix = np.array(([1.6, 0, -50], [0, 1.6, -100]), dtype=np.float32)
# Theta = np.pi*90/180
# Matrix_Rot = np.array(([np.cos(Theta), -np.cos(Theta), 0],
#                        [np.sin(Theta), np.cos(Theta), 0]),
#                       dtype=np.float32)
# Size_X = np.size(img, 0)
# Size_Y = np.size(img, 1)
# print 'Size_X:', Size_X
# print 'Size_Y:', Size_Y
# img[726, 100, 0] = 1
# img_Warp = cv2.warpAffine(img, Matrix_Rot, (Size_X, Size_Y))
# cv2.namedWindow('image')
# cv2.imshow('image', img_Warp)
# cv2.waitKey(0)
# cv2.destroyWindow('image')


# Mask = np.zeros((720, 720, 3), dtype=np.uint8)+255
# Angle = np.array([
#     [(20, 20), (20, 30), (30, 20)],
#     [(60, 180), (20, 237), (100, 237)]])
# phi = 4 * np.pi / 5
# rotations = [[[np.cos(i * phi), -np.sin(i * phi)], [i * np.sin(phi), np.cos(i * phi)]] for i in range(1, 5)]
# pentagram = np.array([[[[0, -1]] + [np.dot(m, (0, -1)) for m in rotations]]], dtype=np.float)
# pentagram = np.round(pentagram * 80 + np.array([160, 120])).astype(np.int)
# pt_color = [int(c) for c in np.random.randint(0, 255, 3)]
# cv2.line(Mask, (280, 280), (360, 360), (0, 0, 0), 2)
# cv2.circle(Mask, (360, 360), 30, (255, 0, 0), 2)
# cv2.rectangle(Mask, (330, 330), (390, 390), (0, 255, 0), 2)
# cv2.fillPoly(Mask, Angle, (0, 0, 255))
# cv2.polylines(Mask, pentagram, True, (0, 255, 255), 4)
# cv2.putText(Mask, 'MM1994UESTC', (0, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 100, 100), 1)
# cv2.circle(Mask, (100, 100), 20, pt_color, 5)
# cv2.namedWindow('image')
# cv2.imshow('image', Mask)
# cv2.waitKey(0)
# cv2.destroyWindow('image')



# def rotate_about_center(src, angle, scale=1.):
#     w = src.shape[1]
#     h = src.shape[0]
#     rangle = np.deg2rad(angle)  # angle in radians
#     # now calculate new image width and height
#     nw = (abs(np.sin(rangle)*h) + abs(np.cos(rangle)*w))*scale
#     nh = (abs(np.cos(rangle)*h) + abs(np.sin(rangle)*w))*scale
#     # ask OpenCV for the rotation matrix
#     rot_mat = cv2.getRotationMatrix2D((nw*0.5, nh*0.5), angle, scale)
#     # calculate the move from the old center to the new center combined
#     # with the rotation
#     rot_move = np.dot(rot_mat, np.array([(nw-w)*0.5, (nh-h)*0.5, 0]))
#     # the move only affects the translation, so update the translation
#     # part of the transform
#     rot_mat[0, 2] += rot_move[0]
#     rot_mat[1, 2] += rot_move[1]
#     return cv2.warpAffine(src, rot_mat, (int(math.ceil(nw)), int(math.ceil(nh))), flags=cv2.INTER_LANCZOS4)
# Sample_Time = 60
# Num_Frames = 1000
# Out_FPS = 25
# Cap = cv2.VideoCapture('V70308-124409.mp4')
# Pixel_Size = (int(Cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
#              int(Cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
# cv2.namedWindow('image')
# while(Cap.isOpened()):
#    ret, frame = Cap.read()
#    frame = rotate_about_center(frame, 90, 0.8)
#    cv2.imshow('image', frame)
#    K = cv2.waitKey(20)
#    if(K & 0xff == ord('q')):
#        break
# cv2.destroyWindow('image')
# Cap.release()


# I = cv2.imread('timg.jpg')
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)  # You can change the size of windows after it show the picture
# cv2.imshow('image', I)
# Key = cv2.waitKey(0)
# if Key == 27:  # ESC's number is 27
#     cv2.destroyWindow('image')
# elif Key == ord('s'):
#     cv2.imwrite('save.jpg', I)
#     cv2.destroyWindow('image')
# img = cv2.imread('timg.jpg', 0)
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyWindow('image')


# MASK = 255*np.ones((256, 256), dtype=np.uint8)
# cv2.line(MASK, (0, 0), (50, 50), (0, 0, 0), 1)
# cv2.ellipse(MASK, (128, 128), (50, 50), 0, 0, 360, (0, 0, 0), -1)
# cv2.imshow('image', MASK)
# cv2.waitKey(0)
# cv2.destroyWindow('image')


# events = [i for i in dir(cv2) if 'EVENT' in i]
# print events
# def draw_circle(event, x, y, flags, param):
#     if event == cv2.EVENT_RBUTTONDBLCLK:
#         cv2.circle(param, (x, y), 100, (255, 0, 0), -1)
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', draw_circle, img)
# while 1:
#     cv2.imshow('image', img)
#     if cv2.waitKey(0) == 27:
#         break
# cv2.destroyWindow('image')


# img = np.ones((512, 512, 3), np.uint8)
# def nothing(x):
#     pass
# cv2.namedWindow('image')
# cv2.createTrackbar('R', 'image', 0, 255, nothing)
# cv2.createTrackbar('G', 'image', 0, 255, nothing)
# cv2.createTrackbar('B', 'image', 0, 255, nothing)
# switch = '0:0FF\n1:ON'
# cv2.createTrackbar(switch, 'image', 0, 1, nothing)
# while 1:
#     cv2.imshow('image', img)
#     k = cv2.waitKey(1)
#     if k == 27:
#         break
#     r = cv2.getTrackbarPos('R', 'image')
#     g = cv2.getTrackbarPos('G', 'image')
#     b = cv2.getTrackbarPos('B', 'image')
#     s = cv2.getTrackbarPos(switch, 'image')
#
#     if s == 0:
#         img[:] = 0
#     else:
#         img[:] = [b, g, r]
# cv2.destroyWindow('image')


# img = cv2.imread('1.jpg')
# print img.item(10, 10, 2)
# img.itemset((10, 10, 2), 100)
# print img.item(10, 10, 2)
# cv2.imshow('image', img)
# print img.dtype
# print img.size
# cv2.waitKey(0)
# cv2.destroyWindow('image')


# I = cv2.imread('1.jpg')
# Mask = I[100:150, 100:150, :]
# I[50:100, 50:100, :] = Mask
# cv2.imshow('image', I)
# cv2.waitKey(0)
# cv2.destroyWindow('image')

# I = cv2.imread('1.jpg')
# b, g, r = cv2.split(I)
# cv2.imshow('image', g)
# cv2.waitKey(0)
# Res = cv2.merge((b, g, r))
# cv2.imshow('image', Res)
# cv2.waitKey(0)
# cv2.destroyWindow('image')
# x = np.uint8([250])
# y = np.uint8([10])
# print cv2.add(x, y)
# print x + y  # 250 + 10 = 260%256=4


# I = cv2.imread('1.jpg')
# X = np.size(I, 0)
# Y = np.size(I, 1)
# print X, Y
# Res = cv2.imread('Linus.jpg')
# Res = cv2.resize(Res, (Y, X))
# Image = cv2.addWeighted(I, 0.9, Res, 0.1, 10)
# cv2.namedWindow('image')
# cv2.imshow('image', Image)
# cv2.waitKey(0)
# cv2.destroyWindow('image')

# I = cv2.imread('1.jpg')
# print I.shape
# rows, cols, channels = I.shape
# print rows, cols, channels
# print I.size
# roi = I[0:rows, 0:cols]
# cv2.imshow('image', roi)
# cv2.waitKey(0)
# cv2.destroyWindow('image')


# import time
# Count1 = cv2.getTickCount()
# T1 = time.time()
# print 'I LOVE YOU!'
# I = cv2.imread('1.jpg')
# for i in xrange(5, 9, 2):
#     I = cv2.medianBlur(I, i)
# Count2 = cv2.getTickCount()
# T2 = time.time()
# T = (Count2 - Count1)/cv2.getTickFrequency()
# t = T2-T1
# print T, ' ', t  # Unit is 's'
# cv2.namedWindow('image')
# cv2.imshow('image', I)
# cv2.waitKey(0)
# cv2.destroyWindow('image')

Cap = cv2.VideoCapture('BlueCapture.mp4')
while 1:
    ret, frame = Cap.read()
    blue = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l = np.array([100, 50, 50])
    h = np.array([180, 255, 255])
    mask = cv2.inRange(blue, l, h)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
