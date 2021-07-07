def check_power_of_2(x):
    while x % 2 == 0:
        x //= 2
    if x == 1:
        return True
    else:
        return False

a = list(map(int, input().split()))

ans = set()

for i in a:
    if check_power_of_2(i):
        ans.add(i)
print(*sorted(ans))