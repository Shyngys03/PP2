h, a, b = map(int, input().split())

up = True

cnt = 0
m = 0
while True:
    if up:
        m += a
        up = False
        cnt += 0.5
        if m >= h:
            print(int(cnt) + 1)
            break
    if not up:
        m -= b
        up = True
        cnt += 0.5
        if m >= h:
            print(int(cnt))
            break