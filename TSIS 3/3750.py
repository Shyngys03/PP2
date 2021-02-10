a, b = list(map(int, input().split()))

cnt = 0

for i in range(min(len(a), len(b))):
    if a[i] == b[i]:
        cnt += 1
print(cnt)