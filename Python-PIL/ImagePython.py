import Image as Im
import ImageFilter as ImFilter
import ImageChops as ImChops
import ImageFont as ImFont
import ImageDraw as ImDraw
import math
import sys
import os

print 'This File is for you to Transform the Original Pic into another Form!'
im = Im.open('/home/ubuntu-mm/Python/ImageProcess/ImageData/IEEEXtreme.png') #Read the Image
w, h = im.size
def RGB2Gray(image):
	w, h = image.size
	print 'The Wide is :',w
	print 'The Length is :',h
RGB2Gray(im)
def ImRoll(image, Theta):
	"Roll a image sideways"
	w, h = image.size
	Theta = Theta % w
	if Theta == 0:
		return image
	Part1 = image.crop((0, 0, Theta, h))
	Part2 = image.crop((Theta, 0, w, h))
	image.paste(Part2, (0, 0, w-Theta, h))
	image.paste(Part1, (w-Theta, 0, w, h))
	return image
Param = 0.5
NewSize = ((int)(w*Param), (int)(h*Param))  #Notice the size must be a integer!
Scaler = Im.ANTIALIAS
im_roll = ImRoll(im, 90)  #roll the pic
im_resize = im.resize(NewSize, Scaler)  #resize the pic to be 25% Origin'area
im_rotate = im.rotate(45)  #rotate the pic for degree at 45
print 'Now,The geomgraphic transform!@ImRoll() @resize() @rotate()'
#im.show()  #show():To output the Picture to the windows
#im_roll.show()
#im_resize.show()
#im_rotate.show()
print 'Now,The Filter Transform!@filter()'
im_filter = im.filter(ImFilter.DETAIL)  #filter is to change the values of pixel
#im_filter.show()
im_new = Im.new('L', (100,100), [0,255])
#im_new.show()
im2 = Im.open('/home/ubuntu-mm/Python/ImageProcess/ImageData/GitHub.png')
im3 = im2.rotate(45) #Rotate the im2 with the degree at 45
im_blend = Im.blend(im2, im3, 0.2)  #The im and im1 must be the same size(im_blend=im2*0.2+im3*(1-0.2))
#im_blend.show()
mask = Im.new('L', im2.size, [0,255])
im4 = Im.composite(im2, im3 ,mask) #Composite two pic into one and filter with the mask windows.
#im4.show()
def ImageTransform(In):
	Res = pow(In,2)/255
	return Res
print 'Attributes of the Image object!'
print im2.format,im2.mode,im2.size,im2.palette,im2.info
im4.save('/home/ubuntu-mm/Python/ImageProcess/ImageData/login.png','png')
im6 = im2.convert("L") #Change the pic into different Mode:@"L"@"l"@"RGB"@"CMYK"
#im6.show()
im7 = im2.copy() #Copy the image file to a new buffer
im8 = im2.crop((0,0,80,80))
#im8.show()
Bands = im2.getbands() #Get The bands of the Pic
print Bands
for i in Bands:
	print i
Extreme = im2.getextrema() #Get Max_values and Min_values of pic(GrayScale) 
for i in Extreme:
	print i
PixelValues = im2.getpixel((0,0)) #Get to values of the coordinate you input(0,0) 
print 'The pixelValues of point(0,0) is:',PixelValues
w, h = im2.size #Get the size of the pic
mask = Im.new('L',(w,h),[0,255]) #To create a new mask
list1 = im2.convert("L").histogram(mask) #To show the histogram with the statical number of the GrayScale Values where the mask is nonzero replect
print list1
im9 = ImChops.offset(im2 , -10, -10) #To move the pic with the offset produce a new pic
#im9.show()
im10 = im2.point(ImageTransform) #To transform every Pixel's values with func ImageTranform which defined before
#im10.show() #show out the image
im2.putpixel((10,10),(0,0,0)) #Location:(10,10) pixel's color value into (0,0,0)
im2.show()
im11 = im2.resize((80,80))  #To resize The picture into newsize (80,80)
#im11.show()
R,G,B = im11.split()  #To split the im11's three channel in to RGB linear bands
print R
im12 = im2.copy()
im12.thumbnail((80,60)) #To resize the Pic as the rate->Height:Width
#For eg:im.size()=(400,150) It's after im.thumbnail((40,40)) will be (40,15)
#im12.show()
Method = Im.ROTATE_90 #@Im.FLIP_RIGHT_LEFT@Im.FLIP_TOP_BOTTOM@Im.ROTATE_90@Im.ROTATE_180
im13 = im2.copy()
im13.transpose(Method) #To transform the pic as the Method show
#im13.show()
print 'Now,Let draw what we want!'
Cavon1 = Im.new('RGB',(300,300),(255,255,255))
draw = ImDraw.Draw(Cavon1)
draw.arc((0,0,202,202), 0, 135, (0,255,0))
draw.arc((0,0,205,205), 0, 135, (255,0,0))
draw.arc((0,0,208,208), 0, 135, (0,0,255))
draw.arc((0,0,211,211), 0, 135, (255,255,0))
draw.arc((0,0,212,212), 0, 135, (255,0,255))
#Cavon2 = Im.new('RGB',(200,300),(255,255,255))
draw.ellipse((0,0,30,40),(0,255,0))
draw.ellipse((20,20,40,30),(255,125,30))
draw.line(((60,60),(90,60),(90,90),(60,90),(60,60)),(255,0,0))
draw.point((100,100),(255,0,255))
draw.polygon([(60,60),(90,60),(90,90),(60,90)],fill="red",outline="green")
#fontPath = "/usr/share/fonts/dejavu-lgc/DejaVuLGCSansCondensed-Bold.ttf"
#sans16 = ImFont.truetype(fontPath,16)
draw.text((130,80),"Hello PIL!",fill="red")
Cavon1.show()
print 'Image Filter!'
im_filter1 = im2.filter(ImFilter.BLUR)
im_filter2 = im2.filter(ImFilter.CONTOUR)
im_filter3 = im2.filter(ImFilter.DETAIL)
im_filter4 = im2.filter(ImFilter.EDGE_ENHANCE)
im_filter5 = im2.filter(ImFilter.EDGE_ENHANCE_MORE)
im_filter6 = im2.filter(ImFilter.FIND_EDGES)
im_filter7 = im2.filter(ImFilter.SMOOTH)
im_filter8 = im2.filter(ImFilter.SHARPEN)
im_filter1.show()
im_filter2.show()
im_filter3.show()
im_filter4.show()
im_filter5.show()
im_filter6.show()
im_filter7.show()
im_filter8.show()
