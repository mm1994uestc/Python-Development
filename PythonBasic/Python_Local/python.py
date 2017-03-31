import math
import string
# import MySQLdb
# print ('Hello Python!')
# # for i in range(1,5):
# #   for j in range(1,5):
# #       for k in range(1,5):
# #           if( i != k ) and (i != j) and (j != k):
# #              print (i,j,k);
# # raw_input('Input you name:')
# # #raw_input cant't be reached
# a=10
# b=11
# if a>b:print(a)
# else:print(b)
# print(3*4/6, 3.1415926*4*4, math.cos(0.5), math.sin(math.pi))
# print(2**3)  # square caculate
# Num=input("Enter your input:")  # Mothed for input IO_Stream
# print(Num)
# print(11 | 5, 5 ^ 3, 5 ^ 5, 2+5 ^ 5, 4 >> 2)
# str = 'hi,python!'
# print(str.capitalize())  # call the capitalize() to show the first letter be big
# print(str.count('p'))  # call the capitalize() to count how many times the letter 'p' is this string
# print(str.find('p'))  # call the find() to find the position of letter 'p'
# s = 'So %s day!'
# print(s % 'beautifull')  # To use the string 'beautifull' to replace the %s
# print('1 %c 1 %c %d' % ('+', '=', 2), '10'+'2')
# # print(string.atoi('10')+4)
# # can not reach the class func named atoi()
# dic = {'apple': 2, 'orange': 1}  # define a dictionary
# print(dic.copy())  # copy the dictionary
# dic['banana'] = 5  # add a new item to the dictionary
# dic.pop('apple')  # delete the apple item from dictionary
# print(dic.items())  # show the member of the dictionary modified just now!
# dic.update({'banana': 3})  # update the value of banana'item;if there is no this item,then add a new item for dictionary
# print(dic.items())
# # dic.clear()#clear the dictionary

# import multiprocessing as mp
# import threading as td
#
# def job1(Q, param1, prama2):
#     print 'job1'
#     Res = param1 + prama2
#     Q.put(Res)  # queue
# def job2(Q, param1, param2):
#     print 'job2'
#     Res = param1*param2
#     Q.put(Res)
# if __name__=='__main__':
# #t1 = td.Thread(target=job1, args=(1, 2))
#     Q = mp.Queue()
#     p1 = mp.Process(target=job1, args=(Q, 10, 10))
#     p2 = mp.Process(target=job2, args=(Q, 10, 10))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     Res2 = Q.get()
#     Res1 = Q.get()
#     print 'Res1:', Res1, 'Res2:', Res2


# import multiprocessing as mp
# def job(x):
#     return x*x
# def multcore():
#     pool = mp.Pool()
#     res = pool.map(job, range(100000))
#     print res
# if __name__ == '__main__':
#     multcore()


import multiprocessing as mp
import time

def func(v, num, l):
    l.acquire()
    for i in range(10):
        time.sleep(0.1)
        v.value += num
        print(v.value)
    l.release()
def multicore():
    v = mp.Value('i', 0)
    l = mp.Lock()
    p1 = mp.Process(target=func, args=(v, 1, l))
    p2 = mp.Process(target=func, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
if __name__ == '__main__':
    multicore()
