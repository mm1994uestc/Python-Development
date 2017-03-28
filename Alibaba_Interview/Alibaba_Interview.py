# 有n个正整数（每个数小于10亿），将它们表示成字符串形式。对每一个字符串s，可以翻转为新字符串s'，如“1234”可以翻转成“4321”。
# 现在，将这n个字符串以任意顺序连成一个字符环，每个字符串可以选择是否翻转。在字符环中，从任意一个位置开始，遍历整个环，得到一
# 个长整数。请问，如何才能得到最大的长整数。
import string
Num = input()
Num_L = Num.split(' ')
N = len(Num_L)
print(N)
for i in range(N):
    Str_L = len(Num_L[i])
    if Num_L[i][0] < Num_L[i][Str_L-1]:
        New = ''
        for index in range(Str_L):
            New = New+Num_L[i][Str_L-1-index]
        Num_L[i] = New
for i in range(N):
    print('Num_L is(After Modify):', Num_L[i])
for i in range(N):
    for j in range(i, N):
        if Num_L[i][0] < Num_L[j][0]:
            Temp = Num_L[i]
            Num_L[i] = Num_L[j]
            Num_L[j] = Temp
        elif Num_L[i][0] == Num_L[j][0]:
            Len1 = len(Num_L[i])
            Len2 = len(Num_L[j])
            if Len1 < Len2:
                L = Len1
            else:
                L = Len2
            for k in range(1, L):
                if Num_L[i][k] < Num_L[j][k]:
                    Temp1 = Num_L[i]
                    Num_L[i] = Num_L[j]
                    Num_L[j] = Temp1
                    break
Res = ''
for i in range(N):
    print(Num_L[i])
    Res = Res+Num_L[i]
print(Res)
