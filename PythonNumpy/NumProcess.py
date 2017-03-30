from numpy import *
#Create a arrays with array() func in Numpy
a = array([[1., 2., 3.], [4., 5., 6.]])
print 'The shape of array a:',a.shape
print 'array([1,2,3],[4,5,6])=',a
#Create a one-demonsional sequences with arange() func in Numpy
b = arange(0,11)
print 'arange(0,11)=',b
c = arange(0.,2.,0.4)
print 'arange(0.,2.,0.4)=',c
d = arange(0.,2.1,0.3)
print 'arange(0.,2.1,0.3)=',d
#Create a one-demonsional sequences with linspace() func im Numpy
e = linspace(0.,3.5,8)
print 'linspace(0.,3.5,8)=',e
#Create a zero array with zeros() func in Numpy
f = zeros((2,4))
print 'zeros((2,4))=',f
#Create a one array with ones() func in Numpy
g = ones((3,3,3))
print 'ones(3,3,3)=',f
#Create two-demonsional arrays with meshgrid
x = arange(0.,5.1)
y = arange(0.,3.1)
(X,Y) = meshgrid(x,y)
print 'meshgrid(x,y)\'s X=',X
print 'meshgrid(x,y)\'s Y=',Y
#To set the array's data types with setting param:dtype = float64 or complex128
h = array([1,2],dtype=float64)
print 'array([1,2],dtype=float64)=',h
#To change the type of array with astype('type') func in Numpy
i = h.astype('float32')
print 'h.astype(\'float32\')\'s type is:',i.dtype
print 'Use Array.dtype to show the type of array,Eg:Type of h is',h.dtype
#How can i get one element in the N demonsional array
j = a[0,0]
print 'a[0,0]=',j
j = a[-1,0]
print 'a[-1,0]=',j
a[0,0] = j
print 'a[0,0]=j',a[0,0]
#Slicing
k = zeros([3,3],dtype='float32')
print 'K is :',k
Row = k.shape[0]
print 'Row is:',Row
Clo = k.shape[1]
print 'Clo is:',Clo
for i in range(Row):
	for j in range(Clo):
		if(i==j):
			k[i][j]=3
		else :
			k[i][j]=0
print 'k[:,0]=',k[:,0]
print 'k[:,1]=',k[:,1]
print 'k[:,2]=',k[:,2]
k = arange(0,10)
print 'k=arange(10)=',k
print 'a[0:10:2]=',a[0:10:2]
print 'a[-1:0:-1]=',a[-1:0:-1]
print 'a[-1::-1]=',a[-1::-1]
#Views And Copies
a = array(([2.1,3.4,6.4],[4.1,25,8.1],[1.02,5.4,6.1]),dtype='float64')
print 'a is:',a
b = a[:,1:2]
print 'b=a[:,1:2]:',b
a[0,1] = 14.5
print 'After a[0,1]=14.5,b=',b
print 'What we did above is to show that the link between a and b whilch the copy'
print 'if you really need to make a new array out of a slice of the original array,use "+" prefix causes this tp happen'
c = +a[1:3]
print 'c=+a[1:3] is:',c
a[1] = 42
print 'After change a[1]=42,The result of c is:',c
#Reshaping arrays
a = array(([1,2],[3,4]),'float64')
print 'The original array a is:',a
print 'The result of a.reshape(4) is:',a.reshape(4)
print 'The result of a.reshape(1,4) is:',a.reshape(1,4)
print 'The result of a.reshape(4,1) is:',a.reshape(4,1)
print 'The result of a.reshape(2,2,1) is:',a.reshape(2,2,1)
print 'You need to remember that the reshape() func don\'t create a new array,just the copy of original array!'
#Array looping
a = arange(12).reshape(4,3)
print 'a=arange(12).reshape(4,3)',a
for x in a:
	print 'the every line of a is:',x
for x in a:
	for y in x:
		print 'The every element of matrix a is:',y
#Array Expressions And Assigments(Importanr!!!!!)
A = array([[1,2],[3,4]])
B = array([[5,6],[7,8]])
C = A + B
D = A * B
E = A*B + C
F = C + A*B
print 'A is:',A
print 'B is:',B
print 'C = A + B:',C
print 'D=A*B:',D
print 'E=A*B + C:',E
print 'F=C+A*B:',F
#Broadcasting
a = array(([1,2],[3,4]))
print 'a=array([[1,2],[3,4]])\'s shape:',a.shape
b = array([[5,10]])
print 'b=array([[5,10]])\'s shape:',b.shape
c = array([[5],[10]])
print 'c=array([[5],[10]])\'s shape:',c
print 'a+b=',a+b
print 'b+c=',b+c#double broadcastign
#Array methods
a = arange(0.,9.5)
print 'a=arange(0.,9.5):',a
print 'a.tolist()=',a.tolist()
b = a.reshape(2,5)
print 'a.reshape(2,5).tolist()=',b
b.tofile('/home/ubuntu-mm/Python/NumProcess/b_Matrix.txt',' ','%f')
print 'b.fill(10)=',b.fill(10)
print 'transpose() is the method transposes arrays of two and higher demensions'
a = array([[1,2],[3,4]])
print 'a=array([[1,2],[3,4]]):',a
print 'a.transpose()=',a.transpose()
print 'The important func sort() is to sort the array!'
a.sort()
print 'a=array(([1,2],[3,4])) transform by sort() is:',a
a = array([3,7,4,8,2,15])
print 'a=array([3,7,4,8,2,15])',a
a.sort()
print 'a transform by sort() is:',a
#Mathematical metheds
a = array([[1,2],[3,4]])
print 'a=array([[1,2],[3,4]]):',a
print 'a.max()=',a.max()
print 'a.max(0)=',a.max(0)
print 'a.min()=',a.min()
b = a.clip(min=1,max=3)
print 'b=a.clip(min=1,max=3):',b
print 'c=a.conj():',a.conj()#return a array with all the elements(complex) conjugated.
print 'a.sum()=',a.sum()
print 'a.sum(axis=0)=',a.sum(axis=0)
print 'a.sum(axis=1)=',a.sum(axis=1)
print 'a.mean()=',a.mean()
print 'a.mean(axis=0)=',a.mean(axis=0)
print 'a.mean(axis=1)=',a.mean(axis=1)
print 'a.var()=',a.var()
print 'a.var(axis=0)=',a.var(axis=0)
print 'a.var(axis=1)=',a.var(axis=1)
print 'a.std()=',a.std()#To calculate the standard deviation.
print 'a.cumsum()=',a.cumsum()#reshape the array to be one dimension and perform a cumulative sum along that dimension.
#Array functions
a = log2(arange(1.0,50.,0.1))
print 'a=log2(arange(1.0,50.,0.1))'
(num,bins) =  histogram(a,bins=10,range=(0,6))
print '(num,bin)=histogram(a,,bins=10,range=(0,6)) excuting the command!'
print 'The return param bins is ',bins
print 'The return param num is ',num
x = linspace(0,10,100)
y = x*x/10
(num, xedge, yedge) = histogram2d(x,y)
print num,xedge,yedge
#..............................................................#
#  Important functions1:correlation(x,y,mode='valid')
#  Important functions2:convolve(x,y,mode='full')
#..............................................................#
x = array((0.1,1.2,1.0,2.6,0.5,0.8,1.9),'float64')
y = array((0.1,0.4,0.8,1.0,0.7,0.5,0.2),'float64')
print 'x=',x
print 'y=',y
#Cor = correlation(x,y)
Con = convolve(x,y,mode='full')
print 'The result Con=convolve(x,y,mode=\'full\')=',Con
#Matrixes
#..............................................................#
#  Important module to create a new matrix with matrix()
#  This command is truelly create a Matrix not a tuple!
#..............................................................#
a = matrix([[1,3,-5],[3,4,2],[-5,2,0]])
print 'a=matrix([[1,3,-5],[3,4,2],[-5,2,0]]) is:',a
b=matrix([[1],[5],[3]])
print 'b=matrix([[1],[5],[3]])',b
c = a*b
print 'c=a*b is:',c
d = a.T
print 'd=a.T:',d#To change the axis of matrix a like this:a^T
print 'a.H=',a.H#Produce the conjugate transpose.
print 'a.I=',a.I#To calculate the inverse of the Matrix a
print 'a*a.I',a*a.I
print 'linalg.det(a)=',linalg.det(a)#To calculate The determinants of the matrix
d = linalg.solve(a,b)#b respect the result of the linear equations!a respect the coffecient of the equations!
print 'd=linalg.solve(a,b):',d
print 'a*d=',a*d
#...............................................................#
#  To find the eigenvalues and eigenvectors
#  Functions:linalg.eig(a)
#...............................................................#
e = linalg.eig(a)
print 'e[0]=',e[0]
print 'e[1]=',e[1]
u = e[1]
u_i = u.I
Lambda = matrix(diag(e[0]))
print 'The diag Matrix of eigenvalues:',Lambda
Res = u*Lambda*u_i
print 'Res=u*Lambda*u_i:',Res
#Endianness
a = arange(0,5)
a.byteswap()
import sys
print 'The Endianness is:',sys.byteorder
