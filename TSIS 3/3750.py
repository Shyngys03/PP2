a = input().split()
b = input().split()

cnt = 0

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            cnt += 1

print(cnt)