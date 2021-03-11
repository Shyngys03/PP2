a = int(input())

cnt = 0
for i in range(1, a + 1):
    cnt += float(1 / (i * i))
print(cnt)