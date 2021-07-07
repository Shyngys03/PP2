def Convert(x):
    s = ""
    if x == 0:
        return '0'
    elif x > 0:
        while x > 0:
            s += str(x % 7)
            x //= 7
    return s[::-1]

n = int(input())

print(Convert(n))