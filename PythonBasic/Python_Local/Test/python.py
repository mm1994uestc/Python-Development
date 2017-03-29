import math;
import string;
import os;
import re;
import sys;
import time;
print('Hello Python!')
A = [1, 1, 3, 6]#创建一个元组
B = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
class Employee:
        'This is a class type for Employee!'
        def __init__(self, a, b, c, erro):
                self.P = a
                self.I = b
                self.D = c
                self.erro = erro
                return
        def Output_fun(self):
                K = self.P*self.erro+self.I*self.erro**self.erro+self.D*abs(self.erro);
                print('The Output Number of System is equal to :',K)
                return K
Emp1 = Employee(10, 0.2, 0.5, 0.06)
Output = Emp1.Output_fun()
print(Output)
if Output > 0:
        print("The System is Unstable!")
elif Output < 0:
        print("The System is Ajusting!")
else:
        print("The System is Sostable!")
Password_tu = "mamiao"
Password_in = input("Please enter the password for programming:")
while Password_in!= Password_tu:
        print("You have enter a wrong password!\n" + "Please try again!")
        Password_in = input("")
Str1 = "Hello,"
Str2 = input("Please Enter a String what you want to Display:")
count = 0
print(Str1+Str2)
print(dir(math))
for day in B:
        print(day)
for num in A:
        print(num)
while count < 10:
        count += 1;
        print("count is equal to :", count)
print(os.times())
sys.stdout.write("Hello World!")
real = 3.001
image = 4.0003
Complex = complex(real, image)
Length_Complex = abs(Complex)
print("The Length of Complex", Complex, " is equal to :", Length_Complex)
print(time.asctime(time.localtime(time.time())))
My_sum = lambda arg1, arg2: arg1 + arg2
print("The sum of My_sum(10,20) is equal to :", My_sum(10, 20))
for i in range(10):
        for j in range(10):
                for k in range(10):
                        print("The Sequence is :", i, j, k)
File = open('test.txt', 'wb', 1000)
String_Write = "This program is written by MirsMa!"
String = String_Write.encode()
print(String)
File.write(String)
File.close()
File = open("test.txt", 'r+', 1000)
Str = File.read(1000)
print(Str)
File.close()
Path = os.getcwd()
print(Path)
os.mkdir("Document for Programming!")
os.rmdir("Document for Programming!")
class Parent_class:
        def __init__(self, X ,Y ,Z):
                self.X = X
                self.Y = Y
                self.Z = Z
                return
        def Function_Normaluse(self):
                print("This is a Normal function!")
                return
        def Function_Overwrite(self):
                Sum = self.X+self.Y+self.Z
                print(Sum)
                return Sum
        def __self_function(self):
                print("Nobody Can Callback me except Parent_Class!")
                return
class Child_class(Parent_class):
        def __init__(self):
                return
        def Function_Overwrite(self):
                print("This function has already been Overwritted by Child_class!")
                return
        def Self_function(self):
                print("This is Child's function of himself!")
                return
Parent = Parent_class(10, 20, 30)
Children = Child_class()

Parent.Function_Normaluse()
Parent.Function_Overwrite()
Children.Function_Normaluse()
Children.Function_Overwrite()
Children.Self_function()
print("我叫马淼！")
phone = "2004-959-559 # This is a phone number!"
Num1 = re.sub(r'\D', '', phone)
Num2 = re.sub(r'#.*$', '', phone)
print(Num1)
print(Num2)
print("The length of String named phone is equal to :",
      phone.__add__('OK!').__sizeof__())
del phone
def My_square(Num):
        result = Num ** 2
        return result
Square_Ori = 3
Square_Res = My_square(Square_Ori)
print("The result of function Square is equal to :", Square_Res)
def My_sqrt(Num):
        guess = Num/2
        for Grade in range(5):
                Res = Num/guess
                guess = (Res + guess)/2
                Grade += 1
        return Res
Sqrt_Ori = 10
Sqrt_Res = My_sqrt(Sqrt_Ori)
print("Sqrt_Res is equal to :", Sqrt_Res)
def length_axis(x1, y1 , x2, y2):
        Res = My_sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
        return Res
x1 = 0
y1 = 0
x2 = 3
y2 = 4
distance = length_axis(x1, y1, x2, y2)
print("The distance of the axis is equal to :", distance)
def My_pow(Num1,Num2):
        Res = 1
        Count = 0
        for Count in range(Num2):
                Res *= Num1
                print("Count number is equal to :", Count)
                Count += 1
        return Res
Pow_Ori = 2
Pow_Res = My_pow(Pow_Ori, 4)
print("The result of function Square_pow is equal to :", Pow_Res)
C = range(3)
print(C[0], C[1], C[2])
def My_exp(Times):
        __E = 2.7
        Res = 1
        for i in range(Times):
                Res *= __E
        return Res
Exp_Ori = 3
Exp_Res = My_exp(Exp_Ori)
print("The result of function exp() is euqal to :", Exp_Res)
def My_sqrt3(Num):
        guess1 = Num/3
        guess2 = Num/guess1
        for i in range(20):
                temp = Num/guess1
                Res = temp/guess2
                guess1 = (Res + guess2 + guess1)/3
                guess2 = (Res + guess2 + guess1)/3
        return Res
Sqrt3_Ori = 27
Sqrt3_Res = My_sqrt3(Sqrt_Ori)
print("The Result of function sqrt3 is equal to :", Sqrt3_Res)
def My_Ln(input):
        "Hello The function named ln for talior!"
        result = math.log(input, 2.73)
        return result
Ln_Ori = 2.73
Ln_Res = My_Ln(Ln_Ori)
print(Ln_Res)
print(dir(math))
def My_floor(Num):
        if Num - int(Num) >= 0.5:
                result = int(Num)+1
        else :
                result = int(Num)
        return result
print(My_floor(10.5))
def My_N(Num):
        result = 1
        for i in range(1, Num+1):
                result *= i
        return result
N_Ori = 5
N_Res = My_N(N_Ori)
print("The result of function N! is equal to :", N_Res)
def My_Amn(m,n):
        result = 1
        for i in range(n, m+1):
                result *= i
        return result
Amn_Orim = 3
Amn_Orin = 2
Amn_Res = My_Amn(Amn_Orim, Amn_Orin)
print("The result of function Amn is equal to :", Amn_Res)
def My_Cmn(m,n):
        Top = 1
        for i in range(n, m+1):
                Top *= i
        Bot = My_N(n)
        result = Top/Bot
        return result
Cmn_Orim = 3
Cmn_Orin = 2
Cmn_Res = My_Cmn(Cmn_Orim, Cmn_Orin)
print("The result of function Cmn is equal to :", Cmn_Res)
def Length_3D(axis1, axis2):
        result = My_sqrt(My_square(axis1[0]-axis2[0])+My_square(axis1[1]-axis2[1])+My_square(axis1[2]-axis2[2]))
        return result
L_3Dax1 = [0, 0, 0]
L_3Dax2 = [1, 1, 1]
L_3DRes = Length_3D(L_3Dax1, L_3Dax2)
print("The result of function Length_3D is equal to :", L_3DRes)
