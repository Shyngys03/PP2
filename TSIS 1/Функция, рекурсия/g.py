def power(a, n):
    cnt = 1
    if(n >= 0):
        while(n != 0):
            cnt *= a
            n -= 1
    else:
        while(n != 0):
            cnt /= a
            n += 1
    return cnt

a = float(input())
n = int(input())

print(power(a, n))