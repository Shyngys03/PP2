n = int(input())

d = dict()
cnt = 0

for i in range(n):
    a = input().split()
    k = int(a[1])
    cnt += k
    s = a[0]
    if s not in d:
        d[s] = k
    else:
        d[s] += k
print()
for i in d:
    d[i] /= cnt
    print(str(i) + ' ' + str(d[i] * 100) + '%')