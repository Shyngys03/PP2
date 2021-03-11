n = int(input())

cnt = 1
i = 0
while(True):
    cnt *= 2
    i += 1
    if(cnt >= n):
        print(i)
        break