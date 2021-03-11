from math import sqrt

def isPrime(x):
    for i in range(2, int(sqrt(x))):
        if x % i == 0:
            return False
    else:
        return True

a = int(input())

i = 2
while i <= a:
    if (a % i == 0 and isPrime(i)):
        print(i)
        break
    i += 1