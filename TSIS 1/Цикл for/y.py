a = int(input())

x = a

for i in range(1, a + 1):
    if i > x:
        print((str(i) + ' ') * x)
        break
    print((str(i) + ' ') * i, end = '')
    x -= i