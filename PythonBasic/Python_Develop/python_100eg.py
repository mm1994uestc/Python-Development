#!/usr/bin/python
# -*- coding: UTF-8 -*-
import string
import math
import time
import sys
import os
#import pygame
#eg1:There are 1, 2, 3, 4 numbers, can be composed of a number of different and no duplication of the three digit number? How much is it?
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if (i != k) and (i != j) and (j != k):
				print("The number is ",i,j,k)
#eg2:Bonuses paid by enterprises in accordance with the profit commission. Total number of 1.5% between 7.5% of the profits (I) less than or equal to 10 million yuan, bonus provided 10%; profit of more than 10 million yuan, less than 20 million yuan, less than 10 million yuan in 10% deduct a percentage from a sum of money, more than 10 million yuan, the Commission; 20 million to 40 million, more than 20 million yuan, to the Commission of 5%; 40 million to 60 million more than 40 million yuan, to the Commission of 3%; 60 million to 100 million, more than 60 million yuan, deduct a percentage from a sum of money, more than 100 million yuan, more than 100 million yuan according to the 1% commission, from the keyboard input month profit I, seeking to be bonuses?
#Solution 1
percent_less10mili = 0.1
percent_less20mili = 0.075
percent_less40mili = 0.05
percent_less60mili = 0.03
percent_less100mili = 0.015
percent_last = 0.01
I=input("Please enter a the profit for this year :")
i=int(I)
if i <= 10:
	Sum = i*percent_less10mili 
elif 10 < i and i <= 20:
	Sum = 1+(i-10)*percent_less20mili 
elif 20 < i and i <= 40:
	Sum = 1+0.75+(i-20)*percent_less40mili 
elif 40 < i and i <= 60:
	Sum = 1+0.75+1+(i-40)*percent_less60mili 
elif 60 < i and i <= 100:
	Sum = 1+0.75+1+0.6+(i-60)*percent_less100mili 
elif 100 < i:
	Sum = 1+0.75+1+0.6+0.6+(i-100)*percent_last
else :
	print("Your have enter a wrong number!")
print("The profit of this year for MaMiao",Sum)
#Solution 2
i = int(input("The profit:"))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print((i-arr[idx])*rat[idx])
        i=arr[idx]
print(r)
#eg3:An integer, which adds 100 and plus 268 is a perfect square, what is the number?
#Solution 1
n=0
m=0
for K_f in range(1,12):#This algorithm has a simple mathematical pretreatment and analysis, to a certain extent, the time complexity of the algorithm is simplified.
	K_s = 168/K_f
	if (K_s == int(K_s)):
		m=(K_s+K_f)/2
		n=(K_s-K_f)/2
	if n == int(n) and m == int(m) and n!=0 and m!=0:
		print(m,n)
		print(m*m-268)
#Solution 2
for i in range(10000):
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if(x * x == i + 100) and (y * y == i + 268):
        print(i)
#eg4:Enter a certain day, judgment day is the first few days this year?
year = int(input("Please enter the year:"))
month = int(input("Please enter the month:"))
day = int(input("Please enter the day:"))
sum = 0
month_day=(31,28,31,30,31,30,31,31,30,31,30,31)
if (year%4==0 and year%100!=0) or year%400==0 :
	day_plus = 1
	print("This year is a leap year!")
else :
	day_plus = 0
	print("This year is not a leap year!") 
if 2 < month :
	sum += day_plus 
for i in range(0,month-1):
	sum += month_day[i]
sum += day
print("The sum of today is equal to:",sum)
#eg5:Enter three integers x, y, z, please put the three number of small to large output.
#Solution 1
def compare(A,B):
	if A>B:
		result = A
	else:
		result = B
	return result
NUM1=int(input("Please enter the first number:"))
NUM2=int(input("Please enter the second number:"))
NUM3=int(input("Please enter the third number:"))
Big1=compare(NUM1,NUM2)
Big2=compare(Big1,NUM3)#caculate the biggest one
if NUM1 == Big2:
	NUM1=0
if NUM2 == Big2:
	NUM2=0
if NUM3 == Big2:
	NUM3=0
middle1=compare(NUM1,NUM2)
middle2=compare(middle1,NUM3)#caculate the second biggest one
if NUM1 == middle2:
	NUM1=0
if NUM2 == middle2:
	NUM2=0
if NUM3 == middle2:
	NUM3=0
small1=compare(NUM1,NUM2)
small2=compare(small1,NUM3)#caculate the second biggest one
print(small2,middle2,Big2)
#Solution 2
l = []
for i in range(3):
    x = int(input("Please enter the first number:"))
    l.append(x)
l.sort()
print(l)
#eg6:Fibonacci sequence
#Solution 1
F = [0,1,1]
print(F[0])
print(F[1])
for i in range(1,10):
	F[0]=F[1]
	F[1]=F[2]
	F[2]=F[0]+F[1]
	print(F[2])
#Solution 2
def fib(n):
	if n==1 or n==2:
		return 1
	return fib(n-1)+fib(n-2)
print(fib(10))
#Copy a list of data into another list.
#Solution 1
a = [1, 2, 3]
b = a[:]
print(b)
#Solution 2
c=[0,0,0]
for i in range(0,3):
	c[i]=a[i]
print(c)
#eg8:The output of 9*9 multiplication table
for i in range(1,10):
	for j in range(1,10):
		print(i,"*",j,"=",i*j)
#eg9:Pause one second output
#It need to import the headfiles named time like this:import time
myD = {1: 'a', 2: 'b'}
for key,value in dict.items(myD):
	print(key, value)
	print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
	time.sleep(1)
	print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
#To determine how many prime numbers between 101-200, and the output of all prime numbers
h = 0
leap = 1
from math import sqrt
from sys import stdout
for m in range(101,201):
    k = int(sqrt(m + 1))
    for i in range(2,k + 1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print('%-4d' % m)
        h += 1
        if h % 10 == 0:
            print('')
    leap = 1
print('The total is %d' % h)
#eg10:Print out all the "daffodils", the so-called "daffodils" is a three digit number. The all digital cube and equal to the number itself. For example: 153 is a "daffodils", because 153=1^3+5^3+3^3
for i in range(100,1000):
	sum = math.pow(int(i/100),3)+ math.pow(int((i%100)/10),3)+ math.pow(i%10,3)
	if sum==i:
		print("This number is a daffodils number equal to:",i)
#eg11:A positive integer factorization. For example: enter 90, print out 90=2*3*3*5
n = int(input("input number:\n"))
print("n = %d" % n)
for i in range(2,n + 1):
    while n != i:
        if n % i == 0:#All the number,which is not a prime number can't appear at there,because that the number(not prime number) have ever been diverse to be the premi number ,for Example:10 have already been diverse to be 2 multiple 5
            print(str(i))
            print("*")
            n = n / i
        else:
            break
print("%d"% n)
#eg11:Use the conditional operator to complete this problem: the study results >=90 points of the students with A, 60-89 points between the use of B, said the following 60 points with C
Score = int(input("Please enter the score:"))#Python haven't the loop function for three member like this : A = expression ? "Q" : "P"
if Score < 60:
	print("Your Grade is equal to C")
elif 60<= Score < 90:
	print("Your Grade is equal to B")
else :
	print("Your Grade is equal to A")
#eg12:Enter a line of characters, respectively, the statistics of the English letters, spaces, numbers and other characters of the number
write = "Come on,Baby!"
write = write.encode()
fo = open("eg_test.txt",'wb',1000)
print("The filename is :",fo.name)
print("The Rquest_Model of files :",fo.mode)
print("This is the sentence which I have already written into the file named ",fo.name,write)
fo.write(write)
fo.close() 
fo = open("eg_test.txt","rb",1)
Str = fo.read(15)
Str = Str.decode()#You have to decode the string to count how many times the letter "C" have appear in the str! 
print("The string i have already read from txt file is :",Str)
C = Str.count('C')
Where = Str.find("Ba")
print("The latter C have appear for ",C,"times!")
print("The string om have appear at the address:",Where)
fo.close()
letters = 0
space = 0
digit = 0
others = 0
for c in Str:
    if c.isalpha():#remember the function to find alpha
        letters += 1
    elif c.isspace():#rememeber the function to find the space
        space += 1
    elif c.isdigit():#remember the function to find the digit
        digit += 1
    else:
        others += 1
print('char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others))#���
#eg13:Detect keyboard to control the size of the key
print("Please enter the keyboard values,this example is used to detect the values of top bottom right and left values of keyboard!")
top = input("Please enter the top key in keyboard!")
#bottom = input("Please enter the bottom key in keyboard!")
#left = input("Please enter the left key in keyboard!")
#right = input("Please enter the right key in keyboard!")
#print("The top values is equal to ",top,int(top))#It's okey when run in the txt type of files!!
#print("The bottom values is equal to ",bottom,int(bottom))
#print("The left values is equal to ",left,int(left))
#print("The right values is equal to ",right,int(right))
#eg14:Find the value of s=a+aa+aaa+aaaa+aa... A, where a is a number. For example, 2+22+222+2222+22222 (at this time a total of 5 numbers add), a few numbers add a keyboard control
K = int(input("Please enter a Number to calculate:"))
N = int(input("Please enter a Number to define how many time you want to calculate:"))
#for i in range(1,10):#��Χ��1��10-1=9����ס�ˣ�����
#	print(i)
#for i in range(10):#��Χ��0��9֮�䣬��ס�ˣ�����
#	print(i)
sum = 0#����ʼ��һ��Ҫ��������������
for i in range(1,N+1):
	temp = i*math.pow(10,N-i)
	sum += temp
	print("The precudure is :",temp,"+")
print(sum)
print("The result is calculate to be :",sum*K)
#eg15��If a number is exactly equal to the sum of its factors, this number is called "end of a few". For example 6=123. programming to find all completed within 1000
i=1
while (i<=1000):
	Buffer = i
	for j in range(1,i):
		if (i%j==0):
			Buffer -= j
	if (Buffer==0):
		print("This number is a complete number equal to:",i)
	i += 1
#eg16:A ball dropped from a height of 100 m free. Each fall to the ground after jump back to the original height of half; to fall for it on the 10th floor, the total number of meters after? How high is the tenth bounce?
Heigth = int(input("Please enter a Number for Heigth:"))
sum = Heigth
Times = int(input("Please enter a Number for calculate times:"))
print("The Heigth of 10th bounce is equal to :",math.pow(0.5,Times)*Heigth)
for i in range(1,Times):
	sum +=  2*Heigth*math.pow(0.5,i)
print("The total length is equal to:",sum)
#eg17:Two table tennis team for the game, each out of the three. A team for the A, B, C three, B team for the X, y, Z three. Draw a draw. Someone asked the team about the competition. A said he did not x than, C said he does not and Z, X than, please make up the program to find out the list of three teams race
for i in range(ord('x'),ord('z') + 1):
    for j in range(ord('x'),ord('z') + 1):
        if i != j:
            for k in range(ord('x'),ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print('order is a -- %s\t b -- %s\tc--%s' % (chr(i),chr(j),chr(k)))
#������Ŀ�к�ǿ�ĳ����ԣ�һ��Ҫע�����ķ���
#eg8:Print out the following pattern (diamond)
print("   *")
print("  ***")
print(" *****")
print("*******")
print(" *****")
print("  ***")
print("   *")
#eg19:There is a sequence of points: 2/1, 3/2, 5/3, 8/5, 13/8, 21/13, and the sum of the first 20 items of this series.
#������Ŀ�Ļ������ɣ�
#���ӣ�2+3=5 3+5=8 5+8=13 8+13=21
#��ĸ��1+2=3 2+3=5 3+5=8 5+8=13
Top_num1=2
Bot_num1=1
Top_num2=3
Bot_num2=2
sum=7/2
for i in range(18):
	#Num = (Top_num1+Top_num2)/(Bot_num1+Bot_num2)
	print("The number is :",Top_num1,Bot_num1)
	Temp1=Top_num1#�м��������������ݸ��¼����ע�Ⱑ����
	Temp2=Bot_num1
	Top_num1 = Top_num2
	Bot_num1 = Bot_num2
	Top_num2 = (Temp1+Top_num2)
	Bot_num2 = (Temp2+Bot_num2)
	sum += Top_num2/Bot_num2
print(sum)
#eg20:Use recursive method for 5!
def recursive(N):
	result = N
	if (N==1):
		return 1
	else :
		result *= recursive(N-1)
	return result
result = recursive(5)
print(result)
#eg21:By using the recursive function call, the input of the 5 characters, in order to print out the opposite order
#Solution 1:
FIFO=['A','B','C','D','E']
print("Please enter five letter for FIFO!")
for i in range(5):
	FIFO[i] = input("Please enter the letter:")
print(FIFO[0],FIFO[1],FIFO[2],FIFO[3],FIFO[4])
print(FIFO[4],FIFO[3],FIFO[2],FIFO[1],FIFO[0])
print(FIFO[4]+FIFO[3]+FIFO[2]+FIFO[1]+FIFO[0])
#Solution 2(���õݹ��㷨):
def output(s,l):
    if l==0:
       return
    print(s[l-1])
    output(s,l-1)
s = FIFO[4]+FIFO[3]+FIFO[2]+FIFO[1]+FIFO[0]	
l = len(s)
output(s,l)
#eg22:A 5 digit number, it is not a palindrome judgment. That 12321 is a palindrome, a bit and bit the same ten million, with thousands of the same

#del Num
Num = 12321
print("The number for test is :",Num)
if (int(Num/10000)==Num%10) and (int(Num/1000)%10==int((Num%100)/10)):
	print("This is a palindrome number!")
#eg23:Please enter the first letter of the week to determine what is a week, if the first letter, then continue to determine the second letters
days = ['Monday','Thuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
print("Please enter the first letter to determine the day in week:")
Ch1=input("Please enter the first letter:")
if Ch1=='M':
	print("Today is Monday!")
elif Ch1=='W':
	print("Today is Wednsday!")
elif Ch1=='F':
	print("Today is Friday!")
elif Ch1=='T':
	print("Please enter the second letter for determined!")
	Ch2=input()
	if Ch2=='h':
		print("Today is Thuesday!")
	else :
		print("Today is Tursday!")
else:
	print("Please enter the second letter for detemined!")
	Ch2=input()
	if Ch2=='a':
		print("Today is Saturday!")
	else :
		print("Today is Sunday!")
#eg24:Comma separated list�����ŷָ��б�
L = [1,2,3,4,5]
s1 = ','.join(str(n) for n in L)
print(s1)
#eg25:�ı���ɫ����--ʾ��35
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(bcolors.WARNING + "Warning mesg color?" + bcolors.ENDC)
#show the triangle of yanghui!
if __name__ == '__main__':
    a = []
    for i in range(10):
        a.append([])
        for j in range(10):
            a[i].append(0)
    for i in range(10):
        a[i][0] = 1
        a[i][i] = 1
    for i in range(2,10):
        for j in range(1,i):
            a[i][j] = a[i - 1][j-1] + a[i - 1][j]
    from sys import stdout
    for i in range(10):
        for j in range(i + 1):
            stdout.write(str(a[i][j]))
            stdout.write(' ')
        print
#To deal the list in different ways!
import _string
import math
import copy#to include this header files to use the function copy!
A = [1,2,3,4,5]
B = list(A)
#Here we use a mothed to make new list the same as A
# while if we use B=A,that will make the B and A point to the same class,they have the same Adress
# so,if we change one of them the other one will be changed together!!
m = 3
n = len(A)
print(n)
print(A)
for i in range(n):
        if i < m:
                B[i] = A[n-m+i]
        else:
                B[i] = A[i-m]
print(A)
print(B)
C = copy.deepcopy(A)
C[3] = 100
print(A)
print(C)
#The game to judge what the last people of game by the rules:people one by one with the third one delet
people = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]#40 people
F=len(people)
Count = 0
peo = 0
while F!=1:
	if Count%3!=0:
		if people[peo] != 0:
			Count += 1
		peo += 1
		if peo == F:
			peo = 0
	else:
		Count = 0
		people[peo-1] = 0
		F -= 1
#Solution2:
if __name__ == '__main__':
    nmax = 50
    n = int(input('请输入总人数:'))
    num = []
    for i in range(n):
        num.append(i + 1)

    i = 0
    k = 0
    m = 0

    while m < n - 1:
        if num[i] != 0 : k += 1
        if k == 3:
            num[i] = 0
            k = 0
            m += 1
        i += 1
        if i == n : i = 0

    i = 0
    while num[i] == 0: i += 1
    print(num[i])
#Function for caculate the length of String!
def My_StrLen(Ori):
        Res = 0
        while Ori[Res]!='k':
                Res += 1
        return Res
StrLen_Ori = input("Please enter a string to caculate:")
StrLen_Res = My_StrLen(StrLen_Ori)
print(StrLen_Res)
#caculate the sum of number
N = int(input("Please enter a number for caculate:"))
def Even(N):
        sum = 0
        for i in range(2,N+2,2):
                sum += 1/i
        return sum
def Odd(N):
        sum = 0
        for i in range(1,N+2,2):
                sum += 1/i
        return sum
if N%2 == 0:
        Car = Even(N)
else:
        Car = Odd(N)
print(Car)
#81-eg




































