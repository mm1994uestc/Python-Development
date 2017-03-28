import math
class Struct:
    def __init__(self):
        self.numerator = 1
        self.denominator = 1
S = int(input())
Array = []
for i in range(S):
    Temp = input().split()
    A = int(Temp[0])
    B = int(Temp[1])
    Array.append(A)
    Array.append(B)
print(Array)
def product(fracs):
    Len = int(len(fracs)/2)
    t = Struct()
    t.numerator = 1
    t.denominator = 1
    i = 0
    for j in range(Len):
        t.numerator = t.numerator*fracs[i]
        t.denominator = t.denominator*fracs[i+1]
        i = i + 2
    Min = min(t.numerator, t.denominator)
    for d in range(1, Min + 1):
        if divmod(t.numerator, d)[1] == 0 and divmod(t.denominator, d)[1] == 0:
            C = d
    return int(t.numerator/C), int(t.denominator/C)
Res1, Res2 = product(Array)
print(Res1, Res2)
