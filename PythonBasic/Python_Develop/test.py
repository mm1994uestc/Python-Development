#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys;
import math;
import time;
import string;
print('Hello World!');#打印字符串
#print('爱你！');
print(4+5,4*5,4/5,pow(4,5));
#注意python的语法对文本缩进的格式要求很高，一定要保证
if True:
	print ("Answer");
	print ("True");
else:
	print ("Answer");
	print ("False");
#total = item_one + \#连接符
	item_two + \
	item_three;
print('total');
days = ['Monday','Thuesday','Wednesday','Thursday','Friday'];
print(days[0],days[1],days[2],days[3],days[4]);
x = 'runoob';
sys.stdout.write(x + '\n')
counter = 100;#整形变量
miles = 101.1;#浮点型数据
name = 'mamiao';#字符型变量
print(name,counter,miles);
a,b,c =1,2,"mamiao";#相当于多个变量同时赋值
print(a,b,c);
del a,b,c;#删除多个对象的引用
real=3.001;
image=4.002;
Num_com=complex(real,image)
Length=abs(Num_com);
print("Complex Number is ",Num_com,".The Length is equal to",Length);
str='I want to learn Python every well,but the time seem to be not enough!';
print(str[1:10]);#截取字符串当中的一部分，小标的起始是从左到右，起始0-左
print(str);#输出完整字符串
print(str[0]);#输出字符串中的第一个字符
print(str[2:5]);#输出字符串中第三个至第五个之间的字符串
print(str[2:]);#输出从第三个字符开始的字符串
print(str * 2);#输出字符串两次
print(str + "TEST");#输出连接的字符串
#加号（+）是列表连接运算符，星号（*）是重复操作
tuple = ('GPIO','FLASH','MCPU');#元组，不允许更新
list = ['A','B','C'];#列表，可以更新
A,B=10,11;
B+=1;
if (A>B) and (A==B):
	print('A is the big one');
else: 
	print('B is the big one');
print(A|B,A**B,A^B,~A,A<<2,A>>1);
#Python成员运算符,in 运算符
List = [1,2,3,4,5,10];
if (A in List) and (B in List):
	print('Oh,yeal!');#一定要注意啊，目前加入不了utf8的库，所以感叹号一定是英文的感叹号
elif (A not in List) and (B not in List):
	print('Ok,There is no one of the Number!');
else:
	print('Some number of them is in the List!');
#Python语言中没有 do while语句
M=input("Enter your input:");
print(M+'2');
#数据类型转换string--convert--int，eg:int('12')
#数据类型转换int--convert--string，eg:str('12')
count=int(M);
while (count < 10):
	print('The count number is equal to:',count);#注意缩进，缩进表示的是当前执行的代码
	count+=1;
print('Good bye!');
i = 1
while i < 10:   
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print(i)         # 输出双数2、4、6、8、10

i = 1
while 1:            # 循环条件为1必定成立
    print(i)         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break
#Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串
for letter in 'Python':
	print('The letter is: ',letter);
for day in days:
	print('Today is:',day);
#通过序列索引迭代来完成对列表等字符串遍历
for index in range(len(days)):
	print(days[index]);
#循环嵌套
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      pass
      #Python pass是空语句，是为了保持程序结构的完整性。
      #pass 不做任何事情，一般用做占位语句
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print(i," prime num")
   i = i + 1
print("Good bye!")
ticks = time.time()#获取当前时间戳
print("The current time is:", ticks)
localtime = time.localtime(time.time())
print('The locate time is:',localtime)
localtime = time.asctime( time.localtime(time.time()))
print('The locate time is:',localtime)

#python函数定义
def printme( str1,str2 ):#"打印传入的字符串到标准显示设备上"
	print(str1+str2);
	return;
printme('Hello world!','I Love Python!')
#两种求和函数：
def sum1( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print("kernel of function : ", total)
   return total;
sum2 = lambda arg1,arg2:arg1+arg2;
print('The total is:',sum1(10,20));
print('The total is:',sum2(10,20));
content = dir(math)
print(content);
#调用自己编写的外部库函数，类似于C语言的.c文件source文件，注意调用的方式
import support;
support.print_func("Zara");
#from support import fibonacci#单独引用support.py文件里面的fibonacci函数，其余函数都不调用
#from support import *#调用所有support文件里面的函数模块model

a,b=0,10;
for a in range(b):
	print(a);
	a+=1;

#import Python_Library;
#import fibonacci;
#fibonacci_func(10);#retry the function to run

#file object = open("file_name","access","Buffer"]);
#filename是文件的名称，access是object操作文件的权限，Buffer是文件是否以寄存器操作来运行#Buffer=1代表使用Buffer，当Buffer是大于1时，限制了Buffer的大小，Buffer=0表示不使用Buffer
#file对象的属性
#file.closed	返回true如果文件已被关闭，否则返回false。
#file.mode	返回被打开文件的访问模式。
#file.name	返回文件的名称。
#file.softspace	如果用print输出后，必须跟一个空格符，则返回false。否则返回true。
fo=open("test.txt","wb",1000);
print("The filename is :",fo.name);
print("The states of files :",fo.closed);
print("The Rquest_Model of files :",fo.mode);
print("Now time I will write something into the files named test.txt!");
fo.write(b'www.runoob.com!\nVery good site!\n');#传递测参数就是要写入fo文件的内容,必须要#使用b参数来限定写入的数据类型是byte类型
fo.close();
fo=open("test.txt","rb",1);
#file.read(count)函数传递的参数count是要从已打开文件中读取的字节计数。该方法从文件的开头
#开始读入，如果没有传入count，它会尝试尽可能多地读取更多的内容，很可能是直到文件的末尾。
print("Now time I will read some information from the files named test.txt!");
Str1=fo.read();
print(Str1);
fo.close();
#tell()方法告诉你文件内的当前位置；换句话说，下一次的读写会发生在文件开头这么多字节之后
#seek（offset ,[from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定#开始移动字节的参考位置,如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果#设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置
fo=open("test.txt","r+",1);
str=fo.read(10);
print(str);
position=fo.tell();
print("The position of file nowtime is equal to :",position);
position=fo.seek(0,0)
str=fo.read(10);
print(str);
fo.close();

import os;
Path=os.getcwd()#获得当前的路径
print(Path)
os.mkdir("Subdirector");#当文件夹已经存在的时候不能再次创建它
os.rmdir("Subdirector");#删除当前目录下的文件夹

class Employee:
	'Hello,This the first class named Employee!'
	empCount=0;
	def __init__(self,name,salary):
		self.name = name;
		self.salary = salary;
		Employee.empCount += 1;
	def displayCount(self):
		print("Total Employee %d"%Employee.empCount);#看这里的语法，如何输出变量
	def displayEmployee(self):
		print("Name:",self.name,",Salary:",self.salary);
emp1 = Employee("mamiao",20000);
emp2 = Employee("zhangle",30000);
emp3 = Employee("jujiabao",40000);
emp1.displayCount();
emp1.displayEmployee();
emp2.displayCount();
emp2.displayEmployee();
emp3.displayCount();
emp3.displayEmployee();
print("Total Employee %d"%Employee.empCount);#class申明的成员变量是共用的，public的
emp1.age = 7;#添加emp1的变量属性age
emp1.sex = 1;
emp1.age = 8;#修改emp1的age变量值
print(emp1.age);
del emp1.age;#删除emp1的变量属性age

#getattr(obj,'name',[default])#访问对象的属性。
#hasattr(obj,'name')#检查是否存在一个属性。
#setattr(obj,'name',value)#设置一个属性。如果属性不存在，会创建一个新属性。
#delattr(obj,'name')#删除属性。
#getattr(emp1,'sex');
if hasattr(emp1,'sex'):
	print("There is a member of emp1 named age!");
setattr(emp1,'Weight',60);
if hasattr(emp1,'Weight'):
	print("There is a member of emp1 named Weight!");
delattr(emp1,'Weight');
if hasattr(emp1,'Weight'):
	print("There is a member of emp1 named Weight!");
else:
	print("The member has already been delete by User miaoma!");
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)

class Parent:#定义父类
   parentAttr = 100
   def __init__(self):
      print("Callback the Structure-function of parent!");

   def parentMethod(self):
      print('Callback the normal parent mothed!');

   def setAttr(self, attr):#成员变量更新方法setAttr
      Parent.parentAttr = attr;

   def getAttr(self):
      print("Characte-Value of Parent:", Parent.parentAttr);

   def Function_Overwrite(self):
      print("This is Parent's Function!");

class Child(Parent): # 定义子类,子类的内部调用了参数Parent，该参数表明Child类继承了Parent类的基本方法
   def __init__(self):
      print("Callback Structure-function of Child!");

   def childMethod(self):
      print('Callback child method');

   def Function_Overwrite(self):
      print("This is Child's Function!");

c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法
c.getAttr()          # 再次调用父类的方法
c.Function_Overwrite()    #方法重写

#__private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
class JustCounter:
	__secretCount = 0  # 私有变量
	publicCount = 0    # 公开变量

	def count(self):
		self.__secretCount += 1
		self.publicCount += 1
		print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
#print(counter.__secretCount)#报错,实例不能访问私有变量

#Python正则表达式（提前学习正则表达式），需要引入头文件：import re
#re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
#函数语法：re.match(pattern, string, flags=0)
#pattern  匹配的正则表达式
#string	 要匹配的字符串
#flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
import re
print(re.match('www','www.runoob.com').span())  # 在起始位置匹配
print(re.match('com','www.runoob.com'))         # 不在起始位置匹配

line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
else:
   print("No match!!")
#re.search 扫描整个字符串并返回第一个成功的匹配
#re.search(pattern, string, flags=0)
#pattern	匹配的正则表达式
#string	要匹配的字符串。
#flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
#匹配成功re.search方法返回一个匹配的对象，否则返回None
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
if searchObj:
   print("searchObj.group() : ", searchObj.group())
   print("searchObj.group(1) : ", searchObj.group(1))
   print("searchObj.group(2) : ", searchObj.group(2))
else:
   print("Nothing found!!")

#比较match函数和search函数的区别，re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print("match --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")

matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print("search --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")

#Python 的re模块提供了re.sub用于替换字符串中的匹配项：re.sub(pattern, repl, string, max=0)
#返回的字符串是在字符串中用 RE 最左边不重复的匹配来替换。如果模式没有发现，字符将被没有改变地返回。可选参数 count 是模式匹配后替换的最大次数；count 必须是非负整数。缺省值是 0 表示替换所有的匹配
phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)#\D匹配一个非数字字符，等价于等价于[^0-9]    
print("Phone Num : ", num)


#Python连接到数据库必须学习，方便进行大数据的数据库处理

#Python2.6和Python3.0的版本的改变：
b = b'china';
print("b is :",b);
print("The type of b is:",type(b))
s = b.decode() 
print(s)
b1 = s.encode();
print("The type of b1 is:",type(b1))
print(b1)

print("The modify before put into the buffer!")


