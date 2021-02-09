a = int(input())

cnt = 0

if a < 0:
    a = abs(a)
    print((-((a + 1) * a) // 2) + 1)
else:
    print((a**2 + a) // 2)