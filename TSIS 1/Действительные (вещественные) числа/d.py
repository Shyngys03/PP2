from math import sqrt

a = float(input())
b = float(input())
c = float(input())

p = (a + b + c) / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
if (s - int(s) == 0):
    print(int(sqrt(p * (p - a) * (p - b) * (p - c))))
else:
    print(sqrt(p * (p - a) * (p - b) * (p - c)))