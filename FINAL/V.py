a, b, k = map(int, input().split())

ans = []

for i in range(min(a, b), 0, -1):
    if (a % i == 0) and (b % i == 0):
        ans.append(i)

print(ans[k - 1])