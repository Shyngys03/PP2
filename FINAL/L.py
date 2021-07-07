n, m = map(int, input().split())

sums = []
for i in range(n):
    a = list(map(int, input().split()))
    sums.append(sum(a))

for i in range(len(sums)):
    if max(sums) == sums[i]:
        print(i + 1)
        break