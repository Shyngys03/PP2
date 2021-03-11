def frac(n, m):
    for i in range(min(n, m), 2, -1):
        if((n % i == 0) and (m % i == 0)):
            print(n // i, m // i)
            break

a = int(input())
b = int(input())

frac(a, b)