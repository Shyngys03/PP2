def check_power_of_2(x):
    while x % 2 == 0:
        x //= 2
    if x == 1:
        return True
    else:
        return False

a = list(map(int, input().split()))

ans = set()

for i in range(len(a)):
    if not check_power_of_2(a[i]):
        ans.add(a[i])

print(*sorted(ans))